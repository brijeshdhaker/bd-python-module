# test_helpers.py

import pytest
from databricks.sql.client import Connection, List, Row
from datetime import datetime
from dbx_module.helpers import select_nyctaxi_trips
from unittest.mock import create_autospec


@pytest.fixture
def mock_data() -> List[Row]:
    return [
        Row(
            tpep_pickup_datetime=datetime(2016, 2, 14, 16, 52, 13),
            tpep_dropoff_datetime=datetime(2016, 2, 14, 17, 16, 4),
            trip_distance=4.94,
            fare_amount=19.0,
            pickup_zip=10282,
            dropoff_zip=10171,
        ),
        Row(
            tpep_pickup_datetime=datetime(2016, 2, 4, 18, 44, 19),
            tpep_dropoff_datetime=datetime(2016, 2, 4, 18, 46),
            trip_distance=0.28,
            fare_amount=3.5,
            pickup_zip=10110,
            dropoff_zip=10110,
        ),
    ]


def test_select_nyctaxi_trips(mock_data: List[Row]):

    # Create a mock Connection.
    mock_connection = create_autospec(Connection)

    # Set the mock Connection's cursor().fetchall() to the mock data.
    mock_connection.cursor().fetchall.return_value = mock_data

    # Call the real function with the mock Connection.
    response: List[Row] = select_nyctaxi_trips(connection=mock_connection, num_rows=2)

    # Check the value of one of the mocked data row's columns.
    assert response[1].fare_amount == 3.5

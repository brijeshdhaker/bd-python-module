### Activate Python VENV
```bash

conda activate bash
conda install jupyter -c defaults

```
### jupyter lab
```bash

$ jupyter lab --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=~/IdeaProjects/bd-notebooks-module/notebooks
```

### jupyter notebook
#
```bash

$ jupyter notebook --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=${HOME}/IdeaProjects/bd-notebooks-module/notebooks
```


### Check the newly built image
```bash
$ docker run -it --rm jupyter/all-spark-notebook:latest pyspark --version
```

```bash

git config --global user.name "Brijesh Dhaker"
git config --global user.email "brijeshdhaker@gmail.com"

git reset --soft HEAD~2 # Changes stay in staging
git reset HEAD~2        # Changes become unstaged

```






## Create Zip File
```bash

python -m zipfile -c bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip bd-pyspark-module/src/main/py/*
```

## Run Python __main__.py get executed
```bash

python bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip --Host localhost --App hello_py
````

## Run Python module
```bash

export PYSPARK_DRIVER_PYTHON=/opt/conda/envs/env_python3_11_13/bin/python
export PYSPARK_PYTHON=/opt/conda/envs/env_python3_11_13/bin/python

export PYTHONPATH=$PYTHONPATH:./bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip
# or
export PYTHONPATH=$PYTHONPATH:~/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=~/IdeaProjects/bd-pyspark-module/src/main/py

python -m com.example.app --Host localhost --App hello_py
python -m com.example.hello --Host localhost --App hello_py
```

# Check the newly built image
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python /apps/bd-pyspark-module-1.0.0.zip --Host localhost --App hello_py
```
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python -m com.example.app --Host localhost --App hello_py
```
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python -m com.example.hello --Host localhost --App hello_py
```

#
```python
import sys
sys.path.insert(0, "/apps/hostpath/python/pyspark-module-distro.zip")
sys.path[0]
import hello
hello.greet("Pythonista")
```

```python
import sys
sys.path.insert(0, "~/IdeaProjects/bd-pyspark-module/src/main/py")
```

## Spark CSV Reader

A simple Spark program to read data from a CSV file.

### Usage

1. Ensure PySpark is installed: `pip install pyspark`
2. Run the program: `python spark_csv_reader.py`

The program will:
- Read the CSV file from `data/customers_20240101070707.csv`
- Display the schema
- Show the first 10 rows
- Print total row and column counts

### Requirements

- Apache Spark
- PySpark library
- CSV file in the `data/` directory
# or
```bash

export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/kafka/confluent/confluent_kafka_AvroProducer.py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/kafka/confluent/confluent_kafka_AvroConsumer.py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/utils/FileUtils.py

```

## Import modules in pyspark
```bash

pyspark --archives bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip#
from com.example.models.Transaction import Transaction
from main import print_hi
```

## Run Python Unit Test
```bash

export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip
export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
python -m unittest ${HOME}/IdeaProjects/bd-pyspark-module/src/test/py/TestUsers.py


# AI Project : bd-crewai-module

Welcome to the bd-crewai-module project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://knowledge.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/main/py/com/example/ai/apps/crewai/config/agents.yaml` to define your agents
- Modify `src/main/py/com/example/ai/apps/crewai/config/tasks.yaml` to define your tasks
- Modify `src/main/py/com/example/ai/apps/crewai/crew.py` to add your own logic, tools and specific args
- Modify `src/main/py/com/example/ai/apps/crewai/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the bd-crewai-module, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The bd-crewai-module is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `src/main/py/com/example/ai/apps/crewai/config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `src/main/py/com/example/ai/apps/crewai/config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BdCrewaiModule Crew or crewAI.
- Visit our [documentation](https://knowledge.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

### RAG : RAG has two completely separate workflows that you need to understand:
![](./knowledge/images/rag_flow_steps.jpg)

𝗢𝗳𝗳𝗹𝗶𝗻𝗲 — the ingestion pipeline (runs once, or on schedule)
① Load your documents (PDFs, URLs, code repos, Word files)
② Split them into small, meaningful passages (chunking)
③ Convert each passage into a vector — a mathematical fingerprint — using an embedding model
④ Store all vectors in a vector database (ChromaDB, FAISS, Pinecone, etc.)

𝗢𝗻𝗹𝗶𝗻𝗲 — the query pipeline (runs every time a user asks something)
① Receive the user's question
② Embed the question using the exact same embedding model
③ Find the most relevant passages via similarity search (top-k retrieval)
④ Inject those passages into the LLM prompt as context
⑤ The LLM generates an answer grounded in YOUR data


### Desing Flow for Design Documente Creation
![](./knowledge/images/RAG_001.png)


### Gmail Server MCP Server

```
send an email notification with folloing details: 
--recipient 'brijeshdhaker@gmail.com'
--subject 'AI Notification Test - 2026-04-17#{id}'
--body 'Hello {name},\n\n This is automated AI message send using AI Tools #Message-{id}'
--params {"id":"2001", "name":"Brijesh"}
```
### SQL Server MCP Server

```
fetch results for provided complex sql query with parameters :
--template select `NAME`, `AGE`, `ADDRESS`, CONVERT(SALARY, FLOAT) AS `SALARY` from CUSTOMERS WHERE ID = {id}
--params {"id":"1"}
```
### Install Application

```
python -m pip install -e .
```

### Create Py Whl files
```
uv build
uv build --wheel
uv pip install dist/bd_crewai_module-0.1.0-py3-none-any.whl
```

###
```
pip install dist/bd_crewai_module-0.1.0-py3-none-any.whl
python -m pip install dist/bd_crewai_module-0.1.0-py3-none-any.whl
```

#### Databricks Access Token Generation
```
# Account Token
curl --request POST \
--url $DATABRICKS_ACCOUNT_TOKEN_URL \
--user "$DATABRICKS_CLIENT_ID:$DATABRICKS_CLIENT_SECRET" \
--data 'grant_type=client_credentials&scope=all-apis'
  
# Workspace Token
curl --request POST \
--url $DATABRICKS_WORKSPACE_TOKEN_URL \
--user "$DATABRICKS_CLIENT_ID:$DATABRICKS_CLIENT_SECRET" \
--data 'grant_type=client_credentials&scope=all-apis'

databricks auth describe

```


User: show tables in databricks uc 

GitHub Copilot: I'll help you show tables in Databricks Unity Catalog. Let me start by discovering what's available. 

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW CATALOGS"
}

Ran `poll_sql_result` 
Completed with input: {
  "statement_id": "01f159e0-5ccf-17f3-a3ff-94481738006f"
}

Found **4 catalogs**:
- `dbx_catalog`
- `samples`
- `system`
- `workspace`

Now let me show tables. I'll query the main catalogs:   

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW SCHEMAS IN dbx_catalog"
}

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW SCHEMAS IN samples"
}

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW SCHEMAS IN workspace"
}

**Schemas found:**

**dbx_catalog:**
- default, information_schema

**samples:**
- accuweather, bakehouse, healthverity, nyctaxi, sec, tpcds_sf1, tpcds_sf1000, tpch, wanderbricks

**workspace:**
- default, information_schema

Let me get the tables from a few schemas:   

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW TABLES IN samples.nyctaxi"
}

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW TABLES IN samples.tpch"
}

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW TABLES IN dbx_catalog.default"
}

**Tables found:**

**samples.nyctaxi:**
- `trips`

**samples.tpch:**
- customer, lineitem, nation, orders, part, partsupp, region, supplier

**dbx_catalog.default:**
- (empty)

Let me check a couple more popular schemas:     

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW TABLES IN samples.accuweather"
}

Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW TABLES IN samples.tpcds_sf1"
}

## Databricks Unity Catalog - Tables Overview

**samples.accuweather** (12 tables):
- forecast_daily_calendar_imperial, forecast_daily_calendar_metric
- forecast_daynight_imperial, forecast_daynight_metric
- forecast_hourly_imperial, forecast_hourly_metric
- historical_daily_calendar_imperial, historical_daily_calendar_metric
- historical_daynight_imperial, historical_daynight_metric
- historical_hourly_imperial, historical_hourly_metric

**samples.tpcds_sf1** (24 tables):
- call_center, catalog_page, catalog_returns, catalog_sales
- customer, customer_address, customer_demographics
- date_dim, household_demographics, income_band
- inventory, item, promotion, reason, ship_mode
- store, store_returns, store_sales
- time_dim, warehouse, web_page, web_returns, web_sales, web_site

To list tables from any other schema, use:
```sql
SHOW TABLES IN catalog_name.schema_name
```

Or describe a specific table:
```sql
DESCRIBE TABLE catalog_name.schema_name.table_name
```

User: DESCRIBE TABLE samples.nyctaxi.trips

GitHub Copilot: Ran `execute_sql_read_only` 
Completed with input: {
  "query": "DESCRIBE TABLE samples.nyctaxi.trips"
}

**samples.nyctaxi.trips** - Table Schema

| Column | Data Type | Comment |
|--------|-----------|---------|
| tpep_pickup_datetime | timestamp | |
| tpep_dropoff_datetime | timestamp | |
| trip_distance | double | |
| fare_amount | double | |
| pickup_zip | int | |
| dropoff_zip | int | |

This NYC taxi trips table contains 6 columns tracking pickup/dropoff times, distance, fare amount, and zip codes.

User: show schemas in catalog 'dbx_catalog'

GitHub Copilot: Ran `execute_sql_read_only` 
Completed with input: {
  "query": "SHOW SCHEMAS IN dbx_catalog"
}

**Schemas in dbx_catalog:**
- `default`
- `information_schema`

```bash

git config --global user.name "Brijesh Dhaker"
git config --global user.email "brijeshdhaker@gmail.com"

git reset --soft HEAD~2 # Changes stay in staging
git reset HEAD~2        # Changes become unstaged

```

```bash
home = /home/brijeshdhaker/snap/code/247/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/bin
include-system-site-packages = false
version = 3.12.13
executable = /home/brijeshdhaker/snap/code/247/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/bin/python3.12
command = /home/brijeshdhaker/snap/code/247/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/bin/python -m venv /home/brijeshdhaker/IdeaProjects/bd-python-module/.venv


uv pip install databricks-connect==16.4.1
uv pip install databricks-connect==17.3.* --python /home/brijeshdhaker/IdeaProjects/bd-python-module/.venv/bin/python

uv build --all

uv build --package core_module
uv build --package api_module
uv build --package app_module
uv build --package dbx_module
uv build --package dqx_module

uv build --all --no-sources

python -m ensurepip --upgrade
```

https://docs.databricks.com/aws/en/dev-tools/sqltools-driver

# bd-databricks-module

The 'bd-databricks-module' project was generated by using the default-python template.

* `src/`: Python source code for this project.
  * `src/bd-databricks-module/`: Shared Python code that can be used by jobs and pipelines.
* `resources/`:  Resource configurations (jobs, pipelines, etc.)
* `tests/`: Unit tests for the shared Python code.
* `fixtures/`: Fixtures for data sets (primarily used for testing).


## Getting started

Choose how you want to work on this project:

(a) Directly in your Databricks workspace, see
    https://docs.databricks.com/dev-tools/bundles/workspace.

(b) Locally with an IDE like Cursor or VS Code, see
    https://docs.databricks.com/dev-tools/vscode-ext.html.

(c) With command line tools, see https://docs.databricks.com/dev-tools/cli/databricks-cli.html

If you're developing with an IDE, dependencies for this project should be installed using uv:

*  Make sure you have the UV package manager installed.
   It's an alternative to tools like pip: https://docs.astral.sh/uv/getting-started/installation/.
*  Run `uv sync --dev` to install the project's dependencies.


# Using this project using the CLI

The Databricks workspace and IDE extensions provide a graphical interface for working
with this project. It's also possible to interact with it directly using the CLI:

1. Authenticate to your Databricks workspace, if you have not done so already:
    ```
    $ databricks configure
    ```

2. To deploy a development copy of this project, type:
    ```
    $ databricks bundle deploy --target dev
    ```
    (Note that "dev" is the default target, so the `--target` parameter
    is optional here.)

    This deploys everything that's defined for this project.
    For example, the default template would deploy a pipeline called
    `[dev yourname] bd-databricks-module_etl` to your workspace.
    You can find that resource by opening your workpace and clicking on **Jobs & Pipelines**.

3. Similarly, to deploy a production copy, type:
   ```
   $ databricks bundle deploy --target prod
   ```
   Note the default template has a includes a job that runs the pipeline every day
   (defined in resources/sample_job.job.yml). The schedule
   is paused when deploying in development mode (see
   https://docs.databricks.com/dev-tools/bundles/deployment-modes.html).

4. To run a job or pipeline, use the "run" command:
   ```
   $ databricks bundle run
   ```

5. Finally, to run tests locally, use `pytest`:
   ```
   $ uv run pytest
   ```

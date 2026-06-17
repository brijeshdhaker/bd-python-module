#
python -m ensurepip --upgrade

# serverless
uv venv --python 3.12.3

#
pip install -e .

# To include development and testing tools specified under your optional blocks, run:
pip install -e .[dev]

uv pip install --python 3.11.15 \
    -e "./databricks-tools-core" \
    -e "./databricks-builder-app" \
    -e "./databricks-mcp-server" \
    -e "./databricks-dqx-app" -q

pip download -d dist cowsay==6.1

# Install using uv pacakage manager
```
uv init 

#
uv sync 
uv sync --active
uv sync --active --dev

#
uv build --all
uv build --package app-module
uv build --all --no-sources

uv build --wheel

uv build --wheel \
    -e "./databricks-tools-core" \
    -e "./databricks-builder-app" \
    -e "./databricks-mcp-server" \
    -e "./databricks-dqx-app"

uv run
uv run --package albatross
uv run --package bird-feeder

dist/databricks_tools_core-0.1.0-py3-none-any.whl

#
uv pip install dist/core_module-0.1.0-py3-none-any.whl
uv pip install dist/api_module-0.1.0-py3-none-any.whl
uv pip install dist/app_module-0.1.0-py3-none-any.whl
uv pip install dist/dbx_module-0.1.0-py3-none-any.whl
uv pip install dist/dqx_module-0.1.0-py3-none-any.whl
uv pip install dist/bd_python_module-0.1.0-py3-none-any.whl

uv tool install dist/bd_notebooks_module-1.0.0-py3-none-any.whl

uv run -m zipfile -c dist/bd_notebooks_module-1.0.0.zip src/main/py/*

uv pip freeze > requirments.txt
```

# Install Using Pip
python -m pip install --upgrade build
python -m build
pip install --force-install dist/bd_notebooks_module-1.0.0-py3-none-any.whl

# Run Module
python -m module_name.main
python -m com.example.hello
python -m com.example.app

python -m com.example.ai.apps.crewai.main

#
## Run Python __main__.py get executed
```bash

python dist/bd_notebooks_module-1.0.0.zip --Host localhost --App hello_py
````

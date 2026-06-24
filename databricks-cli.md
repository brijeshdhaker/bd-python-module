# Install Databricks Cli
```bash 
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh

# Check Installation
command -v databricks

# Add Path
# /usr/local/bin/databricks
PATH=${PATH}:/home/brijeshdhaker/.vscode/extensions/databricks.databricks-2.11.1-linux-x64/bin

# Check Version
databricks -v
Databricks CLI v1.2.0

```

# Method 1: Interactive CLI Configuration (Recommended)
``` bash

databricks configure --profile databricks-cli

```
# Check the active authentication configuration
``` bash

databricks auth env --profile databricks-cli

```
# Alternatively, test access by listing workspace roots
``` bash

databricks fs cat dbfs:/Workspace/Users/brijeshdhaker@gmail.com/
databricks fs cp

databricks fs ls dbfs:/Workspace/Users/brijeshdhaker@gmail.com/
databricks fs ls dbfs:/Volumes/workspace/default/dbx_volume/
databricks fs ls dbfs:/databricks-datasets

databricks fs mkdir

databricks fs rm

```
# Login to Workspace
``` bash

databricks auth login --profile databricks-cli

databricks auth login --host ${DATABRICKS_HOST} --profile databricks-cli

databricks auth login --host ${DATABRICKS_HOST} --account-id eee8ca65-56a2-4cd5-aae4-8edc4a19e595 --profile databricks-cli

databricks auth login --configure-serverless --host ${DATABRICKS_HOST} --profile databricks-cli

databricks auth describe --profile databricks-cli

databricks auth token --profile databricks-cli

databricks current-user me --profile databricks-cli

databricks service-principals list -p databricks-cli
```

#
```bash

databricks functions list data_quality default --output json

databricks catalogs delete --name dqx --force
```
#
### Workspace
#
``` bash
#
databricks workspace list /Workspace/Users/brijeshdhaker@gmail.com/apps --profile databricks-cli

# Download the app files to your computer:
databricks workspace export-dir /Workspace/Users/brijeshdhaker@gmail.com/apps/bd_dqx_module . --profile databricks-cli

# Sync your changes:
databricks sync --watch . /Workspace/Users/brijeshdhaker@gmail.com/apps/bd_dqx_module --profile databricks-cli

```

#
### Databricks Bundle Deploymnet
#
``` bash

#### Validate your syntax: Ensure there are no structural errors in your YAML configuration.
databricks bundle validate

#### Deploy/Update Lakebase only
databricks bundle deploy --target dev --profile databricks-cli
databricks bundle deploy -t dev -p databricks-cli 

#### Destroy Lakebase (does NOT affect the app)
databricks bundle destroy --auto-approve --profile databricks-cli

#### Trigger Remote Job
databricks bundle run --target dev job_pipeline_dqx_qc

```

### Databricks Apps Deploymnet:
```bash
#
databricks apps deploy bd_dqx_module --source-code-path /Workspace/Users/brijeshdhaker@gmail.com/apps/bd_dqx_module --profile databricks-cli

# Show Details
databricks apps list --profile databricks-cli --output json

# Show status
databricks apps get dqx-studio --profile databricks-cli --output json

# Show logs
databricks apps logs dqx-studio -p databricks-cli

# Stop App
databricks apps stop dqx-studio -p databricks-cli   # stop

# Delete the app
databricks apps delete dqx-studio --profile databricks-cli

```

# DQX Installation
```bash

DQX_FORCE_INSTALL=global databricks labs install dqx --profile databricks-cli

DQX_FORCE_INSTALL=global databricks labs install dqx@v0.12.0 --profile databricks-cli

# Using PYPI package
%pip install databricks-labs-dqx==0.12.0

# Using wheel file, DQX installed for the current user:
%pip install /Workspace/Users/brijeshdhaker@gmail.com/Wheels/dqx/databricks_labs_dqx-*.whl

# Using wheel file, DQX installed globally:
%pip install /Applications/dqx/wheels/databricks_labs_dqx-0.12.0-py3-none-any.whl

# in a separate cell run:
dbutils.library.restartPython()
```

# bundle configuration
```yaml
resources:
  jobs:
    my_job:
      # ...
      tasks:
        - task_key: my_task
          # ...
          libraries:
            # install from wheel file
            - whl: /Applications/dqx/wheels/databricks_labs_dqx-0.12.0-py3-none-any.whl
            # or install from pypi
            #- pypi:
            #    package: databricks-labs-dqx==0.12.0

```

```bash
-- /Applications/dqx/config.yml

# Upgrade DQX in the Databricks workspace
databricks labs upgrade dqx --profile databricks-cli

# databricks labs upgrade dqx
databricks labs uninstall dqx --profile databricks-cli

# Usages
databricks labs dqx open-remote-config --profile databricks-cli

databricks labs dqx open-remote-config --profile databricks-cli

databricks labs dqx workflows --profile databricks-cli

databricks labs dqx open-dashboards --profile databricks-cli

```
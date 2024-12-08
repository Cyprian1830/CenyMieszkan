CONDA_ENV_NAME=python-starter

ifeq ($(OS),Windows_NT)
	CONDA_ACTIVATE=CALL "C:\Users\cypri\miniforge3\Library\bin\conda.bat" activate $(CONDA_ENV_NAME)
	CONDA_ACTIVATE_BASE=CALL "C:\Users\cypri\miniforge3\Library\bin\conda.bat" activate base
else
	CONDA_ACTIVATE=source $(shell conda info --base)/etc/profile.d/conda.sh && conda activate $(CONDA_ENV_NAME)
	CONDA_ACTIVATE_BASE=source $(shell conda info --base)/etc/profile.d/conda.sh && conda activate base
endif

.PHONY: lock-file  ## Creates conda-lock file
lock-file:
	$(CONDA_ACTIVATE_BASE) && conda-lock --mamba -f env.yml -f env-dev.yml --lockfile conda-lock-dev.yml
	git add conda-lock-dev.yml

.PHONY: release-lock-file  ## Creates conda-lock file without dev dependencies - to be used for deployment
release-lock-file:
	$(CONDA_ACTIVATE_BASE) && conda-lock --mamba -f env.yml --lockfile conda-lock.yml
	git add conda-lock.yml

.PHONY: conda-lock-install  ## Creates env from conda-lock file
conda-lock-install:
	$(CONDA_ACTIVATE_BASE) && conda-lock install --mamba -n $(CONDA_ENV_NAME) conda-lock-dev.yml

.PHONY: setup-pre-commit  ## Installs pre-commit hooks
setup-pre-commit:
	$(CONDA_ACTIVATE) && pre-commit install

.PHONY: setup-editable  ## Installs the project in an editable mode
setup-editable:
	$(CONDA_ACTIVATE) && pip install -e .

.PHONY: remove-env  ## Removes current conda environment
remove-env:
	$(CONDA_ACTIVATE_BASE) && conda env remove -n $(CONDA_ENV_NAME)

.PHONY: env  ## Combines conda-lock-install, setup-pre-commit, and setup-editable
env:
	make conda-lock-install
	make setup-pre-commit
	make setup-editable

.PHONY: recreate-env  ## Recreates conda environment by removing, generating lock files, and setting up environment
recreate-env:
	make remove-env
	make lock-file
	make env

# Helpers - this will be needed for the next topics during this class

.PHONY: format  ## Runs code formatting (ruff)
format:
	$(CONDA_ACTIVATE) && ruff check --fix --preview .
	$(CONDA_ACTIVATE) && ruff format --preview .

.PHONY: type-check  ## Runs type checking with mypy
type-check:
	$(CONDA_ACTIVATE) && pre-commit run --all-files mypy

.PHONY: test  ## Runs pytest
test:
	$(CONDA_ACTIVATE) && pytest -v tests/

.PHONY: testcov  ## Runs tests and generates coverage reports
testcov:
	$(CONDA_ACTIVATE) && pytest -v --cov-report html --cov-report xml --cov=$(CONDA_ENV_NAME) tests/

.PHONY: mpc  ## Runs manual pre-commit stuff
mpc: format type-check test

.PHONY: pc  ## Runs pre-commit hooks
pc:
	$(CONDA_ACTIVATE) && pre-commit run --all-files

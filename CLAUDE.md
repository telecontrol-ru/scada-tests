# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python/pytest integration test suite for the Telecontrol SCADA server. Tests exercise the server through `scadapy`, a 32-bit CPython C extension (`.pyd`) that wraps the SCADA client API. A running SCADA server is required.

## Running Tests

```batch
test.bat                     # Run all tests
test.bat -k DataItems        # Run tests matching pattern
test.bat -k "not Iec61850"   # Exclude tests matching pattern
```

`test.bat` sources `parameters.bat` (sets `PYTHONPATH`) then invokes `pytest`. Edit `parameters.bat` to point at your local scadapy installation.

Alternatively, set `PYTHONPATH` manually and run pytest directly:

```batch
set PYTHONPATH=C:\Program Files (x86)\Telecontrol SCADA\python;modules
pytest -k DataItems
```

pytest is configured in `pytest.ini` with a 10-second timeout per test and log output to `logs/test.log`.

## Prerequisites

- Python 3.12+ (32-bit) with `pytest` and `pyyaml` (`pip install -r requirements.txt`)
- `scadapy` module available via `PYTHONPATH` (installed with SCADA or built locally)
- Running SCADA server on `localhost` (configurable in `settings.yml`)

## Configuration

Server connection settings are in `settings.yml`:

```yaml
server: localhost
user_name: root
password: ""
```

DLL loading is handled automatically by `conftest.py`, which adds the SCADA installation directory to the DLL search path on Windows.

## Architecture

### Test Framework

- **`modules/scada_test.py`** (`BaseTest`) — Base test class. `setUp` reads `settings.yml`, connects a `scadapy.Client` to the server, and creates a `Stack`. `tearDown` deletes all nodes created by the stack and disconnects.
- **`modules/scada_stack.py`** (`Stack`) — Creates OPC UA nodes from YAML templates via the scadapy client API. Each node definition specifies `TypeDefinitionId`, `ParentId`, `BrowseName`, `DisplayName`, and `Properties`. Nodes are tracked by name and deleted on teardown.

### Test Pattern

Each test file follows the same pattern:
1. Subclass `BaseTest`
2. In `setUp`, call `self.stack.add_from_file("test_<name>_stack.yml")` to create the test node hierarchy
3. Test methods interact with nodes via `self.client` (raw scadapy API) and `self.stack.node("<name>")` (lookup by template name)

### Stack YAML Format

```yaml
NodeName:
  TypeDefinitionId: SomeType      # Required: scadapy.NodeId enum member
  ParentId: DataItems             # Required: scadapy.NodeId enum member
  BrowseName: "Name"              # Optional
  DisplayName: "Display Name"     # Optional
  Properties:                     # Optional: set after node creation
    Host: localhost
    Port: 12345
```

### Test Files

| Test | Stack file | What it tests |
|------|-----------|---------------|
| `test_ping.py` | (none) | Basic connectivity, node browsing, type definitions |
| `test_data_items.py` | `test_data_items_stack.yml` | Data item creation, property categories |
| `test_modbus.py` | `test_modbus_stack.yml` | Modbus device protocol |
| `test_iec61850.py` | `test_iec61850_stack.yml` | IEC 61850 client/server device connectivity |

## CI

GitHub Actions workflow (`.github/workflows/pythonapp.yml`):
- Triggers on push
- Installs SCADA from MSI release (`alexsmn/scada-client`)
- Sets up Python 3.12 (x86)
- Lints with flake8
- Runs pytest with JUnit XML output
- Publishes test results via `dorny/test-reporter`

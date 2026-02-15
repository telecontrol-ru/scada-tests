# SCADA Integration Tests

Python/pytest integration test suite for the Telecontrol SCADA server. Tests exercise the server through `scadapy`, a 32-bit CPython C extension that wraps the SCADA client API.

## Prerequisites

- Python 3.12+ (32-bit)
- `scadapy` module (installed with SCADA or built locally)
- Running SCADA server on `localhost`

Install Python dependencies:

```batch
pip install -r requirements.txt
```

## Running Tests

```batch
test.bat                     # Run all tests
test.bat -k DataItems        # Run tests matching pattern
test.bat -k "not Iec61850"   # Exclude tests matching pattern
```

`test.bat` sources `parameters.bat` to set `PYTHONPATH`, then invokes `pytest`. Edit `parameters.bat` to point at your scadapy installation.

To run pytest directly:

```batch
set PYTHONPATH=C:\Program Files (x86)\Telecontrol SCADA\python;modules
pytest -k DataItems
```

## Configuration

Server connection is configured in `settings.yml`:

```yaml
server: localhost
user_name: root
password: ""
```

## Test Structure

| Test | Stack file | What it tests |
| ---- | ---------- | ------------- |
| `test_ping.py` | (none) | Basic connectivity, node browsing, type definitions |
| `test_data_items.py` | `test_data_items_stack.yml` | Data item creation, property categories |
| `test_modbus.py` | `test_modbus_stack.yml` | Modbus device protocol |
| `test_iec61850.py` | `test_iec61850_stack.yml` | IEC 61850 client/server device connectivity |

Each test subclasses `BaseTest` (`modules/scada_test.py`), which handles connecting to the server and creating a node `Stack` from YAML templates. Nodes created during the test are automatically deleted on teardown.

## CI

GitHub Actions workflow (`.github/workflows/pythonapp.yml`) installs SCADA from an MSI release, sets up Python, lints with flake8, and runs pytest with JUnit reporting.

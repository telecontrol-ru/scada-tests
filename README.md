# SCADA Python Tests

## Python dependencies

Must be installed for all users from Administrator account:

- `pytest`
- `pyyaml`

## SCADA dependencies

`scadapy` must be installed. `scadapy.cp38-win32.pyd` and required DLLs must be copied under `modules` directory (no subdirectories).

## Run a specific test

```batch
test -k DataItems
```

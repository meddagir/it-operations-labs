# My Lab Run Notes

## Environment
- Device: MacBook Pro
- Operating system: macOS
- Python version: 3.9.6
- Run date: November 3, 2026

## Commands I ran
```bash
python3 run_all.py
python3 -m unittest discover -s tests -v
```

## Endpoint readiness
The before scenario correctly failed the readiness checks.
The after scenario passed.
These checks used sample endpoint data, not a real Windows computer.

## Network troubleshooting
The local service was initially unreachable.
After the lab started the listener, the connection succeeded
and the HTTP check returned status 200.

## Backup recovery
The lab detected a corrupted file and a missing file.
The restored files matched the original SHA-256 hashes.

## Test results
All five automated tests passed on my MacBook.
The Windows PowerShell collector has not been tested.

## My observations
The endpoint “before” result showed PASS even though readiness was false. This means the test correctly detected the expected failure. The network and backup labs then verified successful connection and file recovery.

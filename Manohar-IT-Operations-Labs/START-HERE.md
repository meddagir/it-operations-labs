# Start here

1. Extract the ZIP. Keep the entire Manohar-IT-Operations-Labs folder together.
2. Start on your MacBook or a personal Windows computer. An iPhone can view the files but cannot run these Python/PowerShell labs natively using the Files app.
3. Install Python 3.10+ from https://www.python.org/downloads/ if needed. Confirm with `python3 --version` on Mac or `py --version` on Windows.
4. Open Terminal/PowerShell and change directory to the extracted folder. On Mac, type `cd ` and drag the folder into Terminal, then press Enter.
5. Run `python3 run_all.py` (Windows: `py run_all.py`). Four PASS lines are expected; the first represents a correctly detected failure.
6. Run `python3 -m unittest discover -s tests -v` (Windows: `py -m unittest discover -s tests -v`). Five tests should pass.
7. Double-click `evidence.html`. It shows the results of your latest run.
8. Follow each project's README to understand the individual steps. The root runner is a convenience, not a replacement for reading the code.
9. Take your own screenshots. Mac: Shift-Command-4. Windows: Win-Shift-S. Capture the report and your terminal command. Save to each project's screenshots folder.
10. Fill MY-LAB-NOTES.md with your actual run date, results, and lessons. Then follow UPLOAD-TO-GITHUB.md.

## What the included evidence images prove
The four images were rendered from actual JSON output after running the scripts in the preparation environment. Browser capture was unavailable; they are not desktop screenshots. Endpoint evidence uses declared synthetic inputs. Network and backup evidence comes from real local operations. No employer screenshots or made-up cloud consoles are included. Capture your own desktop screenshots using step 9.

## Troubleshooting
- Command not found: install Python, reopen the terminal, and check its version.
- File not found: check that the terminal is inside the extracted repository folder.
- Endpoint returns 1: expected for the before fixture; inspect the failing checks.
- PowerShell collector fails: it requires Windows and access to local CIM/service information. It was not tested in this environment; save the error and investigate locally.
- Local socket denied: run on a personal machine that permits a loopback listener. Do not change employer security controls.

## Publication review
Only synthetic lab data is included. If you add your own evidence, remove personal usernames, employer device names, IP addresses, account IDs, tokens, patient data, and ticket screenshots. Publish only material you can explain and are allowed to share.

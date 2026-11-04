"""Execute every lab and write auditable evidence plus a static results report."""
from pathlib import Path
import subprocess, sys, json, html, datetime, platform
ROOT=Path(__file__).resolve().parent
jobs=[
    ("01-endpoint-readiness","before",["check.py","fixtures/before.json"],1),
    ("01-endpoint-readiness","after",["check.py","fixtures/after.json"],0),
    ("02-network-incident","run",["lab.py"],0),
    ("03-backup-recovery","run",["lab.py"],0)]
blocks=[]
for folder,label,args,expected in jobs:
    p=subprocess.run([sys.executable,*args],cwd=ROOT/folder,text=True,capture_output=True)
    if p.returncode!=expected: raise RuntimeError(p.stdout+p.stderr)
    payload=json.loads(p.stdout)
    evidence=ROOT/folder/"evidence";evidence.mkdir(exist_ok=True)
    record={"command":"python "+ " ".join(args),"exit_code":p.returncode,
            "expected_exit_code":expected,"result":payload}
    (evidence/(label+".json")).write_text(json.dumps(record,indent=2))
    blocks.append((folder,label,record))
    print(folder,label,"PASS (expected exit",str(expected)+")")
generated=datetime.datetime.now(datetime.timezone.utc).isoformat()
style="body{font:17px system-ui;background:#f3f6fa;color:#15283b;margin:40px auto;max-width:1000px;padding:0 25px}h1{font-size:36px}article{background:white;border:1px solid #ccd8e3;border-radius:12px;padding:24px;margin:24px 0}pre{font:15px monospace;white-space:pre-wrap;overflow-wrap:anywhere;background:#edf3f8;padding:20px}small{color:#44576a}"
page=f'<!doctype html><meta charset="utf-8"><title>IT Operations Lab Evidence</title><style>{style}</style><h1>IT Operations Lab Evidence</h1><p>Manohar Eddagiri | Portfolio lab bundle</p><p>Actual script output. Endpoint inputs are synthetic fixtures. Network and recovery operations ran locally.</p><small>Generated {generated} | Python {platform.python_version()} | {platform.system()}</small>'
for folder,label,record in blocks:
    page+=f'<article id="{folder}-{label}"><h2>{html.escape(folder)} / {label}</h2><p>PASS: observed exit code matches expected outcome.</p><pre>{html.escape(json.dumps(record,indent=2))}</pre></article>'
(ROOT/"evidence.html").write_text(page)
(ROOT/"RUN-METADATA.json").write_text(json.dumps({"generated_utc":generated,"python":platform.python_version(),"platform":platform.system(),"windows_collector":"Not executed; Windows unavailable"},indent=2))
print("Open evidence.html to review all results.")

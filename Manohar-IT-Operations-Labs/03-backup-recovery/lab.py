"""Restore only disposable files created by this program in a temporary directory."""
import hashlib, json, shutil, tempfile
from pathlib import Path
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
    with tempfile.TemporaryDirectory(prefix="manohar-backup-lab-") as tmp:
        root=Path(tmp);source=root/"source";source.mkdir()
        (source/"app.conf").write_text("service=lab\nport=8080\n")
        (source/"assets.csv").write_text("asset,status\nLAB-01,ready\n")
        expected={p.name:digest(p) for p in source.iterdir()}
        backup=root/"backup";shutil.copytree(source,backup)
        backup_ok=all(digest(backup/n)==v for n,v in expected.items())
        (source/"app.conf").write_text("BROKEN CONFIG")
        corruption_detected=digest(source/"app.conf")!=expected["app.conf"]
        (source/"assets.csv").unlink()
        missing_detected=not (source/"assets.csv").exists()
        # Restore to a new path, preserving damaged evidence for inspection.
        restored=root/"restored";shutil.copytree(backup,restored)
        actual={p.name:digest(p) for p in restored.iterdir()}
        result={"scope":"Actual temporary file copy and restore","files":len(expected),
            "backup_hashes_match":backup_ok,"corruption_detected":corruption_detected,
            "missing_file_detected":missing_detected,"restore_hashes_match":actual==expected,
            "sha256":actual,"cleanup":"Temporary files removed on exit"}
        assert backup_ok and corruption_detected and missing_detected and actual==expected
    return result
if __name__=="__main__": print(json.dumps(run(),indent=2))

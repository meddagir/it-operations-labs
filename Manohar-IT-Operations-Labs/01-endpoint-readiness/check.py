"""Read-only readiness evaluation; no endpoint configuration changes."""
import json, sys
from pathlib import Path
def evaluate(d):
    checks = {
        "free_disk_gb": (isinstance(d.get("free_disk_gb"), (int,float)) and d["free_disk_gb"] >= 20),
        "spooler": d.get("spooler") == "Running",
        "domain_joined": d.get("domain_joined") is True,
    }
    return {"asset":d.get("asset","UNKNOWN"),"checks":checks,
            "ready":all(checks.values()),"scope":"Three technical checks only; manual acceptance still required"}
if __name__ == "__main__":
    try:
        data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
        result=evaluate(data)
        print(json.dumps(result,indent=2))
        sys.exit(0 if result["ready"] else 1)
    except (OSError,ValueError,IndexError,AttributeError) as e:
        print("Input error: "+str(e),file=sys.stderr);sys.exit(2)

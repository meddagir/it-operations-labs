# Lab incident record

Status: prepared demonstration; repeat run by portfolio owner pending.

**Scenario:** Service connectivity incident.

**Scope:** Disposable local lab or synthetic input, no production impact.

**Investigation and outcome:** A local service had no active listener. Starting that listener restored TCP and HTTP access. No firewall or network configuration was changed.

**Validation:** See the raw JSON in evidence and the project README.

**Limits:** Loopback bypasses VPC routing and security groups. This is not evidence of an AWS deployment, RDS database connection, DNS repair, or remote network diagnosis.

**My repeat-run date:** Not recorded yet.

**My observations / unexpected result:** Add after running.

**Next check:** Repeat with one changed input and explain the difference.

# Lab incident record

Status: prepared demonstration; repeat run by portfolio owner pending.

**Scenario:** Backup integrity and recovery.

**Scope:** Disposable local lab or synthetic input, no production impact.

**Investigation and outcome:** The original lab configuration was corrupted and a second file was missing. Restoring into a separate directory recovered both files with matching SHA-256 hashes.

**Validation:** See the raw JSON in evidence and the project README.

**Limits:** A same-disk copy is not production backup protection. This lab does not validate ACLs, application consistency, offsite storage, encryption, retention, or disaster recovery RPO/RTO.

**My repeat-run date:** Not recorded yet.

**My observations / unexpected result:** Add after running.

**Next check:** Repeat with one changed input and explain the difference.

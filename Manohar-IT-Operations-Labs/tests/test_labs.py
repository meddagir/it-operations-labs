import unittest, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
class LabTests(unittest.TestCase):
    def test_missing_fields_fail_closed(self):
        m=load("endpoint","01-endpoint-readiness/check.py")
        self.assertFalse(m.evaluate({})["ready"])
    def test_disk_boundary(self):
        m=load("endpoint","01-endpoint-readiness/check.py")
        d=dict(free_disk_gb=20,spooler="Running",domain_joined=True)
        self.assertTrue(m.evaluate(d)["ready"])
        d["free_disk_gb"]=19.9
        self.assertFalse(m.evaluate(d)["ready"])
    def test_standalone_is_not_domain_ready(self):
        m=load("endpoint","01-endpoint-readiness/check.py")
        self.assertFalse(m.evaluate(dict(free_disk_gb=40,spooler="Running",domain_joined=False))["ready"])
    def test_service_recovery(self):
        m=load("network","02-network-incident/lab.py")
        self.assertEqual(m.run()["http_status"],200)
    def test_restore_integrity(self):
        m=load("backup","03-backup-recovery/lab.py")
        self.assertTrue(m.run()["restore_hashes_match"])
if __name__=="__main__": unittest.main()

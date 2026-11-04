"""A real loopback TCP service: observe refusal, recovery, and HTTP response."""
import socket, threading, json
from http.server import HTTPServer, BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"LAB service healthy")
    def log_message(self,*args): pass
def probe(host,port):
    try:
        with socket.create_connection((host,port),timeout=2): return "CONNECTED"
    except OSError: return "UNREACHABLE"
def run():
    # Bound but not listening: keeps the chosen port reserved during the before check.
    server=HTTPServer(("127.0.0.1",0),Handler,bind_and_activate=False)
    server.server_bind()
    port=server.server_address[1]
    before=probe("127.0.0.1",port)
    server.server_activate()
    worker=threading.Thread(target=server.serve_forever,daemon=True);worker.start()
    try:
        after=probe("127.0.0.1",port)
        import urllib.request
        opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(f"http://127.0.0.1:{port}",timeout=3) as response:
            status=response.status;body=response.read().decode()
    finally:
        server.shutdown();server.server_close();worker.join()
    result={"scope":"Actual local service; no AWS resources used","host":"127.0.0.1",
            "port":port,"before":before,"after":after,"http_status":status,"body":body}
    assert before=="UNREACHABLE" and after=="CONNECTED" and status==200,result
    return result
if __name__=="__main__": print(json.dumps(run(),indent=2))

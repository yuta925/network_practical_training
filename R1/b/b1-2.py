from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage
from urllib.parse import parse_qs, urlparse
from datetime import datetime

with open("b1-2.html", mode="r", encoding="utf-8") as file:
    template = file.read()

class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(title="イベント期限を調べる", message="")
        self.wfile.write(html.encode("utf-8"))
        return

    def do_POST(self):
        form = FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})

        try:
            name = form["event_name"].value
            date_str = form["event_date"].value
            date = datetime.strptime(date_str, "%Y-%m-%d")
            dt = datetime.now()
            period = date - dt
            message = "{}[{}]まであと{}日です．".format(name, date_str, period.days+1)
        except (ValueError, TypeError, IndexError):
            self.send_error(400, "Invalid id")
            return

        self.send_response(200)
        self.end_headers()
        html = template.format(title = "イベント期限を調べる", name=name, message=message)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
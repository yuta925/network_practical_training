from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import FieldStorage
from urllib.parse import parse_qs, urlparse

with open("b1-4in.html", mode="r", encoding="utf-8") as file:
    input = file.read()

with open("b1-4out.html", mode="r", encoding="utf-8") as file:
    output = file.read()

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = input.format(title="イベント検索")
        self.wfile.write(html.encode("utf-8"))
        return

    def do_POST(self):
        form = FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})

        id = form["id"].value

        try:
            id = int(id)
            name = events[id - 1].get("name")
            location = events[id - 1].get("location")
            if (id == 3): 
                date = '<font color="red">{}</font>'.format( events[id - 1].get("date"))
            else: 
                date = events[id - 1].get("date") 
        except (ValueError, TypeError, IndexError):
            self.send_error(400, "Invalid id")
            return

        self.send_response(200)
        self.end_headers()
        html = output.format(name=name, location=location, date=date)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
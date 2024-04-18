from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

with open("b1-1.html", mode="r", encoding="utf-8") as file:
    template = file.read()

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        query = parse_qs(_url.query)

        try:
            id = int(query["id"][0])
            name = events[id - 1].get("name")
            location = events[id - 1].get("location")
            if (id == 3):
                date = '<font color="red">{}</font>'.format(events[id - 1].get("date"))
            else:
                date = events[id - 1].get("date")
        except (ValueError, TypeError, IndexError):
            self.send_error(400, "Invalid id")
            return
    
        self.send_response(200)
        self.end_headers()
        html = template.format(name=name, location=location, date=date)
        self.wfile.write(html.encode("utf-8"))
        return

HTTPServer(("", 8000), MyServerHandler).serve_forever()

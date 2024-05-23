from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

with open("a1-3.html", mode="r", encoding="utf-8") as file:
    template = file.read()

routes = []

def route(path, method):
    routes.append((path, method))

route("/id1", "id1")
route("/id2", "id2")
route("/id3", "id3")

class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        _url = urlparse(self.path)
        for r in routes:
            if r[0] == _url.path:
                eval("self." + r[1] + "()")
                break
        else:
            self.error()
   
    def id1(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(name="新歓", location="三田駅近くの居酒屋", date="2024/4/4")
        self.wfile.write(html.encode("utf-8"))
        return

    def id2(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(name="誕生日会", location="友達の家", date="2024/4/8")
        self.wfile.write(html.encode("utf-8"))
        return

    def id3(self):
        self.send_response(200)
        self.end_headers()
        html = template.format(name='<font color="red">勉強会</font>', location="Hack Bar", date="2024/5/6") 
        self.wfile.write(html.encode("utf-8"))
        return

    def error(self):
        self.send_error(404, "CANNOT ACCESS!!")
        # エラーコード(404)とメッセージを表示する．
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()

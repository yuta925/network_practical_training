from cgi import FieldStorage
from http.server import BaseHTTPRequestHandler, HTTPServer

with open("sample1-4.html", mode="r", encoding="utf-8") as file:
    input = file.read()
with open("sample1-2.html", mode="r", encoding="utf-8") as file:
    output = file.read()


class MyServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = input.format(title="入力画面")
        self.wfile.write(html.encode("utf-8"))
        return

    def do_POST(self):
        form = FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})
        message = "これは{}のページです．".format(form["name"].value)
        self.send_response(200)
        self.end_headers()
        html = output.format(title="選択リストテスト", message=message)
        self.wfile.write(html.encode("utf-8"))
        return


HTTPServer(("", 8000), MyServerHandler).serve_forever()
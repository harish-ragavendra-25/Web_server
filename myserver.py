from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title>my server</title>
</head>
<body>
<h1>top five web application framework</h1>
<h2>1.django</h2>
<h2>2.angular</h2>
<h2>3.express</h2>
<h2>4.ruby on rails</h2>
<h2>5.bootstrap</h2>
</body>
</html>
'''
class MyServer (BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received....")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())
print("this is my web server")
server_address=('',80)
httpd=HTTPServer(server_address,MyServer)
httpd.serve_forever()
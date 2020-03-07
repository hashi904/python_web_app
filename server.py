import http.server
import socketserver
import xml.etree.ElementTree as ET

# xpathを使ってport番号を取得
tree = ET.parse('conf.xml')
root = tree.getroot()
PORT = int(root.findall('.//server/port')[0].text)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
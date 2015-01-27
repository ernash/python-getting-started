import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
SServer = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port:", PORT
SServer.serve_forever()

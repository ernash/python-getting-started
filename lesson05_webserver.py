import SimpleHTTPServer
import SocketServer

PORT = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
SServer = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port:", PORT
SServer.serve_forever()

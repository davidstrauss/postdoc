from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import pprint

class POSTDoc(Resource):
  def __init__(self):
      Resource.__init__(self)

  def render_POST(self, request):
      pprint.pprint(request.requestHeaders)
      print(request.content.getvalue())
      return 'OK'

  def getChild(self, name, request):
      return self

root = POSTDoc()
factory = Site(root)
reactor.listenTCP(8080, factory)
reactor.run()

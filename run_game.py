from panda3d.core import PointLight, AmbientLight, NodePath, GeomVertexFormat, GeomVertexData, Geom, GeomVertexWriter, GeomPoints, GeomNode, RenderModeAttrib
from direct.showbase.ShowBase import ShowBase
import simplepbr

class TicTacToe27(ShowBase):

    def setup_light(self):
        light = PointLight("plight")
        light.setColor((5, 5, 5, 1))
        light_node = self.render.attachNewNode(light)
        light_node.setPos(0, -10, 10)
        self.render.setLight(light_node)

        #alight = AmbientLight("alight")
        #alight.setColor((5, 5, 5, 1))  # Stronger gray ambient
        #alnp = self.render.attachNewNode(alight)
        #self.render.setLight(alnp)

    def add_origin_dot(self, model):
        vformat = GeomVertexFormat.getV3()
        vdata = GeomVertexData("dot", vformat, Geom.UHStatic)
        vdata.setNumRows(1)

        vertex = GeomVertexWriter(vdata, "vertex")
        vertex.addData3(0, 0, 0)

        points = GeomPoints(Geom.UHStatic)
        points.addVertex(0)
        points.closePrimitive()

        geom = Geom(vdata)
        geom.addPrimitive(points)

        dot_node = GeomNode("origin_dot")
        dot_node.addGeom(geom)

        dot: NodePath = model.attachNewNode(dot_node)
        dot.setRenderMode(RenderModeAttrib.MPoint, 10)
        dot.setColor(1, 0, 0, 1)
        dot.setDepthWrite(False)
        dot.setDepthTest(False)
        dot.setBin("fixed", 10)

    
    def __init__(self):
        ShowBase.__init__(self)
        simplepbr.init()

        self.board = self.loader.loadModel("Assets/board.gltf")
        self.o_piece = self.loader.loadModel("Assets/o_piece.gltf")
        self.x_piece = self.loader.loadModel("Assets/x_piece.gltf")

        self.board.reparentTo(self.render)
        self.o_piece.reparentTo(self.render)
        self.x_piece.reparentTo(self.render)
        
        self.board.setPos(0, 0, 0)
        self.o_piece.setPos(0, 10, 0)
        self.x_piece.setPos(0, 5, 0)
        
        self.add_origin_dot(self.board)
        self.add_origin_dot(self.o_piece)
        self.add_origin_dot(self.x_piece)

        self.setup_light()
        
app = TicTacToe27()
app.run()
from panda3d.core import CollisionNode, CollisionBox, BitMask32, CollisionRay


class Map:
    def __init__(self, pos):
        self.model = 'sources/lvl0.obj'
        self.texture = 'sources/untitled.png'
        self.map = loader.loadModel(self.model)
        self.map.setTexture(loader.loadTexture(self.texture))
        self.map.reparentTo(render)
        self.map.setPos(pos)
        self.collisionsCreate()
    def collisionsCreate(self):
        self.mapGround = self.map.find("**/ground_collide")
        self.mapGround.node().setIntoCollideMask(BitMask32.bit(1))
        self.playerGroundRay = CollisionRay()  # Create the ray
        self.playerGroundRay.setOrigin(0, 0, 10)  # Set its origin
        self.playerGroundRay.setDirection(0, 0, -1)  # And its direction
        # Collision solids go in CollisionNode
        # Create and name the node
        self.playerGroundCol = CollisionNode('groundRay')
        self.playerGroundCol.addSolid(self.playerGroundRay)  # Add the ray
        self.playerGroundCol.setFromCollideMask(
            BitMask32.bit(1))  # Set its bitmasks
        self.playerGroundCol.setIntoCollideMask(BitMask32.allOff())
        # Attach the node to the ballRoot so that the ray is relative to the ball
        # (it will always be 10 feet over the ball and point down)
        self.playerGroundColNp = base.player.playerRoot.attachNewNode(self.playerGroundCol)
        # self.player_col.show()

        base.cTrav.addCollider(self.playerGroundColNp, base.cHandler)


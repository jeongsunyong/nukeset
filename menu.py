import nuke

tb = nuke.toolbar("Nodes")
m = tb.addMenu("sunyong", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/slate", "nuke.createNode('slate')")

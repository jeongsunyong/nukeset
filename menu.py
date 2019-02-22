import nuke
import nukescripts
import checkenv
import openfile
import genwritenode
import helloworld
import choicefile

tb = nuke.toolbar("Nodes")
m = tb.addMenu("sunyong", icon="icon.png")
m.addMenu("Draw")
m.addCommand("Draw/slate", "nuke.createNode('slate')")

mb = menubar.addMenu("sunyong")
mb.addCommand("Issue_and_Bugs", "nukescripts.start('https://github.com/jeongsunyong/nukeset/issues')")
mb.addCommand("-","","")
mb.addCommand("StartPerformanceTimers", "nuke.startPerformanceTimers()")
mb.addCommand("StopPerformanceTimers", "nuke.stopPerformanceTimers()")
mb.addCommand("CheckEnv", "checkenv.main()")
mb.addCommand("OpenFile", "openfile.main()")
#mb.addCommand("GenWriteNode", "genwritenode.main()","F10",shortcutContext=2)
mb.addCommand("HelloWorld", "helloworld.main()")
mb.addCommand("test", "choicefile.main()")

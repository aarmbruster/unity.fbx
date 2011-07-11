import maya.cmds as cmds
#import maya.mel as mel
import tempfile
from functools import partial

def deleteMyWindow(*args):
    cmds.deleteUI(args[0])

def save(*args):
    
    cmds.loadPlugin("fbxmaya.mll")
    #radios = cmds.radioCollection(args[1], q=True,cia=True)

    folder = tempfile.mkdtemp()
    defaultDirectory = cmds.workspace(q=True, rd=True)
    filePath = cmds.fileDialog2(cap="filename", dir=defaultDirectory, ff=".fbx", fm=0)
    
    if(filePath == None):
        print('File dialog has been cancelled.')
        return
    
    
    cmds.FBXExport(f=filePath)
    #cmds.file(filePath, typ="FBX export", force=True, es=True, options="sc=1;group=1;ea=True")
    #file -force -options "sc=1;group=1" -type "FBX export" -ea "D:/Projects_2011/IK_Test/Assets/Standard Assets/Models/Test2.fbx"
    #if(cmds.radioButton(radios[0], q=True, sl=True)):
        #cot.convert_ascii(obj, '', '', filePath[0])
    #else:
        #cot.convert_binary(obj, filePath[0])
    
    deleteMyWindow(args[0])
    
def run():
    
    window = cmds.window( title="Convert to ThreeJS", iconName='Short Name', widthHeight=(120, 200) )
    cmds.columnLayout( adjustableColumn=True )
    #radials = cmds.radioCollection()
    #cmds.radioButton( label='Ascii', sl=True)
    #cmds.radioButton( label='Binary' )
    cmds.button( label='Save', c=partial(save, window) )
    cmds.button( label='Close', c=partial(deleteMyWindow, window))
    
    cmds.setParent( '..' )
    cmds.showWindow( window )


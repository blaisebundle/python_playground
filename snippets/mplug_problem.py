# http://docs.autodesk.com/MAYAUL/2013/ENU/Maya-API-Documentation/cpp_ref/class_m_plug.html
from pymel.core import *
import maya.OpenMaya as om

testSphere = polyCube()[0].getShape().name()
mobj = om.MObject()
sList = om.MSelectionList()
sList.add( testSphere )
sList.getDependNode( 0, mobj )

fnNode = om.MFnDagNode( mobj )
plug = fnNode.findPlug( 'vrts' )
# plug.isArray()
plug.elementByLogicalIndex(5)
try:
	plug.elementByPhysicalIndex(5) # Will result in an error
except RuntimeError, e:
	om.MGlobal.displayWarning( '[elementByPhysicalIndex] >> {0}'.format(e) )
# This Python file uses the following encoding: utf-8
import os.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
import re
import sys

import cherrypy

class Treedraw(object):

    thefile = 'xxx'

    _cp_config = {'tools.staticdir.on' : True,
                  'tools.staticdir.dir' : '/home/anton/icecorpus/treedrawing/data',
                  'tools.staticdir.index' : 'index.html',
  	           'tools.caching.on' : False,
    }

    @cherrypy.expose
    def doSave(self, trees=None):
	f = open(self.thefile+".new",'w')
	tosave = trees.strip()[1:-1]
	f.write(tosave)
	f.close()

    def loadPsd( self, fileName ):
	self.thefile = fileName

	print("sdssssssssssssssssssssssssssssss")
	f = open(fileName, 'r')
	currentText = f.read()	
	allchars = 'a-zA-Z0-9þæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\*\"\,\.\:$\-\{\}'
	trees = currentText.split("\n\n")

	alltrees = '<div class="snode">'
	for tree in trees:
		tree0 = tree.strip()
		tree0 = re.sub('^\(','',tree0)
		tree0 = re.sub('\)$','',tree0).strip()
		tree0 = re.sub('\((['+allchars+']+) (['+allchars+']+)\)','<div class="snode">\\1<span class="wnode">\\2</span></div>',tree0)
		tree0 = re.sub('\(','<div class="snode">',tree0)
		tree0 = re.sub('\)','</div>',tree0)		
		alltrees = alltrees + tree0

 	alltrees = alltrees + '</div>'
	return alltrees

    def loadPsdOld( self, fileName ):
	f = open("torf06.psd", 'r')
	currentText = f.read()	
	allchars = '0-9a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\"\,\.$\-\=\*'
	trees = currentText.split("\n\n")
	tree0 = trees[0].strip()
	tree0 = re.sub('^\(','',tree0)
	tree0 = re.sub('\)$','',tree0).strip()
	tree0 = re.sub('\((['+allchars+']+) (['+allchars+']+)\)','<div class="snode">\\1<span class="wnode">\\2</span></div>',tree0)
	tree0 = re.sub('\(','<div class="snode">',tree0)
	tree0 = re.sub('\)','</div>',tree0)
	return tree0

    def loadTxt( self, fileName ):
	f = open( fileName )
	currentText = f.read()
	trees = currentText.split("\n\n")
	tree0 = trees[1].strip();
	words = tree0.split('\n');
	thetree='<div class="snode">IP-MAT'
	wordnr=0
	for word in words:
		thetree=thetree+'<div class="snode">X<span class="wnode">'+word+'</span></div>'

	thetree=thetree+"</div>"
	return thetree
	

    @cherrypy.expose
    def index(self):
	filename = sys.argv[1]
	
        currentTree=self.loadPsd( filename )  
        #
        return """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html>
<head>  <title>Treedrawing</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link rel="stylesheet" type="text/css" href="css/treedrawing.css" type="text/css"></link>
	<script type= "application/javascript" src="scripts/jquery.js"/></script>		
	<script type= "application/javascript" src="scripts/treedrawing.js"/></script>		
</head>
<body oncontextmenu="return false;">
<div style="display:none"><span>Sel1: </span><span id="labsel1">null</span></div>
<div style="display:none"><span>Sel2: </span><span id="labsel2">null</span></div>

<br />

<div id="floatMenu">
<div style="background-color: navy; color: white; font-weight: bold;">IcePaHC Treedrawing 0.1</div>

Editing: """+self.thefile+""" <br />

<input class="menubutton" type="button" value="Save" id="butsave">

<div id="debugpane">x</div>
</div>
<div id="editpane">"""+currentTree+"""</div>



</body>
</html>"""


#index.exposed = True
cherrypy.quickstart(Treedraw())

# This Python file uses the following encoding: utf-8
import os.path
# current_dir = os.path.dirname(os.path.abspath(__file__))
import re
import sys

import cherrypy

class Treedraw(object):

    _cp_config = {'tools.staticdir.on' : True,
                  'tools.staticdir.dir' : '/home/anton/icecorpus/treedrawing/data',
                  'tools.staticdir.index' : 'index.html',
  	           'tools.caching.on' : False,
    }

    def loadPsd( self, fileName ):
	f = open("torf06.psd", 'r')
	currentText = f.read()	
	allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\"\,\.$\-'
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
        currentTree=self.loadPsd( sys.argv[1] )  
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

<div id="editpane">"""+currentTree+"""</div>

<div id="debugpane">x</div>
</body>
</html>"""


#index.exposed = True
cherrypy.quickstart(Treedraw())

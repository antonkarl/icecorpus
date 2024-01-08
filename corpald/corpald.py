#!/usr/bin/env python

import os
import sys
import re
import shutil
import subprocess
import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import pango
import ConfigParser
from corpussearch import CSQuery
 
class Corpald:
    
    config = None
    is_saved = False
    query_file = "unsaved"
    definitions_file = None
    thequery = None
    combo = None
    filter_size=0    
    querybuffer = None  # ! CodeBuffer(None)
    resultbuffer = None  # ! CodeBuffer(None)    
    
    # syntax highlighting styles
    operator_match = r"\b(AND|OR|NOT)\b"
    operator_style = None        
    keyword_match = r"\b(CCommands|cCommands|ccommands|Column|column|Col|col|Dominates|dominates|Doms|doms\
    DomsWords|domsWords|domswords|Exists|exists|HasLabel|hasLabel|haslabel|HasSister|hasSister|hassister\
    iDominates|idominates|iDoms|idoms|iDomsFirst|idomsfirst|iDomsLast|idomslast|iDomsMod|idomsmod\
    iDomsNumber|idomsnumber|iDomsNum|idomsnum|iDomsOnly|idomsonly|iDomsTotal|idomstotal\
    iDomsViaTrace|idomsviatrace|InID|inID|iPrecedes|iprecedes|iPres|ipres|IsRoot|isRoot|isroot\
    Precedes|precedes|Pres|pres|SameIndex|sameIndex|sameindex)\b"
    keyword_style = None
    definition_match = None
    definition_style = None
    
    comment_match = r"/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/"
    comment_style = None
    text_match = r"/\~\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\~/"
    text_style = None
    
    # ###############################
    # Getters and setters
    # ###############################    
    
    def get_query_directory(self):
        the_dir = os.path.expanduser("~") + "/icepahc"
        if not os.path.exists(the_dir):
            os.mkdir(the_dir)
            os.mkdir(the_dir+"/config")
                        
            shutil.copy2( self.get_corpald_path()+"/icepahc.def",  the_dir+"/config/icepahc.def" )
            
            dative_subjects = "node:IP-*\nnodes_only:true\nremove_nodes:true\ndefine:"+the_dir+"/config/icepahc.def\nquery:(IP-* idoms NP-SBJ) AND (NP-SBJ idoms *-D)"
            sample_file = open(the_dir+"/dative_subjects.q",  "w")
            sample_file.write(dative_subjects)
            sample_file.close()            
        return the_dir
    
    def get_corpald_path(self):
        pathname, scriptname = os.path.split(sys.argv[0])
        return os.path.abspath(pathname)                 
            
    def get_corpussearch_path(self):        
        return self.config.get("paths","corpussearch")
        
    def get_query(self):
        querybuffer = self.builder.get_object("textview_query").get_buffer()   
        thequery=querybuffer.get_text(querybuffer.get_start_iter(), querybuffer.get_end_iter(), include_hidden_chars=True)        
        return thequery
        
    def set_query(self, thequery):        
        querybuffer = self.builder.get_object("textview_query").get_buffer()   
        querybuffer.set_text( thequery )
        
    def set_saved(self, is_saved):
        self.is_saved = is_saved
        self.set_query_file(self.query_file)            
        
    def set_query_file(self, query_file):
        self.query_file = query_file
        markup = "<b>Query</b> ("+self.query_file
        if( not self.is_saved ):
            markup = markup + " *"
        markup = markup + ")"
        self.builder.get_object("label_queryframe").set_markup(markup)
  
    def set_result(self, resultstring):
        txtbuffer = self.builder.get_object("textview_results").get_buffer()   
        txtbuffer.set_text(resultstring)
        
    def clear_result(self):
        self.builder.get_object("label_resultsframe").set_markup("<b>Results</b>")
        self.builder.get_object("resultbuffer").set_text("")
        
    def get_filter(self):
        filter_id=combo.get_active()
        return self.config.get("filters","path"+str(filter_id))

    # ###############################
    # IO stuff
    # ###############################

    def write_file(self, text, filename):
        qfile=open(filename,"w")            
        qfile.write(text)
        qfile.close()   
     
    def read_file(self, filename):
        qfile=open(filename,"r")            
        text = qfile.read()
        qfile.close()      
        return text
        
    # Generate an unused name for a temporary query file
    def generate_tempquery_path(self):       
        pathbase = self.get_query_directory()+"/"
        index = 1        
        temppath = pathbase + "temp" + str(index)+".q"        
        while os.path.exists(temppath):
            index = index + 1
            temppath = pathbase + "temp" + str(index)+".q"    
        return temppath
        
    # Generate an unused name for a temporary result file
    def generate_tempresult_path(self):       
        pathbase = self.get_query_directory()+"/"
        index = 1        
        temppath = pathbase + "corpald_query" + str(index)+".out"    
        while os.path.exists(temppath):
            index = index + 1
            temppath = pathbase + "corpald_query" + str(index)+".out"
        return temppath
    

    # ###############################
    # Event handling 
    # ###############################
    
    def on_cut(self, widget, data=None):
        clipboard = gtk.clipboard_get("CLIPBOARD") 
        querybuffer = self.builder.get_object("querybuffer")
        # querybuffer.select_range(resultbuffer.get_start_iter(), resultbuffer.get_end_iter())
        querybuffer.cut_clipboard(clipboard, True)
        
    def on_copy(self, widget, data=None):
        clipboard = gtk.clipboard_get("CLIPBOARD") 
        querybuffer = self.builder.get_object("querybuffer")
        # querybuffer.select_range(resultbuffer.get_start_iter(), resultbuffer.get_end_iter())
        querybuffer.copy_clipboard(clipboard)    

    def on_paste(self, widget, data=None):
        clipboard = gtk.clipboard_get("CLIPBOARD") 
        querybuffer = self.builder.get_object("querybuffer")
        # querybuffer.select_range(resultbuffer.get_start_iter(), resultbuffer.get_end_iter())
        querybuffer.paste_clipboard(clipboard, None, True)

    def on_new(self, widget, data=None):
        # Reset everything
        self.thequery.nodes_only = self.builder.get_object("checkbutton_nodes_only").set_active(False)
        self.thequery.remove_nodes = self.builder.get_object("checkbutton_remove_nodes").set_active(False)
        self.thequery.print_indices = self.builder.get_object("checkbutton_print_indices").set_active(False)
        self.thequery.print_complement = self.builder.get_object("checkbutton_print_complement").set_active(False)
        self.thequery.node = self.builder.get_object("entry_root_node").set_text("$ROOT")
        self.thequery.definitions = self.builder.get_object("filechooserbutton_def").get_filename()
        self.thequery.remark = self.builder.get_object("entry_remark").set_text("")
                
        self.set_query("")
        self.is_saved = True
        self.set_query_file("unsaved")
        self.clear_result()
        self.builder.get_object("button_save_query").set_sensitive(False)
        self.builder.get_object("menuitem_save_query").set_sensitive(False)        
        self.builder.get_object("button_save_as").set_sensitive(False) 
        self.builder.get_object("menuitem_save_as").set_sensitive(False)       
        
    def on_open_query(self, widget, data=None):            
        # create a new dialog 
        dialog = gtk.FileChooserDialog("Open query", None,
            gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
            gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_current_folder(self.get_query_directory())
        if dialog.run() == gtk.RESPONSE_OK:
            filename = dialog.get_filename()
            self.thequery = CSQuery()
            self.thequery.load(filename)
            # print("back in corpald")
            
            # thequery = self.read_file(filename)
            self.set_query(self.thequery.query.strip())
            self.builder.get_object("entry_root_node").set_text(self.thequery.node)            
            self.builder.get_object("checkbutton_nodes_only").set_active(self.thequery.nodes_only)
            self.builder.get_object("checkbutton_remove_nodes").set_active(self.thequery.remove_nodes)
            self.builder.get_object("checkbutton_print_indices").set_active(self.thequery.print_indices)
            self.builder.get_object("checkbutton_print_complement").set_active(self.thequery.print_complement)            
            if self.thequery.definitions:
                self.builder.get_object("filechooserbutton_def").set_filename(self.thequery.definitions)
            else:
                self.builder.get_object("filechooserbutton_def").unselect_all()
            if self.thequery.remark:
                self.builder.get_object("entry_remark").set_text(self.thequery.remark)
            self.is_saved = True            
            self.set_query_file(filename)
            self.builder.get_object("button_save_query").set_sensitive(False) 
            self.builder.get_object("menuitem_save_query").set_sensitive(False)                    
            
            # Clear result box
            self.clear_result()
            #self.builder.get_object("label_resultsframe").set_markup("<b>Results</b>")
            #self.builder.get_object("resultbuffer").set_text("")
            
        dialog.destroy()

    def accel_on_save(self, accel_group, acceleratable, keyval, modifier):
        self.on_save_query(None)

    # User pressed "Save query" button
    def on_save_query(self, widget, data=None):
        if self.query_file == "unsaved":
            self.on_save_as(widget, data)
        else:
            self.perform_save_query()
        
    # User pressed "Save query as" button
    def on_save_as(self, widget, data=None):
        # create a new save dialog 
        dialog = gtk.FileChooserDialog("Save query", None,
            gtk.FILE_CHOOSER_ACTION_SAVE, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
            gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_current_folder(self.get_query_directory())
        if dialog.run() == gtk.RESPONSE_OK:
            filename = dialog.get_filename()
            self.write_file(self.get_query(), filename)
            self.set_query_file(filename)
            self.builder.get_object("button_save_query").set_sensitive(False) 
            self.builder.get_object("menuitem_save_query").set_sensitive(False)                    
            
        dialog.destroy()
    
    # 
    def perform_save_query(self):
            # self.write_file(self.get_query(), self.query_file)           
            self.thequery = CSQuery()             
            self.thequery.query=self.get_query()
            self.thequery.nodes_only = self.builder.get_object("checkbutton_nodes_only").get_active()
            self.thequery.remove_nodes = self.builder.get_object("checkbutton_remove_nodes").get_active()
            self.thequery.print_indices = self.builder.get_object("checkbutton_print_indices").get_active()
            self.thequery.print_complement = self.builder.get_object("checkbutton_print_complement").get_active()
            self.thequery.node = self.builder.get_object("entry_root_node").get_text()
            self.thequery.definitions = self.builder.get_object("filechooserbutton_def").get_filename()
            self.thequery.remark = self.builder.get_object("entry_remark").get_text()            
            
            self.thequery.save(self.query_file)
            self.set_saved(True)
            self.builder.get_object("button_save_query").set_sensitive(False)  
            self.builder.get_object("menuitem_save_query").set_sensitive(False)  
            
            #XXX
            # self.do_highlight()      
        

    def do_highlight_result(self):                    
        querybuffer = self.builder.get_object("textview_results").get_buffer()   
        thequery=querybuffer.get_text(querybuffer.get_start_iter(), querybuffer.get_end_iter(), include_hidden_chars=True)                

        startall = querybuffer.get_iter_at_offset(0)
        endall = querybuffer.get_iter_at_offset(len(thequery))
        querybuffer.remove_all_tags(startall,endall)        
                            
        for m in re.finditer(self.comment_match, thequery.decode(),re.U):
            startoffset = m.start()
            endoffset = m.end()                    
            start = querybuffer.get_iter_at_offset(startoffset)
            end = querybuffer.get_iter_at_offset(endoffset)                            
            querybuffer.apply_tag(self.comment_style, start, end)
            
        for m in re.finditer(self.text_match, thequery.decode(),re.U):
            startoffset = m.start()
            endoffset = m.end()                    
            start = querybuffer.get_iter_at_offset(startoffset)
            end = querybuffer.get_iter_at_offset(endoffset)                            
            querybuffer.apply_tag(self.text_style, start, end)            
                    
        
    def do_highlight(self):                    
        querybuffer = self.builder.get_object("textview_query").get_buffer()   
        thequery=querybuffer.get_text(querybuffer.get_start_iter(), querybuffer.get_end_iter(), include_hidden_chars=True)                

        startall = querybuffer.get_iter_at_offset(0)
        endall = querybuffer.get_iter_at_offset(len(thequery))
        querybuffer.remove_all_tags(startall,endall)        
                            
        for m in re.finditer(self.operator_match, thequery.decode(),re.U):
            startoffset = m.start()
            endoffset = m.end()                    
            start = querybuffer.get_iter_at_offset(startoffset)
            end = querybuffer.get_iter_at_offset(endoffset)                            
            querybuffer.apply_tag(self.operator_style, start, end)
            
        for m in re.finditer(self.keyword_match, thequery.decode(),re.U):
            startoffset = m.start()
            endoffset = m.end()                    
            start = querybuffer.get_iter_at_offset(startoffset)
            end = querybuffer.get_iter_at_offset(endoffset)                            
            querybuffer.apply_tag(self.keyword_style, start, end)            
            
        if self.definition_match:
            for m in re.finditer(self.definition_match, thequery.decode(),re.U):
                startoffset = m.start()
                endoffset = m.end()                    
                start = querybuffer.get_iter_at_offset(startoffset)
                end = querybuffer.get_iter_at_offset(endoffset)                            
                querybuffer.apply_tag(self.definition_style, start, end)            
        
            
            # textbuffer.apply_tag_by_name(name, start, end)            
            #print( thequery )            
                
    def perform_query_changed(self):
        self.set_saved(False)
        self.builder.get_object("button_save_query").set_sensitive(True)
        self.builder.get_object("menuitem_save_query").set_sensitive(True)        
        self.builder.get_object("button_save_as").set_sensitive(True)   
        self.builder.get_object("menuitem_save_as").set_sensitive(True)             
        self.builder.get_object("button_new").set_sensitive(True)            
                
        self.do_highlight()
        
        defs = self.builder.get_object("filechooserbutton_def").get_filename()
        if self.definitions_file != defs:
            # print("setting file to: " + defs)
            self.definitions_file = defs
            self.reload_definitions()
            
            
    # Reload definitions
    def reload_definitions(self):
        if self.definitions_file == None:
            return None
        
        keywordlist=""
        # definitions_file = open(self.definitions_file,"r")
        lines = open(self.definitions_file).readlines()
        for line in lines:
            if not line[0]=='/':                
                chunks=line.split(":")
                if len(chunks)==2:
                    keyword=chunks[0].strip()
                    keywordlist=keywordlist+keyword+"|"
        
        if len(keywordlist) > 0:
            keywordlist=keywordlist[0:len(keywordlist)-1]
        
        
        self.definition_match = r"\b("+keywordlist +r")\b"
        # print(self.definition_match)
    
    def on_result_changed(self,widget,data=None):
        self.do_highlight_result()
    
    # User made a change to the current query
    def on_query_changed(self, widget, data=None):
        self.perform_query_changed()
    
    # User selected "About" menu item
    def on_about(self, widget, data=None):
        aboutdialog = self.builder.get_object('aboutdialog')
        # Show the main window        
        response = aboutdialog.run()  
        if response == gtk.RESPONSE_DELETE_EVENT or response == gtk.RESPONSE_CANCEL:
            aboutdialog.hide()
        # aboutdialog.destroy()
                         
    def on_show_directory(self, widget, data=None):
        d = self.get_query_directory()
        if sys.platform=='win32':
            subprocess.Popen(['start', d], shell= True)

        elif sys.platform=='darwin':
            subprocess.Popen(['open', d])

        else:
            try:
                subprocess.Popen(['xdg-open', d])
            except OSError:
                pass
        # subprocess.Popen(['nautilus', "/home/anton/icepahc"], stdin=None, stdout=None)
    
    def on_copy_clipboard(self, widget, data=None):
        clipboard = gtk.clipboard_get("CLIPBOARD") 
        resultbuffer = self.builder.get_object("resultbuffer")
        resultbuffer.select_range(resultbuffer.get_start_iter(), resultbuffer.get_end_iter())
        resultbuffer.copy_clipboard(clipboard)
    
    def on_filter_changed(self, widget, data=None):
        # tooltips = gtk.Tooltips()        
        # tooltips.set_tip(combo, self.get_filter(), tip_private=None)                        
        combo.set_tooltip_text( self.get_filter() )
            
    
    # User pressed "Run query" button
    def on_run_query(self, widget, data=None):        
        # print("Starting search")        
        outfile=self.generate_tempresult_path()
        
        if not self.query_file == "unsaved":
            # temppath = self.generate_tempresult_path()
            self.perform_save_query()
            self.run_query(self.query_file)
        else:
            # Use temporary files
            temppath = self.generate_tempquery_path()
            thequery = self.get_query()

            # Write .q file and run CorpusSearch 
            # self.write_file(thequery, temppath)  
            self.query_file=temppath
            self.thequery=CSQuery()
            self.perform_save_query()
            self.is_saved=False
            self.set_query_file("unsaved")
            self.thequery=None
            self.run_query(temppath, outfile)            
            
            # Cleanput since those are temporary files
            os.remove(temppath)      
           
    # Handle "delete_event" event
    def delete_event(self, widget, event, data=None):
        return False

    # Handle "destroy" event
    def destroy(self, widget, data=None):
        gtk.main_quit()          
        
    # ###############################
    # Core functions
    # ###############################        

    firstrun = True
    def run_query(self, queryfile, outfile=None):        
        if not outfile:        
            outfile =  os.path.splitext( queryfile )[0] + ".out"    
            if os.path.exists(outfile):                
                # if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):                               
                os.remove(outfile)

        corpussearch = self.get_corpussearch_path()
        
        
        # searchCommand = "java -classpath "+corpussearch+" csearch/CorpusSearch "+queryfile+" /home/anton/icecorpus/finished/*.psd"
        # filter = os.path.expanduser("~")+"/icecorpus/finished/*.psd"
        filter = self.get_filter()
        searchCommand = "java -classpath "+corpussearch+" csearch/CorpusSearch "+queryfile+" "+filter
        searchCommand = searchCommand + " -out "+outfile        
        os.system( searchCommand )

        # Display result
        resultfile = open(outfile, "r")
        if resultfile:
            resultstring = resultfile.read()
            resultfile.close()
            self.set_result(resultstring)
            self.builder.get_object("label_resultsframe").set_markup("<b>Results</b> ("+outfile+")")
            # self.do_highlight_result()
            global combo            
            if self.firstrun:                            
                combo.append_text("Search last result")
                self.config.set("filters","path"+str(self.filter_size),outfile)                
                self.firstrun=False
            else:
                combo.remove_text(self.filter_size)
                combo.append_text("Search last result")
                self.config.set("filters","path"+str(self.filter_size),outfile)
            

        # print("Search finished")    
        
    # ###############################
    # Initialization
    # ###############################        

    
    def load_settings(self):
            
        config_path = self.get_query_directory() + "/config/corpald.ini"        
        self.config = ConfigParser.ConfigParser(dict())
        
        # Create a config file with default settings if it is missing
        if not os.path.exists(config_path):
            # set a number of parameters            
            self.config.add_section("paths")
            self.config.set("paths", "definitions", self.get_query_directory()+"/config/icepahc.def" )
            
            self.config.set("paths", "corpussearch", self.get_corpald_path()+"/lib/CS_2.002.75.jar" )
            #/home/anton/icecorpus/parsing
            # XXX
            # self.config.set("paths", "corpussearch", os.path.expanduser("~")+"/icecorpus/parsing/CS_2.002.75.jar" )
            
            #self.config.add_section("style")
            #self.config.set("style", "font", "Monospaced 12")
            
            # create filters
            
            default_filters_path = self.get_corpald_path()+"/filters.ini"
            default_filters = open(default_filters_path, "r")
            filtersection=default_filters.read()

            with open(config_path, "wb") as configfile:
                self.config.write(configfile)    
                configfile.write(filtersection)
                configfile.close()
        
        self.config.read(config_path)
    
    def populate_gui(self):
        self.builder.get_object("filechooserbutton_def").set_filename( self.config.get("paths", "definitions") )
                                                                                                    
        global combo 
        combo = gtk.combo_box_new_text()
        combo.connect("changed", self.on_filter_changed)
        # combo.child.connect("activate", self.on_filter_changed)      
        # comboboxentry.child.connect('activate', self.on_change)  
        

        fcount=0
        while( self.config.has_option("filters","name"+str(fcount) ) ):
            combo.append_text( self.config.get("filters","name"+str(fcount)) )
            # combo.append_text("IcePaHC (12th century)")
            fcount = fcount + 1
        
        self.filter_size= fcount
        
        combo.set_active(0)
        combo.show()

        box = self.builder.get_object('hbox_filter')
        box.pack_start(combo, True, False)
        
        fd = pango.FontDescription("Monospace 11"); 
        self.builder.get_object("textview_query").modify_font( fd )

        # Configure save in textview
        self.accels = gtk.AccelGroup()
        self.accels.connect_group(ord('S'), gtk.gdk.CONTROL_MASK, 0, self.accel_on_save)
        self.window.add_accel_group(self.accels)
        
        # Configure syntax highlighting of Query
        # qlang = SyntaxLoader("corpussearch")   
        # self.querybuffer.reset_language(qlang)
        # self.builder.get_object("textview_query").set_buffer(self.querybuffer)
        # self.querybuffer.connect("changed", self.on_query_changed)

        # Configure syntax highlighting of Result
        # psdlang = SyntaxLoader("psd")   
        # self.resultbuffer.reset_language(psdlang)
        # self.builder.get_object("textview_results").set_buffer(self.resultbuffer)
        # self.result.connect("changed", self.on_query_changed)


        #append_text("IcePaHC (Entire corpus)")
        #self.builder.get_object("combobox_filter").append_text("IcePaHC (12th century)")

    def __init__(self):        

        # also not needed if installed:
     
        self.load_settings()
        
        # Configure initial state        
        self.is_saved = False
        
        # Use GTKBuilder to build GUI from corpald.glade
        self.builder = gtk.Builder()
        self.builder.add_from_file("corpald.glade")
        self.builder.connect_signals(self)  
        self.window = self.builder.get_object('corpaldwindow')
        self.window.connect("destroy", self.destroy)
        self.window.connect("delete_event", self.delete_event)        
                        
        # Fill in various default settings

        query = CSQuery()
        self.populate_gui()                
        
        # Make font vars
        # self.operator = self.builder.get_object("textview_query").get_buffer().create_tag('bold', weight = pango.WEIGHT_BOLD )
        self.operator_style = self.builder.get_object("textview_query").get_buffer().create_tag('operator', weight = pango.WEIGHT_BOLD, foreground = gtk.gdk.Color('#008') )
        self.keyword_style = self.builder.get_object("textview_query").get_buffer().create_tag('keyword', weight = pango.WEIGHT_BOLD, foreground = gtk.gdk.Color('#E56717') )
        self.definition_style = self.builder.get_object("textview_query").get_buffer().create_tag('definition', weight = pango.WEIGHT_BOLD, foreground = gtk.gdk.Color('#800') )
        self.comment_style = self.builder.get_object("textview_results").get_buffer().create_tag('comment', foreground = gtk.gdk.Color('#C68E17') )
        self.text_style = self.builder.get_object("textview_results").get_buffer().create_tag('text', foreground = gtk.gdk.Color('#342D7E') )
                
        # Show the main window
        self.window.show()
        
    def main(self):               
        # Start PyGTK
        gtk.main()
                
# Run Corpald
if __name__ == "__main__":
    corpald = Corpald()
    corpald.main()

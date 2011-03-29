from lepl import Delayed, Node, Space, Regexp, Drop, DroppedSpace
from operator import attrgetter
import re

class BracketParser:    
    def get_bracket_parser(self):
        phrase = Delayed()
        label = Regexp(r"[^ \t\n\r\(\)]+")
        word = label > Node
        #terminal = Word() | ( Word() & Drop(Space()) & word )     
        terminal = label | ( label & Drop(Space()) & word )
        with DroppedSpace():
            phrase += Drop('(') & ( terminal | label & phrase[1:] | phrase[1:] ) & Drop(')') > Node
        return phrase
    
    id_counter=-1
    bracket_counter=-1    
    
    def next_bracket(self):
        self.bracket_counter += 1
        return self.bracket_counter
    
    def next_id(self):
        self.id_counter += 1
        return self.id_counter
   
    def recurse_node( self, node, node_list, parent_id, depth ):
        output_node = PhraseNode()                  

        output_node.label = node[0]
        if depth == 0:
            output_node.label = ""   
        output_node.parent_id = parent_id
    
        output_node.start_bracket = self.next_bracket()        
        output_node.node_id = self.next_id()
        
        output_node.depth = depth
        output_node.node = node        
        depth+=1
                
        if hasattr( node, "Node"):
            for child in node.Node:               
                #self.bracket_counter = self.recurse_node(child,node_list, output_node.node_id, depth)
                self.recurse_node(child,node_list, output_node.node_id, depth)            
            #self.bracket_counter-=1                                
        else:
            # this is a terminal 
            output_node.node_type = 3  
        
        output_node.end_bracket = self.next_bracket()    
            
                 
        # parse lemma
        output_node.lemma=None
        if output_node.node_type == 3:
            chunks = output_node.label.split("-") 
            if len(chunks) == 2:                
                output_node.label = chunks[0]
                output_node.lemma = chunks[1]
            
        node_list.append( output_node )

    
    def recurse_node_old( self, node, node_id, id_offset, node_list, parent_id, depth ):
        output_node = PhraseNode()                  
        current_start = node_id - id_offset
        output_node.start_bracket = current_start      
        output_node.label = node[0]
        if depth == 0:
            output_node.label = ""   
        output_node.parent_id = parent_id

        node_id+=1        
        output_node.node_id = node_id        
        if len(node_list) > 0:     
            output_node.node_id = max( node_list, key=attrgetter("node_id")).node_id + 1
        
        output_node.depth = depth
        output_node.node = node        
        depth+=1

                
        if hasattr( node, "Node"):
            for child in node.Node:               
                node_id=self.recurse_node(child,node_id,id_offset,node_list, output_node.node_id, depth)
                #node_id+=1                                
        else:
            # this is a terminal 
            output_node.node_type = 3    
            
        output_node.end_bracket = node_id 
        # parse lemma
        output_node.lemma=None
        if output_node.node_type == 3:
            chunks = output_node.label.split("-") 
            if len(chunks) == 2:
                output_node.label = chunks[0]
                output_node.lemma = chunks[1]
            
        node_list.append( output_node )
        #print( str(output_node.start_bracket) + "\t" + str(output_node.end_bracket) + "\t" + str(output_node.node_type) + "\t" + output_node.label  )
        return node_id +1

    def parse(self, bracket_parse, start_id=0):       
        bracket_parse = bracket_parse.replace('\n',' '); 
        parser = self.get_bracket_parser()
        stuff = parser.parse( bracket_parse )[0]   
        #print(stuff)             
        currentNode = stuff #.Node[0]
        node_list = []
        self.id_counter = start_id - 1
        self.bracket_counter = -1
        self.recurse_node( currentNode, node_list, -1, 0 )        
        node_list = sorted(node_list, key=attrgetter('start_bracket'))        
        return PhraseTree(node_list)

class PhraseTree:
    node_list = None
    
    def __init__(self, node_list):
        self.node_list = node_list
        
    def max_id(self):
        return max( self.node_list, key=attrgetter("node_id") ).node_id
    
    def to_text(self):
        text = ""
        for bracket_node in self.node_list:
            if bracket_node.node_type == 3:
                lstart = bracket_node.label[0] 
                if not (lstart == "*" or lstart == "{" or lstart == "<" or lstart=="0"):                
                    text += bracket_node.label + " "
        text = text.replace("$ $", "")
                
        return text.strip() 
    
    def to_brackets(self):
        bracket_list = []
        for node in self.node_list:
            bracket_list.append(0)
            bracket_list.append(0)
                    
        last_depth = 0        
        
        for node in self.node_list:
            if node.depth == 0:
                node.label = ""
            if node.node_type == 3:
                bracket_list[node.start_bracket] = ""+node.label+""
                if node.lemma != None:
                    bracket_list[node.start_bracket] += "-"+ node.lemma
                bracket_list[node.end_bracket] = ""        
            else:        
                opening = ""
                if node.depth < last_depth:
                    opening = "\n"
                    for i in range(0, node.depth):
                        opening+="\t"
                    opening += "  "
                bracket_list[node.start_bracket] = opening + "("+str(node.label)+" " 
                bracket_list[node.end_bracket] = ")"                
            last_depth = node.depth
                
        return ''.join([label for label in bracket_list])
        
    def to_table(self):
        table = ""
        for output_node in self.node_list:               
            table += str(output_node.node_id) + "\t" + str(output_node.start_bracket) + "\t" + str(output_node.end_bracket) + "\t" + str(output_node.depth) + "\t" + str(output_node.node_type) + "\t" + str(output_node.parent_id) + "\t" + str(output_node.label) + "\t" + str(output_node.lemma) + "\n"            
        return table.strip()    

          
class PhraseNode:        
    def __init__(self):
        self.node_type = 1

class Corpus:
    trees = []
    filter = [] 
    def __init__(self, trees):
        if( trees ):
            self.trees = trees
            self.reset_filter()

    def from_brackets(self,path):
        pass
            
    def reset_filter(self):
        self.filter = [i for i in range( len(self.trees) )]
                            
    def add_filter(self,filter):
        self.filter = self.filter & filter
    
# some testing
bracket_tree = """( (IP-MAT (NP-SBJ (NPR-N Halldór-halldór))
  (VBDI hét)
  (NP-PRD (NP (ONE-N einn) (ADJ-N ríkur) (N-N maður))
      (CONJP (CONJ og)
         (NP (N-N vinur)
             (NP-POS (NPR-G Haralds)
                 (NP-PRN (N-G konungs-konungur))))))
  (. .-.) ) (ID 1275.MORKIN.NAR-HIS,.2) )"""

fourtrees="""( (META (NP (ADJ-N XLIII.) (N-N KAPÍTULI))) (ID 1275.MORKIN.NAR-HIS,.1))

( (IP-MAT (NP-SBJ (NPR-N Halldór))
      (VBDI hét)
      (NP-PRD (NP (ONE-N einn) (ADJ-N ríkur) (N-N maður))
          (CONJP (CONJ og)
             (NP (N-N vinur)
                 (NP-POS (NPR-G Haralds)
                     (NP-PRN (N-G konungs))))))
      (. .-.)) (ID 1275.MORKIN.NAR-HIS,.2))

( (IP-MAT (NP-SBJ (N-N Dóttir)
          (NP-POS (PRO-G hans)))
      (VBDI hét)
      (NP-PRD (NPR-N Ingibjörg)
          (, ,-,)
          (NP-PRN (ADJP (ADJ-N vitur)
                (CONJP *ICH*-1))
              (N-N kona)
              (CONJP-1 (CONJ og) (ADJ-N væn))))
      (. ,-,)) (ID 1275.MORKIN.NAR-HIS,.3))

( (IP-MAT (CONJ og)
      (NP-SBJ *con*)
      (BEDI var)
      (ADVP-TMP (ADV enn))
      (PP (P í)
          (NP (N-D vináttu)))
      (PP (P við)
          (NP (N-A konung-konungur)))
      (. ,-,)) (ID 1275.MORKIN.NAR.HIS,.4))"""


def run_test():
    # corpus = corpus.replace('\n',' ');
    # tree = parser.parse( bracket_tree,5 )
    #print(len(node_list))
    print( "\nid\tstart\tend\tdepth\ttype\tpar_id\tlabel\tlemma" )
    thetrees = re.split("\n\n",fourtrees)
    parser = BracketParser()
    
    theid = 0
    for bracket_tree in thetrees:
        tree = parser.parse(bracket_tree,theid)
        theid=tree.max_id()+1        
        for output_node in tree.node_list:               
            print( str(output_node.node_id) + "\t" + str(output_node.start_bracket) + "\t" + str(output_node.end_bracket) + "\t" + str(output_node.depth) + "\t" + str(output_node.node_type) + "\t" + str(output_node.parent_id) + "\t" + str(output_node.label) + "\t" + str(output_node.lemma) )    
    
    #tree = parser.parse( bracket_tree )
    #for output_node in tree.node_list:               
    #    print( str(output_node.node_id) + "\t" + str(output_node.start_bracket) + "\t" + str(output_node.end_bracket) + "\t" + str(output_node.depth) + "\t" + str(output_node.node_type) + "\t" + str(output_node.parent_id) + "\t" + str(output_node.label) + "\t" + str(output_node.lemma) )    
    # print( tree.to_brackets() )
    
    print( tree.to_text() )

def read_trees( bracket_file_path ):
    input_file = open( bracket_file_path )
    alltrees = input_file.read()
    alltrees = re.sub("(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)","",alltrees)
    alltrees = alltrees.strip()
    bracket_trees = alltrees.split("\n\n")
#    print( len(bracket_trees) )
#    print( bracket_trees[0] )
    parser = BracketParser()
    
    trees = []
    next_id = 0
    for i in range(0,10):
        bracket_tree = bracket_trees[i]        
        tree = parser.parse( bracket_tree, next_id )
        next_id = tree.max_id() + 1
        trees.append(tree)
        #print( len(trees) )
        print( tree.to_table() ) 
    return trees


trees = read_trees("1200.sturltest.nar.sag.psd")



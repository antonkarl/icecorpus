from lepl import Delayed, Node, Space, Word, Regexp, Drop, DroppedSpace
from operator import attrgetter

class NumberedBracket:
    def __init__(self):
        self.node_type = 1

class BracketParser:    

    def get_bracket_parser(self):
        phrase = Delayed()
        label = Regexp(r"[^ \t\n\r\(\)]+")
        word = Word() > Node
        terminal = Word() | ( Word() & Drop(Space()) & word )     
        with DroppedSpace():
            phrase += Drop('(') & ( terminal | label & phrase[1:] | phrase[1:] ) & Drop(')') > Node
        return phrase
    
    def recurse_node( self, node, node_id, id_offset, node_list, parent_id, depth ):
        output_node = NumberedBracket()                  
        current_start = node_id - id_offset
        output_node.start_bracket = current_start      
        output_node.label = node[0]   
        output_node.parent_id = parent_id
        output_node.node_id = node_id     
        output_node.depth = depth
        depth+=1
        if hasattr( node, "Node"):
            for child in node.Node:
                node_id+=1               
                node_id=self.recurse_node(child,node_id,id_offset,node_list, output_node.node_id, depth)
        else:
            # this is a terminal 
            output_node.node_type = 3
        node_id+=1
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
        return node_id

    def parse(self, bracket_parse):        
        parser = self.get_bracket_parser()
        stuff = parser.parse( bracket_parse )[0]   
        #print(stuff)             
        currentNode = stuff.Node[0]
        node_list = []
        self.recurse_node( currentNode, 1, 0, node_list, -1, 0 )        
        node_list = sorted(node_list, key=attrgetter('start_bracket'))
        return node_list

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
            
    def reset_filter(self):
        self.filter = [i for i in range( len(self.trees) )]
                            
    def add_filter(self,filter):
        self.filter = self.filter & filter

def stuff():
    pass
    
# some testing
corpus = """( (IP-MAT (NP-SBJ (NPR-N Halldór-halldór))
  (VBDI hét)
  (NP-PRD (NP (ONE-N einn) (ADJ-N ríkur) (N-N maður))
      (CONJP (CONJ og)
         (NP (N-N vinur)
             (NP-POS (NPR-G Haralds)
                 (NP-PRN (N-G konungs-konungur))))))
  (. .-.) (ID 1275.MORKIN.NAR-HIS,.2)))"""

parser = BracketParser()
corpus = corpus.replace('\n',' ');
node_list = parser.parse( corpus )
#print(len(node_list))
#print( "id\tstart\tend\ttype\tpar_id\tlabel" )
for output_node in node_list:   
    print( str(output_node.node_id) + "\t" + str(output_node.start_bracket) + "\t" + str(output_node.end_bracket) + "\t" + str(output_node.depth) + "\t" + str(output_node.node_type) + "\t" + str(output_node.parent_id) + "\t" + output_node.label + "\t" + str(output_node.lemma) )
    

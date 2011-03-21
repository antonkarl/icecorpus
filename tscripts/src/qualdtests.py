import unittest
from qald import BracketParser

class ParsingBrackets(unittest.TestCase):
    tree = """( (IP-MAT (NP-SBJ (NPR-N Halldór-halldór))
      (VBDI hét)
      (NP-PRD (NP (ONE-N einn) (ADJ-N ríkur) (N-N maður))
          (CONJP (CONJ og)
             (NP (N-N vinur)
                 (NP-POS (NPR-G Haralds)
                     (NP-PRN (N-G konungs-konungur))))))
      (. .-.) (ID 1275.MORKIN.NAR-HIS,.2)))"""
        
    
    def testParse(self):                          
        """There should be some output from the parser"""
        parser = BracketParser()
        tree = self.tree.replace('\n',' ');
        #stuff = phrase.parse( corpus )[0]
#        currentNode = stuff.Node[0]                        
        parse_output = parser.parse( tree )           
        assert parse_output is not None

    def testLemmaParse(self):
        """Check some known lemmas"""
        parser = BracketParser()
        tree = self.tree.replace('\n',' ');
        #stuff = phrase.parse( corpus )[0]
#        currentNode = stuff.Node[0]                        
        parse_output = parser.parse( tree )
        print(parse_output)
        print(  len(parse_output) )                
        for node in parse_output:
            if( node.node_id == 44 ):
                assert( node.lemma == "konungur")
            if( node.node_id == 39 ):
                assert( node.lemma == None )
            if( node.node_type == 1 ):
                assert( node.lemma == None )
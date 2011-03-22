import unittest
import re
from qald import BracketParser

class ParsingBrackets(unittest.TestCase):
    bracket_tree = """( (IP-MAT (NP-SBJ (NPR-N Halldór-halldór))
  (VBDI hét)
  (NP-PRD (NP (ONE-N einn) (ADJ-N ríkur) (N-N maður))
      (CONJP (CONJ og)
         (NP (N-N vinur)
             (NP-POS (NPR-G Haralds)
                 (NP-PRN (N-G konungs-konungur))))))
  (. .-.) ) (ID 1275.MORKIN.NAR-HIS,.2) )"""
      
    def testParseAgainstNoOutput(self):                          
        """There should be some output from the parser"""
        parser = BracketParser()                
        tree = parser.parse( self.bracket_tree )           
        assert tree is not None

    def testParseConversions(self):                          
        """Parsed tree should be the same as original when converted back"""
        parser = BracketParser()
        tree = parser.parse( self.bracket_tree )
        newbrackets = tree.to_brackets()
        # print(newbrackets)
        newbrackets = re.sub(r"\s+", "", newbrackets )
        oldbrackets = re.sub(r"\s+", "", self.bracket_tree )        
        #print( newbrackets )
        #print( oldbrackets )
        assert newbrackets == oldbrackets     
        
    def testRoundTripParseConversions(self):
        """Two rounds of conversion between brackets and internal format"""
        parser = BracketParser()        
        oldbrackets = re.sub(r"\s+", "", self.bracket_tree )                
        newbrackets = parser.parse( parser.parse( self.bracket_tree ).to_brackets() ).to_brackets()
        newbrackets = re.sub(r"\s+", "", newbrackets )
        assert newbrackets == oldbrackets

        """With id offest: Two rounds of conversion between brackets and internal format"""
        parser = BracketParser()        
        oldbrackets = re.sub(r"\s+", "", self.bracket_tree )                
        newbrackets = parser.parse( parser.parse( self.bracket_tree, 5 ).to_brackets(), 10 ).to_brackets()
        newbrackets = re.sub(r"\s+", "", newbrackets )
        assert newbrackets == oldbrackets
        

    def testLemmaParse(self):
        """Check some known lemmas"""
        parser = BracketParser()
        tree = self.bracket_tree.replace('\n',' ');
        #stuff = phrase.parse( corpus )[0]
#        currentNode = stuff.Node[0]                        
        tree = parser.parse( tree )                    
        for node in tree.node_list:
            if( node.node_id == 44 ):
                assert( node.lemma == "konungur")
            if( node.node_id == 39 ):
                assert( node.lemma == None )
            if( node.node_type == 1 ):
                assert( node.lemma == None )
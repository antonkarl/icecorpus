# Converts table format to plain text 

def is_empty( label ):
    if label[0] == "*":
        return True
    if label[0] == "0":
        return True
    if label[0] == "{":
        return True
    if label[0] == "<":
        return True
    if is_id(label):
        return True
    
    return False


def is_id( label ):
    # horrible, but works
    return len( label.split(".") ) == 5  and len( label.split(",") ) == 2 
     

def make_text_version( datfile_path ):
    tablefile = open( datfile_path ,"r")
    lines = tablefile.readlines()
    output = ""
    for node in lines:
        chunks = node.split("\t")
        if len(chunks) == 8:
            type = int(chunks[4])
            depth = int(chunks[5])
            label = chunks[6]
            lemma = chunks[7]
        
            if type == 3 and not is_empty(label):
                output += label + " "
                #print( label + " ", end="" )
                    
            if depth == -1:
                output = output.strip() + "\n"        
        
    output = output.replace("$ $","")
    print( output.strip() )
    
def make_wordlist( datfile_path ):
    tablefile = open( datfile_path ,"r")
    lines = tablefile.readlines()
    output = ""
    for node in lines:
        chunks = node.split("\t")
        if len(chunks) == 8:
            type = int(chunks[4])
            parent = int(chunks[5])
            label = chunks[6]
            lemma = chunks[7]

            if type == 3 and not is_empty(label):
                output += label + " "
                #print( label + " ", end="" )
                    
            if parent == -1:
                output = output.strip() + "\n"        
        
    output = output.replace("$ $","")
    print( output.strip() )    
    
#make_text_version("sentences.dat")    
make_text_version("sturlunga.dat")
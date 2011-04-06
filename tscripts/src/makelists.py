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
     

path = "/home/anton/icecorpus/tscripts/src/icepahc.dat"

file = open(path)
lines = file.readlines()

labels = {}
lemmas = {}
for line in lines:
    chunks = line.split("\t")
    
    lab = chunks[9]
    lemma = chunks[10]
    type = int(chunks[6])
    
    if not is_id(lab) and not type == 3:
        if lab in labels:
            labels[lab] += 1
        else:
            labels[lab] = 1

output = ""
for idx, label in enumerate( sorted(labels.keys()) ):    
    output += str(idx) + "\t"+ label.strip() + "\t" + str(labels[label]) + "\n"


print( output )


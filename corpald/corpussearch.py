# Corpus
import re

class CSQuery:
    node="$ROOT"
    definitions=None
    remark=None
    nodes_only=False
    remove_nodes=False
    print_indices=False
    print_complement=False    
    query=""        
   
    def load(self, filename):
        # print("loading")
        query_file = open(filename, "r")
        file_contents = query_file.read()
        # print("filecon: \n\n"+file_contents)
        #if re.search("begin\_remark:([.\n]*)end\_remark", file_contents):
        rematch = "begin\_remark:\n(.*)\nend_remark"
        if re.search(rematch, file_contents):
            # print("in restuff")
            remarkSection = re.search(rematch, file_contents).group(0)
            self.remark = re.search(rematch, file_contents).group(1).replace("\n", "; ").strip()
            file_contents = file_contents.replace(remarkSection, "\n")
        
        lines = file_contents.split("\n")
        inquery = False
        for line in lines:
            # print("line >>" + line +"<<")
            chunks = line.split(":")
            # print("chunks "+ str(len(chunks)) )
            if inquery:
                self.query = self.query + "\n" + line.strip()                        
            elif len(chunks) == 2:
                chunks[1] = chunks[1].strip()
                if chunks[1] == "T" or chunks[1] == "t" or chunks[1] == "TRUE":
                    chunks[1] = "true"
                elif chunks[1] == "F" or chunks[1] == "t" or chunks[1] == "FALSE":
                    chunks[1] = "true"                    
                chunks[0] = chunks[0].strip()
                
                if chunks[0] == "node":
                    self.node = chunks[1]
                elif chunks[0] == "nodes_only":
                    self.nodes_only = (chunks[1] == "true")
                elif chunks[0] == "remove_nodes":
                    self.remove_nodes = (chunks[1] == "true")
                elif chunks[0] == "print_indices":
                    self.print_indices = (chunks[1] == "true")
                elif chunks[0] == "print_complement":
                    self.print_complement = (chunks[1] == "true")
                elif chunks[0] == "define":
                    self.definitions = chunks[1]                    
                elif chunks[0] == "query":
                    self.query = chunks[1]
                    inquery = True

            
    def save(self,  filename):
        outputfile = open(filename, "w")
        outputfile.write(self.query_text())
        
    def query_text(self):
        output = "node: " + self.node + "\n"        
        if self.remark:
            output = output + "begin_remark:\n\t"+self.remark+"\nend_remark\n"
        if self.definitions:
            output = output + "define: " + self.definitions + "\n"
        if self.nodes_only:
            output = output + "nodes_only: true" + "\n"
        if self.remove_nodes:
            output = output + "remove_nodes: true" + "\n"
        if self.print_indices:
            output = output + "print_indices: true" + "\n"
        if self.print_complement:
            output = output + "print_complement: true" + "\n"        
        output=output+"\nquery: " + self.query.replace("\n", "\n       ")
        return output

    

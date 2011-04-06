import sqlite3
import glob



conn = sqlite3.connect('icepahc-sql')

c = conn.cursor()

c.execute('drop table corpus')
# Create table
c.execute('''create table corpus
   (text_id integer, sentence_id integer,
    node_id integer, start_bracket integer,
    end_bracket integer, depth integer,
    type integer, idx integer,
    parent integer, label text,
    lemma text)''')

path = "/home/anton/icecorpus/tscripts/src/table/11xx.f*.dat"
allfiles = glob.glob( path )
for idx, filename in enumerate(allfiles):
    print("doing file " + str(idx) + " " + filename )
    file = open(filename)
    lines = file.readlines()
    for line in lines:        
        line = line.replace("\t\t","\t0\t")        
        line = line.replace("\t\n","\t0")        
        chunks = line.strip().split("\t")
                
        if len(chunks) == 10:
            chunks = (line+"\t0").split("\t")
        #print(chunks)
        # Insert a row of data
        #c.execute("insert into corpus values ('"+chunks[0]+"','"+chunks[1]+"','"+chunks[2]+"','"
        #      +chunks[3]+"','"+chunks[4]+"','"+chunks[5]+"','"+chunks[6]+"','"
        #      +chunks[7]+"','"+chunks[8]+"','"+chunks[9]+"')")
        c.execute("insert into corpus values (?,?,?,?,?,?,?,?,?,?,?)",chunks)

# Save (commit) the changes
conn.commit()
# We can also close the cursor if we are done with it
c.close()
print("done")


import sys
import re

f = open(sys.argv[1]+".ppsd", 'r')
currentText = f.read()

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ.$'
enCase = {'n':'N','o':'A','þ':'D','e':'G'}
lemmas={}
modal = "skulu|munu|mega|vilja|geta"

#def rep( before, after ):
#	global currentText 
#	currentText = re.sub( before, after, currentText )

def   get_john( word ):

    # foreign words
    if hinn == "hinn":
        print ("FW")


def treebank_tag( icenlp_tag ):


    # injp
    if icenlp_tag == "au":
        return "INTJ"

    # adverbs
    if icenlp_tag == "aa":
        return "ADV"
    if icenlp_tag == "aam":
        return "ADVR"
    if icenlp_tag == "aae":
        return "ADVS"

    # prepositions
    if re.match( "a[oþe]", icenlp_tag ):
        return "P"

    # infinitival marker
    if icenlp_tag == "cn":
        return "TO"

    # numbers
    if re.match( "t[anoþe]", icenlp_tag):
        case = re.search("t([anoþe])",icenlp_tag).group(1)
        if case == "a":
            case = "n"
        return "NUM-"+enCase[case]

    if re.match( "t[a-z]{3}[noþe]", icenlp_tag):
        case = re.search("t[a-z]{3}([noþe])",icenlp_tag).group(1)
        return "NUM-"+enCase[case]

    # nouns
    if re.match("n[a-zþ\-]{3,5}", icenlp_tag):
        nounTag = "N"
        if re.match("n[a-zþ\-]{5}", icenlp_tag):
            nounTag = nounTag + "PR"
        if re.match("n[a-z]f[a-zþ\-]{1,3}", icenlp_tag):
            nounTag = nounTag + "S"
        nounTag = nounTag+"-"+enCase[icenlp_tag[3]]
        return nounTag

    # determiners
    if icenlp_tag.startswith("g"):
        detTag = "D"
        detTag = detTag+"-"+enCase[icenlp_tag[3]]
        return detTag

    if icenlp_tag.startswith("f"):
        proTag = "PRO"
        proTag = proTag +"-"+enCase[icenlp_tag[4]]
        return proTag

    # verbs
    if icenlp_tag == "slg":
        return "VAG"
    if icenlp_tag.startswith("sb"):
        return "VBI"
    if re.match("sn[gm]", icenlp_tag):
        return "VB"
    if re.match("ss[gm]", icenlp_tag):
        return "VBN"
    if re.match("sþ[a-zþ]{4}",icenlp_tag):
        return "VAN"
    if re.match("sf[a-z1-3]{3}n",icenlp_tag):
        return "VBPI"
    if re.match("sf[a-z1-3]{3}þ",icenlp_tag):
        return "VBDI"
    if re.match("sv[a-z1-3]{3}n",icenlp_tag):
        return "VBPS"
    if re.match("sv[a-z1-3]{3}þ",icenlp_tag):
        return "VBDS"

    # adjectives
    if re.match("l[a-zþ]{5}",icenlp_tag):
        adjtag="ADJ"
        if re.match("l[a-zþ]{4}m",icenlp_tag):
            adjtag=adjtag+"R"
        if re.match("l[a-zþ]{4}e",icenlp_tag):
            adjtag=adjtag+"S"
        adjtag=adjtag+"-"+enCase[icenlp_tag[3]]
        return adjtag
    
    return icenlp_tag

def get_lemma(word,tag):
	if word+"-"+tag in lemmas:
		return lemmas[word+"-"+tag]
	else:
		return word

def convert_tag( match ):
        tagPattern="(["+allchars+"\_\-0-9]+) (["+allchars+"\_\-0-9]+)"
        theTag = re.search(tagPattern,match.group()).group(1)
        theWord = re.search(tagPattern,match.group()).group(2)
        theLemma = get_lemma(theWord,theTag)

        # check for 2n person clitic
        if re.match("s[a-z]{2}2[a-zþ]{2}",theTag) and re.match("['"+allchars+"']+(ðu|du|tu)$",theWord):
            verbstem = re.search("(['"+allchars+"']+)(ðu|du|tu)$",theWord).group(1)
            clitic = re.search("(['"+allchars+"']+)(ðu|du|tu)$",theWord).group(2)
            # print(theWord + " "+theTag)
            return "("+treebank_tag(theTag)+" "+verbstem+"$-"+theLemma+") (NP-SBJ (PRO-N $"+clitic+"-þú))"
            
        # check for suffixed determiner
        determiner=None
        detmatch1="(["+allchars+"]+)(inn|inum|ins|inir|ina|inna|in|inni|innar|inar|ið|inu)$"
        detmatch2="(["+allchars+"]+)(num|ns|nir|nna|nn|nni|n{1,2}ar|ð|nu)$"
        detmatch3="(["+allchars+"]+)(n|na)$"
        if re.match("n[a-zþ]{3}g[a-zþ]*",theTag) and (re.match(detmatch1,theWord) or re.match(detmatch2,theWord)):
            # there is a determiner
            currentMatch = None
            if re.match(detmatch1,theWord):
                currentMatch = detmatch1
            elif re.match(detmatch2,theWord):
                currentMatch = detmatch2
            elif re.match(detmatch3,theWord):
                currentMatch = detmatch3

#            print(theWord + " "+theTag)
            determiner = re.search(currentMatch,theWord).group(2)
            theWord = re.search(currentMatch,theWord).group(1)

        theTag = treebank_tag(theTag)
#        if( theWord == "." ):
#               return "(. .)"
        if determiner == None:
            output = "("+theTag+" "+theWord+"-"+theLemma+")"
        else:
            chunks = theTag.split("-")
            output = "("+theTag+" "+theWord+"$-"+theLemma+") (D-"+chunks[1]+" $"+determiner+"-hinn)"
        return output

# Open input file for reading

def remove_extra_ipsd_stuff():
    # Remove extra stuff
    rep("[\<\>]","")
    rep("MWE\_","")

    rep("\{\*TIMEX ","")
    rep("\*TIMEX\}","")
 #   rep("\{\*COMP ","")
 #   rep("\*COMP\}","")
    rep("\[NPs","[NP")
    rep("NPs\]","NP]")
    rep("\[APs","[AP")
    rep("APs\]","AP]")
    rep("\[VPs","[VP")
    rep("VPs\]","VP]")


def load_lemmas():
    # Read lemmas from file
    lemmaFile=open(sys.argv[1]+".lemmatized",'r')
    lines=lemmaFile.readlines()
    for line in lines:
            chunks=line.split(" ")
            if len(chunks)>2:
                    theLemma = chunks[2].strip().lower()
                    theLemma = theLemma.replace("(","")
                    theLemma = theLemma.replace(")","")
                    lemmas[chunks[0]+"-"+chunks[1]]=theLemma


def convert_iceparser_functions():
    # Open syntactic function bracket
    rep("\{\*OBJAP* \[NP","(NP-OB1")
    rep("\{\*OBJNOM* \[NP","(NP-OB1")
    rep("\{\*SUBJ* \[NP","(NP-SBJ")
    rep("\{\*OBJ* \[NP","(NP-OB1")
    rep("\{\*IOBJ* \[NP","(NP-OB2")
    rep("\{\*COMP* \[NP","(NP-PRD")

    # Close syntactic function bracket
    rep("\*(SUBJ|OBJ|OBJAP|IOBJ|COMP|OBJNOM)*\}","")

    # Throw away remaining opening brackets
    rep("\{\*(SUBJ|OBJ|IOBJ|COMP)","")

    # NP-POS
    rep("\{\*QUAL \[NP","(NP-POS")
    rep(" NP\] \*QUAL\}",")")

def convert_brackets_to_pars():
    # Convert brackets to parenthteses
    rep("\[","(")
    rep(" [A-Za-z_]+\]",")")

def parenthesize_punctuation():
    rep("\. \.","(. .)")
    rep("\, \,","(, ,-,)")
    rep("\: \:","(, :-:)")
    rep("\; \;","(. ;-;)")
    rep("\! \!","(. !-!)")
    rep("\? \?","(. ?-?)")
    rep("\- \-","(, -)")
    rep("\" \"","(\" \")")

def convert_phrase_labels():
    # Make Phrase labels uppercase
    rep("\(AdvP","(ADVP")
    rep("\(InjP","(INTJP")
    rep("\(VPi","(IP-INF")
    rep("\(VPp","(VP")
    rep("\(VPb","(VP")
    rep("\(VPg","(VP")
    rep("\(VPs","(VP")
    # Rename some phrase labels
    rep("\(AP","(ADJP")
    
def make_tag_word_pars():
    # Make tag+word parentheses
    global currentText
    currentText = re.sub("\( (["+allchars+"\-0-9]+) \(  (["+allchars+"0-9\_\-—]+) (["+allchars+"0-9\_\-]+)","(\\1 (\\3 \\2)",currentText)
    while re.search("\)[ ]{1,2}(["+allchars+"0-9\_\-—]+) (["+allchars+"0-9\_\-]+)", currentText):
            currentText = re.sub("\)[ ]{1,2}(["+allchars+"0-9\_\-—]+) (["+allchars+"0-9\_\-]+)",") (\\2 \\1)",currentText)

def add_ip_mat():
    global currentText
    currentText = re.sub("\)[ ]{0,1}\n\n\(",")))\n\n((IP-MAT (",currentText)
    currentText = "((IP-MAT " + currentText.strip() + "))"

def split_determiners():
    global currentText
    nounMatch = '\(n([a-z]{3})g[a-z]* (['+allchars+']+)(inn|inum|ins|inir|ina|inna|in|inni|innar|inar|ið|inu)-(['+allchars+']+)\)'
    nounMatch2 = '\(n([a-z]{3})g[a-z]* (['+allchars+']+)(num|ns|nir|n{1,2}a|n{1,2}|nni|n{1,2}ar|ð|nu)-(['+allchars+']+)\)'

def convert_tags_to_icepahc():
    # Convert tags from icenlp format to icepahc format
    global currentText
    tagMatch = re.compile("\((["+allchars+"\_\-0-9]+) (["+allchars+"\_\-0-9]+)\)")
    currentText = tagMatch.sub( convert_tag, currentText )

def replace_special_verb_tags():
    global currentText
    # infinitives
    currentText = re.sub("\(VB (["+allchars+"]+)\-vera\)","(BE \\1-vera)", currentText)
    currentText = re.sub("\(VB (["+allchars+"]+)\-(gera|gjöra)\)","(DO \\1-gera)", currentText)
    currentText = re.sub("\(VB (["+allchars+"]+)\-verða\)","(RD \\1-verða)", currentText)
    currentText = re.sub("\(VB (["+allchars+"]+)\-hafa\)","(HV \\1-hafa)", currentText)    
    currentText = re.sub("\(VB (["+allchars+"]+)\-("+modal+")\)","(MD \\1-\\2)", currentText)

    # present participle
    currentText = re.sub("\(VAG (["+allchars+"]+)\-vera\)","(BAG \\1-vera)", currentText)
    currentText = re.sub("\(VAG (["+allchars+"]+)\-(gera|gjöra)\)","(DAG \\1-gera)", currentText)
    currentText = re.sub("\(VAG (["+allchars+"]+)\-verða\)","(RAG \\1-verða)", currentText)
    currentText = re.sub("\(VAG (["+allchars+"]+)\-hafa\)","(HAG \\1-hafa)", currentText)    

    # passive participle
    currentText = re.sub("\(VAN (["+allchars+"]+)\-hafa\)","(HAN \\1-hafa)", currentText)
    currentText = re.sub("\(VAN (["+allchars+"]+)\-verða\)","(RDN \\1-verða)", currentText)
    currentText = re.sub("\(VAN (["+allchars+"]+)\-(gera|gjöra)\)","(DAN \\1-gera)", currentText)
    currentText = re.sub("\(VAN (["+allchars+"]+)\-(koma)\)","(VBN \\1-koma)", currentText)

    # perfect participle
    currentText = re.sub("\(VBN (["+allchars+"]+)\-vera\)","(BEN \\1-vera)", currentText)
    currentText = re.sub("\(VBN (["+allchars+"]+)\-verða\)","(RDN \\1-verða)", currentText)
    currentText = re.sub("\(VBN (["+allchars+"]+)\-(gera|gjöra)\)","(DON \\1-gera)", currentText)
    currentText = re.sub("\(VBN (["+allchars+"]+)\-hafa\)","(HVN \\1-hafa)", currentText)

    # imperative
    currentText = re.sub("\(VBI (["+allchars+"]+)\-vera\)","(BEI \\1-vera)", currentText)
    currentText = re.sub("\(VBI (["+allchars+"]+)\-(gera|gjöra)\)","(DOI \\1-gera)", currentText)
    currentText = re.sub("\(VBI (["+allchars+"]+)\-verða\)","(RDI \\1-verða)", currentText)
    currentText = re.sub("\(VBI (["+allchars+"]+)\-hafa\)","(HVI \\1-hafa)", currentText)
    currentText = re.sub("\(VBI (["+allchars+"]+)\-("+modal+")\)","(MDI \\1-\\2)", currentText)

    # present and past (including subjunctive)
    currentText = re.sub("\(VB([PD])([IS]) (["+allchars+"]+)\-vera\)","(BE\\1\\2 \\3-vera)", currentText)
    currentText = re.sub("\(VB([PD])([IS]) (["+allchars+"]+)\-(gera|gjöra)\)","(DO\\1\\2 \\3-gera)", currentText)
    currentText = re.sub("\(VB([PD])([IS]) (["+allchars+"]+)\-hafa\)","(HV\\1\\2 \\3-hafa)", currentText)
    currentText = re.sub("\(VB([PD])([IS]) (["+allchars+"]+)\-verða\)","(RD\\1\\2 \\3-verða)", currentText)
    currentText = re.sub("\(VB([PD])([IS]) (["+allchars+"]+)\-("+modal+")\)","(MD\\1\\2 \\3-\\4)", currentText)
    
    #reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-vera\)"]="(BED\\1 \\2-vera)"  # BED 	BE, past (including past subjunctive)
    #reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-vera\)"]="(BEP\\1 \\2-vera)"  # BEI 	BE, present (including present subjunctive)


# This renames stuff and builds/removes some pieces of structure
def final_replacements():
    global currentText

    # ONE 	the word ONE (except as focus particle)
    currentText = re.sub("\((NUM|ADJ|PRO)-([NADG] ["+allchars+"]+-einn)\)","(ONE-\\2)",currentText)

    # samur
    currentText = re.sub("\((PRO)-([NADG] ["+allchars+"]+-samur)\)","(ADJ-\\2)",currentText)

    # hinn
    currentText = re.sub("\(PRO-(N) ([Hh]inn)-hinn\)","(D-\\1 \\2-hinn)",currentText)


    # NEGATION
    currentText = re.sub("\(ADVP \(ADV ([Ee]kki|[Ee]igi|[Ee]i)-(ekki|eigi|ei)\)\)","(NEG \\1-\\2)",currentText)
    # CONJUNCTIONS
    currentText = re.sub("\(CP \(C ([Oo]g|[Ee]n|[Ee]ða|[Ee]ður|[Ee]llegar|[Hh]eldur|[Ee]nda)-([Oo]g|[Ee]n|[Ee]ða|[Ee]ður|[Ee]llegar|[Hh]eldur|[Ee]nda)\)\)","(CONJ \\1-\\2)",currentText)
    rep("\(SCP \(C bæði\-bæði\)\)","(CONJ bæði-bæði)")
    rep("\(CP \(C né-né\)\)","(CONJ né-né)")
    # Quantifiers
    rep("\(PRO-([A-Z]) (["+allchars+"]+)-(allur|báðir|nokkur|enginn|sumur|fáeinir|fár|einhver|neinn|ýmis)\)","(Q-\\1 \\2-\\3)")
    # Demonstratives
    rep("\(PRO-([A-Z]) (["+allchars+"]+)-(hinn)\)","(D-\\1 \\2-\\3)")

    # WQ
    rep("\(PRO-([A-Z]) (["+allchars+"]+)-(hvor)\)","(Q-\\1 \\2-\\3)")


    # Make sjálfur -PRN
    # (NP-SBJ (PRO-N sjálfur-sjálfur))
    rep("\(NP-SBJ \(PRO-([A-Z]) (["+allchars+"]+)-(sjálfur)\)\)","(NP-PRN (PRO-\\1 \\2-\\3))")
    rep("\(PRO-([A-Z]) (["+allchars+"]+)-(sjálfur)\)","(NP-PRN (PRO-\\1 \\2-\\3))")
    rep("\(NP-PRN \(NP-PRN \(PRO-([A-Z]) (["+allchars+"]+)-(sjálfur)\)\)\)","(NP-PRN (PRO-\\1 \\2-\\3))")

    # Focus particle
    rep("\(ADVP \(ADV aðeins-aðeins\)\)","(FP aðeins-aðeins)")
    rep("\(ADV aðeins-aðeins\)","(FP aðeins-aðeins)")

    # ALSO
    rep("\(ADVP \(ADV líka-líka\)\)","(ALSO líka-líka)")
    rep("\(ADVP \(ADV einnig-einnig\)\)","(ALSO einnig-einnig)")

    # heldur
    rep("\(CONJ heldur-heldur\)","(ADVP (ADVR heldur-heldur))")

    # negation, ekki and eigi
    rep("\(ADV ekki-ekki\)","(NEG ekki-ekki)")
    rep("\(NEG eigi-eigi\)","(NEG eigi-ekki)")
    rep("\(ADV eigi-eigi\)","(NEG eigi-ekki)")
    rep("\(ADV Eigi-eigi\)","(NEG Eigi-ekki)")
    rep("\(ADV Ekki-ekki\)","(NEG Ekki-ekki)")
    rep("\(NEG Eigi-eigi\)","(NEG Eigi-ekki)")

    # relative clauses
    rep("\(SCP \(CT ([Ss])em-sem\)\)","(CP-REL (WNP 0) (C \\1em-sem))")
    rep("\(SCP \(CT er-er\)\)","(CP-REL (WNP 0) (C er-er))")

    # margur and mikill
    rep("\(ADJ-([NADG]) ([Mm][aö]rg[a-z]+)-margur\)","(Q-\\1 \\2-margur)")
    rep("\(ADJR-([NADG]) ([Ff]leir[a-z]+)-margur\)","(QR-\\1 \\2-margur)")
    rep("\(ADJS-([NADG]) ([Ff]lest[a-z]+)-(margur|fles[a-z]+)\)","(QS-\\1 \\2-margur)")
    rep("\(ADJ-([NADG]) ([Mm]iki[a-zð]+)-mikill\)","(Q-\\1 \\2-mikill)")
    rep("\(ADJR-([NADG]) ([Mm]eir[a-z]+)-mikill\)","(QR-\\1 \\2-mikill)")
    rep("\(ADVR ([Mm]eir[a-z]*)-meira\)","(QR-N \\1-mikill)")
    rep("\(ADJS-([NADG]) ([Mm]est[a-z]+)-mikill\)","(QS-\\1 \\2-mikill)")

    # einhver
    rep("\(Q-([NADG]) (einhve[a-z]+)-einhver\)","(ONE+Q-\\1 \\2-einhver)")

    # demonstratives
    rep("\(PRO-([NADG]) (["+allchars+"]+-sá)\)","(D-\\1 \\2)")
    rep("\(PRO-([NADG]) (["+allchars+"]+-þessi)\)","(D-\\1 \\2)")

    # OTHER
    rep("\(PRO-([NADG] ["+allchars+"]+-annar)\)","(OTHER-\\1)")

    # eins og
    rep("\(ADV eins-eins\)","(ADVR eins-eins)")
    rep("\(CP \(ADVR eins-eins\) \(C og-og\)\)","(ADVP (ADVR eins) (PP (P og)))")

    # til (þess) að
    #(CP (P til-til) (TO að-að))
    #(CP (P til-til) (PRO-G þess-það) (TO að-að))
    rep("\(CP \(P til-til\) \(TO að-að\)\)","(PP (P til-til) (TO að-að))")
    rep("\(CP \(P til-til\) \(PRO-G þess-það\)","(PP (P til-til) (PRO-G þess-það)")
    rep("\(PP \(P til-til\) \(PRO-G þess-það\) \(TO að-að\)\)","(PP (P til-til) (NP (PRO-G þess-það)) (IP-INF-PRP (C að-að)))")
    #  (PP (P til-til) (PRO-G þess-það) (TO að-að))

    # (af) því að
    rep("\(CP \(ADV því-því\) \(C að-að\)\)","(PP (P 0) (NP (PRO-D því-það) (CP-THT-PRN (C að-að))))")
    rep("\(CP \(PRO-D því-það\) \(C að-að\)\)","(PP (P 0) (NP (PRO-D því-það) (CP-THT-PRN (C að-að))))")
    rep("\(CP \(P af-af\) \(PRO-D því-það\) \(C að-að\)\)","(PP (P af-af) (NP (PRO-D því-það) (CP-THT-PRN (C að-að))))")
       #(CP (P af-af) (PRO-D því-það) (C að-að))

    # þótt að
    rep("\(CP \(ADV þó-þó\) \(C að-að\)\)","(PP (P þó-þó) (CP-ADV (C að-að)))")
    rep("\(CP \(ADV þótt-þótt\) \(C að-að\)\)","(PP (P þótt-þótt) (CP-ADV (C að-að)))")

    # svo að
    rep("\(CP \(ADV svo-svo\) \(C að-að\)\)","(PP (P svo-svo) (CP-ADV (C að-að)))")
    rep("\(CP \(ADV þar-þar\) \(C sem-sem\)\)","(CP-REL (ADV þar-þar) (C sem-sem))")

    # svo sem 
    rep("\(ADV svo-svo\) \(ADV sem-sem\)","(ADV svo-svo) (C sem-sem)")

    # more
    rep("\(SCP ","(CP-ADV ")
    rep("\(CP-ADV \(C að-að\)\)","(CP-THT (C að-að))")

    # fix þótt að
    rep("\(PP \(P þó-þó\) \(CP-THT \(C að-að\)\)\)","(PP (P þó-þó) (CP-ADV (C að-að)))")
    rep("\(PP \(P Þó-þó\) \(CP-THT \(C að-að\)\)\)","(PP (P Þó-þó) (CP-ADV (C að-að)))")
    rep("\(CP-ADV \(C þótt-þótt\)\)\n\(CP-THT \(C að-að\)\)","(PP (P þótt-þótt) (CP-ADV (C að-að)))")
    rep("\(CP-ADV \(C Þótt-þótt\)\)\n\(CP-THT \(C að-að\)\)","(PP (P Þótt-þótt) (CP-ADV (C að-að)))")

    # ef að
    rep("\(CP-ADV \(C ef-ef\)\)\n\(CP-THT \(C að-að\)\)","(PP (P ef-ef) (CP-ADV (C að-að)))")
    rep("\(CP-ADV \(C Ef-ef\)\)\n\(CP-THT \(C að-að\)\)","(PP (P Ef-ef) (CP-ADV (C að-að)))")

    # ADVP-TMP
    currentText = re.sub("\(ADVP \(ADV ([Þþ]á|[Nn]ú|[Áá]ður|[Ææ]tíð|[Aa]ldrei|[Aa]ldregi|[Áá]rla|[Áá]vallt|[Bb]rátt|[Ss]nemma|[Ll]oks|[Ll]oksins|[Oo]ft|[Oo]fvalt|[Ss]eint|[Ss]jaldan|[Ss]nemma|[Þþ]egar|[Ss]íðan)-(["+allchars+"]+)\)\)","(ADVP-TMP (ADV \\1-\\2))",currentText)

    # ADVP-LOC
    currentText = re.sub("\(ADVP \(ADV ([Þþ]ar|[Hh]ér|[Þþ]arna|[Hh]érna|[Hh]eima|[Uu]ppi|[Nn]iðri|[Vv]íða|[Óó]víða|[Aa]llvíða|[Úú]ti|[Ii]nni)-(["+allchars+"]+)\)\)","(ADVP-LOC (ADV \\1-\\2))",currentText)

    # ADVP-DIR
    currentText = re.sub("\(ADVP \(ADV ([Þþ]angað|[Hh]ingað|[Hh]eim|[Áá]leiðis|[Uu]pp|[Nn]iður|[Bb]urt|[Oo]fan|[Þþ]aðan)-(["+allchars+"]+)\)\)","(ADVP-DIR (ADV \\1-\\2))",currentText)

    # Shouldn't really be an ADV at this point, but just in case
    rep("\(ADV sem-sem\)","(C sem-sem)")

    # For some reason there is still a problem with SVO AÐ here, so fix it
    rep("\(PP \(P svo-svo\) \(CP-THT \(C að-að\)\)\)","(PP (P svo-svo) (CP-ADV (C að-að)))")

    #áður, which should be ADVR not ADV
    rep("\(ADV áður-áður\)","(ADVR áður-áður)")
    
    # Fix (VAN Það-þa)
    currentText = re.sub("\(VAN ([Þþ]að)-þa\)", "(NP-SBJ (PRO-N \\1-það))",currentText)

# Start script
# Load input file (ipsd)
#f = open(sys.argv[1]+".ppsd", 'r')
#currentText = f.read()

#load_lemmas() # ... into the lemmas dictionary
#remove_extra_ipsd_stuff() # ... like TIMEX
#convert_iceparser_functions() # ... like NP-SBJ
#convert_brackets_to_pars() # just simple "[" to "(" conversion
#parenthesize_punctuation() # before this command those do not have their own pars

# Fix foreign word "bug" and similar stuff
currentText = re.sub("\n(["+allchars+"]+) e\n","\n(e \\1)\n",currentText)
currentText = re.sub("\nað cn\n","\n(cn að)\n",currentText)
currentText = re.sub("\n(["+allchars+"]+) ft([a-z123]+)\n","\n(WPRO \\1)\n",currentText)

#make_tag_word_pars()
#add_ip_mat()
#convert_phrase_labels()
#split_determiners()
#convert_tags_to_icepahc()
#replace_special_verb_tags()
#final_replacements()

#rep("\([,;\.:?!] ([,;\.:?!]-[,;\.:?!][\)]+\n\n)","(. \\1")

# Write result to output file
#f = open(sys.argv[1]+".pppsd", 'w')
#f.write(currentText)
#f.close()

print(currentText)

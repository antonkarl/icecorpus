# This Python file uses the following encoding: utf-8

### Makes adjustments to .ipsd files as the last step in txt2ipsd-risamalheild.sh.

### Usage:
### python3 risamalheild_fix_abbreviations.py [input file] [output file]

### Created by Kristján Rúnarsson

import sys,re

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()
f.close()

wordchars = "A-Za-z0-9ÁáÐðÉéÍíÓóÚúÝýÞþÆæÖöØøÄäÜü"

# fix dashes inside words
# word-final dash (e.g. efnahags-)
# (ADJ-N efnahags99xCOM_dashx66-efnahags99xcom_dashx66)
output = re.sub(r"\(([A-Z0-9-]+) (["+wordchars+"]+)99xCOM_dashx66-(["+wordchars+"]+)99xcom_dashx66\)", r"(\1 \2<dash/>-\3)", output)
# mid-word dash (e.g. EFTA-ríkin)
output = re.sub(r"\(([A-Z0-9-]+) (["+wordchars+"]+)99xCOM_dashx66(["+wordchars+"]+)-(["+wordchars+"]+)99xcom_dashx66(["+wordchars+"]+)\)", r"(\1 \2<dash/>\3-\4<dash/>\5)", output)
# correct lemma for common words
output = re.sub(r"\([A-Z0-9-]+ efnahags<dash/>-efnahags\)", r"(NP-POS (N-G efnahags<dash/>-efnahagur))", output)

# change (CODE {COM:dash}) to (, <dash/>) and (CODE {COM:threedots}) to (, <threedots/>)
output = output.replace("(CODE {COM:dash})", "(, <dash/>)")
output = output.replace("(CODE {COM:threedots})", "(, <threedots/>)")

# resolve common abbreviations that were already parsed as a single token (including the final dot)
output = output.replace("(as t.d.-t.d.)", "(PP (P t.$-til) (NP (N-G $d.-dæmi)))")
output = output.replace("(as þ.e.-þ.e.)", "(IP-MAT-PRN (NP-SBJ (PRO-N þ.$-það)) (BEPI $e.-vera))")
output = output.replace("(as m.a.-m.a.)", "(PP (P m.$-meðal) (NP (OTHER-G $a.-annar)))")
output = output.replace("(as a.m.k.-a.m.k.)", "(PP (P a.$-meðal) (NP (ADJS-D $m.$-lítill) (N-D $k.-kostur)))")
output = output.replace("(as o.s.frv.-o.s.frv.)", "(CONJP (CONJ o.$-og) (ADVP (ADV $s.$-svo) (ADVP (ADV $frv.-framvegis))))")
output = output.replace("(as o.fl.-o.fl.)", "(CONJP (CONJ o.$-og) (NP (Q-N $fl.-mikill)))")
output = output.replace("(as þús.-þús.)", "(NUM-N þús.-þúsund)")
output = output.replace("(as kr.-kr.)", "(NS-N kr.-króna)")
output = output.replace("(as bls.-bls.)", "(N-D bls.-blaðsíða)")
output = output.replace("(as gr.-gr.)", "(N-N gr.-grein)")
output = output.replace("(as umr.-umr.)", "(N-N umr.-umræða)")
output = output.replace("(as mgr.-mgr.)", "(N-N mgr.-málsgrein)")
output = output.replace("(as nr.-nr.)", "(N-N nr.-númer)")
output = output.replace("(as km-km)", "(NS-N km-kílómetri)")
output = output.replace("(as m-m)", "(NS-N m-metri)")
output = output.replace("(as kl.-kl.)", "(N-N kl.$-klukka) (D-N $-hinn)")

# fix cardinals
output = re.sub(r"\(NUM-([A-Z0-9-]+) 0-0\)", r"(ONE-\1 0-núll)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 1-1\)", r"(ONE-\1 1-einn)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 2-2\)", r"(NUM-\1 2-tveir)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 3-3\)", r"(NUM-\1 3-þrír)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 4-4\)", r"(NUM-\1 4-fjórir)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 5-5\)", r"(NUM-\1 5-fimm)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 6-6\)", r"(NUM-\1 6-sex)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 7-7\)", r"(NUM-\1 7-sjö)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 8-8\)", r"(NUM-\1 8-átta)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 9-9\)", r"(NUM-\1 9-níu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 10-10\)", r"(NUM-\1 10-tíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 11-11\)", r"(NUM-\1 11-ellefu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 12-12\)", r"(NUM-\1 12-tólf)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 13-13\)", r"(NUM-\1 13-þrettán)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 14-14\)", r"(NUM-\1 14-fjórtán)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 15-15\)", r"(NUM-\1 15-fimmtán)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 16-16\)", r"(NUM-\1 16-sextán)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 17-17\)", r"(NUM-\1 17-sautján)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 18-18\)", r"(NUM-\1 18-átján)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 19-19\)", r"(NUM-\1 19-nítján)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 20-20\)", r"(NUM-\1 20-tuttugu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 30-30\)", r"(NUM-\1 30-þrjátíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 40-40\)", r"(NUM-\1 40-fjörutíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 50-50\)", r"(NUM-\1 50-fimmtíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 60-60\)", r"(NUM-\1 60-sextíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 70-70\)", r"(NUM-\1 70-sjötíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 80-80\)", r"(NUM-\1 80-áttatíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 90-90\)", r"(NUM-\1 90-níutíu)", output)
output = re.sub(r"\(NUM-([A-Z0-9-]+) 100-100\)", r"(NUM-\1 100-hundrað)", output)

# fix ordinals
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 1\.-1\.\)", r"(ADJ-\2 1.-fyrstur)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 2\.-2\.\)", r"(ADJ-\2 2.-annar)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 3\.-3\.\)", r"(ADJ-\2 3.-þriðji)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 4\.-4\.\)", r"(ADJ-\2 4.-fjórði)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 5\.-5\.\)", r"(ADJ-\2 5.-fimmti)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 6\.-6\.\)", r"(ADJ-\2 6.-sjötti)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 7\.-7\.\)", r"(ADJ-\2 7.-sjöundi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 8\.-8\.\)", r"(ADJ-\2 8.-áttundi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 9\.-9\.\)", r"(ADJ-\2 9.-níundi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 10\.-10\.\)", r"(ADJ-\2 10.-tíundi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 11\.-11\.\)", r"(ADJ-\2 11.-ellefti)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 12\.-12\.\)", r"(ADJ-\2 12.-tólfti)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 13\.-13\.\)", r"(ADJ-\2 13.-þrettándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 14\.-14\.\)", r"(ADJ-\2 14.-fjórtándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 15\.-15\.\)", r"(ADJ-\2 15.-fimmtándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 16\.-16\.\)", r"(ADJ-\2 16.-sextándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 17\.-17\.\)", r"(ADJ-\2 17.-sautjándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 18\.-18\.\)", r"(ADJ-\2 18.-átjándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 19\.-19\.\)", r"(ADJ-\2 19.-nítjándi)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 20\.-20\.\)", r"(ADJ-\2 20.-tuttugasti)", output)
output = re.sub(r"\((NUM|ADJ)-([A-Z0-9-]+) 30\.-30\.\)", r"(ADJ-\2 30.-þrítugasti)", output)

# fix tag for some other common abbreviations
output = re.sub(r"\(as ([Hh])v\.-háttvirtur\)", r"(ADJ-N \1v.-háttvirtur)", output)
output = re.sub(r"\(as ([Hh])æstv\.-hæstvirtur\)", r"(ADJ-N \1æstv.-hæstvirtur)", output)
output = re.sub(r"\(as ([Þþ])m\.-þingmaður\)", r"(NPR-N \1m.-þingmaður)", output)

# fix feminine nouns in -a with clitic article
# kvk. et. nf. mgr. (feminine singular nominative with clitic definite article)
output = re.sub(r"\(N-N (["+wordchars+"]+)an-\0a\)", r"(N-N \0a$-\0a) (D-N $n-hinn)", output)
# automatically covers this case also:
#output = output.replace(r"(N-N klukkan-klukka)", r"(N-N klukka$-klukka) (D-N $n-hinn)")
# kvk. et. þf. mgr. (feminine singular accusative with clitic definite article)
output = re.sub(r"\(N-A (["+wordchars+"]+)una-\0a\)", r"(N-N \0u$-\0a) (D-N $na-hinn)", output)
# with u-mutation on a single vowel
output = re.sub(r"\(N-A (["+wordchars+"]*)ö(["+wordchars+"]*)una-\0a\1a\)", r"(N-N \0ö\1u$-\0a\1a) (D-N $na-hinn)", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()

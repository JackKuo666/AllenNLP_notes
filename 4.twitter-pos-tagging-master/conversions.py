# convert PENN to universal POS

conversions = """
USR =>	X	twitter user
#	=>	.	_	#
$	=>	.	_	$, C$, US$, A$, HK$
''	=>	.	PunctSide=Fin|PunctType=Quot	'', '
,	=>	.	PunctType=Comm	,, 2, an
-LRB-	=>	.	PunctSide=Ini|PunctType=Brck	
-RRB-	=>	.	PunctSide=Fin|PunctType=Brck	
.	=>	.	PunctType=Peri	., ?, !
:	=>	.	_	--, :, ;, ..., -
AFX	=>	ADJ	Hyph=Yes	
CC	=>	CONJ	_	and, or, but, &, nor
CD	=>	NUM	NumType=Card	million, billion, one, two, three
DT	=>	DET	_	the, a, an, this, some
EX	=>	ADV	AdvType=Ex	there
FW	=>	X	Foreign=Foreign	de, perestroika, glasnost, vs., naczelnik
HYPH	=>	.	PunctType=Dash	
IN	=>	ADP	_	of, in, for, on, that
JJ	=>	ADJ	Degree=Pos	new, other, last, such, first
JJR	=>	ADJ	Degree=Cmp	more, higher, lower, less, better
JJS	=>	ADJ	Degree=Sup	most, least, largest, latest, best
LS	=>	.	NumType=Ord	3, 2, 1, 4, First
MD	=>	VERB	VerbType=Mod	will, would, could, can, may
NIL	=>	X	_	), }
NN	=>	NOUN	Number=Sing	%, company, year, market, share
NNP	=>	NOUN	Number=Sing	Mr., U.S., Corp., New, Inc.
NNPS	=>	NOUN	Number=Plur	Securities, Democrats, Americans, Brothers, Airlines
NNS	=>	NOUN	Number=Plur	years, shares, sales, companies, prices
PDT	=>	DET	AdjType=Pdt	all, such, half, both, nary
POS	=>	PRT	Poss=Yes	's, '
PRP	=>	PRON	PronType=Prs	it, he, they, I, we
PRP$	=>	DET	Poss=Yes|PronType=Prs	its, his, their, our, her
RB	=>	ADV	Degree=Pos	n't, not, also, only, as
RBR	=>	ADV	Degree=Cmp	more, earlier, less, higher, further
RBS	=>	ADV	Degree=Sup	most, best, least, hardest, Worst
RP	=>	PRT	_	up, out, off, down, in
SYM	=>	X	_	
TO	=>	VERB	PartType=Inf|VerbForm=Inf	to, na
UH	=>	PRT	_	yes, well, no, OK, oh
VB	=>	VERB	VerbForm=Inf	be, have, make, buy, get
VBD	=>	VERB	Tense=Past|VerbForm=Fin	said, was, were, had, did
VBG	=>	VERB	Aspect=Prog|Tense=Pres|VerbForm=Part	including, being, according, going, making
VBN	=>	VERB	Aspect=Perf|Tense=Past|VerbForm=Part	been, expected, made, based, sold
VBP	=>	VERB	Tense=Pres|VerbForm=Fin	are, have, do, say, 're
VBZ	=>	VERB	Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	is, has, says, 's, does
WDT	=>	PRON	PronType=Int,Rel	which, that, what, whatever, .what
WP	=>	PRON	PronType=Int,Rel	who, what, whom, whoever
WP$	=>	DET	Poss=Yes|PronType=Int,Rel	whose
WRB	=>	ADV	PronType=Int,Rel	when, how, where, why, whenever
``	=>	.	PunctSide=Ini|PunctType=Quot	``, `, non-``
"""

conversions = conversions.replace('\t', ' ')
lines = conversions.split("\n")
penn_to_universal = {}
for line in lines:
	tokens = line.split("=>")
	if len(tokens) > 1:
		universal_substring = tokens[1].strip()
		universal_substring = universal_substring[:universal_substring.index(' ')]
		penn_to_universal[tokens[0].strip()] = universal_substring

count = 0
with open("subset.txt") as data:
	with open("twitter_test.pos", 'w') as result_data:
		for line in data:
			if line.strip() == "":
				count += 1
			tokens = line.split()
			if len(tokens) == 2:
					if tokens[1] in penn_to_universal:
						line = tokens[0] + "\t" + penn_to_universal[tokens[1]]
						result_data.write(line + "\tNone\tNone\n")
			else:
				result_data.write(line)
print(set(penn_to_universal.values()))
print(len(set(penn_to_universal.values())))
print(count, "lines")


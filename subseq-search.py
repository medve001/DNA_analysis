'''
Testing way to find all substrings in a string
Restriction Analysis, promoter finding, etc.

To do:
1. ignoring spaces, numbers and other non-nucleotides 
2. Database of restriction sites
3. Formatting output; graphics, numbers, etc

'''


import re

rest_db = [("EcoRI", "gaattc", 1),
           ("KpnI", "ggtacc", 5),
           ("MluI", "acgcgt", 1),
           ("BamHI", "ggatcc", 1),
           ("PvuII", "cagctg", 3),
           ("HindIII", "aagctt", 1),]

def cleaning_seq(seq):
    clean_seq = []
    for i in seq:
        if i == 'a':
            clean_seq.append(i)
        elif i == 'c':
            clean_seq.append(i)
        elif i == 'g':
            clean_seq.append(i)
        elif i == 't':
            clean_seq.append(i)
        else:
            continue
    return clean_seq

def rest_analysis(string1, string2, pos):
    cuts = [m.start() + pos for m in re.finditer(string2, string1)]
    return cuts


# Getting sequence from text file
with open(input("File name?\n"), 'r') as f:
    x = f.read()
    input_seq = x.lower()
    print('Analyzing Sequence:\n{}'.format(input_seq))


# Removing all non-nucleotide elements
clean_seq = cleaning_seq(input_seq)
string1 = "".join(clean_seq)


print("The length of the sequence is {} bp.".format(len(string1)))

# Restriction Analysis
for rest in rest_db:
    cuts = rest_analysis(string1, rest[1], rest[2])
    print("Enzyme {0} cuts the sequence at positions: {1}".format(rest[0], cuts))
    

    


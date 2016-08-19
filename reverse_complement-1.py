'''
Script to generate reverse-complement DNA sequence from input txt file.
'''

def rev_comp(seq):
    rev_seq = []
    for i in seq:
        if i == 'a':
            rev_seq.append('t')
        elif i == 'c':
            rev_seq.append('g')
        elif i == 'g':
            rev_seq.append('c')
        elif i == 't':
            rev_seq.append('a')
        else:
            continue
    return rev_seq

with open('seq1.txt', 'r') as f:
    x = f.read()
    x = x.lower()
    print('Original Sequence:\n{}'.format(x))


bb = "".join(reversed(rev_comp(x)))
print('Reverse-Complement Sequence:\n{}'.format(bb))





        
    

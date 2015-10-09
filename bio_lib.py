#!/usr/bin/python

#This is Diego's python library for bioinformatics 

#=Function to find the reverse complement of a dna sequence
def rev_complement(dna_seq_string):
    #This function takes a dna string and returns its reverse complement'''
    dna_complem_dict= {'a':'t','c':'g','t':'a','g':'c'}#Make dictionary of complementary bases
    dna_seq_string= dna_seq_string.lower()#Lowers case of dna sequence so they're recognized in dictionary
    print dna_seq_string, 'turn to lower case'
    seq_as_list= list(dna_seq_string)#Turns string into list 
    print seq_as_list,'turn to list'
    comp_list= []#Initializes new list for complementary sequence
    print 'Pairing input, dictionary values'
    for base in seq_as_list:#Loops through dna seq list and  
        if base in dna_complem_dict.keys():#looks for element (base) in dna_complem_dict dictionary
            print base, ',', dna_complem_dict[base]
            comp_list.append(dna_complem_dict[base])#Appends result to comp_list 
        else:
            print 'n'
            comp_list.append('n')#or appends 'n' if not in dictionary
    print seq_as_list,'Input DNA sequence'#Print new list before reversing
    comp_list.reverse()#Reverse list order
    print comp_list, 'Reverse complement'
    rev_dna_str= ''.join(comp_list)
    return rev_dna_str
	
#==Function to find start codons in a sequence
def find_start(input_seq):

	start= 'atg'#Define start
	stop= ['taa','tag','tga']#Define stop codons
	start_pos= []#Initialize empty list to append indices of start codons
	for i in range(0,len(input_seq)):#Scan entire given sequence
		codon= input_seq[i:i+3]#Scan three bases at a time starting with i
		print codon
		if codon == start:#If codon equals previously defined start sequence
			print i,'Found one!'#Print index, statement
			start_pos.append(i)#And add index to list of starting positions
		else:
			print 'Nothing to see here'#Else statement and move to next position
	return start_pos
	
#==Find frame number
def find_frame(position,sequence):
    '''This function finds the frame of the position in a given sequence'''
    rem= position%3#Since codons are multiples of 3,
    #remainders should tell us what frame they are since a perfect multiple of 3
    #would correspond to frame 3, and remainder 2: frame 2, remainder 1: frame1

    if rem==1:
        frame =1
    elif rem==2:
        frame =2
    else: #Can only be rem==0
        frame =3
    print "Remainder:", rem, 'Frame:', frame
    return frame
			
def load_fasta(file_name):#Parse out seq names and seq strings
    seqs= {}
    file0= open(file_name)#
    counter= 0
    for line in file0:
        line= line.rstrip()#rstrip gets rid of characters at the end of your last character, if nothing gets rid of empty spaces
        if line[0]== '>':
            words= line.split()
            name= words[0][1:]
            seqs[name]= ''#Can't assign value yet but we can enter key name
#         counter= counter + 1
#         print counter
        else:
            seqs[name]= seqs[name] + line #Concats dna sequence to empty dict. entry/previous header
    return seqs            
    
#==Pull sequence from given file (not finished)
'''def list_seq(file_name):
   ''' '''This function identifies file type and pulls out sequence or 
    first sequence to quickly view the file and test functions on it'''

    '''file= open(file_name,'r')
    if '.fasta' in file_name:
        sequence= load_fasta(file_name)
        seq= sequence.values()
        print "Output is a list of sequences"
    return seq'''
#==Naive matching algorithm (Coursera genomic algorithms class)

def naive(p, t):
    '''Naive matching algorithm: iterates over sequence to find matching occurrences'''
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


#==Variation of naive with two mismatches (hw)==

def naive_2mm(p, t):
    '''Naive matching algorithm (without reverse complement) that allows 
    up to two mismatches before break'''
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        mismatch= 0 #Initialize a counter for mismatch of characters. Resets for every alignment
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatch = mismatch + 1 #If character comparison is off, add 1 to mismatch counter
                
                if mismatch > 2: #Check if mismatch counter is greater than 2
                    match = False #If it is, break like in naive function
                    break
        if match:
            occurrences.append(i)  # all chars matched; record position
    return occurrences


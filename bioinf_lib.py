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
			
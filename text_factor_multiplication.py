
text_path = '/home/sherlock31/NLP_intern/dic2.txt'
text_path_out = '/home/sherlock31/NLP_intern/dic3.txt'
text_corpus = open(text_path, "r+")			#opening the file for both reading and writing
text_out = open(text_path_out,'w')

for line in text_corpus:
	
	line_split = line.split()
	name = line_split[0]
	freq = int(line_split[1])
	#if((len(name) == 1) or name.isdigit()):
	#	continue
	#else:	 
	#	text_out.write(name + " " + str(freq) + "\n")
	for line2 in text_corpus:
	
	 

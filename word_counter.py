from collections import Counter
def word_counter(textpath):
	with open(textpath) as f:
		
		text_out = textpath.replace('.txt', '_counted.txt')
		file_output = open(text_out, 'w')										#Opening a text file for writing
		words = [word for line in f for word in line.split()]
		c = Counter(words)
		
		for word, count in c.most_common():
			file_output.write(word + " " + str(count) + "\n") 

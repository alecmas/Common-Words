# Common Words
# Alexander Mas
import string
import sys
from collections import OrderedDict

strip = (string.whitespace + string.punctuation + string.digits + "\"'") # ignore quotations
commonWords = {}
wordsInOrder = {}
files = {}
commonFiles = {}

# read file and create a dictionary of its words
for filename in sys.argv[1:]:
	words = []
	for line in open(filename):
		for word in line.lower().split():
			word = word.strip(strip)
			words.append(word)

	files[filename] = words

	# copy first file's words
	if not commonWords:
		commonWords = words

	# dict comprehension to keep only words that are common across all files
	commonWords = {word for word in commonWords if word in words}

# get the common words in the order that they are seen in each file
for filename in sys.argv[1:]:
	words = []
	for line in open(filename):
		for word in line.lower().split():
			word = word.strip(strip)

			if word in commonWords:
				words.append(word)

	wordsInOrder[filename] = words

# compare all of the files to see which ones contain the common words in the same order
for filename1,words1 in wordsInOrder.items():
	# list comprehension to hold the filenames which share common words in the same order
	f = [filename2 for filename2,words2 in wordsInOrder.items() if words2 == words1]
	# get rid of the case where a file matches itself
	if filename1 in f:
		f.remove(filename1)
	# dict which holds each filename as a key and the common files (files with common words in same order) as values
	commonFiles[filename1] = f

print("COMMON WORDS")
for word in commonWords:
	sys.stdout.write(word + " ")
print("\n")

# list to keep track of already printed filenames
printedFiles = []
for file1,fs in sorted(commonFiles.items()):
	# eliminate printing duplicates
	if file1 not in printedFiles:
		sys.stdout.write(file1 + ": ")
		for i in fs:
			printedFiles.append(i)
			sys.stdout.write(i + " ")
		sys.stdout.write("\n")
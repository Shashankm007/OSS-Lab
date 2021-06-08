# Compute the number of characters, words and lines in a file.

file = open("file.txt", "r")

lines_count = 0
words_count = 0
characters_count = 0
for line in file:
  line = line.strip("\n")

  words = line.split()
  lines_count += 1
  words_count += len(words)
  characters_count += len(line)

file.close()

print("lines:", lines_count, "words:", words_count, "characters:", characters_count)
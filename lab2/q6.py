# Use Python Built-in Functions 'open', 'read', 'readline', 'write', 'writelines' to work with files.

f = open("file.txt", 'w')
f.write("my first file\n")
f.writelines(["second line\n", "third line"])
f.close()
f = open("file.txt", 'r')
print(f.readline())
print(f.read())
f.close()
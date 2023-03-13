text = open("hello.txt", "r")
text_from_file = text.read()
text_from_file *= 5
print(text_from_file)
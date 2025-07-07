sentence=input("enter the sentence: ")
char_count=len(sentence)
print("number of characters: ",char_count)
print("uppercase: ", sentence.upper())
print("lowercase: ", sentence.lower())
print("with underscore: ", sentence.replace(" ","_"))
if 'python' in sentence.lower():
	print("the sentence have 'python'.")
else:
	print("the sentence does not contain the word 'python'.")



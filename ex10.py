tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* cat food
\t* Fishies
\t* catnip\n\t* Grass
'''

print tabby_cat
print persion_cat
print backslash_cat
print fat_cat


while True:
	for i in ["/","-","|","\\","|"]:
		print "%r\r" % i,
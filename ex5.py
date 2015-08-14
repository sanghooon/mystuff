name = 'Sanghoon Han'
age = 23 # not a lie
height = 6 # feet
weight = 195 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He's %d inches tall" % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print"His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "My name is %r." % name
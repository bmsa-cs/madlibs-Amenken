"""
MadLibs
Author: Andrea Menken
Period/Core: 6


"""
print("Input the words instructed.")
print("Put in a place, please.")

place = input()
print("Put in a verb.")
verb = input()
print("Put in an adjective.")
adjective = input()
print("Put in an animal.")
animal = input()
print("Put in a natural disaster.")
natural_disaster = input()
print("Put in a verb.")
verb2 = input()
print("Put in a noun.")
noun = input()
print("Put in a class subject.")
class_subject = input()
print('I was in %s, just about to %s. But, I noticed the clouds become\n %s. It was unsettling, but I decided to take my %s for a walk anyways.\n About halfway through, there was a %s. I began to %s back. But, there was a %s. I tried to get past but it told me about %s.' % (place, verb, adjective, animal, natural_disaster, verb2, noun, class_subject))
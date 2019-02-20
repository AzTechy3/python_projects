"""
This is a Mad Lips project that requires:
- Words from the reader (for the blank spaces)
- A story to plug the words into
The program does the following:
- Prompt the user for input
- Print the entire Mad Lips story with the user's input in the right places
"""

print "Your Mad Lips session is starting..."

#Main Chacter Name
name = raw_input('What is the name of your main character?')

#Adjectives
first_adj = raw_input('Enter an adjective: ')
second_adj = raw_input('Enter a second adjective: ')
third_adj = raw_input('Enter one more adjective: ')

#Verbs
first_verb = raw_input('Enter a verb: ')
second_verb = raw_input('Enter a second verb: ')
third_verb = raw_input('Enter one more verb: ')

#Nouns
first_noun = raw_input('Enter a noun: ')
second_noun = raw_input('Enter a second noun: ')
third_noun = raw_input('Enter a third noun: ')
fourth_noun = raw_input('Enter one more noun: ')

#Weird Part of the Story
animal = raw_input('Enter an animal: ')
food = raw_input('Enter a food: ')
fruit = raw_input('Enter a fruit: ')
number = raw_input('Enter a number: ')
hero = raw_input('Enter a superhero name: ')
country = raw_input('Enter a country: ')
dessert = raw_input(' Enter a dessert: ')
year = raw_input('Enter a year: ')


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (first_adj, name, first_verb, second_adj, first_noun, second_noun, animal, food, second_verb, third_noun, fruit, third_adj, name, third_verb, number, name, hero, hero, name, country, name, dessert, name, year, fourth_noun)

print STORY
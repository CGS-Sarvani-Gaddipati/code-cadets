##word = input("Long word: ")
##new_word = len(word)
##vocab = 28 - new_word
##print(f'It is {vocab} letter(s) shorter than the longest word.')

##plan = input('What are your plans? ')
##plan = plan.replace('train', 'bus')
##print(plan)

##name = input('Name: ')
##relation = input('Relation: ')
##noun = input('Noun: ')
##animal = input('Animal (plural): ')
##sport = input('Sport: ')
##adj = input('Adjective: ')
##another_adj = input('Another Adjective: ')
##verb = input('Verb: ')
##print(f'Dear {relation},')
##print(f'Camp {noun} has been {adj} so far!')
##print(f'Tomorrow we will play {sport} if the weather is ok.')
##print(f'Today it has been raining cats and {animal} all day!')
##print(f'If we cannot play {sport}, maybe we will just {verb}.')
##print(f'I am sure it will be {another_adj} either way!')
##print(f'See you soon! {name}')

##Fr_name = input('First name: ')
##l_name = input('Last name: ')
##Fr_name = Fr_name.lower
##l_name = l_name.lower
##print ("Your email address is %s." % (Fr_name))

#line = input('Line: ') 
#while line[0:7] != 'You are' :
  #line = input('Line: ') 
  #while line[0:7] == 'You are' :
    #print('I know you are, you said you are, but what am I?')
    #line = input('Line: ')
    #while line[0:7] != 'You are' :
       #line = input('Line: ') 
    #when line == ' ':
        #break
#print('cat ' * 9999)
#line = input('Line: ')
#while line:
  #if line[-1] == '?':
    #line = input('Line: ')
  #else:
    #print('Statement!')
  
#print('Arrr, I am Captain Featherbot.')
#print('What be your name?')
#name = input('> ')
#print(f'Ahoy {name}! What be on your mind?')
#line = input('> ')
#while line:
  #line = line.lower()
  #if line == 'go away':
    #print('Shiver me timbers!')
    #print(f'Farewell {name}, yer landlubber.')
    #print('I will be off for more swashbuckling adventures!')
    #break
  #elif 'boat' in line:
 #   print('Oh, I do love my boat, Floaty McFloatface.')
#    line = input('> ')
 # elif 'sea' in line:
#    print('Oh, the sea. Arrr to be back on the sea.')
#    line = input('> ')
 # elif line[-1] == '!':
#    print(f'Yo ho ho. That be a good one, {name}! Then what?')
#    line = input('> ')
 # elif line[-1] == '?':
#    print(f'That be the real question {name}. I wish I knew.')
#    line = input('> ')
 # elif 'I feel' in line:
#    print('When I feel that way, I go sailing. What do you do?')
#    line = input('> ')
 # else:
#    print('Arrr. Go on...')
#    line = input('> ')
word = input('Word: ')
word_2 = input('Word: ')
while word:
  word = word.lower()
  word_2 = word_2.lower()
  if word_2[0] == word[-1]:
    word = word_2 
    word_2 = input('Word: ')
  else:
    print('Invalid word')
    word = input('Word: ')
    word_2 = input('Word: ')

import random ,sys
HANGMAN_PICS = ["""
+---+
|   |
    |
    |
    |
    |
=====""",

"""
+---+
|   |
O   |
    |
    |
    |
=====""",

"""
+---+
|   |
O   | 
|   |
    |
    |
=====""",

"""
 +---+
 |   | 
 O   |
/|   |
     |
     |
=====""",

"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=====""",

"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=====""",

"""
 +---+
 |   |
 O   |
/|\  | 
/ \  |
     |
====="""]

Category =['Animals','SoccerPlayers']
Words='ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()
PLayers='MESSI,MBABE,KANE,INIESTA,XAVI,MODRIC,YAMAL,SUAREZ'.split(',')
def main():
    print('HANGMAN')
    missedletters=[]
    correctletters=[]
    print("""Please Choose category from 
            1.Animals 
            2.SoccerPlayers""")
    CategoryNO=int(input())
    if CategoryNO==1:
        secretword=random.choice(Words)
    else:
        secretword=random.choice(PLayers)

    
    while True:
            
        drawHangman(missedletters,correctletters,secretword)
        guess = getPlayerGuess(missedletters + correctletters)
        if guess in secretword:
            correctletters.append(guess)
            foundAllLetters =True 
            for secretWordLetter in secretword :
                if secretWordLetter not in correctletters:
                    foundAllLetters=False
                    break  
            if foundAllLetters :
                print('Yes! The secret word is:', secretword)
                print('You have Won!')
                break
        else:
            missedletters.append(guess)       
            if len(missedletters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedletters, correctletters, secretword)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretword))
                break 





def getPlayerGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')    
        else:
             return guess    


def drawHangman(missedletters,correctletters,secretword):
    print(HANGMAN_PICS[len(missedletters)])
    #print('The category is '+Flag)
    print()
        

    print('Missed letters: ', end='')
    for letter in missedletters:
        print(letter, end=' ')
    if len(missedletters) == 0:
        print('No missed letters yet.')
    print()

    blanks = ['_'] * len(secretword)        

    for i in range(len(secretword)):
        if secretword[i] in correctletters:
            blanks[i] = secretword[i]

    print(' '.join(blanks))  
    



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()


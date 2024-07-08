import random

ALPHA_DIGITS=3
MAX_GUESSES=10

def main():
    print(f"""Bagels, alphabet version of the game .         
        I am thinking of a {ALPHA_DIGITS}-digit string with no repeated Alphapets.
        Try to guess what it is. Here are some clues:
        When I say:    That means:
            Pico         One alphabet is correct but in the wrong position.
            Fermi        One alphabet is correct and in the right position.
            Bagels       No alphabet is correct.
            For example, if the secret string was azx and your guess was xza, the
            clues would be Fermi Pico.""")

    while True:
        secretWord=getSecretWord()
        print('I have thought up a String.')
        print(f" You have {MAX_GUESSES} guesses to get it.")
        numGuesses=1
        while numGuesses <= MAX_GUESSES:
             guess=''
             while(len(guess))!=ALPHA_DIGITS or not guess.isalpha():
                print(f"Guess #{numGuesses}: ")
                guess = input('> ') 
             clues = getClues(guess,secretWord)
             print(clues)
             numGuesses+=1
             if guess == secretWord:
                  break
             if numGuesses >MAX_GUESSES:
                 print('You ran out of guesses.')
                 print(f"The answer was {secretWord}.")


        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
             break
        

    print('Thanks for playing!')    
                  


def getSecretWord():
        words =list('abcdefghijklmnopstuvwxyz')
        random.shuffle(words)

        secretWord=''
        for i in range(ALPHA_DIGITS):
             secretWord += str(words[i])
        return secretWord



def getClues(guess,secretWord):
    if guess == secretWord:
        return 'You got it!'

    clues=[]
    for i in range(len(guess)):
        if guess[i]==secretWord[i]:
            clues.append('Fermi')
        elif guess[i] in secretWord:
             clues.append('Pico')
    if len(clues)== 0:
         return 'Bagels'
    else:
         clues.sort()
         return ''.join(clues) 


if __name__=='__main__':
    main()
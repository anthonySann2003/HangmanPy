class Hangman:
    #Class variables
    secretPhrase = "theo"
    guessesLeft = 5
    guessPhrase = "****"
    def __init__(self, playerName):
        self.playerName = playerName


    def getGuess(self):
        guess = input("Enter a guess: ")
        #input validation on the guess (1 character, not a number, not already guessed, etc)
        self.checkGuess(guess)

    def checkGuess(self, guess):
        for char in self.secretPhrase:
            if(char == guess): #Guessed a letter correct
                print('Correct Guess')

    def updatePhrase(self, guess):
        #Loop through guessPhrase and change * to correct letter where guessed
        print('Updating Phrase')

    def updateBoard(self):
        #Update the guessesLeft and hangman ascii
        print('Guesses Left: ', self.guessesLeft)

    def runGame(self):
        while self.guessesLeft > 0:
            self.getGuess()

userName = input("Enter your name: ")
h1 = Hangman(userName)
print(h1.playerName)

h1.runGame()



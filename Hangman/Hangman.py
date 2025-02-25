from sympy import Q


class Hangman:
    #Class variables
    secretPhrase = "anthony sannazzaro"
    guessesLeft = 6
    guessPhrase = ''
    guessList = []
    def __init__(self, playerName):
        self.playerName = playerName
   
    def getGuess(self):
        print('__________________________________________________________________')
        print('You have', self.guessesLeft, "guesses left.")
        print(self.guessPhrase)
        guess = input("Enter a guess: ")
        
        self.validateGuess(guess) #Call validate guess

    def validateGuess(self, guess):
        #input validation on the guess (1 character, not a number, not already guessed, etc)        
        guess = guess.lower() #Converting guess to lowercase
        
        badGuessFlag = False #Creating flag for a bad guess
        winGameFlag = False #Creating flag for an exact guess

        for val in self.guessList: #Check if already guessed
            if guess == val:
                print("You already guessed this letter!")
                badGuessFlag = True
                break
        
        if len(guess) != 1 and badGuessFlag == False: #Making sure guess is only 1 letter, can add functionality later to have an or statement for exact guess of phrase
            if(guess == self.secretPhrase): #If guess phrase exactly then instant win
                self.gameWin()
                winGameFlag = True

            if(len(guess) != len(self.secretPhrase)):
                print("Your guess must be only 1 letter!")
                badGuessFlag = True

        if(badGuessFlag):
            self.getGuess() #Retry getting a guess
        else:
            if(winGameFlag == False):
                self.checkGuess(guess) #Continue to checking the guess

    def checkGuess(self, guess):
        correctGuessFlag = False #Create flag
        self.guessList.append(guess) #Add guess to list of already guessed letter

        for char in self.secretPhrase:
            if(char == guess): #Guessed a letter correct
                correctGuessFlag = True
                break

        if(correctGuessFlag):
            self.updatePhrase(guess)
        else:
            self.updateBoard(guess)

    def updatePhrase(self, guess):
        #Loop through guessPhrase and change * to correct letter where guessed
        updatedPhrase = list(self.guessPhrase) #Changing guessPhrase to a list because strings are immutable

        for i, char in enumerate(self.secretPhrase):
            if char == guess:
                updatedPhrase[i] = guess #Replacing * with correct letter

        self.guessPhrase = "".join(updatedPhrase) #Joining back to a string
        
        if(self.guessPhrase == self.secretPhrase): #Checking if player won
            self.gameWin()
        else:
            print("You guessed correctly!")
            print(self.guessPhrase)

    def updateBoard(self, guess):
        #Update the guessesLeft and hangman ascii
        self.guessesLeft = self.guessesLeft - 1 #Update guesses left

        if(self.guessesLeft == 0): #Checking if out of guesses
            self.gameOver()
        else:
            if(len(guess) != 1):
                print("Thats not it, but good guess!")
            else:
                print('Sorry that letter is not in the phrase.')

    def runGame(self):
        self.gameStart() #Run starting background functionality
        self.showInstructions() #Show player the instructions
        while self.guessesLeft > 0:
            self.getGuess()

    def gameOver(self):
        #Call this when out of guesses
        print("Sorry you're out of guesses, you lose!")
        print("The phrase was:", self.secretPhrase)

    def gameWin(self):
        #Call when secretPhrase matches guessPhrase
        print("Congratulations you won!")
        print("The phrase was:", self.secretPhrase)
        self.guessesLeft = 0 #Setting to 0 so game ends

    def showInstructions(self):
        print("Welcome", self.playerName, "to Hangman")
        print("The object of the game is to guess the hidden phrase")
        print("The phrase will be hidden by asteriks (*)")
        print("Each round you will enter one letter as a guess, or if you think you know it, guess the whole phrase!")
        print("Guess right and you will see the updated phrase, guess wrong and you will lose a guess")
        print("The game continues until you either guess the phrase or run out of guesses")
        print("Good luck!")

    def gameStart(self):
        #Run startup functionality
        tempGuessPhrase = list(self.guessPhrase)
        for char in self.secretPhrase: #Creating the asteriks for the guessPhrase
            tempGuessPhrase.append('*')

        self.guessPhrase = "".join([" " if char == " " else "*" for char in self.secretPhrase]) #Joining back to a string

#Main
userName = input("Enter your name: ")
h1 = Hangman(userName)

h1.runGame()



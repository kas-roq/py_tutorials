# Score function - returns score of a scrabble word.
def score(word):

    # This is the user's score.
    userScore = 0
    
    # This is output message.
    outputMessage = "" 

    # Allocated points for each character.
    onePointCharacters = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
    twoPointsCharacters = ['D', 'G']
    threePointsCharacters = [ 'B',  'C', 'M', 'P'] 
    fourPointsCharacters = ['F', 'H', 'V', 'W', 'Y']
    fivePointsCharacters = ['K']
    eightPointsCharacters = ['J', 'X']
    tenPointsCharacters = ['Q', 'Z']

    # Iterate through the argument [word]
    for character in word:
        if character.upper() in onePointCharacters:
            userScore= userScore+ 1
        if character.upper() in twoPointsCharacters:
            userScore= userScore+ 2
        if character.upper() in threePointsCharacters:
            userScore= userScore+ 3
        if character.upper() in fourPointsCharacters:
            userScore= userScore+ 4
        if character.upper() in fivePointsCharacters:
            userScore= userScore+ 5
        if character.upper() in eightPointsCharacters:
            userScore= userScore+ 8
        if character.upper() in tenPointsCharacters:
            userScore = userScore + 10


    # Output Message.
    if userScore == 1:
        outputMessage = 'You got', userScore, 'point!' 
    elif userScore == 0:
        outputMessage = 'You are a failure!'
    else:
        outputMessage = 'You got', userScore, 'points!'

    #This returns output message.
    return outputMessage

    # This returns user's score.
    return userScore



seniordevScore = score("seniordev")
print(seniordevScore)



            

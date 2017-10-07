def guessVerticaly(posibleGuessesList, allGuessesList, stepList, recusionDepth, dimension):
    for guess in posibleGuessesList[0][stepList[recusionDepth][0]]:
        shortenGuessesList = (posibleGuessesList[0],())
        for i in range(0,dimension):
            shortenGuessesList =
        shortenGuessesList = posibleGuessesList
        i=0
        for digit in str(guess):
            shortenGuessesList[1][i] = posibleGuessesList[1][i] & allGuessesList[("byDigit",int(digit),i)]

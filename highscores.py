#GitHub: Odiy-sc
#Type Zhuyin
#file for reading / writing high scores

def setScore(score, number):
    '''
    write the correct score into the text file 
    '''
    values = getScore()
    values[number-1] = score

    file  = open("scores.txt", "w")

    for i in range(len(values)):
        file.write(str(values[i]) + "\n")
        
    file.close()

def getScore():
    '''
    return a float array of all of the scores
    '''
    file  = open("scores.txt", "r")
    values = file.readlines()
    file.close()

    for i in range(len(values)):
        values[i] = float(values[i].rstrip('\n'))

    return values

#GitHub: Odiy-sc
#Type Zhuyin
#main file

#do in virtual environment with .\virtual\Scripts\activate.bat

#import statements
#import PyQt
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel, QMessageBox
from PyQt5.QtGui import QIcon, QFont

#for the keypress events!
from PyQt5.QtCore import Qt

#import other files
import lessonInfo
import highscores

class scoreButton(QPushButton):
    def __init__(self, content, window):
        '''
        initializes a "high score" button
        '''
        #call parent class constructor (QWidget)
        super().__init__(window)

        #title of the button
        self.name = content
        
        self.setText(content)
        self.setFont(QFont("Arial", 9))
        self.setGeometry(200,750,100,30)

        #connet to event function
        self.clicked.connect(self.clicker)

        #define variable for high score window
        self.myScorer = None

    def clicker(self):
        '''
        event function for scoreButton - when scoreButton is clicked, create a window
        '''
        self.myScorer = scoreWindow(self.name)


class scoreWindow(QWidget):
    def __init__(self, name):
        '''
        initializes the score window
        '''
        super().__init__()
        
        #set size
        self.resize(1000, 700)

        #set window title and icon
        self.setWindowTitle(name)
        self.setWindowIcon(QIcon('icon.png'))

        #create title and scores on window
        title = QLabel("High Scores", self)
        title.setGeometry(80,320,340,30)
        title.setFont(QFont("Arial", 20))

        lesson1H = QLabel("Lesson 1: " + str(highscores.getScore()[0]) + "%", self)
        lesson2H = QLabel("Lesson 2: " + str(highscores.getScore()[1]) + "%", self)
        lesson3H = QLabel("Lesson 3: " + str(highscores.getScore()[2]) + "%", self)
        lesson4H = QLabel("Drill 4: " + str(highscores.getScore()[3]) + "%", self)
        lesson5H = QLabel("Lesson 5: " + str(highscores.getScore()[4]) + "%", self)
        lesson6H = QLabel("Lesson 6: " + str(highscores.getScore()[5]) + "%", self)
        lesson7H = QLabel("Lesson 7: " + str(highscores.getScore()[6]) + "%", self)
        lesson8H = QLabel("Drill 8: " + str(highscores.getScore()[7]) + "%", self)
        lesson9H = QLabel("Lesson 9: " + str(highscores.getScore()[8]) + "%", self)
        lesson10H = QLabel("Lesson 10: " + str(highscores.getScore()[9]) + "%", self)
        lesson11H = QLabel("Lesson 11: " + str(highscores.getScore()[10]) + "%", self)
        lesson12H = QLabel("Drill 12: " + str(highscores.getScore()[11]) + "%", self)
        lesson13H = QLabel("Lesson 13: " + str(highscores.getScore()[12]) + "%", self)
        lesson14H = QLabel("Lesson 14: " + str(highscores.getScore()[13]) + "%", self)
        lesson15H = QLabel("Lesson 15: " + str(highscores.getScore()[14]) + "%", self)
        lesson16H = QLabel("Drill 16: " + str(highscores.getScore()[15]) + "%", self)

        #put into array for ease
        scoreArray = [lesson1H, lesson2H, lesson3H, lesson4H, lesson5H, lesson6H, lesson7H, lesson8H, lesson9H, lesson10H, lesson11H, lesson12H, lesson13H, lesson14H, lesson15H, lesson16H]

        #set parameters for each label
        for i in range(len(scoreArray)):
            scoreArray[i].setGeometry(500,70+35*(i),500,35)
            scoreArray[i].setFont(QFont("Arial", 12))

        #show window
        self.show()



class lessonButton(QPushButton):
    def __init__(self, number, content, window, typer="Lesson"):
        '''
        initializes a lesson button
        '''
        #call parent class constructor (QWidget)
        super().__init__(window)
        
        self.number = number
        self.name = (typer + " " + str(number) + ": " + content)

        self.setText(self.name)
        self.setFont(QFont("Arial", 9))

        #position by math
        self.setGeometry(500,50*(number-1),500,50)

        #no parentheses because not calling function, just passing reference
        self.clicked.connect(self.buttonClicked)
  
        self.myLesson = None

    def buttonClicked(self):
        '''
        event function for lessonButton - when lessonButton is clicked, create a window
        '''
        #self is so that the window persists
        self.myLesson = lessonWindow(self.number, self.name)


class lessonWindow(QWidget):
    def __init__(self, number, name):
        '''
        initializes the lesson window
        '''
        super().__init__()

        #information variables
        self.infoString = lessonInfo.stringList[number-1]
        self.infoKey = lessonInfo.keyList[number-1]
        self.index = 0 #not used yet

        #turns out, I still need to keep track of lesson number
        self.number = number

        #set size
        self.resize(1000, 750)

        #set title and icon
        self.setWindowTitle(name)
        self.setWindowIcon(QIcon('icon.png'))

        #correct number vars
        self.correct = 0.0
        self.total = lessonInfo.totalList[number-1]

        #on screen lesson
        self.infoList = []
        currAvaliable = 840
        column = 0
        row = 0

        #place each character on screen
        for i in range(self.total):
            text = QLabel(lessonInfo.splitList[self.number-1][i], self)
            text.setGeometry(80+24*column,50+24*row, 24, 24)
            text.setFont(QFont("Arial", 18))

            #add to final list
            self.infoList.append(text)

            #continue with row
            if currAvaliable > 24:
                currAvaliable = currAvaliable - 24
                column += 1
            #new row!
            else:
                currAvaliable = 840
                column = 0
                row += 1

        #instructions at bottom
        remind = QLabel(lessonInfo.descList[number-1], self)
        remind.setGeometry(80, 550,840,200)
        remind.setFont(QFont("Arial", 12))
        remind.setWordWrap(True)

        #show window
        self.show()

        #popup box
        self.instructions = QMessageBox.information(self, "Instructions", lessonInfo.descList[number-1], QMessageBox.Ok)

    def keyPressEvent(self, e):
        '''
        every time a key press happens...
        '''
        #if at the end...
        if self.index == self.total:
            finalScore = self.calculateScore()
            scorebox = QMessageBox.information(self, 'Congratulations', 'Your score for this lesson was ' + str(finalScore) + "%.", QMessageBox.Ok)

            #update score board if necessary
            if finalScore > highscores.getScore()[self.number-1]:
                highscores.setScore(finalScore, self.number)

            #close lesson
            self.close()
            
        else:
            color = self.infoList[self.index]

            #if correct key...
            if e.key() == self.infoKey[self.index]:
                self.correct+=1
                color.setStyleSheet("background-color: #90ee90")
                
            else:
                color.setStyleSheet("background-color: #ff6c5c")
                
            self.index+=1

    def calculateScore(self):
        '''
        calculates final score
        '''
        return round(self.correct/self.total*100, 2)



#main window
if __name__ == "__main__":           
    #make window
    app = QApplication(sys.argv)
    mainWindow = QWidget()

    #set size
    mainWindow.resize(1000, 800)

    #set title and icon
    mainWindow.setWindowTitle('Type Zhuyin')
    mainWindow.setWindowIcon(QIcon('icon.png'))

    #set title and intro with description of prgram
    title = QLabel("Type Zhuyin", mainWindow)
    desc = QLabel("Type Zhuyin is a program aimed at helping those who want to improve their Chinese by memorizing the positions of each symbol in the Zhuyin alphabet on a keyboard. Zhuyin is a phonetic system used in Taiwan as a reading aid and a typing system. It is highly recommended that users are already familiar with the Zhuyin alphabet and basic Chinese before using this program.", mainWindow)

    title.setGeometry(80,270,340,30)
    title.setFont(QFont("Arial", 20))
    desc.setGeometry(80,320,340,200)
    desc.setFont(QFont("Arial", 12))
    desc.setWordWrap(True)

    #lesson buttons
    lesson1B = lessonButton(1, "ㄑㄨㄎㄜ", mainWindow)
    lesson2B = lessonButton(2, "ㄋㄠㄇㄤ", mainWindow)
    lesson3B = lessonButton(3, "ㄕㄘ", mainWindow)
    lesson4B = lessonButton(4, "Review 1", mainWindow, "Drill")
    lesson5B = lessonButton(5, "ㄔㄗㄐㄧ", mainWindow)
    lesson6B = lessonButton(6, "ㄍㄛㄊㄟ", mainWindow)
    lesson7B = lessonButton(7, "ㄆㄣ", mainWindow)
    lesson8B = lessonButton(8, "Review 2", mainWindow, "Drill")
    lesson9B = lessonButton(9, "ㄖㄙㄒㄩ", mainWindow)
    lesson10B = lessonButton(10, "ㄏㄝㄌㄡ", mainWindow)
    lesson11B = lessonButton(11, "ㄈㄥ", mainWindow)
    lesson12B = lessonButton(12, "Review 3", mainWindow, "Drill")
    lesson13B = lessonButton(13, "ㄅㄉㄓ", mainWindow)
    lesson14B = lessonButton(14, "ㄚㄞㄢㄦ", mainWindow)
    lesson15B = lessonButton(15, "Tone Marksˇˋˊ˙", mainWindow, "Special")
    lesson16B = lessonButton(16, "Review 4", mainWindow, "Drill")

    #high score button
    score = scoreButton("High Scores", mainWindow)
  
    #show window
    mainWindow.show()

    #loop
    sys.exit(app.exec_())

#GitHub: Odiy-sc
#Type Zhuyin
#file for preparing all the info of each lessson

#possibility: split from main for faster loading

#for the keypress events!
from PyQt5.QtCore import Qt
import random

def translateToKey(string):
    '''
    translate a single Zhuyin into the the right key
    '''
    switcher = {
        " ": Qt.Key_Space,
        "ㄑ": Qt.Key_F,
        "ㄨ": Qt.Key_J,
        "ㄎ": Qt.Key_D,
        "ㄜ": Qt.Key_K,
        "ㄋ": Qt.Key_S,
        "ㄠ": Qt.Key_L,
        "ㄇ": Qt.Key_A,
        "ㄤ": Qt.Key_Semicolon,
        "ㄕ": Qt.Key_G,
        "ㄘ": Qt.Key_H,
        "ㄔ": Qt.Key_T,
        "ㄗ": Qt.Key_Y,
        "ㄐ": Qt.Key_R,
        "ㄧ": Qt.Key_U,
        "ㄍ": Qt.Key_E,
        "ㄛ": Qt.Key_I,
        "ㄊ": Qt.Key_W,
        "ㄟ": Qt.Key_O,
        "ㄆ": Qt.Key_Q,
        "ㄣ": Qt.Key_P,
        "ㄖ": Qt.Key_B,
        "ㄙ": Qt.Key_N,
        "ㄒ": Qt.Key_V,
        "ㄩ": Qt.Key_M,
        "ㄏ": Qt.Key_C,
        "ㄝ": Qt.Key_Comma,
        "ㄌ": Qt.Key_X,
        "ㄡ": Qt.Key_Period,
        "ㄈ": Qt.Key_Z,
        "ㄥ": Qt.Key_Slash,
        "ㄅ": Qt.Key_1,
        "ㄉ": Qt.Key_2,
        "ㄓ": Qt.Key_5,
        "ㄚ": Qt.Key_8,
        "ㄞ": Qt.Key_9,
        "ㄢ": Qt.Key_0,
        "ㄦ": Qt.Key_hyphen,
        "ˇ": Qt.Key_3,
        "ˋ": Qt.Key_4,
        "ˊ": Qt.Key_6,
        "˙": Qt.Key_7
    }

    return switcher.get(string, Qt.Key_Space)


def totalLength(stringList):
    '''
    takes an array of lesson Zhuyin strings and turns that into lesson lengths
    '''
    totalList = []
    for i in stringList:
        totalList.append(len(i))

    return totalList


def splitList(stringList):
    '''
    takes an array of lesson Zhuyin strings and turns each string into an array
    returns a 2D array
    '''
    splitList = []
    for i in stringList:
        splitList.append(list(i))
        
    return splitList


def makeKey(oneLessonSplit):
    '''
    translates one lesson Zhuyin array into a lesson key array
    '''
    keyList = []
    for i in oneLessonSplit:
        keyList.append(translateToKey(i))

    return keyList



#a list of all the lessons in Zhuyin string format
oneS = "ㄑㄑㄑㄑ ㄨㄨㄨㄨ ㄑㄑㄨㄑ ㄨㄨㄑㄑ ㄨㄑㄑㄨ ㄑㄑㄑ ㄨㄨㄨ ㄨㄨㄨㄨ ㄑ ㄑㄑㄑ ㄨㄑ ㄑㄨ ㄑㄨ ㄨㄑㄨㄑㄑ ㄨㄑㄑㄨ ㄑㄑㄑ ㄨㄨ ㄑㄨ ㄑㄨ ㄨㄑ ㄨㄨㄨㄨ ㄑㄑㄑ ㄑㄨ ㄨㄑㄨㄑㄑ ㄨㄑ ㄨㄑ ㄑㄨ ㄑㄑㄑㄑ ㄨㄨㄨㄨ ㄨㄨㄨ ㄑㄑㄑ ㄨㄑㄑㄨ ㄑㄑㄨㄨ ㄑㄨㄑㄑ ㄨ ㄨ ㄨㄨ ㄑㄑㄑㄑ ㄑㄨ ㄑㄑㄨㄑㄨ ㄨㄑ ㄑㄑㄑ ㄨㄨㄑㄨ ㄑㄨ ㄨㄑ ㄨㄑ ㄨㄨ ㄑㄑㄑ ㄨㄑㄑㄨ ㄑㄑㄨㄑㄨ ㄨㄑ ㄎㄎㄎㄎㄎ ㄜㄜㄜㄜ ㄜㄜㄎㄎ ㄜㄎㄎㄜ ㄎㄜ ㄎㄜ ㄜㄎㄜ ㄜㄜㄜ ㄎㄎㄎㄎ ㄎ ㄜ ㄜ ㄎㄎㄜㄜ ㄜㄜㄎ ㄎ ㄜ ㄎ ㄎㄎㄜ ㄎㄜㄜㄎ ㄜㄜㄜㄜ ㄜ ㄎㄜ ㄜㄎㄎ ㄜㄎ ㄎㄎㄎ ㄜㄜ ㄜㄎ ㄜㄎ ㄎㄎㄜ ㄜㄎㄎ ㄎㄜ ㄎㄜ ㄜㄜ ㄎㄎㄎ ㄎㄜ ㄎㄎㄜ ㄜㄎ ㄜ ㄜㄜㄜㄜ ㄎㄜㄜㄎ ㄜㄎㄎ ㄎ ㄜ ㄎ ㄎㄜㄜ ㄜㄜㄎㄎ ㄜ ㄜ ㄎ ㄎㄎㄎㄎ ㄜㄜㄜ ㄜㄎㄜ ㄜㄎ ㄜㄎ ㄜㄎㄎㄜ ㄎㄎㄜㄜ ㄜㄜㄜㄜ ㄎㄎㄎ ㄎㄎ ㄑㄎ ㄎㄜㄜ ㄑㄑㄜㄜ ㄎㄑ ㄨㄜ ㄜ ㄜ ㄨㄑㄨㄨ ㄨㄎㄜㄨㄜ ㄑㄜㄑ ㄎ ㄎ ㄎㄜㄎㄑ ㄜㄜㄎㄎ ㄑㄎㄜㄎ ㄜㄨㄨ ㄜㄨ ㄨㄨ ㄎ ㄑ ㄑㄎㄜ ㄨㄨㄜ ㄜㄎㄎㄜ ㄎㄨ ㄑㄎ ㄜㄨ ㄜㄨ ㄜㄎㄜ ㄨㄑㄎㄑ ㄨㄨ ㄑㄜ ㄎ ㄨ ㄨ ㄨㄑㄎ ㄎ ㄎ ㄜㄨㄜㄑ ㄎㄜㄜㄎ ㄨㄨㄜ ㄜ ㄑㄜㄎ ㄨㄎㄨㄎ ㄜㄜㄑ ㄑㄎ ㄜ ㄜㄑㄑ ㄎㄑ ㄜ ㄎㄨ ㄜㄎ ㄜㄨ ㄎㄨㄨ ㄑㄜㄑ ㄎㄎㄎ ㄑ ㄜㄨㄨ ㄜ ㄨ ㄜ ㄨㄎ"
twoS = "ㄋㄋㄋㄋ ㄠㄠㄠㄠ ㄋㄠㄋㄠ ㄠㄋㄠㄋ ㄋ ㄠㄠ ㄋㄋㄠㄠ ㄋㄠ ㄠ ㄋ ㄠㄋ ㄋㄋ ㄋ ㄠㄠ ㄋㄋ ㄋㄋ ㄋㄋ ㄠㄋㄋㄋ ㄋㄋ ㄠㄋ ㄋ ㄠ ㄋㄋㄠㄠ ㄠㄠ ㄋㄠ ㄠㄋ ㄠㄋ ㄋㄠㄋ ㄋㄠ ㄋㄠㄠ ㄠㄋㄋ ㄠㄋㄠ ㄋ ㄋㄠㄋ ㄋㄋ ㄋ ㄠㄋㄋ ㄋㄋㄋㄠ ㄠㄋㄋㄠ ㄠ ㄋㄋ ㄠ ㄠㄋㄋ ㄋㄠ ㄠ ㄠ ㄠㄠ ㄠ ㄋㄋ ㄠㄠ ㄋ ㄠㄠ ㄠㄠㄋ ㄠㄋ ㄋㄋㄋ ㄠㄠㄋ ㄠㄠ ㄋㄠㄠ ㄠㄠㄠㄠ ㄋㄋㄠ ㄋㄋㄠㄠ ㄋㄋㄠ ㄋㄋ ㄇㄇㄇㄇ ㄤㄤㄤㄤ ㄇㄤㄤ ㄇㄤㄤ ㄤㄤㄇ  ㄇ ㄇ ㄤ ㄇㄤㄇ ㄇㄤㄇㄇ ㄤㄤㄤㄤ ㄤㄤㄇ ㄤ ㄤㄇㄤ ㄇ ㄇ ㄇ ㄇㄤㄇ ㄇㄇ ㄇㄤ ㄇㄤ ㄇㄇㄇ ㄇㄇㄤ ㄤㄤ ㄤㄤ ㄤㄇㄤ ㄤㄇ ㄤㄤ ㄤㄤㄇㄇ ㄤㄇ ㄇ ㄇㄤㄤ ㄤㄇ ㄤㄤ ㄇ ㄤ ㄤㄇㄤ ㄤㄤㄇ ㄤㄤㄤ ㄇㄇㄤ ㄤ ㄇㄤ ㄤㄇㄇ ㄤㄤㄤ ㄤㄤ ㄤㄇ ㄇㄤㄤ ㄤㄤㄤ ㄤ ㄤ ㄤㄇ ㄤ ㄤㄇㄤ ㄇㄤ ㄤ ㄤㄇㄤ ㄤ ㄇ ㄇ ㄤㄇㄇ ㄤㄤㄇ ㄤㄤ ㄤ ㄤ ㄤㄇㄤ ㄇㄇ ㄤㄋ ㄠㄇ ㄤ ㄋㄇ ㄠㄤ ㄇㄤㄤ ㄋㄋ ㄤㄤㄇ ㄤㄇㄋㄇ ㄋㄇㄇ ㄋㄋ ㄤ ㄠ ㄋ ㄤㄤㄇ ㄋㄇ ㄋ ㄤㄋ ㄠㄋ ㄤㄤ ㄋㄤㄠ ㄋㄠㄤ ㄠㄤ ㄇ ㄋㄤ ㄋㄤㄋ ㄠㄤㄠㄤ ㄤㄋ ㄇㄇ ㄋㄠ ㄋㄋ ㄤ ㄠ ㄇㄋ ㄠㄋ ㄇㄤ ㄠ ㄠ ㄋㄋㄤ ㄠㄇㄠㄤ ㄤㄤㄋ ㄇㄇㄤ ㄤ ㄋ ㄇㄠㄇㄠㄤ ㄠ ㄋㄇ ㄠㄤ ㄇ ㄋ ㄋㄋ ㄇ ㄋ ㄠㄇ ㄤㄤ ㄋ ㄠ ㄇ ㄋㄇㄠ ㄠㄇㄤㄇ ㄇ ㄇㄇ ㄋ ㄠ ㄤㄇ ㄋㄠㄋ ㄠㄤ ㄠㄇ ㄇㄠ ㄠㄤ ㄋㄋ ㄠ"
threeS = "ㄕㄕㄕㄕ ㄘㄘㄘㄘㄘ ㄕㄕㄕㄘ ㄕㄘ ㄘㄘㄘ ㄕㄘㄕ ㄘ ㄘㄘ ㄘㄘㄕ ㄕㄕㄕ ㄕㄘㄕㄕㄕ ㄕ ㄘㄘ ㄘㄘㄕ ㄘ ㄘㄘ ㄕ ㄕㄘ ㄕㄕㄘ ㄘㄕㄕㄕ ㄘㄕㄘ ㄕㄕ ㄘ ㄘㄘ ㄕㄘ ㄕㄕㄕㄕ ㄕ ㄘㄕㄘ ㄘㄕㄕ ㄘㄘㄕ ㄕ ㄘ ㄕ ㄕㄕ ㄘ ㄕ ㄕ ㄘ ㄘㄘㄕㄘ ㄕㄕ ㄘㄕ ㄕㄕㄘㄕ ㄕㄘㄘ ㄘ ㄘㄕㄕ ㄕㄘ ㄕㄘㄘ ㄕㄕ ㄘㄕ ㄕㄘ ㄕㄘ ㄘㄕㄕ ㄕ ㄘㄕㄘ ㄕㄕ ㄘ ㄘㄘ ㄕㄘ ㄕㄕㄕㄕ ㄕ ㄘㄕㄘ ㄘㄕㄕ ㄘㄘㄕ ㄕ ㄘㄕ ㄘㄘㄘ ㄕㄕ ㄘ ㄘㄘㄘ ㄘ ㄘㄘ ㄘㄘ ㄕ ㄕ ㄕㄘ ㄘ ㄘ ㄘ ㄕ ㄘㄕ ㄘㄘ ㄘㄘ ㄘ ㄕㄘ ㄘㄘ ㄘ ㄘㄘ ㄘㄕ ㄘㄕ ㄘ ㄕㄘㄘ ㄕㄕㄕ ㄘㄕ ㄕ ㄕㄘㄘㄕ ㄕㄕ ㄕ ㄕ ㄕㄕㄘ ㄘ ㄕㄕ ㄕㄕ ㄘㄘ ㄕ ㄘㄕ ㄘ ㄘ ㄕ ㄘ ㄘㄘ ㄘ ㄕㄘ ㄘ ㄘㄘ ㄕㄘ ㄕ ㄕ ㄕ ㄕㄘㄕ ㄕ ㄘㄘ ㄕ ㄘㄕㄘ ㄘㄘ ㄕㄕ ㄘㄘ ㄘㄘㄘ ㄕㄕ ㄘㄕ ㄕㄕ ㄘㄕ ㄘ ㄘㄕㄕ ㄘㄘ ㄕ ㄘㄕㄕㄕ ㄘㄘㄘㄘ ㄘ ㄘㄘ ㄘㄘㄕ ㄕ ㄘㄕ"
fourS = "ㄤㄑㄋ ㄠ ㄤㄑ ㄜㄠㄇㄎㄘ ㄨㄎ ㄤㄨ ㄠㄨ ㄋㄎㄠㄤ ㄋ ㄋㄑ ㄜ ㄠㄤㄇㄑ ㄑㄠ ㄨ ㄕㄘㄠ ㄜㄤ ㄨ ㄑㄎ ㄇㄜㄑㄑ ㄋ ㄕㄘ ㄇㄠ ㄠㄇㄨ ㄨㄕ ㄠㄠㄋㄠ ㄘㄕ ㄜㄤㄋ ㄎㄕㄨㄤ ㄨㄑㄠ ㄕㄜㄤㄠㄕ ㄜㄜㄋ ㄠ ㄤㄨㄇ ㄤㄠ ㄇㄤㄠ ㄋㄤ ㄠ ㄎ ㄇㄋ ㄇㄕㄘ ㄜ ㄘㄘㄨ ㄠㄨ ㄠㄜㄨㄇ ㄋㄋ ㄜㄘㄘㄠ ㄨㄕ ㄜㄠㄑㄤ ㄑㄘ ㄎㄕㄇㄕ ㄇㄨ ㄇㄨ ㄠㄑ ㄇㄕ ㄑㄎㄤ ㄎㄨ ㄤ ㄠㄠㄤㄨ ㄑㄇㄜㄋ ㄎㄕ ㄠㄤㄜ ㄑㄘㄠㄎ ㄋㄇㄕㄜ ㄘㄕㄤㄨ ㄨㄠㄠㄤ ㄤㄨㄇㄑ ㄎㄋ ㄜㄘㄎㄑ ㄨㄘ ㄨㄜㄨ ㄇㄕㄋ ㄤ ㄨㄜㄨㄎ ㄤㄋ ㄇㄋㄎ ㄎㄋㄎㄨ ㄨㄋㄜㄤ ㄋㄇ ㄎ ㄨㄕㄕ ㄑㄠㄨㄠ ㄑㄕㄨ ㄎㄜ ㄠㄜ ㄨㄎ ㄠ ㄕㄤㄎ ㄜㄜ ㄇㄕ ㄇㄎ ㄋㄋㄤ ㄎ ㄜㄨ ㄜㄑㄋ ㄑ ㄨ ㄠ ㄠ ㄜㄇㄎ ㄎ  ㄜ ㄨ ㄠㄨㄤ ㄘ ㄜ ㄨㄤ ㄎ ㄤㄋ ㄨㄨ ㄘ ㄑ ㄤㄘㄑ ㄘ ㄘㄘ ㄎㄋㄑㄜ ㄑㄎ ㄋㄎ ㄎ ㄜㄇ ㄇㄎㄘ ㄜㄑ ㄑㄜㄎ ㄎㄠ  ㄎ ㄨ ㄎ"
fiveS = "ㄔㄔㄔㄔ ㄗㄗㄗㄗ ㄔㄔ ㄔㄔ ㄗㄔㄔ ㄔㄗㄗㄔ ㄔㄗㄗ ㄗㄔ ㄔㄗㄗㄔㄗ ㄔ ㄔ ㄗㄔㄔㄗ ㄗㄗㄔㄗ ㄗㄔㄗ ㄔ ㄔㄗ ㄔ ㄗㄗㄔ ㄗㄗㄔㄗ ㄔㄔㄗ ㄗ ㄔㄗ ㄔㄗ ㄗㄔ ㄔㄗ ㄔㄔㄔㄔ ㄗㄗㄗ ㄔㄗㄗ ㄔㄗ ㄔㄔㄗ ㄔㄗ ㄗㄗ ㄔ ㄗㄗ ㄗ ㄗㄗㄔ ㄔㄗ ㄗㄔㄗ ㄔㄗㄔㄔ ㄗㄔ ㄗㄔ ㄗ ㄔ ㄗㄗㄗ ㄔㄔㄔ ㄔㄗㄗ ㄗㄗㄔ ㄗㄔㄗㄗ ㄔㄔㄗ ㄗㄔㄗ ㄔㄔㄗㄔ ㄗㄔㄔ ㄗㄔ ㄔㄔㄗㄗ ㄔㄗㄗ ㄔㄗ ㄐㄐㄐㄐ ㄧㄧㄧㄧ ㄧㄐㄧ ㄧㄧ ㄐㄧㄐ ㄧㄐ ㄐㄐㄐㄧ ㄐㄧㄐ ㄧㄐ ㄐ ㄐㄧㄐ ㄐㄧ ㄐㄐ ㄧㄧㄧ ㄐㄐ ㄐㄐㄧ ㄧㄧㄐ ㄧ ㄐㄐㄐ ㄧㄐ ㄧㄧㄧ ㄐㄐㄐㄐㄐ ㄧㄐ ㄧㄧㄐ ㄐㄧㄐ ㄧㄐㄐ ㄧ ㄐ ㄧㄐㄧ ㄐㄧㄐ ㄐㄐ ㄐㄐ ㄧㄧㄐ ㄐㄧㄧ ㄐㄧ ㄐㄧ ㄧㄐㄧ ㄐㄐ ㄐㄐㄧ ㄧㄐㄐ ㄧㄐㄧ ㄐㄐ ㄐ ㄐ ㄧㄐㄐ ㄐ ㄐㄧㄐㄐㄐ ㄐㄧ ㄧㄧ ㄐㄧㄧㄧㄐ ㄧㄧㄐ ㄐㄧ ㄧㄐㄧ ㄐㄐㄧ ㄐㄧ ㄧㄐㄐ ㄐㄐㄐ ㄧㄐㄐㄔ ㄔㄔㄐ ㄗㄧ ㄔㄧㄗ ㄐㄗㄐ ㄐ ㄗㄐ ㄧ ㄔㄐㄗㄗ ㄔㄔ ㄐㄔ ㄧ ㄐ ㄔㄐㄐㄔ ㄧㄗㄗ ㄐㄗ ㄐㄐ ㄗㄗ ㄧ ㄧ ㄗ ㄐㄗㄗ ㄔ ㄔㄧ ㄧ ㄔㄧㄧㄔ ㄐㄐ ㄗ ㄔㄐㄧ ㄧㄔ ㄔ ㄗㄐㄐㄔ ㄧㄗㄐ ㄗ ㄔㄗ ㄔ ㄗ ㄐㄔㄧ ㄐㄔ ㄔ ㄐ ㄧㄐ ㄐㄧ ㄐㄗ ㄧ ㄐ ㄔ ㄔㄐㄐ ㄧㄐ ㄗ ㄐ ㄗㄧㄐㄐ ㄔㄐㄗ ㄧㄗㄔ ㄐㄗ ㄧㄐㄐ ㄧㄧㄧㄧ ㄧㄧ ㄐ ㄐㄧ ㄐ ㄧㄐㄔㄐ ㄧ ㄔ ㄗㄔㄧ ㄧㄗ ㄧ ㄗ ㄗ ㄐㄔㄐ ㄔㄐ"
sixS = "ㄍㄍㄍㄍ ㄛㄛㄛㄛ ㄛㄛㄛ ㄛㄍㄛ ㄛㄍ ㄛㄍㄍ ㄍ ㄍㄛ ㄍ ㄛㄛ ㄛㄍㄍ ㄛㄛ ㄛ ㄛㄍ ㄛㄛ ㄍ ㄍㄍ ㄛ ㄛㄍㄍ ㄛㄍㄛ ㄛㄍㄍ ㄛㄍㄛㄍ ㄛㄛㄛ ㄛㄛ ㄍ ㄍ ㄛ ㄛㄍㄍ ㄛ ㄍ ㄍㄍㄛ ㄍ ㄛㄛㄍ ㄍ ㄛㄍ ㄛ ㄛ ㄛㄛ ㄛ ㄛ ㄛㄍㄛ ㄍ ㄍㄍㄛㄍ ㄛ ㄛ ㄍ ㄛㄍ ㄛ ㄛ ㄛ ㄛㄍ ㄍㄛ ㄍ ㄛ ㄛ ㄍ ㄛ ㄛㄍ ㄛㄍ ㄍㄛ ㄛㄍ ㄍㄛ ㄍㄍ ㄍㄍ ㄛㄛ ㄛㄛ ㄍㄛ ㄍㄍㄛ ㄛ ㄍㄛㄍㄍ ㄍㄍ ㄍㄍㄍ ㄛㄍㄛㄛ ㄍㄛ ㄊㄊㄊㄊ ㄟㄟㄟㄟㄟ ㄊㄊㄟ ㄟㄊ ㄟㄟ ㄟㄊㄟ ㄟㄟ ㄊㄟㄊ ㄟㄊㄟ ㄊㄊㄟ ㄊ ㄊ ㄊㄟ ㄟ ㄊㄟㄟ ㄊ ㄟ ㄊㄊㄟ ㄊㄊㄟㄟ ㄟㄟ ㄊㄊㄊ ㄟㄊ ㄊ ㄟㄊ ㄟㄟ ㄊ ㄊ ㄊ ㄟㄟ ㄊ ㄟ ㄟ ㄊ ㄊㄟㄟ ㄟ ㄊㄊㄟ ㄟ ㄊㄟ ㄊ ㄟㄟㄟ ㄊㄟ ㄟㄊ ㄟㄊ ㄟㄊㄟㄟ ㄊㄟ ㄊㄟ ㄟ ㄟㄟㄟ ㄊㄊ ㄊㄟㄊ ㄟㄟ ㄊㄟㄊ ㄊ ㄟ ㄟㄊㄊ ㄊ ㄊㄊ ㄟ ㄟ ㄊㄟ ㄊ ㄊㄟ  ㄊㄟㄊㄊㄊ ㄟ ㄊㄟㄊㄟ ㄟㄟ ㄟㄊ ㄟㄟ ㄟㄟ ㄊ ㄟ ㄊㄟㄍㄊ ㄊ ㄊ ㄊㄍ ㄍㄍ ㄍ ㄟㄊㄍ ㄍㄟ ㄛㄟ ㄊ ㄍㄟ ㄍㄍㄍ ㄊㄊ ㄍ ㄍㄛㄛㄊ ㄍㄍ ㄍㄍㄟ ㄍㄟ ㄛ ㄍ  ㄍㄟ ㄍㄊ ㄛㄍㄛㄟ ㄟ ㄛㄛ ㄟㄍㄛ ㄊㄛ ㄟㄊㄍ ㄍ ㄊ ㄊㄍㄟ ㄛㄍ ㄍㄊ ㄍㄟ ㄍ ㄍㄟㄛㄍ ㄛ ㄍㄍㄟㄛ ㄊㄟ ㄊㄍㄟㄍ ㄍㄟ ㄍㄛㄊ ㄟㄊㄛㄊ ㄍㄛㄟㄍㄍㄍ ㄛㄊㄟ ㄍ ㄟㄍㄊ ㄟㄟ ㄍ ㄊㄍㄛㄍ ㄍㄍ ㄊㄛㄛ ㄊㄟㄛㄊ ㄟㄍ ㄊㄍㄛㄍ ㄍㄊ ㄛㄛㄊㄍ ㄊㄟ ㄍㄊ ㄍㄊㄍ"
sevenS = "ㄆㄆㄆㄆ ㄣㄣㄣㄣ ㄣㄆ ㄆㄣㄣㄣ ㄣ ㄆㄣ ㄣㄣㄣ ㄣㄆ ㄣ ㄣㄆ ㄆ ㄣㄆㄆ ㄆㄣ ㄆㄣㄆㄣ ㄣㄣㄣ ㄆㄣㄆ ㄆㄆ ㄣㄆ ㄆ ㄣㄣㄆ ㄆㄣ ㄆㄆ ㄣㄣㄆ ㄆ ㄣㄆ ㄆ ㄣ ㄆ ㄣ ㄣ ㄣ ㄣㄣ ㄣ ㄆㄆ ㄣ ㄣㄣㄣ ㄣㄣ ㄆㄆ ㄣ ㄆㄣ ㄆ ㄣㄣ ㄆㄣㄣㄣ ㄆㄆㄆㄆ ㄣㄣ ㄣㄆㄆ ㄣ ㄣ ㄆㄣ ㄣㄆ ㄣㄣ ㄆ ㄣ ㄣ ㄆ ㄆ ㄣㄣㄣ ㄆㄣ  ㄣㄣㄣㄣ ㄣㄣㄆ ㄣㄣ ㄣㄆ ㄆㄆ ㄆㄆ ㄆㄆ ㄆㄆㄆ ㄆ ㄣㄆ ㄣㄣㄆㄣ ㄆㄆ ㄣㄣ ㄆ ㄆㄣㄆㄣ ㄣㄆ ㄆㄆ ㄆㄣㄆ ㄣㄣ ㄣㄣ ㄣㄆ ㄣ ㄣㄆ ㄣㄆ ㄆㄣ ㄆ ㄆ ㄣ ㄣㄣ ㄣㄣㄣ ㄆ ㄣㄣ ㄆ ㄣㄣ ㄣ ㄆ ㄆ ㄣㄣㄆ ㄆㄣ ㄣ ㄣ ㄆ ㄆ ㄣㄣ ㄣ ㄆ ㄆㄣ ㄆ ㄣㄣ ㄣㄣ ㄣ ㄆ ㄣ ㄆ ㄣㄣ ㄣㄆ ㄆㄣ ㄆ ㄣㄣㄣ ㄆ ㄆ ㄣㄣ ㄆ ㄣ ㄣㄆㄣ ㄆ ㄣㄣㄣ ㄣ ㄆㄆ ㄣ ㄣ ㄣㄣㄣ ㄣ ㄆㄆㄆ ㄆ ㄆ ㄆㄣ ㄆㄣ ㄣ ㄆ ㄣ ㄣ ㄆ ㄣ ㄆㄣ ㄣㄆ ㄆ ㄣㄣ ㄆ ㄣ ㄆㄣㄣ ㄆ ㄣ ㄆ ㄆ ㄆㄣㄣ ㄆ ㄣㄣ ㄆㄣㄣ"
eightS = "ㄊㄆㄗㄣ ㄔㄗㄍㄔ ㄛㄍㄍ ㄐㄟ ㄛㄗㄗㄟ ㄧㄐㄧㄆ ㄧㄔㄧ ㄟㄆㄐ ㄣㄊㄍㄊㄟ ㄣ ㄔ ㄔㄊㄟㄆ ㄐㄟㄆㄣ ㄔ ㄛㄗ ㄐ ㄧㄣㄗ ㄛ ㄊㄗㄐ ㄐ ㄣㄣ ㄧㄧㄧ ㄔㄔ ㄍㄐㄔㄍ ㄐ ㄊ ㄗㄔㄟ ㄗ ㄍ ㄣㄗㄐ ㄟㄔ ㄔ ㄊㄊ ㄐ ㄗㄊ ㄟ ㄛㄆㄊ ㄆ ㄐ ㄔㄣㄔㄗ ㄛ ㄍㄛㄧㄊ ㄆㄣ ㄔ ㄔㄊㄛ ㄔ ㄣㄍㄟㄐ ㄆ ㄗ ㄛㄣㄧㄆ ㄔㄆㄆ ㄐ ㄟㄟ ㄣㄗ ㄛㄣ ㄧㄊ ㄣㄛ ㄆ ㄧㄔ ㄣㄊㄐ ㄍㄐㄐ ㄗ ㄊㄗㄍ ㄣ ㄍ ㄆㄟㄟㄟ ㄟㄊ ㄧㄔㄛㄣ ㄣ ㄆ ㄛㄗ ㄗㄐ ㄍ ㄔㄟㄗㄔ ㄟ ㄛ ㄗㄧㄔㄛㄍ ㄊㄧ ㄐㄟ ㄟ ㄊ ㄍㄛㄣ ㄐㄧ ㄊ ㄔㄟ ㄟㄧㄊㄍ ㄟㄐㄟㄍ ㄍㄗㄛㄆ ㄔㄔ ㄋㄠㄋㄤ ㄠㄋ ㄠㄠㄔ ㄇㄋ ㄤ ㄨㄜㄗ ㄠㄇ ㄤ ㄠㄗ ㄟㄨㄊㄜ ㄜㄛㄣ ㄜㄋㄋ ㄘㄤ ㄣㄋㄍㄜ ㄔ ㄤㄧ ㄎㄧ ㄟㄛ ㄇㄆㄍㄘ ㄔㄊㄕ ㄐㄊㄠㄆ ㄕ ㄎㄘ ㄘㄤㄗ ㄣㄜ ㄊㄤㄟㄊ ㄠ ㄎㄜ ㄔㄋㄕㄧ ㄋㄨ ㄧㄗㄔㄎ ㄔ ㄜㄎ ㄟㄋㄗㄧ ㄣㄐㄔㄤ ㄔㄔㄕㄊ ㄣㄨ ㄔㄆ ㄇㄎㄎ ㄊㄗ ㄔ ㄣ ㄋㄋㄕ ㄠ ㄆ ㄆ ㄘㄨㄔ ㄔ ㄜ ㄋㄛ ㄧ ㄕ ㄗ ㄋㄣㄨ ㄆㄔ ㄍ ㄇㄐ ㄟㄕ ㄊㄟ ㄆㄎ ㄔㄣㄎㄤㄘ ㄘ ㄛㄤㄊㄔ ㄜㄎ ㄔ ㄤ ㄗㄜㄍ ㄗㄘ ㄗㄇㄎ ㄕㄆㄆ ㄎㄜㄔ ㄘㄤ ㄗㄊㄣ ㄊㄠㄛ ㄤㄣㄜ ㄛㄋ ㄜㄛ ㄨㄍ ㄐㄕㄔ ㄊㄔ ㄊㄋㄋㄛ ㄧㄨ ㄛㄔㄨ ㄐㄤ ㄠㄔㄍㄠ ㄗㄎ ㄕ ㄠㄠㄛ ㄠㄆㄘ ㄔㄎ ㄔ ㄔㄔ ㄔㄕㄊ ㄍㄣ ㄧㄗㄟㄆ ㄇㄧㄛㄆ ㄆㄐ ㄜㄋㄋㄍ ㄠ ㄆㄊㄤㄕ"
nineS = "ㄖㄖㄖㄖ ㄙㄙㄙㄙ ㄙㄙㄖ ㄖㄖㄙ ㄖ ㄙㄙㄖ ㄙㄖ ㄖㄖ ㄖ ㄙㄙㄖ ㄖㄖ ㄙ ㄖㄙ ㄙㄖㄙ ㄙ ㄙㄙ ㄙ ㄖㄖ ㄖㄙ ㄖ ㄙ ㄖ ㄖㄖ ㄖ ㄖㄖ ㄖ ㄙ ㄖ ㄙㄖㄖㄖ ㄙ ㄙㄙㄖ ㄙㄖ ㄖㄙㄙ ㄖㄖ ㄖ ㄙㄖ ㄖㄖ ㄖ ㄖ ㄖ ㄖㄖ ㄖ ㄖ ㄖ ㄙ ㄙ ㄙ ㄙ ㄙ ㄙㄙ ㄙ ㄖㄖ ㄖ ㄙㄙ ㄙ ㄙ ㄖㄙ ㄖ ㄖ ㄙ ㄙ ㄙㄙ ㄖ ㄙ ㄖ ㄙ ㄖ ㄖ ㄙㄖ ㄙ ㄖㄙㄖ ㄖㄙ ㄖ ㄙㄙ ㄖ ㄙㄙㄖ ㄙㄙ ㄖ ㄙ ㄖㄙ ㄖ ㄖ ㄙ ㄙㄙ ㄙ ㄙㄖ ㄖ ㄖㄙ ㄒㄒㄒㄒ ㄩ ㄩ ㄩ ㄩ ㄩㄒ ㄒㄒㄒ ㄩㄩ ㄩ ㄒㄩ ㄒㄩ ㄩㄩㄒ ㄒㄒ ㄩㄩㄩ ㄩㄩ ㄩㄒㄩㄒ ㄩ ㄩㄩㄒ ㄩ ㄩㄒㄩㄒ ㄩㄒㄩ ㄩㄒㄩㄩ ㄩㄩ ㄩ ㄒㄩㄒ ㄩㄒ ㄩㄩㄩ ㄒㄒ ㄒㄩㄩ ㄩㄒㄒ ㄒ ㄩ ㄩ ㄩㄩㄒ ㄒㄒㄩ ㄩ ㄒ ㄩㄒㄒ ㄩ ㄩ ㄒㄒ ㄒ ㄒㄩㄩㄩ   ㄩㄩ ㄩㄩ ㄒㄩㄒ ㄒㄩㄒ ㄩㄒㄒ ㄒㄩ ㄒㄒ ㄒ ㄩㄩ ㄩㄩ ㄒ ㄒㄒㄒ ㄒㄒ ㄩㄩ ㄩㄩ ㄒ ㄒㄩ ㄒㄩ ㄩ ㄩ ㄒ ㄒ ㄩ ㄒ ㄒㄒ ㄩ ㄩㄒ ㄩ ㄒ ㄖㄙ ㄙㄩ ㄒㄒㄒ ㄩㄙㄒ ㄒㄙㄩ ㄩㄙㄩㄖ ㄒㄩㄙ ㄖㄒ ㄖ ㄖㄒㄙ ㄙㄙ ㄒㄒㄖㄒㄩ ㄩㄒㄩㄒ ㄒㄒㄖㄩ ㄙㄙㄒㄖㄒ ㄩㄩ ㄩㄩ ㄙㄩ ㄒㄩㄩㄒ ㄒ ㄒㄙ ㄒ ㄒㄙㄒ ㄖㄖ ㄒ ㄙㄒㄩ ㄙㄖㄒㄩ ㄩㄖ ㄩㄙㄙ ㄒ ㄩㄒㄒ ㄩㄙ ㄩㄒㄒ ㄙㄖㄙ ㄙㄩ ㄩㄩㄙㄩ ㄩㄒㄩ ㄖㄒㄖ ㄒ ㄖㄩㄒㄩ ㄖㄒㄒ ㄒㄙㄖㄩㄙ ㄖㄙㄙ ㄩㄩㄒ ㄒㄖㄩㄖㄩ ㄙㄒ ㄙㄩㄖ ㄒㄖ ㄒㄙㄙ ㄙ ㄙㄖ ㄖㄖㄩ ㄒㄙㄙㄩ ㄖ"
tenS = "ㄏㄏㄏㄏ ㄝㄝㄝㄝ ㄏㄝㄝ ㄏㄏㄏ ㄏㄝㄝ ㄝㄝㄝㄏ ㄝㄝㄏ ㄝㄝㄏㄝ ㄝㄝㄏㄏㄏ ㄏㄏ ㄏㄝ ㄝㄏ ㄝㄝㄝ ㄝㄝㄝㄝ ㄏㄝㄏ ㄝㄏ ㄝㄝㄏ ㄝㄏ ㄝㄝㄝㄏ ㄝㄏ ㄝㄝ ㄝㄝㄝㄏ ㄏㄏㄏ ㄏㄏ ㄏㄝㄝ ㄏㄏ ㄝㄏㄝ ㄝ ㄏ ㄝㄝㄝ ㄝㄏ ㄝㄏ ㄝㄝ ㄝ ㄝ ㄏㄝㄝ ㄏㄝ ㄝㄏㄝ ㄏㄝㄏㄝ ㄝㄝㄏㄝ ㄏㄏㄝ ㄝㄝ ㄏㄝㄏ ㄝㄏㄝㄝ ㄏㄏㄏ ㄝㄏ ㄏㄏㄝ ㄏㄝㄝ ㄏ ㄏ ㄏㄝㄝ ㄝㄝ ㄝㄏㄝ ㄝㄏㄝ ㄝ ㄌㄌㄌㄌ ㄡㄡㄡㄡ ㄌㄡ ㄌㄌㄡㄌ ㄌㄡ ㄡㄌㄡ ㄌㄡㄌ ㄡㄌ ㄡㄡ ㄡㄌㄡ ㄌㄌ ㄌㄡㄌㄡ ㄡㄡ ㄌㄡ ㄡㄡㄡ ㄡ ㄡㄌ ㄡ ㄌㄡㄡㄌ ㄡㄌ ㄡ ㄌㄡㄌ ㄡ ㄌㄌ ㄌㄌㄌ ㄌㄡㄌ ㄌ ㄌㄌ ㄡㄡ ㄡ ㄡ ㄌ ㄡㄡㄌ ㄡ ㄡㄡㄌ ㄡ ㄌㄡ ㄌㄡ ㄌㄌㄡ ㄡㄌ ㄡ ㄡ ㄡㄡㄌ ㄌ ㄡㄡ ㄡㄡ ㄌ  ㄌ ㄡ ㄌ ㄡㄌ ㄌㄌ ㄌㄡ ㄌㄌㄌ ㄌㄡㄡㄡ ㄡㄡ ㄌ ㄡㄡㄡㄌ ㄡ ㄌ ㄌㄡㄌ ㄡ ㄌㄡ ㄡㄡ ㄌ ㄌ ㄌㄌ ㄡㄌ ㄡㄡ ㄌㄌ ㄏㄏㄡ ㄏㄝㄏ ㄌㄌ ㄡㄏ ㄏㄌㄡ ㄡ ㄏㄝㄝ ㄏㄌㄡ ㄏㄌ ㄝ ㄡㄌ ㄌㄏ ㄝㄡㄏㄡㄡ ㄝㄡㄝ ㄡ ㄏㄌ ㄏ ㄡㄝㄌ ㄡ ㄝ ㄏ ㄡ ㄡㄌ ㄝㄝㄝ ㄌㄌ ㄌㄌ ㄡㄏ ㄌ ㄏㄌ ㄡㄝㄏ ㄝㄡ ㄏㄝㄡ ㄏㄡ ㄌ ㄡㄏ ㄝㄡㄌ ㄡㄡ ㄌㄝㄝ ㄝㄝ ㄏ ㄡㄏㄏ ㄡㄌ ㄡㄡ ㄌ ㄌㄏ ㄝㄝ ㄡ ㄏ ㄌㄌㄡ ㄏㄝ ㄌㄌ ㄝ ㄝㄌㄌ ㄝㄏ ㄝ ㄌㄏㄏㄡ ㄏㄝ ㄏㄏㄡㄌ ㄝ ㄝ ㄡㄡㄡ ㄌ ㄏ ㄝㄌ ㄝ  ㄡㄌㄡ ㄌㄡ ㄝㄏ ㄌㄡ ㄌ"
elevenS = "ㄈㄈㄈㄈ ㄥㄥㄥㄥ ㄈㄈ ㄥㄈㄥ ㄈㄥㄥ ㄥ ㄈ ㄥㄥㄥ ㄈ ㄥ ㄥㄥㄈ ㄥ ㄥㄥ ㄥ ㄈㄥ ㄈ ㄈ ㄥㄥ ㄈㄈㄈ ㄥㄥ ㄈ ㄥ ㄥㄥ ㄈ ㄈ ㄥㄥㄈ ㄥ ㄈ ㄈ ㄈㄈㄈ ㄈ ㄥ ㄥㄥ ㄥㄥ ㄥ ㄈㄈ ㄈ ㄈ ㄈㄥㄈ ㄈ ㄥㄥ ㄥㄥㄈ ㄥ ㄥ ㄈㄥ ㄥ ㄥㄥ ㄥㄥ ㄥ ㄥ ㄥㄈㄈ ㄥ ㄥ ㄥㄈ ㄈ ㄥ ㄥㄈ ㄥ ㄥ ㄈ ㄈㄈㄥㄥ ㄈ ㄈㄥㄥ ㄈㄥ ㄥㄈ ㄥㄥ ㄥㄥㄈ ㄈ ㄈㄥ ㄥㄈ ㄥ ㄥㄥ ㄈㄥㄥㄈ ㄥㄈ ㄈ ㄈㄥ ㄥㄈ ㄈㄈ  ㄈㄈ ㄈ ㄥㄈㄥ ㄈㄈ ㄈㄥ ㄥ ㄥㄈㄥ ㄥㄈㄥㄈ ㄈㄈ  ㄈ ㄥㄥ  ㄈ ㄥ ㄥㄥ ㄥㄥ ㄈ ㄈㄥ ㄥㄥ ㄥㄈ ㄈㄈ ㄈ ㄥ ㄈㄥ ㄈ ㄈㄈ ㄈㄈㄥ ㄈㄈ ㄥㄥㄈ ㄈㄈ ㄥㄈ ㄥㄥ ㄈㄥ ㄈㄥㄈ ㄈㄈㄥ ㄈㄈㄈㄥ ㄥㄈ ㄈㄥㄈ ㄈㄥ ㄈㄥㄥ ㄥㄈ ㄈㄥ ㄥㄈㄈㄈ ㄥㄥ ㄈㄈㄥ ㄥㄈㄥㄈ ㄈㄈ ㄥ ㄈㄈㄈ ㄥㄈ ㄈㄈㄥ ㄈㄈ ㄈㄥ ㄥㄈ ㄥㄈㄈ ㄈㄈ ㄥㄥㄥ ㄈ ㄈㄥㄥ ㄥㄈㄥ ㄥㄈㄈ ㄥ ㄥㄈㄈ ㄥㄥ ㄥ ㄥㄥㄥㄥ ㄥㄈ ㄈㄥ ㄥ ㄈ"
twelveS = "ㄝㄏㄝ ㄒㄩㄖ ㄌㄖㄙ ㄝㄈ ㄈㄡ ㄒㄏ ㄈㄥㄙ ㄌㄖ ㄝ ㄌㄡ ㄖㄌㄖ ㄏㄩ ㄩㄖㄡㄡ ㄌㄒ ㄥㄌ ㄏㄡ ㄥㄒ ㄙㄙㄥㄥ ㄥ ㄌㄙㄌㄡㄒㄝ ㄙ ㄒ ㄝㄥ ㄈ ㄥㄌ ㄌㄌ ㄈㄝ ㄝㄒ ㄖ ㄏㄥㄡ ㄈ ㄒㄥ ㄙ ㄒㄥㄖ ㄌㄡ ㄌㄩㄝ ㄌㄒ ㄝㄒ ㄖㄖ ㄝㄖ ㄡㄝㄈ ㄖㄙ ㄥㄡㄙ ㄡㄝ ㄏㄈㄙㄏ ㄝㄝㄝㄏ ㄥ ㄩㄙㄈㄡ ㄖㄏㄙ ㄏㄈㄌ ㄩㄥㄖ ㄒ ㄩㄌㄙㄌ ㄏ ㄡㄒㄩㄡ ㄙㄥ ㄖ ㄙ ㄒㄥㄏ ㄡ ㄏㄡㄙ ㄏㄙㄖ ㄩㄌ ㄙㄒ ㄒ ㄡㄈㄌ ㄡㄥㄏ ㄈㄥ ㄏㄏ ㄈㄈㄌ ㄥㄖ ㄙ ㄏㄒㄒ ㄡㄥ ㄡ ㄖㄏ ㄡㄏ ㄡㄖㄈ ㄌㄙ ㄌㄖㄝㄒㄩ ㄡㄌ ㄏㄏㄙ ㄏㄡㄌㄖㄥ ㄡㄙㄩㄌㄈ ㄥㄙㄩㄡ ㄥㄩㄩㄙ ㄈㄖ ㄥㄙ ㄙㄥ ㄥㄝ ㄖ ㄏ ㄒㄆㄗ ㄕㄔㄤ ㄩㄑㄒ ㄔㄐㄑ ㄏㄐㄈㄊ ㄠㄩㄎ ㄇㄡㄑ ㄆㄏㄜㄧ ㄩㄇ ㄆㄘㄏ ㄠㄎㄏ ㄈㄘ ㄘㄠㄑㄏ ㄛㄎ ㄖㄠㄡㄩ ㄕㄈㄕ ㄨㄆ ㄐㄗ ㄔㄈㄌ ㄏㄌㄒ ㄋㄖㄐ ㄋㄒ ㄇㄆㄝ ㄡㄙ ㄗㄡㄠ ㄒㄩ ㄡㄑ ㄊㄇ ㄇㄡㄒ ㄠㄣㄍ ㄏㄛ ㄧㄝ ㄌㄐ ㄒㄘㄩ ㄡ ㄎㄍㄍㄑ ㄏㄆㄗ ㄈㄣㄙㄇ ㄌㄥㄒㄧ ㄎㄧ ㄜㄖㄘ ㄡㄆ ㄑㄤㄌ ㄇㄨ ㄝㄛㄘㄛ ㄩㄆㄔ ㄧㄑㄏ ㄧㄥㄕㄩ ㄊㄤㄎ ㄌㄒㄙ ㄗㄜㄇ ㄖㄡㄌㄈ ㄩㄒㄠㄛㄛ ㄣㄟ ㄖㄝ ㄛㄨ ㄩㄜ ㄈㄙㄗ ㄜㄡ ㄝㄐㄘㄡㄩ ㄔㄋ ㄇㄈㄊ ㄠㄡㄒ ㄖㄘㄨㄆ ㄑㄛ ㄤㄐㄣ ㄠㄤ ㄩㄕㄘㄇ ㄔㄩ ㄤㄤㄇ ㄈㄇ ㄎ ㄠㄊㄤㄧ ㄩㄝㄑ ㄝㄆ ㄆㄘ ㄆㄟ ㄐㄍㄝ ㄜㄔㄤ ㄋ"
thirteenS = "ㄅㄅㄅㄅ ㄉㄉㄉㄉ ㄓㄓㄓㄓ ㄓㄓㄓㄉㄓ ㄉㄅ ㄓㄅ ㄅ ㄓㄉㄓ ㄉ ㄅㄉㄓ ㄅㄉ ㄉㄅㄓ ㄓ ㄉㄅㄓ ㄉㄓ ㄉㄅㄉ ㄓㄓ ㄉㄉㄉ ㄉㄅ ㄉㄓㄅ ㄓㄓ ㄓ ㄅㄅㄉ ㄅ ㄓㄉ ㄅㄓㄓ ㄓ ㄉㄓㄓ ㄓ ㄉㄅ ㄓ ㄉㄉ ㄉ ㄓㄓ ㄓ ㄓ ㄓ ㄅㄉㄅ ㄅㄉㄅ ㄅㄅ ㄓㄉ ㄉㄉ ㄓㄉ ㄉㄅ ㄅ ㄉ ㄓㄉㄅㄅ ㄅㄓㄅㄅ ㄓㄅ ㄅㄓ ㄉㄉ ㄉㄓ ㄉㄉㄉ ㄉㄅㄓ ㄅ ㄉㄅㄅㄅ ㄅ ㄅㄓ ㄅㄓ ㄓ ㄉㄉㄓㄉㄅ ㄉㄉㄅ ㄅㄉㄅ ㄅㄓ ㄅㄓ ㄓㄓ ㄅㄉㄅ ㄉㄅ ㄉ ㄓㄉㄅ ㄓㄓㄅ ㄓㄉㄉ ㄉㄅㄅ ㄉ ㄓ ㄉㄉㄉㄅ ㄉㄅ ㄉㄉㄅㄓ ㄅㄉㄉㄉ ㄅ ㄉ ㄅㄓ ㄅ ㄓ ㄉ ㄓㄓㄓ ㄉㄅㄉ ㄅㄅㄉ ㄅㄓㄉ ㄓㄓ ㄅㄓㄉ ㄓㄅㄓㄓ ㄓㄉ ㄉㄅㄉ ㄉㄅㄓ ㄉㄅㄓㄓ ㄉ ㄓ ㄅㄅ ㄓㄉㄉ ㄅㄉㄉ ㄉㄅㄅ ㄅㄅ ㄅ ㄉㄉㄉㄅ ㄉㄓ ㄅㄉㄅ ㄓ ㄉㄅ ㄓㄅ ㄅ ㄉㄓㄅㄓㄅ ㄅㄓ ㄅㄓㄅ ㄅㄉ ㄅㄅㄅ ㄉ ㄅㄅㄅㄅ ㄅㄅ ㄅ ㄅㄉㄉㄅ ㄉ ㄅㄉㄉ ㄓㄅ ㄓㄅㄉ ㄅㄓ ㄅㄅㄅㄉ ㄓㄓㄉ ㄅㄓ ㄅㄉ ㄅ ㄅㄉㄓㄅ ㄅ ㄓㄓ ㄅ ㄓㄓㄓ ㄉㄓ ㄓ ㄓ ㄓㄓ ㄓㄅㄅㄓ ㄓ ㄅㄓㄉ ㄉㄅ ㄅㄅㄓㄅ ㄉㄉ ㄓㄅㄅ ㄉㄉ ㄅㄅ ㄓㄓㄉ ㄅㄅㄉ ㄅㄓ ㄓㄅㄓ ㄓㄉ ㄓㄉㄉ ㄅㄅㄓ ㄅㄉ ㄅㄉㄅ ㄅㄓ ㄉㄉㄓㄅ ㄓㄅ ㄅㄅㄓㄉ ㄉㄉㄅ ㄓ ㄉㄉㄅ ㄉㄓㄅ ㄓㄉ ㄓㄓㄅ ㄓㄅㄉㄅ ㄉㄓㄓ ㄉㄓ ㄅㄅㄓㄉ ㄉㄅ ㄅㄉ ㄓㄅㄅㄅ ㄓㄅ ㄓㄓㄉ ㄉㄉ ㄅㄉㄉ ㄓㄓㄅ ㄓㄓㄅ ㄅㄓ ㄅㄅㄉ"
fourteenS = "ㄚㄚㄚㄚ ㄞㄞㄞㄞ ㄚㄚ ㄚㄚㄞ ㄚㄚㄞ ㄞㄚㄞ ㄞㄚㄞ ㄞㄞ ㄚㄚ ㄚㄚ ㄚㄚㄞ ㄞㄞㄚ ㄚㄞ ㄚㄞㄞ ㄞㄚㄞ ㄚㄚ ㄚㄞㄚ ㄚㄚ ㄚㄚㄚㄞ ㄚㄚ ㄞㄚㄞㄚ ㄞㄞㄞ ㄞㄚㄞ ㄚㄞㄞㄚ ㄞㄞ ㄚㄚㄚ ㄞㄞㄚㄚㄞ ㄞㄚ ㄚ ㄚㄞㄚ ㄞ ㄞㄚ ㄞㄚㄞㄞ ㄚㄞ ㄞㄚㄞ ㄞㄚ ㄞㄞㄚ ㄚㄚㄞ ㄚㄚㄞㄞ ㄞㄞㄞ ㄚ ㄞ ㄞㄚㄚㄞ ㄚㄞ ㄚㄚㄚㄞ ㄞㄚ ㄞㄞㄞㄚ ㄚ ㄚㄞㄚㄚ ㄞㄚ ㄞㄚㄞ  ㄚㄚㄚ ㄞ ㄞㄞㄚ ㄞㄚ ㄢㄢㄢㄢ ㄦㄦㄦㄦ ㄦㄦㄢ ㄦㄢ ㄢㄢㄦ ㄢㄢㄢ ㄢㄢ ㄦㄢㄦ ㄦㄢㄦㄦ ㄢㄢㄦㄦㄦ ㄢㄦ ㄦㄦㄦ ㄢㄦ ㄦㄢ ㄦ ㄦㄢ ㄢㄢㄦ ㄦㄦ ㄢㄦ ㄢㄢㄦ ㄦㄦㄦ ㄢ ㄢㄢ ㄦ ㄦ ㄢㄢㄢ ㄢ ㄢ ㄢㄢㄢ ㄢㄢ ㄢㄢㄢ ㄦ ㄢㄢ ㄦ ㄢㄦ ㄢㄢ ㄦ ㄦ ㄦㄢ ㄢㄦㄢ ㄢㄦ ㄢㄢㄢ ㄢㄢ ㄢㄢㄦ ㄦ ㄦ ㄦ ㄢㄦ ㄦㄦ ㄦㄦ ㄦㄢ ㄢㄢㄦ ㄦㄦ ㄢㄢㄦ ㄢ ㄦㄢㄢㄦ ㄦㄢㄢ ㄢㄢ ㄦㄦㄢ ㄢㄢㄦ ㄢ ㄦㄦㄢㄢ ㄢㄦ ㄦ ㄦㄞㄞ ㄞㄦ ㄚㄚㄞ ㄚㄚㄢㄞ ㄢㄢㄦㄞ ㄞㄢㄦ ㄢㄚㄞㄢㄦ ㄞㄞㄚ ㄞㄚㄚ ㄦㄚㄦ ㄢㄢ ㄚㄦ ㄢㄞㄚ ㄦㄦㄦ ㄢㄞㄚ ㄚㄚㄞㄞ ㄢㄦ ㄢㄚ ㄢㄦ ㄞㄚㄢ ㄞㄦ ㄦㄦ ㄞㄢㄚ ㄦㄦㄦ ㄦㄢㄢㄦ ㄚ ㄞ ㄚㄦㄦ ㄚㄦ ㄞ ㄦㄞㄚ ㄞㄢㄞ ㄚㄞㄚ ㄞㄞ ㄦ ㄞㄚㄞ ㄚㄦ ㄚㄞㄚㄦ ㄚㄦ ㄚㄢㄦ ㄦㄦ ㄞㄢㄚㄢ ㄚㄢㄦ ㄚㄢㄞ ㄦㄦㄚ ㄞㄚ ㄚ ㄞㄚ ㄚㄚ ㄚㄞ ㄦ ㄦㄞㄦ ㄦㄞ ㄚㄚ ㄢㄦ ㄢ ㄢㄦ ㄞㄦ"
fifteenS = "ˇˇˇˇ ˋˋˋˋ ㄏㄣˇ ㄒㄧㄚˋ ㄐㄧㄡˇ ㄧˇ ㄗㄞˋ ㄖˋ ㄅㄣˇ ㄒㄧㄠˇ ㄘㄨㄣ ㄌㄨㄛˋ ㄌㄧˇ ㄓㄨˋ ㄨㄟˋ ㄌㄠˇ ㄍㄨㄥ ㄏㄢˋ ㄌㄠˇ ㄊㄚ ㄅㄨˋ ㄏㄠˇ ㄩˋ ㄙㄨㄛˇ ㄧˇ ㄉㄠˋ ㄏㄛˋ ㄍㄠˋ ㄋㄚˇ ㄌㄩˇ ㄕㄨˋ ㄕㄤˋ ㄊㄧㄠˋ ㄐㄧˇ ㄧㄠˋ ㄑㄩ ㄖˋ ㄍㄟˇ ㄨㄛˇ ㄎㄢˇ ㄎㄜˇ ㄌㄨˋ ㄑㄧㄚˋ ㄨㄤˋ ㄐㄧˋ ㄏㄨ ㄒㄧ ㄉㄠˋ ㄉㄧˇ ㄎㄤˋ ㄐㄩˋ ㄍㄨㄛˇ ㄅㄨˋ ㄍㄡˋ ㄅㄟ ㄕㄤ ㄐㄧㄡˋ ㄈㄚˇ ㄩㄝˋ ㄍㄨㄤ ㄎㄜˇ ㄧㄡˇ ˊˊˊˊ ˙˙˙˙ ㄑㄧㄢˊ ㄉㄜ˙ ㄧˊ ㄍㄜ˙ ㄖㄨˊ ㄘㄨㄥˊ ㄓㄜ ˙ ㄍㄨㄥ ㄆㄛˊ ㄆㄛ˙ ㄇㄣ˙ ㄘㄥˊ ㄕㄥ ㄏㄞˊ ㄗ˙ ㄋㄧㄢˊ ㄆㄟㄥˊ ㄔㄤˊ ㄅㄧㄝˊ ㄕ ㄊㄨˊ ㄖㄢˊ ㄏㄛˊ ㄗ˙ ㄋㄚ ㄉㄜ˙ ㄖㄨˊ ㄌㄜ˙ ㄍㄨ ㄉㄨˊ ㄏㄨㄣ ㄇㄧˊ ㄖㄤˋ ㄍㄨㄛˇ ㄋㄞˇ ㄐㄧㄡˋ ㄙㄨㄛˇ ㄧㄡˇ ㄇㄧㄢˋ ㄇㄨˋ ㄉㄡ ㄖㄨˊ ㄨˊ ㄈㄟ ㄒㄧㄤˊ ㄧㄤˊ ㄩㄢˊ ㄌㄞˊ ㄨㄟ ㄓㄜ ˙ ㄐㄧㄢ ㄑㄧㄤˊ ㄔㄥˊ ㄇㄣ˙ ㄉㄜ˙ ㄨˊ ㄑㄧㄤˊ ㄑㄧㄥˊ ㄗ˙ ㄔㄥˊ ㄉㄧㄠˋ ㄌㄠˇ ㄍㄜ ㄕㄡˇ ㄑㄧㄣˊ ㄧㄣ ㄧㄡˊ ㄗㄞˋ ㄉㄨˊ ㄅㄨˋ ㄐㄧㄢˋ ㄏㄥˊ ㄔㄨㄣ ㄔㄨㄢˊ ㄑㄧˊ ㄌㄨㄛˋ ㄈㄥ ㄒㄧㄤˋ ㄏㄞˇ ㄧㄤˊ ㄍㄢˇ ㄕㄤ ㄏㄨㄟˋ ㄒㄧㄠ ㄕ ㄐㄧㄝ ㄒㄩˋ ㄋㄧˇ ㄒㄧㄡ ㄓˇ ㄈㄨˊ ㄗㄞˋ ㄔㄤˋ ㄊㄤˊ ㄕㄢ ㄧㄠˊ ㄖㄤˋ ㄨㄛˇ ㄞˋ ㄋㄞˇ ㄖㄢˊ ㄏㄡˋ ㄅㄚˇ ㄆㄠ ㄑㄧˋ ㄨㄛˇ ㄓˇ ㄧㄠˋ ㄔㄨ ㄈㄚ ㄅㄨˋ ㄧㄠˋ ㄇㄨˋ ㄉㄧˋ ㄨㄛˇ ㄏㄨㄟˋ ㄧ ㄓˊ ㄒㄧㄤˇ ㄋㄞˇ "
sixteenS = "ㄓㄚˊ ㄓㄉ ㄞˊ ㄅㄞ ㄚㄞ ˙˙ ㄅㄢˋ ㄓㄅㄦ ㄉㄞˇ ㄢ ㄢㄓ ˙˙˙ ㄅㄚ ㄉㄉㄢㄓ ㄓㄞˊ ㄢ ㄞㄚㄦ ㄅㄞˊ ㄚㄉ ㄢㄚ ㄓㄞ ㄓㄢˇ ㄅㄞˇ ㄚ ㄦㄦ ˙˙ ㄅㄢ ㄞㄞ ㄦ ㄉㄅㄉ ㄅㄞ ㄚㄉ ㄅㄉ ㄚ ㄓㄢˋ ㄓㄚ ㄢㄉ ㄉㄦㄞ ㄓㄢˊ ㄦ ㄉㄞ ㄞˋ ㄦ ㄚㄦㄉ ㄚˇ ㄓㄓ ㄓ ㄅㄦ ㄅㄚˊ ㄅㄢㄢㄢ ㄓㄚˋ ㄉㄚˋ ㄢㄓ ㄉㄚㄓ ㄅㄚˋ ㄓㄓ ㄉㄢˋ ㄓㄞㄓ ㄞˇ ㄅㄉㄢ ㄓㄞˇ ㄞ ㄢㄢ ㄚㄞㄚ ㄅㄢˇ ㄚㄉ ㄞㄢㄢ ㄢㄦ ㄓㄞˋ ㄚㄅㄞ ㄅㄢ ㄚˋ ㄓㄚ ㄞㄉ ㄅㄢˊ ㄚㄚ ㄚˊ ㄅㄞ ㄞㄞ ㄓㄚˇ ㄉㄞˊ ㄞ ㄢㄓ ˙˙˙ ㄦㄢ ㄢ ㄢㄓㄉ ㄉㄚˇ ㄚ ㄓㄢㄞ ㄉㄢˊ ㄅㄞˋ ㄞ ㄢㄚ ㄞ ㄦ ㄦ ㄞㄓ ㄅㄚˇ ㄚ ㄉㄚˊ ㄅ ㄚ ㄢ ㄉㄞˋ ㄢㄉㄓ ㄞㄦ ㄉㄓ ㄉㄢˇ ㄅㄠ ㄇㄧˊ ㄉㄧ ˇㄐㄧㄠˋ ㄆㄨ ㄑㄧㄠˇ ㄓ ㄖㄨˋ ㄘㄞˊ ㄉㄚˋ ㄕㄟˊ ㄕㄠˇ ㄕㄥ ㄦˊ ㄋㄧˋ ㄋㄩˇ ㄆㄧㄥˊ ㄗ˙ ㄏㄨㄦˊ ㄒㄧㄤˇ ㄒㄧㄤˋ ㄨㄛˇ ㄗㄨㄟˋ ㄌㄜ˙ ㄕˇ ㄨㄛˇ ㄧㄡˇ ㄩˇ ㄊㄧㄢ ㄉㄜ˙ ㄒㄧㄣ ㄑㄧㄥˊ ㄩˇ ㄊㄧㄢ ㄉㄜ˙ ㄒㄧㄣ ㄑㄧㄥˊ ㄧㄠˋ ㄓㄢˇ ㄔˋ ㄈㄟ ㄒㄧㄤˊ ㄩㄝˋ ㄍㄨㄛˋ ㄍㄠ ㄕㄢ ㄏㄜˊ ㄏㄞˇ ㄧㄤˊ ㄉㄞˋ ㄓㄜ˙ ㄨㄛˇ ㄉㄜ˙ ㄧˇ ㄨㄤˇ ㄓㄠˇ ㄍㄜˋ ㄉㄧˋ ㄈㄤ˙ ㄇㄞˊ ㄘㄤˊ ㄧㄡ ㄕㄤ ㄔㄤˋ ㄧ ㄉㄨㄢˋ ㄙ ㄒㄧㄤˇ ㄑㄧˇ ㄔㄤˋ ㄊㄤˊ ㄕㄢ ㄧㄠˊ ㄗㄡˇ ㄅㄨˋ ㄐㄧㄣˋ  ㄖㄨˊ ㄗㄨˇ ㄒㄧㄢ ㄉㄜ˙ ㄅㄨˋ ㄌㄩˇ ㄅㄠˋ ㄓ ㄌㄠˇ ㄩㄝˋ ㄑㄧㄣˊ ㄙㄢ ㄌㄧㄤˇ ㄕㄥ ㄅㄨˋ"

#put the Zhuyin strings into a list
stringList = [oneS, twoS, threeS, fourS, fiveS, sixS, sevenS, eightS, nineS, tenS, elevenS, twelveS, thirteenS, fourteenS, fifteenS, sixteenS]

#make list of length of each string
totalList = totalLength(stringList)

#split each lesson into an array of Zhuyin characters
#a 2D array
splitList = splitList(stringList)

#translate each lesson into an array of keys and stores every into keyList
#keyList is a 2D array!
keyList = []
for i in splitList:
    keyList.append(makeKey(i))



#popup box for each message
oneD = "ㄑ is typed with the left pointer finger. It is located on the f key.\nㄨ is typed with the right pointer finger. It is located on the j key.\nㄎ is typed with the left middle finger. It is located on the d key.\nㄜ is typed with the right middle finger. It is located on the k key."
twoD = "ㄋ is typed with the left ring finger. It is located on the s key.\nㄠ is typed with the right ring finger. It is located on the l key.\nㄇ is typed with the left pinky finger. It is located on the a key.\nㄤ is typed with the right pinky finger. It is located on the ; key."
threeD = "ㄕ is typed with the left pointer finger. It is located on the g key.\nㄘ is typed with the right pointer finger. It is located on the h key."
fourD = "Review the ㄑ(f), ㄨ(j), ㄎ(d), ㄜ(k), ㄋ(s), ㄠ(l), ㄇ(a), ㄤ(;), ㄕ(g), ㄘ(h) keys."
fiveD = "ㄔ is typed with the left pointer finger. It is located on the t key.\nㄎ is typed with the right pointer finger. It is located on the y key.\nㄐ is typed with the left pointer finger. It is located on the r key.\nㄧ is typed with the right pointer finger. It is located on the u key."
sixD = "ㄍ is typed with the left middle finger. It is located on the e key.\nㄛ is typed with the right middle finger. It is located on the i key.\nㄊ is typed with the left ring finger. It is located on the w key.\nㄟ is typed with the right ring finger. It is located on the o key."
sevenD = "ㄆ is typed with the left pinky finger. It is located on the q key.\nㄣ is typed with the right pinky finger. It is located on the p key."
eightD = "Review the ㄔ(t), ㄗ(y), ㄐ(r), ㄧ(u), ㄍ(e), ㄛ(i), ㄊ(w), ㄟ(o), ㄆ(q), ㄣ(p) keys."
nineD = "ㄖ is typed with the left pointer finger. It is located on the b key.\nㄙ is typed with the right pointer finger. It is located on the n key.\nㄒ is typed with the left pointer finger. It is located on the v key.\nㄩ is typed with the right pointer finger. It is located on the m key."
tenD = "ㄏ is typed with the left middle finger. It is located on the c key.\nㄝ is typed with the right middle finger. It is located on the , key.\nㄌ is typed with the left ring finger. It is located on the x key.\nㄡ is typed with the right ring finger. It is located on the . key."
elevenD = "ㄈ is typed with the left pinky finger. It is located on the z key.\nㄥ is typed with the right pinky finger. It is located on the / key."
twelveD = "Review the ㄖ(b), ㄙ(n), ㄒ(v), ㄩ(m), ㄏ(c), ㄝ(,), ㄌ(x), ㄡ(.), ㄈ(z), ㄥ(/) keys."
thirteenD = "ㄅ is typed with the left pinky finger. It is located on the 1 key.\nㄉ is typed with the left ring finger. It is located on the 2 key.\nㄓ is typed with the left pointer finger. It is located on the 5 key."
fourteenD = "ㄚ is typed with the right middle finger. It is located on the 8 key.\nㄞ is typed with the right ring finger. It is located on the 9 key.\nㄢ is typed with the right pinky finger. It is located on the 0 key.\nㄦ is typed with the right pinky finger. It is located on the - key."
fifteenD = "ˇ is typed with the left middle finger. It is located on the 3 key.\nˋ is typed with the left pointer finger. It is located on the 4 key.\nˊ is typed with the right pointer finger. It is located on the 6 key.\n˙ is typed with the right pointer finger. It is located on the 7 key."
sixteenD = "Review the ㄅ(1), ㄉ(2), ㄓ(5), ㄚ(8), ㄞ(9), ㄢ(0), ㄦ(-), ˇ(3), ˋ(4), ˊ(6), ˙(7) keys."

#put instructions into list
descList = [oneD, twoD, threeD, fourD, fiveD, sixD, sevenD, eightD, nineD, tenD, elevenD, twelveD, thirteenD, fourteenD, fifteenD, sixteenD]




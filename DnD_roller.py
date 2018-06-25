import sys
import random
from tkinter import *
import pkg_resources   # this is included for other types of exe compiles

#### global variables
testRolls = []
myCharacter = []
statRoll = []

#### Dice roll functions for buttons later
def roll_a_character():
    a = 0
    rolls.delete(1.0, (18.0 * 4) + 1.0)
    result.set("")
    for stat in range(6):
        for dice in range(4):
            statRoll.append(random.randint(1, 6) )
        temp = []
        temp = sorted(statRoll, key= int, reverse= True)
        rolls.insert(INSERT, str(temp) )
        statRoll.remove(min(statRoll))
        for i in statRoll:
            a = a + i
        myCharacter.append(a)
        txtDisplay.insert(INSERT, str(a) )
        if stat < 5:
            txtDisplay.insert(INSERT, ", ")
        a = 0
        del statRoll[:]

def cleanUp():
    rolls.delete(1.0, 23.0)
    rolls.insert(1.0, str(sorted(testRolls, key= int, reverse = True)) )
    del testRolls[:]
    
def chr():
    roll_a_character()
    return(myCharacter)
    del myCharacter[:]

def dice(i, sided):
    total = 0
    die = i.get()
    for x in range(die):
        roll = random.randint(1, sided)
        total = total + roll
        testRolls.append(roll)
    result.set(total)    
    cleanUp()

def increment(event):
    if diceNumber.get() < 100:
        diceNumber.set( diceNumber.get() + 1 )

def decrement(event):
    if diceNumber.get() > 1:
        diceNumber.set( diceNumber.get() - 1 )
    
#### main window function
window = Tk()
frame = Frame(window)
frame.pack()
window.title("D&D Roller")
window.bind('<Up>', increment)
window.bind('<Down>', decrement)

# Number of dice to be rolled (used later)
diceNumber = IntVar()
diceNumber.set(1)

#### main output window
result = IntVar()
outputFrame = Frame(window)
outputFrame.pack(side = TOP)

txtDisplay = Entry(outputFrame, textvariable = result,
                   bd= 20, insertwidth= 1,
                   font= 30)
txtDisplay.pack( side = TOP )

#### All rolls display
allTheRolls = Frame(window)
allTheRolls.pack(side = TOP)
rolls = Text(allTheRolls, height = 1, width = 23)
rolls.tag_add("diceRollz", "1.0", "23.0")
rolls.insert(INSERT, str(testRolls))
rolls.pack(side = TOP)

#### All of the dice buttons1
#####################################
buttonRow1 = Frame(window)
buttonRow1.pack(side = TOP)

buttonD2 = Button(buttonRow1, padx= 16, pady= 16, bd= 8, text="d2",
                  fg="black", command= lambda:dice(diceNumber, 2) )
buttonD2.pack(side = LEFT)
buttonD4 = Button(buttonRow1, padx= 16, pady= 16, bd= 8, text="d4",
                  fg="black", command= lambda:dice(diceNumber, 4) )
buttonD4.pack(side = LEFT)
buttonD6 = Button(buttonRow1, padx= 16, pady= 16, bd= 8, text="d6",
                  fg="black", command= lambda:dice(diceNumber, 6) )
buttonD6.pack(side = LEFT)

#####################################
buttonRow2 = Frame(window)
buttonRow2.pack(side = TOP)

buttonD8 = Button(buttonRow2, padx= 16, pady= 16, bd= 8, text="d8",
                  fg="black", command= lambda:dice(diceNumber, 8) )
buttonD8.pack(side = LEFT)
buttonD12 = Button(buttonRow2, padx= 13, pady= 16, bd= 8, text="d10",
                   fg="black", command= lambda:dice(diceNumber, 10) )
buttonD12.pack(side = LEFT)
buttonD20 = Button(buttonRow2, padx= 13, pady= 16, bd= 8, text="d12",
                   fg="black", command= lambda:dice(diceNumber, 12) )
buttonD20.pack(side = LEFT)

#####################################
buttonRow3 = Frame(window)
buttonRow3.pack(side = TOP)

buttonD50 = Button(buttonRow3, padx= 13, pady= 16, bd= 8, text="d20",
                   fg="black", command= lambda:dice(diceNumber, 20) )
buttonD50.pack(side = LEFT)
buttonD100 = Button(buttonRow3, padx= 10, pady= 16, bd= 8, text="d100",
                    fg="black", command= lambda:dice(diceNumber, 100) )
buttonD100.pack(side = LEFT)
buttonCHR = Button(buttonRow3, padx= 11, pady= 16, bd= 8, text="CHR",
                   fg="black", command= lambda:roll_a_character() )
buttonCHR.pack(side = LEFT)

#### number of dice to roll selection
numberOfDiceSelection = Frame(window)
numberOfDiceSelection.pack(side = TOP)

instructionLabel = Label(numberOfDiceSelection,
                         text = "Number of dice to roll: ")
instructionLabel.pack(side = LEFT)
numberOfDice = Entry(numberOfDiceSelection, justify = CENTER, exportselection = 0,
                     bd = 5, width = 10, textvariable = diceNumber)
numberOfDice.pack(side = RIGHT)

##### run the main loop
window.mainloop()

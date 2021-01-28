########################################################
# Author: Robert Ball - Coding, App and Game Design Instructor
# Program Name = 'Dev1-0030 Dictionary Practice';
# Date = '01/25/21';
# Program Name = '';
# Description = 'More practice with Dictionaries - Dice Roll Game';
# Assignment Number = 'Dev1-0030';
#############################################################
import random as rd 

def printResults(DiceTracker,WinLoseCount):
    print('==============================================')
    print(f"Your Record is {WinLoseCount['Win']} wins and {WinLoseCount['Lose']} loses!")
    print(f"ones: {DiceTracker[1]} | Twos: {DiceTracker[2]} | Threes: {DiceTracker[3]} | Fours: {DiceTracker[4]} | Fives: {DiceTracker[5]} | Sixes: {DiceTracker[6]}")
    print('=====')

DiceTracker = {1:0,2:0,3:0,4:0,5:0,6:0}
Dice = [1,2,3,4,5,6]
WinLoseCount = {'Win':0,'Lose':0}

print("Welcome to the Dice Game.  You roll then the computer will roll, Highest Die wins, Ties are ingored")
response = input("Would you like to play? (Y or N) ")
if response.upper() == 'Y':
    KeepPlaying = True
    while KeepPlaying:
        PlayerRoll = rd.randint(1,6)
        print(f"Player rolls a {PlayerRoll}")
        ComputerRoll = rd.randint(1,6)
        print(f"Computer rolls a {ComputerRoll}")
        if PlayerRoll == ComputerRoll:
            print("It is a tie - There is no win or lose")
            CurrentRollCount = DiceTracker[PlayerRoll]
            CurrentRollCount += 1
            DiceTracker[PlayerRoll] = CurrentRollCount
        elif PlayerRoll > ComputerRoll:
            print("You won!!! Stats are updated")
            CurrentRollCount = DiceTracker[PlayerRoll]
            CurrentRollCount += 1
            DiceTracker[PlayerRoll] = CurrentRollCount
            WinCount = WinLoseCount['Win']
            WinCount += 1
            WinLoseCount['Win'] = WinCount
        else:
            print("Sorry you Lose!!!")
            CurrentRollCount = DiceTracker[PlayerRoll]
            CurrentRollCount += 1
            DiceTracker[PlayerRoll] = CurrentRollCount
            LoseCount = WinLoseCount['Lose']
            LoseCount += 1
            WinLoseCount['Lose'] = LoseCount
        printResults(DiceTracker,WinLoseCount)
        response = input("Would you like to play again? (Y or N) ")
        if response.upper() == 'Y':
            pass
        else:
            KeepPlaying = False
            print("Thanks for Playing!!")       
else: 
    print("Thanks for Playing")

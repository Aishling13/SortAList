import random

#Generate 5 random numbers between 10 and 30
NumberList = random.sample(range(-10, 1000), 30)

while True:
    FirstNumber = NumberList[0]
    
    SwapCounter = 0

    for PositionInList in range(len(NumberList)-1):
        CurrentNumber = NumberList[PositionInList]
        NextNumber = NumberList[PositionInList + 1]

        if CurrentNumber > NextNumber:
            NumberList[PositionInList] = NextNumber
            NumberList[PositionInList + 1] = CurrentNumber
            SwapCounter = SwapCounter + 1
    print(NumberList)
    if SwapCounter == 0:
        break

 


        
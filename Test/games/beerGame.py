#Beer Game

beerNum = 99

while beerNum > 0:
    print(beerNum, "bottles of beer on the wall")
    print(beerNum, "bottles of beer")
    print("take one down, pass it around")
    print(beerNum, "bottles of beer on the wall")
    beerNum = beerNum - 1
    input("Press Enter to do it again!")
if beerNum == 0:
    print('No more bottles of beer')
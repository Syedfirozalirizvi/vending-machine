import random
import os
import time




player = 0
dealer = 0


for i in range(0,3):


    player_points = random.randint(2,11)   
    dealer_points = random.randint(2,11)
    time.sleep(2)

    print('Player Card Is :',player_points)
    print('Dealer Card Is :',dealer_points)


    player = player + player_points
    dealer = dealer + dealer_points

    print('Player Points:',player)
    print('Dealer Points :',dealer)


    input('press enter to continue')


    if player > 21:
        print('PLayer Is LOSE')
        break

    if dealer > 21:
        print('Dealer Is LOSE')
        break



    if player == 21:
        print('Player is WIN')
        break

    if dealer == 21:
        print('Dealer is WIN')
        break    


print('#####game over######')
print('Player Points Is : ',player)
print('Dealer Points Is : ',dealer)


if player == dealer:
        print('A Tie Game')


if player > dealer:
        print('*********player is winer*********')
else:
        print('*********dealer is winer*********')





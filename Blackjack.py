
import random
import os
import time


class blackjack:
    def fun(self):

        rows = 15
        cols = 20
        

        player = 0
        dealer = 0

        for i in range(1,4):
            time.sleep(2)
            for k in range(rows):
                print('|' +('-' if k in (0,rows-1) else ' ') * (cols-2) + '|')
                
            for l in range(rows):
                print('|' +('-' if l in (0,rows-1) else ' ') * (cols-2) + '|')
            
                                
            if i == 1:

                for j in range(i):
                    
                    player_points = random.randint(2,11)   
                    dealer_points = random.randint(2,11)
                    

                    print('Player Card :',player_points)
                    print('Dealer Card :',dealer_points)
                    print()


                    player = player + player_points
                    dealer = dealer + dealer_points

                    print('Player Points:',player)
                    print('Dealer Points :',dealer)


                    input('press enter to continue')


                    
            if i == 2:

                    player_points = random.randint(2,11)   
                    dealer_points = random.randint(2,11)
                    

                    print('Player Card :', player_points)
                    print('Dealer Card : Hidden')
                    print()
                

                    player = player + player_points
                    dealer = dealer + dealer_points

                    print('Player Points:',player)
                    #print('Dealer Points :',dealer)


                    input('press enter to continue')


                    
            if i == 3:

                    player_points = random.randint(2,11)   
                    dealer_points = random.randint(2,11)
                    

                    print('Player Card :',player_points)
                    print('Dealer Card :',dealer_points)
                    print()


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




obj = blackjack()
obj.fun()




game_runnung = True
while game_runnung == True:
    new_round = True
    player = {'name': 'Sam', 'attack': 12, 'heal': 15, 'health': 100}
    monster = {'name': 'Dragon', 'attack': 15, 'health': 100}

    print('Enter player name: ')
    print('---' * 7)
    player['name'] = input()
    
    
    while new_round == True:
        import random

        player_won = False
        monster_won = False
        
        print('')
        print('***' * 7)
        print(player['name'] + ' has ' + str(player['health']) + ' health!')
        print(monster['name'] + ' has ' + str(monster['health']) + ' health!')
        print('***' * 7)
        print('')
        print('Hello, ' + player['name'] + '!' + ' Please select an action: ')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        choice = input()

        if choice == '1':
            first = random.randint(0,9) 
            second = random.randint(0,9) 
            result = first + second
            answer = input(str(first) + ' + ' + str(second) + ': ')
            if result == int(answer):
                monster['health'] = monster['health'] - player['attack']
                print('You are correct!')
                
            else:
                player['health'] = player['health'] - monster['attack']
                print('Sorry you are wrong!')
                
            if monster['health'] <= 0:
                player_won = True
            else:
                
                if player['health'] <= 0:
                    monster_won = True
            
            
        
        elif choice == '2' and player['health'] != 100:
            first = random.randint(100,999) 
            second = random.randint(100,999) 
            result = first + second
            answer = input(str(first) + ' + ' + str(second) + ': ')
            if result == int(answer):
                player['health'] = player['health'] + player['heal']
                print('You are correct!')
            else:
                player['health'] = player['health'] - monster['attack']
                print('Sorry you are wrong!')
            

        elif choice == '3':
            new_round = False
            game_runnung = False
            print('Thanks for playing!')
        else:
            print('Invalid Input!')

        if player_won == False and monster_won == False:
            pass

        elif player_won:
            print('')
            print('$$$' + player['name'] + ' WON!' + '$$$')
            print('')
            new_round = False
        
        elif monster_won:
            print('')
            print('$$$' + monster['name'] + ' WON!' + '$$$')
            print('')
            new_round = False

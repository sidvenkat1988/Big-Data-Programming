class Card:
    num_of_cards = 0
    def __init__(self, speed, name):
        self.speed = speed
        
        self.name = name
        Card.num_of_cards += 1
        
        
print(Card.num_of_cards)
#Creating cards
c1 = Card(20, "a")
c2 = Card(40, "b")
c3 = Card(36, "c")
c4 = Card(19, "d")
c5 = Card(21, "e")
c6 = Card(39, "f")
c7 = Card(38, "g")
c8 = Card(34, "h")
c9 = Card(24.8, "i")
c10 = Card(21.5, "j")
print(Card.num_of_cards)

player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
player1GodSpell = 0
player1ResurrectSpell = 0
player2GodSpell = 0
player2ResurrectSpell = 0
player1Points = 0
player2Points = 0
round = 0


import random
from random import randint
from time import sleep

Cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
Cards = set(Cards)
sample1 = random.sample(Cards, 5)
sample2 = [x for x in Cards if x not in sample1]
outdated = []

while len(outdated) == 0:
    
    print("Dear " + player1 + ", type 'roll' to roll the dice")
    player1Input = input(">>>")
    if player1Input == "roll":
            value1 = randint(1,6)
            print(player1 + " rolled", value1)
            print(player2 + ", now it's your turn, enter 'roll' to roll the dice")
            player2Input = input(">>>")
            if player2Input == "roll":
                value2 = randint(1,6)
                print(player2 + " rolled", value2)
                if value1 > value2:
                    print(player1 + " rolled a higher value")
                    print("Hey " + player1 + ", press '1' for 'Regular Spell' and '2' for 'God Spell'")
                    player1SpellInput = input(">>>")
                    if player1SpellInput == "1":
                        print("Hey " + player1 + ", you've opted for 'Regular Spell'.")
                        
                        print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                        print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                        if sample1[0].speed > sample2[0].speed:
                            print(player1 + " won this round")
                            
                            player1Points += 1
                            #print(sample1[0].name)
                            outdated.append(sample1[0])
                            #print(outdated[0].name)
                            sample1.remove(sample1[0])
                            #print(sample1[0].name)
                            #print(sample2[0].name)
                            outdated.append(sample2[0])
                            #print(outdated[1].name)
                            sample2.remove(sample2[0])
                            #print(sample2[0].name)
                            
       
                            
                        else:
                            print(player2 + " won this round")
                            
                            player2Points += 1
                            #print(sample1[0].name)
                            outdated.append(sample1[0])
                            #print(outdated[0].name)
                            sample1.remove(sample1[0])
                            #print(sample1[0].name)
                            #print(sample2[0].name)
                            outdated.append(sample2[0])
                            #print(outdated[1].name)
                            sample2.remove(sample2[0])
                            #print(sample2[0].name)
                        
        
                        
        
                    else:
                        print("Hey " + player1 + ", you've opted for 'God Spell'.")
                        player1GodSpell += 1
                        print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                        player1GodSpellInput = input(">>>")
                        if player1GodSpellInput == "1":
                            print("You've chosen 1")
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            
                        
                        elif player1GodSpellInput == "2":
                            print("You've chosen 2")
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[1].speed)
                            if sample1[0].speed > sample2[1].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[1])
                                sample2.remove(sample2[1])
                                
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[1])
                                sample2.remove(sample2[1])
                        
                        
                        elif player1GodSpellInput == "3":
                            print("You've chosen 3")
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[2].speed)
                            if sample1[0].speed > sample2[2].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[2])
                                sample2.remove(sample2[2])
                                
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[2])
                                sample2.remove(sample2[2])
                                
                            
                        
                        
                        elif player1GodSpellInput == "4":
                            print("You've chosen 4")
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[3].speed)
                            if sample1[0].speed > sample2[3].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[3])
                                sample2.remove(sample2[3])
                            
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[3])
                                sample2.remove(sample2[3])
                        
                        
                        else:
                            print("You've chosen 5")
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[4].speed)
                            if sample1[0].speed > sample2[4].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[4])
                                sample2.remove(sample2[4])
                            
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[4])
                                sample2.remove(sample2[4])
                    
                        
                elif value1 == value2:
                    print("It's a draw")
                    
                else:
                    print(player2 + " rolled a higher value")
                    print("Hey " + player2 + ", press '1' for 'Regular Spell' and '2' for 'God Spell'")
                    player2SpellInput = input(">>>")
                    if player2SpellInput == "1":
                        print("Hey " + player2 + ", you've opted for 'Regular Spell'.")
                        
                        print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                        print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                        if sample2[0].speed > sample1[0].speed:
                            print(player2 + " won this round")
                            player2Points += 1
                            #print(sample1[0].name)
                            outdated.append(sample1[0])
                            #print(outdated[0].name)
                            sample1.remove(sample1[0])
                            #print(sample1[0].name)
                            #print(sample2[0].name)
                            outdated.append(sample2[0])
                            #print(outdated[1].name)
                            sample2.remove(sample2[0])
                            #print(sample2[0].name)
                            
       
                            
                        else:
                            print(player1 + " won this round")
                            player1Points += 1
                            #print(sample1[0].name)
                            outdated.append(sample1[0])
                            #print(outdated[0].name)
                            sample1.remove(sample1[0])
                            #print(sample1[0].name)
                            #print(sample2[0].name)
                            outdated.append(sample2[0])
                            #print(outdated[1].name)
                            sample2.remove(sample2[0])
                            #print(sample2[0].name)
                            
       
        
                        
                        
                    else:
                        print("Hey " + player2 + ", you've opted for 'God Spell'.")
                        player2GodSpell += 1
                        print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                        player2GodSpellInput = input(">>>")
                        if player2GodSpellInput == "1":
                            print("You've chosen 1")
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            if sample2[0].speed > sample1[0].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                            
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                
                            
                                
                                
                        elif player2GodSpellInput == "2":
                            print("You've chosen 2")
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[1].speed)
                            if sample2[0].speed > sample1[1].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[1])
                                sample1.remove(sample1[1])
                            
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[1])
                                sample1.remove(sample1[1])
                                
                            
                                
                                
                        elif player2GodSpellInput == "3":
                            print("You've chosen 3")
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[2].speed)
                            if sample2[0].speed > sample1[2].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[2])
                                sample1.remove(sample1[2])
                            
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[2])
                                sample1.remove(sample1[2])
                                
                            
                                
                                
                        elif player2GodSpellInput == "4":
                            print("You've chosen 4")
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[3].speed)
                            if sample2[0].speed > sample1[3].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[3])
                                sample1.remove(sample1[3])
                            
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[3])
                                sample1.remove(sample1[3])
                            
                                
                                
                        else:
                            print("You've chosen 5")
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[4].speed)
                            if sample2[0].speed > sample1[4].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[4])
                                sample1.remove(sample1[4])
                            
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                outdated.append(sample1[4])
                                sample1.remove(sample1[4])
                            
                                
            
            elif player2Input == "quit":
                print(player1 + " is the default winner")
                
            else:
                print("Wrong value entered")
        
    elif player1Input == "quit":
        print(player2 + " is the default winner")
        
        
                
    else:
        print("Wrong value entered")
        
    if len(outdated) > 0:
        break
    

print(player1 + " has scored " + str(player1Points))
print(player2 + " has scored " + str(player2Points))

while (len(sample1) > 0) or (len(sample2) > 0):
    if player1Points > player2Points:
        print("Dear " + player1 + ", type 'roll' to roll the dice")
        player1Input = input(">>>")
        if player1Input == "roll":
                value1 = randint(1,6)
                print(player1 + " rolled", value1)
                print(player2 + ", now it's your turn, enter 'roll' to roll the dice")
                player2Input = input(">>>")
                if player2Input == "roll":
                    value2 = randint(1,6)
                    print(player2 + " rolled", value2)
                    if value1 > value2:
                        print(player1 + " rolled a higher value")
                        print("Hey " + player1 + ", press '1' for 'Regular Spell', '2' for 'God Spell' and '3' for 'Resurrect Spell'")
                        player1SpellInput = input(">>>")
                        if player1SpellInput == "1":
                            print("Hey " + player1 + ", you've opted for 'Regular Spell'.")
                            
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                
                                player1Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
                                
                            else:
                                print(player2 + " won this round")
                                
                                player2Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                            
            
                            
            
                        elif player1SpellInput == "2":
                            
                        
                                
                            
                            
                            
                            print("Hey " + player1 + ", you've opted for 'God Spell'.")
                            
                            
                            player1GodSpell += 1
                            print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                            player1GodSpellInput = input(">>>")
                            if player1GodSpellInput == "1":
                                print("You've chosen 1")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                if sample1[0].speed > sample2[0].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                
                            
                            elif player1GodSpellInput == "2":
                                print("You've chosen 2")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[1].speed)
                                if sample1[0].speed > sample2[1].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[1])
                                    sample2.remove(sample2[1])
                                    
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[1])
                                    sample2.remove(sample2[1])
                            
                            
                            elif player1GodSpellInput == "3":
                                print("You've chosen 3")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[2].speed)
                                if sample1[0].speed > sample2[2].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[2])
                                    sample2.remove(sample2[2])
                                    
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[2])
                                    sample2.remove(sample2[2])
                                    
                                
                            
                            
                            elif player1GodSpellInput == "4":
                                print("You've chosen 4")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[3].speed)
                                if sample1[0].speed > sample2[3].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[3])
                                    sample2.remove(sample2[3])
                                
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[3])
                                    sample2.remove(sample2[3])
                            
                            
                            else:
                                print("You've chosen 5")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[4].speed)
                                if sample1[0].speed > sample2[4].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[4])
                                    sample2.remove(sample2[4])
                                
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[4])
                                    sample2.remove(sample2[4])
                        
                        else:
                            print("Hey " + player1 + ", you've opted for 'Resurrect Spell'.")
                            sample1.append(outdated[0])
                            outdated.remove(outdated[0])
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                        
                        
                            
                    elif value1 == value2:
                        print("It's a draw")
                        
                    else:
                        print(player2 + " rolled a higher value")
                        print("Hey " + player2 + ", press '1' for 'Regular Spell', '2' for 'God Spell' and '3' for 'Resurrect Spell'")
                        player2SpellInput = input(">>>")
                        if player2SpellInput == "1":
                            print("Hey " + player2 + ", you've opted for 'Regular Spell'.")
                            
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            if sample2[0].speed > sample1[0].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
                                
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
            
                            
                            
                        elif player2SpellInput == "2":
                            
                            
                            
                            print("Hey " + player2 + ", you've opted for 'God Spell'.")
                            player2GodSpell += 1
                            print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                            player2GodSpellInput = input(">>>")
                            if player2GodSpellInput == "1":
                                print("You've chosen 1")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                if sample2[0].speed > sample1[0].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "2":
                                print("You've chosen 2")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[1].speed)
                                if sample2[0].speed > sample1[1].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[1])
                                    sample1.remove(sample1[1])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[1])
                                    sample1.remove(sample1[1])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "3":
                                print("You've chosen 3")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[2].speed)
                                if sample2[0].speed > sample1[2].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[2])
                                    sample1.remove(sample1[2])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[2])
                                    sample1.remove(sample1[2])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "4":
                                print("You've chosen 4")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[3].speed)
                                if sample2[0].speed > sample1[3].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[3])
                                    sample1.remove(sample1[3])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[3])
                                    sample1.remove(sample1[3])
                                
                                    
                                    
                            else:
                                print("You've chosen 5")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[4].speed)
                                if sample2[0].speed > sample1[4].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[4])
                                    sample1.remove(sample1[4])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[4])
                                    sample1.remove(sample1[4])
                                    
                        else:
                            print("Hey " + player2 + ", you've opted for 'Resurrect Spell'.")
                            sample2.append(outdated[0])
                            outdated.remove(outdated[0])
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                
                                    
                
                elif player2Input == "quit":
                    print(player1 + " is the default winner")
                    
                else:
                    print("Wrong value entered")
            
        elif player1Input == "quit":
            print(player2 + " is the default winner")
            
            
                    
        else:
            print("Wrong value entered")

    else:
        print("Dear " + player2 + ", type 'roll' to roll the dice")
        player2Input = input(">>>")
        if player2Input == "roll":
                value2 = randint(1,6)
                print(player2 + " rolled", value2)
                print(player1 + ", now it's your turn, enter 'roll' to roll the dice")
                player1Input = input(">>>")
                if player1Input == "roll":
                    value1 = randint(1,6)
                    print(player1 + " rolled", value1)
                    if value1 > value2:
                        print(player1 + " rolled a higher value")
                        print("Hey " + player1 + ", press '1' for 'Regular Spell', '2' for 'God Spell' and '3' for 'Resurrect Spell'")
                        player1SpellInput = input(">>>")
                        if player1SpellInput == "1":
                            print("Hey " + player1 + ", you've opted for 'Regular Spell'.")
                            
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                
                                player1Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
                                
                            else:
                                print(player2 + " won this round")
                                
                                player2Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                            
            
                            
            
                        elif player1SpellInput == "2":
                            
                            
                            print("Hey " + player1 + ", you've opted for 'God Spell'.")
                            player1GodSpell += 1
                            print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                            player1GodSpellInput = input(">>>")
                            if player1GodSpellInput == "1":
                                print("You've chosen 1")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                if sample1[0].speed > sample2[0].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                
                            
                            elif player1GodSpellInput == "2":
                                print("You've chosen 2")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[1].speed)
                                if sample1[0].speed > sample2[1].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[1])
                                    sample2.remove(sample2[1])
                                    
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[1])
                                    sample2.remove(sample2[1])
                            
                            
                            elif player1GodSpellInput == "3":
                                print("You've chosen 3")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[2].speed)
                                if sample1[0].speed > sample2[2].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[2])
                                    sample2.remove(sample2[2])
                                    
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[2])
                                    sample2.remove(sample2[2])
                                    
                                
                            
                            
                            elif player1GodSpellInput == "4":
                                print("You've chosen 4")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[3].speed)
                                if sample1[0].speed > sample2[3].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[3])
                                    sample2.remove(sample2[3])
                                
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[3])
                                    sample2.remove(sample2[3])
                            
                            
                            else:
                                print("You've chosen 5")
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                print("Speed of " + player2 + "'s card = ", sample2[4].speed)
                                if sample1[0].speed > sample2[4].speed:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[4])
                                    sample2.remove(sample2[4])
                                
                                else:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    outdated.append(sample2[4])
                                    sample2.remove(sample2[4])
                                    
                        else:
                            print("Hey " + player1 + ", you've opted for 'Resurrect Spell'.")
                            sample1.append(outdated[0])
                            outdated.remove(outdated[0])
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                        
                            
                    elif value1 == value2:
                        print("It's a draw")
                        
                    else:
                        print(player2 + " rolled a higher value")
                        print("Hey " + player2 + ", press '1' for 'Regular Spell', '2' for 'God Spell' and '3' for 'Resurrect Spell'")
                        player2SpellInput = input(">>>")
                        if player2SpellInput == "1":
                            print("Hey " + player2 + ", you've opted for 'Regular Spell'.")
                            
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            if sample2[0].speed > sample1[0].speed:
                                print(player2 + " won this round")
                                player2Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
                                
                            else:
                                print(player1 + " won this round")
                                player1Points += 1
                                #print(sample1[0].name)
                                outdated.append(sample1[0])
                                #print(outdated[0].name)
                                sample1.remove(sample1[0])
                                #print(sample1[0].name)
                                #print(sample2[0].name)
                                outdated.append(sample2[0])
                                #print(outdated[1].name)
                                sample2.remove(sample2[0])
                                #print(sample2[0].name)
                                
           
            
                            
                            
                        elif player2SpellInput == "2":
                            
                            
                            print("Hey " + player2 + ", you've opted for 'God Spell'.")
                            player2GodSpell += 1
                            print("Now select a number between 1 and 5 to choose the card position of your opponent with which your first card will be compared.")
                            player2GodSpellInput = input(">>>")
                            if player2GodSpellInput == "1":
                                print("You've chosen 1")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                                if sample2[0].speed > sample1[0].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[0])
                                    sample1.remove(sample1[0])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "2":
                                print("You've chosen 2")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[1].speed)
                                if sample2[0].speed > sample1[1].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[1])
                                    sample1.remove(sample1[1])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[1])
                                    sample1.remove(sample1[1])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "3":
                                print("You've chosen 3")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[2].speed)
                                if sample2[0].speed > sample1[2].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[2])
                                    sample1.remove(sample1[2])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[2])
                                    sample1.remove(sample1[2])
                                    
                                
                                    
                                    
                            elif player2GodSpellInput == "4":
                                print("You've chosen 4")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[3].speed)
                                if sample2[0].speed > sample1[3].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[3])
                                    sample1.remove(sample1[3])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[3])
                                    sample1.remove(sample1[3])
                                
                                    
                                    
                            else:
                                print("You've chosen 5")
                                print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                                print("Speed of " + player1 + "'s card = ", sample1[4].speed)
                                if sample2[0].speed > sample1[4].speed:
                                    print(player2 + " won this round")
                                    player2Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[4])
                                    sample1.remove(sample1[4])
                                
                                else:
                                    print(player1 + " won this round")
                                    player1Points += 1
                                    outdated.append(sample2[0])
                                    sample2.remove(sample2[0])
                                    outdated.append(sample1[4])
                                    sample1.remove(sample1[4])
                                    
                        else:
                            print("Hey " + player2 + ", you've opted for 'Resurrect Spell'.")
                            sample2.append(outdated[0])
                            outdated.remove(outdated[0])
                            print("Speed of " + player1 + "'s card = ", sample1[0].speed)
                            print("Speed of " + player2 + "'s card = ", sample2[0].speed)
                            if sample1[0].speed > sample2[0].speed:
                                print(player1 + " won this round")
                                player1Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                            else:
                                print(player2 + " won this round")
                                player2Points += 1
                                outdated.append(sample1[0])
                                sample1.remove(sample1[0])
                                outdated.append(sample2[0])
                                sample2.remove(sample2[0])
                                
                                    
                
                elif player2Input == "quit":
                    print(player1 + " is the default winner")
                    
                else:
                    print("Wrong value entered")
            
        elif player1Input == "quit":
            print(player2 + " is the default winner")
            
            
                    
        else:
            print("Wrong value entered")

    if (len(sample1) == 0) or (len(sample2) == 0):
        break

print(player1 + "'s final score is " + str(player1Points))
print(player2 + "'s final score is " + str(player2Points)) 

if player1Points > player2Points:
    print(player1 + " is the winner!")
else:
    print(player2 + " is the winner!")
     
                
                    



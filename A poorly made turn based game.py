#Pruben
#03/17/2020
#To see if I can write a turn based game with at least three fights
import random
import os
import math



class_choice = 1
boss_choice = 1



#Main menu
while True:
    print("Main Menu:")
    print("1 - Begin!")
    print("2 - Options")
    print("9 - Exit")
    main_menu_choice = input(": ")
    
    if main_menu_choice == "9":
        break
    elif main_menu_choice == "2":
        while True:
            print("1 - Player Options")
            print("2 - Enemy Options")
            print("9 - Back")
            men_op = input(": ")
            #Player Options
            if men_op == "1":
                while True:
                    print("Please choose Player class:")
                    print("1 - Stronk")
                    print("2 - Spell boy")
                    print("3 - Speedy boy")
                    print("9 - Back")
                    player_class_choice = input(": ")
                    if player_class_choice == "1":
                        class_choice = 1
                        print("Class choice: Stronk")
                        input()
                        
                        break
                    elif player_class_choice == "2":
                        class_choice = 2
                        print("Class choice: Spell Boy")
                        input()
                        
                        break
                    elif player_class_choice == "3":
                        class_choice = 3
                        print("Class choice: Speedy Boy")
                        input()
                        
                        break
                    elif player_class_choice == "9":
                        break
                    else:
                        print("Invalid input! Please try again.")
                        input()
            
            #Boss Options
            elif men_op == "2":
                while True:
                    print("Please choose which enemy you want to face")
                    print("1 - Big Bat")
                    print("2 - Weird Echidna")
                    print("3 - Pile of Mud")
                    print("9 - Back")
                    men_boss = input(": ")
                    if men_boss == "1":
                        boss_choice = 1
                        print("You'll be facing Big Bat")
                        input()
                        break
                    elif men_boss == "2":
                        boss_choice = 2
                        print("You'll be facing Weird Echidna")
                        input()
                        break
                    elif men_boss == "3":
                        boss_choice = 3
                        print("You'll be facing Pile of Mud")
                        input()
                    elif men_boss == "9":
                        break
                    else:
                        print("Invalid input! Please try again")
                        input()
                    
            #Back to main menu
            elif men_op == "9":
                break
            
        
            #False
            else:
                print("Invalid input! Please try again")
                input()
                
    
    
    
    
    
    
    
    #Game
    elif main_menu_choice == "1":
        #Initialize player
        if class_choice == 1:
            play_hp = 200
            play_mp = 80
            play_speed = 15
            play_def = 20
            play_off = 25
            play_mag = 15
        
        elif class_choice == 2:
            play_hp = 150
            play_mp = 150
            play_speed = 20
            play_def = 15
            play_off = 10
            play_mag = 35
        
        elif class_choice == 3:
            play_hp = 175
            play_mp = 100
            play_speed = 100
            play_def = 10
            play_off = 20
            play_mag = 20
        #Initialize boss    
        if boss_choice == 1:
            boss_hp = 1000
            boss_speed = 25
            boss_def = 15
            boss_off = 25
            boss_mag = 25
        
        elif boss_choice == 2:
            boss_hp = 1250
            boss_speed = 50
            boss_def = 20
            boss_off = 30
            boss_mag = 15
        
        elif boss_choice == 3:
            boss_hp = 1500
            boss_speed = 2
            boss_def = 30
            boss_off = 50
            boss_mag = 0
        
        
        #Starting off finally
        print("Enemy Approaches")
        while True:
            print("HP:",play_hp,"\tMP:",play_mp)
            print("Whatchu gon' do?")
            move = input("1 - Attack\t2 - Magic - ")
            if play_speed > boss_speed:
                if move == "1":
                    miss_chance = random.randint(0,10)
                    if miss_chance == 10:
                        print("You missed!")
                        input()
                    else:
                        raw_dam = random.randint(50,75)
                        play_dam = raw_dam + play_off
                        boss_hp = boss_hp - play_dam
                        print("You did",play_dam,"damage!")
                        input()
                if move == "2":
                    #Strong Boy
                    if class_choice == 1:
                        while True:
                            print("1 - Cure (10 MP)")
                            print("2 - Lightning (10 MP)")
                            print("3 - Big Boy Super Power Up (40 MP)")
                            print("9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Cure!")
                                    input()
                                    cur_raw = random.randint(40, 50)
                                    cure_hp = cur_raw + play_mag
                                    play_hp = play_hp + cure_hp
                                    if play_hp >= 200:
                                        print("Your health maxed out!")
                                        input()
                                        play_hp = 200
                                    else:
                                        print("You healed",cure_hp,"HP!")
                                        input()
                                    
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "2":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Lightning!")
                                    input()
                                    lig_raw = random.randint(30, 35)
                                    light = lig_raw + play_mag
                                    print("You did",light,"damage!")
                                    input()
                                    boss_hp = boss_hp - light
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "3":
                                if play_mp < 40:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Big Boy Super Power Up!")
                                    input()
                                    play_off = play_off + 25
                                    print("You're feeling totally pumped!!!")
                                    input()
                                    play_mp = play_mp - 40
                                    break
                            elif mag_choice == "9":
                                break
                            else:
                                print("Invalid input! Please try again.")
                                input()
                        if mag_choice == "9":
                            continue
                    
                    #Mage Boy
                    elif class_choice == 2:
                        while True:
                            print("1 - Cure (10 MP)\t2 - Lightning (10 MP)\t3 - Fire (10 MP)")
                            print("4 - Freeze (8 MP)\t5 - Beam (20 MP)\t6 - Defense Boost (15 MP)")
                            print("7 - Mind Read (5 MP)\t8 - Magic Boost (40 MP)\t9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Cure!")
                                    input()
                                    cur_raw = random.randint(40, 50)
                                    cure_hp = cur_raw + play_mag
                                    play_hp = play_hp + cure_hp
                                    if play_hp >= 150:
                                        print("You maxed out your health!")
                                        input()
                                        play_hp = 150
                                    else:
                                        
                                        print("You healed",cure_hp,"HP!")
                                        input()
                                    
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "2":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Lightning!")
                                    input()
                                    lig_raw = random.randint(30, 35)
                                    light = lig_raw + play_mag
                                    print("You did",light,"damage")
                                    input()
                                    boss_hp = boss_hp - light
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "3":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Fire!")
                                    input()
                                    fir_raw = random.randint(30, 40)
                                    fir_dam = fir_raw + play_mag
                                    if boss_choice == 2:
                                        fir_dam = fir_dam * 2
                                    print("You did",fir_dam,"damage!")
                                    input()
                                    boss_hp = boss_hp - fir_dam
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "4":
                                if play_mp < 8:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Freeze!")
                                    input()
                                    fre_raw = random.randint(25, 40)
                                    fre_dam = fre_raw + play_mag
                                    if boss_choice == 1:
                                        fre_dam = fre_dam * 2
                                    print("You did",fre_dam,"damage!")
                                    input()
                                    boss_hp = boss_hp - fre_dam
                                    play_mp = play_mp - 8
                                    break
                            elif mag_choice == "5":
                                if play_mp < 20:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Beam!")
                                    input()
                                    bem_raw = random.randint(40, 50)
                                    beam = bem_raw + play_mag
                                    print("You did",beam,"damage!")
                                    input()
                                    boss_hp = boss_hp - beam
                                    play_mp = play_mp - 20
                                    break
                            elif mag_choice == "6":
                                if play_mp < 15:
                                    print("Not enough MP!")
                                    input()
                                elif play_def > 20:
                                    print("Your defense is at its max!")
                                    input()
                                else:
                                    print("You casted Defense Boost!")
                                    input()
                                    boost = 10
                                    play_def = play_def + boost
                                    print("You defense was raised by 10")
                                    input()
                                    break
                            elif mag_choice == "7":
                                if play_mp < 5:
                                    input("Not enough MP!")
                                    print()
                                else:
                                    if boss_choice == 1:
                                        input("You read the Big Bat's mind")
                                        input("Big Bat hates the cold")
                                        input("Big Bat is very leftist")
                                        print("Big Bat has",boss_hp,"HP left!")
                                        input()
                                    elif boss_choice == 2:
                                        input("Weird Echidna is self conscience about his feet")
                                        input("Weird Echidna hates the heat!")
                                        print("Weird Echidna has",boss_hp,"HP left!")
                                        input()
                                    elif boss_choice == 3:
                                        print("It's a pile of mud. What do you want from me?")
                                        input()
                                    play_mp = play_mp - 5
                                    break
                            
                            elif mag_choice == "8":
                                if play_mp < 40:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Magic Boost!")
                                    input()
                                    mag_boo  = 25
                                    play_mag = play_mag + mag_boo
                                    play_mp = play_mp - 40
                                    break
                            elif mag_choice == "9":
                                break
                            else:
                                print("Invalid input! Please try again.")
                                input()
                        if mag_choice == "9":
                            continue
                    #Speedy Boy
                    if class_choice == 3:
                        while True:
                            print("1 - Cure (10 MP)\t2 - Freeze (8 MP)\t3 - Jabby Boi (30 MP)")
                            print("9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                if play_mp < 10:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Cure!")
                                    input()
                                    cur_raw = random.randint(40, 50)
                                    cure_hp = cur_raw + play_mag
                                    play_hp = play_hp + cure_hp
                                    if play_hp >= 175:
                                        print("You maxed out your HP!")
                                        input()
                                        play_hp = 175
                                    else:
                                        
                                        print("You healed",cure_hp,"HP!")
                                        input()
                                    
                                    play_mp = play_mp - 10
                                    break
                            elif mag_choice == "2":
                                if play_mp < 8:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    print("You casted Freeze!")
                                    input()
                                    bem_raw = random.randint(25, 40)
                                    beam = bem_raw + play_mag
                                    if boss_choice == 1:
                                        beam = beam * 2
                                    print("You did",beam,"damage!")
                                    input()
                                    boss_hp = boss_hp - beam
                                    play_mp = play_mp - 8
                                    break
                            elif mag_choice == "3":
                                if play_mp < 30:
                                    print("Not enough MP!")
                                    input()
                                else:
                                    input("You revved up your engines!")
                                    for i in range(0, 3):
                                        miss_chance = random.randint(0,10)
                                        if miss_chance == 10:
                                            print("You missed!")
                                            input()
                                        else:
                                            raw_dam = random.randint(50,75)
                                            play_dam = raw_dam + play_off
                                            boss_hp = boss_hp - play_dam
                                            print("You did",play_dam,"damage!", end = '') 
                                            input()
                                    play_mp = play_mp - 30
                                    break
                            elif mag_choice == "9":
                                break
                        
                            else:
                                print("Invlid input! Please try again")
                                input()
                        if mag_choice == "9":
                            continue
                                
                if boss_hp <= 0:
                    input("You Won! Holy shit!")
                    print()
                    break
                
                boss_move = random.randint(1,5)
                if boss_move == 1 or boss_move == 2:
                    if boss_choice == 1:
                        print("Big Bat charges!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                        
                    elif boss_choice == 2:
                        print("Weird Echidna kicks you!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam - play_def
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud flings mud at you!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    
                elif boss_move == 3 or boss_move ==4:
                    if boss_choice == 1:
                        print("Big Bat shot fire out of its mouth!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 2:
                        print("Weird Echidna shoots laser eyes at you! (Do echidnas have those?)")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud tries earthbending!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                elif boss_move == 5:
                    if boss_choice == 1:
                        print("Big Bat screeches at the top of its lungs")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 2:
                        print("Weird Echidna takes a BIG bite!!!")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud encases you!")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                
            elif boss_speed > play_speed:
                if move == "2":
                    if class_choice == 1:
                        
                        while True:
                            print("1 - Cure (10 MP)")
                            print("2 - Lightning (10 MP)")
                            print("3 - Big Boy Super Power Up (40 MP)")
                            print("9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                break
                            elif mag_choice == "2":
                                break
                            elif mag_choice == "3":
                                break
                            elif mag_choice == "9":
                                break
                            else:
                                print("Invalid input! Please try again.")
                                print()
                        if mag_choice == "9":
                            continue
                    elif class_choice == 2:
                        while True:
                            print("1 - Cure (10 MP)\t2 - Lightning (10 MP)\t3 - Fire (10 MP)")
                            print("4 - Freeze (8 MP)\t5 - Beam (20 MP)\t6 - Defense Boost (15 MP)")
                            print("7 - Mind Read (5 MP)\t8 - Magic Boost (40 MP)\t9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                break
                            elif mag_choice == "2":
                                break
                            elif mag_choice == "3":
                                break
                            elif mag_choice == "4":
                                break
                            elif mag_choice == "5":
                                break
                            elif mag_choice == "6":
                                break
                            elif mag_choice == "7":
                                break
                            elif mag_choice == "8":
                                break
                            elif mag_choice == "9":
                                break
                            else:
                                print("Invalid input! Please try again.")
                                print()
                        if mag_choice == "9":
                            continue
                    
                    elif class_choice == 3:
                        while True:
                            print("1 - Cure (10 MP)\t2 - Freeze (8 MP)\t3 - Jabby Boi (30 MP)")
                            print("9 - Back")
                            mag_choice = input(": ")
                            if mag_choice == "1":
                                break
                            elif mag_choice == "2":
                                break
                            elif mag_choice == "3":
                                break
                            elif mag_choice == "9":
                                break
                            else:
                                print("Invalid input! Please try again.")
                                print()
                        if mag_choice == "9":
                            continue
                        
                boss_move = random.randint(1,5)
                if boss_move == 1 or boss_move == 2:
                    if boss_choice == 1:
                        print("Big Bat charges!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                        
                    elif boss_choice == 2:
                        print("Weird Echidna kicks you!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud flings mud at you!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    
                elif boss_move == 3 or boss_move ==4:
                    if boss_choice == 1:
                        print("Big Bat shot fire out of its mouth!")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 2:
                        print("Weird Echidna shoots laser eyes at you! (Do echidnas have those?)")
                        input()
                        boss_raw = random.randint(15,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud tries earthbending!")
                        input()
                        boss_raw = random.randint(20,25)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                elif boss_move == 5:
                    if boss_choice == 1:
                        print("Big Bat screeches at the top of its lungs")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_mag - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 2:
                        print("Weird Echidna takes a BIG bite!!!")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                    elif boss_choice == 3:
                        print("Pile of Mud encases you!")
                        input()
                        boss_raw = random.randint(20,35)
                        boss_dam = boss_raw + boss_off - play_def
                        print("You took",boss_dam,"damage!")
                        input()
                        play_hp = play_hp - boss_dam
                        if play_hp <= 0:
                            input("You lost! Typical...")
                            input("Try again?")
                            print()
                            break
                
                if move == "1":
                    miss_chance = random.randint(0,10)
                    if miss_chance == 10:
                        input("You missed!")
                    else:
                        raw_dam = random.randint(50,75)
                        play_dam = raw_dam + play_off
                        boss_hp = boss_hp - play_dam
                        print("You did",play_dam,"damage!")
                        input()
                
                if move == "2":
                    if class_choice == 1:
                        if mag_choice == "1":
                            if play_mp < 10:
                                    input("Not enough MP!")
                                    print()
                            else:
                                print("You casted Cure!")
                                input()
                                cur_raw = random.randint(40, 50)
                                cure_hp = cur_raw + play_mag
                                play_hp = play_hp + cure_hp
                                if play_hp >= 200:
                                    print("You maxed out your HP!")
                                    input()
                                    play_hp = 200
                                else: 
                                    
                                    print("You healed",cure_hp,"HP!")
                                    input()
                                
                                play_mp = play_mp - 10
                                
                        elif mag_choice == "2":
                            
                            if play_mp < 10:
                                input("Not enough MP!")
                                print()
                            else:
                                print("You casted Lightning!")
                                input()
                                lig_raw = random.randint(30, 35)
                                light = lig_raw + play_mag
                                print("You did",light,"damage!")
                                input()
                                boss_hp = boss_hp - light
                                play_mp = play_mp - 10
                                
                        elif mag_choice == "3":
                            if play_mp < 40:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Big Boy Super Power Up!")
                                input()
                                play_off = play_off + 30
                                print("You're feeling totally pumped!!!")
                                input()
                                play_mp = play_mp - 40
                                
                        
                    elif class_choice == 2:
                        if mag_choice == "1":
                            if play_mp < 10:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Cure!")
                                input()
                                cur_raw = random.randint(40, 50)
                                cure_hp = cur_raw + play_mag
                                play_hp = play_hp + cure_hp
                                if play_hp >= 150:
                                    print("You maxed out your HP!")
                                    input()
                                    play_hp = 150
                                else:
                                    
                                    print("You healed",cure_hp,"HP!")
                                    input()
                               
                                play_mp = play_mp - 10
                                
                        elif mag_choice == "2":
                            if play_mp < 10:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Lightning!")
                                input()
                                lig_raw = random.randint(30, 35)
                                light = lig_raw + play_mag
                                print("You did",light,"damage")
                                input()
                                boss_hp = boss_hp - light
                                play_mp = play_mp - 10
                            
                        elif mag_choice == "3":
                            if play_mp < 10:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Fire!")
                                input()
                                fir_raw = random.randint(30, 40)
                                fir_dam = fir_raw + play_mag
                                if boss_choice == 2:
                                    fir_dam = fir_dam * 2
                                print("You did",fir_dam,"damage!")
                                input()
                                boss_hp = boss_hp - fir_dam
                                play_mp = play_mp - 10
                            
                        elif mag_choice == "4":
                            if play_mp < 8:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Freeze!")
                                input()
                                fre_raw = random.randint(25, 40)
                                fre_dam = fre_raw + play_mag
                                if boss_choice == 1:
                                    fre_dam = fre_dam * 2
                                print("You did",fre_dam,"damage!")
                                input()
                                boss_hp = boss_hp - fre_dam
                                play_mp = play_mp - 8
                            
                        elif mag_choice == "5":
                            if play_mp < 20:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Beam!")
                                input()
                                bem_raw = random.randint(40, 50)
                                beam = bem_raw + play_mag
                                print("You did",beam,"damage!")
                                input()
                                boss_hp = boss_hp - beam
                                play_mp = play_mp - 20
                            
                        elif mag_choice == "6":
                            if play_mp < 15:
                                print("Not enough MP!")
                                input()
                            elif play_def > 20:
                                print("Your defense is as high as we can get it!")
                                input()
                            else:
                                print("You casted Defense Boost!")
                                input()
                                boost = 10
                                play_def = play_def + boost
                                print("You defense was raised by 10")
                                input()
                                play_mp = play_mp - 15
                            
                        elif mag_choice == "7":
                            if play_mp < 5:
                                print("Not enough MP!")
                                input()
                            else:
                                if boss_choice == 1:
                                    input("You read the Big Bat's mind")
                                    input("Big Bat hates the cold")
                                    input("Big Bat is very leftist")
                                    print("Big Bat has",boss_hp,"HP left!")
                                    input()
                                elif boss_choice == 2:
                                    input("Weird Echidna is self conscience about his feet")
                                    input("Weird Echidna hates the heat!")
                                    print("Weird Echidna has",boss_hp,"HP left!")
                                    input()
                                elif boss_choice == 3:
                                    print("It's a pile of mud. What do you want from me?")
                                    input()
                                play_mp = play_mp - 5
                            
                            
                        elif mag_choice == "8":
                            if play_mp < 40:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Magic Boost!")
                                input()
                                mag_boo  = 25
                                play_mag = play_mag + mag_boo
                                play_mp = play_mp - 40
                                print("Something awoke inside you!")
                                input()
                            
                            
                    elif class_choice == 3:
                        if mag_choice == "1":
                            if play_mp < 10:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Cure!")
                                input()
                                cur_raw = random.randint(40, 50)
                                cure_hp = cur_raw + play_mag
                                play_hp = play_hp + cure_hp
                                if play_hp >= 175:
                                    print("You maxed out your HP!")
                                    input()
                                    play_hp = 175
                                else:
                                    print("You healed",cure_hp,"HP!")
                                    input()
                                
                                play_mp = play_mp - 10
                            
                        elif mag_choice == "2":
                            if play_mp < 8:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You casted Freeze!")
                                input()
                                bem_raw = random.randint(25, 40)
                                beam = bem_raw + play_mag
                                if boss_choice == 1:
                                    beam = beam * 2
                                print("You did",beam,"damage!")
                                input()
                                boss_hp = boss_hp - beam
                                play_mp = play_mp - 8
                            
                        elif mag_choice == "3":
                            if play_mp < 30:
                                print("Not enough MP!")
                                input()
                            else:
                                print("You revved up your engines!")
                                input()
                                for i in range(0, 3):
                                    miss_chance = random.randint(0,10)
                                    if miss_chance == 10:
                                        input("You missed!")
                                    else:
                                        raw_dam = random.randint(50,75)
                                        play_dam = raw_dam + play_off
                                        boss_hp = boss_hp - play_dam
                                        print("You did",play_dam,"damage!", end = '')
                                        input()
                            play_mp = play_mp - 30
                
                
                
                if boss_hp <= 0:
                    input("You Won! Holy shit!")
                    print()
                    break
        
        
        
    
    
    
    
    
    
    
else:
    print("Invalid input! Please try again")
    print()
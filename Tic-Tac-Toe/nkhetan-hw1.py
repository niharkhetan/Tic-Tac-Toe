'''
Created on Aug 31, 2014

Assignment 1:B551

This is a Tic Tac Toe between a Human and a reflex agent i.e Computer
Reflex agents learns through the moves of human and never let him/her win
It gives Human chance either to play as 'X' or as 'O'

Expected Outcome: Human should never WIN

@author: NiharKhetan
'''
 
import random

from operator import pos

'''Print current state of Tic Tac Toe on Screen'''

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""

''' Paremeter noDraw Type Boolean
    Function checks if the game has ended
        noDraw helps to reuse the function to know if game has ended
        noDraw --> True then do not print board and message -- Just proceed with return True
        noDraw --> False Game has actually ended so print board and message'''

def check_done(noDraw):
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            if noDraw != True:
                print_board()
                print turn, "won!!!"
            return True
        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        if noDraw != True:
            print_board()
            print turn, "won!!!"
        return True
    if noDraw != True:
        if " " not in map[0] and " " not in map[1] and " " not in map[2]:
            print_board()
            print "Draw"
            return True
    return False

'''Function  gets the position in number [pos] and converts it to equivalent location on map[X,Y]
    Input Parameter <-- Position 
    return --> converted location on map [X,Y]'''

def number_to_loc_on_map(position):
    mapY = position/3
    mapX = position%3
    if mapX != 0:
        mapX -=1
    else:
        mapX = 2
        mapY -=1
    return (mapX,mapY)

''' Function acts as a switch between X and O depending upon human plays first or computer
    Parameter <-- human_first  if True that means Human = X and Computer = O otherwise vice versa '''

def determine_current_turn(human_first):
    human = "X"
    computer ="O"
    if human_first == True:        
        return human, computer
    else:       
        return computer, human  
    
''' Checks if player is going to win:
        if YES then it blocks it and makes a move
        if NO then it leaves the position on the map as it is and does not make a move 
            RETURNS TRUE if it has made the move
            RETURNS FALSE if it has not made a move '''
    
def check_if_player_is_winning(human_first):
    turn1, turn2 = determine_current_turn(human_first)
    noDraw = True
    '''Fill positions one by one and check if Player is going to win '''
    for anticipated_pos in range(1,10):            
        X, Y = number_to_loc_on_map(anticipated_pos)        
        if map[Y][X] == " ":
            map[Y][X] = turn1
            player_wins = check_done(noDraw);
            '''Player is winning so block by making a move'''
            if player_wins == True:
                map[Y][X] = turn2
                return True
            else:
                map[Y][X] = " "
    noDraw = False
    return False

''' Function learns if there is an opportunity to win: 
        if there is an opportunity it makes the move and win the game
        RETURNS TRUE if it has made the move
        RETURNS FALSE if it has not made a move  '''

def learn_to_win(human_first):
    '''learn to fill Horizontal and Vertical lines if two blocks are filled'''
    turn1, turn2 = determine_current_turn(human_first)   
    for i in range(0,3):
        if map[i][0] == map[i][1] == turn2 and map[i][2] == " ":           
            map[i][2] = turn2
            return True
        elif map[i][1] == map[i][2] == turn2  and map[i][0] == " ":
            map[i][0] = turn2
            return True
        elif map[i][0] == map[i][2] == turn2  and map[i][1] == " ":
            map[i][1] = turn2
            return True
        elif map[0][i] == map[1][i] == turn2  and map[2][i] == " ":
            map[2][i] = turn2
            return True
        elif map[0][i] == map[2][i] == turn2  and map[1][i] == " ":
            map[1][i] = turn2
            return True
        elif map[1][i] == map[2][i] == turn2  and map[0][i] == " ":
            map[0][i] = turn2
            return True
    '''learn to fill diagonals if two blocks are filled'''  
    if map[0][0] == map[1][1] == turn2  and map[2][2] == " ":
        map[2][2] = turn2
        return True
    elif map[0][0] == map[2][2] == turn2  and map[1][1] == " ":
        map[1][1] = turn2
        return True
    elif map[1][1] == map[2][2] == turn2  and map[0][0] == " ":
        map[0][0] = turn2
        return True
    elif map[0][2] == map[1][1] == turn2  and map[2][0] == " ":
        map[2][0] = turn2
        return True
    elif map[0][2] == map[2][0] == turn2  and map[1][1] == " ":
        map[1][1] = turn2
        return True
    elif map[1][1] == map[2][0] == turn2  and map[0][2] == " ":
        map[0][2] = turn2
        return True
    else:
        return False


'''Function is a defensive function:
    it tries to find If two of same kind exist together diagonally [(1,5),(3,5),(7,5)(9,5)] then always make a move to a empty corner if it exists
    RETURNS TRUE if it has made the move
    RETURNS FALSE if it has not made a move '''
   
def two_x_together(human_first):
    turn1, turn2 = determine_current_turn(human_first)
    if map[1][1] == map [0][0] == turn1 or map[1][1] == map [2][2] == turn1 or map[1][1] == map [2][0] == turn1 or map[1][1] == map [0][2] == turn1:
        ''' find if all corners are full'''
        corner_full = True        
        for i in corners:
            X, Y = number_to_loc_on_map(i)
            if map[X][Y] == " ":
                corner_full = False
                break         
        if corner_full == False:
                
            '''not full --> so fill a corner 1,3,7,9'''
            moved = False
            while moved != True:
                random_position = random.choice(corners)           
                X, Y = number_to_loc_on_map(random_position)
                if map[Y][X] == " ":
                    map[Y][X] = turn2
                    moved = True
                    return True
        else:
            return False        
    else:
        return False
    

'''Function is a defensive function:
    it tries to find If two of same kind exist on opposite corners [(1,9),(3,7)] then never play on a corner
    RETURNS TRUE if it has made the move
    RETURNS FALSE if it has not made a move '''
   
def two_same_kind_on_corner_never_play_on_corner(human_first):
    turn1, turn2 = determine_current_turn(human_first)
    if map[0][0] == map[2][2] == turn1 or map[2][0] == map[0][2] == turn1:
        '''find if positions 2,4,6,8 are full'''
        others_full = True
        for i in other:
            X, Y = number_to_loc_on_map(i)
            if map[X][Y] == " ":
                others_full = False
                break        
        if others_full == False:
                
            '''Not full --> so fill one of the positions 2,4,6,8'''
            moved = False
            while moved != True:
                random_position = random.choice(other)           
                X, Y = number_to_loc_on_map(random_position)
                if map[Y][X] == " ":
                    map[Y][X] = turn2
                    moved = True
                    return True
        else:
            return False        
    else:
        return False
    
     
'''Function rule1 --> Whenever Human Plays on Corners - Move at Center.
    Also do some pre-checks >>
    1> Computer should always find an opportunity and try to win and take the action --> call learn_to_win()
    2> If opportunity to win is not there then it should find out if other player is going to win and take the action --> call check_if_player_is_winning()
    3> Then it does other checks to never let the opponent win:
        3.1> If two of same kind exist together diagonally [(1,5),(3,5),(7,5)(9,5)] then always make a move to a empty corner if it exists --> call two_x_together()
        3.2> If two of same kind exist on opposite corners [(1,9),(3,7)] then never play on a corner --> call two_same_kind_on_corner_never_play_on_corner()  
    '''
   
def rule1(human_first):   
    turn1, turn2 = determine_current_turn(human_first)    
    player_won = False
    learn = learn_to_win(human_first)
      
    if learn == False:
        player_won = check_if_player_is_winning(human_first)       
        if player_won == False:
            block_two_same_kind = two_x_together(human_first)
            if block_two_same_kind == False:
                never_play_opp_corners = two_same_kind_on_corner_never_play_on_corner(human_first);   
    
    
    if player_won == False and learn == False and block_two_same_kind == False and never_play_opp_corners ==False: 
        '''Move at Center'''      
        X, Y = number_to_loc_on_map(center[0])        
        if map[Y][X] == " ":
            map[Y][X] = turn2
        else:
            '''Center is full then fill any other place, so find a random place to fill'''
            rule3(human_first)            
            
'''Function rule2 --> Whenever Human Plays on Center - Move at Corners. Moving on other location creates opportunities for human to win
    Also do some pre-checks >>
    1> Computer should always find an opportunity and try to win and take the action --> call learn_to_win()
    2> If opportunity to win is not there then it should find out if other player is going to win and take the action --> call check_if_player_is_winning()
    3> Then it does other checks to never let the opponent win:
        3.1> If two of same kind exist together diagonally [(1,5),(3,5),(7,5)(9,5)] then always make a move to a empty corner if it exists --> call two_x_together()
        3.2> If two of same kind exist on opposite corners [(1,9),(3,7)] then never play on a corner --> call two_same_kind_on_corner_never_play_on_corner()  
    '''
def rule2(human_first):
    turn1, turn2 = determine_current_turn(human_first)
    player_won = False
    learn = learn_to_win(human_first)    
    if learn == False:
        player_won = check_if_player_is_winning(human_first)
        if player_won == False:
            block_two_same_kind = two_x_together(human_first)
            if block_two_same_kind == False:
                never_play_opp_corners = two_same_kind_on_corner_never_play_on_corner(human_first);      
    
    if player_won == False and learn == False and block_two_same_kind == False and never_play_opp_corners ==False:
        moved = False
        '''find if positions 1,3,7,9 are full'''        
        corner_full = True                
        for i in corners:
            X, Y = number_to_loc_on_map(i)
            if map[X][Y] == " ":
                corner_full = False
                break          
        if corner_full == False:
                
            '''Not full --> so fill one of the positions 1,3,7,9'''
            moved = False
            while moved != True:
                random_position = random.choice(corners)           
                X, Y = number_to_loc_on_map(random_position)
                if map[Y][X] == " ":
                    map[Y][X] = turn2
                    moved = True
                    return True
        else:
            rule3(human_first)                    
        
''' Function rule 3 --> Just fills up a available position on Map Randomly'''
                    
def rule3(human_first):    
    turn1, turn2 = determine_current_turn(human_first)   
    player_won = False
    learn = learn_to_win(human_first)    
    if learn == False:
        player_won = check_if_player_is_winning(human_first)
        if player_won == False:
            block_two_same_kind = two_x_together(human_first)
            if block_two_same_kind == False:
                never_play_opp_corners = two_same_kind_on_corner_never_play_on_corner(human_first);   
    
    if player_won == False and learn == False and block_two_same_kind == False and never_play_opp_corners ==False:
        moved = False        
        while moved != True:
            random_position = random.choice(range(1,10))            
            X, Y = number_to_loc_on_map(random_position)
            if map[Y][X] == " ":
                map[Y][X] = turn2
                moved = True
 
'''MAIN 
    Modified main of given program to:
    1> Give option Who Plays First? Human or Computer
    2> The way input happens if either of them plays first'''

if __name__ == '__main__':
   
    turn = "X"
    map = [[" "," "," "],
           [" "," "," "],
           [" "," "," "]]
    done = False
    right_selection = False
    corners = [1,3,7,9]
    center = [5]
    other = [2,4,6,8]
    
    while right_selection != True:
        print "Select >> (1) If you want to play X"
        print "          (2) If you want to play O"
        try:
            chance = input("Select: ")
            
            if chance == 1:
                '''human plays first'''
                human_first = True
                right_selection = True
                while done != True:
                    print_board()
                    
                    print turn, "'s turn"
                    print                    
                    moved = False
                    while moved != True:                        
                        if turn == "X":
                            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
                            print "7|8|9"
                            print "4|5|6"
                            print "1|2|3"
                            print
                    
                            try:
                                pos = input("Select: ")
                                if pos <=9 and pos >=1:                        
                                    X, Y = number_to_loc_on_map(pos)
                                        
                                    if map[Y][X] == " ":                           
                                        map[Y][X] = turn
                                        moved = True
                                        done = check_done(False)
                                        
                                        if done == False:
                                            if turn == "X":                                    
                                                turn = "O"
                                            else:
                                                turn = "X"                        
                                
                            except:
                                print "You need to add a numeric value"
                        else:
                            print ("Was Computer's turn")
                            
                            if pos in corners:                                                  
                                rule1(human_first)
                            elif pos in center:
                                rule2(human_first)
                            else:
                                rule3(human_first) 
                                  
                            moved = True
                            done = check_done(False)
                            
                            if done == False:
                                if turn == "X":                        
                                    turn = "O"
                                else:
                                    turn = "X"
                
                
            elif chance == 2:
                '''computer plays first'''
                human_first = False
                right_selection = True                
                while done != True:
                    print_board()
                    print turn, "'s turn"
                    print                    
                    moved = False
                    while moved != True:
                        if turn == "X":
                            print "Was Computer's turn"
                            rule3(human_first)
                            moved = True
                            done = check_done(False)
                            
                            if done == False:
                                if turn == "X":                        
                                    turn = "O"
                                else:
                                    turn = "X"
                        else:
                            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
                            print "7|8|9"
                            print "4|5|6"
                            print "1|2|3"
                            print
                    
                            try:
                                pos = input("Select: ")
                                if pos <=9 and pos >=1:                        
                                    X, Y = number_to_loc_on_map(pos)
                                        
                                    if map[Y][X] == " ":                           
                                        map[Y][X] = turn
                                        moved = True
                                        done = check_done(False)
                                        
                                        if done == False:
                                            if turn == "X":                                    
                                                turn = "O"
                                            else:
                                                turn = "X"                        
                                
                            except:
                                print "You need to add a numeric value"
                                    
        except:
            print ("You need to give a numeric value")

    
   
                

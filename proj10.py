
''' 
Computer Project #10
Functions that correspond with the options in the menu
def functions
    call the deck deal and shuffe display the cards 
    and move the cards to the right tableaus
while loop 
    elif statements for each option
        for statements and if statements 
for loop 
    call functions 
    output the functions answers
end the program '''

import cards  

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''
     
     
MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''



def init_game():
    '''
    this function is to initialize a game
    
    Returns
    -------
    my_deck : the deck of cards that are shuffled 
    tabelau_lst : the cards that are sorted out in the tableau 
    '''
    my_deck = cards.Deck()
    my_deck.shuffle()
    tabelau_lst=[[],[],[],[]]
    foundation_lst=[]
    deal_to_tableau(tabelau_lst, my_deck)
   
    return (my_deck, tabelau_lst, foundation_lst)   
    
def deal_to_tableau( tableau, stock):
    '''This function doesnt return anything it just deals cards to the tableau'''
    for index in range(4):       
        card=stock.deal()        
        if card != None:
            tableau[index].append(card)           
                    
def validate_move_to_foundation( tableau, from_col ):
    '''  this function will determine if a requested move to the foundation is valid. 
         check for the right order then check for the right suit
             tableau: the 7 piles that make up the main table
             from_col: is the index of the column in the tableau range from 0 to 3. 
         returns:
             True : if move is valid
             False: if the move isnt valid
             '''
    if True:
        try:            
            value2= tableau[from_col][-1]
        except:
            print("\nError, empty column: {}".format(from_col+1))
            return False            
    rank=value2.rank()
    if rank==1:
        rank=100
    suit=value2.suit()
    for columns in tableau:
        if columns:
            lastcard=columns[-1]
            lastcard_rank=lastcard.rank()
            if lastcard_rank==1:
                lastcard_rank=100
            lastcard_suit=lastcard.suit()
            if lastcard_suit== suit and lastcard_rank>rank:
                return True 
    print("\nError, cannot move {}.".format(value2))
    return False
        
    
def move_to_foundation( tableau, foundation, from_col):
    '''this will move a card from the tableau to the foundation. 
            tableau: the 7 piles that make up the main table
            from_col: is the index of the column in the tableau range from 0 to 3
        return:
            foundation: the 4 piles of cards once moved to the 
                foundation they cant be moved back
                '''
    charcter=validate_move_to_foundation(tableau, from_col)
    if charcter:
        element=tableau[from_col].pop()
        foundation=foundation.append(element)
    return foundation

def validate_move_within_tableau( tableau, from_col, to_col ):
    '''this function will determine if a requested move to the tableau is valid. 
         check for the right order then check for the right suit
             tableau: the 7 piles that make up the main table
             from_col: is the index of the column in the tableau range from 0 to 3
             to_col: the indices of the columns in the tableau range from 0 to 3.
         returns:
             True : if move is valid
             False: if the move isnt valid'''
    
    if len(tableau[to_col]) != 0:
        print("\nError, target column is not empty:",to_col+1)
        return False

    if True:
        try:            
            value2= tableau[from_col][-1]
        except:
            print("\nError, no card in column: {}".format(from_col+1))
            return False            
    if not tableau[to_col]:
        return True
    print("\nError, target column is not empty:",to_col+1)
    return False

def move_within_tableau( tableau, from_col, to_col ):
    '''this will move a card from one tableau to the other tableau. 
            tableau: the 7 piles that make up the main table
            from_col: is the index of the column in the tableau range from 0 to 3
            to_col: the indices of the columns in the tableau range from 0 to 3.
        return:
            Tableau: seven piles that make up the main table
    '''
    charcter=validate_move_within_tableau(tableau, from_col, to_col)
    if charcter :
        element=tableau[from_col].pop()
        tableau[to_col].append(element)
    return tableau
    
        
def check_for_win( tableau, stock ):
    '''this will be used to check if the game has been won by the user. 
        tableau: the 7 piles that make up the main table
        stock:contains cards that have not yet been moved to a 
        foundation pile or tableau column. 
    returns:
            True: If the user won the game
            False: If the user has not won the game yet
        '''
    
    value=len(stock)
    count=0  
    emptylst=[]
    if value ==0:
        for character in tableau:
            if character==emptylst:
                continue
            for element in character:
                if element== None:
                    continue
                card_rank=element.rank()
                if card_rank==1:
                    count+=1
                else:
                    return False
        if count==4:
            return True   
        else:
            return False
    else:
        return False
                

def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.
        tableau: the 7 piles that make up the main table
        stock:contains cards that have not yet been moved to a 
        foundation pile or tableau column. 
        doesnt return  anything just prints out the crads in the right format'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')                
        print()


def get_option():
    '''Returns: what the user chose wants to do with the program'''
    option1 =input("\nInput an option (DFTRHQ): ")
    option=option1.upper().strip().split()
    if option[0] =="D" or option[0]=="R" or option[0]=="H" or option[0]=="Q":
        if len(option) == 1:
            return (option)

    
    elif option[0]=="F":
        try:
            x=int(option[1])-1
            if x >= 0 and x <= 3:
                emptylst=[]
                emptylst.extend([option[0],x])            
                return emptylst
        except :
            print("\nError in option:",option1)
            return []
        
    elif option[0]=="T":
        try:
            x=int(option[1])-1
            y=int(option[2])-1
            if x >= 0 and y >= 0 and x <= 3 and y <= 3:
                emptylst=[]
                emptylst.extend([option[0],x,y])            
                return emptylst
        except :
            print("\nError in option:",option1) 
            return []
                       
    else:
        print("\nError in option:",option1) 
        return [] 

    print("\nError in option:",option1)  
    return []   # stub; delete and replace with your code
        
def main():
    print(RULES) #prints the rules of the game
    print(MENU)  #prints the menu that the user chooses from 
    stock, tableau, foundation =init_game()  #intial card set up to start 
    display(stock, tableau, foundation)
    #will display the cards in the right format   
    
    while True: #start of the while loop
        choice=get_option() #for the user to input the option
        if choice != []: #if there are cards in the column then we continue
            if choice[0]=="D": #this will deal the cards to the tableaus
                deal_to_tableau(tableau,stock) #calls the function to deal
                                    
            elif choice[0]=="R": 
                #this will restart the game and give a new set of cards
                stock, tableau, foundation =init_game()
                print("\n=========== Restarting: new game ============")
                print(RULES)  #prints the rules of the game
                print(MENU) #prints the menu that the user chooses from 
            
            elif choice[0]=="H": #reprompts for the menu
                print(MENU) #prints the menu that the user chooses from 
                
            elif choice[0] =="Q": #quits the game and ends the loop
                print("\nYou have chosen to quit.") #quit message
                break #breaks the while loop
            
            elif choice[0]=="F": 
            #moves the cards from Tableau column the user wants to the Foundation.
                num_x=choice[1] 
                #indexs to find out which column that the user wants to move from          
                move_to_foundation(tableau, foundation, num_x) 
                #calls function to see if the move is valid 
            
            elif choice[0]=="T":
            #moves the cards from Tableau column x to empty Tableau column y.
                num_x= choice[1]
                #indexs to find out which column that the user wants to move from 
                num_y=choice[2]
                move_within_tableau(tableau, num_x, num_y)
                #calls function to see if the move is valid 
            
            if check_for_win(tableau, stock):
                #calls the check for win to see if the user won
                print("\nYou won!") #prints the you won message
                break #breaks the while loop
            
            display(stock, tableau, foundation) 
            #displays the cards depending on what the user said 
  

if __name__ == '__main__':
     main()

# Tic-Tac-Toe.  Matias Schvindt

def main():
    choise = ""
    box_one = 1
    box_two = 2
    box_three = 3
    box_four = 4
    box_five = 5
    box_six = 6
    box_seven = 7
    box_eight = 8
    box_nine = 9
    turn = 1
    board = create_board(box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine)
    win = False
    game = True

    while game == True:
        display_board(box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine)
        if box_one == "x" and box_two == "x" and box_three == "x":
            print("Player X win, Congratulations")
            win = True
            game = False
        elif  box_one == "x" and box_four == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_one == "x" and box_five == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_two == "x" and box_five == "x" and box_eight == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_three == "x" and box_six == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_three == "x" and box_five == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_four == "x" and box_five == "x" and box_six == "x": 
            print("Player X win, Congratulations")   
            win = True
            game = False
        elif  box_seven == "x" and box_eight == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif turn == 10 and win == False:        
                print("It's a draw, Good game.")
                game = False
        else:  
            choise = int(input("O's turn to choose a square (1-9): "))
            turn = turn + 1
            print()
            if choise == 1:
                box_one = "o"
            elif choise == 2:
                box_two = "o"    
            elif choise == 3:
                box_three = "o"
            elif choise == 4:
                box_four = "o"
            elif choise == 5:
                box_five = "o"
            elif choise == 6:
                box_six = "o"    
            elif choise == 7:
                box_seven = "o"
            elif choise == 8:
                box_eight = "o"
            elif choise == 9:
                box_nine = "o"   
      
        display_board(box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine)             

        if box_one == "o" and box_two == "o" and box_three == "o":
            print("Player O win, Congratulations")
            win = True
            game = False
        elif  box_one == "o" and box_four == "o" and box_seven == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif  box_one == "o" and box_five == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif  box_two == "o" and box_five == "o" and box_eight == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif  box_three == "o" and box_six == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif  box_three == "o" and box_five == "o" and box_seven == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif  box_four == "o" and box_five == "o" and box_six == "o": 
            print("Player O win, Congratulations")   
            win = True
            game = False
        elif  box_seven == "o" and box_eight == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            win = True
            game = False
        elif turn == 10:
                print("It's a draw, Good game.")
                game = False

        if box_one == "x" and box_two == "x" and box_three == "x":
            print("Player X win, Congratulations")
            win = True
            game = False
        elif  box_one == "x" and box_four == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_one == "x" and box_five == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_two == "x" and box_five == "x" and box_eight == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_three == "x" and box_six == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_three == "x" and box_five == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False
        elif  box_four == "x" and box_five == "x" and box_six == "x": 
            print("Player X win, Congratulations")   
            win = True
            game = False
        elif  box_seven == "x" and box_eight == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            win = True
            game = False                    
        else:
            choise = int(input("X's turn to choose a square (1-9): "))
            turn = turn + 1
            print()
            if choise == 1:
                box_one = "x"
            elif choise == 2:
                box_two = "x"    
            elif choise == 3:
                box_three = "x"
            elif choise == 4:
                box_four = "x"
            elif choise == 5:
                box_five = "x"
            elif choise == 6:
                box_six = "x"    
            elif choise == 7:
                box_seven = "x"
            elif choise == 8:
                box_eight = "x"
            elif choise == 9:
                box_nine = "x"
           
    print("Thanks for playing.")    

def create_board(box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine):
    board = [box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine]
    
    return board

def display_board(box_one, box_two, box_three, box_four, box_five, box_six, box_seven, box_eight, box_nine):
    print()
    print(f"      {box_one}|{box_two}|{box_three}")
    print('      -+-+-')
    print(f"      {box_four}|{box_five}|{box_six}")
    print('      -+-+-')
    print(f"      {box_seven}|{box_eight}|{box_nine}")
    print()


if __name__ == "__main__":
    main()   
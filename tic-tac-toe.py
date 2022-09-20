# Tic-Tac-Toe.  Matias Schvindt

def main():

    box_one = 1
    box_two = 2
    box_three = 3
    box_four = 4
    box_five = 5
    box_six = 6
    box_seven = 7
    box_eight = 8
    box_nine = 9

    game = True

    while game == True:

        if box_one == "x" and box_two == "x" and box_three == "x":
            print("Player X win, Congratulations")
            game = False
        elif  box_one == "x" and box_four == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            game = False
        elif  box_one == "x" and box_five == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            game = False
        elif  box_two == "x" and box_five == "x" and box_eight == "x": 
            print("Player X win, Congratulations") 
            game = False
        elif  box_three == "x" and box_six == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            game = False
        elif  box_three == "x" and box_five == "x" and box_seven == "x": 
            print("Player X win, Congratulations") 
            game = False
        elif  box_four == "x" and box_five == "x" and box_six == "x": 
            print("Player X win, Congratulations")   
            game = False
        elif  box_seven == "x" and box_eight == "x" and box_nine == "x": 
            print("Player X win, Congratulations") 
            game = False
        else:
            input("o's turn to choose a square (1-9): ")    
            #ingresar el numero a la funcion player_two




        if box_one == "o" and box_two == "o" and box_three == "o":
            print("Player O win, Congratulations")
            game = False
        elif  box_one == "o" and box_four == "o" and box_seven == "o": 
            print("Player O win, Congratulations") 
            game = False
        elif  box_one == "o" and box_five == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            game = False
        elif  box_two == "o" and box_five == "o" and box_eight == "o": 
            print("Player O win, Congratulations") 
            game = False
        elif  box_three == "o" and box_six == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            game = False
        elif  box_three == "o" and box_five == "o" and box_seven == "o": 
            print("Player O win, Congratulations") 
            game = False
        elif  box_four == "o" and box_five == "o" and box_six == "o": 
            print("Player O win, Congratulations")   
            game = False
        elif  box_seven == "o" and box_eight == "o" and box_nine == "o": 
            print("Player O win, Congratulations") 
            game = False
        else:
            input("x's turn to choose a square (1-9): ")    
            #ingresar el numero a la funcion player_one




def player_one():
    # crear una lista de las opciones del jugador X


def player_two():    
    # crear una lista de las opciones del jugador o







 if __name__ == "__main__":
    main()   
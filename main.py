import random



# generate user input  
 
while True:
     #create a list and variables for the game
     R = "Rock"
     S = "Scissors"
     P = "Paper"

    
   
     list1 = ["Rock", "Scissors", "Paper"]

  

     Player1 = "Any Player"
     Player2 = "CPU"

     Player1_select = input("This is a rock,paper and scissors game.Rock crashes scissors ,scissors cuts through paper and paper covers the rock.Choose from the options(Rock,Paper or Scissors)  ")
     Player2_select = random.choice(list1)

     print(Player1_select)
     print(Player2_select)
    
    
     if Player1_select==Player2_select:
         print("it is a tie ")
     elif Player1_select== R:
         if Player2_select== S:
             print("you win, Rock crashes scissors")
         elif Player2_select==P:
             print("CPU wins ,paper covers the rock")
         

             

     elif Player1_select==S:
         if Player2_select == R:
             print("CPU wins ,Rock crashes scissors")
         elif Player2_select== P:
             print("you win,scissors cuts through paper")
         

     elif Player1_select==P:
         if Player2_select==R:
             print("you win, paper covers the rock")
         elif Player2_select==S:
             print("CPU wins, scissors cuts through paper")
         
     else:
        print("invalid input")
     Replay =  input("do you wanna try again?yes or no  ")
     if Replay.lower() != "yes":
         break
        






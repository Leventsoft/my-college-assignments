from random import randint

squares = [
{
"penalty": -1,
"reward": -1
},
{
"penalty": -1,
"reward": -1
}
]
squares[0]["penalty"] = int(input("Player 1, please enter your penalty square number: "))
squares[0]["reward"] = int(input("Player 1, please enter your reward square number: "))
squares[1]["penalty"] = int(input("Player 2, please enter your penalty square number: "))
squares[1]["reward"] = int(input("Player 2, please enter your reward square number: "))
players_current_squares = [0, 0]

while players_current_squares[0] < 100 and players_current_squares[1] < 100:
# TODO: implement game logic
    tmp = input("Player 1 please press enter.")
    dice1 = randint(1,6)
    players_current_squares[0] = players_current_squares[0] + dice1

    print(f"Player 1 rolls {dice1}!")
    
    if players_current_squares[0] == squares[0]["penalty"] or players_current_squares[0] == squares[1]["penalty"]:
        players_current_squares[0] = players_current_squares[0] - 10
        print(f"Player 1 hit the penalty square and went 10 squares back")
    
    if players_current_squares[0] == squares[0]["reward"] or players_current_squares[0] == squares[1]["reward"]:
        players_current_squares[0] = players_current_squares[0] + 10
        print(f"Player 1 hit the reward square and went 10 squares forward")

    if players_current_squares[0] < 100:
        print(f"Player 1 is on {players_current_squares[0]} now!\n")
    
    else:
        print("Player 1 won!")
        break


    tmp = input("Player 2 please press enter.")
    dice2 = randint(1,6)
    players_current_squares[1] = players_current_squares[1] + dice2

    print(f"Player 2 rolls {dice2}!")
    
    if players_current_squares[1] == squares[0]["penalty"] or players_current_squares[1] == squares[1]["penalty"]:
        players_current_squares[1] = players_current_squares[1] - 10
        print(f"Player 2 hit the penalty square and went 10 squares back")
    
    if players_current_squares[1] == squares[0]["reward"] or players_current_squares[1] == squares[1]["reward"]:
        players_current_squares[1] = players_current_squares[1] + 10
        print(f"Player 2 hit the reward square and went 10 squares forward")

    if players_current_squares[1] < 100:
        print(f"Player 2 is on {players_current_squares[1]} now!\n")
    
    else:
        print("Player 2 won!")
        break
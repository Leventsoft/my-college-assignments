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
    squares[0] = squares[0] + dice1

    print(f"Player 1 rolls {dice1}!")
    
    if squares[0] == squares[0]["penalty"] or squares[0] == squares[1]["penalty"]:
        squares[0] = squares[0] - 10
        print(f"Player 1 hit the penalty square and went 10 squares back, now It is on {squares[0]}")
    
    else squares[0] == squares[0]["reward"] or squares[0] == squares[1]["reward"]:
        squares[0] = squares[0] + 10
        print(f"Player 1 hit the reward square and went 10 squares forward")

    print(f"Player 1 is on {squares[0]} now!")
# Paste Task 7's solution here
from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises
import random

def initialise_game() -> dict:
    snakes = {'25': 6, '44': 23, '65': 34, '76': 28, '99': 56}
    ladders = {'8': 43, '26': 39, '38': 55, '47': 81, '66': 92}
    players = {'Red': 0, 'Blue': 0, 'Green': 0, 'White': 0}
    game = {'players': players,'snakes': snakes,'ladders': ladders}    
    return game
    

def get_num_players() -> int:
    players_count = int(input("Please enter the number of players, at most 4 players:"))
    return players_count

def play_game(game: dict) -> str:
    game["surprise_tiles"] = generate_surprises()
    if_skip = False
    while True:
        for player, position in game['players'].items():
            print(if_skip)
            if if_skip == True:
                if_skip = False
                continue
            else:
                print(f"{player}'s turn.")
                roll_result = roll_the_dice()
                print(roll_result)
                position += roll_result
                if position > 100:
                    position -= roll_result
                else:
                    game['players'][player] = position
                    print(f"after roll position={position} players={game['players']}")
                    winner = pick_winner(game["players"])
                    if pick_winner(game["players"]) != None:
                        return winner
                    game['players'][player] = position
                    position = check_snakes_and_ladders(position, game)
                    game['players'][player] = position
                    print(f"after check_snakes_and_ladders position={position} players={game['players']}")
                    winner = pick_winner(game["players"])
                    if pick_winner(game["players"]) != None:
                        return winner                
                    position,if_skip = check_surprise_tiles(position, game)
                    game['players'][player] = position
                    print(f"after check_surprise_tiles position={position} players={game['players']}")
                    winner = pick_winner(game["players"])
                if pick_winner(game["players"]) != None:
                    return winner                
            

def check_snakes_and_ladders(position: int, game: dict) -> int:
    position_str = str(position)
    while position_str in game['snakes'] or position_str in game['ladders']:
        if position_str in game['snakes']:
            print(f"{position} is a snake head! Going down to {game['snakes'][position_str]}.")
            position = game['snakes'][position_str]
        elif position_str in game['ladders']:
            print(f"{position_str} is a ladder base! Climbing up to {game['ladders'][position_str]}.")
            position = game['ladders'][position_str]
        position_str = str(position)
    return position

def check_surprise_tiles(position: int, game: dict) -> (int,bool):
    if_skip = False
    if position in game['surprise_tiles']:
        print(f"Surprise tile at {position}!")
        special_roll_result = special_roll()
        print(f"Special roll result: {special_roll_result}.")
        if special_roll_result == 0:
            print("You get to roll again!")
            roll_result = roll_the_dice()
            position += roll_result
            if position > 100:
                position -= roll_result
            position = check_snakes_and_ladders(position, game)
            position,if_skip = check_surprise_tiles(position, game)
        elif special_roll_result == 1:
            print("The next player loses a turn.")
            if_skip = True
        elif special_roll_result == 2:
            print("All other players move back 5 spaces.")
            for player, player_position in game['players'].items():
                print(player_position)
                print(position)
                if player_position != position:
                    new_position = max(0, player_position - 5)
                    game['players'][player] = new_position
                    print(f"{player} moves back to {new_position}.")
        if special_roll_result in [0,1]:
            position = check_snakes_and_ladders(position, game)
            #game["players"][player] = position
            #check_surprise_tiles(position, game)

    return (position,if_skip)

def pick_winner(players: dict) -> str:
    for player, position in players.items():
        if position == 100:
            return player
    return None
    

def get_num_players() -> int:
    while True: 
        num_players = input("Enter the number of players: ")
        if num_players in ['2','3','4']:
            return int(num_players)
        else:
            print('Please re-enter again!')



def turn_by_turn_gameplay():
    global game
    game["surprise_tiles"] = generate_surprises()
    if_skip = False
    
    while True:
        for player, position in game['players'].items():
            if if_skip == True:
                if_skip = False
                continue
            else:
                while True:
                    answer = input('Please enter roll or quit:')
                    if answer == 'roll':
                        print(f"{player}'s turn.")
                        roll_result = roll_the_dice()
                        position += roll_result
                        if position > 100:
                            position -= roll_result
                        position = check_snakes_and_ladders(position, game)
                        position,if_skip = check_surprise_tiles(position, game)
                        game['players'][player] = position
                        print(f"{player} is in {position}.")
                        break
                    elif answer == 'quit':
                        return 
                    else:
                        print('Please re-enter again!')

game = None
def main():
    global game
    game = initialise_game()
    num_players = get_num_players()
    players = ["Red", "Blue", "Green", "White"]
    game["players"] = dict(zip(players[:num_players], [0]*num_players))
    if num_players in [3,4]:
        winner = play_game(game)
        print(f"The winner is {winner}!")

    # Play a turn by turn game
    if num_players == 2:
        turn_by_turn_gameplay()
        winner = pick_winner(game["players"])
        print(f"The winner is {winner}!")

        

if __name__ == '__main__':
    main()


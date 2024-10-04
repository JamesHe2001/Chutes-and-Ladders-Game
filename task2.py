# Paste Task 2's solution here
# DO NOT delete this line
import random
# Player 1 Name
p1_name = random.choice(['Red','Blue','Green','White'])
# Player 1 Position
p1_position = 0
# Player 2 Name
p2_name = random.choice(['Red','Blue','Green','White'])
while p1_name == p2_name :
    p2_name = random.choice(['Red','Blue','Green','White'])
# Player 2 Position
p2_position = 0
# Snake Head Positions
snake_heads = []
while len(snake_heads) < 5:
    random_snake_heads = random.randint(2,100)
    if random_snake_heads not in snake_heads:
        snake_heads.append(random_snake_heads)
# Snake Tail Positions
snake_tails = []
for i in range(5):
    while len(snake_tails) < 5:
        random_snake_tails = random.randint(1,snake_heads[i]-1)
        if random_snake_tails not in snake_tails:
            snake_tails.append(random_snake_tails)
# Ladder Base Positions
ladder_bases = []
while len(ladder_bases) < 5:
    random_ladder_bases = random.randint(1,99)
    if random_ladder_bases not in ladder_bases:
        ladder_bases.append(random_ladder_bases)
# Ladder Tops Positions
ladder_tops = []
for i in range(5):
    while len(ladder_tops) < 5:
        random_ladder_tops = random.randint(ladder_bases[i]+1,100)
        if random_ladder_tops not in ladder_tops:
            ladder_tops.append(random_ladder_tops)
# Print the position for Player 1
print('Player',p1_name,'is in position',p1_position)
# Print the position for Player 2
print('Player',p2_name,'is in position',p2_position)




# Task 2 begins here 
def roll_the_dice():
    return random.randint(1,6)

# Roll the dice for the first player
diceroll = roll_the_dice()

# Write the logic to move the first player
if p1_position + diceroll <=100:
    p1_position += diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Write the logic to move the second player
if p2_position + diceroll <= 100:
    p2_position += diceroll

# Print the position of the first player
print(f'Player {p1_name} is in position {p1_position}')

# Print the position of the second player
print (f'{p2_name} is in this postiion {p2_position}')

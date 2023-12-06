with open("day2/input.txt", 'r') as f:
  lines = f.readlines()

games = [line.split(':')[1] for line in lines]

stripped = []
for game in games:
  stripped_g = []
  turns = [g.split(',') for g in game.split(';')]
  for t in turns:
    if 'red' in t:
      

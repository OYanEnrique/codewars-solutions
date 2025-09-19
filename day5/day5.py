'''
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes
this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
'''
def count_points(game_results):
	total_points = 0
	for game in game_results:
		score = game.split(':')
		our_goal = int(score[0])
		opponent_goal = int(score[1])
		if our_goal > opponent_goal:
			total_points += 3 
		if our_goal == opponent_goal:
			total_points += 1
		else:
		 	total_points += 0
	return f"Your team have {total_points} total points"

# Use example
games = ["2:2","4:4","7:7","2:1"]
print(count_points(games))
			
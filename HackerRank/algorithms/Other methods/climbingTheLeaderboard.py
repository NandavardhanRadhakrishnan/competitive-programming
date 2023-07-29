# https://www.hackerrank.com/challenges/climbing-the-leaderboard
# for dense ranking, current leaderboard given in:ranked , player's score after each game given in:player, track and display rank after every game

def climbingLeaderboard(ranked, player):
	playerRanks=[]
	ranked_set = list(set(ranked))
	ranked_set.sort(reverse=True)
	for score in player:
		if score in ranked_set:
			print(score,"in list")
			playerRanks.append(ranked_set.index(score)+1)
		else:
			ranked_set.append(score)
			ranked_set.sort(reverse=True)
			print(score,"not in list")
			playerRanks.append(ranked_set.index(score)+1)
			ranked_set.remove(score)
	return playerRanks

r = [100,90,90,80]
p = [70,80,105]
print(climbingLeaderboard(r,p))

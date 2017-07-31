import numpy as np
import random
import scipy.stats as ss  

def distance(p1,p2):
	"""Find the distance btw points p1 and p2"""
	return np.sqrt(np.sum(np.power(p1-p2, 2)))


p1 = np.array([1,1])
p2 = np.array([4,4])


def majority_vote(votes):
	"""
	"""
	vote_counts = {}
	for vote in votes:
		if vote in vote_counts:
			vote_counts[vote] += 1
		else:
			vote_counts[vote] = 1
	return vote_counts

votes = [1,2,3,1,2,3,1,2,3,3,3,3,3]
vote_counts = majority_vote(votes)


winners = []
max_count = max(vote_counts.values())
for vote, count in vote_counts.items():
	if count == max_count:
		winners.append(vote)


"""this version 2 returns the winner"""
def majority_vote_2(votes):
	"""
	"""
	vote_counts = {}
	for vote in votes:
		if vote in vote_counts:
			vote_counts[vote] += 1
		else:
			vote_counts[vote] = 1

	winners = []
	max_count = max(vote_counts.values())
	for vote, count in vote_counts.items():
		if count == max_count:
			winners.append(vote)

	return random.choice(winners)

def majority_vote_short(votes):
	"""
	Return the most common element in votes
	"""
	mode, count = ss.mstats.mode(votes)
	return mode


# votes = [1,2,3,1,2,3,1,2,3,3,3,3,3]
# winner = majority_vote_short(votes)
# print(winner)


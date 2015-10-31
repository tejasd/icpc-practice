# (population, initial_perc, delta_p) = precinct

def calcVotes(precinct, money):
	(population, initial_perc, delta_p) = precinct
	final_perc = initial_perc + (money/(10.1 + money)) * delta_p
	return int(round(population * final_perc / 100))

if __name__ == "__main__":
	money = 100
	precincts = 3

	precintcList = []
	precintcList.append((3000, 45, 15))
	precintcList.append((2000, 60, 10))
	precintcList.append((4000, 20, 5))



	precinctMoneyList = []

	for i in range(precincts):
		precinctMoneyList.append(0)

	for dontCare in range(money):
		maxVoteIncrease = 0
		maxPrecinct = -1
		for (i, precinct) in enumerate(precintcList):
			diff = calcVotes(precinct, precinctMoneyList[i]+1) - calcVotes(precinct, precinctMoneyList[i])
			if (diff > maxVoteIncrease):
				maxVoteIncrease = diff
				maxPrecinct = i

		precinctMoneyList[maxPrecinct] += 1

	totalVotes = map(calcVotes, precintcList, precinctMoneyList)
	print(sum(totalVotes))
	print(precinctMoneyList)







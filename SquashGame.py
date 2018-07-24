import random
import csv
import matplotlib.pyplot as plt

#'gameover', the function to test if game is over
def gameover(a, b):
	if a == 11 and b <= 9 or a <= 9 and b == 11:
		return True
	#if game is 10-10, hence is drawn
	elif a >= 10 and b >= 10 and abs (a-b) == 2:
		return True
	#Game is not over
	else:
		return False

def game(ra,rb):
	a = 0
	b = 0
	#probability that player a wins a point
	P = ra / (ra + rb)
	while not gameover (a,b):
		#random number generated - point won by player based on chance
		r = random.random()
		if r < P:
			a += 1
		else:
			b += 1

	return(a, b)

#print (game(70, 30))

#Function to estimate probability of player A to win a game again player B
def winProbability(ra, rb, n):
	A = 0
	B = 0

	for i in range(0, n):
		winner = game(ra, rb)
		#if ra is larger than rb, add 1 to A and if not, add 1 to B
		if winner[0] > winner[1]:
			A += 1
		else:
			B += 1

	probability = float(round(A/(A + B), 2))
	return probability
#print(winProbability(70, 30, 100))

#function to read csv file as filename and return a list of tuples
def csvOpen(filename):
	dic = []
	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		#this skips the header row
		heading = next(rdr)
		#this goes through the first two columns and add them to 'dic' from the csv file
		for row in rdr:
			dic.append((int(row[0]), int(row[1])))

	return dic

#print (csvOpen("test.csv"))	

def table(dic):
	#probability and ability calculated from csvOpen function
	probabibility = [(row[0]) / (row[0] + row[1]) for row in dic]
	ability = [(row[0]) / row[1] for row in dic]

	plt.title('Graph showing the probability that \n player beats player b versus ra/ab')
	plt.plot(ability, probability, 'ro')
	plt.axis([0.0, 4.0, 0.0, 1.0])
	plt.xlabel('ra / rb')
	plt.ylabel('Probability that A will win')
	plt.show()

#table(csvOpen("test.csv"))



#in repeated games the overall probability increases. The definition starts with 1 game.
def simulate(ra, rb, winProbability):
	i = 1 
	prob = ra / (ra + rb)
#whilst the probability of player A winning an amount of games is lower than the desired, the number of games increases.
	while 1 - prob ** i < winProbability:
		i += 1
	return i
#print(simulate(60, 40, 0.9))

def Englishscoringsystem(ra,rb):
	
	probability = ra/(ra + rb)

	ascore = 0
	bscore = 0

	theserver = "A"
	firstto8 = "A"#this is the first player who reaches 8 points.

	while ascore < 9 and bscore < 9 and bscore + ascore != 16:
		newpoint = random.random()
		if newpoint<probability:
			if theserver == "A":
				ascore += 1
			else:
				theserver = "A"
		else:
			if theserver == "B":
				bscore += 1
				if bscore == 8 and ascore <8:
					firstto8 = "B"#if b scores 8 before a then it becomes the instigator
			else:
				theserver = "B"
#code for when scored are tied 8-8.
	if bscore ==8 and ascore == 8:
		if firsto8 == "A":#A will play for 9
			while ascore < 9 and bscore < 9:
				newpoint = random.random()
				if newpoint<probability:
#if point won by A
					if theserver == "A":
						ascore+=1
					else:
						theserver = "A"
				else:
					if theserver == "B":
						bscore+=1
					else:
						theserver == "B"
#if B wants to play to 10
		elif firstto8 == "B":
			while ascore < 10 and bscore < 10:
				newpoint = random.random()
				if newpoint<probability:
					if theserver == "A":
						ascore+=1
					else:
						theserver = "A"
				else:
					if theeserver == "B":
						bscore+=1
					else:
						theserver == "B"

	return(ascore, bscore)

def englishtime():	
#I assume that each point 45 seconds
#assume that each match is best of 3 games
#player A will choose to play to 10 and player B choose to play to 9
	a = (10,1)
	b = (8,1)
	c = (6,1)
	d = (4,1)
	e = (2,1)
	f = (1,1)
	
	abilitylist = [a,b,c,d,e,f]
	Time = 0
	Time_Taken = []

	for i in abilitylist:
		A_Games = 0
		B_Games = 0
		while A_Games < 2 and B_Games < 2:
			finalscore = Englishscoringsystem(i[0], i[1])
			Time += (45*(finalscore[0]+finalscore[1]))
			if finalscore[0] > finalscore[1]:
				A_Games +=1
			else:
				B_Games +=1
		Time_Taken.append(Time/60)
		Time = 0
	return (Time_Taken)

def parstime():
	#I assume that each point takes 45 seconds and each match is best of 3 games
	a = (10,1)
	b = (8,1)
	c = (6,1)
	d = (4,1)
	e = (2,1)
	f = (1,1)

	abilitylist = [a,b,c,d,e,f]
	Time = 0
	Time_Taken = []

	for i in abilitylist:
		A_Games = 0
		B_Games = 0
		while A_Games < 2 and B_Games < 2:
			finalscore = game(i[0],i[1])
			Time += (45*(finalscore[0]+finalscore[1]))            
			if finalscore[0] > finalscore[1]:
				A_Games +=1
			else:
				B_Games +=1
		Time_Taken.append(Time/60)
		Time = 0
	return (Time_Taken)

def parsaverage():
	atimes=[]
	btimes=[]
	ctimes=[]
	dtimes=[]
	etimes=[]
	ftimes=[]

	for i in range(1,100):
		result=parstime()
		atimes.append(result[0])
		btimes.append(result[1])
		ctimes.append(result[2])
		dtimes.append(result[3])
		etimes.append(result[4])
		ftimes.append(result[5])
		#averages found
	aave=(sum(atimes))/len(atimes)
	bave=(sum(btimes))/len(btimes)
	cave=(sum(ctimes))/len(ctimes)
	dave=(sum(dtimes))/len(dtimes)
	eave=(sum(etimes))/len(etimes)
	fave=(sum(ftimes))/len(ftimes)
	averages = [aave,bave,cave,dave,eave,fave]
	return (averages)

def englishaverage():
	atimes=[]
	btimes=[]
	ctimes=[]
	dtimes=[]
	etimes=[]
	ftimes=[]
	for i in range(1,100):
		result=englishtime()
		atimes.append(result[0])
		btimes.append(result[1])
		ctimes.append(result[2])
		dtimes.append(result[3])
		etimes.append(result[4])
		ftimes.append(result[5])
	aave=(sum(atimes))/len(atimes)
	bave=(sum(btimes))/len(btimes)
	cave=(sum(ctimes))/len(ctimes)
	dave=(sum(dtimes))/len(dtimes)
	eave=(sum(etimes))/len(etimes)
	fave=(sum(ftimes))/len(ftimes)
	averages = [aave,bave,cave,dave,eave,fave]
	return (averages)
    
def timegraph():
	abilities = [10, 8, 6, 4, 2, 1]
	PARS_Time = parsaverage()
	English_Time = englishaverage()

	plt.plot(abilities, PARS_Time, "b-", label="PARS") 
	plt.plot(abilities, English_Time, "r-", label="English")
	plt.legend()
	plt.xlabel("Player A ability / Player B ability")
	plt.ylabel("Time taken for match (minutes)")
	plt.axis([1 , 10, 0, 60])
	plt.show()

       
       
   
#game(70,30)
#winProbability(70,30,100)
#englishscoring(70,30)
parstime()
englishtime()
timegraph()

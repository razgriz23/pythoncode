#Rob Niesen
#CS 419

import collections,math,sys
from pprint import pprint


data = (72, 61.0, 69.0, 74.0, 69.0, 68.0, 74.0, 68.0, 61.0, 61.0, 72, 65.0, 73.0, 63.0, 62.0, 64.0, 60, 64.0, 69.0, 62.0, 64.0, 62.0);
std = 3
datalistEStepA = []
datalistEStepB = []
mstepA = []
mstepB = []
k = []



def norm_density(datalist, sigma, mean1, mean2):  #E step calculation
	listmeanA = []
	listmeanB = []
	calcDenom = []
	for index in range(len(datalist)): #calculate the numerator for both sets
		listmeanA.append(math.exp((-1/(2*math.pow(sigma,2))) * math.pow((datalist[index] - mean1), 2)))
		listmeanB.append(math.exp((-1/(2*math.pow(sigma,2))) * math.pow((datalist[index] - mean2), 2)))
		calcDenom = listmeanA[index] + listmeanB[index] #calculate the denominator
		datalistEStepA.append(listmeanA[index] / calcDenom) #final results in a list
		datalistEStepB.append(listmeanB[index] / calcDenom)
	return datalistEStepA, datalistEStepB

def mStep(datalist): #M step calculation
	for index in range(len(datalistEStepA)):
		mstepA.append(datalistEStepA[index] * datalist[index])
		mstepB.append(datalistEStepB[index] * datalist[index])
	mstepAsum = sum(mstepA)
	mstepBsum = sum(mstepB)
	sumEstepA = math.fsum(datalistEStepA)
	sumEstepB = math.fsum(datalistEStepB)
	mStepACalc = mstepAsum / sumEstepA
	mStepBCalc = mstepBsum / sumEstepB

	global newmeanA, newmeanB
	newmeanA = mStepACalc
	newmeanB = mStepBCalc
	del datalistEStepA[:] #clear the list to start over with the new means
	del datalistEStepB[:]
	del mstepA[:]
	del mstepB[:]
	return newmeanA, newmeanB

	
def em(data, k, std): #calls our functions above to get our means that result from convergence
	meanA = data[0]
	meanB = data[1]
	norm_density(data, std, meanA, meanB)
	mStep(data)

	meanDiffA = newmeanA - meanA
	meanDiffB = newmeanB - meanB
	if (meanDiffA < 0):
		meanDiffA *= -1 #some results end up being negative. Need to ensure this doesn't happen
	x = 0

	while (meanDiffA > .0001): #keep calculating our sets with the new means until we find convergence
		norm_density(data, std, newmeanA, newmeanB)
		meanA = newmeanA
		meanB = newmeanB

		mStep(data)

		meanDiffA = newmeanA - meanA
		meanDiffB = newmeanB - meanB
	
		if (meanDiffA < 0):
			meanDiffA *= -1

		x += 1
	k = [meanA, meanB]
	pprint(k)
	print "Number of iterations: ", x

em(data, k, std)
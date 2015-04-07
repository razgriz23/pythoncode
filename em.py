#Rob Niesen
#CS 419

import collections,math,sys
from pprint import pprint

data = (72, 61.0, 69.0, 74.0, 69.0, 68.0, 74.0, 68.0, 61.0, 61.0, 72, 65.0, 73.0, 63.0, 62.0, 64.0, 60, 64.0, 69.0, 62.0, 64.0, 62.0)
newmeans = []




def norm_density(datalist, means, k, sigma):  #E step calculation
	denom = []
	calcDenom = []
	numerator = []
	a = 0
	x = 0
	z = 0
	while x < len(means):
		for index in range(len(datalist)): #calculate the numerator
			numerator.append(math.exp((-1/(2*math.pow(sigma,2))) * math.pow((datalist[index] - means[x]), 2)))
		x += 1
	while z < len(means):
		size = len(numerator)
		r = 0
		n = 0
		p = 0
		while r < len(numerator):
			a += numerator[r]
			z += 1
			r += len(datalist)
			p += 1
			if p == len(means):
				calcDenom.append(a)
				n += 1
				r = n
				a = 0
				p = 0
						
	#pprint(calcDenom)
	
	divided = []
	dividedsum = []
	dividedsums = []

	x = 0
	for index in range(len(numerator)):
		divided.append(numerator[index] / calcDenom[x])
		dividedsum.append(numerator[index] / calcDenom[x])
		x += 1
		if x == len(calcDenom):
			x = 0
			f = sum(dividedsum)
			del dividedsum[:]
			dividedsums.append(f)
			f = 0
	
	#pprint(divided)
	#pprint(dividedsums)

	multiplied = []
	multipliedsums = []
	multipliedsumsfornewmeans = []

	x = 0
	for index in range(len(divided)):
		multiplied.append(divided[index] * datalist[x])
		multipliedsums.append(divided[index] * datalist[x])
		x += 1
		if x == len(datalist):
			x = 0
			f = sum(multipliedsums)
			del multipliedsums[:]
			multipliedsumsfornewmeans.append(f)
			f = 0

	#pprint(multiplied)
	#pprint(multipliedsumsfornewmeans)

	for index in range(len(multipliedsumsfornewmeans)):
		newmeans.append(multipliedsumsfornewmeans[index] / dividedsums[index])

	pprint(newmeans)
	#pprint(datalistEStep)


	return newmeans



	
def em(data, k, std): #calls our functions above to get our means that result from convergence
	means = []
	for x in range(0,k):
		means.append(data[x])
		x += 1

	norm_density(data, means, k, std)

	newmean = 0
	meanDiff = newmean - newmeans[0]
	if meanDiff < 0:
		meanDiff = meanDiff * -1
		
	x = 0
	means = list(newmeans)
	del newmeans[:]
	while (meanDiff > .0001): #keep calculating our sets with the new means until we find convergence	
		norm_density(data, means, k, std)

		meanDiff = means[0] - newmeans[0]
		if meanDiff < 0:
			meanDiff = meanDiff * -1
		del means[:]
		means = list(newmeans)
		del newmeans[:]

		x += 1
	print means
	print "Number of iterations: ", x
	

em(data, 2, 3)
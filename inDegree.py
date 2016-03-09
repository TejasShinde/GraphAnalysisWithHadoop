#Visualize Hadoop output using this script

import csv
import numpy as np
import matplotlib.pyplot as plt

def visualize(output):
	with open(output, newline='') as tsvfile:
		filereader = csv.reader(tsvfile, delimiter='\t', quotechar='|')
		degreeDist = list()
		for row in filereader:
			degreeDist.append(int(row[1]))
	distrib = np.array(degreeDist)
	plt.hist(distrib, bins=100, histtype='stepfilled', log=True)
	plt.xlabel('In-degree value')
	plt.ylabel('Node frequency')
	plt.title('Incoming edge distribution')
	plt.show()

smallOutput = "../task1output1.tsv"
largeOutput = "../task1output2.tsv"
visualize(smallOutput)
visualize(largeOutput)
#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import csv

x = []
y = []
y1 = []

def main():
	i = 0
	with open('time.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			if i < 1000 :
				x.append(row[1])
				i+=1
			else :
				i = 0
				break
			
	with open('rho.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			if i < 1000 :
				y.append(row[1])
				i+=1
			else :
				i = 0
				break
	
	with open('stim.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			if i < 1000 :
				y1.append(row[1])
				i+=1
			else :
				i = 0
				break
	
	fig, ax1 = plt.subplots()
	ax1.plot(x, y, color = '#ff0000')
	ax2 = ax1.twinx()
	# TODO: Fix the scaling
	plt.plot(x, y1, color = '#0000cc')
	plt.show()
		
if __name__ == '__main__':
	main()

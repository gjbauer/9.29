#!/usr/bin/python3
import matplotlib.pyplot as plt
import sys
import csv

x = []
y = []
y1 = []

def main():
	with open('time.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			x.append(row[1])
			
	with open('rho.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			print(row[1])
			y.append(row[1])
	
	with open('stim.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
	
		for row in plots:
			print(row[1])
			y1.append(row[1])
	
	fig, ax1 = plt.subplots()
	ax1.plot(x, y)
	ax2 = ax1.twinx()
	plt.plot(x, y1)
	plt.show()
		
if __name__ == '__main__':
	main()

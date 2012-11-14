#!/usr/bin/env python

# Simple script to generate a LaTeX table sequence
# This script supports algorithms, but they have to be coded
#  into the script

def getResult(value):
	if (not isinstance(value, int)) | (not isinstance(value, float)):
		return None
	return 2*value 

class table:
	def __init__(rows):
		self.rows = rows
		self.firstRow = []
		
	def addValue(row, value):
		if (row < 0 ) | (row > self.rows):
			self.firstRow[row] = value
		else if (row == self.rows:
			self.firstRow.append(value)
			
	def fillTable():
		for( i in range(0, self.rows):
			

def main():
	
	
	
	return 0


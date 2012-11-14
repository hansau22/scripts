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
		self.secondRow = []
		self.firstRow = []
		
		self.start = "\\begin{tabular}"
		self.end = "\\end{tabular}"
		
	def addValue(row, value):
		if (row < 0 ) | (row > self.rows):
			self.firstRow[row] = value
		elif (row == self.rows):
			self.firstRow.append(value)
			self.rows += 1
			
	def fillTable():
		self.secondRow = []
		for i in range(0, self.rows):
			self.secondRow.append(getResult(self.firstRow[i]))
		
	def __exportTable(filepath):
		f = open(filepath, 'r')
		f.clear()
		
		f.write(start)
		
		formatString = "{"
		for i in range(0, self.rows):
			formatString.append("|c|")
		formatString.append("}")
		f.write(formatString)
		del formatString
		
		firstString = ""
		for i in range(0, self.rows):
			firstString.append(self.firstRow[i])
			firstString.append("&")
		firstString.append("\\\\")
		f.write(firstString)
		del firstString
		
		secondString = ""
		for i in range(0, self.rows):
			secondString.append(self.secondRow[i])
			secondString.append("&")
		secondString.append("\\\\")
		f.write(secondString)
		del secondString
		
		f.write(self.end)
		
				

def main():
	
	
	
	return 0


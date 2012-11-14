#!/usr/bin/env python

# Simple script to generate a LaTeX table sequence
# This script supports algorithms, but they have to be coded
#  into the script

def getResult(value):
#	if (not isinstance(value, int)) | (not isinstance(value, float)):
#		return None
	return 2*value 

class Table:
	def __init__(self):
		self.rows = 0
		self.secondRow = []
		self.firstRow = []
		self.secondTitle = ""
		self.firstTitle = ""
		
		self.start = "\\begin{tabular}"
		self.end = "\\end{tabular}"
		
	def addValue(self, row, value):
		if (row == self.rows):
			self.firstRow[row] = value
			return True
		elif (row < 0 ) | (row > self.rows):
			self.firstRow.append(value)
			self.rows += 1
			return True
		else:
			return False
			
	def fillTable(self):
		self.secondRow = []
		for i in range(0, self.rows):
			self.secondRow.append(getResult(self.firstRow[i]))
		self.__exportTable("table.tex")
			
	def addTitle(self, first, second):
		self.firstTitle = first
		self.secondTitle = second
		
	def __exportTable(self, filepath):
		f = open(filepath, 'w')
		f.write(self.start)
		
		formatString = "{|c "
		for i in range(0, self.rows):
			formatString += "|c"
		formatString += "|}"
		f.write(formatString)
		del formatString
		
		f.write("\hline ")
		
		firstString = self.firstTitle
		firstString += "&"
		for i in range(0, self.rows):
			firstString += str(self.firstRow[i])
			firstString += "&"
		firstString += "\\\\"
		f.write(firstString)
		del firstString
		
		f.write("\hline ")
		
		secondString = self.secondTitle
		secondString += "&"
		for i in range(0, self.rows):
			secondString += str(self.secondRow[i])
			secondString += "&"
		secondString +="\\\\"
		f.write(secondString)
		del secondString
		f.write("\hline")
		
		f.write(self.end)
		f.close()
				

def main():
	
	print("Simple script to generate a LaTeX table sequence")
	
	inputString = None
	table = Table()
	i = 0
	
	inputTitle1 = input("Namen Reihe 1 eingeben: ")
	inputTitle2 = input("Namen Reihe 2 eingeben: ")
	print("")
	print("Daten eingeben, mit \"end\" beenden.")
	print("")
	table.addTitle(inputTitle1, inputTitle2)
	del inputTitle1, inputTitle2
	
	while(inputString != "end"):
		inputString = input("Datensatz eingeben: ")
		if inputString != "end":
			i += 1
			if not table.addValue(i, inputString):
				print("Fehler, Invalide Zahl !")
				return 1
	
	table.fillTable()
	print("Die Tabelle wurde in table.text geschrieben.")
	return 0



if __name__ == "__main__":
	main()

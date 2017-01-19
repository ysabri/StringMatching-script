import csv
import py_stringmatching as sm

#Use the Levenshtien algorithim in py_stringmatching library
simWater = sm.Levenshtein()
#Table to read data from
with open('table.csv', 'rb') as file:
	scanner = csv.reader(file, delimiter=',', quotechar='|')
	#Table to output results to
	with open ('output.csv', 'wb') as table2:
		output = csv.writer(table2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		#The three types of scores: raw score, similarity score, gloden score (1 if matching, 0 otherwise)
		output.writerow(['raw_scr'] + ['sim_scr'] + ['golden_scr'])
		#The current column count
		colCount = 0
		#Global counter to be used in last for loop to write data into output file
		gc = 1
		#Each item holds a row's scores sperated by commas.
		rows = []
		#Get the two string columns to be compared later plus the golden score (1 if matching, 0 otherwise)
		for row in scanner:
			#Each item in scanner is a row in the read from table
			String1 = ""
			String2 = ""
			gScore = 0
			#Traverse colmns in each row to get the strings and gScore.
			for elem in row:
				#Change the numbers in each if clause based on the columns desired. Colmns are zero indexed.
				if(colCount==1):
					String1 = elem
					##print string1
					colCount = colCount + 1
				elif(colCount==4):
					String2 = elem
					##print string2
					colCount = colCount + 1
				elif(colCount==6):
					gScore = elem
					colCount=0
				else:
					colCount = colCount + 1
			##print simWater.get_raw_score(String1, String2)
			##print simWater.get_sim_score(String1, String2)
			#Compute the score and insert in array.
			rows.insert(gc, str(simWater.get_raw_score(String1, String2)) + ", " + str(simWater.get_sim_score(String1, String2)) + ", " + str(gScore))
			gc = gc + 1
		#Write scores to output file.
		for row in rows:
			x = str(row).split(", ")
			##print x
			output.writerow([x[0]] + [x[1]] + [x[2]])
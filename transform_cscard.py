# Notes, PrivacySuppressed needs to be transformed into NULL


import csv
import re

def extract_csv():
	with open('Most-Recent-Cohorts-All-Data-Elements.csv', 'r+') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		column_name = list()
		data_type = list()
		for val in spamreader.next():
			column_name.append(val)
	#zip needs to be delt with differently (as varchar(10))
	#NULL is numeric, so is PrivacySuppressed 

	f = open('schema_cscard.sql', 'w')
	f.truncate()
	f.write("CREATE TABLE college_scorecard ( \n")
	for i in xrange(len(column_name)):
		feature = "  %s %s,\n"%(column_name[i],data_type[i])
		f.write(feature)
	f.write("CONSTRAINT persons_pkey PRIMARY KEY (UNITID) )")
	f.close()



if __name__ == "__main__":
    extract_csv()








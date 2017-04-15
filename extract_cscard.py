import urllib
import csv
import re

def guess_data_type(value):
	pattern = re.compile("^\d*\.?\d*$")
	to_compare = unicode(value)
	if to_compare == unicode("PrivacySuppressed") or to_compare == unicode("NULL"):
		return "DECIMAL"
	elif re.match(pattern, to_compare):
		return "DECIMAL"
	return "VARCHAR(100)"

def extract_csv():
	testfile = urllib.URLopener()
	testfile.retrieve("https://ed-public-download.apps.cloud.gov/downloads/Most-Recent-Cohorts-All-Data-Elements.csv", "Most-Recent-Cohorts-All-Data-Elements.csv")

	with open('Most-Recent-Cohorts-All-Data-Elements.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		column_name = list()
		data_type = list()
		for val in spamreader.next():
			column_name.append(val)
	#zip needs to be delt with differently (as varchar(10))
	#NULL is numeric, so is PrivacySuppressed 
		i = 0
		for val in spamreader.next():
			# architecture built to be able to modify this stage as needed.
			# This is where we would add other features such as unique constraints, ect.
			if(column_name[i] == "ZIP"):
				data_type.append(unicode("varchat(10)"))
			else:
				data_type.append(guess_data_type(val))
			i+=1

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








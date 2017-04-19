# Notes, PrivacySuppressed needs to be transformed into NULL
import csv

csvfile = open("Most-Recent-Cohorts-All-Data-Elements.csv","rb")
csvout = open("Most-Recent-Cohorts-All-Data-Elements_transformed.csv","wb")

reader = csv.reader(csvfile)
writer = csv.writer(csvout)

def transform_csv():
	for row in reader:
	    for i in xrange(len(row)):
	    	if row[i] == "PrivacySuppressed":
	    		row[i] = "NULL"
	    	if i >= 1600:
	    		row[i] = ""
	    writer.writerow(row) 


if __name__ == "__main__":
    transform_csv()








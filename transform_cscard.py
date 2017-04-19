# Notes, PrivacySuppressed needs to be transformed into NULL
import csv

csvfile = open("Most-Recent-Cohorts-All-Data-Elements.csv","rb")
csvout = open("Most-Recent-Cohorts-All-Data-Elements_transformed.csv","wb")

reader = csv.reader(csvfile)
writer = csv.writer(csvout)

def transform_csv():
	count = 0
	for row in reader:
	    for i in xrange(len(row)):
	    	if row[i] == "PrivacySuppressed":
	    		row[i] = "NULL"
	    	count+=1
	    writer.writerow(row)
	while count >= 1600:
		with open(csvfile,"r") as fin:
		    with open(csvout,"w") as fout:
		        w = csv.writer(fout)
		        for row in csv.reader(fin):
		            w.writerow(row[:-1])
		count-=1


if __name__ == "__main__":
    transform_csv()





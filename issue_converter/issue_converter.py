#!/usr/bin/env python

### Input example
###  #,Tracker,Status,Priority,Subject,Assignee,Updated,Category,Due date,Project
###  9107,Bug,New,Normal (P3),Cannot rearrange tiles on customise dashboard tiles dialog,"",2013-11-19 11:41 am,"","",StarDesk - 2013

### Corresponding output
### Url,#,Tracker,Status,Priority,Subject,Assignee,Updated,Category,Due date,Project
### https://projects.syslab.com/issues/9107,Bug,New,normal,Cannot rearrange tiles on customise dashboard tiles dialog,"",2013-11-19 11:41 am,"","",StarDesk - 2013


import sys
import csv

SUPPORTERS = ('Wolfgang Thomas', 'Alexander Pilz', 'Lennart Regebro', 'Manuel Reinhardt', 'Jan-Carel Brand', 'Cillian de Roiste')
if (len(sys.argv) == 1):
    filename = 'issues.csv'
elif (len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    print 'Please give exactly one argument!'
    sys.exit(0)

newfilename = filename + '.out'

cnt = 0

with open(filename, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    with open(newfilename, 'wb') as newcsvfile:
        csvwriter = csv.writer(newcsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for line in csvreader:
            items = line
            if cnt == 0:
                url = "Url"
            else:
                url = 'https://projects.syslab.com/issues/' + items[0]

            newitems = [url] + items
            if (newitems[4] in ('Low (P4)', 'Very Low (P5)')):
                newitems[4]='-1'
            elif (newitems[4]=='Normal (P3)'):
                newitems[4]='0'
            elif (newitems[4] in ('High (P2)','Very High (P1)')):
                newitems[4]='1'
            else:
                newitems[4]=newitems[4]

            if cnt>0 and newitems[6].strip() and newitems[6] not in SUPPORTERS:
                print "User %s not found, dropping" % newitems[6]
                newitems[6] = ""

            # drop a few columns
            del newitems[11]  # position
            del newitems[7]  # Updated
            del newitems[3]  # Status
            del newitems[2]  # Tracker

            csvwriter.writerow(newitems)
            cnt += 1

print "Done. File converted. Output in %s" % newfilename




         

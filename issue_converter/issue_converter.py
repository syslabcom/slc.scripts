### Input
###  #,Tracker,Status,Priority,Subject,Assignee,Updated,Category,Due date,Project
###  9107,Bug,New,Normal (P3),Cannot rearrange tiles on customise dashboard tiles dialog,"",2013-11-19 11:41 am,"","",StarDesk - 2013

### Output
### Url,#,Tracker,Status,Priority,Subject,Assignee,Updated,Category,Due date,Project
### https://projects.syslab.com/issues/9107,Bug,New,normal,Cannot rearrange tiles on customise dashboard tiles dialog,"",2013-11-19 11:41 am,"","",StarDesk - 2013

# lies input filename, defaulte auf 'issues.csv'
# generiere output filename aus inputfilename+'.out'

import sys

if (len(sys.argv) == 1):
    filename = 'issues.csv'
elif (len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    print 'Please give exactly one argument!'
    sys.exit(0)

newfilename = filename + '.out'

try:
    lines = open(filename, 'r').readlines()
except IOError:
    print "There is no file named '" + filename + "' in this directory."
    sys.exit(0)
    
newfile = open(newfilename, 'w')
newlines = []

newline = lines[0]
newline = 'Url,' + newline
newlines.append(newline)

for line in lines[1:]:
    items = line.split(',')
    url = 'https://projects.syslab.com/issues/' + items[0]
    newitems = [url] + items
    if (newitems[4]=='Low (P4)'):
        newitems[4]='low'
    elif (newitems[4]=='Normal (P3)'):
        newitems[4]='normal'
    elif (newitems[4] in ('High (P2)','Very High (P1)')):
        newitems[4]='high'
    else:
        newitems[4]=newitems[4] + '<- Fehler beim parsen'
    newline=newitems[0]
    for i in range(len(newitems)-1):
        newline = newline + ',' + newitems[i+1]
    newlines.append(newline)

for line in newlines:
    newfile.write(line)

newfile.close()



         
#           # evtl namen umschreiben
#             # priority umschreiben
#               # Statt "Normal (P3)" schreib "normal"
#                 # Statt "Low (P4)" schreib "low"
#                   # Statt "High und very high (P1+2)" schreib "high"

#                     newitems = [url] + items
#                       newfile.write(','.join(newitems))

#                       newfile.close()
                      

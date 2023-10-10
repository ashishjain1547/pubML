import csv

file = "2.csv"
d={}
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for x,y in csvreader:
        if x in d.keys():
            d[x].append(y)
        else:
            d[x]=[y]
Support_count=3
confidence = 60

# Step-1:
#Create candidate set C1
C1={}
for x in d:
    for y in d[x]:
        if y in C1.keys():
            C1[y]+=1
        else:
            C1[y]=1
#compare candidate set C1 item’s support count with minimum support count and Create L1
L1={x:C1[x] for x in C1 if C1[x]>Support_count}


# Step-2:
#Create candidate set C2
C2={}
l=[x for x in L1]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        c=0
        for x in d:
            if l[i] in d[x] and l[j] in d[x]:
                c+=1
        C2[(l[i],l[j])]=c
#compare candidate set C2 item’s support count with minimum support count and Create L2
L2={x:C2[x] for x in C2 if C2[x]>Support_count}

# Step-3:
#Create candidate set C3
C3={}
l=[x for x in L2]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i][0]==l[j][0]:
            c=0
            for x in d:
                if l[i][0] in d[x] and l[i][1] in d[x] and l[j][1] in d[x]:
                    c+=1
            C3[(l[i][0],l[i][1],l[j][1])]=c
#compare candidate set C3 item’s support count with minimum support count and Create L3
L3={x:C3[x] for x in C3 if C3[x]>=Support_count}

# Step-4:
#Create candidate set C4
C4={}
l=[x for x in L3]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i][0]==l[j][0] and l[i][1]==l[j][1]:
            c=0
            for x in d:
                if l[i][0] in d[x] and l[i][1] in d[x] and l[i][2] in d[x] and l[j][2] in d[x]:
                    c+=1
            C4[(l[i][0],l[i][1],l[i][2],l[j][2])]=c
#compare candidate set C4 item’s support count with minimum support count and Create L4
L3={x:C3[x] for x in C3 if C3[x]>=Support_count}

#We stop here because no frequent itemsets are found further

# Association Rule
rule={}

l=[x for x in L2]
for i in range(len(l)):
    rule['{}->{}'.format(l[i][0],l[i][1])]=int((L2[l[i]]/L1[l[i][0]])*100)
    rule['{}->{}'.format(l[i][1],l[i][0])]=int((L2[l[i]]/L1[l[i][1]])*100)
l=[x for x in L3]
for i in range(len(l)):
    rule['{} -> {} {}'.format(l[i][0],l[i][1],l[i][2])]=int((L3[l[i]]/L1[l[i][0]])*100)
    rule['{} -> {} {}'.format(l[i][1],l[i][0],l[i][2])]=int((L3[l[i]]/L1[l[i][1]])*100)
    rule['{} -> {} {}'.format(l[i][2],l[i][0],l[i][1])]=int((L3[l[i]]/L1[l[i][2]])*100)
    rule['{} {}->{}'.format(l[i][0],l[i][1],l[i][2])]=int((L3[l[i]]/L2[(l[i][0],l[i][1])])*100)
    rule['{} {}->{}'.format(l[i][0],l[i][2],l[i][1])]=int((L3[l[i]]/L2[(l[i][0],l[i][2])])*100)

for x in rule:
    if rule[x]>confidence:
        print(x)
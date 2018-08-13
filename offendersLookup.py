import pyodbc


server = 'bwsql'
database = 'infobase'
username = 'infobase'
password = 'ib'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
#cursor.autocommit=True
#Queries in order of execution


findAll = "select * from dbo.Projects;"
 

 
# while row: 
#     print (row[13], row[14]) 
#     row = cursor.fetchone()
""" Get the bosses """     
def headOffenders(jobChosen):
    findJob = "select * from dbo.Projects where ProjectNo='"+str(jobChosen)+"';"
    cursor.execute(findJob)
    row = cursor.fetchone()
    while row:
        if row[13] == row[14]:
            return (row[13],) #the comma makes it a tuple, easier to deal with for consistency
        else:
            return (row[13], row[14])
""" Get the Staff """
def staffOffenders(jobChosen):
    findStaff = "select * from dbo.Project_Staff where ProjectNumber='"+str(jobChosen)+"';"
    cursor.execute(findStaff)
    row = cursor.fetchall()
    return [item for item,_ in row]
    # while row:
    #    return(row)

def nameSearcher(number):
    getNameStaff = "SELECT * FROM dbo.Staff where StaffID="+str(number)+";"
    cursor.execute(getNameStaff)
    row = cursor.fetchone()
    return row[1],row[3],row[9]

def namingNames(head,minions):
    contacts = open('mycontacts.txt','w')
    if (len(head) == 2):
        i = 0
        while i < len(head):
            res = nameSearcher(head[i])
            contacts.write(str(res)+'\n')
            i +=1
    else:
            print(head[0])
            res = nameSearcher(head[0])
            contacts.write(str(res)+'\n')
    
    for x in minions:
        res = nameSearcher(x)
        contacts.write(str(res)+'\n')



headHonchos = headOffenders('ad915')
print(headHonchos)
minions = staffOffenders('ad915')
print(minions)
namingNames(headHonchos,minions)


import pyodbc


server = 'bwsql'
database = 'infobase'
username = 'infobase'
password = 'ib'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
def dataMagic(jobChosen):
    jobChosen = jobChosen

    """ Get the bosses """     
    def headOffenders(jobChosen):
        findJob = "select * from dbo.Projects where ProjectNo='"+str(jobChosen)+"';"
        cursor.execute(findJob)
        row = cursor.fetchone()
        # while row:
        #     if row[13] == row[14]:
        #         return (row[13],) #the comma makes it a tuple, easier to deal with for consistency
        #     else:
        #         return (row[13], row[14])
        """ Only get Project Leaders as per Brett Request"""
        while row:
            return (row[14],)
    """ Get the Staff """
    def staffOffenders(jobChosen):
        findStaff = "select * from dbo.Project_Staff where ProjectNumber='"+str(jobChosen)+"';"
        cursor.execute(findStaff)
        row = cursor.fetchall()
        return [item for item,_ in row]
        # while row:
        #    return(row)

    def nameSearcher(number):
        #getNameStaff = "SELECT * FROM dbo.Staff where StaffID="+str(number)+"AND CurrentEmploy = 1;"
        #Cleaned out later as returning TypeError None is harder to deal with here. Check bottom of file
        getNameStaff = "SELECT * FROM dbo.Staff where StaffID="+str(number)+";"
        cursor.execute(getNameStaff)
        row = cursor.fetchone()
        return row[1],row[3],row[9],row[11]

    def namingNames(head,minions):
        contacts = []
        #oringally meant to check if both leader and director were same person, does nothing now. However in case I have left it there, head can not = 2. 
        if (len(head) == 2):
            i = 0
            while i < len(head):
                res = nameSearcher(head[i])
                contacts.append(res)
                i +=1
        else:
                #print(head[0])
                res = nameSearcher(head[0])
                contacts.append(res)

        for x in minions:
            res = nameSearcher(x)
            contacts.append(res)

        return(contacts)

    #Main Running
    leaders = headOffenders(jobChosen)
    staff = staffOffenders(jobChosen)
    contactList = namingNames(leaders,staff)
    #Remove staff member if not currently employed!
    contactListTrue = []
    for contact in contactList:
        if contact[3]:
            #print(contact)
            contactListTrue.append(contact)
    contactListTrue = set(contactListTrue) #Removes Duplicates
    #print(contactListTrue)
    
    return contactListTrue
    
   
    
    

   

#eh = dataMagic('16339')
#print(eh)
#for contact in eh:
#    print(contact)
#    firstName = contact[0]
#    lastName = contact[1]
#    email = contact[2]
#    print(firstName, lastName, email)


#print(test)
# leader = test[0]
# print('Leader:', leader)
# leaderName = leader[0]+' '+leader[1]
# print('Leader Name:', leaderName)
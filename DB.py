#Import the TinyDB module and submodules
from tinydb import TinyDB, Query
 

#Declare our database variable and the file to store our data in
def getConnection(str):
    db = TinyDB(str+'.json')
    return db



db=getConnection('Game')
#db=getConnection('myDB')
tb=db.table('User')
tbq=db.table('Questions')
tbp=db.table('Parent')



usr1 = {'ID':1,'Password':'1','Name': 'Avi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr2 = {'ID':2,'Password':'2','Name': 'Yossi','User':'Player', 'AerageOfWAs': 0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}
usr3 = {'ID':3,'Password':'3','Name': 'Natan','User':'Player', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':6}
usr4 = {'ID':4,'Password':'4','Name': 'Chen','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr5 = {'ID':5,'Password':'5','Name': 'Yaniv','User':'Manager', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':0}
usr6 = {'ID':6,'Password':'6','Name': 'Itay','User':'Parent', 'AerageOfWAs':0,'AerageOfSMs':0,'GamePlayed':0,'ParentID':4}



#Insert 4 reords into our todo list database

tbq.insert(Q1)
tbq.insert(Q2)
tbq.insert(Q3)
tbq.insert(Q4)
tbq.insert(Q5)

tb.insert(usr1)
tb.insert(usr2)
tb.insert(usr3)
tb.insert(usr4)
tb.insert(usr5)
tb.insert(usr6)

tbp.insert(p1)
tbp.insert(p2)

#db.insert(Item1)
#db.insert(Item2)
#db.insert(Item3)
#db.insert({'Status':'New','DueDate': '5/14/18', 'Category': 'Work','Description':'Request a Promotion'})
 
#print(tb.all())
#print(tbq.all())
#print(tbp.all())
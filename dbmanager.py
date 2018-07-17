#-----------------------------------------
#---------Members management--------------
#-----------------------------------------

def syncmembers(conn, members):
    conn.execute("DELETE FROM members")
    conn.commit()
    for i in members:
        conn.execute("INSERT INTO members (iduser) VALUES(\'" + i.id + "\')")
    conn.commit()

def adduser(conn, iduser):
    conn.execute("INSERT INTO members (iduser) VALUES(\'" + iduser + "\'")
    conn.commit()

def removeuser(conn, iduser):
    conn.execute("DELETE FROM members where iduser=\'" + iduser + "\'")
    conn.commit()

def memberlist(conn):
    return conn.execute("SELECT iduser FROM members") 

def showaccounts(conn):
    return conn.execute("SELECT iduser,balance FROM members") 

def getBalance(conn, iduser):
    return conn.execute("SELECT balance FROM members WHERE iduser=\'" + iduser + "\'").fetchone()[0]



#-----------------------------------------
#---------Quests management---------------
#-----------------------------------------

def getQuestId(conn,name):
    i = conn.execute("SELECT id FROM quests where name=\'" + name + "\'").fetchone()[0]
    return i


def createQ(conn, name, price, numberp):
    conn.execute("INSERT INTO quests (name, price, numberp) VALUES(\'" + name + "\'," + str(price) + "," + str(numberp) + ")")
    conn.commit()
    
def contribute(conn, quest, iduser, amount):
    questid = getQuestId(conn,quest)   
    conn.execute("INSERT INTO contribs (idquest, iduser, amount) VALUES (\'" + str(questid) + "\',\'" + iduser + "\'," + str(amount) +")")
    conn.commit()

def updateBalance(conn, iduser, idquest):    
    contrib = conn.execute("SELECT sum(amount) FROM contribs where idquest=" + str(idquest) + " AND iduser=\'" + iduser + "\'").fetchone()[0]
    if not(contrib):
        contrib = 0    
    prevBalance = conn.execute("SELECT balance FROM members where iduser=\'" + iduser + "\'").fetchone()[0]
    (price, np) = conn.execute("SELECT price, numberp FROM quests WHERE id=" + str(idquest)).fetchone()
    askedContrib = price//np
    newBalance = prevBalance + contrib - askedContrib
    conn.execute("UPDATE members SET balance=" + str(newBalance) + " WHERE iduser=\'" + iduser + "\'")
    conn.commit()

def endquest(conn, quest):
    members = memberlist(conn)
    for m in members:
        updateBalance(conn, m[0], getQuestId(conn,quest))
    conn.execute("DELETE FROM quests where name=\'" + quest + "\'")
    conn.commit()

def showquests(conn):
    res = []
    a = conn.execute("SELECT name, price, numberp FROM quests")
    for i in a:
        (name,price,nbp) = i        
        res.append("Name : " + str(name) + " | Price : " + str(price) + " | Contribution/p : " + str(price//nbp))
    return res



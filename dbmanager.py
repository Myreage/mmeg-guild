
def syncmembers(conn, members):
    conn.execute("DELETE FROM members")
    conn.commit()
    for i in members:
        conn.execute("INSERT INTO members (iduser) VALUES(\'" + i.id + "\')")
    conn.commit()

def memberlist(conn):
    return conn.execute("SELECT iduser FROM members") 

def createQ(conn, name, price, numberp):
    conn.execute("INSERT INTO quests (name, price, numberp) VALUES(\'" + name + "\'," + str(price) + "," + str(numberp) + ")")
    conn.commit()
    
def contribute(conn, quest, iduser, amount):
    questid = conn.execute("SELECT id FROM quests where name=\'" + quest + "\'")    
    conn.execute("INSERT INTO contribs (idquest, iduser, amount) VALUES (\'" + str(questid.fetchone()[0]) + "\',\'" + iduser + "\'," + str(amount) +")")
    conn.commit()

def nonpayes(conn, quest):
    np=[]
    questid = conn.execute("SELECT id FROM quests where name=\'" + quest + "\'").fetchone()[0]
    payes = conn.execute("SELECT iduser FROM contribs where idquest=" + str(questid))
    members = conn.execute("SELECT iduser FROM members")  
    lpayes = [p[0] for p in payes]
    lmembers = [m[0] for m in members]       
    return list(set(lmembers) - set(lpayes))

def delquest(conn, quest):
    conn.execute("DELETE FROM quests where name=\'" + quest + "\'")
    conn.commit()

def showquests(conn):
    res = []
    a = conn.execute("SELECT name, price, numberp FROM quests")
    for i in a:
        (name,price,nbp) = i        
        res.append("Name : " + str(name) + " | Price : " + str(price) + " | Contribution/p : " + str(price//nbp))
    return res



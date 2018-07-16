import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE members
         (iduser TEXT PRIMARY KEY);''')

conn.execute('''CREATE TABLE quests
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         price INTEGER NOT NULL,
         numberp INTEGER NO NULL);''')

conn.execute('''CREATE TABLE contribs
         (iduser TEXT PRIMARY KEY,
         idquest INTEGER NOT NULL,         
         amount INTEGER NOT NULL,
         
         CONSTRAINT fk_quests
         FOREIGN KEY (idquest)
         REFERENCES quests(id)
         ON DELETE CASCADE

         CONSTRAINT fk_member
         FOREIGN KEY (iduser)
         REFERENCES members(iduser)
         ON DELETE CASCADE
         );''')


conn.close()


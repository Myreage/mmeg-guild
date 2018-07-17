import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE members
         (iduser TEXT PRIMARY KEY,
          balance INTEGER DEFAULT 0);''')

conn.execute('''CREATE TABLE quests
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         price INTEGER NOT NULL,
         numberp INTEGER NO NULL);''')

conn.execute('''CREATE TABLE contribs
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         iduser TEXT NOT NULL,
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

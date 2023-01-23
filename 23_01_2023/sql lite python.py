import sqlite3 as sq #module pour gerer la base de donnee

#creation d'une base de donnees si elle n'existe pas
con= sq.connect(r'C:\Users\Lenovo\Documents\SM5\A&G\semestre 2\puf.sq3')
#Base de donnes contenir 4 tables : 
#U ('NU', NomU, Ville)
#P ('NP, NompP, Couleur, Poids)
#F ('NF',NomF, Statut, Ville)
#PUF ('NP','NU','NF',Quantité)

cursor= con.cursor()
cursor.execute("create table if not exists F(NF integer primary key, NomF text, Statut integer, Ville text)")
cursor.execute("create table if not exists P(NP integer primary key, NompP text, Couleur text, Pods integer)")
cursor.execute("create table if not exists U(NU integer primary key, NomU text, Ville text)")
cursor.execute("create table if not exists PUF(NP integer, NU integer, NF integer, Quantité integer, foreign key(NP) references P(NP), foreign key(NF) references F(NF), foreign key(NU) references U(NU), primary key(NP,NU,NF))")


"""
cursor.execute("insert into F values(1,'Smith' , 20 ,'Londres')")
cursor.execute("insert into F values(2,'Martin' , 10, 'Paris')")
cursor.execute("insert into F values(3,'Robert' , 30,'Paris')")
cursor.execute("insert into f values(4,'Clark' , 20, 'Londres')")
cursor.execute("insert into F values(5,'Dukas' , 30, 'Athènes')")

cursor.execute("insert into U values(1,'Citroen', 'Paris')")
cursor.execute("insert into U values(2,'Peugeot', 'Sochaux')")
cursor.execute("insert into U values(3,'Citroen', 'Lille')")
or

L = [(4,'Renault','Marseille'),(5,'Peugeot','Sochaux'),(6,'Opel','Paris')]
cursor.executemany("insert into u values(?,?,?)",L)
#Nombre de ? = nombres de columns


cursor.execute("insert into P values(1, 'Carosserie', 'Noir', 270)")
cursor.execute("insert into P values(2, 'Siège', 'Rouge', 1570)")
cursor.execute("insert into P values(3, 'Moteur', 'Noir', 5670)")

lpuf = [(1,1,1,60),(1,4,1,240),(3,1,2,50),(3,2,2,70),(3,3,2,200),(3,4,2,460),(3,5,2,120),(3,6,2,50)]
cursor.executemany('insert into PUF values(?,?,?,?)',lpuf)
"""

cursor.execute("select * from F")
print(cursor.fetchall())
cursor.execute("select * from P")
print(cursor.fetchall())
cursor.execute("select * from U")
print(cursor.fetchall())
cursor.execute("select * from PUF")
print(cursor.fetchall())


#enregistrer les modification dans la base de donnees
con.commit()
#fermer le curseur et la connexion la base
cursor.close()
con.close()


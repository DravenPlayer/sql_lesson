import sqlite3 as sq #module pour gerer la base de donnee
#creation d'une base de donnees si elle n'existe pas
con= sq.connect(r'C:\Users\Lenovo\Documents\sm5\A&G\sql_lesson-main\23_01_2023\puf.sq3')
#Base de donnes contenir 4 tables : 
#U ('NU', NomU, Ville)
#P ('NP, NompP, Couleur, Pods)
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
print('F')
print(*cursor.fetchall(),end='\n')
cursor.execute("select * from P")
print('P')
print(*cursor.fetchall())
cursor.execute("select * from U")
print('U')
print(*cursor.fetchall(),end='\n')
print('PUF')
cursor.execute("select * from PUF")
print(*cursor.fetchall(),end='\n')

#changer la ville du fournisseur 1 a geneve
#☺cursor.execute("update F set ville='Genève' where nf=1")
l = [(4,'Echappemet','Gris',127),(5,"Freinage","vert",58),(6,'Filtre','Blue',40)]
#cursor.executemany('insert into P values(?,?,?,?)',l)
#enregistrer les modification dans la base de donnees
cursor.execute('select nomu from U where lower(nomu) like "c%"')
cursor.execute('select np from P where nompp like "%s%" or nompp like "%S%"')
#cursor.execute('select np from P where lower(nompp) like "%s%"')
#cursor.execute('insert into P(np,pods) values(7,20)')
#donner le plus petit poids parmi les produits dont on connait la couleur
cursor.execute('select min(Pods) from P where couleur is not null')
cursor.execute('select nomf,count(*) from puf,f where puf.nf=f.nf group by nomf')
#l1= [(3,7,2,30),(5,2,2,1200),(3,1,3,70),(1,2,3,50),(6,3,4,30),(6,7,4,450),(2,2,5,1230),(2,4,5,40),(5,5,5,500),(5,7,5,300),(6,2,5,700),(1,4,5,600),(3,4,5,1200),(4,4,4,450),(5,4,3,320)]
cursor.execute('select couleur, avg(pods) from P group by couleur')

# cursor.executemany('insert into puf values(?,?,?,?)',l1)
cursor.execute('select couleur, avg(pods) m from P group by couleur having m>300 ')
print(*cursor.fetchall())
#fonction qui permet d'ajouter un fournisseur
def ajouter(cursor,l):
    cursor.execute('insert into f values(?,?,?,?)',l)
#ajouter(cursor,[45,'Sami',25,'Tunis'])
def delete_f_numero(cursor, numero):
    cursor.execute('delete from f where nf =?',numero)
def delete_f_nom(cursor, nom):
    cursor.execute('delete from f where nomf="'+nom+'"')
#delete_f_nom(cursor,'Sami')
con.commit()
#fermer le curseur et la connexion la base
cursor.close()
con.close()


import sqlite3 as sq
def creer_table_vaccination(cur):
    cur.execute('Create table Vaccination(IdCitoyen text,IdVaccin text, NumDose text, DateVaccin text, centre text,primary key(IdCitoyen, IdVaccin , NumDose) foreign key(IdCitoyen) references Citoyen(IdCitoyen), foreign key(IdVaccin) references Vaccin(IdVaccin))')

con = sq.connect(r'C:\Users\Lenovo\Documents\sm5\A&G\sql_lesson-main\06_02_2023\Vaccination.sqlite')
cur = con.cursor()
#cur.execute('create table citoyen(IdCitoyen text primary key, nom text, prenom text, DateNaissance text, ville text)')
#cur.execute('create table vaccin(idvaccin text primary key, designation text, laboratoire text, nbdoses integer, disponible boolean)')
#creer_table_vaccination(cur)
#cur.execute('create table maladie(idmaladie text primary key ,description text, compatible boolean)')
#cur.execute('insert into maladie values(?,?,?)',['1','Covid',True])
#cur.execute('create table etatcitoyen(idcitoyen text references Citoyen, idmaladie text references maladie, dateaff text, primary key(idcitoyen, idmaladie))')

#cur.execute('select compatible from maladie')
print(cur.fetchall()) 
def inserer_citoyens(cur, L) : 
    cur.executemany('insert into citoyen values(?,?,?,?,?)',L)
def supprimer_citoyens(cur,id):
    cur.execute('delete from citoyen where idCitoyen = "{}"'.format(id))
    cur.execute('delete from vaccination where idCitoyen = "{}"'.format(id))
    cur.execute('delete from etatcitoyen where idCitoyen = "{}"'.format(id))
#inserer_citoyens(cur,[('1','Osse','Adam','2003','Lol')])
#cur.execute('update citoyen set ville = "Tunis" where idcitoyen = "1"')
#supprimer_citoyens(cur, '2')
def verifier_compatibilite(cur,id):
    cur.select('select compatible from maladie where') 

cur.execute('select * from citoyen')

print(cur.fetchall())
con.commit()

con.close()

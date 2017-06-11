# Ovaj skript se koristi za testiranje CouchDB baze podataka.
# Vraca vrednosti koje su ubacene pomocu modula randPersons.py

import sys;
import couchdb;

konekcija = couchdb.Server(); 
db = konekcija['testiranje']; 

# Definicije map funkcija.
# JavaScript funkcije u obliku Python stringova.
mapJedan = '''function(dokument) {
if(dokument.zarada > 50000 && dokument.zarada < 90000)
   emit(dokument._id, dokument);
}'''

mapDva = '''function(dokument) {
if(dokument.zarada > 50000 && dokument.zarada < 90000
      && dokument.starost > 25)
   emit(dokument._id, dokument);
}'''

mapTri = '''function(dokument) {
if(dokument.zarada > 50000 && dokument.zarada < 90000
      && dokument.starost > 25
      && dokument.porodica)
   emit(dokument._id, dokument);
}'''

mapCetiri = '''function(dokument) {
if(dokument.zarada > 50000 && dokument.zarada < 90000
      && dokument.starost > 25
      && dokument.southpark)
{
      var pronadjen = false;

      for(var i = 0; i < dokument.southpark.length; i++)
      {
         if(dokument.southpark[i] == 'Randy')
            pronadjen = true;
      }

      if(pronadjen)
         emit(dokument._id, dokument);
}
}'''

mapPet = '''function(dokument) {
if(dokument.zarada > 50000
      && dokument.zarada < 90000
      && dokument.starost > 25
      && dokument.ljubimac)
{
      var pronadjen = false;

      for(var i = 0; i < dokument.ljubimac.length; i++)
      {
          if(dokument.ljubimac[i] == 'Pingvin' || dokument.ljubimac[i] == 'Zmaj')
             pronadjen = true;
      }

      if(pronadjen)
         emit(dokument._id, dokument)};
}'''


mapSest = “””function(dokument) { 
emit (document.porodica,1); 
}“””

reduceSest = “””function(keys, values) {
return sum(values);
}“””

redovi = 0
if len(sys.argv) != 2:
	print "Izaberite broj test upita (0-6).";
elif len(sys.argv) == 2:
	opcija = sys.argv[1];
	if opcija == '1':
		redovi = db.query(mapJedan);
	if opcija == '2':
		redovi = db.query(mapDva);
	if opcija == '3':
		redovi = db.query(mapTri);
	if opcija == '4':
		redovi = db.query(mapCetiri);
	if opcija == '5':
		redovi = db.query(mapPet);
	if opcija == '6':
		redovi = db.query(mapSest, reduceSest, group = True);


# Ispisuje se broj dokumenata
print len(redovi)

# Prolazak kroz sve redove u rezultujucem pogledu
for red in redovi:
	pass;

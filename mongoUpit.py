
# Ovaj skript se koristi za testiranje MongoDB baze podataka.
# Vraca vrednosti koje su ubacene pomocu modula randPersons.py

import sys;
from pymongo import Connection;
from bson.code import Code;


konekcija = Connection();
db = konekcija.testiranje;
kolekcija = db.osobe;

if len(sys.argv) != 2:
	print "Izaberite broj test upita (0-6).";
elif len(sys.argv) == 2:
	opcija = sys.argv[1];
	if opcija == '1':
		kursor = kolekcija.find({"zarada":{"$gt":50000, "$lt":90000}});
	elif opcija == '2':
		kursor = kolekcija.find({"zarada ":{"$gt":50000, "$lt":90000},
		  "starost":{"$gt":25}})
	elif opcija == '3':
		kursor = kolekcija.find({"zarada":{"$gt":50000, "$lt":90000},
		  "starost":{"$gt":25},
		  "porodica":{"$exists":True}});
	elif opcija == '4':
		kursor = kolekcija.find({"zarada":{"$gt":50000, "$lt":90000},
		  "starost":{"$gt":25},
		  "southpark":{"$exists":True},
		  "southpark":"Randy"});
	elif opcija == '5':
		kursor = kolekcija.find({"zarada":{"$gt":50000, "$lt":90000},
		  "starost":{"$gt":25},
		  "ljubimac":{"$exists":True},
		  "$or":[{"ljubimac":"Pingvin"},
		{"ljubimac":"Zmaj"}]});
	elif opcija == '6':
		mapper = Code( “””
			function() { 
				this.porodica.forEach(function(k) {
				emit (k,1);
				});
				}
			“””);
		reducer = Code( “””
			function(key, values) {
				var total = 0;
				for (var i = 0; i < values.length; i++) {
				total += values[i];
				}
				return total;
				}
				“””);
		kursor = kolekcija.map_reduce(mapper,reducer,”myresults”);


# Ispisuje se broj dokumenata
print kursor.count();

# Prolazak kroz sve rezultate
for osoba in kursor:
	pass;

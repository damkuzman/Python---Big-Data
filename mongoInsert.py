
# Ovaj skript generise odredjeni broj osoba.
# Broj osoba se upisuje na komandnoj liniji.
# Ako se prosledi parametar "drop", kolekcija se odbacuje.
import sys;
from pymongo import Connection;
from randOsobe import flatOsoba;
from randOsobe import dodatnoOsoba;

if len(sys.argv) == 2 or len(sys.argv) == 3:
	konekcija = Connection(); 
	db = konekcija.testiranje; #testiranje je naziv baze podataka
	kolekcija = db.osobe; #osobe je naziv kolekcije
	if sys.argv[1] == 'drop':
		print "Kolekcija se odbacuje.";
		db.drop_collection(kolekcija);
	else:
		if len(sys.argv) == 3 and sys.argv[2] == 'dodatno':
			dodatno = True;
		else:
			dodatno = False;
		brojOsoba = sys.argv[1];
		print "Ubacivanje", brojOsoba, "dokumenata. Sacekajte…";
		if dodatno:
			brojac = 1;
			for i in range(int(brojOsoba)):
				kolekcija.insert(dodatnoOsoba());
				print (float(brojac)/float(brojOsoba))*100,"\b%\r",;
				brojac = brojac + 1;
		else:
			brojac = 1;
			for i in range(int(brojOsoba)):
				kolekcija.insert(flatOsoba());
				print (float(brojac)/float(brojOsoba))*100,"\b%\r",;
				brojac = brojac + 1;
else:
	print "Prosledite broj osoba koje zelite da ubacite u formatu", sys.argv[0], "[BROJ OSOBA] [MOD]";
	print "Takodje mozete odbaciti kolekciju 'osoba' komandom", sys.argv[0], "drop";

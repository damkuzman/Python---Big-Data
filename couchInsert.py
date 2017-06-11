# Ovaj skript generise odredjeni broj osoba.
# Broj osoba se upisuje na komandnoj liniji.
# Ako se prosledi parametar "drop", kolekcija se odbacuje.
import sys;
import couchdb;
from randOsobe import flatOsoba;
from randOsobe import dodatnoOsoba;

if len(sys.argv) == 2 or len(sys.argv) == 3:
	konekcija = couchdb.Server(); 
	db = konekcija['testiranje']; 
	if sys.argv[1] == "drop":
		print "Baza se odbacuje.";
		konekcija.delete('testiranje');
		print "Baza se ponovo kreira.";
		konekcija.create('testiranje');
	else:
		if len(sys.argv) == 3 and sys.argv[2] == 'dodatno':
			dodatno = True;
		else:
			dodatno = False;
		brojOsoba = sys.argv[1];
		print "Ubacivanje", brojOsoba, "dokumenata. Sacekajte...";
		if dodatno:
			brojac = 1;
			for i in range(int(brojOsoba)):
				db.create(dodatnoOsoba());
				print "\t\r",; 
				print (float(brojac)/float(brojOsoba))*100,"\b\r%",;
				brojac = brojac + 1;
		else:
			brojac = 1;
			for i in range(int(brojOsoba)):
				db.create(flatOsoba());
				print "\t\r",; 
				print (float(brojac)/float(brojOsoba))*100,"\b%\r",;
				brojac = brojac + 1;
else:
	print "Prosledite broj osoba koje zelite da ubacite u formatu", sys.argv[0], "[BROJ OSOBA]";
	print "Takodje mozete odbaciti bazu komandom", sys.argv[0], "drop";
import random;
from collections import defaultdict;
# Konstante
SEED = 3509;
SLOVA = 'abcdefghijklmnopqrstuvwxyz';
BROJEVI = '0123456789';
LJUBIMCI = ["Pas","Iguana","Tarantula","Pingvin","Jednorog","Zmaj","R2D2"];
PORODICE = ['Lannister','Stark','Targaryen','Baratheon','Greyjoy','Martell'];
SOUTH_PARK = ['Cartman','Kenny','Stan','Kyle','Randy','Butters','Tweak'];
MIN_DUZINA_IME = 5;
MAX_DUZINA_IME = 15;
MIN_ZARADA = 20000;
MAX_ZARADA = 150000;
MIN_GODINE = 18;
MAX_GODINE = 90;
MIN_ELEMENATA = 1;
MAX_ELEMENATA = 5;
# Verzije skupa podataka
DEFAULT = 0;
IMA_LJUBIMCA = 1;
SOUTH_PARK = 2;
SLAVNA_PORODICA = 3;

random.seed(SEED);

def randomIme():
	imeNiz=random.sample(SLOVA,random.randint(MIN_DUZINA_IME,MAX_DUZINA_IME));
	ime = '';
	for c in imeNiz:
	ime += c;
	return ime;

def randomLjubimac():
	return LJUBIMCI[random.randint(0,len(LJUBIMCI)-1)];

def randomPorodica():
	return PORODICE[random.randint(0,len(PORODICE)-1)];

def randomSouthPark():
	return SOUTH_PARK[random.randint(0,len(SOUTH_PARK)-1)];

def randomZarada():
	return random.randint(MIN_ZARADA, MAX_ZARADA);

def randomStarost():
	return random.randint(MIN_GODINE, MAX_GODINE);

def randomTelefon():
	telefonNiz = random.sample(BROJEVI,10);
	telefon = '';
	for i in telefonNiz:
		telefon += i;
	return telefon;

# Ova funkcija generise dokumente.
# U zavisnosti od vrednosti parametra verzija novi kljuc/vrednost parovi se dodaju dokumentu.
def randomDokument(verzija, dodatno):
	osoba = 
	{"ime":randomIme(),
	"zarada": randomZarada(),
	"starost": randomStarost(),
	"telefon": randomTelefon()};
	if verzija == IMA_LJUBIMCA:
		if dodatno:
			brojLjubimaca=random.randint(MIN_ELEMENATA, MAX_ELEMENATA);
			ljubimci = [];
			for i in range(brojLjubimaca):
				ljubimci.append(randomLjubimac());
			osoba['ljubimac'] = ljubimci;
		else:
			osoba['ljubimac'] = randomLjubimac();
	elif verzija == SOUTH_PARK:
		if dodatno:
			brojLikova = random.randint(MIN_ELEMENATA, MAX_ELEMENATA);
			likovi = [];
			for i in range(brojLikova):
				likovi.append(randomSouthPark());
			osoba['southpark'] = likovi;
		else:
			osoba ['southpark'] = randomSouthPark();
	elif verzija == SLAVNA_PORODICA:
		osoba ['porodica'] = randomPorodica();
	return osoba;

def flatOsoba():
	return randomDokument(random.randint(0,3), False);

def dodatnoOsoba():
	return randomDokument(random.randint(0,3), True);

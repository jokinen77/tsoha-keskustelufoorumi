# Lokaali asennusohje Linux/macOS

Asennusohjeet ja sovellus on testattu käyttäen macOS Mojavea, Python 3.7.0 ja SQLite 3.24.0.

1. Lataa repositio koneellesi.
```{bash}
git clone https://github.com/jokinen77/tsoha-keskustelufoorumi
cd tsoha-keskustelufoorumi
```

2. Luo virtuaaliympäristo esimerkiksi käyttäen venv:iä, anna suoritusoikeus, aktivoi se ja asenna riippuvuudet.
```{bash}
python3 -m venv ./venv
chmod +x ./venv/bin/activate
source ./venv/bin/activate
pip install -r requirements.txt 
```

3. Käynnistä palvelinohjelmisto käyttäen Gunicornia.
```{bash}
gunicorn --preload --workers 1 application:app
```

4. Avaa tietokanta esimerkiksi SQLitellä. Voit avata uuden terminaalin reposition juurihakemistoon tai sammuttaa palvelinohjelmiston hetkeksi painamalla CTRL+c, jotta pääset käsiksi tietokantaan.
```{bash}
sqlite3 application/forum.db
```

5. Suorita tietokannan alustuskomennot tietokannassa. Käyttäjää luodessa (viimeinen komento) korvaa "\<jotain\>" kohdat haluamisilla arvoilla.
```{bash}
INSERT INTO usertype(id,name,value) VALUES(1,'Developer',100.0);
INSERT INTO usertype(id,name,value) VALUES(2,'Admin',50.0);
INSERT INTO usertype(id,name,value) VALUES(3,'Normal',30.0);
INSERT INTO account(username,name,email,password,usertype_id) VALUES('<username>','<name>','<email>','<password>',1);
```

6. Kirjaudu sovellukseen. Kun käynnistät sovelluksen kohdan 3 mukaisesti, niin käynnistyksen yhteydessä terminaaliin pitäisi tulostua palvelimen osoite esimerkiksi "Listening at: http://127.0.0.1:8000". Voit nyt siis käyttää sovellusta kyseisestä osoitteesta luomillasi tunnuksilla. Voit muuttaa sovelluksen osoitetta lisäämällä gunicornin käynnistyskomentoon [bind](http://docs.gunicorn.org/en/stable/settings.html#bind) argumentin.

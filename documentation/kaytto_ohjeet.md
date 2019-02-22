# Käyttöohjeet

## Peruskäsitteitä

### Käyttäjätyypit

Sovelluksessa toiminnallisuudet toimivat hierarkisen mallin mukaan. Käyttäjän hierarkia luokan kertoo käyttäjätyypin arvo (0-100). Korkemmalla käyttäjätyypin tasolla olevalla käyttäjällä on kaikki samat oikeudet kuin alemman luokan käyttäjällä. Käyttäjätyyppejä on tavallisesti kolme, mutta halutessaan niitä voi tehdä miten paljon tahansa ja vertailu tapahtuun tyypin arvolla.

1. (100) **Kehittäjä/ylläpitäjä** Heillä on oikeus luoda käyttäjäryhmiä, käyttäjiä ja käyttäjätyyppejä. Heillä on lisäksi oikeudet poistaa yksittäisiä viestejä ja käyttäjiä. He voivat lisätä kenet tahansa mihinkä käyttäjäryhmään tahansa.

2. (50) **Admin** Heillä on oikeus luoda käyttäjiä (korkeintaan toisia admineja) ja lisätä heidät omiin käyttäjäryhmiinsä.

3. (30) **Normaali** Heillä on oikeus luoda keskustelu alueita omille käyttäjärymillensä ja kirjoittaa niihin viestejä. Heillä on oikeus muokata omia tietojaan.

### Käyttäjäryhmät

Käyttäjäryhmien tarkoituksena on rajata sovelluksen toimintojen (tässä tapauksessa foorumien) käyttöä. Tällöin toimintoja voidaan antaa vain näitä toimintoja tarvitseville/tilaaville käyttäjille. Tässä sovelluksessa käyttäjillä on mahdollisuus perustaa foorumeja jonkin käyttäjäryhmän sisälle, johon hän itsekin kuuluu. Käyttäjä myös näkee vain omiin käyttäjäryhmiinsä liitetyt foorumit.

### Foorumi

Foorumit liittyvät aina johonkin käyttäjäryhmään paitsi ne, jotka ovat kaikille (rekisteröityneille) käyttäjille avoimet. Käyttäjä voi katsoa tai lähettää viestejä foorumiin, jos käyttäjällä kuuluu foorumiin liitettyyn käyttäjäryhmään.

## Perustoiminnallisuudet

* Käyttäjä voi käyttää foorumeja, joihin hänellä on oikeus.

* Käyttäjä voi filteröidä foorumeita niiden nimien perusteella ja halutessaan voi etsiä vain niitä foorumeita, johon on laittanut ainakin yhden viestin.

* Käyttäjä voi muokata omia tietojaan hallintasivulta.

* Käyttäjät näkevät toisten käyttäjien tiedot ja voivat tarvittaessa hakea käyttäjiä käyttäjänimen, oikean nimen tai sähköpostin perusteella käyttäjänäkymässä.

## Käyttö esimerkkejä

1. **Käyttäjä haluaa aloittaa palvelun käytön.** Hän rekisteröityy palveluun sisäänkirjautumis sivulta löytyvän linkin kautta. Uudet rekisteröityneet käyttäjät ovat käyttäjätyypiltään normaaleja käyttäjiä, joten he voivat käyttää vain kaikille käyttäjille avoimia foorumeita tai muuttaa omia tietojaan. Admin (tai sitä korkeammat) käyttäjät voivat lisätä käyttäjän käyttäjäryhmiin mihin heilläkin on oikeus (poikkeuksena ylläpitäjä voi lisätä kenet tahansa mihinkä ryhmään tahansa).

2. **Organisaatio tarvitsee oman käyttäjäryhmän.** Ylläpitäjä luo uuden käyttäjäryhmän ja organisaation jollekin henkilölle admin käyttäjätilin ja lisää kyseisen admin tilin uuteen käyttäjäryhmään. Nyt tämä admin käyttäjä voi lisätä tarvittavat henkilöt kyseiseen ryhmään.

3. **Käyttäjä haluaa avata keskustelu alueen.** Käyttäjä painaa uuden alueen luomis nappia forum-sivulta ja määrittelee uudelle keskustelualueelle nimen ja käyttäjäryhmän, josta muut käyttäjät pääsevät ja näkevät keskustelualueen.

4. **Käyttäjä haluaa etsiä jonkin keskustelualueen.** Käyttäjä filtteröi forum-sivulta keskustelualueet hakusanalla.

# Käyttöohjeet

## Käyttäjätyypit

Sovelluksessa toiminnallisuudet toimivat hierarkisen mallin mukaan. Käyttäjän hierarkia luokan kertoo käyttäjätyypin arvo (0-100). Korkemmalla käyttäjätyypin tasolla olevalla käyttäjällä on kaikki samat oikeudet kuin alemman luokan käyttäjällä. Käyttäjätyyppejä on tavallisesti kolme, mutta halutessaan niitä voi tehdä miten paljon tahansa ja vertailu tapahtuun tyypin arvolla.

1. (100) **Kehittäjillä/ylläpitäjillä** Heillä on oikeus luoda/poistaa käyttäjäryhmiä, käyttäjiä ja käyttäjätyyppejä. Heillä on lisäksi oikeudet poistaa yksittäisiä viestejä ja lisätä kenet tahansa mihinkä käyttäjäryhmään tahansa.

2. (50) **Admin** Heillä on oikeus luoda käyttäjiä (korkeintaan toisia admineja) ja lisätä heidät omiin käyttäjäryhmiinsä.

3. (30) **Normaali** Heillä on oikeus luoda keskustelu alueita omille käyttäjärymillensä ja kirjoittaa niihin viestejä. Heillä on oikeus muokata omaa sähköpostiosoitetta ja salasanaa.

## Käyttäjäryhmät

Käyttäjäryhmien tarkoituksena on rajata sovelluksen toimintojen (tässä tapauksessa foorumien) käyttöä. Tällöin toimintoja voidaan antaa vain näitä toimintoja tarvitseville/tilaaville käyttäjille. Tässä sovelluksessa käyttäjä joukoilla on mahdollisuus perustaa "omia alueita" oman käyttäjäryhmänsä sisällä.

## Käyttö esimerkkejä

1. **Käyttäjä haluaa aloittaa palvelun käytön.** Hän rekisteröityy palveluun sisäänkirjautumis sivulta löytyvän linkin kautta. Uudet rekisteröityneet käyttäjät ovat käyttäjätyypiltään normaaleja käyttäjiä, joten he voivat käyttää vain kaikille käyttäjille avoimia foorumeita tai muuttaa omia tietojaan. Admin (tai sitä korkeammat) käyttäjät voivat lisätä käyttäjän käyttäjäryhmiin mihin heilläkin on oikeus (poikkeuksena ylläpitäjä voi lisätä kenet tahansa mihinkä ryhmään tahansa).

2. **Organisaatio tarvitsee oman käyttäjäryhmän.** Ylläpitäjä luo uuden käyttäjäryhmän ja organisaation jollekin henkilölle admin käyttäjätilin ja lisää kyseisen admin tilin uuteen äjäryhmään. Nyt tämä admin käyttäjä voi lisätä tarvittavat henkilöt kyseiseen ryhmään.

3. **Käyttäjä haluaa avata keskustelu alueen.** Käyttäjä painaa uuden alueen luomis nappia forum-sivulta ja määrittelee uudelle keskustelualueelle nimen ja käyttäjäryhmän, josta muut käyttäjät pääsevät ja näkevät keskustelualueen.

4. **Käyttäjä haluaa etsiä jonkin keskustelualueen.** Käyttäjä filtteröi forum-sivulta keskustelualueet hakusanalla.

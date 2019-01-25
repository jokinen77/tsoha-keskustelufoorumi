# Käyttöohjeet

## Käyttäjätyypit

Sovelluksessa toiminnallisuudet toimivat hierarkisen mallin mukaan. Käyttäjän hierarkia luokan kertoo käyttäjätyypin arvo (0-100). Korkemmalla käyttäjätyypin tasolla olevalla käyttäjällä on kaikki samat oikeudet kuin alemman luokan käyttäjällä. Käyttäjätyyppejä on tavallisesti kolme, mutta halutessaan niitä voi tehdä miten paljon tahansa ja vertailu tapahtuun tyypin arvolla.

1. (100) **Kehittäjillä/ylläpitäjillä** Heillä on oikeus luoda/poistaa käyttäjäryhmiä, käyttäjiä ja käyttäjätyyppejä. Heillä on lisäksi oikeudet poistaa yksittäisiä viestejä ja lisätä kenet tahansa mihinkä käyttäjäryhmään tahansa.

2. (50) **Admin** Heillä on oikeus luoda käyttäjiä (korkeintaan toisia admineja) ja lisätä heidät omiin käyttäjäryhmiinsä.

3. (30) **Normaali** Heillä on oikeus luoda keskustelu alueita omille käyttäjärymillensä ja kirjoittaa niihin viestejä. Heillä on oikeus muokata omaa sähköpostiosoitetta ja salasanaa.

## Käyttö esimerkkejä

1. **Uusi organisaatio haluaa aloittaa palvelun käytön.** He ottavat yhteyttä palvelun ylläpitäjiin ja kertovat että ovat kiinnostuneita palvelusta. Organisaatio antaa heiltä yhden tulevan admin henkilön tiedot ja listan tarvitsemistaan eri käyttäjäryhmistä. Ylläpitäjät luovat tarvittavat käyttäjäryhmät ja organisaatiolle admin käyttäjätilin kyseiselle henkilölle kyseisillä käyttäjäryhmillä. Organisaation admin käyttäjä voi ruveta luomaan muille jäsenilleen tarvittavia tilejä tarvittaviin ryhmiin. Organisaatio voi aloittaa palvelun käytön.

2. **Organisaatio tarvitsee uuden käyttäjäryhmän käyttöönsä.** He ottavat yhteyden ylläpitoon ja kertovat tarpeensa. Ylläpitäjät luovat tarvittavat käyttäjäryhmät ja lisäävät organisaation admin tilin näihin ryhmiin. Organisaation admin voi ruveta lisäilemään henkilöitä näille listoille.

3. **Käyttäjä haluaa avata keskustelu alueen.** Käyttäjä painaa uuden alueen luomis nappia pääsivulta. Käyttäjä määrittää keskustelu alueelle nimen ja jonkin käyttäjäryhmän omista ryhmistään, sitten hän tallentaa uuden alueen. Uusi alue löytyy nyt pääsivulta.

4. **Käyttäjä haluaa etsiä keskustelu alueita, johon on laittanut ainakin yhden viestin tai luonut.** Käyttäjä filtteröi pääsivulta nämä keskustelu alueet valitsemalla kyseisen checkboxin ja painaa päivitys-nappia.

#Luentoviikko 3, 13.2.-19.2.2017
Luennolla demottiin flaskia, tosin hyvin lyhyesti. Vastaavan demon sai jalkeille itsekin parissa minuutissa. Aikaisempi anaconda-asennuskin oli näemma jo valmiiksi asentanut Flaskin. Pythoninia nyt viime aikoina paljonkin käsitelleenä vaikutti ihan mukavalta ja helposti lähestyttävältä. Demon ja oman pienen leikkimisen jälkeen jäi kuitenkin vielä hieman hämäräksi, millainen tuki varsinaiseen front-kehitykseen ja nettisivun visualisointiin.

Tarina kilpailevista kehyksistä toi tietysti mieleen <a href=https://xkcd.com/927/>xkcd:n stripin standardeista</a>.<img src="https://imgs.xkcd.com/comics/standards.png" />

Kehyksien detaljeja enemmän pääpaino oli yleisissä ominaisuuksissa. Monethan kuulosti hyvin perusasioilta. Joukossa on myös paljon asioita, jotka tietää tärkeäksi, mutta jotka tulee yleensä aina skipattua, koska toistaiseksi tekee lähinnä pieniä demoja tai harjoitustöitä. Omaan flaskilla tehtyyn Hello world-demoon tulee harvemmin upotettua vielä lokalisointia tai monimutkaista pääsynhallintaa. Ihan oikeaa palvelua olisi kuitenkin vaikea kuvitellakaan toteuttavansa miettimättä näitäkin asioita.

Toimenpiteiden luokittelemeninen safe/unsafe-jaolla pisti mietityttämään: aika moni perinteinen get-nykyään jossain määrin muutta sovelluksen tilaa. Joillain sivustoilla on rajoitettu lukemista, Twitter esimerkiksi säätelee kuinka paljon hakuja saa tehdä, ja melkein mitä tahansa selaimeen kirjoitettua hyödynnetään myös mainosten kohdentamiseen.


##Oivallukset (5)
1. maininta python-kirjastojen versio-ongelmista ja niiden välttämisestä virtuaaliympäristöjen avulla oli hyvä oppi. Aloitin Python-harjoittelun hankkimalla Anacondan, joten olen välttynyt tuhottomalta asennusrumbalta, mutta eri kirjastojen versio-ongelmat olisi jäänyt kantapään kautta opittavaksi ellei olisi ollut luennolla mainittuna.
1. suurien visioiden äärellä voi olla tympeää puuttua pieniin ohjelmallisiin detaljeihin, mutta silti perusasiat, pääsynhallinta, tunnistaminen, käyttöoikeudet ja muut luennolla käydyt teemat ovat elintärkeitä. Siksipä kehyksillä voi välttää pyörän uudelleenkeksimisen jotta voi keskittyä olennaiseen ja välttyä ns. <a href="https://xkcd.com/327/">helpoilta virheiltä</a>.<img src="https://imgs.xkcd.com/comics/exploits_of_a_mom.png" />
1. xkcd-sarjakuvalle erityismaininta loistavasta web-palvelusta: löysin mieleen jääneet stripit hetkessä, ja niihin oli heti tarjolla sekä sivuille vievät linkit että suoraan kuviin tähtäävät. Pieniä asioita, mutta ah niin mukavia.
1. web-lomakkeiden käytettävyys-esimerkkien ohessa tulee hyvin mieleen omat muistot kun graafisen ohjelmoinnin kurssilla teki ohjelmaa, ja kuinka käytettävyyden tekeminen oli paljolti pientä näpräämistä. Teknisessä mielessä voi tuntua turhauttavalta lisätä ne pari koodiriviä, jotka muuttavat tekstin "Levyn tiedot lisätty" muotoon "Levyn nieminen ja Litmanen tiedot lisätty", mutta käytettävyyden kannalta merkitys onkin jo isompi.
1. vaikka kehykset tarjoaisivat valmiit palikat, tarvitaan räätälöintiä esimerkiksi paremman ja yhtenäisemmän käyttökokemuksen takia. Kehyksissä on todennäköisesti eroja senkin suhteen kuinka helppo niillä on tehdä jokin ratkaisu ja kuinka helppo sitä sitten puolestaan on räätälöidä.

##Kehitysehdotukset (1-3)
1. koodiklinikoista omatoimiset harjoitustehtävät: jos koodiklinikkaa käsittelee vaikka Twitter-analytiikkaa, niin sivuilla voisi olla haasteena "tee hökötys joka hakee twitteristä jotain". Jos missaa luennon, voisi omatoimisesta koittaa myöhemmin paikata. T. nimim. mitäköhän keskiviikkona käytiin läpi.

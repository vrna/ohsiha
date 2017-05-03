#Luentoviikko 10, 3.4.-9.4.2017
Luentoviikolla vuorossa Käytön seuranta.

Ensimmäinen mielleyhtymähän tästä on vanha lainaus "sitä saat mitä mittaat". Sitä kokeilevaa helloworld-sovellusta kirjoittaessa ei ensimmäisenä tule mieleen tehdä analytiikkaa perus debuggaus-toiminnallisuutta pidemmälle. Kuitenkin pidemmän päälle siitä tulee mierkittävämpää.

Useat vaihtoehdot nojautuvat kolmansien osapuolien palveluihin. Periaatteessa web-sovelluksessa on mahdollista seurata paljon itsekin tapahtumia, jos vain rahkeet riittävät toteuttaa diagnostiikkaa jokaiseen tapahtumaan. Työlästä.

Yksityisyyden suoja nostettiinkin isona teemana: kolmannen osapuolen palvelu voi olla helppo käyttöönottaa, mutta datan hallinta siirtyy tällöin ainakin osittain muualle. Jos käyttäjän tietoja viedään ulkopuolisiin paikkoihin, tästä olisi monesti mukava saada tieto. Toisaalta tieto siitä, että nyt tietoja tosiaan siirrytään, huolestuttaa käyttäjiä, joilla on hyvin vähän valtaa siihen mitä ja miten heistä kerätään. Toisaalta on hauska miettiä sitäkin, että samalla kun yksinkertainen sijaintitiedon pyyntö verkkosivulla nostaa karvat pystyyn, niin minustakin löytyy tuhottomat määrät tietoja jo valmiiksi, ja tämä tiedon määrä vain kasvaa.

Visualisoinnit mainittiin erikseen. Mitattuhan on aina, ja dataa on käytännössä aina ollut saatavilla. Datamäärien kasvaessa visualisoinneilla voi kuitenkin nopeasti saada isoista datajoukoista enemmän järkeä.

##Oivallukset (5)
1. Kuinka paljon minusta on jo kerätty dataa ilman että tiedän ja mihin sitä käytetään?
1. Mittaaminen ei tule ensimmäisten asioiden joukossa mieleen sovellusta kehitettäessä.
1. Kuinka paljon arkkitehtuuria joutuukaan muuttamaan myöhemmin saadakseen ympättyä mukaan tehokkaat seurantameneltmät?
1. Perinteiset http-kutsujen mukana kulkevat tiedot paljon käytössä, mutta niistä saa loppujen lopuksi suhteellisen vähän irti.
1. Jos ja kun dataa saa, niin miten siitä jalostetaan päätöksiä sen sijaan, että jäädään "kiva käppyrä kävijöistä" -asteelle

##Kehitysehdotukset (1-3)
1. Yammer oli ihan hyvä ajatus mutta ei ottanut hirveästi tuulta alleen. Matalan kynnyksen keskustelualusta olisi kuitenkin edelleen hyvä.

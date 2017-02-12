#Luentoviikko 3, 6.2.-12.2.2017
Kolmannella luentoviikolla ihmeteltiin datan hankintaa. Dataahan on ympäriinsä valtavat määrät, mutta sen muoto vaihtelee. Joskus dataa pitää poimia ryömijöillä tai raapijoilla ns. Presentation seasta. Nykyään enenevissä määrin tuetaan myös API First -lähestymistapaa, jolloin voidaan tarjota helpommin sivustoa esim. API-muodossa myös muille kehittäjille.

Nopea empriininen tutkimuskin sen osoittaa: melkein joka palvelu tarjoaa hanakasti kehittäjärajapintoja, ja selkeästi kehittäjiä halutaan tukea. Luennolta hyvä maininta myös toki siitä, että esim. Twitterillä näiden ulkopuolisten appien pyyntöjen käsittely on myös iso kuluero ja kutsujen hallinta keskeinen osa palvelun toimivuutta.

Koodiklinikka tarjosi oppia/aikayksikkö -asteikolla yhden TTY-aikani kenties laadukkaimmista tunneista. Esimerkissä käytiin nopeasti datan hakeminen Twitter-API-rajapinnasta, sen käsittely ja visualisoiminen.

Esimerkki oli ymmärrettävästi sangen nopeatempoinen, mutta auttoi riittävästi: demon pohjalta pystyi toistamaan suurimman osan tempuista itsekin. Koodiklinikalla haettiin twitteristä joukko twiittejä API-haulla, poimittin niistä maininnat, luotiin graafi ja visualisoitiin se Gelphillä. Esimerkin puuttuessa (tätä kirjoittaessa) oma toistokokeiluni käytti Tweepyä Twitter-hakuun (kiitos https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/) ja visualisointiin networkx-kirjastoa. Sainkin lopulta luotua Gelphillä näytettävän graafin, joskin Geplhin UI ei vielä täysin auennut. Koodi: ./../TweetReader/tweetsToNetwork.py


##Oivallukset (5)
1. ah, elämä helpottui kun käytti kurssin kotisivuina osoitetta https://ohsiha.github.io/2017 . Ilman vuosilukua meni vähän sekaisin.
1. kirjastojen avulla elämä totisesti helpottuu: aloitin twitter-kehittäjätunnuksen hankinnasta ja parissa tunnissa kummastelin jo Gelphissä graafiani.
1. jos oikein ymmärsin ihan määrättömästi twitter ei anna palveluaan kutsua: kannattaa ehkä kehitysvaiheessa hakea data kerran, tallettaa johonkin, ja käyttää kehitystyöhön tätä paikallista dataa sen sijaan että hakee koko ajan twitteristä uudelleen kaiken, kun oli typottanut muuttujan nimen.
1. Tweepyllä näköjään onnistuisi kanssa useamman twiitin haku helposti. Search-funktion parametreissahan on page. Yhdellä for-loopilla olisi siis saanut enemmänkin twiittejä.
1. Saattoi mennä luennolla ohi - jos se siellä mainittiin - mutta yllätyin semi-positiivisesti kun tajusin että näillekin graafeille oli määritelty graphml, jonka pystyin tulostaan (ja jota ihmissilmälläkin pystyi ymmärtämään) ja toisaalta lukea suoraan Gelphissä.


##Kehitysehdotukset (1-3)
1. visualisointeja tarjoavat palvelut kiinnostaisivat. Nyt käytiin vain nopeasti läpi Gelphiä, mutta noista olisi kiva tietää muutenkin. Äkkiäkös sitä datan kerää nätisti itselleen!

<h1>Luentoviikko 1, 23.-29.1.2017</h1>
<p>Avausluento pidetty. Toissa kev��n� k�vinkin jo kerran kurssilla, mutta j�in tentist� kiinni ja uusintatenttien suhteen oli omia haasteitaan. Joten yritet��s uudestaan, ja jos t�ll� kertaa ei pyrkisi ihan aidan matallimmasta kohdasta. Joka tapauksessa yleiskuva kurssista oli etuk�teen hallussa.<br/><br/>
Johdantona tarjottiin tuttuja ja tuntemattomia esimerkkej� sek� yleiskuvausta kurssista, jonka k�yt�nn�n toteutus taitaa olla hieman avoin. Varsinaista opetusasiaa t�ll� viikolla oli hieman v�hemm�n.<br/><br/>
Keskiviikkona oli koodiklinikka. Harmittavasti en p��ssyt t�ll� kertaa paikalle, ja en ainakaan viel� onnistunut l�yt�m��n tietoa klinikan t�m�n viikkoisesta aiheesta, joten yrit�n korvata omatoimisella etsimisell�.<br/><br/>
Er�st� harkkaty�ideaani (slack-bottina toimiva levyraatisovellus) silm�ll�pit�en vilkaisin Spotifyn ja Slack-viestint�sovelluksen tarjoamat kehitt�j�rajapinnat.<br/><br/>
Spotify (https://developer.spotify.com/web-api/) tarjoaa REST-apin. Vaatii Spotify-k�ytt�j�tunnuksen, ja jos haluaa esimerkiksi k�ytt�jien soittolistoja, rekister�innin. Esimerkit ovat node.js:ll�.<br/><br/>
Pikaviestinsovellus slack (https://slack.com/developers, https://api.slack.com/) tarjoaa my�s paljon apuja botin-tekoon. Palvelu vinkkaa jopa ihan bot-ty�kaluun, https://howdy.ai/botkit/, joka Spotifyn tapaan ilmeisesti toimii Node.js:n varassa. Varsinainen bot-esimerkki on kuitenkin Rubylla. Tarjolla on esimerkkej�, API-rajapintakuvaus ja kaikkea. N�ht�v�sti my�s Slackiin pit�isi sovellukset rekistre�id� erikseen.<br/><br/>
Nopean katselmoinnin perusteella ty�st�n viel� harkkaty�ideaani. Slackissa toimiva spotifyta hy�dynt�v� botti voi olla kovat�inen, kun jo yhdess� API-rajapinnassa on miellytt�v�sti tutkimista.<br/><br/>
</p>
<h2>Oivallukset/Opitut asiat:</h2>
1. Nopean tutkimisen perusteella Slackissa toimiva Spotifyta hy�dynt�v� bot saattaa olla suht. Raskas toteuttaa rekister�intien sun muiden kanssa.
1. Ainakin n�iss� esimerkeiss� dokumentaatiot ja ohjeet ovat hyv�ll� tasolla, ihan kuin palvelut oikeasti suorastaan rohkaisisivat kehitt�m��n omia appeja ;) .
1. T�llaisia API-dokumentaatioita etsiess� �mit�s t��ll� olisi tarjolla�-tyylisess� l�hestymistavassa on vaarassa hukkua informaatio�hkyyn. Suosittelen vain etsim��n nopeasti haluamansa, kokeilemaan agressiivisesti ja sitten vasta kun se postaus ei mill��n toimi, voi lukea tarkemmin miten homma toimii.
1. Luennon esimerkkien perusteella varsin pienell�kin voi saada aikaan mielenkiintoisia tuotteita, kuten #JeSuisCharlie-tagien haistelulla toteutettu hieno aikajanakartta. Tai no, en min� viel� tied� millainen homma tuollainen todella on tehd�.
1. Useat rajapinnat toimivat kuitenkin samankaltaisilla perusperiaatteilla: kun handlaa perus json-k�sittelyt ja API-kutsut, OAuthin ja t�llaiset, on aika nopeasti aika paljon mahdollisukksia.
<h2>Kehitysehdotuksia:</h2>
1. Ensimm�isest� koodiklinikasta ei ainakaan l�ytynyt hirve�sti tietoa mit� siell� l�pik�ytiin. Todella hankalaa heille jotka ei paikalle p��se.
1. Yhteinen matalan kynnyksen kommunikaatioalusta heti kurssin alusta olisi hieno, ns. Koodinimi irc-kanava. Helpottaisi esim. Meik�l�ist�, joka ei tule kaikille luennoille p��sem��n.

<h1>Luentoviikko 1, 23.-29.1.2017</h1>
<p>Avausluento pidetty. Toissa keväänä kävinkin jo kerran kurssilla, mutta jäin tentistä kiinni ja uusintatenttien suhteen oli omia haasteitaan. Joten yritetääs uudestaan, ja jos tällä kertaa ei pyrkisi ihan aidan matallimmasta kohdasta. Joka tapauksessa yleiskuva kurssista oli etukäteen hallussa.<br/><br/>
Johdantona tarjottiin tuttuja ja tuntemattomia esimerkkejä sekä yleiskuvausta kurssista, jonka käytännön toteutus taitaa olla hieman avoin. Varsinaista opetusasiaa tällä viikolla oli hieman vähemmän.<br/><br/>
Keskiviikkona oli koodiklinikka. Harmittavasti en päässyt tällä kertaa paikalle, ja en ainakaan vielä onnistunut löytämään tietoa klinikan tämän viikkoisesta aiheesta, joten yritän korvata omatoimisella etsimisellä.<br/><br/>
Erästä harkkatyöideaani (slack-bottina toimiva levyraatisovellus) silmälläpitäen vilkaisin Spotifyn ja Slack-viestintäsovelluksen tarjoamat kehittäjärajapinnat.<br/><br/>
Spotify (https://developer.spotify.com/web-api/) tarjoaa REST-apin. Vaatii Spotify-käyttäjätunnuksen, ja jos haluaa esimerkiksi käyttäjien soittolistoja, rekisteröinnin. Esimerkit ovat node.js:llä.<br/><br/>
Pikaviestinsovellus slack (https://slack.com/developers, https://api.slack.com/) tarjoaa myös paljon apuja botin-tekoon. Palvelu vinkkaa jopa ihan bot-työkaluun, https://howdy.ai/botkit/, joka Spotifyn tapaan ilmeisesti toimii Node.js:n varassa. Varsinainen bot-esimerkki on kuitenkin Rubylla. Tarjolla on esimerkkejä, API-rajapintakuvaus ja kaikkea. Nähtävästi myös Slackiin pitäisi sovellukset rekistreöidä erikseen.<br/><br/>
Nopean katselmoinnin perusteella työstän vielä harkkatyöideaani. Slackissa toimiva spotifyta hyödyntävä botti voi olla kovatöinen, kun jo yhdessä API-rajapinnassa on miellyttävästi tutkimista.<br/><br/>
</p>
<h2>Oivallukset/Opitut asiat:</h2>
1. Nopean tutkimisen perusteella Slackissa toimiva Spotifyta hyödyntävä bot saattaa olla suht. Raskas toteuttaa rekisteröintien sun muiden kanssa.
1. Ainakin näissä esimerkeissä dokumentaatiot ja ohjeet ovat hyvällä tasolla, ihan kuin palvelut oikeasti suorastaan rohkaisisivat kehittämään omia appeja ;) .
1. Tällaisia API-dokumentaatioita etsiessä “mitäs täällä olisi tarjolla”-tyylisessä lähestymistavassa on vaarassa hukkua informaatioähkyyn. Suosittelen vain etsimään nopeasti haluamansa, kokeilemaan agressiivisesti ja sitten vasta kun se postaus ei millään toimi, voi lukea tarkemmin miten homma toimii.
1. Luennon esimerkkien perusteella varsin pienelläkin voi saada aikaan mielenkiintoisia tuotteita, kuten #JeSuisCharlie-tagien haistelulla toteutettu hieno aikajanakartta. Tai no, en minä vielä tiedä millainen homma tuollainen todella on tehdä.
1. Useat rajapinnat toimivat kuitenkin samankaltaisilla perusperiaatteilla: kun handlaa perus json-käsittelyt ja API-kutsut, OAuthin ja tällaiset, on aika nopeasti aika paljon mahdollisukksia.
<h2>Kehitysehdotuksia:</h2>
1. Ensimmäisestä koodiklinikasta ei ainakaan löytynyt hirveästi tietoa mitä siellä läpikäytiin. Todella hankalaa heille jotka ei paikalle pääse.
1. Yhteinen matalan kynnyksen kommunikaatioalusta heti kurssin alusta olisi hieno, ns. Koodinimi irc-kanava. Helpottaisi esim. Meikäläistä, joka ei tule kaikille luennoille pääsemään.

# Harjoitustyön 2. vaiheen palautus.

Sanon vaan kerran: toteutus toimii, muttei ole kaunein mahdollinen. Mutta se toimii.

Ensimmäinen osa työtä oli tehdä toimenpiteet käyttäjätunnuksen lisäämiselle ja sisään + uloskirjautumiselle.

Käyttäjätunnuksen hallintaan olisi löytynyt flaskin omia kirjastoja, mutta niistä en oikein päässyt liikkeelle.

Onneksi löysin demon, jolla sain homman toimiin. Ytimessä oli tehdä html-form, johon käyttäjätiedot pystyi syöttään, ja tämä ohjattiin sitten joko login- tai register -sivulle.

Formiin syötetty URL ohjasi kutsun
```html
<form method=POST action="{{ url_for('register') }}">
```
ja tälle oli sitten funktio
```python
@app.route('/register', methods=['POST', 'GET'])
def register():
```

Jossa sitten tehtiin perustoimenpiteet: katsotaan onko käyttäjä olemassa, onko salasana ja ktunnus syötetty jne. Jos homma onnistui, tallennettiin käyttäjätunnus lopulta sessio-tietoihin:
```python
session['username'] = request.form['username']
```

tai poistetiin sieltä uloskirjautuessa:
```python
session.pop('username', None)
```

Toinen vaihe oli saada lisäys, näytä, päivitä ja tuhoa -ominaisuudet.

Lisääminen oli helpointa: aivan kuten käyttäjätunnuksenkin kanssa, formissa pystyi määrittämään kutsuttavan funktion, jossa päästiin käsiksi haluttuihin inputteihin. Näin ollen lisääminen toimi samalla logiikalla kuin käyttäjissä. Samaan syssyyn onnistui päivittäminen, sillä lisäämisen yhteydessä tarkasteltiin oliko ko. objekti jo olemassa:
```python
@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
      existing['content'] = request.form['content']
      ...
      lists.insert({'name' : request.form['listname'], 'content' : request.form['content']})
```

Näyttämisessä jouduin vähän kikkaileen. Kirjautumisen jälkeen renderöin actions.html -sivun, jossa oli ensin päivitystoiminto perinteisen formin ja inputin avulla. Kun tietokannassa oli tavaraa, tämän pystyi hakemaan muuttujaan, ja antamaan sivun renderöinnin yhteydessä parametrina:

```python
return render_template('actions.html',cont=mylists())
```

jossa mylists() haki tietokannassa haluamani objektit muuttujaan. Kun tämä muuttuja oli tehty, sitä pystyi selaamaan for-loopilla, jolloin siihen pystyi tulostamaan helposti myös Update- ja Delete -painikkeet. Laittamalla listan sisään input-palikat tyypillä "hidden" sain väliteltyä myös tietoja joita en halunnut useaan kertaan näyttää.
```html
{% for ls in cont %}
    {{ls.name}}
    <form method=POST action="{{ url_for('list') }}">
      <div class="form-group">
          <input type="hidden" class="form-control" name="listname" value="{{ls.name}}">
          <input type="hidden" class="form-control" name="deleting" value="true">
          <button type="submit" class="btn btn-primary btn-block">Delete</button>
      </div>
    </form>
{% endfor %}
```

Poistaminen piti toteuttaa hieman kankeasti lisäämällä ylimääräinen input-elementti arvolla "deleting". Jos se oli olemassa, poistettiin löydetty objekti.

## Vaikeaa:
1. oikean pohjan löytäminen ja alkuun pääseminen, oikeat kirjastot jne.
1. tietojen välittäminen html:n ja palvelimen välillä, ts. millä saan tietokantaobjektit näkymään.
1. pysyminen kärryillä siitä, pitikö neuvoa etsiä html:stä, pythonista, flaskista vai milloin mistäkin. Ts. mikä kuuluu mihinkin kehykseen.

## Helppoa
1. perustoiminnot, kuten ohjelmalogiikka tai html-koodaus sitten kun sai kiinni välitettävästä kutsusta ja datasta.
1. tiedon etsiminen. Yllättävän yleisistä virheistä tyyllin "bad request" löytyi nopeasti hyödyllisiäkin vihjeitä.
1. kokeilu sitten kun puolivahingossa sai debug-tilan päälle, joka päivitti python-scriptiä lennosta ja johon pystyi tulostamaan tarvittaessa lisäinfoa.

## Linkkejä:
###Loginiin parikin:
https://flask-login.readthedocs.io/en/latest/
https://blog.openshift.com/use-flask-login-to-add-user-authentication-to-your-python-application/

### Tämän tutoriaalin pohjalta sain loginin lopulta toimimaankin, ja tämän pohjalta onnistui muutkin toiminnot soveltamalla:
https://www.youtube.com/watch?v=vVx1737auSE
https://github.com/PrettyPrinted/mongodb-user-login

Perusgooglaus: pymongo, html, flask, python...

### lähdekoodit:
https://github.com/vrna/ohsiha/tree/master/Harjoitustyo/Koodit

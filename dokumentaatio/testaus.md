# Testaus

### Tekoäly

Tekoälyn testit kansiossa src/tests/ai_test.py

Testattuja skenaariota: 
 * Tekoäly käynnistyy oikein
 * Minimax löytää yhden siirron voiton syvyydellä 1 ja palauttaa arvon 100000 (voitto)
 * Minimax estää avokolmosta syntymästa sillä se johtaa varmaan häviöön
 * Minimax löytää monimutkaisemman neljän siirron voiton ja palauttaa arvon 100000
 * Minimax osaa pelata tasapelin loppupelissä (15 siirtoa)
 * Evaluaatiofunktio kattaa koko laudan
   * Evaluaatiofunktion toimintaa muuten testattu lähinnä pelaamamalla, sillä sen lähteenä on oma pääni ja laudan tilanteiden käsin laskeminen olisi työlästä.
 * Iteratiivinen syveneminen toimii ja löytää kolmen siirron voiton minimaxia käyttäen
 * Tekoäly tunnistaa myös tappion ja palauttaa arvon -100000 (tappio)
 * Iteratiivinen syveneminen toimii myös kun voittoa tai tappiota ei ole löydettävissä ja aikakatkaisee haun.

Lisäksi tekoälyä on testattu paljon pelaamalla sitä vastaan ja se on kokemattomalle pelaajalle vahva vastustaja. Muistaakseni voitin valmiin tekoälyn kerran loppupelissä mutta muuten häviän melkein aina.

Tekoälyn evaluaatio on toki oma tuotokseni eikä se ole täydellinen

### Yksikkötestaus

Luokat Game (entities/game.py), Board (entities/board.py) ja AI (entities/ai.py) on yksikkötestattu kattavasti. 

Luokkien Game ja AI testauksessa on käytetty integraatiotestausta luokan Board kanssa.

Luokkaa App.py ei ole yksikkötestattu, mutta sen toiminnasta on varmistuttu pelaamalla paljon pelejä kehityksen aikana ja sen jälkeen.


Yksikkötestit voi ajaa asentamalla kehityksen aikaiset riippuvuudet komennolla ```poetry install --with dev```,

käynnistämällä virtuaaliympäristön ```poetry shell ```,

ja suorittamalla virtuaaliympäristössä komennon ```pytest src```,



Testikattavuutta voi tutkia komennoilla ```coverage run --branch -m pytest src ```

ja ```coverage html ``` ja avaamalla coveragen luoman tiedoston index.html (htmlcov/index.html) selaimessa. 

Haaraumakattavuus main.py poisluettuna:

![image](https://github.com/kaarleol/connect4/assets/127772376/87c1f33f-81c1-4046-b12c-13a1fc037b61)

### Muu testaus

Yksikkötestauksen lisäksi testausta on suoritettu paljon manuaalisesti pelin ja tekoälyn toiminnan varmistamiseksi.

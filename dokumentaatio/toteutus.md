# Toteutus

### Rakenne

Ohjelma koostuu neljästä luokasta, App (src/main.py), Board (src/entities/board.py), AI (src/entities/AI.py) ja Game (src/entities/game.py)

Luokkien tarkemmat metodit on dokumentoitu koodissa.

App (src/main.py):
  * Peliloop
  * Huolehtii käyttäjän siirroista
  * Huolehtii tekoälyn siirroista
  * Huolehtii pelin säännöistä ja päättymisestä
  * Yhteydessa Gameen vuorojen ylläpitämiseksi ja siirtojen tekemiseksi ja sen tarjoamia tarkistuksia varten
  * Yhteydessa Boardiin laudan tilanteen ylläpitämiseksi ja sen tarjoamia tarkistuksia varten

Board (src/entities/board.py):
  * Tarjoaa paljon apufunktiota laudan ja siirtojen tarkistamiseen ja muokkaamiseen ja laudan tilanteen ylläpitoon.
  * Kaikki muut luokat yhteydessä lautaan tai mahdollisesti omiin lautoihinsa.

AI (src/entities/AI.py):
  * Minimaxilla toimiva tekoäly
  * Pelin vastapelaaja
  * Saa Appilta pelitilanteen ja laskee mielestään parhaan vastasiirron
  * Käyttaa Boardia laudan ylläpitoon ja erilaisiin tarkistuksiin

Game (src/entities/game.py):
  * Pitää yllä siirtovuoroa ja tarjoaa pari lyhyempää tarkistusmetodia Appille Boardia käyttaen

  * Olisi varmaan voinut jäädä osaksi Appia, mutta eriytin projektin alkuvaiheessa omaksi luokakseen ja sellaiseksi se jäi

![image](https://github.com/kaarleol/connect4/assets/127772376/36497e44-af4d-4feb-b697-638c21949a5b)

### Aikavaativuus

Minimax algoritmin aikavaatimus on O(b^m) eli (laillisten siirtojen määrä)^hakusyvyys. Connect4:ssä laillisia siirtoja on max 7 eli toivottavasti pääsin alle  O(7^hakusyvyys).

Alpha-beta karsinnan jälkeen minimaxin ihanteellinen aikavaativuus olisi O(7^(hakusyvyys)/2), mutta tämä ei ole käytännossä mahdollista ilman täydellistä tietoa. Algorimini aikavaativuus on siis jossain naiden välillä

Empiirisen testauksen perusteella pelkkä minimax pääsi 3:ssa sekunnissa noin syvyydelle 6 iteratiivisessa syvenemisessä ja alpha-beta-karsinnan siirtojen järjestämisen jälkeen syvyydelle 8-9.

Eli todellinen aikavaativuus on ehkä noin O( 7^(hakusyvyys*(2/3)) ) tai vähän yli sen riippuen siirtojen pakottavuudesta ja kuinka lähelle laudan keskustaa oikeasti paras siirto sijoittuu. Sarakkeiden täyttyessä algoritmi nopeutuu huomattavasti.

### Työn puutteet

Peliä voi pelata vain aloitusvuorossa olevana pelaajana. Olisi ollut hyvä tehdä mahdollisuus pelata 2. siirtovuorossa olevana pelaajana, vaikkei sillä itse algorimin kannalta ole niin merkitystä.

Vaikka uskon, että itse minimax ja alpha-beta-karsinta toimivat projektissa on varmasti monia operaatioita jotka olisi voinut suorittaa tehokkaammin.

Connect4:ssä on myös melko rajallinen määrä eri laudan tilanteita ja eri siirtojärjestykset johtavat samoihin laudan tilanteisiin. Olisi varmaan mahdollista toteuttaa paremmin pelaava tekoäly jos sille loisi jonkun tietopankin tiedetyistä voittavista asemista joita tavoitella


### Laajat kielimallit

Käytin ChatGPT V4 pseudokoodia ja selityksiä varten minimaxin ja aplha/beta karsinnan ymmärtämiseksi. Käytin sitä myös docstringien kirjoittamiseen joillain muokkauksilla. Yritin käyttää sitä koodin refaktorointiin epäonnistuneesti.

Käytin sitä myös pythonin eri syntaxien, valmiiden funktioiden komentojen ja kirjastojen muistamiseen. 

Käytin sitä myös joihinkin lambda-funktioihin jotka eivät kuitenkaan päätyneet lopulliseen palautukseen.

### Lähteet

[Wikipedia minimax](https://en.wikipedia.org/wiki/Minimax), pseudokoodi + algoritmin ymmärtäminen

[Wikipedia alpha-beta-pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), pseudokoodi + algoritmin ymmärtäminen

[Connect4 solver](https://connect4.gamesolver.org/) eri pelitilanteiden etsimiseen testejä varten

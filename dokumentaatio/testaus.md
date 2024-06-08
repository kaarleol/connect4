# Testaus

### Yksikkötestaus

Luokat Game (entities/game.py) ja Board (entities/board.py) on yksikkötestattu kattavasti, mutta muihin luokkiin en ole vielä päässyt. 

Luokan Game testauksessa on käytetty integraatiotestausta luokan Board kanssa.



Yksikkötestit voi ajaa asentamalla kehityksen aikaiset riippuvuudet komennolla ```poetry install --with dev```,

käynnistämällä virtuaaliympäristön ```poetry shell ```,

ja suorittamalla virtuaaliympäristössä komennon ```pytest src```,



Testikattavuutta voi tutkia komennoilla ```coverage run --branch -m pytest src ```

ja ```coverage html ``` ja avaamalla coveragen luoman tiedoston index.html (htmlcov/index.html) selaimessa. 

### Muu testaus

Yksikkötestauksen lisäksi testausta on enimmäkseen suoritettu manuaalisesti käyttöliittymän kautta. Etenkin tekoälyn toimintaa on testattu näin.


# connect4

[Määrittely](https://github.com/kaarleol/connect4/blob/main/dokumentaatio/maarittely.md)

[Testaus](https://github.com/kaarleol/connect4/blob/main/dokumentaatio/testaus.md)

## Käynnistysohjeet

Projektin riippuvuudet ovat tällä hetkellä melko yksinkertaisia, lähinnä python asennettuna.

Sovellus käynnistyy kirjoittamalla pääkansiossa komennon ```python3 scr/main.py ```

Pelin aikana siirrot saa tehtyä yksinkertaisesti sarakkeita vastaavilla numeroilla (0-6)


---

Yksikkötestit voi ajaa asentamalla kehityksen aikaiset riippuvuudet komennolla ```poetry install --with dev```,

käynnistämällä virtuaaliympäristön ```poetry shell ```,

ja suorittamalla virtuaaliympäristössä komennon ```pytest src```,

---

Testikattavuutta voi tutkia komennoilla ```coverage run --branch -m pytest src ```

ja ```coverage html ``` ja avaamalla coveragen luoman tiedoston index.html (htmlcov/index.html) selaimessa. 


Pylint on myös käytössä ja sitä voi tarkkailla komennolla ```pylint src ```




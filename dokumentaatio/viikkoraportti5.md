# Viikkoraportti 5

### Tekemiset & edistyminen

Tällä viikolla tapahtui algoritmissa edistystä, otin käyttöön iteratiivisen syvenemisen ja ajastuksen minimaxin kanssa, alfa-beta-karsinnan ja sanakirjan eri paliasetelmille.

Loin myös boardille apufunktion joista laudan tilasta muodostetaan yksilöivä koodi.

Laudan tilan eri jatkosiirtojen evaluaatiot tallennetaan sanakirjaan ja niitä voidaan käyttää uudestaan hakujärjestyksen parantamiseksi jos samaan tilaan palataan uudestaan toista kautta tai syvemmillä hauilla. Siirrot evaluoidaan kuitenkin uudestaan, sillä syvenmmän haun evaluaatio voi olla eri.

Sanakirja tyhjennetään joka vuoron jälkeen poislukien tekoälyn tekemän siirron jatkosiirrot, joita käytetään uudestaan järjestämään seuraavaa hakua.

Lisäksi koodiin on tehty jonkin verran refaktorointia vaikka etenkin tekoälyn metodeja pitäisi edelleen siistiä

### Oppimiset

Luulen ymmärtäväni nyt paremmin alfa-beta-karsimista ja sen implementaatio ainakin nopeutti tekoälyä. Toivottavasti se toimii

### Epäselvää

Tietorakenteeni + alfa-beta-karsiminen nopeuttivat tekoälyä huomattavasti: 3s aikana tekoälyn syvyys vaihtui 6 -> 9 niiden toteuttamisen jälkeen.

En kuitenkaan ole satavarma toimivatko ne täysin oikein

### Seuraavaksi

Itse evaluaatio on vielä aivan liian yksinkertainen ja haluan sitä parannella, mutta aika tällä viikolla loppui kesken. Lisäksi tekoälyä ei vieläkään testata järjestelmätasolla.

Vaikka tiedän että tekoäly löytää voittavat siirrot syvyyshakunsa sisällä jne pitää testausta vielä tehdä paljon.

Lisäksi monet tekoälyn metodit ovat todedlla pitkiä ja sotkuisiaa ja vaativat refaktorointia myös testaamisen helpottamiseksi. Tähän todennäköisesti kuluu viimeinen viikko dokumentaation parantamisen ohella.

### Tunnit

Yhteensä noin 13h

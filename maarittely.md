# Määrittelydokumentti

* Ohjelmointikieli: python. Osaan myös javascriptiä melko hyvin.
* Aikomukseni on toteuttaa minimax-algoritmilla toimiva tekoäly pelille Connect4
* Ohjelma saa syötteenä vastapelaajan eli ihmisen siirrot ja yrittää laskea parhaan jatkon
* Minimax algoritmin aikavaatimus on O(b^m) eli (laillisten siirtojen määrä)^hakusyvyys. Connect4:ssä laillisia siirtoja on max 7 eli toivottavasti pääsin alle O(7^hakusyvyys). Alfa-beta karsinnalla pitäisi parhaassa tapauksessa päästä O(7^(syvyys/2)) ja siirtojen järjestämisen tehostaa asiaa entisestään [[1]](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Rekursion tehostamiseksi aikaisemmin laskettuja tuloksia tallennetaan todennäköisesti esimerkiksi sanakirjaan

### Aiheen ydin

Aiheen ytimenä on toivottavasti connect4:ää hyvin pelaava tekoäly sekä sen toteuttaminen tehokkaasti ja rekursiivisesti minimax-algorimilla. Aikomuksenani on käyttää kurssilla tarjottua tekoälypohjaa connect4:ään. Algoritmin rakenteen tukena käytän varmaan wikipediasta löytyvää pseudokoodia alfa-betakarsintaan ja itse minimax algoritmiin

### Muuta

* Dokumentaatiokieli: Suomi
* Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma

### Viitteet 
1. [Alpha-beta pruning, wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), viitattu 14.05.2024

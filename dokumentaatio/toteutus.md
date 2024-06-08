# Toteutus

# Rakenne

Tällä hetkellä sovelluksen komponentteja ovat luokat App, Game, Board ja AI.

Luokka App löytyy tiedostosta main.py kansion src alta. Luokka App käynnistää pelin, huolehtii pelisyklistä ja pelaajan ja tekoälyn syötteistä. Luokka lähettää pelitilanteen tekoälylle ja pyytää siltä siirtoa.

Luokka Game (entities/game.py) on melko yksinkertainen luokka jossa ylläpidetään käynnissä olevaa peliä ja vuoroja. Sillä on pari metodia joilla helpotetaan Appin ja Boardin välistä kommunikointia

Luokka Board (entities/board.py) on laajahko luokka jolla on monia metodeja laudan muokkaukseen ja laudan tilanteen tarkistamiseen.

Luokka AI (entities/ai.py) on pelin tekoäly ja vastapelaaja. Luokka vastaanottaa pelitilanteen ja laskee parhaan vastaussiirron. Tekoäly toimii tällä hetkellä vain 2. siirtovuorossa olevalla pelaajalla.

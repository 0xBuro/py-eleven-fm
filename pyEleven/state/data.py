from ..models.club import Club
from ..models.coach import Coach
from ..models.goalkeeper import Goalkeeper
from ..models.player import Player

clubs = []

# Liste aus Club-Namen und Fan-Stimmung
club_names = ["FC Bayern München", "Real Madrid CF", "Arsenal FC", "AC Milan", "AFC Ajax Amsterdam", "Fenerbahce SK"]
fan_sentiments = [0.65, 0.75, 0.85, 0.6, 0.5, 0.9]

# Club-Objekt aus den Listen erstellen
for name, sentiment in zip(club_names, fan_sentiments):
    club = Club(name, sentiment, None, None)
    clubs.append(club)

coaches = []

# Liste aus Trainer-Namen, Alter und Strategie
coach_names = ["Thomas Tuchel", "Carlo Ancelotti", "Mikel Arteta", "Stefan Pioli", "Maurice Steijn", "Jorge Jesus"]
ages = [49, 64, 41, 57, 49, 68]
strategies = ["offensiv", "offensiv", "konter", "defensiv", "konter", "defensiv"]

# Coach-Objekt aus den Listen erstellen
for name, age, strategy in zip(coach_names, ages, strategies):
    coach = Coach(name, age, strategy)
    coaches.append(coach)

goalkeepers = []

# Liste aus Torwart-Namen, Alter, Rückennummer und reflex-stats
goalkeeper_names = ["M. Neuer", "T. Courtois", "A. Ramsdale", "M. Maignan", "J. Gorter", "A. Bayindir"]
ages = [37, 31, 25, 27, 23, 25]
numbers = [1, 1, 1, 16, 1, 1]
reflexes = [0.85, 0.9, 0.8, 0.8, 0.75, 0.7]

# Goalkeeper-Objekt aus den Listen erstellen
for name, age, number, reflex in zip(goalkeeper_names, ages, numbers, reflexes):
    goalkeeper = Goalkeeper(name, age, number, reflex)
    goalkeepers.append(goalkeeper)


players_by_club = [
    # Bayern
    [
        # DEF
        Player("M. De Ligt", 23, "DEF", 4, 0.8),
        Player("D. Upamecano", 24, "DEF", 2, 0.8),
        Player("A. Davies", 22, "DEF", 19, 0.85),
        Player("N. Mazraoui", 25, "DEF", 40, 0.8),
        Player("B. Pavard", 27, "DEF", 5, 0.75),

        # MF
        Player("J. Kimmich", 28, "MF", 6, 0.85),
        Player("L. Goretzka", 28, "MF", 8, 0.75),
        Player("J. Musiala", 20, "MF", 42, 0.85),
        Player("K. Coman", 27, "MF", 11, 0.8),

         # ST
        Player("S. Gnabry", 27, "ST", 7, 0.8)
    ],

    # Real Madrid
    [
        # DEF
        Player("E. Militao", 25, "DEF", 3, 0.9),
        Player("D. Alaba", 30, "DEF", 4, 0.8),
        Player("A. Rüdiger", 30, "DEF", 22, 0.8),
        Player("D, Carvajal", 31, "DEF", 2, 0.85),

        # MF
        Player("F. Valverde", 24, "MF", 15, 0.9),
        Player("T. Kroos", 33, "MF", 8, 0.85),
        Player("L. Modric", 37, "MF", 10, 0.85),
        Player("K. Coman", 27, "MF", 11, 0.9),

         # ST
        Player("V. Junior", 22, "ST", 7, 0.85),
        Player("K. Benzema", 35, "ST", 9, 0.9)
    ],

    # Arsenal
    [
        # DEF
        Player("W. Saliba", 22, "DEF", 12, 0.85),
        Player("G. Magalhaes", 25, "DEF", 6, 0.8),
        Player("O. Zinchenko", 26, "DEF", 35, 0.75),
        Player("B. White", 25, "DEF", 4, 0.8),

        # MF
        Player("T. Partey", 31, "MF", 5, 0.75),
        Player("G. Xhaka", 30, "MF", 34, 0.75),
        Player("M. Odegaard", 24, "MF", 8, 0.75),

         # ST
        Player("R. Nelson", 23, "ST", 24, 0.8),
        Player("G. Martinelli", 22, "ST", 11, 0.8),
        Player("B. Saka", 21, "ST", 7, 0.9)
    ],

    # AC Milan
    [
        # DEF
        Player("F. Tomori", 25, "DEF", 23, 0.8),
        Player("T. Hernandez", 25, "DEF", 19, 0.75),
        Player("P. Kalulu", 23, "DEF", 20, 0.7),
        Player("D. Calabria", 26, "DEF", 2, 0.85),

        # MF
        Player("S. Tonali", 23, "MF", 8, 0.8),
        Player("I. Bennacer", 25, "MF", 4, 0.7),
        Player("B. Diaz", 23, "MF", 10, 0.85),
        Player("A. Saelmaekers", 23, "MF", 56, 0.8),
        Player("R. Leao", 24, "MF", 17, 0.9),

         # ST
        Player("D. Origi", 28, "ST", 27, 0.8)
    ],

    # Ajax Amsterdam
    [
        # DEF
        Player("J. Timber", 22, "DEF", 2, 0.85),
        Player("C. Bassey", 23, "DEF", 3, 0.7),
        Player("O. Wijndal", 23, "DEF", 5, 0.75),
        Player("D. Rensch", 20, "DEF", 15, 0.8),

        # MF
        Player("E. Alvarez", 25, "MF", 4, 0.85),
        Player("K. Taylor", 21, "MF", 8, 0.75),
        Player("D. Klaassen", 30, "MF", 6, 0.75),
        Player("M. Kudus", 22, "MF", 20, 0.8),

         # ST
        Player("S. Bergwijn", 25, "ST", 7, 0.85),
        Player("D. Tadic", 34, "ST", 10, 0.85)
    ],

    # Fenerbahce
    [
        # DEF
        Player("A. Szalai", 25, "DEF", 41, 0.75),
        Player("L. Peres", 28, "DEF", 28, 0.7),
        Player("F. Kadioglu", 23, "DEF", 7, 0.8),
        Player("S. Aziz", 32, "DEF", 4, 0.7),

        # MF
        Player("W. Arao", 31, "MF", 5, 0.75),
        Player("A. Güler", 18, "MF", 10, 0.9),
        Player("M. Crespo", 26, "MF", 27, 0.75),

         # ST
        Player("E. Mor", 25, "ST", 99, 0.75),
        Player("E. Valencia", 33, "ST", 13, 0.8),
        Player("M. Batshuayi", 29, "ST", 23, 0.85)
    ],
]

# Spieler-Objekte den Clubs zuordnen
for club, players in zip(clubs, players_by_club):
    club.players.extend(players)

    coach = coaches.pop(0)
    club.coach = coach

    goalkeeper = goalkeepers.pop(0)
    club.goalkeeper = goalkeeper
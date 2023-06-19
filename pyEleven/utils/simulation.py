import time
import random

def intro_text(team, opp):
    '''
    Ausgabe eines Intro Kommentator Texts, bevor das Spiel startet.
    Hier werden die Trainer, ihre Strategie und die jeweiligen Kader
    vorgestellt.
    '''
    print("========================================================")
    time.sleep(1)
    print(f"Willkommen zum Spiel {team.name} vs {opp.name}.")
    time.sleep(2)
    print(f"Wir sehen wie sich die beiden Trainer {team.coach.name} und {opp.coach.name} begrüßen.")
    time.sleep(1)
    print(f"{team.coach.name} kennen wir als Meister der {team.coach.strategy} Strategie,")
    print(f"mal schauen wie {opp.coach.name} mit seiner {opp.coach.strategy} Strategie antworten wird.")    
    time.sleep(2)
    print(f"\nHier die Aufstellung zum heutigen Spiel:\n")
    print(f"{team.name} spielt mit folgender 11:")
    time.sleep(1)
    print(f"({team.goalkeeper.position}) {team.goalkeeper.number}. {team.goalkeeper.name}")
    for player in team.players:
        print(f"({player.position}) {player.number}. {player.name}")
    print("\n") 
    time.sleep(1)
    print(f"{opp.name} spielt mit folgender 11:")
    time.sleep(1)
    print(f"({opp.goalkeeper.position}) {opp.goalkeeper.number}. {opp.goalkeeper.name}")
    for player in opp.players:
        print(f"({player.position}) {player.number}. {player.name}")     
    print("========================================================")
    time.sleep(2)
    print("\nEs ist soweit. Anpfiff! 90 Minuten pure Spannung erwarten uns heute.")      
    
    
def generate_event():
    '''
    Generiert zufällige Ereignisse im Spielverlauf.
    '''
    position = ['target', 'pass', 'corner', 'foul']
    event = random.choice(position)
    return event

def duell_event(player, goalkeeper):
    '''
    Simuliert ein Duell zwischen Spieler und Torhüter
    Kann "goal" oder "save" zurückgeben.
    '''
    shoot_skill = player.shoot()
    parry_skill = goalkeeper.parry()
    
    if shoot_skill > parry_skill:
        return "goal"
    else:
        return "save"
    
def random_event(team, opp):
    '''
    Simuliert zufällige Ereignisse während des gesamten Spiels.
    Ausgabe True, wenn das Spiel vorbei ist, sonst False.
    '''
    min_played = 0
    home_goal = 0
    away_goal = 0
    
    while min_played < 90:
        interval = random.randint(1, 15)
        
        if min_played + interval > 90:
            interval = 90 - min_played
        
        
        player = random.choice(team.players + opp.players)
        event = generate_event()
        club = random.choice([team.name, opp.name])
        
        time.sleep(1)
        if event == 'target':
            print(f"{min_played}: {player.name} versucht es mit eine Schuss")
            goalkeeper = opp.goalkeeper if player in team.players else team.goalkeeper
            result = duell_event(player, goalkeeper)
            if result == "goal":
                if player in team.players:
                    home_goal += 1
                    print(f"{min_played}: TOOOOOR!! {player.name} hat ihn für {team.name} verwandelt!")     
                else:
                    away_goal += 1
                    print(f"{min_played}: TOOOOOR!! {player.name} hat ihn für {opp.name} verwandelt!")     
            else:
                print(f"{min_played}: Glanzvolle Parade von {goalkeeper.name}!")
        if event == 'pass':
            print(f"{min_played}: Zuspiel von {player.name}") 
        if event == 'corner':
            print(f"{min_played}: Eckball für {club}")
        if event == 'foul':
            print(f"{min_played}: Foulspiel durch {player.name}")             
        
        min_played += interval
        
        if min_played >= 90:
            print(f"{min_played}: Abpfiff! Das Spiel ist vorbei!") 
            time.sleep(1)
            print(f"Endstand: {team.name} {home_goal} - {away_goal} {opp.name}")
            time.sleep(2)
            return True
        
    return False    
        
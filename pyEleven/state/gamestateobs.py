from ..models.manager import Manager

import datetime as dt
import sys

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

from . import data
from ..utils.simulation import intro_text, random_event
from ..utils.save_load import save_state, load_state

import random

class GameStateObserver:
    def __init__(self):
        self.state_action = {
            'init_game': self.init_game_state,
            'new_game': self.new_game_state,
            'onboard_game': self.onboard_game_state,
            'main_menu': self.main_menu_state,
            'match_simulation': self.match_simulation_state
        }

    def update(self, game_state, *args, **kwargs):
        '''
        Update des Game States abhängig vom übergebenen State and ruft die entsprechende
        Aktion auf.

        Args:
            game_state (str): der neue Game State.
            *args: optional zusätzliche Argumente.
            **kwargs: optionale Key-Word-Argumente.
        '''
        action = self.state_action.get(game_state)
        if action:
            action(*args, **kwargs)

    def init_game_state(self):
        '''
        Aktion für 'init_game' state.
        '''
        init_game()

    def new_game_state(self):
        '''
        Aktion für 'new_game' state.
        '''
        start_new_game()      

    def onboard_game_state(self, manager):
        '''
        Aktion für 'onboard_game' state.
        
        Args:
            manager (Manager): Manager Objekt.
        '''
        onboard_game(manager)     
    
    def main_menu_state(self, manager):
        '''
        Aktion für 'main_menu' state.
        
        Args:
            manager (Manager): Manager Objekt.
        '''
        main_menu(manager)  
        
    def match_simulation_state(self, team, opp, manager):
        '''
        Aktion für 'match_simulation' state.

        Args:
            team (Team): Spieler-Team.
            opp (Team): Gegner-Team.
            manager (Manager): Manager-Objekt.
        '''
        match_simulation(team, opp, manager)   

class GameState:
    def __init__(self):
        self.observers = []
    
    def register_observer(self, observer):
        '''
        Registrieren eines observers für game state.

        Args:
            observer (GameStateObserver): Observer-Objekt.
        '''
        self.observers.append(observer)
    
    def update_game_state(self, new_state, *args, **kwargs):
        '''
        Update des game state und informieren des observers.

        Args:
            new_state (str): neuer Game State.
            *args: optionale Argumente.
            **kwargs: optionale Key-Word-Argumente.
        '''
        for observer in self.observers:
            observer.update(new_state, *args, **kwargs)    


gameState = GameState()
gameStateObserver = GameStateObserver()
gameState.register_observer(gameStateObserver)            


def init_game():
    '''
    Initialisiere das Spiel und zeige Menü-Optionen für den Benutzer.
    '''
    print("\n")
    cprint(figlet_format('pyEleven FM', font='standard'),
           'white', 'on_green', attrs=['bold'])
    print("\n-----------------")
    print("* Neuer Spielstand (n)")
    print("* Lade Spielstand (l)")
    print("-----------------")

    choice = str(input())
    if choice.lower() == 'n':
        try:
            gameState.update_game_state('new_game')
        except ValueError as e:
            print(f"Error: {e}")
            init_game()
    elif choice.lower() == 'l':
        game_state = load_state('./game_state.json') 
        manager_name = game_state['name']
        age = game_state['age']
        club_index = game_state['club']
        
        selected_club = data.clubs[club_index]
        manager = Manager(manager_name, age, selected_club)
        gameState.update_game_state('main_menu', manager)     
    else:
        init_game()


def start_new_game():
    '''
    Startet ein neues Spiel und fragt Manager Details ab.
    '''
    while True:
        manager_name = str(input('Bitte geben Sie Ihren Namen ein: '))
        if not manager_name:
            print("Bitte gib einen Namen ein.")
            continue 
        while True:
            birthday_str = str(input('Bitte geben Sie Ihr Geburtsdatum ein (tt.mm.jjjj): '))
            try:
                birthday = dt.datetime.strptime(birthday_str, '%d.%m.%Y')
                if birthday.date() > dt.date.today():
                    print("Geburtsdatum muss in der Vergangenheit liegen.")
                    continue
                break
            except ValueError:
                print("Ungültiges Format. Bitte nutze tt.mm.jjjj.")
                continue
        break
    
    manager = Manager(manager_name, birthday)
    gameState.update_game_state('onboard_game', manager)

        
def onboard_game(manager):
    '''
    Onboard für den Spieler (Manager) mit Auswahl-Option aus verschiedenen Clubs

    Args:
        manager (Manager): Manager-Objekt.
    '''
    clubs = data.clubs
    print(f"\nWillkommen bei pyEleven, {manager.get_name()} ({manager.get_ageFromBirthday()})!\nWähle nun einen Club, um in der Liga der Legenden um den Pokal zu kämpfen.\n")    
    
    print("Wähle deinen Club\n")
    for index, club in enumerate(clubs):
        print(f"({index+1}) {club.name}, Fan Sentiment: {club.fan_sentiment}")
        print(f"Coach: {club.coach.name}, Strategie: {club.coach._strategy}\n")
            
    selected_club = None
    
    while selected_club is None:
        club_choice = int(input("Tippe von 1 - 6 um einen Club auszuwählen: "))
        
        try:
            club_choice = int(club_choice)
            
            if 1 <= club_choice <= len(clubs):
                selected_club = clubs[club_choice - 1]
                manager._club = selected_club
                
                manager_data = {
                    'name': manager.name,
                    'age': manager.get_ageFromBirthday(),
                    'club': club_choice - 1
                }
                
                save_state('./game_state.json', manager_data)
                gameState.update_game_state('main_menu', manager)
            else:
                print("Ungültige Eingabe. Bitte wähle eine Nummer von 1 - 6")   
        except ValueError:
            print("Ungültige Eingabe. Bitte gib die Nummer des gewünschten Clubs ein.")           
            

def main_menu(manager):  
    '''
    Menü Anzeige und Benutzerauswahl abfrage.

    Args:
        manager (Manager): Manager-Objekt.
    '''  
    clubs = data.clubs
    opps = [club for club in clubs if club != manager._club]
    
    print(f"\nHallo, {manager.name}! Hier ist dein Büro bei {manager._club.name}.\n")
    print(f"Coach: {manager._club.coach.name}")
    print(f"Stimmung der Fans: {manager._club.fan_sentiment}")
    print(f"\nKader:\n ______________________ ")
    print(f"({manager._club.goalkeeper.position}) {manager._club.goalkeeper.number}. {manager._club.goalkeeper.name}")
    for player in manager._club.players:
        print(f"({player.position}) {player.number}. {player.name}")
        
    opp = random.choice(opps)    
    print("\nUnser nächstes Spiel:\n")
    print(f"{manager._club.name} vs. {opp.name} (s)")
    
    start_match = str(input("Tippe 's' um das die nächste Partie anzutreten: "))
    if start_match.lower() == 's':
        gameState.update_game_state('match_simulation', manager._club, opp, manager)
          
def match_simulation(team, opp, manager):
    '''
    Simuliert ein Match Spieler-Team und Gegner-Team.

    Args:
        team (Team): Spieler-Team.
        opp (Team): Gegner-Team.
        manager (Manager): Manager-Objekt.
    '''
    intro_text(team, opp)
    while True:
        if random_event(team, opp):
            break    
    gameState.update_game_state('main_menu', manager)
    
    
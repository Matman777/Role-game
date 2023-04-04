
from colorama import Fore, Style, Back
from random import randint
from game_mechanism import GameOverException
from game_mechanism import critical_hit, choice_1, choice_2, choice_3



my_life: int = 150
ennemy_life: int = 200
number_of_potions: int = 2
magician_help: int = 1
critical: int = 1
remaining_critical: int = critical


# introduction
rules = Fore.WHITE + Back.BLACK + Style.BRIGHT +'''\nBienvenue, Aventurier! Vous allez devoir affronter l'Orc qui se dresse sur votre route!
Vous avez 150 points de vie, l'Orc en a 200. \nDans votre sac à dos, vous avez 2 potions qui redonnent de 15 à 40 PV!
Attention, quand vous buvez une potion, vous passez votre prochain tour!
En cas de difficultés, invoquez le Mage! Mais il ne viendra qu'une seule fois..
⚔️  Bonne chance!⚔️\n''' + Style.RESET_ALL
print(rules)


while True:
    #print(f"Remaining critical: {remaining_critical}")
    
    # easter egg: si la vie du joueur est entre 1 et 7 points, on déclenche un coup critique de 50 dégâts
    if remaining_critical > 0:
        try:
            ennemy_life, remaining_critical = critical_hit(remaining_critical, my_life, ennemy_life)
        except GameOverException:
            "Vous assenez alors un coup critique de 50 dégâts! \n Bravo, vous l'avez vaincu !💪"
            

    # menu des choix qui apparaît après chaque action
    print("-" * 50)
    user_choice: str = input("\nQuelle action souhaitez-vous faire?\nAttaquer ⚔️  : 1 \nBoire une potion 🧪 : 2 \nInvoquer le Mage 👴 : 3 \n👉 Votre choix : ")
    print("-" * 50)
    if not user_choice.isdigit():
        continue
    user_choice = int(user_choice)


    # choix No 1 pour attaquer
    if user_choice == 1:
        try:
            ennemy_life, my_life = choice_1(ennemy_life, my_life)
        except GameOverException as e:
            print(e)
            input("Appuyez sur une touche pour quitter.")
            break


    # choix No 2 pour boire une potion
    if user_choice == 2:
        try:
            number_of_potions, ennemy_life, my_life = choice_2(number_of_potions, ennemy_life, my_life)
        except GameOverException:
            print("Malgré l'aide des potions, c'est une défaite..")
            input("Appuyez sur une touche pour quitter.")
            break
        

    # choix No 3 pour invoquer le mage
    if user_choice == 3:
        try:
             ennemy_life, magician_help = choice_3(magician_help, ennemy_life)
        except GameOverException:
            print("Bravo, vous l'avez vaincu !💪")
            input("Appuyez sur une touche pour quitter.")
            break

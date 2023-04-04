from random import randint
from colorama import Fore, Style, Back


class GameOverException(Exception): #pour déterminer la fin de jeu, et dans le script, on met un bloc try/except
     pass 


def critical_hit(critical: int, my_life: int, ennemy_life: int) -> int:
    if 0 < my_life <= 7:
        critical -= 1
        damages_to_ennemy = 50
        ennemy_life = ennemy_life - damages_to_ennemy
        print("-" * 50)
        if ennemy_life <= 0:
            raise GameOverException()
        else:
            print("Vous êtes en mauvaise posture et puisez dans vos dernières ressources...")
            print(f"Vous assenez alors un coup critique de 50 dégâts! \nIl reste {ennemy_life} points de vie à l'ennemi! \n Tenez bon!")
    return ennemy_life, critical

#--------------------------------------------------------------------------------------------------------------------------------------

def choice_1(ennemy_life, my_life):
        damages_to_myself: int = randint(10, 25)
        damages_to_ennemy: int = randint(10, 20)
        my_life: int = my_life - damages_to_myself
        ennemy_life: int = ennemy_life - damages_to_ennemy

        if ennemy_life <= 0:
            print(f"Vous avez infligé {damages_to_ennemy} points de dégâts à l'ennemi.")
            victory_message = "Bravo, vous l'avez vaincu !💪"
            raise GameOverException(victory_message)

        if my_life <= 0:
            print(f"Vous avez seulement infligé {damages_to_ennemy} points de dégâts à l'ennemi..")
            print(f"..Et l'ennemi, lui, vous en a infligé {damages_to_myself} 💘.")
            defeat_message = Fore.RED + Style.BRIGHT + Back.WHITE +"☠️  Vous avez été vaincu!☠️" + Style.RESET_ALL
            raise GameOverException(defeat_message)
            
        print(f"Vous avez infligé {damages_to_ennemy} points de dégâts à l'ennemi.")
        print(f"L'ennemi vous a infligé {damages_to_myself} points de dégâts.")
        print(f"Il vous reste {my_life} points de vie.")
        print(f"Il reste {ennemy_life} points de vie à l'ennemi.")
        return ennemy_life, my_life
#--------------------------------------------------------------------------------------------------------------------------------------

def choice_2(number_of_potions, ennemy_life, my_life ):
    if number_of_potions > 0:
        damages_to_myself: int = randint(5, 15)
        number_of_potions -= 1
        increase_life_with_potions: int = randint(15, 40)
        my_new_life: int = my_life + increase_life_with_potions - damages_to_myself
        print(f"Vous récupérez {increase_life_with_potions} points de vie 💓 ({number_of_potions} 🧪 restante(s))")
        print(f"L'ennemi vous a infligé {damages_to_myself} points de dégâts.")
        print(f"Il vous reste {my_new_life} points de vie.\n Il reste {ennemy_life} points de vie à l'ennemi. ")
        print("-" * 55)
        print("vous passez votre tour...")

        damages_to_myself: int = randint(5, 15)

        print(f"L'ennemi vous a infligé {damages_to_myself} points de dégâts.")
        print(f"Il reste {ennemy_life} points de vie à l'ennemi.")
        my_life = my_new_life - damages_to_myself
        if my_life <= 0:
             raise GameOverException()
        print(f"Il vous reste {my_new_life - damages_to_myself} points de vie.")
        return number_of_potions, ennemy_life, my_life
        
    else:
        print("Vous n'avez plus de potions...")
        return number_of_potions, ennemy_life, my_life

#--------------------------------------------------------------------------------------------------------------------------------------

def choice_3(magician_help: int, ennemy_life: int) -> int:
    if magician_help == 0:
        print("Le Mage a tout donné, il se repose..😴")
    elif magician_help > 0:
            magician_damages: int = randint(30, 60)
            if  ennemy_life <= 30:
                magician_help -= 1
                print(f"Le Mage vous vient en aide et inflige {magician_damages} points de dégâts à l'ennemi!")
                raise GameOverException()
            else:
                magician_help -= 1
                ennemy_life = ennemy_life - magician_damages
                print(f"Le Mage vous vient en aide et inflige {magician_damages} points de dégâts à l'ennemi!")
                print(f"Il reste alors {ennemy_life} points de vie à l'Orc,\n tenez bon!")
    return ennemy_life, magician_help

"""
gra w wisielca 

Author: Marcin Chruszcz 
email: chinek01@gmail.com
data: 2023-01-31

na podstawie dnia 07 z #100DaysOfCode with Python 
"""


import random as rnd 
import hangman_ui as ui 
from replit import clear

# przygotowanie listy haseł do odgadnięcia 

passwords = ['czarny', 'hasło', 'kamień', 'samochód', 'komputer', 'słownik', 
             'monitor', 'zwierzę', 'szafa', 'kapusta', 'gruszka', 'wiosło']

# określenie ilości żyć użytkownika 
user_lifes = 7
match_letters = 0

win_lose_falg = False

# losowanie hasła do zgadnięcia 
game_password = list(rnd.choice(passwords))
hidden_game_password = list(len(game_password) * '_')

while user_lifes > 0:

    # pobieranie od użytkownika liter 
    char = input("Podaj literę: ")
    
    clear()

    # print(''.join(game_password))

    match_flag = False

    # sprawdzenie czy dana litera występuje w haśle 
    for l in range(len(game_password)):
        if game_password[l] == char:
            hidden_game_password[l] = char
            match_flag = True   
            match_letters += 1         

    #  zabieranie życia użytkownika 
    if match_flag == False:
        user_lifes -= 1
        print(ui.lifes_stage[user_lifes])
        
    if match_letters == len(game_password):
        user_lifes = 0
        win_lose_falg = True

    print("Ilość żyć: " + user_lifes.__str__())
    print(''.join(hidden_game_password))

if win_lose_falg == True:
    print("Wygałeś :)")
    print("Hasło to " + ''.join(hidden_game_password))
else:
    print("Przegrałeś! :(")
    print("Hasło to " + ''.join(game_password))



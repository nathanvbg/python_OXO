# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: naverbru <naverbru@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/07/04 13:01:16 by naverbru          #+#    #+#              #
#    Updated: 2022/07/05 14:30:37 by naverbru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def player_input(table, str, sign):
    print("c'est a votre tour " + str)
    entree = list(map(int, input().split()))
    while (len(entree) != 2) or (entree[0] > 2) or (entree[0] < 0) or (entree[1] > 2) or (entree[1] < 0) or (table[entree[0]][entree[1]] != "_") :
        print("invalid input, it's still your turn " + str)
        entree = list(map(int, input().split()))
    table[entree[0]][entree[1]] = sign
    print_table(table)


def create_table():
    table = [['_','_','_'], ['_','_','_'], ['_','_','_']]
    return (table)

def print_table(table):
    print()
    print(*table[0])
    print(*table[1])
    print(*table[2])
    print()

def is_finished(table, str):
    if ((table[0][0] != '_') and (table[0][0] == table[0][1] == table[0][2]) or
    (table[1][0] != '_') and (table[1][0] == table[1][1] == table[1][2]) or
    (table[2][0] != '_') and (table[2][0] == table[2][1] == table[2][2]) or 
    (table[0][0] != '_') and (table[0][0] == table[1][1] == table[2][2]) or 
    (table[2][0] != '_') and (table[2][0] == table[1][1] == table[0][2]) or 
    (table[0][0] != '_') and (table[0][0] == table[1][0] == table[2][0]) or
    (table[0][1] != '_') and (table[0][1] == table[1][1] == table[2][1]) or
    (table[0][2] != '_') and (table[0][2] == table[1][2] == table[2][2])) :
        print("oyeee, " + str + " a gagné!")
        return(1)
    elif "_" not in table[0] and "_" not in table[1] and "_" not in table[2] :
        print("tie")
        return(1)
    return (0)

def play():
    table = create_table()
    print_table(table)
    while True :
        player_input(table, "joueur 1", "O")
        if (is_finished(table, "joueur 1") == 1) :
            break
        player_input(table, "joueur 2", "X")
        if (is_finished(table, "joueur 2") == 1) :
            break
        
if __name__ == '__main__':
    play()


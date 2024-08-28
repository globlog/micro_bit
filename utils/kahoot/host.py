from microbit import *

import radio

radio.config(group=137)
radio.on()


'''
    The protocol of a message is simply:
    sender:receiver:text
'''

id = 'HOST'

choice = 0
new_question = True

'''players = {id : {points : int, current_ans : int}'''

players = {}

def get_ranks(players):
    if players == {}:
        return []
    else:
        points_player = [[players[player]['points'],player] for player in players]
        points_player.sort(reverse = True)
        current_rank = 1
        current_points = points_player[0][0]
        ranks = []
        for entry in points_player:
            points, player = entry
            if points != current_points:
                current_rank += 1
                current_points = points
            ranks.append([current_rank, player])
        return ranks

while True:
    message = radio.receive()
    if message:
        sender, receiver, answer = message.split(':')
        if receiver == 'HOST':
            if sender in players:
                players[sender]['current_ans'] = int(answer)
            else:
                players[sender] = {'points' : 0, 'current_ans' : int(answer)}        
                
    if button_a.is_pressed():
        if new_question:
            choice = 0
            new_question = False
        choice = choice % 5 + 1
        if choice == 5:
            display.show('E')
        else:
            display.show(choice)
        sleep(300)

    if button_b.is_pressed():
        if choice == 5:
            ranks = get_ranks(players)
            for entry in ranks:
                rank, player = entry
                radio.send(id + ':' + player + ':' + 'Points ' + str(players[player]['points']) + ',Rank ' + str(rank))
        else:    
            for player in players:
                correct = players[player]['current_ans'] == choice
                players[player]['points'] += (1 if correct else 0)
                players[player]['current_ans'] = ''
            radio.send(id + ':' + '' + ':' + str(choice))
            new_question = True
            choice = 0
            display.clear()
    if button_a.is_pressed() and button_b.is_pressed():
        reset()

    
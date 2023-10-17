list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = 0
for i in list_players:
    count += 1
count = int(count/2)
print(list_players[:count], list_players[count:], sep='\n')

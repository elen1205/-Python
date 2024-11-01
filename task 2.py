def find_common_participants(str_1,str_2, splitter = ','):
    list_participants = str_1.split(splitter)
    second_list_participants = str_2.split(splitter)
    common_participants = list(set(list_participants).intersection(second_list_participants))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,splitter= '|'))
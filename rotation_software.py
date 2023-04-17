from random import random

########################################################################################################################

cleaning_position_names = open('position_names/cleaning_position_names.txt', encoding="utf-8")
down_position_names = open('position_names/down_position_names.txt', encoding="utf-8")
top_position_names = open('position_names/top_position_names.txt', encoding="utf-8")

cleaning_worker_name = open('rotation/cleaning_worker_name.txt', encoding="utf-8")
down_worker_name = open('rotation/down_worker_name.txt', encoding="utf-8")
top_worker_name = open('rotation/top_worker_name.txt', encoding="utf-8")
OFF_days_worker_name = open('rotation/OFF_days_worker_name.txt', encoding="utf-8")

########################################################################################################################

cleaning_position = dict()
down_position = dict()
top_position = dict()

OFF_days_copy = OFF_days_worker_name.readlines().copy()


########################################################################################################################


def remove_symbol(file) -> list:
    ready = []
    for i in file:
        ready.append(i.replace('\n', ''))
    return ready


def difference(work) -> list:
    return list(set(remove_symbol(work)).difference(set(remove_symbol(OFF_days_copy))))


########################################################################################################################

shuffled_cleaning_names = sorted(difference(cleaning_worker_name), key=lambda x: random())
shuffled_down_names = sorted(difference(down_worker_name), key=lambda x: random())
shuffled_top_names = sorted(difference(top_worker_name), key=lambda x: random())

########################################################################################################################


def program(slides, worker, array) -> dict:
    for i in range(len(slides)):
        array[slides[i].replace('\n', '')] = worker[i]

    print("---------------------------------------")
    print("↓ HOW MANY PEOPLE DON'T HAVE POSITION ↓")
    for i in worker[len(slides):]:
        print(i)
    print("---------------------------------------")

    return array


def view(ready_program):
    for p, w in ready_program.items():
        print(f"{p}: {w}")


########################################################################################################################


try:
    print("===========================================================================================================")
    print("↓ CLEANING PROGRAM ↓")
    view(program(cleaning_position_names.readlines(), shuffled_cleaning_names, cleaning_position))
    print("===========================================================================================================")
except IndexError:
    print("Add more worker in CLEANING worker list (file)")
    print("===========================================================================================================")

print()
print()

try:
    print("===========================================================================================================")
    print("↓ DOWN ROTATION PROGRAM ↓")
    view(program(down_position_names.readlines(), shuffled_down_names, down_position))
    print("===========================================================================================================")
except IndexError:
    print("Add more worker in DOWN worker list (file)")
    print("===========================================================================================================")

print()
print()

try:
    print("===========================================================================================================")
    print("↓ TOP ROTATION PROGRAM ↓")
    view(program(top_position_names.readlines(), shuffled_top_names, top_position))
    print("===========================================================================================================")
except IndexError:
    print("Add more worker in TOP worker list (file)")
    print("===========================================================================================================")

########################################################################################################################

cleaning_position_names.close()
down_position_names.close()
top_position_names.close()

cleaning_worker_name.close()
down_worker_name.close()
top_worker_name.close()
OFF_days_worker_name.close()

########################################################################################################################

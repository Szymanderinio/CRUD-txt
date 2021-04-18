import datetime

data = []

colors = {"black": "\033[0;37;40m", "white": "\033[0;37;47m",
          "yellow_txt": "\033[0;33;40m", "yellow_txt_bold": "\033[1;33;40m", "white_txt": "\033[0;37;40m",
          "white_txt_bold": "\033[1;37;40m", "red_txt_black_bgr": "\033[1;31;40m",
          "red_txt_white_bgr": "\033[1;31;47m", "blue_txt_black_bgr": "\033[1;36;40m",
          "blue_txt_white_bgr": "\033[1;36;47m", "green_txt": "\033[1;32;40m"}


def take_decision():
    decision = ""
    while decision is not int:
        try:
            decision = int(input())
            return decision
        except ValueError or SyntaxError:
            print("{}Not an integer!{}".format(colors["red_txt_black_bgr"], colors["white_txt"]))

    return decision


def load():
    file = open("data.txt", 'r', encoding='utf-8')
    for line in file:
        words = line.split(';')
        data.append({"id": int(words[0]), "name": words[1], "surname": words[2], "pesel": words[3]})
    file.close()


def print_data():
    for line in data:
        print(line)


def delete():
    print("Type the {}ID{} of entity you want to {}DELETE{}"
          .format(colors["yellow_txt_bold"], colors["white_txt"], colors["red_txt_black_bgr"], colors["white_txt"]))
    id_to_delete = take_decision()
    found = 0
    for entity in data:
        if entity["id"] == id_to_delete:
            found = 1
            data.remove(entity)
            break
    if found:
        print("Entity with given {}ID{} was {}DELETED{}"
              .format(colors["yellow_txt_bold"], colors["white_txt"], colors["red_txt_black_bgr"], colors["white_txt"]))
    else:
        print("{}Given {}ID{} not found!{}"
              .format(colors["red_txt_black_bgr"], colors["yellow_txt_bold"], colors["red_txt_black_bgr"],
                      colors["white_txt"]))


def update():
    print("Type the {}ID{} of entity you want to {}UPDATE{}"
          .format(colors["yellow_txt_bold"], colors["white_txt"], colors["yellow_txt_bold"], colors["white_txt"]))
    id_to_update = take_decision()
    found = 0
    for entity in data:
        if entity["id"] == id_to_update:
            found = 1
            entity["name"] = str(input("Type {}NAME{}: ".format(colors["yellow_txt_bold"], colors["white_txt"])))
            entity["surname"] = str(input("Type {}SURNAME{}: ".format(colors["yellow_txt_bold"], colors["white_txt"])))
            pesel = input("Type {}PESEL: ".format(colors["yellow_txt_bold"], colors["white_txt"]))
            while len(str(pesel)) != 11:
                print("{}PESEL{} has to be 11 digit long!{}".format(colors["yellow_txt_bold"],
                                                                    colors["red_txt_black_bgr"], colors["white_txt"]))
                pesel = input()
            entity["pesel"] = pesel
            print("{}Entity successfully {}UPDATED{}".format(colors["green_txt"], colors["yellow_txt_bold"],
                                                             colors["white_txt"]))
            break
    if not found:
        print("{}Entity with {}ID{} not found!{}"
              .format(colors["red_txt_black_bgr"], colors["yellow_txt_bold"], colors["red_txt_black_bgr"],
                      colors["white_txt"]))


def check_if_id_taken(id_to_check):
    for entity in data:
        if entity["id"] == id_to_check:
            return True
    return False


def create():
    while True:
        print("Type {}ID{} to add: ".format(colors["yellow_txt_bold"], colors["white_txt"]))
        id_to_add = take_decision()
        if not check_if_id_taken(id_to_add):
            break
        else:
            print("{}Given {}ID{} is taken!{}".format(colors["red_txt_black_bgr"],
                                                      colors["yellow_txt_bold"],
                                                      colors["red_txt_black_bgr"],
                                                      colors["white_txt"]))

    name = str(input("Type {}NAME{}: ".format(colors["yellow_txt_bold"], colors["white_txt"])))
    surname = str(input("Type {}SURNAME{}: ".format(colors["yellow_txt_bold"], colors["white_txt"])))
    pesel = input("Type {}PESEL{}: ".format(colors["yellow_txt_bold"], colors["white_txt"]))
    while len(str(pesel)) != 11:
        print("{}PESEL{} has to be 11 digit long!{}".format(colors["yellow_txt_bold"],
                                                            colors["red_txt_black_bgr"], colors["white_txt"]))
        pesel = input()
    data.append({"id": id_to_add, "name": name, "surname": surname, "pesel": pesel})
    print("{}Entity successfully CREATED{}".format(colors["green_txt"], colors["white_txt"]))


def count_gender():
    male = 0
    female = 0
    for entity in data:
        gender = int(entity["pesel"]) % 2
        if gender == 1:
            male += 1
        else:
            female += 1
    print("{}[{}]{} - FEMALES".format(colors["yellow_txt_bold"], female, colors["white_txt"]))
    print("{}[{}]{} - MALES".format(colors["yellow_txt_bold"], male, colors["white_txt"]))


def count_age():
    sum_of_age = 0
    entity_count = 0
    year = 0
    for entity in data:
        entity_count += 1
        pesel = []
        for cyfra in entity["pesel"]:
            pesel.append(cyfra)
        # print(pesel)

        month = pesel[2] + pesel[3]
        # print("miesiac {}".format(month))
        if int(month) <= 12:
            year = 1900
        elif int(month) >= 13:
            year = 2000
        rest_of_yearage = int(str(pesel[0])+str(pesel[1]))
        # print("rok {}".format(year))

        # print(datetime.date.today().year - (year + rest_of_yearage))
        # print("\n")
        sum_of_age += datetime.date.today().year - (year + rest_of_yearage)
    print("Average age of entities is {}{}{}".format(colors["yellow_txt_bold"],
                                                     sum_of_age//entity_count, colors["white_txt"]))


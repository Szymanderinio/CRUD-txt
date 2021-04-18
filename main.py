import crud
from crud import colors

data = None


def show_menu(skipFirst):
    if not skipFirst:
        print("Choose an {}option{} from below: ".format
              (colors["blue_txt_black_bgr"], colors["white_txt"])
              + "\n{}1{}) Load {}data.txt{} file".format(colors["yellow_txt"], colors["white_txt"], colors["green_txt"],
                                                         colors["white_txt"])
              + "\n{}2{}) {}Exit{} a program".format(colors["yellow_txt"], colors["white_txt"],
                                                     colors["red_txt_black_bgr"],
                                                     colors["white_txt"]))
    else:
        if load_data():
            print("\nChoose an {}option{} from below: ".format
                  (colors["blue_txt_black_bgr"], colors["white_txt"])
                  + "\n{}1{}) {}Create{} a new entity".format(colors["yellow_txt"], colors["white_txt"],
                                                              colors["green_txt"], colors["white_txt"])
                  + "\n{}2{}) {}Read{} entire data file".format(colors["yellow_txt"], colors["white_txt"],
                                                                colors["blue_txt_black_bgr"], colors["white_txt"])
                  + "\n{}3{}) {}Update{} an entity".format(colors["yellow_txt"], colors["white_txt"],
                                                           colors["yellow_txt_bold"], colors["white_txt"])
                  + "\n{}4{}) {}Delete{} an entity".format(colors["yellow_txt"], colors["white_txt"],
                                                           colors["red_txt_black_bgr"], colors["white_txt"])
                  + "\n{}5{}) Count age of entities".format(colors["yellow_txt"], colors["white_txt"])
                  + "\n{}6{}) Count females and males".format(colors["yellow_txt"], colors["white_txt"])
                  + "\n{}7{}) Go back".format(colors["yellow_txt"], colors["white_txt"]))


def load_data():
    try:
        global data
        data = open("data.txt", 'r', encoding='utf-8')
        data.close()
        return True
    except:
        return False


if __name__ == '__main__':
    print(colors["white_txt"])
    skipFirst = False
    secondMenu = False
    loaded = False
    while True:
        inner_decision = None
        if not secondMenu:
            show_menu(skipFirst)
            inner_decision = crud.take_decision()
            while inner_decision not in range(1, 3):
                print("{}There is no option like that!{}".format(colors["red_txt_black_bgr"], colors["white_txt"]))
                inner_decision = crud.take_decision()
        if inner_decision == 1 or secondMenu:
            if load_data():
                if not loaded:
                    crud.load()
                    loaded = True
                skipFirst = True
                show_menu(skipFirst)
                secondMenu = True

                inner_decision2 = crud.take_decision()

                while inner_decision2 not in range(1, 8) or None:
                    if inner_decision2 is None:
                        print("{}There is no option like that!{}".format(colors["red_txt_black_bgr"],
                                                                         colors["white_txt"]))
                    inner_decision2 = crud.take_decision()

                if inner_decision2 == 1:
                    crud.create()
                elif inner_decision2 == 2:
                    crud.print_data()
                elif inner_decision2 == 3:
                    crud.update()
                elif inner_decision2 == 4:
                    crud.delete()
                elif inner_decision2 == 5:
                    crud.count_age()
                elif inner_decision2 == 6:
                    crud.count_gender()
                elif inner_decision2 == 7:
                    skipFirst = False
                    secondMenu = False
            else:
                print("{}There was an error with loading a data file!{}"
                      .format(colors["red_txt_black_bgr"], colors["white_txt"]))

        if inner_decision == 2 and not secondMenu:
            break

#BUGGED

def display_health(object):

    display = "["

    hp = object.Hp
    mhp = object.MHp

    while True:
        if mhp - hp >= 10:
            display += "!"
        elif mhp - hp >= 1:
            display += "."
        else:
            break
    
    display += "]"

    print(display)
    print(hp, mhp)

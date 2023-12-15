def roll_call_dwarves(l):
    [print(f"{index+1}. {name}") for index, name in enumerate(l)]


def summon_captain_planet(l):
    return [f"{item.title()}!" for item in l]


def long_planeteer_calls(l):
    # for item in l:
    #     if len(item) > 4:
    #         return True
    # return False
    return any(len(item) > 4 for item in l)


def find_the_cheese(l):
    # for item in l:
    #     if item == "cheddar" or item == "gouda" or item == "camembert":
    #         return item
    # return None
    cheeses = ["cheddar", "gouda", "camembert"]

    for item in l:
        if item in cheeses:
            return item
    return None

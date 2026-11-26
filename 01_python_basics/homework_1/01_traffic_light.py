def traffic_light_if_else(color: str):
    if color == "red":
        print("зупинитися")
    elif color == "yellow":
        print("очікувати або підготуватися відповідно до навчальної моделі")
    elif color == "green":
        print("рух дозволено за умови безпеки")
    else:
        print("невідомий сигнал")


def traffic_light_match_case(color: str):
    match color:
        case "red":
            print("зупинитися")
        case "yellow":
            print("очікувати або підготуватися відповідно до навчальної моделі")
        case "green":
            print("рух дозволено за умови безпеки")
        case _:
            print("невідомий сигнал")

print("if - else")
traffic_light_if_else("green")

print("match - case")
traffic_light_match_case("wrong value")
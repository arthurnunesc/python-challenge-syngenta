def get_parsed_days(info_to_be_splitted):
    parsed_days = []
    day_of_the_week = []

    for each in info_to_be_splitted[1:]:
        day_of_the_week = each.split("(")
        day_of_the_week[1] = day_of_the_week[1].replace(")", "")
        parsed_days.append(day_of_the_week[1])

    return parsed_days


def get_cheapest_hotel(info):
    cheapest_hotel = "cheapest_hotel_name"

    weekdays = ["mon", "tues", "wed", "thur", "fri"]
    weekend = ["sat", "sun"]

    split_info = info.replace(":", ",")
    split_info = split_info.split(", ")

    lakewood = {
        "name": "Lakewood",
        "classification": 3,
        "normal_rate": 110,
        "reward_rate": 80,
        "weekend_normal_rate": 90,
        "weekend_reward_rate": 80,
        "total_cost": 0
    }
    bridgewood = {
        "name": "Bridgewood",
        "classification": 4,
        "normal_rate": 160,
        "reward_rate": 110,
        "weekend_normal_rate": 60,
        "weekend_reward_rate": 50,
        "total_cost": 0
    }
    ridgewood = {
        "name": "Ridgewood",
        "classification": 5,
        "normal_rate": 220,
        "reward_rate": 100,
        "weekend_normal_rate": 150,
        "weekend_reward_rate": 40,
        "total_cost": 0
    }

    if split_info[0] == "Regular":
        info_to_be_analysed = get_parsed_days(split_info)
        for day in info_to_be_analysed:
            if day in weekdays:
                lakewood["total_cost"] += lakewood["normal_rate"]
                bridgewood["total_cost"] += bridgewood["normal_rate"]
                ridgewood["total_cost"] += ridgewood["normal_rate"]
            elif day in weekend:
                lakewood["total_cost"] += lakewood["weekend_normal_rate"]
                bridgewood["total_cost"] += bridgewood["weekend_normal_rate"]
                ridgewood["total_cost"] += ridgewood["weekend_normal_rate"]
    elif split_info[0] == "Rewards":
        info_to_be_analysed = get_parsed_days(split_info)
        for day in info_to_be_analysed:
            if day in weekdays:
                lakewood["total_cost"] += lakewood["reward_rate"]
                bridgewood["total_cost"] += bridgewood["reward_rate"]
                ridgewood["total_cost"] += ridgewood["reward_rate"]
            elif day in weekend:
                lakewood["total_cost"] += lakewood["weekend_reward_rate"]
                bridgewood["total_cost"] += bridgewood["weekend_reward_rate"]
                ridgewood["total_cost"] += ridgewood["weekend_reward_rate"]

    if lakewood["total_cost"] < bridgewood["total_cost"] and lakewood["total_cost"] < ridgewood["total_cost"]:
        cheapest_hotel = lakewood["name"]
    elif bridgewood["total_cost"] < lakewood["total_cost"] and bridgewood["total_cost"] < ridgewood["total_cost"]:
        cheapest_hotel = bridgewood["name"]
    elif ridgewood["total_cost"] < lakewood["total_cost"] and ridgewood["total_cost"] < bridgewood["total_cost"]:
        cheapest_hotel = ridgewood["name"]
    elif ridgewood["total_cost"] == bridgewood["total_cost"] or ridgewood["total_cost"] == lakewood["total_cost"]:
        cheapest_hotel = ridgewood["name"]
    elif bridgewood["total_cost"] == lakewood["total_cost"]:
        cheapest_hotel = bridgewood["name"]

    return cheapest_hotel

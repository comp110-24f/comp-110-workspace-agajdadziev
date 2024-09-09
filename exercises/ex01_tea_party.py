"""Exercise 1: Tea Party"""

__author__ = "730691687"


def main_planner(guests: int) -> None:
    """Output All Information"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Tea Bags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Treats Needed"""
    return int((tea_bags(people=people) * 1.5))


# set return to an int


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of Treats and Tea"""
    return tea_count * 0.5 + treat_count * 0.75


# overcomplicated to call to results of past functions


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

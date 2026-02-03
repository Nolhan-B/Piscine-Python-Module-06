import alchemy.elements as e


def healing_potion() -> str:
    return (f"Healing potion brewed with {e.create_fire()} "
            f"and {e.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {e.create_earth()} "
            f"and {e.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {e.create_air()} "
            f"and {e.create_water()}")


def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements"
            f"{e.create_air()}, {e.create_earth()}, "
            f"{e.create_fire()}, {e.create_water()}")

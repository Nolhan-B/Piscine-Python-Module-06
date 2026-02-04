def validate_ingredients(ingredients: str) -> str:
    if any(e in ingredients for e in ("fire", "air", "earth", "water")):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

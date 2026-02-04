def validate_ingredients(ingredients: str) -> str:
	if any(param in ingredients for param in ("fire", "air", "earth", "water")):
		return f"{ingredients} - VALID"
	return f"{ingredients} - INVALID"

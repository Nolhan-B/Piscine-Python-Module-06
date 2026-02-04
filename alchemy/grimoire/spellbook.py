def record_spell(spell_name: str, ingredients: str) -> str:
	from .validator import validate_ingredients
	v_text = validate_ingredients(ingredients)
	if "- VALID" in v_text:
		return f"Spell recorded: {spell_name} ({v_text})"
	elif "- INVALID" in v_text:
		return f"Spell rejected: {spell_name} ({v_text})"
	else:
		return "Invalid parameters."
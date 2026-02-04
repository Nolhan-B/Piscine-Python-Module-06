from alchemy.grimoire import validator
from alchemy.grimoire import spellbook

def main() -> None:
	print("\n=== Circular Curse Breaking ===\n")

	print("Testing ingredient validation:")
	print("validate_ingredients(\"fire air\"):",
		  validator.validate_ingredients("fire air"))
	print("validate_ingredients(\"shadow\"):",
		  validator.validate_ingredients("shadow"))

	print("\nTesting spell recording with validation:")
	print("record_spell(\"fireball\",\"fire air\"):",
	      spellbook.record_spell("fireball", "fire air"))
	print("record_spell(\"Dark Magic\",\"shadow\"):",
	      spellbook.record_spell("Dark Magic", "shadow"))

	from alchemy.grimoire.spellbook import record_spell
	print("\nTesting late import technique:")
	print("record_spell(\"Lightning\",\"air\"):",
	      record_spell("Lightning", "air"))

	print("\nCircular dependency curse avoided using late imports!")
	print("All spells processed safely!")

if __name__ == "__main__":
	main()

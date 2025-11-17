glossary = {"red": 5, "green": 4, "blue": 3}
color = input("pick a color: ")
if (color.lower() in glossary.keys()):
    print(f'That is worth { glossary[color.lower()] }')
else:
    print(f"I don't know '{color}'.")
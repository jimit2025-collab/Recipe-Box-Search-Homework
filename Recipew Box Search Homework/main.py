RECIPES = [
    ("Pancakes", "mix flour eggs and milk then fry the batter in a pan"),
    ("Tomato Soup", "cook tomatoes with onion and salt then blend the soup"),
    ("Fruit Salad", "chop apple banana and mango and mix the fruit in a bowl"),
    ("Omelette", "beat eggs with salt and cook the eggs in a pan"),
    ("Cookies", "mix flour butter and sugar then bake the cookies"),
]
TEST_SEARCHES = [
    ("fry the batter", "Pancakes"),
    ("blend the soup", "Tomato Soup"),
    ("mango and apple", "Fruit Salad"),
    ("eggs in a pan", "Omelette"),
    ("butter and sugar", "Cookies"),
    ("cookie", "Cookies"),
]
def build_index(recipes):
    index = {}
    return index
INDEX = build_index(RECIPES)
print("PART 1: Index")
print(INDEX.get("eggs"), INDEX.get("pizza", "not found"))
def score(query):
    scores = {}
    return scores
print("\nPART 2: Score")
print(round(score("eggs in a pan").get(3, 0), 2))
def best_recipe(query):
    return "no match"
print("\nPART 3: Best recipe")
print(best_recipe("fry the batter"), "|", best_recipe("pizza"))
print("\nPART 4: Test all searches")
mistakes = 0
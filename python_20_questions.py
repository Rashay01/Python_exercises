# Q1
print("Q1")


students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]

# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.
sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)
for i, student in enumerate(sorted_students):
    student["rank"] = i + 1
print(sorted_students)

# =========================================================================================================================================
print()
print("Q2")
# Q2
# Setup Code
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]


merged_list = [{**x, **y} for x, y in zip(employees, salaries)]
print(merged_list)

# =========================================================================================================================================
print()
print("Q3")
# Q3
# Setup Code
products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.
# filtered_products = [
#     product
#     for product in products
#     if product["category"] == "Electronics" and product["price"] < 500
# ]
# print(filtered_products)

filtered_products = filter(
    lambda x: x["category"] == "Electronics" and x["price"] < 500, products
)
print(list(filtered_products))


# =========================================================================================================================================
print()
print("Q4")
# Q4
# Setup Code
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.


quattity_products = {}
for order in orders:
    for item in order["items"]:
        quattity_products[item["product"]] = (
            quattity_products.get(item["product"], 0) + item["quantity"]
        )

print(quattity_products)


# =========================================================================================================================================
print()
print("Q5")
# Q5
# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.

product_totals = {}
for transaction in transactions:
    product_totals[transaction["category"]] = (
        product_totals.get(transaction["category"], 0) + transaction["amount"]
    )

print(product_totals)


# =========================================================================================================================================
print()
print("Q6")
# Q6
# Setup Code
sales = [
    {"salesperson": "Alice", "amount": 200},
    {"salesperson": "Bob", "amount": 150},
    {"salesperson": "Alice", "amount": 100},
]
# Expected Task: Group sales by salesperson and calculate the total sales amount for each.

grouped_sales_data = {}
for sale in sales:
    grouped_sales_data[sale["salesperson"]] = (
        grouped_sales_data.get(sale["salesperson"], 0) + sale["amount"]
    )

print(grouped_sales_data)

# =========================================================================================================================================
print()
print("Q7")
# 7
# Setup Code
spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]
# Expected Task: Sort the spells list by power level in descending order using a lambda function.

sorted_spells = sorted(spells, key=lambda spell: spell[1], reverse=True)

print(sorted_spells)

# =========================================================================================================================================
print()
print("Q8")
# 8
# Setup Code
ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]
# Expected Task: Use `map` to append ": 3 grams" to each ingredient.

ingredients_3grams = map(lambda x: x + ": 3 grams", ingredients)

print(list(ingredients_3grams))

# =========================================================================================================================================
print()
print("Q9")
# 9
# Setup Code
books = [
    {"title": "A History of Magic", "pages": 100},
    {"title": "Magical Drafts and Potions", "pages": 150},
]
# Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

filtered_books = filter(lambda book: book["pages"] > 120, books)
book_names = map(lambda book: book["title"].upper(), filtered_books)
print(list(book_names))

# =========================================================================================================================================
print()
print("Q10")
# 10
# Setup Code
# Expected Task: Implement a class with methods for casting spells, reducing health points, and determining the winner.


class WizardDuel:
    heal = 10
    fireballl = 20

    def __init__(self, name):
        self.name = name
        self.health = 50

    def cast_spell(self, spell, target):
        if spell == "fireball":
            target.reducing_health_points(WizardDuel.fireballl)
        elif spell == "heal":
            self.health += WizardDuel.heal
            print(f"{self.name} healed now with {WizardDuel.heal} health points.")
        else:
            print("Invalid spell")

    def reducing_health_points(self, amount):
        self.health -= amount

    def determin_winner(self, target):
        if target.health <= 0:
            return f"After a duel between {self.name} and {target.name}, {self.name} wins with {self.health}  health points left."
        else:
            return f"{target.name} turn with {target.health} health points left."


harry = WizardDuel("Harry")
draco = WizardDuel("Draco")
harry.cast_spell("fireball", draco)
print(harry.determin_winner(draco))
draco.cast_spell("heal", harry)
print(draco.determin_winner(harry))
harry.cast_spell("fireball", draco)
print(harry.determin_winner(draco))
draco.cast_spell("fireball", harry)
print(draco.determin_winner(harry))
harry.cast_spell("fireball", draco)
print(harry.determin_winner(draco))

# =========================================================================================================================================
print()
print("Q11")
# 11
# Setup Code
# Expected Task: Define a `PotionError` exception and use it in a potion-making function.


class PotionError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "same ingredients cannot be mixed into a new potion"
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.value} error: {self.message}"


def potion_making(ingredient_1, ingredient_2):
    try:
        if ingredient_1 == ingredient_2:
            raise PotionError(ingredient_1)
        else:
            print(f"Mixing {ingredient_1} and {ingredient_2} will create a potion")
    except PotionError as e:
        print(e)


potion_making("frog", "grass")
potion_making("grass", "grass")

# =========================================================================================================================================
print()
print("Q12")
# 12
# Setup Code
library = [
    {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
    {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
]
# Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.

author = "Bathilda Bagshot"
books_by_author = [book for book in library if book["author"] == author]

print(books_by_author)

# =========================================================================================================================================
print()
print("Q13")
# 13
# Setup Code
house_points = [
    {"house": "Gryffindor", "points": 35},
    {"house": "Slytherin", "points": 50},
    {"house": "Gryffindor", "points": 60},
    {"house": "Slytherin", "points": 40},
]
# Expected Task: Aggregate points for each house and print the total.

total_house_points = {}
for house in house_points:
    total_house_points[house["house"]] = (
        total_house_points.get(house["house"], 0) + house["points"]
    )

output = ""
for house, points in total_house_points.items():
    output = output + f"{house} {points}, "

print(output[:-2])

# =========================================================================================================================================
print()
print("Q14")
# 14
# Setup Code
# Expected Task: Create a base class `MagicalCreature` and subclasses `Dragon`, `Unicorn`. Each subclass should have a unique `sound` method.


class MagicalCreature:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "unknown sound"


class Dragon(MagicalCreature):
    def sound(self):
        return "Roar"


class Unicorn(MagicalCreature):
    def sound(self):
        return "Neigh"


john = MagicalCreature("John")
print("John says:", john.sound())
draco = Dragon("Draco")
print("Draco says:", draco.sound())
unicorn = Unicorn("Unicorn")
print("Unicorn says:", unicorn.sound())

# =========================================================================================================================================
print()
print("Q15")
# 15
# Setup Code
artifacts = [
    {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
    {"name": "Elder Wand", "age": 1000, "power": 10},
    {"name": "Resurrection Stone", "age": 800, "power": 7},
]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.

sorted_artifacts = sorted(artifacts, key=lambda x: (x["age"], x["power"]))


print(sorted_artifacts)


# =========================================================================================================================================
print()
print("Q16")
# 16
# Setup Code
wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}
# Expected Task: Use an f-string to create a profile string that includes the wizard's name, title, and house.

# Expected Output: 'Albus Dumbledore, the Headmaster of Gryffindor.'


def profile(wizard):
    name, title, house = wizard.values()
    return f"{name}, the {title} of {house}."


print(profile(wizard))

# =========================================================================================================================================
print()
print("Q17")
# 17
# Setup Code
adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]
# Expected Task: Use `filter` and `map` to create a list of matches between adopters and creatures.

# [('Harry', 'Fawkes'), ('Hermione', 'Dobby')]


def isin(name):
    for tup in adopters:
        if tup[1] == name[1]:
            return name[1]


def get_matches(name):
    for tup in adopters:
        if tup[1] == name[1]:
            return (tup[0], name[0])


print(list(map(get_matches, filter(isin, creatures))))


# =========================================================================================================================================
print()
print("Q18")
# 18
# Setup Code
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

for i in range(len(ingredients) - 1):
    for j in range(i + 1, len(ingredients)):
        if i != j:
            print(
                f"Combining {ingredients[i]} and {ingredients[j]} produces a {ingredients[i]} {ingredients[j]} Potion."
            )

# =========================================================================================================================================
print()
print("Q19")
# 19
# Setup Code
data = [
    {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
    {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
    {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
]
# Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.


def add_tag(data):
    for item in data:
        if "tag1" in item["tags"]:
            item["tags"].append("tag4")


add_tag(data)

print(data)

# =========================================================================================================================================
print()
print("Q20")
# 20
# Setup Code
tasks = [
    {"id": 1, "priority": "High", "completed": False},
    {"id": 2, "priority": "Low", "completed": True},
    {"id": 3, "priority": "Medium", "completed": False},
    {"id": 4, "priority": "Low", "completed": False},
]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").


def priority_to_num(task):
    if task["priority"] == "High":
        return {**task, "priority": 1}
    elif task["priority"] == "Medium":
        return {**task, "priority": 2}
    else:
        return {**task, "priority": 3}


def num_to_priority(task):
    if task["priority"] == 1:
        return {**task, "priority": "High"}
    elif task["priority"] == 2:
        return {**task, "priority": "Medium"}
    else:
        return {**task, "priority": "Low"}


def sorted_tasks(tasks):
    ans = map(priority_to_num, tasks)
    sorted_tasks = sorted(ans, key=lambda x: (x["completed"], x["priority"]))
    return list(map(num_to_priority, sorted_tasks))


print(sorted_tasks(tasks))

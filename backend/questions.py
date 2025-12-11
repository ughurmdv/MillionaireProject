import random

EASY_QUESTIONS = [
    {"q": "What is the capital of France?", "a": ["Paris", "London", "Rome", "Berlin"], "correct": "Paris"},
    {"q": "What color is the sky on a clear day?", "a": ["Blue", "Green", "Red", "Yellow"], "correct": "Blue"},
    {"q": "How many legs does a spider have?", "a": ["6", "8", "10", "12"], "correct": "8"},
    {"q": "Which animal barks?", "a": ["Cat", "Dog", "Cow", "Sheep"], "correct": "Dog"},
    {"q": "What do bees produce?", "a": ["Honey", "Milk", "Water", "Wax"], "correct": "Honey"},
    {"q": "What is 2 + 2?", "a": ["3", "4", "5", "6"], "correct": "4"},
    {"q": "Which fruit is red?", "a": ["Apple", "Banana", "Grape", "Pear"], "correct": "Apple"},
    {"q": "Which planet do we live on?", "a": ["Mars", "Earth", "Venus", "Jupiter"], "correct": "Earth"},
    {"q": "How many days are in a week?", "a": ["5", "6", "7", "8"], "correct": "7"},
    {"q": "Which is a primary color?", "a": ["Purple", "Yellow", "Pink", "Black"], "correct": "Yellow"},
    {"q": "What do cows drink?", "a": ["Milk", "Water", "Juice", "Tea"], "correct": "Water"},
    {"q": "Which shape has 3 sides?", "a": ["Circle", "Square", "Triangle", "Hexagon"], "correct": "Triangle"},
    {"q": "What is the opposite of hot?", "a": ["Warm", "Cold", "Mild", "Cool"], "correct": "Cold"},
    {"q": "How many letters are in the English alphabet?", "a": ["24", "25", "26", "27"], "correct": "26"},
    {"q": "Which is a type of transport?", "a": ["Car", "Tree", "Rock", "House"], "correct": "Car"},
    {"q": "What color is a banana?", "a": ["Yellow", "Red", "Green", "Purple"], "correct": "Yellow"},
    {"q": "Which animal meows?", "a": ["Dog", "Cat", "Cow", "Horse"], "correct": "Cat"},
    {"q": "What do you breathe in?", "a": ["Smoke", "Air", "Dust", "Water"], "correct": "Air"},
    {"q": "What do plants need to grow?", "a": ["Sand", "Light", "Plastic", "Metal"], "correct": "Light"},
    {"q": "Which month comes after January?", "a": ["March", "February", "April", "May"], "correct": "February"},
]

MEDIUM_QUESTIONS = [
    {"q": "Which planet is known as the Red Planet?", "a": ["Mars", "Venus", "Earth", "Jupiter"], "correct": "Mars"},
    {"q": "Who invented the telephone?", "a": ["Newton", "Einstein", "Alexander Graham Bell", "Tesla"], "correct": "Alexander Graham Bell"},
    {"q": "How many continents are there?", "a": ["5", "6", "7", "8"], "correct": "7"},
    {"q": "Which ocean is the largest?", "a": ["Atlantic", "Indian", "Pacific", "Arctic"], "correct": "Pacific"},
    {"q": "Who wrote 'Romeo and Juliet'?", "a": ["Shakespeare", "Dickens", "Tolstoy", "Homer"], "correct": "Shakespeare"},
    {"q": "Which gas do plants absorb?", "a": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "correct": "Carbon Dioxide"},
    {"q": "How many bones are in an adult human body?", "a": ["206", "205", "201", "300"], "correct": "206"},
    {"q": "What is the square root of 64?", "a": ["6", "7", "8", "9"], "correct": "8"},
    {"q": "Which country invented pizza?", "a": ["France", "USA", "Italy", "Greece"], "correct": "Italy"},
    {"q": "Who painted the Mona Lisa?", "a": ["Van Gogh", "Picasso", "Da Vinci", "Michelangelo"], "correct": "Da Vinci"},
    {"q": "Which metal is liquid at room temperature?", "a": ["Iron", "Mercury", "Silver", "Gold"], "correct": "Mercury"},
    {"q": "Which organ pumps blood?", "a": ["Liver", "Heart", "Lungs", "Stomach"], "correct": "Heart"},
    {"q": "Which planet has rings?", "a": ["Saturn", "Mars", "Earth", "Venus"], "correct": "Saturn"},
    {"q": "What is H2O?", "a": ["Oxygen", "Hydrogen", "Water", "Salt"], "correct": "Water"},
    {"q": "Which is the fastest land animal?", "a": ["Lion", "Tiger", "Cheetah", "Horse"], "correct": "Cheetah"},
    {"q": "Which country hosted the 2016 Olympics?", "a": ["China", "Brazil", "Russia", "Japan"], "correct": "Brazil"},
    {"q": "What is the hardest natural substance?", "a": ["Gold", "Iron", "Diamond", "Silver"], "correct": "Diamond"},
    {"q": "Which instrument has keys, pedals and strings?", "a": ["Violin", "Drums", "Flute", "Piano"], "correct": "Piano"},
    {"q": "What is the boiling point of water at sea level?", "a": ["50°C", "75°C", "100°C", "150°C"], "correct": "100°C"},
    {"q": "What is the capital of Japan?", "a": ["Tokyo", "Osaka", "Kyoto", "Nagoya"], "correct": "Tokyo"},
]

HARD_QUESTIONS = [
    {"q": "Who developed the theory of relativity?", "a": ["Newton", "Tesla", "Einstein", "Bohr"], "correct": "Einstein"},
    {"q": "What is the powerhouse of the cell?", "a": ["Ribosome", "Nucleus", "Mitochondria", "Chloroplast"], "correct": "Mitochondria"},
    {"q": "What is the currency of Switzerland?", "a": ["Euro", "Swiss Franc", "Dollar", "Pound"], "correct": "Swiss Franc"},
    {"q": "Which element has the atomic number 1?", "a": ["Hydrogen", "Helium", "Oxygen", "Carbon"], "correct": "Hydrogen"},
    {"q": "What year did World War II end?", "a": ["1943", "1944", "1945", "1946"], "correct": "1945"},
    {"q": "Who discovered penicillin?", "a": ["Fleming", "Curie", "Thomas", "Edison"], "correct": "Fleming"},
    {"q": "How many moons does Mars have?", "a": ["1", "2", "3", "4"], "correct": "2"},
    {"q": "Which city is known as the City of Canals?", "a": ["Paris", "Venice", "Amsterdam", "Rome"], "correct": "Venice"},
    {"q": "What is the chemical symbol for Gold?", "a": ["Go", "Ag", "Au", "Gd"], "correct": "Au"},
    {"q": "Which desert is the largest?", "a": ["Gobi", "Sahara", "Kalahari", "Arabian"], "correct": "Sahara"},
    {"q": "What is the tallest mountain?", "a": ["K2", "Kangchenjunga", "Everest", "Makalu"], "correct": "Everest"},
    {"q": "What is the longest river?", "a": ["Amazon", "Nile", "Yangtze", "Mississippi"], "correct": "Nile"},
    {"q": "Who wrote 'The Odyssey'?", "a": ["Homer", "Virgil", "Plato", "Socrates"], "correct": "Homer"},
    {"q": "Which metal is mainly used in phone batteries?", "a": ["Copper", "Lithium", "Silver", "Iron"], "correct": "Lithium"},
    {"q": "Which scientist formulated the laws of motion?", "a": ["Einstein", "Newton", "Bohr", "Galileo"], "correct": "Newton"},
    {"q": "What is the largest internal organ of the human body?", "a": ["Liver", "Heart", "Lungs", "Kidneys"], "correct": "Liver"},
    {"q": "Which country has the most volcanoes?", "a": ["Japan", "Iceland", "Indonesia", "USA"], "correct": "Indonesia"},
    {"q": "What is the largest bone in the human body?", "a": ["Femur", "Humerus", "Skull", "Spine"], "correct": "Femur"},
    {"q": "What is considered the rarest blood type?", "a": ["A", "O", "AB-", "AB+"], "correct": "AB-"},
    {"q": "Who painted 'Starry Night'?", "a": ["Van Gogh", "Picasso", "Monet", "Rembrandt"], "correct": "Van Gogh"},
]


def _add_difficulty(q_list, diff):
    return [{**q, "difficulty": diff} for q in q_list]


def get_game_questions():
    """
    Returns 12 questions:
    - 4 easy (Q1–Q4)
    - 4 medium (Q5–Q8)
    - 4 hard (Q9–Q12)
    Each question has: q, a (answers), correct, difficulty.
    """
    selected = []
    selected += random.sample(_add_difficulty(EASY_QUESTIONS, "easy"), 4)
    selected += random.sample(_add_difficulty(MEDIUM_QUESTIONS, "medium"), 4)
    selected += random.sample(_add_difficulty(HARD_QUESTIONS, "hard"), 4)
    return selected


def get_random_question_by_difficulty(level: str):
    """
    For 'change question' lifeline: returns a single random question of given difficulty.
    """
    if level == "easy":
        return random.choice(_add_difficulty(EASY_QUESTIONS, "easy"))
    if level == "medium":
        return random.choice(_add_difficulty(MEDIUM_QUESTIONS, "medium"))
    if level == "hard":
        return random.choice(_add_difficulty(HARD_QUESTIONS, "hard"))
    raise ValueError("Invalid difficulty")

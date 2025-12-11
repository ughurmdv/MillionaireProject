import random

EASY_QUESTIONS = [
    {"q": "What is the capital of France?", "a": ["Paris", "London", "Rome", "Berlin"], "correct": "Paris"},
    {"q": "What color is the sky on a clear day?", "a": ["Blue", "Green", "Red", "Yellow"], "correct": "Blue"},
    {"q": "How many legs does a spider have?", "a": ["6", "8", "10", "12"], "correct": "8"},
    {"q": "What shape is a ball?", "a": ["Circle", "Square", "Triangle", "Rectangle"], "correct": "Circle"},
    {"q": "What color are most leaves?", "a": ["Blue", "Green", "Red", "Purple"], "correct": "Green"},
    {"q": "Which animal says 'moo'?", "a": ["Cow", "Dog", "Sheep", "Goat"], "correct": "Cow"},
    {"q": "How many days are in a weekend?", "a": ["1", "2", "3", "4"], "correct": "2"},
    {"q": "Which fruit is orange in color?", "a": ["Apple", "Orange", "Grape", "Banana"], "correct": "Orange"},
    {"q": "How many wheels does a bicycle have?", "a": ["1", "2", "3", "4"], "correct": "2"},
    {"q": "Which animal lives in water?", "a": ["Bird", "Fish", "Cat", "Dog"], "correct": "Fish"},
    {"q": "What helps you see?", "a": ["Eyes", "Ears", "Nose", "Mouth"], "correct": "Eyes"},
    {"q": "What season is the coldest?", "a": ["Summer", "Winter", "Spring", "Autumn"], "correct": "Winter"},
    {"q": "What do chickens lay?", "a": ["Eggs", "Stones", "Leaves", "Seeds"], "correct": "Eggs"},
    {"q": "How many legs does a cat have?", "a": ["2", "3", "4", "6"], "correct": "4"},
    {"q": "Which number comes after 4?", "a": ["3", "5", "6", "8"], "correct": "5"},
    {"q": "Which is used for writing?", "a": ["Pen", "Spoon", "Bottle", "Plate"], "correct": "Pen"},
    {"q": "Which animal is the largest?", "a": ["Mouse", "Dog", "Elephant", "Cat"], "correct": "Elephant"},
    {"q": "What color is fire?", "a": ["Blue", "Green", "Orange", "Purple"], "correct": "Orange"},
    {"q": "Which of these can fly?", "a": ["Cow", "Fish", "Bird", "Horse"], "correct": "Bird"},
    {"q": "Which is a hot drink?", "a": ["Tea", "Water", "Juice", "Milk"], "correct": "Tea"},
    {"q": "How many fingers are on one hand?", "a": ["3", "4", "5", "6"], "correct": "5"},
    {"q": "Which object tells time?", "a": ["Clock", "Chair", "Shoe", "Bag"], "correct": "Clock"},
    {"q": "What color is snow?", "a": ["White", "Blue", "Black", "Red"], "correct": "White"},
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
    {"q": "What is the largest mammal?", "a": ["Elephant", "Blue Whale", "Giraffe", "Hippo"], "correct": "Blue Whale"},
    {"q": "Which country is home to the kangaroo?", "a": ["India", "Australia", "Brazil", "USA"], "correct": "Australia"},
    {"q": "Which gas is essential for human breathing?", "a": ["Nitrogen", "Oxygen", "Carbon", "Hydrogen"], "correct": "Oxygen"},
    {"q": "Which country is known for the Great Pyramid?", "a": ["Greece", "Egypt", "Italy", "Spain"], "correct": "Egypt"},
    {"q": "Which planet has the strongest gravity?", "a": ["Earth", "Mars", "Jupiter", "Venus"], "correct": "Jupiter"},
    {"q": "Who wrote 'The Little Prince'?", "a": ["Saint-Exupéry", "Tolstoy", "Twain", "Hemingway"], "correct": "Saint-Exupéry"},
    {"q": "What is the largest desert?", "a": ["Sahara", "Arabian", "Gobi", "Kalahari"], "correct": "Sahara"},
    {"q": "How many teeth does an adult have?", "a": ["28", "30", "32", "34"], "correct": "32"},
    {"q": "Which instrument is played with a bow?", "a": ["Flute", "Guitar", "Violin", "Drums"], "correct": "Violin"},
    {"q": "Which continent is the smallest?", "a": ["Europe", "Australia", "Asia", "Africa"], "correct": "Australia"},
    {"q": "What does CPU stand for?", "a": ["Central Process Unit", "Central Processing Unit", "Computer Power Unit", "Control Processing Unit"], "correct": "Central Processing Unit"},
    {"q": "Which scientist discovered gravity?", "a": ["Newton", "Einstein", "Tesla", "Galileo"], "correct": "Newton"},
    {"q": "Which is the largest ocean?", "a": ["Indian", "Atlantic", "Pacific", "Arctic"], "correct": "Pacific"},
    {"q": "What is the square root of 49?", "a": ["5", "6", "7", "8"], "correct": "7"},
    {"q": "Where is the Eiffel Tower located?", "a": ["Rome", "Paris", "Madrid", "Berlin"], "correct": "Paris"},
    {"q": "Which animal is known as the King of the Jungle?", "a": ["Tiger", "Lion", "Leopard", "Wolf"], "correct": "Lion"},
    {"q": "What is the chemical symbol for Iron?", "a": ["Ir", "Fe", "In", "I"], "correct": "Fe"},
    {"q": "Who was the first man on the Moon?", "a": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Chris Hadfield"], "correct": "Neil Armstrong"},
    {"q": "What is the capital of Canada?", "a": ["Toronto", "Ottawa", "Montreal", "Vancouver"], "correct": "Ottawa"},
    {"q": "Which animal is the tallest?", "a": ["Elephant", "Giraffe", "Horse", "Camel"], "correct": "Giraffe"},
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
    {"q": "What is the largest artery in the human body?", "a": ["Aorta", "Carotid", "Femoral", "Pulmonary"], "correct": "Aorta"},
    {"q": "Which physicist discovered the electron?", "a": ["Bohr", "Thomson", "Rutherford", "Faraday"], "correct": "Thomson"},
    {"q": "Which country has the longest coastline?", "a": ["Russia", "Canada", "USA", "Australia"], "correct": "Canada"},
    {"q": "How many chromosomes do humans have?", "a": ["44", "46", "48", "50"], "correct": "46"},
    {"q": "What is the smallest country in the world?", "a": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"], "correct": "Vatican City"},
    {"q": "Who formulated the uncertainty principle?", "a": ["Heisenberg", "Bohr", "Dirac", "Planck"], "correct": "Heisenberg"},
    {"q": "Which gas forms the majority of Earth's atmosphere?", "a": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct": "Nitrogen"},
    {"q": "What is the most abundant metal in the Earth's crust?", "a": ["Iron", "Aluminum", "Copper", "Silver"], "correct": "Aluminum"},
    {"q": "Which mathematician proved Fermat's Last Theorem?", "a": ["Andrew Wiles", "Gauss", "Euler", "Turing"], "correct": "Andrew Wiles"},
    {"q": "Which planet rotates on its side?", "a": ["Neptune", "Uranus", "Jupiter", "Mars"], "correct": "Uranus"},
    {"q": "What is the deepest known point on Earth?", "a": ["Tonga Trench", "Mariana Trench", "Java Trench", "Puerto Rico Trench"], "correct": "Mariana Trench"},
    {"q": "Who is the author of '1984'?", "a": ["Orwell", "Huxley", "Bradbury", "Hemingway"], "correct": "Orwell"},
    {"q": "Which particle has a negative charge?", "a": ["Proton", "Neutron", "Electron", "Photon"], "correct": "Electron"},
    {"q": "What is the speed of light?", "a": ["150,000 km/s", "299,792 km/s", "500,000 km/s", "1,000,000 km/s"], "correct": "299,792 km/s"},
    {"q": "Which country has the most pyramids?", "a": ["Egypt", "Mexico", "Sudan", "Peru"], "correct": "Sudan"},
    {"q": "What is the rarest naturally occurring element?", "a": ["Francium", "Astatine", "Osmium", "Promethium"], "correct": "Astatine"},
    {"q": "Who discovered the circulation of blood?", "a": ["Harvey", "Pasteur", "Lister", "Fleming"], "correct": "Harvey"},
    {"q": "Which scientist discovered radioactivity?", "a": ["Curie", "Becquerel", "Rutherford", "Fermi"], "correct": "Becquerel"},
    {"q": "What is the second-largest moon in the solar system?", "a": ["Ganymede", "Titan", "Callisto", "Europa"], "correct": "Titan"},
    {"q": "Which ancient civilization built Machu Picchu?", "a": ["Inca", "Maya", "Aztec", "Egyptian"], "correct": "Inca"},
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

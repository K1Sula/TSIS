import random

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

random_film = random.randint(1,15)

#Exercie 1 
def movies_f(movie):
    if movie["imdb"] >= 5.5:
        return "True"
    return "False"

print(movies[random_film]["name"])
print(movies_f(movies[random_film]))

print()


#Exercise 2 find film over 5.5 imdb

film_level5_5 = []

def movies_f(movie):
    if movie["imdb"] >= 5.5:
        return True
    return False

for i in movies:
    if movies_f(i) == True:
        film_level5_5.append(i["name"])
    else:
        continue
print(film_level5_5, end = "\n")


#Esersices 3
film_levelcat = []
category_film = str(input("Write name of catefory = "))

def movies_f(category_film,movies):
    for i in movies:
        if i["category"]  == category_film:
            film_levelcat.append(i["name"])

movies_f(category_film,movies)
print(film_levelcat)

#Exercises 4
def movies_av(movies):
    avarage = 0
    for i in movies:
        avarage += i["imdb"]

    print(avarage / len(movies))

movies_av(movies)

#5
def calculate_average_imdb(category, movies):
    total_imdb_score = 0
    count = 0

    for movie in movies:
        if movie["category"] == category:
            total_imdb_score += movie["imdb"]
            count += 1

    if count == 0:
        return 0
    average_imdb = total_imdb_score / count
    return average_imdb

category_input = str(input("Write name of category: "))
average_imdb_score = calculate_average_imdb(category_input, movies)
print(f"Средний балл IMDB для категории {category_input}: {average_imdb_score}")
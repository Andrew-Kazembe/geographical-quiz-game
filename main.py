"""
Geographical Quiz Game
Author: Andrew Kazembe
Description:
A Python Turtle-based game for guessing
- African Countries
- Zambian Provinces
- Zambian Districts

"""
import random
import turtle
import pandas
my_screen = turtle.Screen()
my_screen.title("Welcome to the Geographical Quiz Game")
my_screen.setup(width=800, height=700)
image = "reception_pic.png"
my_screen.bgcolor("black")
my_screen.addshape(image)
turtle.shape(image)

def main_function():
    root = []
    user_level = my_screen.textinput(title="Choose Game Level",
                                      prompt="Enter 'easy' for Provinces, 'medium' for Countries,"
                                             " 'hard' for Districts:").lower()

    if user_level == "easy":
        file_directory = r".\zambian provinces.csv"
        root.append(file_directory)
        column_name = "Province"
        image = "zambian_provinces.png"
        title = "Zambian Provinces"


    elif user_level == "medium":
        file_directory = r".\African countries.csv"
        root.append(file_directory)
        column_name = "Country"
        image = "African_map.jpg"
        title = "African Countries"

    elif user_level == "hard":
        file_directory = r".\Zambia_Districts.csv"
        root.append(file_directory)
        column_name = "District"
        image = "ZambiaDistrictsBlank.gif"
        title = "zambian Districts"

    else:
        my_screen.bye()
        return

    data = pandas.read_csv(root[0]).to_dict(orient="records")
    data2 = pandas.read_csv(root[0])
    all_data = data2[column_name].to_list()
    my_screen.addshape(image)
    my_screen.title(title)
    turtle.shape(image)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    already_guessed = []


    while len(already_guessed) < len(all_data):
            user_guess = my_screen.textinput(title=f"{len(already_guessed)}/{len(all_data)}",
                                             prompt=f"whats the next {column_name}?").lower()
            colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

            if user_guess == "exit":
                missed_guessed = [geo for geo in all_data if geo not in already_guessed]
                new_data = pandas.DataFrame(missed_guessed)
                new_data.to_csv(f"{column_name}_to_learn.csv")
                exit()

            for item in data:
                if item[column_name].lower() == user_guess:
                    if item[column_name] not in already_guessed:
                        already_guessed.append(item[column_name])
                        x = item["Longitude"]
                        y = item["Latitude"]
                        writer.goto(x, y)
                        writer.dot(12, random.choice(colors))
                        writer.write(item[column_name], align="left", font=("Arial", 13, "bold"))


main_function()




my_screen.mainloop()
import pandas as pd

import os

# Absolute path of this script ("project.py"):
script_dir = os.path.dirname(os.path.abspath(__file__))

# "'results.csv' file with the same path (folder) of this srcipt:
file_path = os.path.join(script_dir, "results.csv")

print("\n----------------------------------------------")
print("Welcome to the Ecological Footprint Calculator")
print("----------------------------------------------")

# Function to ask questions
def ask_questions():

    print("\nAnswer the following questions:\n")

    transport = int(input("How many times per week do you use a car? "))
    meat = int(input("How many times per week do you eat meat? "))
    electricity = int(input("How many hours of electricity do you use per day? "))
    waste = int(input("How many trash bags do you produce per week? "))

    return transport, meat, electricity, waste


# Function to calculate score
def calculate_score(transport, meat, electricity, waste):

    score = (transport * 2) + (meat * 2) + electricity + (waste * 3)

    return score


# Function to classify impact
def classify_impact(score):

    if score < 20:
        level = "Low"
    elif score < 40:
        level = "Medium"
    else:
        level = "High"

    return level


# Function to give recommendations
def give_recommendations(level):

    print("\nRecommendations:")

    if level == "Low":
        print("Great job! Your ecological footprint is low.")
        print("Keep maintaining sustainable habits.")

    elif level == "Medium":
        print("Your ecological impact is moderate.")
        print("Try reducing car usage and eating less meat.")

    else:
        print("Your ecological footprint is high.")
        print("Consider using public transportation, reducing waste, and saving electricity.")


# Function to save results
def save_results(name, score, level):

    data = {
        "Name": [name],
        "Score": [score],
        "Impact Level": [level]
    }

    df = pd.DataFrame(data)

    try:
        old_data = pd.read_csv(file_path)
        new_data = pd.concat([old_data, df], ignore_index=True)
        new_data.to_csv(file_path, index=False)

    except (FileNotFoundError, pd.errors.EmptyDataError):
        df.to_csv(file_path, index=False)

    print(f"\nResults saved to {os.path.basename(file_path)}")


# Main program
def main():

    name = input("\nEnter your name: ")

    transport, meat, electricity, waste = ask_questions()

    score = calculate_score(transport, meat, electricity, waste)

    level = classify_impact(score)

    print("\nYour ecological footprint score is:", score)
    print("Impact Level:", level)

    give_recommendations(level)

    save_results(name, score, level)


# Loop so multiple users can try
while True:

    main()

    again = input("\nDo you want to calculate another footprint? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank you for using the Ecological Footprint Calculator!")
        break
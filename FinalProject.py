# The libraries we added upgrades our overall code. For example, the GUI library tkinter makes the program look visually good :)
import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox


# This window is were all the fun stuff happens! This is the visual way to portray the code.
window = tk.Tk()
window.title("Ecological Footprint Calculator")
window.geometry("520x660")


# This variables stores the user's infromation, so we can keep track of it!
name_var = tk.StringVar()
age_var = tk.StringVar()
transport_var = tk.StringVar()
meat_var = tk.StringVar()
electricity_var = tk.StringVar()
waste_var = tk.StringVar()


# We added this question to ask the user for their name and age, as it helps us keep track of their input and outcome.
instruction_label = tk.Label(
    window,
    text="Enter your name and age, then answer the questions below:",
    font=("Arial", 20)
)


# Here we ask for the user's name, as said previously, to keep track of their data.
instruction_label.pack(pady=5)
name_entry = tk.Entry(
    window,
    textvariable=name_var,
    font=("Arial", 14),
    width=30
)
name_entry.pack(pady=5)


# Same applies here from what is said in the last comment, but now with the age.
age_entry = tk.Entry(
    window,
    textvariable=age_var,
    font=("Arial", 14),
    width=10
)
age_entry.pack(pady=5)


# One of the questions we ask is their car usage, because cars emmit alarming amounts of C02, which is bad for the environment!
tk.Label(
    window,
    text="How many times per week do you use a car?",
    font=("Arial", 20)
).pack(anchor="w", padx=10)
car_entry = tk.Entry(
    window,
    textvariable=transport_var,
    font=("Arial", 20),
    width=10
)
car_entry.pack(pady=5)


# Another question we ask is about their meat consumption, as the production of meat is a major contributor to greenhouse gas emissions and deforestation!!
tk.Label(
    window,
    text="How many times per week do you eat meat?",
    font=("Arial", 20)
).pack(anchor="w", padx=10)
meat_entry = tk.Entry(
    window,
    textvariable=meat_var,
    font=("Arial", 20),
    width=10
)
meat_entry.pack(pady=5)


# Electricy as well is a contributor to greenhouse gas emissions, harming the enviroment.
tk.Label(
    window,
    text="How many hours of electricity do you use per day?",
    font=("Arial", 20)
).pack(anchor="w", padx=10)
electricity_entry = tk.Entry(
    window,
    textvariable=electricity_var,
    font=("Arial", 20),
    width=10
)
electricity_entry.pack(pady=5)


# Lastly, we ask about their waste production, as the more waste they produce, the more it harms the enviroment...
tk.Label(
    window,
    text="How many trash bags do you produce per week?",
    font=("Arial", 20)
).pack(anchor="w", padx=10)
waste_entry = tk.Entry(
    window,
    textvariable=waste_var,
    font=("Arial", 20),
    width=10
)
waste_entry.pack(pady=5)


# This is were the result are shown, so the user will know how they did.
output_label = tk.Label(
    window,
    text="",
    font=("Arial", 20),
    justify=tk.LEFT,
    fg="green",
    anchor="w"
)
output_label.pack(fill="x", padx=10, pady=15)


# This just makes sure that the user adds a valid number, negative hours don't exist!
def safe_int_input(answer, field_name):
    try:
        value = int(answer)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        messagebox.showerror(
            "Invalid input",
            f"Please enter a non-negative whole number for {field_name}.",
        )
        raise


# This is the storage of the user's answers, so we can use it to calculate their score!
# It's important to the overall program, as without it, the purpose of the calculator will be lost
def ask_questions():
    transport = safe_int_input(transport_var.get(), "times per week you use a car")
    meat = safe_int_input(meat_var.get(), "times per week you eat meat")
    electricity = safe_int_input(electricity_var.get(), "hours of electricity used per day")
    waste = safe_int_input(waste_var.get(), "trash bags produced per week")
    return transport, meat, electricity, waste


# This is the math part of the program
# Why are some factores multiplied by higher number? Because they have a bigger impact on the enviroment!
# And also for usage. We throw away way more things (and in a bigger capacity) than using a car, which we may not use everyday.
# So, we thought a way to make it even with every factor this way
def calculate_score(transport, meat, electricity, waste):
    score = (transport * 2) + (meat * 2) + electricity + (waste * 3)
    return score


# This is the user's ecological grade, so they can understand how they did in a more simple way, instead of just a number.
def classify_impact(score):
    if score < 20:
        level = "Low"
    elif score < 40:
        level = "Medium"
    else:
        level = "High"
    return level


# This are the recommendations! This is important, as a score without suggestions on how to improve is not very useful
# We want people to realize how much they are using and have an idea on how to reduce it, so the Earth can be a better place for us and future generations!
def give_recommendations(level):
    print("\nRecommendations:")
    if level == "Low":
        print("Great job! Your ecological footprint is low.")
        print("Keep maintaining sustainable habits.")
        return "Great job! Your ecological footprint is low.\nKeep maintaining sustainable habits."
    elif level == "Medium":
        print("Your ecological impact is moderate.")
        print("Try reducing car usage and eating less meat.")
        return "Your ecological impact is moderate.\nTry reducing car usage and eating less meat."
    else:
        print("Your ecological footprint is high.")
        print("Consider using public transportation, reducing waste, and saving electricity.")
        return "Your ecological footprint is high.\nConsider using public transportation, reducing waste, and saving electricity."


# This is the average score of all the users that have used the calculator
# With this, the user can compare their score to others and see how they are doing in a more general way.
def get_average_score():
    try:
        df = pd.read_csv("results.csv")
        return df["Score"].mean()
    except:
        return None


# This is the treasure chest of the program, where all the information is stored!
# This is important, because without it, we wouldn't be able to keep track of the user's data (and compare it to others!)
def save_results(name, age, score, level):
    data = {
        "Name": [name],
        "Age": [age],
        "Score": [score],
        "Impact Level": [level]
    }
    df = pd.DataFrame(data)
    filename = "results.csv"
    fallback = os.path.expanduser("~/results.csv")

    def try_save(dataframe, path):
        try:
            dataframe.to_csv(path, index=False)
            return True
        except OSError:
            return False

    try:
        old_data = pd.read_csv(filename)
        new_data = pd.concat([old_data, df], ignore_index=True)

        if not try_save(new_data, filename):
            if try_save(new_data, fallback):
                print(f"\nCould not write to '{filename}'. Saved results to '{fallback}' instead.")
                return
            raise OSError

    except (FileNotFoundError, pd.errors.EmptyDataError):
        if not try_save(df, filename):
            if try_save(df, fallback):
                print(f"\nCould not write to '{filename}'. Saved results to '{fallback}' instead.")
                return
            print("\nUnable to save results. Please run the program from a writable folder.")
            return

    except OSError:
        if try_save(df, fallback):
            print(f"\nCould not write to '{filename}'. Saved results to '{fallback}' instead.")
            return
        print("\nUnable to save results. Please run the program from a writable folder.")
        return

    print("\nResults saved to results.csv")


# This let's the user to retry again! Maybe they can lend it to a friend that can use it also!
# The cycle begins again and we store the new user's data
def reset_program():
    name_var.set("")
    age_var.set("")
    transport_var.set("")
    meat_var.set("")
    electricity_var.set("")
    waste_var.set("")
    output_label.config(text="")
    again_frame.pack_forget()
    name_entry.focus()

# Goodbye program! Maybe the user got bored... :( We hope they learned from the calculator!
def close_program():
    window.destroy()

# This is what we display to the users according to their input!
# It's very important to transmit errors or successes to the user, because this is how they recieve feedback from the program!
def main():
    while True:
        name = name_var.get().strip()
        age = age_var.get().strip()
        if not name or not age:
            messagebox.showerror("Missing information", "Both name and age are required, please try again.")
            return
        else:
            break

    try:
        transport, meat, electricity, waste = ask_questions()
    except ValueError:
        return

    score = calculate_score(transport, meat, electricity, waste)
    level = classify_impact(score)

    avg_score = get_average_score()
    comparison_text = ""
    if avg_score is not None:
        if score > avg_score:
            comparison_text = "\nYour score is ABOVE the average of previous users."
        else:
            comparison_text = "\nYour score is BELOW the average of previous users."

    recommendations_text = give_recommendations(level)

    output_label.config(
        text=(
            f"Your ecological footprint score is: {score}\n"
            f"Impact Level: {level}\n\n"
            f"{recommendations_text}"
            f"{comparison_text}"
        )
    )

    save_results(name, age, score, level)
    again_frame.pack(pady=(10, 5), before=calculate_button)


# The magic button that calculates everything we said previously!
calculate_button = tk.Button(
    window,
    text="Calculate Footprint",
    command=main,
    font=("Arial", 20),
)
calculate_button.pack(pady=5)

# This is the retry button, if the user's wants to, they can input another person's data!
again_frame = tk.Frame(window)

again_label = tk.Label(
    again_frame,
    text="Do you want to calculate a new footprint?",
    font=("Arial", 20),
)
again_label.pack(side="top", pady=(0, 5))

yes_button = tk.Button(
    again_frame,
    text="Yes",
    command=reset_program,
    font=("Arial", 20),
)
yes_button.pack(side="left", padx=10)

no_button = tk.Button(
    again_frame,
    text="No",
    command=close_program,
    font=("Arial", 20),
)
no_button.pack(side="right", padx=10)

# Get ready, start, go!
window.mainloop()

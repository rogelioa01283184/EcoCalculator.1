
 EcoCalculator

General Description
The main problem this project addresses is the lack of awareness about how daily consumption habits like  transportation, food, electricity, and waste impact the environment and contribute to climate change. Many people meake actions, without knowing, that cause  to overconsumption and environmental degradation.
This project provides a solution through an ecological footprint calculator developed in Python. The program allows users to input their daily habits, calculates a footprint score based on these inputs, then classifies the environmental impact level, and provides personalized recommendations. Additionally, it stores theuser data on a .csv to allow comparisons with previous results, helping users better understand their impact.



Setup and Execution Instructions

Requirements
-Python 3 installed on your computer
- Required libraries: pandas (for the data storage and analysis)

                      tkinter (for the graphical user interface; normally included with Python)
  

Install the required library by running:
-pip install pandas

Steps to Run

1-Copy or download this repository.

2-Open a terminal in the project folder.

3-Run the program 


Usage

-When the program runs, a graphical user interface (GUI) will open.   
-Enter your name, age, and answer the questions about your daily habits.   
-Click "Calculate Footprint" to see your results.    
-The program will display your score, impact level, and recommendations.
-Results are automatically saved in a results.csv file.


Summary of Implemented Features


-GUI: Collects data on transportation, meat consumption, electricity usage, and waste production.

-Score Calculation: Uses a  formula to estimate ecological impact.

-Impact Classification: Categorizes results into Low, Medium, or High impact levels.

-Personalized Recommendations: Provides feedback based on your score.

-Data Storage: Saves results in a CSV file using pandas.

-Data Comparison: Compares the user’s score with the average of previous users.

-Error Handling: Validates user input and prevents crashes by showing helpful error messages.



Technical Decisions and Design Choices


Libraries Used


-Tkinter: Chosen to build an userfriendly graphical interface, making the program easy to understand to every users.

-Pandas: Used to store, manage, and analyze user data in CSV format, including calculating the average scores.

-OS module: Implemented to ensure the program can safely handle file paths and save results 

Design Choices

-The program is structured using functions to separate responsibilities (one for inputs, calculations, data storage, and GUI interaction), making it clean and efficient.

-A scoring system is used to reflect the environmental impact of different activities (waste has a higher multiplier due to its long term effects).

-The GUI design prioritizes clarity 

Error Handling: -The program validates all numeric inputs to ensure they are non-negative integers.

                -If invalid data is entered, the program displays error messages instead of crashing.
                
                -File-saving errors are handled with a mechanism that stores data in the user’s home directory if needed.
                
Additional Considerations

-The pandas library must be installed before running the program.

-The results.csv file is automatically created if it does not exist.

-If the program does not have permission to write in the current folder, it will save the file in the user’s home directory to prevent data loss.

-The ecological footprint score is an estimation, not an exact scientific measurement, and is intended for educational purposes.


Video:[https://drive.google.com/drive/folders/1es5bZUjs4tlkRC6One446-DaWBg0HBoH?usp=sharing](https://drive.google.com/file/d/1Pqqr7Gl-62MZispO7mwJSEJj0Fr-5Qf0/view?usp=share_link)


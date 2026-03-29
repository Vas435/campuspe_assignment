#  Python Basics &  AI API Integrations

This repository contains two main projects: a collection of 20 foundational Python scripts built to practice core programming concepts, and a Generative AI API integration task that connects to multiple LLM providers.

---

##  Part 1: Python Basics (20 Mini-Projects)

A collection of 20 Python scripts focused on straightforward, functional code to practice loops, strings, conditionals, and standard library modules.

###  Scripts Overview
1. **Personal Bio Card**: Generates a formatted bio card using f-strings and space padding.
2. **Calculator**: A basic arithmetic calculator that safely handles division by zero.
3. **String Manipulator**: Formats user input (uppercase, title case, reversed) using built-in string methods.
4. **Age Calculator**: Uses the `datetime` module to calculate exact age, accounting for leap years.
5. **Bill Splitter**: Calculates total with tax and tip, then divides by the number of people.
6. **Grade Calculator**: Averages 5 subject scores and flags if a student failed an individual subject.
7. **Temperature Converter**: A `while`-loop menu that converts between Celsius, Fahrenheit, and Kelvin.
8. **Leap Year Checker**: Evaluates a year using compound boolean logic.
9. **Movie Tickets**: Calculates base ticket prices by age and applies weekend discounts.
10. **ATM Simulator**: An interactive menu tracking balance, enforcing minimums, and preventing overdrafts.
11. **Number Patterns**: Prints pyramids and mirrored grids using nested `for` loops.
12. **Multiplication Tables**: Generates a fully padded 10x10 grid.
13. **Sum and Average**: Calculates results for an arbitrary list of numbers using `sum()` and `len()`.
14. **Factorial**: Uses a backward loop to dynamically build and print the equation string.
15. **Prime Numbers**: An optimized prime checker and range finder.
16. **Guessing Game**: A 7-attempt game using the `random` module with "higher/lower" hints.
17. **Palindrome Checker**: Cleans input strings and checks for palindromes using slice reversal.
18. **Modular Calculator**: Separates operations into individual functions mapped via a dictionary.
19. **Text Analysis**: Counts vowels, finds the longest word, and calculates word frequencies.
20. **Number Systems Toolkit**: Menu-driven script for Fibonacci, GCD, Armstrong, and Perfect numbers.

**How to Run Part 1:**
Navigate to the directory and run: `python <filename>.py`

---

##  Part 2: AI API Integration - Gen AI Task

This section contains Python programs designed to send user prompts and retrieve AI-generated responses from 6 different Generative AI providers. Each script securely loads API keys via environment variables and handles potential API/HTTP errors gracefully.

###  Included Files
* `openai_example.py` (Connects to OpenAI)
* `groq_example.py` (Connects to Groq)
* `huggingface_example.py` (Connects to Hugging Face Inference Providers)
* `gemini_example.py` (Connects to Google Gemini)
* `cohere_example.py` (Connects to Cohere)
* `requirements.txt` (List of required Python packages)
* `screenshots/` (Contains screenshots of successful terminal executions)

###  Setup Instructions
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

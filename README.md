# CampusPe Python Basics Assignment

Welcome to my Python Basics Assignment repository! This project contains 20 foundational Python programming challenges. I wrote these scripts with a focus on clean, readable code and graceful error handling—because nobody likes a program that crashes when you accidentally divide by zero!

## The Projects

Here is a breakdown of what I built and the approach I took for each challenge:

1. **Personal Bio Card** *What it does:* Generates a nicely formatted, ASCII-style ID card for a student.  
   *The approach:* I used Python's f-strings and text alignment methods (like `<20`) to ensure the box borders stay perfectly rigid regardless of the input length.

2. **Simple Calculator** *What it does:* Takes two numbers and runs them through basic arithmetic operations.  
   *The approach:* Kept it simple but robust. I added inline conditional checks to catch division and modulo by zero so the program fails gracefully.

3. **String Manipulator** *What it does:* Slices and dices a user's sentence into various formats (uppercase, title case, reversed, etc.).  
   *The approach:* Heavily utilized Python's built-in string methods (`.split()`, `.replace()`, slicing `[::-1]`) to avoid writing overly complex manual loops.

4. **Age Calculator** *What it does:* Calculates a person's exact age in years, months, days, hours, and minutes.  
   *The approach:* Imported the `datetime` module to handle the heavy lifting of calendar math, accounting for leap years and exact date differences.

5. **Bill Splitter** *What it does:* Calculates the total cost of a restaurant bill, including tax and tip, and splits it evenly.  
   *The approach:* Modeled a real-world checkout process using standard float variables and formatted the final output to exactly two decimal places for currency accuracy.

6. **Grade Calculator** *What it does:* Averages scores from 5 subjects and assigns a letter grade.  
   *The approach:* Used a list to collect the marks dynamically, then applied an `if/elif` ladder to filter the percentage into the correct grade bracket. Added a quick check to ensure the student passed *all* individual subjects.

7. **Temperature Converter Menu** *What it does:* Converts temperatures between Celsius, Fahrenheit, and Kelvin.  
   *The approach:* Built an interactive, repeating `while` loop menu. The logic relies on straightforward mathematical formulas mapped to the user's menu choice.

8. **Leap Year Checker** *What it does:* Determines if a given year is a leap year and explains why.  
   *The approach:* Used logical operators (`and`, `or`) to perfectly translate the real-world rules of leap years (divisible by 4, but not 100, unless divisible by 400) into a single, clean `if` statement.

9. **Movie Ticket Pricing** *What it does:* Calculates ticket costs based on the customer's age and the day of the week.  
   *The approach:* Separated the logic into two steps: first establishing the base price using age brackets, then applying a boolean check to see if a weekend discount applies.

10. **ATM Simulator** *What it does:* A stateful banking menu allowing deposits, withdrawals, and balance checks.  
    *The approach:* Used an infinite `while True` loop to keep the ATM "open" until the user explicitly exits. Added safety checks to prevent overdrawing and to maintain a minimum required balance.

11. **Number Patterns** *What it does:* Prints various visually satisfying pyramids and grids of numbers.  
    *The approach:* Used nested `for` loops and the `range()` function. For the more complex mirroring patterns, I concatenated ascending and descending string sequences.

12. **Multiplication Tables** *What it does:* Generates custom math tables and a full 10x10 grid.  
    *The approach:* Used simple loops for the basic table, and list comprehensions with string padding (`:4`) to ensure the 10x10 grid aligns perfectly into columns.

13. **Sum & Average Math** *What it does:* Takes an arbitrary amount of numbers and calculates key statistics.  
    *The approach:* Instead of manual tracking, I appended all inputs to a list and let Python's powerful built-in functions (`sum()`, `max()`, `min()`) do the work.

14. **Factorial Loop** *What it does:* Calculates the factorial of a number and shows the math step-by-step.  
    *The approach:* Implemented a reverse `for` loop to step backward from the target number down to 1, building a visual string of the equation alongside the actual math.

15. **Prime Number Logic** *What it does:* Checks if a number is prime and finds all primes within a specific range.  
    *The approach:* Optimized the prime-checking algorithm by only looping up to the square root of the number (`int(num**0.5) + 1`), which makes it significantly faster for large inputs.

16. **Number Guessing Game** *What it does:* An interactive game where the user tries to guess a randomly generated number within 7 attempts.  
    *The approach:* Imported the `random` module. Added "Too high" and "Too low" feedback logic, and included a hint feature that triggers if the guess is within 5 digits of the answer.

17. **Palindrome Checker** *What it does:* Checks if a word or number reads the same forwards and backwards.  
    *The approach:* Sanitized the input first by removing spaces and forcing lowercase, then compared it directly against its sliced reverse (`[::-1]`).

18. **Modular Calculator** *What it does:* A menu-driven calculator, completely reorganized using functions.  
    *The approach:* Abstracted each math operation into its own dedicated function. Used a dictionary to map the user's menu choice directly to the corresponding function for cleaner code.

19. **Text Analysis Engine** *What it does:* A comprehensive tool that counts vowels, finds the longest word, and builds frequency maps of text.  
    *The approach:* Built a suite of specialized, single-purpose functions. Used dictionary `get()` methods for efficient word frequency counting and list comprehensions for quick vowel filtering.

20. **Number Systems Toolkit** *What it does:* A massive toolkit of mathematical functions (Fibonacci, GCD, Armstrong numbers) wrapped in a user menu.  
    *The approach:* Mixed Python's built-in `math` library (for GCD and factorials) with custom algorithmic logic (for Armstrong and perfect numbers) to create a highly modular and testable script.

## 🛠️ How to Run

You don't need any special libraries outside of standard Python! 

1. Ensure you have Python installed (`python --version`).
2. Clone this repository or download the files.
3. Open your terminal/command prompt.
4. Run any file using the `python` command. 

For example:
```bash
python <filename>.py
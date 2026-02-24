# CampusPe Python Basics Assignment

This assignment was all about getting the basics of Python down, you know, like loops and strings and stuff. I ended up building these 20 little scripts, and honestly, it felt good to see them actually run without too many bugs. I tried to keep the code pretty straightforward, nothing fancy, because I am not some pro coder yet. The whole thing is in this repo, just a bunch of .py files that I threw together over a couple weeks.

Starting with the personal bio card thing.  I used f strings to format it, and padded things with spaces so the borders did not mess up if the name was long. It seems simple, but it took a few tries to get the alignment right. Then there is the calculator, super basic, just adds, subtracts, multiplies, divides two numbers you type in. I added checks for dividing by zero, because that would crash everything otherwise, and I hate error messages popping up out of nowhere.

The string manipulator was fun, I guess. You input a sentence, and it spits out versions like all uppercase or reversed or title case. I leaned on those built in methods a lot, like split and slice with negative steps, instead of writing my own loops, which probably would have been a mess. Age calculator came next, that one pulls in the datetime module to figure out exact age down to minutes, handling leap years and all. I think it works okay, but dates can be tricky if you input something weird.

Bill splitter feels practical, like for when you go out with friends. It adds tax and tip to the total, then divides by how many people. I used floats and rounded to two decimals for money stuff, which made sense. Grade calculator averages five subject scores and gives a letter, but I also checked if any single one failed, because passing all matters more than just the average sometimes. That if elif chain was straightforward, though.

Temperature converter has this menu that loops until you quit, switching between C, F, K with some math formulas. I kept the while loop going with user input, nothing too complicated. Leap year checker explains the rules, like divisible by four but not a hundred unless four hundred, all in one if statement with ands and ors. It seems accurate, I tested a few years like 2000 and 1900.

Movie tickets base price on age, then discounts for weekends, two steps basically. ATM simulator is more involved, infinite loop for menu, tracks balance, stops you from overdrawing. I added a minimum balance check, which felt like a real ATM thing. Number patterns print pyramids and grids with nested fors, concatenating strings for the mirrors, that part got a bit fiddly.

Multiplication tables, simple loops for one number, then list comps for the full ten by ten, padded to line up. Sum and average takes as many numbers as you want, lists them up and uses sum and len built ins, easy. Factorial shows steps backward in a loop, building the product as it goes, with a string for the equation.

Prime numbers, I check up to square root to speed it up, and find all in a range too. Guessing game uses random, gives hints if close, limits attempts to seven. Palindrome cleans input to lower no spaces, then compares to reverse slice.

Modular calculator breaks operations into functions, dictionary maps choices to them, cleaner that way. Text analysis counts vowels, longest word, word frequencies with dicts and comprehensions. Number systems toolkit has a menu for fib, gcd from math module, armstrong checks, perfect numbers, all modular.

To run any of this, just need Python, no extras. Type python filename.py in terminal, that is it.

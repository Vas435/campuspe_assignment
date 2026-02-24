def count_words(text): return len(text.split())
def count_vowels(text): return sum(1 for c in text.lower() if c in 'aeiou')
def count_consonants(text): return sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
def reverse_text(text): return text[::-1]
def is_palindrome(text): 
    clean = ''.join(c.lower() for c in text if c.isalpha())
    return clean == clean[::-1]
def remove_vowels(text): return ''.join(c for c in text if c.lower() not in 'aeiou')
def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq
def longest_word(text):
    words = text.split()
    longest = max(words, key=len) if words else ""
    return f"{longest} ({len(longest)} letters)"

def analyze_text(text):
    print("\nTEXT ANALYSIS")
    print(f"Words: {count_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    print(f"Reversed: {reverse_text(text)}")
    print(f"Palindrome: {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels: {remove_vowels(text)}")
    print(f"Longest word: {longest_word(text)}")
    freq_str = ", ".join(f"{k}: {v}" for k, v in word_frequency(text).items())
    print(f"Word Frequency: {freq_str}")

analyze_text(input("Enter text: "))
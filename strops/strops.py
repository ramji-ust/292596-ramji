import string
import itertools

def getspan(s, ss):
    """Find the start and end indices of a substring in a string."""
    trimmed_s = s.strip()  # Remove leading/trailing spaces
    start = trimmed_s.find(ss)
    if start == -1:
        return None  # Substring not found
    return (start, start + len(ss))

def reverseWords(s):
    """Reverse the words in a sentence."""
    return ' '.join(s.split()[::-1])

def removePunctuation(s):
    """Remove punctuation from a string."""
    return s.translate(str.maketrans('', '', string.punctuation))

def countWords(s):
    """Count the number of words in a string."""
    return len(s.split())

def charecterMap(s):
    """Return a dictionary with character frequencies."""
    return {char: s.count(char) for char in set(s)}

def makeTitle(s):
    """Convert a string to title case."""
    return s.title()

def normalizeSpaces(s):
    """Replace multiple spaces with a single space."""
    return ' '.join(s.split())

def transform(s):
    """Custom transformation (example: lowercase and remove spaces)."""
    return s.lower().replace(' ', '')

def getPermutations(s, limit=10):
    """Return up to 'limit' unique permutations of a string."""
    return list(set(''.join(p) for p in itertools.permutations(s)))[:limit]

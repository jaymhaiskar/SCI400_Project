import re
from collections import Counter
import math

def clean_text(text):
    """Remove filler words and punctuation from text."""
    filler_words = {  "a", "an", "the", "and", "or", "but", "if", "while", "of", "at", "by",
    "for", "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "can", "will",
    "just", "don", "should", "now", "is", "am", "are", "was", "were", "be",
    "been", "being", "do", "does", "did", "having", "have", "has", "had"}  # you can expand this set
    # Remove punctuation
    text = re.sub(r"[.,;!?]", "", text)
    # Split into words
    words = text.lower().split()
    # Remove filler words
    return " ".join(word for word in words if word not in filler_words)

def text_to_set(text):
    """Convert a paragraph into a set of lowercase words (cleaned)."""
    text = clean_text(text)
    words = re.findall(r"\b\w+\b", text.lower())
    return set(words)

def text_to_counter(text):
    """Convert a paragraph into a word frequency counter (cleaned)."""
    text = clean_text(text)
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words)

def jaccard_similarity(text1, text2):
    """Compute Jaccard similarity between two texts."""
    set1 = text_to_set(text1)
    set2 = text_to_set(text2)
    
    intersection = set1 & set2
    union = set1 | set2
    
    if not union:
        return 0.0
    return len(intersection) / len(union)

def cosine_similarity(text1, text2):
    """Compute Cosine similarity between two texts."""
    counter1 = text_to_counter(text1)
    counter2 = text_to_counter(text2)
    
    # Find common words
    common = set(counter1.keys()) & set(counter2.keys())
    
    # Dot product
    dot_product = sum(counter1[word] * counter2[word] for word in common)
    
    # Magnitudes
    mag1 = math.sqrt(sum(v**2 for v in counter1.values()))
    mag2 = math.sqrt(sum(v**2 for v in counter2.values()))
    
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot_product / (mag1 * mag2)

# Example usages
para1 = "The park board approved the event months ago in a private meeting, despite it only being announced last week. Most commissioners are not interested in revisiting the decision, except Green Party commissioner Tom Digby.RCMP confirmed the suspect, the womans brother, is also dead. The victims ages range from 18 to 60."
para2 = "The park board announced an event that was approved months ago in a private, in-camera meeting. A majority of commissioners, with the exception of Green Party commissioner Tom Digby, showed little interest in revisiting the decision."

print(f"Jaccard Similarity: {jaccard_similarity(para1, para2):.3f}")
print(f"Cosine Similarity: {cosine_similarity(para1, para2):.3f}")

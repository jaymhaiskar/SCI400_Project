import re
from collections import Counter
import math

def text_to_set(text):
    """Convert a paragraph into a set of lowercase words."""
    words = re.findall(r"\b\w+\b", text.lower())
    return set(words)

def text_to_counter(text):
    """Convert a paragraph into a word frequency counter."""
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
para1 = "An 18-year-old woman was killed and seven others were injured in multiple stabbings in the Hollow Water First Nation. RCMP confirmed the suspect, the woman's brother, is also dead. The victims' ages range from 18 to 60."
para2 = "an 18 year old woman was killed and her brother the suspect also died after a stabbing in hollow water first nation. seven others aged 18 to 60 were injured in the early morning attacks according to manitoba rcmp."


print(f"Jaccard Similarity: {jaccard_similarity(para1, para2):.3f}")
print(f"Cosine Similarity: {cosine_similarity(para1, para2):.3f}")





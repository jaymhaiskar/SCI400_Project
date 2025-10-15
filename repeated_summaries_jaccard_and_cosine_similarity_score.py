import re
from collections import Counter
import math
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Text cleaning & similarity functions
# ---------------------------
def clean_text(text):
    filler_words = {
        "a","an","the","and","or","but","if","while","of","at","by","for","with",
        "about","against","between","into","through","during","before","after",
        "above","below","to","from","up","down","in","out","on","off","over",
        "under","again","further","then","once","here","there","when","where",
        "why","how","all","any","both","each","few","more","most","other","some",
        "such","no","nor","not","only","own","same","so","than","too","very",
        "can","will","just","don","should","now","is","am","are","was","were",
        "be","been","being","do","does","did","having","have","has","had"
    }
    text = re.sub(r"[.,;!?]", "", text or "")
    words = text.lower().split()
    return " ".join(word for word in words if word not in filler_words)

def text_to_set(text):
    # print("def text to set reached", set(re.findall(r"\b\w+\b", clean_text(text).lower())))
    return set(re.findall(r"\b\w+\b", clean_text(text).lower()))

def text_to_counter(text):
    # print("def text to counter reached")
    return Counter(re.findall(r"\b\w+\b", clean_text(text).lower()))

def jaccard_similarity(text1, text2):
    # print("def jaccard reached")
    set1, set2 = text_to_set(text1), text_to_set(text2)
    if set1 and set2:
        # print("inside if statement")
        return len(set1 & set2) / len(set1 | set2)

def cosine_similarity(text1, text2):
    # print("def cosine reached")
    counter1, counter2 = text_to_counter(text1), text_to_counter(text2)
    common = set(counter1) & set(counter2)
    dot_product = sum(counter1[w] * counter2[w] for w in common)
    mag1 = math.sqrt(sum(v**2 for v in counter1.values()))
    mag2 = math.sqrt(sum(v**2 for v in counter2.values()))
    if mag1 and mag2:
        return dot_product / (mag1 * mag2)
                                                            
# ---------------------------
# Fetch data from DB
# ---------------------------
conn = sqlite3.connect("articles.db")  # your DB file
cursor = conn.cursor()
cursor.execute("""
    SELECT ChatGPT_repeated_summaries
    FROM repeated_summaries
    WHERE ChatGPT_repeated_summaries IS NOT NULL
    ORDER BY id
""")
rows = cursor.fetchall()
conn.close()

# Flatten to list
summaries = [r[0] for r in rows]
# print(summaries)

# ---------------------------
# Compute similarities
# ---------------------------
results = []
if len(summaries) > 1:
    base = summaries[0]
    # print(base)
    for i in range(1, len(summaries)):
        jaccard = jaccard_similarity(base, summaries[i])
        print(jaccard)
        # print("jaccard reached", jaccard)
        cosine = cosine_similarity(base, summaries[i])
        results.append((f"1 vs {i+1}", round(jaccard, 3), round(cosine, 3)))

# ---------------------------
# Save to CSV
# ---------------------------
df = pd.DataFrame(results, columns=["Comparison", "Jaccard", "Cosine"])
print(df)

df.to_csv("ChatGPT_Repeated_Similarity.csv", index=False)
print("✅ Saved as Gemini_Repeated_Summaries.csv")

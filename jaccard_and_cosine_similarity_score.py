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
    return set(re.findall(r"\b\w+\b", clean_text(text).lower()))

def text_to_counter(text):
    return Counter(re.findall(r"\b\w+\b", clean_text(text).lower()))

def jaccard_similarity(text1, text2):
        set1, set2 = text_to_set(text1), text_to_set(text2)
            if not set1 or not set2:
                    return 0.0
                        return len(set1 & set2) / len(set1 | set2)

def cosine_similarity(text1, text2):
    counter1, counter2 = text_to_counter(text1), text_to_counter(text2)
    common = set(counter1) & set(counter2)
    dot_product = sum(counter1[w] * counter2[w] for w in common)
    mag1 = math.sqrt(sum(v**2 for v in counter1.values()))
    mag2 = math.sqrt(sum(v**2 for v in counter2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
        return dot_product / (mag1 * mag2)
                                                            
# ---------------------------
# Fetch data from DB
# ---------------------------
conn = sqlite3.connect("articles.db")  # change to your db
cursor = conn.cursor()
cursor.execute("SELECT id, Gemini_Summaries, ChatGPT_Summaries FROM articles where ChatGPT_Summaries is not null")
rows = cursor.fetchall()
conn.close()

# ---------------------------
# Compute similarities
# ---------------------------
results = []
for row in rows:
    article_id, chatgpt_sum, gemini_sum = row
    if chatgpt_sum and gemini_sum:
        jaccard = jaccard_similarity(chatgpt_sum, gemini_sum)
        cosine = cosine_similarity(chatgpt_sum, gemini_sum)
        results.append((article_id, round(jaccard, 3), round(cosine, 3)))
    else:
        results.append((article_id, None, None))

# Put into DataFrame
df = pd.DataFrame(results, columns=["Article ID", "Jaccard", "Cosine"])

print(df)

# ---------------------------
# Save table as PNG
# ---------------------------
# fig, ax = plt.subplots(figsize=(8, len(df) * 0.5 + 1))
# ax.axis("off")
# table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")

# table.auto_set_font_size(False)
# table.set_fontsize(10)
# table.scale(1.2, 1.2)

# plt.tight_layout()
# plt.savefig("ChatGPT-Grok-articles-similarity.png", dpi=300)
# plt.close()


#----- Save Table as CSV -------------------------------
df.to_csv("Gemini-ChatGPT-articles-similarity.csv", index=False)

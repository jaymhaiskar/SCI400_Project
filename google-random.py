from google import genai
import sqlite3

# # client = genai.Client(api_key=)
# client = genai.Client()
# # Connect to database
# conn = sqlite3.connect("articles.db")
# cursor = conn.cursor()
# print("connection opened")

# # Select articles where ChatGPT_Summaries is still empty

# cursor.execute("SELECT id, prompt FROM articles LIMIT 20")
# articles = cursor.fetchall()
# print("articles fetched")


# for article_id, prompt in articles:
#     print("in for loop")
#     try:
        
#         #ERROR
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents="Explain how AI works in a few words"
#         )

#         summary = response.output_text.strip()
        

#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

# print("connection closed")
# conn.close()

#---------------------------- from Gemini ------------------------------------

# import os
# from google import genai
# from google.genai import types


# 1. Initialize the client using the API key
# try:
#     # Passing the key explicitly is shown here for clarity, 
#     # but setting the environment variable is often cleaner.
#     client = genai.Client(api_key=API_KEY)
# except Exception as e:
#     print(f"Error initializing Gemini client: {e}")
#     exit()


# # 2. Define the user prompt and the model
# MODEL_NAME = "gemini-2.5-pro"
# PROMPT = (
#     "Write a short, professional email summarizing the Q3 earnings for a "
#     "fictional tech company called 'Nova Solutions'. Highlight key growth and a challenge."
# )


# # 3. Define generation settings (optional, but good practice for Pro)
# config = types.GenerateContentConfig(
#     # Lower temperature for more deterministic, professional output
#     temperature=0.4, 
#     max_output_tokens=1024,
# )


# def generate_pro_content():
#     """Makes the API call to Gemini 2.5 Pro and prints the response."""
#     print(f"--- Calling model: {MODEL_NAME} ---")
#     print(f"Prompt: {PROMPT[:70]}...")

#     try:
#         # Call the generate_content method
#         response = client.models.generate_content(
#             model=MODEL_NAME,
#             contents=PROMPT,
#             config=config
#         )

#         # 4. Process and print the response
#         print("\n--- Generated Email ---")
#         print(response.text)
        
#     except Exception as e:
#         print(f"\nAn error occurred during the API call: {e}")


# if __name__ == "__main__":
#     generate_pro_content()

#------------------ from google website -----------------------------------
# from openai import OpenAI

# client = OpenAI(
#     api_key="",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Explain to me how AI works"
#         }
#     ]
# )

# print(response.choices[0].message)

#-------------------------------------------------------------------------------------------------------
# client = genai.Client(api_key= "")
# # Connect to database
# conn = sqlite3.connect("articles.db")
# cursor = conn.cursor()
# print("connection opened")

# # Select articles where ChatGPT_Summaries is still empty

# cursor.execute("SELECT id, prompt FROM articles LIMIT 20")
# articles = cursor.fetchall()
# print("articles fetched")


# for article_id, prompt in articles:
#     print("in for loop")
#     try:
        
#                 #ERROR
#                 response = client.models.generate_content(
#                     model="gemini-2.5-flash",  
#                     input=prompt,
#                     instructions="Summarize this article in 150 words."
#                 )

#                 summary = response.output_text.strip()
                
# # Save summary into ChatGPT_Summaries column
#                 cursor.execute(
#                     "UPDATE articles SET Gemini_Summaries = ? WHERE id = ?",
#                     (summary, article_id)
#                 )
#                 conn.commit()
#                 print(f"✅ Saved Gemini summary for article {article_id}")
#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

#         print("connection closed")
#         conn.close()




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
cursor.execute("SELECT id, Gemini_Summaries, Grok_Summaries FROM articles where Gemini_Summaries is not null")
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
fig, ax = plt.subplots(figsize=(8, len(df) * 0.5 + 1))
ax.axis("off")
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.tight_layout()
plt.savefig("Gemini-Grok-articles-similarity.png", dpi=300)
plt.close()

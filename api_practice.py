import os
from openai import OpenAI
import sqlite3
import httpx
import pandas as pd
# from google import genai

# upload csv data in database


# # CSV details
# csv_file_path = 'CNN_articles_cleaned.csv'
# column_name = 'Body'

# # Load the CSV into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Open a connection to the existing database
# db_file_path = 'articles.db'
# conn = sqlite3.connect(db_file_path)
# cursor = conn.cursor()

# # Ensure the schema exists
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS articles (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     prompt TEXT NOT NULL,
#     ChatGPT_Summaries TEXT,
#     Gemini_Summaries TEXT,
#     Grok_Summaries TEXT
# )
# """)

# # Insert each row from the CSV "Body" column into "prompt"
# for body_text in df[column_name].dropna():  # dropna() to skip blanks
#     cursor.execute("INSERT INTO articles (prompt) VALUES (?)", (body_text,))

# # Commit and close
# conn.commit()
# conn.close()

# print("Data inserted successfully into 'articles.prompt'.")


# ---------------------------------------------------------------------------------------------------------


#--------------------------------------------- ChatGPT ----------------------------------------------------

# Initialize OpenAI client
# client = OpenAI(api_key=)

# # Connect to database
# conn = sqlite3.connect("articles.db")
# cursor = conn.cursor()
# print("connection opened")

# # Select articles where ChatGPT_Summaries is still empty

# cursor.execute("SELECT id, prompt FROM articles LIMIT 20")
# articles = cursor.fetchall()
# print("articles fetched", articles)


# for article_id, prompt in articles:
#     print("in for loop")
#     try:
#         response = client.responses.create(
#             model="gpt-5",  
#             input=prompt,
#             instructions="Summarize this article in 150 words."
#         )
#         summary = response.output_text.strip()
        

#         # Save summary into ChatGPT_Summaries column
#         cursor.execute(
#             "UPDATE articles SET ChatGPT_Summaries = ? WHERE id = ?",
#             (summary, article_id)
#         )
#         conn.commit()
#         print(f"✅ Saved ChatGPT summary for article {article_id}")
#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

# print("connection closed")
# conn.close()

#--------------------------------------------- Grok ----------------------------------------------
# client = OpenAI(
#     api_key= "",
#     base_url="https://api.x.ai/v1",
#     timeout=httpx.Timeout(3600.0), # Override default timeout with longer timeout for reasoning models
# )

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
#         response = client.responses.create(
#             model="grok-4",  
#             input=prompt,
#             instructions="Summarize this article in 150 words."
#         )
#         summary = response.output_text.strip()
        

#         # Save summary into ChatGPT_Summaries column
#         cursor.execute(
#             "UPDATE articles SET Grok_Summaries = ? WHERE id = ?",
#             (summary, article_id)
#         )
#         conn.commit()
#         print(f"✅ Saved Grok summary for article {article_id}")
#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

# print("connection closed")
# conn.close()


#--------------------------------------------- Gemini ----------------------------------------------
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
#         response = client.generate_content(
#             model="gemini-2.5-flash",
#             contents="Explain how AI works in a few words"
#         )

#         summary = response.output_text.strip()
        

#         # Save summary into ChatGPT_Summaries column
#         cursor.execute(
#             "UPDATE articles SET Gemini_Summaries = ? WHERE id = ?",
#             (summary, article_id)
#         )
#         conn.commit()
#         print(f"✅ Saved Gemini summary for article {article_id}")
#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

# print("connection closed")
# conn.close()



client = OpenAI(
    api_key= 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Connect to database
conn = sqlite3.connect("articles.db")
cursor = conn.cursor()
print("connection opened")

# Select articles where ChatGPT_Summaries is still empty

cursor.execute("SELECT id, prompt FROM articles LIMIT 20")
articles = cursor.fetchall()
print("articles fetched")


for article_id, prompt in articles:
    print("in for loop")
    try:
        response = client.responses.create(
            model="gemini-2.5-flash",  
            input=prompt,
            instructions="Summarize this article in 150 words."
        )
        summary = response.output_text.strip()
        

        # Save summary into ChatGPT_Summaries column
        cursor.execute(
            "UPDATE articles SET Gemini_Summaries = ? WHERE id = ?",
            (summary, article_id)
        )
        conn.commit()
        print(f"✅ Saved Geimini summary for article {article_id}")
    except Exception as e:
        print(f"⚠️ Error on article {article_id}: {e}")

print("connection closed")
conn.close()




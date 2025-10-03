import os
from openai import OpenAI
import sqlite3
import httpx
import pandas as pd
from google import genai

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


# ---------------------------------------------------------Clean Data to SQL Table---------------------------------------------

# import sqlite3
# import pandas as pd

# # ---------------------------
# # Load CSV
# # ---------------------------
# csv_file = "csv_data/CNN_articles_cleaned.csv"  # change to your actual filename
# df = pd.read_csv(csv_file)

# # ---------------------------
# # Ensure column names are correct
# # ---------------------------
# expected_cols = ["id", "title", "description", "body", "keywords", "theme", "link"]

# if list(df.columns) != expected_cols:
#     raise ValueError(f"CSV columns {list(df.columns)} do not match expected {expected_cols}")

# # ---------------------------
# # Insert into SQLite
# # ---------------------------
# db_file = "articles.db"  # change to your DB file
# conn = sqlite3.connect(db_file)

# df.to_sql("clean_data", conn, if_exists="append", index=False)

# conn.commit()
# conn.close()

# print("✅ CSV data inserted into clean_data table successfully.")


#--------------------------------------------- ChatGPT ----------------------------------------------------

# Initialize OpenAI client
# client = OpenAI(api_key="")

# # Connect to database
# conn = sqlite3.connect("articles.db")
# cursor = conn.cursor()
# print("connection opened")

# # Select articles where ChatGPT_Summaries is still empty

# cursor.execute("SELECT id, prompt FROM articles LIMIT 100")
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

# cursor.execute("SELECT id, prompt FROM articles LIMIT 100")
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
# --- Gemini client setup ---
# client = OpenAI(
#     api_key="",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # --- Connect to database ---
# conn = sqlite3.connect("articles.db")
# cursor = conn.cursor()
# print("✅ Connection opened")

# # Select rows where Gemini_Summaries is empty (adjust WHERE if needed)
# cursor.execute("SELECT id, prompt FROM articles WHERE Gemini_Summaries IS NULL LIMIT 100")
# articles = cursor.fetchall()
# print(f"📄 {len(articles)} articles fetched")

# for article_id, prompt in articles:
#     print(f"\n▶️ Processing article {article_id}...")

#     try:
#         # Send prompt to Gemini
#         response = client.chat.completions.create(
#             model="gemini-2.5-flash",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {
#                     "role": "user",
#                     "content": f"Summarize this article in 150 words:\n\n{prompt}"
#                 }
#             ]
#         )

#         # Extract summary
#         AIzaSyCMPD3krx61lPPltBpoRyfCniHxsg23vtQ

#         # print(summary)

#         # Save summary back into database
#         cursor.execute(
#             "UPDATE articles SET Gemini_Summaries = ? WHERE id = ?",
#             (summary, article_id)
#         )
#         conn.commit()
#         print(f"✅ Saved Gemini summary for article {article_id}")

#     except Exception as e:
#         print(f"⚠️ Error on article {article_id}: {e}")

# # Close DB connection
# conn.close()
# print("🔒 Connection closed")
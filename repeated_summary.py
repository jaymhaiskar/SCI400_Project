import os
from openai import OpenAI
import sqlite3
import httpx
import pandas as pd
from google import genai


# #------------------------------ChatGPT--------------------------------------------------

# client = OpenAI(api_key="")
# db_file = "articles.db"  # your SQLite database file
# article_id = 1  # we are using the prompt at id=1 in table articles

# # ---------------------------
# # Fetch the prompt from articles
# # ---------------------------
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()

# cursor.execute("SELECT prompt FROM articles WHERE id = ?", (article_id,))
# row = cursor.fetchone()

# if not row:
#     raise ValueError(f"No prompt found in articles for id={article_id}")

# prompt = row[0]
# # print(f"Using prompt: {prompt}")


# # Ensure repeated_summaries exists

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS repeated_summaries (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     article_id INTEGER,
#     ChatGPT_repeated_summaries TEXT,
#     Gemini_repeated_summaries TEXT,
#     Grok_repeated_summaries TEXT,
#     FOREIGN KEY (article_id) REFERENCES articles(id)
# );
# """)
# conn.commit()

# # ---------------------------
# # Call API 10 times and insert summaries
# # ---------------------------
# for i in range(10):
#     print(f"Request {i+1}...")

    
#     response = client.responses.create(
#             model="gpt-5",  
#             input=prompt,
#             instructions="Summarize this article in 150 words."
#         )
    
#     summary = response.output_text.strip()


#     # Insert into repeated_summaries
#     cursor.execute("""
#         INSERT INTO repeated_summaries (article_id, ChatGPT_repeated_summaries)
#         VALUES (?, ?)
#     """, (article_id, summary))

#     conn.commit()

# conn.close()
# print("✅ 10 ChatGPT summaries saved into repeated_summaries for article_id=1")

#--------------------Grok---------------------------------------------------------------

# client = OpenAI(
#     api_key= "",
#     base_url="https://api.x.ai/v1",
#     timeout= httpx.Timeout(3600.0),
#  ) # Override default timeout with longer timeout for reasoning models)

# db_file = "articles.db"  # your SQLite database file
# article_id = 1  # we are using the prompt at id=1 in table articles

# # ---------------------------
# # Fetch the prompt from articles
# # ---------------------------
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()

# cursor.execute("SELECT prompt FROM articles WHERE id = ?", (article_id,))
# row = cursor.fetchone()

# if not row:
#     raise ValueError(f"No prompt found in articles for id={article_id}")

# prompt = row[0]
# # print(f"Using prompt: {prompt}")

# # ---------------------------
# # Call API 10 times and insert summaries
# # ---------------------------
# for i in range(10):
#     print(f"Request {i+1}...")

    
#     response = client.responses.create(
#             model="grok-4",  
#             input=prompt,
#             instructions="Summarize this article in 150 words."
#         )
    
#     summary = response.output_text.strip()


#     # Insert into repeated_summaries
#     cursor.execute("""
#         INSERT INTO repeated_summaries (article_id, Grok_repeated_summaries)
#         VALUES (?, ?)
#     """, (article_id, summary))

#     conn.commit()

# conn.close()
# print("✅ 10 Grok summaries saved into repeated_summaries for article_id=1")

#---------------------Gemini-------------------------------------------------------------------

# client = OpenAI(
#     api_key="",
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
#  ) # Override default timeout with longer timeout for reasoning models)

# db_file = "articles.db"  # your SQLite database file
# article_id = 1  # we are using the prompt at id=1 in table articles

# # ---------------------------
# # Fetch the prompt from articles
# # ---------------------------
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()

# cursor.execute("SELECT prompt FROM articles WHERE id = ?", (article_id,))
# row = cursor.fetchone()

# if not row:
#     raise ValueError(f"No prompt found in articles for id={article_id}")

# prompt = row[0]
# # print(f"Using prompt: {prompt}")

# # ---------------------------
# # Call API 10 times and insert summaries
# # ---------------------------
# for i in range(10):
#     print(f"Request {i+1}...")

    
#     response = client.chat.completions.create(
#         model="gemini-2.5-flash",
#         messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": f"Summarize this article in 150 words:\n\n{prompt}"                
#         }
#         ]
#     )
    
#     summary = response.choices[0].message.content


#     # Insert into repeated_summaries
#     cursor.execute("""
#         INSERT INTO repeated_summaries (article_id, Gemini_repeated_summaries)
#         VALUES (?, ?)
#     """, (article_id, summary))

#     conn.commit()

# conn.close()
# print("✅ 10 Gemini summaries saved into repeated_summaries for article_id=1")
from google import genai

# client = genai.Client(api_key=)
client = genai.Client()
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
        
        #ERROR
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Explain how AI works in a few words"
        )

        summary = response.output_text.strip()
        

    except Exception as e:
        print(f"⚠️ Error on article {article_id}: {e}")

print("connection closed")
conn.close()

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
#     api_key="AIzaSyCMPD3krx61lPPltBpoRyfCniHxsg23vtQ",
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
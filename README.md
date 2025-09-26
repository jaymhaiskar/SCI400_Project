SCI 400 Project

Q1) Should I put each article summary as an item in a list to compare them? or just make a database for them?
Q 1.1) would the size of the list be too big
 - first figure out how to do API call
 - look into OpenAI python API
 - database might be easier for data retrieval
 - id, prompt, openAI, Gemini, Grok
 - create system for structured prompt evaluation

   
Q2) should I take the avg of cosine similarity? as in, each article is compared against the other and then I derive the avg, or i see the similarity between the total of the 2 arrays. 


Data cleaning:
- remove any rows with null values
- remove duplicates articles
- remove â€™ from body

Table: articles
schema:
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt TEXT NOT NULL,
    ChatGPT_Summaries TEXT,
    Gemini_Summaries TEXT,
    Grok_Summaries TEXT
);


When I try to access Gemini API thru random.py by import (pip install google-genai) it gives me the error: AttributeError: partially initialized module 'google.genai' has no attribute 'Client' (most likely due to a circular import)

When I try to access Grok and ChatGPT API thru api_practice.py after trying to access gemini I get the error: ImportError: cannot import name 'compat32' from partially initialized module 'email._policybase' (most likely due to a circular import) (/home/codespace/.python/current/lib/python3.12/email/_policybase.py)




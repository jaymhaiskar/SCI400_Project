from transformers import BertTokenizer, BertModel
import torch
import matplotlib.pyplot as plt
import seaborn as sns

# Jaccard Similarity
# 

### ORIGINAL
### An 18-year-old woman was killed and the suspect — her brother — is dead after multiple people were stabbed in Hollow Water First Nation on Thursday, RCMP say. 
### Seven other community members were injured in the early morning attacks, said Supt. Rob Lasson, the officer in charge of Manitoba RCMP major crime services, at a news conference Thursday afternoon. 
### The victims ranged in age from 18 to 60.

###
text = """An 18-year-old woman was killed and seven others were injured in multiple stabbings in the Hollow Water First Nation. RCMP confirmed the suspect, the woman's brother, is also dead. The victims' ages range from 18 to 60."""

# Load model & tokenizer (BERT for demo, works with others too)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased", output_attentions=True)

inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# Get attention from last layer [batch, heads, seq_len, seq_len]
attentions = outputs.attentions[-1][0]  

# Visualize attention of the first head
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

plt.figure(figsize=(50, 40))
sns.heatmap(attentions[0].detach().numpy(), 
            xticklabels=tokens, 
            yticklabels=tokens, 
            cmap="viridis")

plt.title("Attention Map (Head 1, Last Layer)")
plt.xticks(rotation=90)
plt.yticks(rotation=0)

# Save as PNG instead of showing
plt.savefig("attention_map_gemini.png", dpi=300, bbox_inches="tight")
plt.close()

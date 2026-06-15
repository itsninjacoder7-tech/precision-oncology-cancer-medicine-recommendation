import json
import faiss
import numpy as np

# Load dataset
with open("data/fda_context.json", "r") as f:
    records = json.load(f)

# Load FAISS index
index = faiss.read_index(
    "data/latest_db/indexes/oncology.faiss"
)

# Create searchable documents
docs = [
    f"{r['gene']} | {r['disease']} | {r['drug']}"
    for r in records
]

def retrieve(query):

    query = query.upper()

    for i, record in enumerate(records):

        gene = record["gene"].upper()
        disease = record["disease"].upper()

        if gene in query or disease in query:

            return f"""
Gene: {record['gene']}
Disease: {record['disease']}
Recommended Drug: {record['drug']}
"""

    return "No matching oncology evidence found."
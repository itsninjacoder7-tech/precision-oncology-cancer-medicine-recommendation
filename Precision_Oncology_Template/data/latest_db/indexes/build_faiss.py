import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

docs = [
    "EGFR treated with Osimertinib",
    "HER2 treated with Trastuzumab",
    "ALK treated with Alectinib"
]

vectors = model.encode(docs)

index = faiss.IndexFlatL2(
    vectors.shape[1]
)

index.add(
    np.array(vectors)
    .astype("float32")
)

faiss.write_index(
    index,
    "oncology.faiss"
)

print("FAISS Created")
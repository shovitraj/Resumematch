from sentence_transformers import SentenceTransformer, util
import numpy as np
model = SentenceTransformer('stsb-roberta-large')
# encode list of sentences to get their embeddings
embedding1 = model.encode(sentences1, convert_to_tensor=True)
embedding2 = model.encode(sentences2, convert_to_tensor=True)

# compute similarity scores of two embeddings
cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
score=[]
for i in range(len(sentences1)):
    for j in range(len(sentences2)):
        if cosine_scores[i][j] > 0.5:
            score.append(cosine_scores[i][j].item())
            print("Sentence 1:", sentences1[i])
            print("Sentence 2:", sentences2[j])
            print("Similarity Score:", cosine_scores[i][j].item())
            print()

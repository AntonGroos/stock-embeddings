import numpy as np
import json
from numpy.linalg import norm
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import matplotlib.pyplot as plt

with open('stock_ticker_lists.json', 'r') as f:
    data = json.load(f)

# Flatten the list of lists and fit the tokenizer

stock_index = {key: val - 1 for val, key in enumerate(sorted(data[0]), start=1)}

#embedding_weights = np.load('stock_embedding_weights.npy')

model = Word2Vec.load('stock2vec.model')


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

example_stocks = ['AAPL', 'DIS', 'JPM', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NFLX', 'NVDA', 'WBD']
similarities = {}

for i in range(len(example_stocks)):
    for j in range(i + 1, len(example_stocks)):
        stock1, stock2 = example_stocks[i], example_stocks[j]
        idx1, idx2 = stock_index[stock1], stock_index[stock2]
        vec1, vec2 = model.wv[stock1], model.wv[stock2]
        similarity = cosine_similarity(vec1, vec2)
        similarities[f'{stock1}-{stock2}'] = similarity

print(similarities)


# Reduce the dimensionality of the embeddings to 3D using t-SNE
tsne = TSNE(n_components=2, random_state=42)
reduced_embeddings = tsne.fit_transform(model.wv.vectors)

# Plot the 2D embeddings
fig, ax = plt.subplots(figsize=(10, 10))
for stock, idx in stock_index.items():
    ax.scatter(reduced_embeddings[idx, 0], reduced_embeddings[idx, 1])
    ax.text(reduced_embeddings[idx, 0], reduced_embeddings[idx, 1], stock, fontsize=9)

ax.set_title('2D Visualization of Stock Embeddings', fontdict={'fontsize': 14, 'fontweight': 'bold'})
ax.set_xlabel('Dimension 1')
ax.set_ylabel('Dimension 2')
plt.show()

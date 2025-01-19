import numpy as np
import json
from gensim.models import Word2Vec


# Sample data: list of lists containing strings (tokens)

with open('stock_ticker_lists.json', 'r') as f:
    data = json.load(f)

# Create a dictionary mapping tokens to integers
stock_index = {key: val+1 for val, key in enumerate(sorted(data[0]))}


# Train Word2Vec model
print('Training Word2Vec model...')
stock2vec_model = Word2Vec(sentences=data, vector_size=8, window=10, min_count=1, workers=4)
stock2vec_model.save("stock2vec.model")




# Stock Vector Embedding

## Overview

This project focuses on creating vector embeddings for stock data. The goal is to represent stock information in a high-dimensional space for various machine learning applications.

I am using this very simple embedding as a benchmark for a different stock embedding model. Feel free to use this as a starting point as well.

## Features

- Data preprocessing
- Vector embedding generation
- Visualization tools
- Model training and evaluation

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/AntonGroos/StockVectorEmbedding.git
cd StockVectorEmbedding
pip install -r requirements.txt
```

## Usage

Run the scripts in this order to get embeddings:

```bash
python yfinance_loader.py

python train_embedding.py
```

Now you are ready to go. If you want to visualize your embedding run the visualize_embedding.py.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

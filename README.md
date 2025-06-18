# 🧠 Sentiment Analysis using DistilBERT (SST-2 Fine-Tuned)

This project demonstrates how to use the Hugging Face 🤗 Transformers library with the model [`distilbert/distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) for sentiment analysis. The model is a lightweight version of BERT, fine-tuned on the Stanford Sentiment Treebank v2 (SST-2) for binary sentiment classification (positive or negative).

---
# Project Title

>🧠 Sentiment Analysis using DistilBERT (SST-2 Fine-Tuned)

This project demonstrates how to use the Hugging Face 🤗 Transformers library with the model distilbert/distilbert-base-uncased-finetuned-sst-2-english for sentiment analysis.

## 📌 Table of Contents

 
- [Overview](#overview)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Example Usage](#example-usage)
- [API](#api)
- [Performance](#performance)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

The SST-2 dataset is widely used for training sentiment classifiers. This project allows you to:

- Classify input text into **positive** or **negative** sentiment.
- Use the DistilBERT transformer model for faster inference.
- Integrate easily with web apps, notebooks, or production systems.

---

## Installation
First, clone the repository and set up the Python environment.

```bash
git clone https://github.com/yourusername/distilbert-sentiment-analysis.git
cd distilbert-sentiment-analysis

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

transformers
torch
scikit-learn
gradio  # Optional, if you want to build a UI

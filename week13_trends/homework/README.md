## Bonus Homework, Semantic IDs
This homework requires you to go through a full pipeline: item embedding preparation → semantic ID construction → sequence modeling → evaluation.

The goal is to implement and compare different ways of constructing Semantic IDs for recommender systems. You will start with item embeddings, build Semantic IDs using residual quantization methods such as RQ-KMeans and RQ-VAE, and then train generative recommendation models that predict these IDs instead of raw item IDs.

By the end of the homework, you should understand how Semantic IDs can be used as compact, structured targets for generative retrieval, how collisions between items can be handled, and how different semantic ID construction methods affect recommendation quality.

#### Submission
Write code and conduct experiments in the [notebook](homework/homework.ipynb), submit via YSDA LMS. 

#### Author
[Krasilnikov Aleksei](https://github.com/KrasilnikovAV)

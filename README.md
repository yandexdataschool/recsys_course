# YSDA Recommender Systems Course

This repository contains materials for the Recommender Systems course taught at the [Yandex School of Data Analysis](https://shad.yandex.ru). This branch corresponds to the ongoing 2026 spring semester.

## Syllabus

- Week 1: Intro
    - Lecture: course overview and organizational details, intro to "Recommender Systems" problem
    - Seminar: basic recommenders, user-item latent space
- Week 2: Candidate generation & metrics
    - Lecture: recsys metrics & candidate generation: classic ML, ANN, mixing
    - Seminar: yambda contest overview & baseline solution
- Week 3: Ranking, diversity & metrics
    - Lecture: reranking - losses, algorithms, metrics; diversity control and MRR / DPP
    - Seminar: classic algorithms (MF, SLIM, EASE); ranking - pool building, undersampling, composite targets
- Week 4: Deep learning for RecSys & neural candidate generation
    - Lecture: two-tower architecture, softmax model & sampled softmax loss, contrastive learning, negative sampling and LogQ
    - Seminar: paper review on LogQ correction and negative sampling techniques
- Week 5: Neural candidate generation, pt.2
    - Lecture: cold start and long-tail, user / item encoding strategies, sequential models, beyond two-tower (GPU retrieval, generative retrieval)
    - Seminar: aspects of training neural networks for RecSys
- Week 6: Neural ranking, pt.1
    - Lecture: why use DL, feature encoding (categorical, embedding, scalar), model composition
    - Seminar: paper review on Piecewise Linear Encoding and Unified Embeddings
- Week 7: Neural ranking, pt.2
    - Lecture: feature interaction modelling, MLP, multi-task & knowledge distillation
    - Seminar: paper review on DCNv2 architecture 
- Week 8: System Design, pt. 1
    - Lecture: data architectures, logging, biases, data drift and monitoring
    - Seminar: feature storages for different scales
- Week 9: System Design, pt. 2
    - Runtime design, candidate funnel, GPU inference, data delivery, controlled degradation, cold start
    - Seminar: paper review on GPU retrieval - LiNR, SilverTorch
- Week 10: RecSys Transformers applications
    - Lecture: all about sequential models (transformers) on user action history
    - Seminar: paper review on PinnerFormer & TransAct (by Pinterest)
- Week 11: Reinforcement Learning in RecSys
    - Lecture: all about bandits - algorithms, Thompson sampling, contextual bandits
    - Seminar: applications of bandits & off-policy evaluation for e-grocery
- Week 12: Case Studies of Yandex's services
    - Lecture: recsys design for e-grocery, movie streaming platform, blogpost & news feed
    - Practice: deep dive in Lavka (Yandex's e-grocery) recommender system
- Week 13: Trends in RecSys
    - Lecture: state-of-the-art approaches & novel papers in RecSys
    - Practice: best contest colutions on yambda retrieval

## Staff

- [Daniil Tkachenko](https://github.com/deadpadre)
- [Kirill Khrylchenko](https://github.com/KhrylchenkoKirill)
- [Roma Nigmatullin](https://github.com/rmnigm)
- [Alexey Krasilnikov](https://github.com/KrasilnikovAV)
- [Artem Matveev](https://github.com/matfu-pixel)
- [Vladimir Baikalov](https://github.com/NonameUntitled)
- [Vlad Tytskiy](https://github.com/Tytskiy)
- [Ruslan Kuliev](https://github.com/kuliev-r)

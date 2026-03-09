# 🎬 Movie Recommendation System

A collaborative filtering-based movie recommendation system built with Python. This project implements multiple recommendation approaches to suggest movies to users based on their viewing history and preferences.

## 📋 Overview

This project builds a movie recommendation system using the MovieLens 100K dataset. It implements three different recommendation approaches and evaluates their performance using precision, recall, and mean average precision metrics.

## 🎯 Features

- **Exploratory Data Analysis**: Visualize rating distributions, user behavior, and movie popularity
- **User-Based Collaborative Filtering**: Recommend movies based on similar users' preferences
- **Item-Based Collaborative Filtering**: Suggest movies similar to those a user has liked
- **Matrix Factorization (SVD)**: Use latent factors to predict user preferences (Bonus)
- **Model Evaluation**: Compare performance using Precision@K, Recall@K, and MAP@K
- **Visualization**: Generate comprehensive visualizations of results

## 📊 Dataset

The project uses the **MovieLens 100K dataset** containing:
- 100,000 ratings from 943 users on 1,682 movies
- Ratings scale: 1 to 5 stars
- Timestamp information for each rating
- Movie metadata including titles and release dates

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Scikit-learn** - Similarity metrics and evaluation
- **SciPy** - Matrix factorization (SVD)

## 📁 Project Structure

# Naive Bayes Classifier

## Overview

Supervised. Probabilistic algorithm that’s typically used for classification problems with categorical features.
"Naive" comes from the basic assumption that all features are independent. This greatly
simplifies computations. Even if in practice this assumption is violated, the results are 
still reasonable.

## Core equation 

p(B|A) = p(A|B) * p(B) / p(A)

## Independence assumption

Naive Bayes assumes that all features are independent. This means that 

p(A|B) = p(a_1 | B) * p(a_2 | B) * ... * p(a_n | B) 

Hence,

p(B|A) ∝ p(A|B) * p(B) = p(a_1 | B) * p(a_2 | B) * ... * p(a_n | B) * p(B)

Where we removed the denominator p(A) because it is constant for a given input

Example : p(Class_j | sentence) ∝ p(word_1 | class_j) * p(word_2 | class_j) * ... * p(word_n | class_j) *  p(class_j) 

with p(word_i | class_j) = #(word_i & class_j) / #(class_j)

Note thath for the previous example we use the bag-of-word model : we just count words
without taking into account their order in the sentence

## Laplace smoothing 

One issue is that if some feature values rarely show, their likelihood will be zero, 
which makes the whole posterior probability zero. One simple way to fix this problem 
is called Laplace smoothing: add imaginary samples (usually one) to each category

## PS : Continuous features

Naive Bayes is usually performed on discrete features. However, it is not a requirement.
If we deal with continuous features, Naive Bayes is still possible but we first need
to recode the continuous features into quartiles. 

## Strengths

* Nicely suited for categorical data
* Even though the naive assumption is rarely true, the algorithm performs surprisingly good in many cases
* Handles high dimensional data well. Easy to parallelize and handles big data well
* Performs better than more complicated models when the data set is small

## Weaknesses

* The estimated probability is often inaccurate because of the naive assumption. Not ideal for regression use or probability estimation
* When data is abundant, other more complicated models tend to outperform Naive Bayes

## Credits

* Siraj Raval
* Disclaimer : Code is used as an illustration of the README theory file. Code has been forked from [AlanBuzdar](https://github.com/alanbuzdar) and [Zixuan Zhang](https://towardsdatascience.com/naive-bayes-explained-9d2b96f4a9c0). I mainly corrected/updated it to make it work on my computers.


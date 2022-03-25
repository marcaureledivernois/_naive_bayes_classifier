import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import string

#creating a spam model
#runs once on a training data
def train(xtrain,ytrain):
    total = 0
    numSpam = 0
    for (email, label) in zip(xtrain, ytrain):
        email = email.translate(str.maketrans('', '', string.punctuation)).split()
        if label == 'spam' :
            numSpam +=1
        total += 1
        processEmail(email , label)
        pA = numSpam/float(total)
        pNotA = (total - numSpam)/float(total)
    return pA, pNotA


#reading words from a specific email
def processEmail(body , label):
    for word in body:
        words.add(word)
        if label == 'spam':
            trainPositive[word] = trainPositive.get(word, 0) + 1
            count_words['spam'] = count_words.get('spam', 0) + 1
        else:
            trainNegative[word] = trainNegative.get(word, 0) + 1
            count_words['ham'] = count_words.get('ham', 0) + 1

#gives the conditional probability p(B_i/A_x)
def conditionalEmail(body , spam) :
    result =1.0
    for word in body:
        result *= conditionalWord(word , spam)
    return result

#classifies a new email as spam or not spam
def classify(email):
    isSpam = pA * conditionalEmail(email, True) # P (A | B)
    notSpam = pNotA * conditionalEmail(email, False) # P(¬A | B)
    return isSpam > notSpam

#Laplace Smoothing for the words not present in the training set
#gives the conditional probability p(B_i | A_x) with smoothing
def conditionalWord(word, spam):
    if spam:
        return (trainPositive.get(word,0)+alpha)/(float)(count_words['ham']+alpha*numWords)
    else:
        return (trainNegative.get(word,0)+alpha)/(float)(count_words['spam']+alpha*numWords)

## Load data

data_kaggle = pd.read_csv('spam.csv')
X = data_kaggle['v2']
y = data_kaggle['v1']

y.value_counts(normalize=True)
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.33)

## Train model

alpha = 1
trainPositive = {}
trainNegative = {}
count_words = {}
words = set()
pA, pNotA = train(X_train,y_train)
numWords = len(words)

## Classification

preds = X_train.apply(classify)
y_train=='spam' #true if spam, false if ham

confusion_matrix(y_train=='spam', preds)
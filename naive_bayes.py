import pandas as pd
from sklearn.model_selection import train_test_split

#creating a spam model
#runs once on a training data
def train(data):
    total = 0
    numSpam = 0
    for email in data:
        if email.label == 'spam' :
            numSpam +=1
        total += 1
        processEmail(email.body , email.label)
        pA = numSpam/float(total)
        pNotA = (total - numSpam)/float(total)

#reading words from a specific email
def processEmail(body , label):
    for word in body:
        if label == 'spam':
            trainPositive[word] = trainPositive.get(word, 0) + 1
            positiveTotal += 1
        else:
            trainNegative[word] = trainNegative.get(word, 0) + 1
            negativeTotal += 1

#gives the conditional probability p(B_i/A_x)
def conditionalEmail(body , spam) :
    result =1.0
    for word in body:
        result *= conditionalWord(body , spam)
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
        return (trainPositive.get(word,0)+alpha)/(float)(positiveTotal+alpha*numWords)
    else:
        return (trainNegative.get(word,0)+alpha)/(float)(negativeTotal+alpha*numWords)


data_kaggle = pd.read_csv('spam.csv')
X = data_kaggle['v2']
y = data_kaggle['v1']

y.value_counts(normalize=True)

X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.33)
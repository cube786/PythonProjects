#====================== IMPORT PACKAGES ===============================
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn import linear_model
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import numpy as np

#===================== READ A INPUT DATA ==============================

dataframe=pd.read_csv("dataset2.csv")
print("*******************************************************")
print()
print("                   Data Selection                     ")
print()
print("******************************************************")
print()
print(dataframe.head(10))
print()


#========================== PRE PROCESSING ================================

#=== ckecking missing values ===

print("**************************************")
print()
print("    Before Handling Missing Values    ")
print()
print("**************************************")
print()
print(dataframe.isnull().sum())
print() 

#=== replace the missing values by 0 ===

median = dataframe['MMSE'].median()
dataframe['MMSE'].fillna(median, inplace=True)
print("****************************************************")
print()
print("     After Handling Missing Values    ")
print()
print("****************************************************")
print()
print("---- 1.Remove missing values in MMSE ----")
print()
print(dataframe.isnull().sum())
print()

median = dataframe['SES'].median()
dataframe['SES'].fillna(median, inplace=True)
print()
print("---- 2.Remove missing values in SES ----")
print()
print(dataframe.isnull().sum())
print()


#=== label encoding ===

print("****************************************************")
print()
print("              Before Label Encoding                 ")
print()
print("****************************************************")
print()
print(dataframe['Group'].head(10))
label_encoder = preprocessing.LabelEncoder() 
print("****************************************************")
print()
print("              After Label Encoding                 ")
print()
print("****************************************************")
print()
dataframe['Group']= label_encoder.fit_transform(dataframe['Group'])
print(dataframe['Group'].head(10)) 
dataframe['M/F']= label_encoder.fit_transform(dataframe['M/F']) 
dataframe['Hand'] = label_encoder.fit_transform(dataframe['Hand'])


#========================== DATA SPLITTING  ==========================

feature_col_names = ["M/F", "Age", "EDUC", "SES", "MMSE", "eTIV", "nWBV", "ASF"]
predicted_class_names = ['Group']


X = dataframe[feature_col_names].values
y = dataframe[predicted_class_names].values

#spliting the x and y into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)


#==================== CLASSIFICATION ==================================

#=== SUPPORT VECTOR MACHINE ===

#initialize the model
svm = SVC(kernel="linear", C=0.1,random_state=0)

#fitting the model
svm.fit(X_train, y_train.ravel())

#predict the model
pred_svm = svm.predict(X_test)


#==================== PERFORMANCE ANALYSIS ===============================


#=== confusion matrix ===
print("******************************************************")
print()
print("          Performance Metrics for SVM                 ")
print()
print("******************************************************")
cm_svm=confusion_matrix(y_test,pred_svm)
print()
print("1.Confusion Matrix",cm_svm)
print()

#find the performance metrics 
TP = cm_svm[0][2]
FP = cm_svm[0][1]
FN = cm_svm[1][0]
TN = cm_svm[1][1]

#Total TP,TN,FP,FN
Total=TP+FP+FN+TN

#Accuracy Calculation
accuracy1=((TP+TN)/Total)*100
print("2.Accuracy",accuracy1,'%')
print()

#Precision Calculation
precision=TP/(TP+FP)*100
print("3.Precision",precision,'%')
print()

#Sensitivity Calculation
Sensitivity=TP/(TP+FN)*100
print("4.Sensitivity",Sensitivity,'%')
print()

#specificity Calculation
specificity = (TN / (TN+FP))*100
print("5.specificity",specificity,'%')
print()

#========================== LOGISTIC REGRESSION ==================================

#initialize the model
lr = linear_model.LogisticRegression()
#fitting the model
lr.fit(X_train, y_train.ravel())

#predict the model
pred_lr = lr.predict(X_test)


#==================== PERFORMANCE ANALYSIS ===============================

#=== confusion matrix ===
print("******************************************************")
print()
print("          Performance Metrics for LR                 ")
print()
print("******************************************************")
print()
cm_lr=confusion_matrix(y_test,pred_lr)
print()
print("1.Confusion Matrix",cm_lr)
print()

#find the performance metrics 
TP = cm_lr[0][2]
FP = cm_lr[0][1]
FN = cm_lr[1][0]
TN = cm_lr[1][1]

#Total TP,TN,FP,FN
Total=TP+FP+FN+TN

#Accuracy Calculation
accuracy2=((TP+TN)/Total)*100
print("2.Accuracy",accuracy2,'%')
print()

#Precision Calculation
precision=TP/(TP+FP)*100
print("3.Precision",precision,'%')
print()

#Sensitivity Calculation
Sensitivity=TP/(TP+FN)*100
print("4.Sensitivity",Sensitivity,'%')
print()

#specificity Calculation
specificity = (TN / (TN+FP))*100
print("5.specificity",specificity,'%')
print()


#==================== PREDICTION =================================

#disease prection
for i in range(1,10):
    if pred_lr[i]== 2:
        print("**************************")
        print()
        print([i],' Demented ')
        print()
        print("**************************")
        print()
    else:
        print("**************************")
        print()
        print([i],'Non Demented ')
        print()
        print("*************************")
        print()

#====================== ALGORITHM COMPARISON ==================================

#algorithm comparion 
if(accuracy1>accuracy2):
    print("*****************************************************")
    print()
    print("   Support Vector Machine algorithm is efficient     ")
    print()
    print("*****************************************************")
else:
    print("*****************************************************")
    print()
    print("        Logistic regression is efficient             ")
    print()
    print("*****************************************************")

#====================== VISUALIZATION ==================================


objects = ('SVM', 'LR')
y_pos = np.arange(len(objects))
performance = [accuracy1,accuracy2]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Accuracy')
plt.title('Algorithm comparison')
plt.show()

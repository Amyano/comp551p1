
import numpy as np

Wine = np.loadtxt(open("winequality-red.csv", "rb"), delimiter=";", skiprows=1)
Cancer = np.genfromtxt(open("breast-cancer-wisconsin.data", "rb"),
                       missing_values="?", delimiter=",",usecols=range(1,11))   #We drop the ID column which is not usefull for training 
                                                                                 # the data. and load the samples with missing values as well.


Wine[:,11]=Wine[:,11]>5     # Switch it to binary 1 is for good quality 0 for bad.
Cancer[:,9]=Cancer[:,9]>3        # 1 for Malignant, 0 for benign

Cancer=Cancer[np.all(np.isfinite(Cancer), axis=1)]   #Delete samples with missing values. 16 samples were removed


X1 = Wine[:,0:11]        #For here, we do not add the bias column.  The complementation part will add to the matrix later on.
Y1 = Wine[:,11]
X2 = Cancer[:,0:9]
Y2 = Cancer[:,9]

N1 = X1.shape[0]      #The size of the data set.
N2 = X2.shape[0]

M1= 11
M2= 9   #number of weights without the bias one..

Py1P = np.sum(Y1)/N1    #Probablity of possitive results for firsts dataset
Py1N = 1 - Py1P

Py2P = np.sum(Y2)/N2
Py2N= 1 - Py2P




Mean11 = np.zeros(12)   #initialize the mean value vector for features of positive results.
Mean21 = np.zeros(10)


for row in Wine:                #Using loop to sum up all featrues with positive results.
    if row[Wine.shape[1]-1]==1:
        Mean11 = Mean11 + row

Mean11=Mean11[0:11]                        # Drop the last column
Mean10=X1.sum(axis=0)-Mean11                 # Using the entire summation minux the positve result, so we get negative results.
Mean11=(Mean11/np.sum(Y1))                    # Calculate the mean
Mean10=(Mean10/(N1-np.sum(Y1)))



for row in Cancer:
    if row[Cancer.shape[1]-1]==1:
        Mean21 = Mean21 + row

Mean21=Mean21[0:9]
Mean20=X2.sum(axis=0)-Mean21    
Mean21=np.transpose(Mean21/np.sum(Y2))
Mean20=np.transpose(Mean20/(N2-np.sum(Y2)))




Sigma1=np.zeros((11,11))                 #initialize the Sigma Matrix
Sigma2=np.zeros((9,9))

                     
for row in Wine:                            #Using for loop to update the matrix just following the euqation.
    if row[Wine.shape[1]-1]==1:
        Sigma1 = Sigma1 + np.outer(row[0:11]-Mean11,row[0:11]-Mean11)

for row in Wine:
      if row[Wine.shape[1]-1]==0:
        Sigma1 = Sigma1 + np.outer(row[0:11]-Mean10,row[0:11]-Mean10)
        
for row in Cancer:
      if row[Cancer.shape[1]-1]==1:
        Sigma2 = Sigma2 + np.outer(row[0:9]-Mean21,row[0:9]-Mean21)
     
for row in Cancer:
      if row[Cancer.shape[1]-1]==0:
        Sigma2 = Sigma2 + np.outer(row[0:9]-Mean20,row[0:9]-Mean20)
        
        
Sigma1=Sigma1/(N1-2)           #Finally divide by the samples number
Sigma2=Sigma2/(N2-2)        
        





        
        

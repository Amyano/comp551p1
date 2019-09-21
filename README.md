# comp350p1

## Requirements

* Python 3.7

## Getting started

```sh
pip install poetry --user
poetry install
```

## Tasks
AAAAAAAAAAAAAAAA.  Things to do for the data sets.

Notation:  N is the size of training set, and M is the dimension of features.

1.red wine part

//We should load up the data as some matrix for our project. All tasks will be easier if they are implemented in a vectorized way. As there are 11 features,  our X1 (input) matrix should be (n * 12)size, where m is the number of samples.  and there is one bias colunm.
a (12*1) size vector W1 is also needed. as well as a Y1 ourput. (n*1).


// Remark: the output of this dataset is the quality of redwine represented by a digit from 0 to 10. We should convert it to a binary situation where 6-10 is positive, otherwise negative.  Also some clearing should be done as some samples miss or malform feaures.



 2. breast-cancer part

 Similarly, there are 9+1 features and m samples.  So with X matrix (n * 10).  other setup is the same as above



  ///Results that will be provided for the following implementation.

 X1,X2,Y1,Y2 matrix.    /Remark: for Y1: 1 is good quality, 0 is bad.    Y2: 1 is benign   2 is malignant/

 Py1P= p(y1)=1(positive) Py1N
 Py2N= p(y2)=0(Negative) Py2N

 Four vectors= M11= [μ11;μ21......μ111] (11*1 size vector)  which means that average of features for the red wine set when it is good quality.
               M10 =......... bad quality
               M21 M20 Similarly.

 Sigma matrix= sigma1=  (11*11)
               sigma2=  (9*9)   
               
               
               

BBBBBBBBBBBBBBBBB.Implement 2 linear classification techniques:

* logistic regression
* linear discriminant

1. acquire, preprocess and analyze data of
   [wine quality] (red wine only) and
   [breast cancer diagnosis].

   Define data structures, e.g. using numpy arrays and panda DataFrames.
   Clean up malformed features, missing data etc.
   Statistical analysis on the datasets.

2. Actual implementation of classification techniques

[wine quality]: https://archive.ics.uci.edu/ml/datasets/Wine+Quality
[breast cancer diagnosis]: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

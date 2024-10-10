# FEATURE ENGINEERING FOR ML AND DL


## Feature Engineering

- To manipulate,addition,deletion,combination,mutation of the given data set to improve machine learning model training which leads to better performance and with greater accuracy .
    - Types of Feature Engineering 
        - Feature Encoding 
        - Feature Binning
    - Why do we need Feature Scaling ?
        - solving Machine learning and Deep Learning use cases 
        - Discussing on features.
        - The feature values represented as Magnitude and Units.
        - Scaling requires:
            - Linear regression 
                - used in the gradient descent,used to find the global minima.
            - KNN
            - K MEANS
            - No scaling Required
                - decision tree
                - Random Forest
                - Xgboosyt
        - Convergence takes place easily and easy to visualize.
        - Using while performing euclid's distance.

## Encoding
    - Conversion of the categorical data into numerical data 
    - Where the group of data with same values are categorized as 1's and remaining all has 0's

## Types of Feature Engineering Encoding Techniques
### Nominal Encoding
    - It is type of data set in which the order or the rank of the features are not maintained.
    - For example :
        - color of the shirt,city names,Maritial status....,etc
        - No rearrangement of features is required usually.
    - feature rearrangement is required according to the rank/order.
##  Types of Nominal Encoding
>One Hot Encoding 
- How many numbers of categories are there, that many columns will be created.
- we have created has the dummy variable.
- There is also a dummy variable category.
- Whenever your doing one hot encoding that means you have to delete one column in the front/back/at any position.
- The result is binary and that everything sits in an orthoginal vector space.
- Disadvantages of one hot encoding 
    - [ ] When the no. of columns increases that means your increasing the dimensions which leads to curse of dimensionality
>One Hot Encoding with many categorical
- This is the technique used by the Researchers in the competetion called KDD organe.
- They have checked and selected the top 10 repeating categories of the DataSet.
- After selecting the Top 10 categories They have appilied one hot encoding to it.
>Mean Encoding
- converting the features into mean values with respect to the particular category of the features.
### Ordinal Encoding 
    - It is a type of data set which the order or the rank of the features are  maintained.
    - for example :
    - Student performance,customer Review,Education of person...,etc

##  Types of Ordinal Encoding
>Label Encoding
- The rank will provided to the columns. 
- The rank will in the order of high to low.
- Disadvantage of Label Encoding 
- The numeric values can be misinterpreted by algorithms as having some sort of Hierachy/Order in them.
>Target Guided Ordinal Encoding
- Not taking the feature alone,we are also taking the output variable.
- for Classification mainly used.
- Computing the mean of the Feature Category and output variable.
- Assign the Ranks to the category with the use of calculated mean .
- Based on the Rank ,The labels are arranged and Then given given machine learning model.
- Disadvantages of Target-Based Encoding
    - Its dependency to the distribution of the target and its lower predictability power compare to the binary encoding method.

### Frequency encoding or count encoding
    - Basically applied on the high number of labels or categories which means high cardinality.
    - To replace each label of the categorical variable by the coount, this is the amount of times each label appears in the dataset.
    - Advantages of the Frequency Encoding
    - It is very simple to implement.
    - does not increase the feature dimensional space.
    - Disadvantages of the Frequecy Encoding
    - If some of the label with same count will replaced as same count, then they will loose some valuable information.
    - Adds somewhat arbitary numbers,and therefore weights to the different labels,that may not be related to their predictive power.


##  How to handle Missing Values In Categorical Variable.
-  When a empty value is present in a categorical value,delete the missing value record. [leads to delte the important record sometime]
- Replacing the empty values with the most Frequent repeating values in the features. [leads to Imbalanced dataset]
- By applying an classification algorithm to predict, making the empty value as the target category of the dataset and becomes the test dataset and rest all values will be in the train dataset. [more efficient]
- By applying Unsupervised Technique like clustering 
    making the empty category has one group and rest all becomes the another group.[less efficient]

>



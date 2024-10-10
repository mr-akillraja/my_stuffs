#       STATISTICS
- Statistics in the form data in which we have implement the collection,organization,analysis,interpretation and presentation of the data.
- Two types of Statistics 
    >Descriptive Stats
    - Analyzing,Summarize,Organizing Data in the form of Graph.
    - Barplot,Histogram,Pie-chart etc.
    - Measure of central Tendency.
        - A single value that reflects the center of the data distribution.
        - The data can described using MEAN,MODE,MEDIAN.
    - Measure of Variance.
        - The way to extracting the meaningful information from a set of provided data.
        - Types Measure of variations:
            >> Range 
                - It is the simplest measure of variaiton.
                - The range of dataset is the difference between the highest value and the lowest value.
                - Range is also most affected by the Outliers .So that it uses only the extreme values.
                - It is used when only for small distribution which has no Outliers.
            >> Interquartile Range [IQR]
                - The middle 50% of the values when ordered from lowest to highest value.
                - To calculate the IQR we have find the median of the lower and upper half of the data.Then IQR is difference between them.
                - It is good measure of variation in Skewed dataset as it is resistant to outliers.
                - They are generally paired with median to describe the data.
            >> Variance
                - It is the average Squared difference of values from the mean.
                To calculate the Variance we Square the differnece between each data value and the mean.
                - Then we sum them and divide them with the no.of values in the dataset.
                - It is not used much as it is represented in Squared Units and it is not intuitive measure.
            >> Standard Deviation
                - It is used to calculate how much the data is deviate from the mean.
                - Larger amount of standard deviation,greater the amount of variation.
                - It is calculated has the Square root of the variance.
                - It uses the original units of data which makes the interpretation easier.
                - It is used for normal distrbution or distribution.

> Inferential Stats
- It is used to predict the results of a general population dataset from the immediate dataset available.
- Types of Infernetial Stats.
    >>Hypothesis Testing:
        - It is an Educated Guess about something which is testable either by experiment or observation.
        - Basically it should have meaningful result in the end.
    >>Confidence Interval
        - It is a range that estimates for an unknown parameter.
    >> Regression Analysis
        - It shows the relationship between two or more variables.
        - The method tests the relationship between the independent and dependent variables. 
        - For examples :
            - Z-test
            - T-test
            - Chi square test 

## Population(N) 
- Population data is the entire group that you want to draw conclusions about.
## Population Mean
- It is an average of a group of characteristics.
- for example :
    - In a school of 1300 students and the average GPA is 3.7.
>Formula and Explanation:
- Sumation of all the values in the data 
- Then dividing with the number of items in the data.
- formula:
    >μ = (Σ X)/ N
    - X = all the individual items in the group.
    - N = the number of items in the group.
## Sample(n)
- Sample is the group(part of the population) from which you'll collect Data.
## Sample Mean
- It is an average of a set of data.
- It can be used to calculate the central tendency,Standard Deviation and the Variance of a dataset.
- It is type of data which is picked from the population data.
>Formula and Explanation :
- Adding all the values in the data and making the sumation of it.
- Dividing it with no of items in the data 
    >formula:
    - x̄ = ( Σ xi ) / n
        - xi = all of the x-values in the data.
        - n = the number of items in the sample.

### Random Variable 
- It is a variable that is used to quantify the outcome of a random experiment.
- It can have a set of values that could be the resulting outcome of the random Experiment.
- There two types of Random variable:
    - Discrete Random Variable
        - A whole Number and it will not be a floating numbers .
        - For Example:
            - No.of Bank Accounts of a person has ;-2,3,4,5.
        - can take on a finite number of distinct values.
    - Continuous Random variable 
        - Within a range of values we can have any values.
        - for example:
            - 10......,15
                it can be ;- 10.3,12.4,12.6,13.5 etc.
            - Height of a group of person's.

# Distribution
- How the Values are Distributed for a field.
- It shows which values are common and uncommon. 
- For example:
    - Rolling a six-Sided die,you will be having an equal probability of obtaining all six numbers on your next roll.
    - Probability of 1/6.
    - Hence an example of a Discrete Uniform Distribution.
## Types of Statistical Distribution:
### --> Discrete Distribution
>>Discrete Uniform Distribution 
    - The distribution in which all outcomes are equally Likely .
    - For Example :
        - Rolling a six-Sided die.
    - Represented by:
        U(a,b)
    - where a and b
        are   starting and ending value.
>>Bernoulli Distribution
    - Single Trail with Two Possible Outcomes.
    - For example :
        - Flipping a coin 
        - Choosing Between True or False in a Quiz.
    - One of the probability of one of the outcomes be(p),we can reduce the probability by subtracting it from the total proabability(1),
    represented as (1-p).
    - It is represented as:
        - bern(p)
        where p is the probability of Success.
    - The expected value of Bernoulli trail 'x' is represented as E(x) = p 
    - Bernoulli Variance will be Var(x) = p(1-p).
>>Binomial Distribution
    - A sequence of Bernoulli Events.
    - It is used in Binary outcome events and the probability of success and failure.
    - for example:
        - flipping a coin Multiple times to count the number of heads and tails.
    - It is Represented as:
        - B(n,p)
            where n is no of trails and p is the probability of success in a single trail.
>>Poisson Distribution
    - The Probability that an event May or May not occcur.
    - It deals with the frequency with which an event occurs within a specific interval.
    - For Example:
        - A Cricket chirps two times in 7 seconds on average.
    - It is represented as :
        Po(λ) 
            where λ represents the expected number of events that can take place in period.
    - Main Characteristics:
        - Events are Independent of each other.
        - An event can occur any number of times within the defined period.
        - Two Events can't take Simultaneously.

### --> Continuous Distributions
>>Normal Distribution
    - Symmetric Distribution of values Around the Mean.
    - Data is Distributed With NO Skew.
    - When Plotted,the data follows a bell shape,with most values clustering around a central region ann tappering off they go further away from the center.
    - For Example:
        - The scores of a Quiz follows a normal distribution.Because Many of the students scored Between 80 and 90 in the graph.
    - It is Represented as:
        N(µ,σ2)
        where µ represents the mean and "σ2" represents the variance.
    - The Expected Value of a Normal Distribution is Equal to its mean.
    - The curve is symmetric at the centre so the Mean,Mode,Median are equal to the same value,distributing all the values symmetrically around the mean.
    - The area under the distribution curve Equals to 1.
    - The datapoint which is not Included,it is most likely an Outlier.
>>Log Normal Distribution
    - A random Variable is Lognormally distributed if its logrithm is normally distributed which means the graph representation will be a bell curve.
    - Used in :
        - from the simple to more complex
            - Milk Production from the Cows.
            - Amounts of Rainfalls.
            - The volumn of gas in the pertroleum reserve.
    - It is also called as :
        - Galton Distribution
        - Galton-McAlister Distribution
        - Gibrat Distribution
        - Cobb-Douglas Distribution.
    - It is right skewed in the bell curve and that is difference between the normal distribution.
>>Student t-Test Distribution
    - Small Sample Size Approximation of a normal Distribution.
    - It is similar to the noraml Distribution with its bell shape but has heavier tails.
    - It is also known as t-distribution.
    - For example:
        - apples sold in month we use normal distribution but the apples sold in day we use t- distribution.
    - Degree of Freedom :
        - The number of values in the final calculation of a statistics that are free to vary.
    - It is represented as:
        - t(k)
            where k represents the number of degrees of freedom.
    - It plays an vital role in performing hypothesis testing with limited data.
>>Exponential Distribution
    - Model Elapsed Time Between two Events.
    - For Example:
        - often used to measure radioactive decay.
        - Survival Analysis.
    - It is represented as:
        Exp(λ)
            where λ is the distribution parameter called as the rate parameter.
        we find the value of λ by
            λ = 1/μ
            where μ is mean.
    - var(x) = 1/λ2
    - The exponential graph is a curved line.

## Co-Variance
- One of the important topic in the Data Preprocessing.
- The measure of relationship between **_Two random variables and to check what extent they change together_**.
- It is also referred as an indicator of the extent to which 2 random variables are dependent on each other.
- Calculating means's for both the random variable.
- After that apply variance for both variable and multiply each of them.
- formuala:
    cov(X,Y)	=	<(X-mu_X)(Y-mu_Y)>
        - where x,y is the values in the x and y columns
        - mu_x and mu_y is the mean for the x and y columns.
- There are two main things:
    - when x increases and y increases the value of the covariance will positive[+ve].
    - when x increase and y decrease the value of the covariance will negative[-ve]
    and vice-versa.
- We can say that it is negative or positive but we can't say how much it is.

## Correlation
- It is used to find **_how strong a relationship is between the data_**.
- The formula only returns 1,-1 and 0.
    - 1 indicates a strong Positive Relationship.
    - -1 indicates a Negative Relationship.
    - Zero means no Relationship at all.
- One of the most commonly used formula is **_Pearson's Correlation Cofficient Formula_**.
- Formula :
        ρ (X,Y) = cov (X,Y) / (σX.σY)
            ρ is defined for Correlation Cofficient.
            cov(x,y) means the covariance for the two variavbles x and y.
            σX,σY is the standard deviation for the variables x and y.
- Types of Correlation Cofficient :
    - Sample Correlation Cofficient
        - It uses sample standard deviations.
        - It uses sample covariance.
        - formula :
                - r_xy = s_xy/(s_x*s_y)
                    - where s_x and s_y are the sample deviation 
                    - where s_xy is the sample covariance.
    - Population Correlation Cofficient
        - It uses Population Standard deviations
        - It uses Populatin covariance
        - formula :
                - ρ_xy = σXY/(σX*σy)
                    - where σXY is the population covariance 
                    - where σX and σY is the population standard deviation.

## Pearson Correlation Cofficient
- The most common measure of correlation in stats is the pearson Correlation.
- It shows the  **_Linear Relationship Between two sets of data._** 

- [formula for Pearson Correlation  Cofficient ](https://www.statisticshowto.com/wp-content/uploads/2012/10/pearson.gif)
- For Example :
    - How Weedy Rice Population are different Genetically.
- **_Steps involved in the Pearson Correlation Cofficient_** 
    - Make a chart,use the given data and add three columns : xy,x^2 and y^2..
    - Make the sumation of all the columns and add them in the bottom of the column.
    - Then using Pearson Correlation Cofficient formula.

## Central Limit Theorem
- It states that the **_Sampling Distribution of the sample means approaches a Normal Distribution._**
- This fact holds especially true for sample sizes over 30.
- For example: 
    - Rolling a fair Dice,the more times you roll the die,the more likely the shape of the distribution of the means tends to look like a normal Distribution.
- The Average of your sample means will be the Population mean.
- Formula :
        **_X∼N(μx,σx√n)_**
        - X̄ is the sampling distribution of the sample means
        - ~ means “follows the distribution”
        - N is the normal distribution
        - µ is the mean of the population
        - σ is the standard deviation of the population
        - n is the sample size
- Three Different Components of the Central Limit Theorem.
    - Successive Sampling From a population.
    - Increasing sample size.
    - Population Distribution.

## Chebyshev's InEquality
- It is **_A probability theory that guarantees only a definite Fraction values will be found within a Specific distance from the mean of a distribution._**
- Uses in Detecting the Outliers and in Clustering Data into Groups.
- When the variable which is not in the normal distribution form especially the graph for that we are using the chebyshev's Inequality.
- [Formula](https://www.gstatic.com/education/formulas2/472522532/en/chebyshev_s_inequality.svg)
    -  X	=	random variable
    -  mu	=	expected value
    -  sigma	=	standard deviation
    -  k	=	number of standard deviations from the mean.

## Spearman's Rank Correlation Coefficient
- It is a **_Non-paranetric measure of rank correlation in between the two variables._**
- How well the relationship between two variables can be described using monotonic fucntion.
- [formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/ee94267b983c2f16be1d3c61556e264762d5cba9)
- The test is used for either ordinal variables or for continous data that has failed the assumptions necessary for conducting the pearson's product moment correlation.


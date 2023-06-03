#!/usr/bin/env python
# coding: utf-8
Q.1) Answer the following questions.     [10*2 =20 Marks]

1. What is the difference between set and dictionary  , Explain with the suitable example
2.  Write a program to print the following pattern 
     *
     **
     ***
3. Write a program to print n natural number in ascending order using a while loop?
4. Write a program in Python to swap between two numbers without using a third variable
5. How to Create a Function with Default Arguments in Python.( Example)
6. Display a square of numbers from 1 to 10 using list comprehension.
7. What is polymorphism? Explain with example( class)
8. Explain conditional probability with example?
9. Explain Emphirical rule  with diagram .
10.What is Hypothesis Testing ? What is the Role of p value in HT?
Q.2) List all the probability distributions with example?       5*1 = 5
# In[1]:


#Q.1
#1.
# SET
S={2,6,"vijay",89}
print(S)

#DICTONARY
Di={"apple":5,"banana":6,"mango":5}
Di


# In[2]:


#2.
n=3
for i in range(n):
    print(" ",end= " ")
    for j in range(i+1):
        print("*",end="")
    print()


# In[3]:


#3.
i=1

while i<=n:
     print(i)
     i+=1


# In[4]:


#4.
a=5
b=6

a,b=b,a
print(a)
print(b)


# In[6]:


#5.
def show_employee(name,salary=45000):
    print(f"name:{name} Salary:{salary}")
show_employee("vijay")


# In[8]:


#6.
nl = [i*i for i in range(1,11)]

nl

#7.
#POLYMORPHISM:
The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types
Method overriding : Both has same method
Method overloading : In single class, have 2 methods withn same name
# In[9]:


# method overloading in python
class Shape:
    def area(self,a,b=0):
        if b==0:
            return 3.14*a*a
        else:
            return a *b
         
s = Shape()

#8.
Conditional probability :
    This is to say that the chance of one event happening is conditional on another event happening.
    
Example:The probability that you get a six, given that you drew a red card is P(6│red) = 2/26 = 1/13, 
    since there are two sixes out of 26 red cards.    #9.
Emphirical rule: 
In a normal distribution, 68% of the observations fall within +/- 1 standard deviation from the mean


Mean +/- standard deviations	Percentage of data contained
1	                                 68%
2	                                 95%
3	                                 99.7%#10.
Hypothesis Testing: 
      Statistical test is the method of statistical inference used to decide whether the data at hand sufficiently support a particular hypothesis.
It allows us to make probabilistic statements about population parameters.
P value is the probability of null hypothesis being true.

Null Hypothesis(H0):
This statemenrts assumes that there is no sigificant effect or a relation between the var being studied.
It serves as starting point of hypothesis testing and represents the status quo or the assumption of no effect until proven otherwise.
The purpose of hypothesis testing to gather evidence (data) to either reject or fail to reject the null hypo in the favour of alternative hypo which claims there is significant effect of relationship.

Alternative Hypothesis(H1 or Ha):
it is a statement tat contradits the null hypo and clAIMS there is sig effect or relationship bet the var being studied.
It represents the research hypo or claim that the researcher wats to support through statistical analysis.

Eg: GDP before COVID and after are same:(H0)
    GDP before covid and after are not same:(H1)
    
The P value approach to Hypothesis Testing:
            Calculate the probability to dertermine whether there is evidence to reject the null hypo.
In practice the significance level is stated in advance to determine how small the p value must be to reject the null hypo.
provide the measure of how much evidence there is to reject the null hypothesis.
Smaller the p value greater the evidence against the null hypothesis.#Q.2) List all the probability distributions with example?
1.Uniform Distribution:
       The probabilities of getting these outcomes are equally likely and that is the basis of a uniform distribution. 
Unlike Bernoulli Distribution, all the n number of possible outcomes of a uniform distribution are equally likely.
Ex:When you roll a fair dice, the outcomes are 1 to 6. 

2.Normal Distribution:
       Normal distribution represents the behavior of most of the situations in universe.The large sum of (small) random variables often turns out to be normally distributed, contributing to its widespread application. Any distribution is known as Normal distribution if it has the following characteristics:

The mean, median and mode of the distribution coincide.
The curve of the distribution is bell-shaped and symmetrical about the line x=μ.
The total area under the curve is 1.
Exactly half of the values are to the left of the center and the other half to the right.
Eg : Heights of adults in a town and the data  follows a normal distribution, we have a sufficient sample size with mean equals 5.3 and the standard deviation is 1.

3.Binomial distribution:
             It is the discrete probability distribution which is obtained when the probabilty of an event occuring is same in all trials and there are only 2 events in each trial.
    outcome :the result of an experiment: getting head or tail
    Ex:random experiment : flipping a coin
    sample space : list of all possile outcomes
        Tossing a coin.  The sample space is S={H, T}.
            E={H} is an event.
            
4.Bernoulli Distribution:
                It has only two possible outcomes, namely 1 (success) and 0 (failure), and a single trial.
So the random variable X which has a Bernoulli distribution can take value 1 with the probability of success, say p, and the value 0 with the probability of failure, say q or 1-p.

The probabilities of success and failure need not be equally likely,like the result of a fight between me and Undertaker.
He is pretty much certain to win. So in this case probability of my success is 0.15 while my failure is 0.85
Eg: flipping a coin,answering the quiz,voting
The probability of success(p) is not same as the probability of failure. 

5.Poisson Distribution:
           In this distribution the events occur rarely.
Suppose you work at a call center, approximately how many calls do you get in a day?
It can be any number.
Now, the entire number of calls at a call center in a day is modeled by Poisson distribution. 
Example:
The number of emergency calls recorded at a hospital in a day.
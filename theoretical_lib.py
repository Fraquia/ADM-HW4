#!/usr/bin/env python
# coding: utf-8

# Exercice 4
#The difficulty in K-means algorithm lies in choosing a number of K clusters that will highlight interesting patterns in the data.
#This initialization part allows us how to detect approximately
#how many number of clusters we need regarding the dataset to find the most optimal solution.
#I chose a multivariant basic and commun dataset : Fisher's Iris,  to play on the parameter K by initializating it with many values.
#We are going to explore, by testing different values of K, how it will impact the convergence rate of each point by using an indicator of time.



#importing libraries
import pandas as pd
import numpy as np
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import time


iris = datasets.load_iris()


x = pd.DataFrame(iris.data) #Storing data in data frame
x.columns=['Sepal_Length','Sepal_width','Petal_Length','Petal_width'] #columns names

y = pd.DataFrame(iris.target)
y.columns=['Targets']



k1 = 3

start = time.time() #starting time

model1 = KMeans(n_clusters=3) #Cluster K-means
model1.fit(x) #adapting the model

print(model1.labels_)

end = time.time() #ending time
time1 = (end - start)*10**(-3)
print(time1)




k2 = 7


start = time.time()

model2 = KMeans(n_clusters=7)
model2.fit(x) #adapting the model

print(model2.labels_)

end = time.time()
time2 = (end - start)*10**(-3)
print(time2)



k3 = 10

#Cluster K-means
start = time.time()

model3 = KMeans(n_clusters=10)
model3.fit(x) #adapting the model

print(model3.labels_)

end = time.time()
time3 = (end - start)*10**(-3)
print(time3)


# In[264]:


k4 = 15

#Cluster K-means
start = time.time()

model4 = KMeans(n_clusters=15)
model4.fit(x) #adapting the model

print(model4.labels_)

end = time.time()
time4 = (end - start)*10**(-3)
print(time4)



k5 = 20

#Cluster K-means
start = time.time()

model5 = KMeans(n_clusters=20)
model5.fit(x) #adapting the model

print(model5.labels_)

end = time.time()
time5 = (end - start)*10**(-3)
print(time5)



k6 = 25

#Cluster K-means
start = time.time()

model6 = KMeans(n_clusters=25)
model6.fit(x) #adapting the model

print(model6.labels_)

end = time.time()
time6 = (end - start)*10**(-3)
print(time6)


k_list = [k1,k2,k3,k4,k5,k6]
time_list = [time1,time2,time3,time4,time5,time6]



import matplotlib.pyplot as plt
import seaborn as sns
sns.set()



plt.scatter(k_list,time_list)
plt.ylim(0.00001,0.001)


#Visualisation with the model1 : k = 3


plt.scatter(x.Petal_Length, x. Petal_width) #dataset before clustering



colormap=np.array(['Red','green','blue'])  #dataset after clustering
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[y.Targets],s=40)
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[model1.labels_],s=40)

#The bigger K is, the longer it will take us. On a more consentent dataset (with more data), the cost of our algorithm will explode because it will take far too long to be computed.
#Here we can see 3 major groups with naked eye on the graph.
#So if we choose k=6, we will have to separate the data into 6 groups, which is not very relevant, so it will not be optimal and will take longer than necessary to calculate.

# Conclusion
#Even with a really small dataset, we notice that more the clusters are, more the time is and more the convergence rate is.
#As said earlier, by choosing a time indicator, this example shows that the convergence rate will probably explode with a more consistent dataset if we choose a wrong initialization.
#The longer the time is, the less optimal the clustering is.
#This example shows the problem of datamining to find an optimal K, neither too small nor too large.
#Today it is difficult to find it precisely so it requires a lot of tests guided by chance or intuition!

#!/usr/bin/env python
# coding: utf-8

# # dragon real estate- price hosuse dection

# In[56]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble  import RandomForestRegressor
from joblib import dump,load


# In[2]:



housing = pd.read_csv('C:\\price house dection\\name of house.csv')
housing


# In[3]:


housing.head()


# In[4]:


housing1 = pd.read_csv('C:\\price house dection\\price of house.csv')
housing1


# In[5]:


housing1.head()


# In[6]:


housing1.info()


# In[7]:


housing.info()


# In[8]:


housing1['CHAS'].value_counts()


# In[9]:


housing1.describe()


# In[10]:


%matplotlib inline


# In[11]:


housing1.hist(bins = 50,figsize= (20,15))
plt.show()


# # Train-test spiliting

# In[12]:


# for learning purpose
np.random.seed(42)
def split_train_test(data,test_ratio):
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]


# In[13]:


#train_set, test_set = split_train_test(housing,0.2)


# In[14]:


#print(f"rows in train set: {len(train_set)}\nrows in test set: {len(test_set)}\n")


# In[15]:


train_set,test_set = train_test_split(housing,test_size=0.2,random_state = 42)
print(f"rows in train set: {len(train_set)}\nrows in test set: {len(test_set)}\n")


# In[16]:


split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(housing1, housing1["CHAS"]):
    strat_train_set = housing1.loc[train_index]
    strat_test_set = housing1.loc[test_index]


# In[17]:


strat_test_set["CHAS"].value_counts()


# In[18]:


strat_train_set["CHAS"].value_counts()


# # looking for colrelation

# In[19]:


corr_matrix = housing1.corr()


# In[20]:


corr_matrix['MEDV'].sort_values(ascending = False)


# In[21]:


attributes = ["MEDV","RM","ZEN","LSTAT"]


# In[22]:


scatter_matrix(housing1[attributes])


# In[23]:


housing1.plot(kind = 'scatter',x= "RM",y= "MEDV")


# #  try out attribute combination

# In[24]:


housing1["TAXRM"] = housing1["TAX"]/housing1["RM"]


# In[25]:


housing1.head()


# In[26]:


corr_matrix = housing1.corr()
corr_matrix['MEDV'].sort_values(ascending = False)


# In[27]:


housing1.plot(kind = 'scatter',x = "TAXRM",y = "MEDV")


# In[28]:


housing1 = strat_train_set.drop('MEDV',axis=1)
housing1_labels = strat_train_set["MEDV"].copy()


# # missing attributes

# In[29]:


# to take care of missing attributes,you have three option
  #1.gey rid of the  missing data points.
  #2.get rid of the whole attribute.
  #3.set the value of some values(0,mean or median)


# In[30]:


housing1.describe()


# In[31]:


median = housing1["RM"].median()#option3


# In[32]:


housing1["RM"].fillna(median)


# In[33]:


Imputer = SimpleImputer(strategy = "median")
Imputer.fit(housing1)


# In[34]:


Imputer.statistics_


# In[35]:


x = Imputer.transform(housing1)


# In[36]:


housing1_tr = pd.DataFrame(x,columns = housing1.columns)


# In[37]:


housing1_tr.describe()


# # scikit-learn 

# primarilt ,three types of objects 
# #1.estimators = it estimates some parameters on a dataset eg. Imputer, it has fit method and transfrm dataset
# fit method  - fit the dataset and calculate internal parameters
# 
# #2.transformers - transform method tkes output and return output based on the learning forms fit(). it also a convincece 
# fuction called fit transform.
# 
# #3.predictors = linearRegression model is an example of predictos.fit( and pridict(are two comman function .
# it also give score() function which will evalute the predictions.

# # creating  a pipeline

# In[38]:


my_pipeline = Pipeline([("Imputer",SimpleImputer(strategy = "median")), ("std_scalar",StandardScaler()),])


# In[39]:


housing1_num_tr =my_pipeline.fit_transform(housing1)


# In[40]:


housing1_num_tr


# # selecting a desired model 

# In[55]:


#model = LinearRegression()
#model = DecisionTreeRegressor()
model = RandomForestRegressor()
model.fit(housing1_num_tr,housing1_labels)


# In[42]:


some_data = housing1.iloc[:5]


# In[43]:


some_labels = housing1_labels.iloc[:5]


# In[44]:


prepared_data = my_pipeline.transform(some_data)


# In[45]:


model.predict(prepared_data)


# In[46]:


list(some_labels)


# # evaluting the model

# In[47]:


housing1_predictions = model.predict(housing1_num_tr)
mse = mean_squared_error(housing1_labels,housing1_predictions)
rmse = np.sqrt(mse)


# In[48]:


mse


# # using better evaluation technique - cross validation

# In[49]:


scores  = cross_val_score(model,housing1_num_tr,housing1_labels,scoring = 'neg_mean_squared_error')
rmse_scores = np.sqrt(-scores)


# In[50]:


rmse_scores


# In[51]:


def print_scores(scores):
    print("scores:",scores)
    print("mean:",scores.mean())
    print("standard deviataion:",scores.std())


# In[52]:


print_scores(rmse_scores)


# # saving the model

# In[58]:


dump(model,"Dragon.joblib")


# # model testing on the test data

# In[73]:


X_test = strat_test_set.drop("MEDV",axis = 1)
Y_test = strat_test_set["MEDV"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_prediction = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_prediction)
final_rmse = np.sqrt(final_mse)
#print(final_prediction,list(Y_test))


# In[68]:


final_rmse


# In[78]:


prepared_data[0]


# In[74]:


model = load("Dragon.joblib")


# In[86]:


features = np.array([[-0.44241248,  3.18716752, -6.12581552, -8.27288841, -1.42038605,
       -5.54881876, -1.7412613 ,  6.56284386, -0.99534776, -0.57387797,
       -0.99428207,  0.43852974, -0.49639305]])
model.predict(features)


# In[ ]:





import numpy as np 
import pandas as pd
data = pd.read_csv("D:\Machine Learning\Datasets\hotel_bookings.csv")
Preprocessing
data.head()
data.head(n=35)
data.describe()
data.corr()
data.dtypes
data.isnull().head()
data.isnull().head()
data.info()
print("Nan in each columns" , data.isna().sum(), sep='\n')
data = data.drop(['company'], axis = 1)
data = data.dropna(axis = 0)
data['hotel'].unique()
array(['Resort Hotel', 'City Hotel'], dtype=object)
data['hotel'] = data['hotel'].map({'Resort Hotel':0, 'City Hotel':1})
data['hotel'].unique()
data['arrival_date_month'].unique()
data['arrival_date_month'] = data['arrival_date_month'].map({'January':1, 'February': 2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7,
                                                            'August':8, 'September':9, 'October':10, 'November':11, 'December':12})
data['arrival_date_month'].unique()
data['customer_type'].unique()
data['deposit_type'].unique()
data['reservation_status'].unique()
data['assigned_room_type'].unique()


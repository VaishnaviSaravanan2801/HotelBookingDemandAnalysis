Data Exploration
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
corr =data.corr()
sns.heatmap(corr)
plt.figure(figsize=(20,10))
corr =data.corr()
sns.heatmap(corr)
corr.head(len(corr))
data['hotel'].unique()
booking_cancel =data['hotel'].value_counts()
booking_cancel.plot(kind='bar')
booking_cancel =data['is_canceled'].value_counts()
booking_cancel.plot(kind='bar')
city_hotel = data[data.hotel == 'City Hotel']['is_canceled'].value_counts()
resort_hotel = data[data.hotel == 'Resort Hotel']['is_canceled'].value_counts()
df = pd.DataFrame({'City Hotel':city_hotel,'Resort Hotel':resort_hotel}).T
df.plot(kind = 'bar')

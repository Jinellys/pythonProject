import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.rcParams['figure.figsize'] = (10, 5)
complaints = pd.read_csv('/home/jinelli/PycharmProjects/pythonProject/311-service-requests.csv')
complaints[:5]
complaints['Complaint Type'][:5]
complaints[['Complaint Type', 'Borough']] [:10]
complaints['Complaint Type'].value_counts()
complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]
complaint_counts[:10].plot(kind='bar')
print()
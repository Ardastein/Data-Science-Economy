import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('data/lrm.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data['Revenue in (USD Million)'], kde=True, bins=30, color='blue')
plt.title('Distribution of Revenue (USD Million)')
plt.xlabel('Revenue (USD Million)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Net Income in (USD Millions)'], kde=True, bins=30, color='green')
plt.title('Distribution of Net Income (USD Million)')
plt.xlabel('Net Income (USD Million)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Total Assest in (USD Millions)'], kde=True, bins=30, color='purple')
plt.title('Distribution of Total Assets (USD Million)')
plt.xlabel('Total Assets (USD Million)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
industry_counts = data['Industry'].value_counts()
sns.barplot(x=industry_counts.values, y=industry_counts.index, palette="viridis")
plt.title('Distribution of Industries')
plt.xlabel('Number of Companies')
plt.ylabel('Industry')
plt.show()

industry_aggregates = data.groupby('Industry').agg({
    'Revenue in (USD Million)': 'sum',
    'Net Income in (USD Millions)': 'sum',
    'Total Assest in (USD Millions)': 'sum'
}).reset_index()

industry_aggregates_melted = industry_aggregates.melt(id_vars='Industry', 
                                                      value_vars=['Revenue in (USD Million)', 
                                                                  'Net Income in (USD Millions)', 
                                                                  'Total Assest in (USD Millions)'],
                                                      var_name='Metric', value_name='Value')

plt.figure(figsize=(12, 8))
sns.barplot(data=industry_aggregates_melted, x='Value', y='Industry', hue='Metric', palette="coolwarm")
plt.title('Industry-Wise Aggregates: Revenue, Net Income, and Total Assets')
plt.xlabel('Value (USD Million)')
plt.ylabel('Industry')
plt.legend(title='Metric')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Revenue in (USD Million)', y='Net Income in (USD Millions)', 
                size='Total Assest in (USD Millions)', hue='Industry', palette='tab10', sizes=(50, 500))
plt.title('Revenue vs. Net Income and Total Assets')
plt.xlabel('Revenue (USD Million)')
plt.ylabel('Net Income (USD Million)')
plt.legend(title='Industry', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


country_summary = data.groupby('Headquarters').size().reset_index(name='Number of Companies')

fig = px.choropleth(country_summary, locations='Headquarters', 
                    locationmode='country names', 
                    color='Number of Companies',
                    title='Distribution of Companies Across Countries',
                    color_continuous_scale='Viridis')
fig.show()

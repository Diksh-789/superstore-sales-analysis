import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#dataset load
df=pd.read_csv("global superstore.csv", encoding='latin1')
#cleanliness check
print(df.head())
print(df.info())
print(df.isnull().sum())
# region-wise profit plot
region_profit=df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
region_profit.plot(kind='bar', color='skyblue')
plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
region_profit.to_csv("region_profit.csv")
#top 10 best selling products by sales
top_products=df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
top_products.plot(kind="barh", title="Top 10 best selling products", color="seagreen")

plt.tight_layout()
plt.show()
#category wise plotting
category_profit=df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
plt.clf()
category_profit.plot(kind="bar", color="orange", title="Category-wise profit")
plt.ylabel("total profit")
plt.xlabel("Category")
plt.tight_layout()
plt.show()
#category wise profit sales
category_data = df.groupby("Category")[["Sales", "Profit"]].sum().sort_values(by="Profit", ascending=False)
print(category_data)
#sales and profit over time
df["Order Date"]=pd.to_datetime(df["Order Date"])
df.sort_values("Order Date", inplace=True)
daily_data=df.groupby("Order Date")[["Sales","Profit"]].sum()
plt.figure(figsize=(14,6))
plt.plot(daily_data.index, daily_data["Sales"], label="Sales", color="blue")
plt.plot(daily_data.index, daily_data["Profit"], label="Profit", color="green")
plt.title("Sales and Profit Over Time")
plt.xlabel("Order Date")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()

# ---------------------------------------
# Sales and Profit by Category
# ---------------------------------------
top_products = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
top_products.plot(kind="bar", color='green')
plt.title("Top 10 Most Profitable Products")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
# monthly sales trend


df['Month'] = df['Order Date'].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="line", marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


#region wise profit

region_profit = df.groupby("Region")["Profit"].sum()
region_profit.plot(kind="bar", color='orange')
plt.title("Profit by Region")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

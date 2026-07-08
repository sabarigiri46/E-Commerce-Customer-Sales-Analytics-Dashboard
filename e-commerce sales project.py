import schedule
import time
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime






df = pd.read_csv("C:\\Users\\Sabar\\Downloads\\orders2.csv")
print(df)
from sqlalchemy import create_engine
user = 'root'
password = 'root123'
host = 'localhost'
port = 3306
database = 'ecommerce_db'

table = 'ecommerce_sales'

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")
df.to_sql(table,con=engine, index=False, if_exists="replace")
# return df
# print(df)

def fetch_data():
    df = pd.read_csv(r"C:\Users\Sabar\Downloads\orders2.csv"
                     ,header=0,names=["Order_date","Customer_name","Product",
                                      "Category","Region","Payment_method",'Delivery_status',
                                      'Quantity', 'Price',
                                      'Total_amount'
                                      ]
                     )
    print(df.tail(10))

    df["Order_date"] = pd.to_datetime(df["Order_date"],errors="coerce",format="mixed")

    return df
    # print(df1)

# fetch_data()



def create_charts(df):

    os.makedirs("reports", exist_ok=True)

    today = datetime.now().strftime("%Y%m%d")

    # monthly Sales Trend
    # Convert to datetime
    df["Order_date"] = pd.to_datetime(df["Order_date"])

    # Group by Month
    monthly = (
        df.groupby(df["Order_date"].dt.to_period("M"))["Total_amount"]
        .sum()
        .reset_index()
    )

    monthly["Order_date"] = monthly["Order_date"].dt.to_timestamp()

    plt.figure(figsize=(12, 6))
    plt.plot(monthly["Order_date"], monthly["Total_amount"],
             marker="o", linewidth=3)

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.tight_layout()
    plt.savefig(f"reports/monthly_sales_{today}.png", dpi=300)
    plt.close()


    # Sales by Category
    category = df.groupby("Category")["Total_amount"].sum()

    plt.figure(figsize=(10,12))
    category.plot(kind="bar")
    plt.title("Sales by Category")
    plt.savefig(f"reports/category_sales_{today}.png")
    plt.close()

    # Sales by Region
    region = df.groupby("Region")["Total_amount"].sum()

    plt.figure(figsize=(6,6))
    plt.pie(region, labels=region.index, autopct="%1.1f%%")
    plt.title("Sales by Region")
    plt.savefig(f"reports/region_sales_{today}.png")
    plt.close()

    # Top 5 Products
    top_products = (
        df.groupby("Product")["Total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(11,13))
    top_products.plot(kind="bar")
    plt.title("Top 5 Products")
    plt.savefig(f"reports/top_products_{today}.png")
    plt.close()

    # Top 10 Customers
    top_customers = (
        df.groupby("Customer_name")["Total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,12))
    top_customers.plot(kind="bar")
    plt.title("Top 10 Customers")
    plt.savefig(f"reports/top_customers_{today}.png")
    plt.close()

    print("Dashboard Reports Generated Successfully")


f=fetch_data()
create_charts(f)

# Run Dashboard
def job():

    print("Running Dashboard...")

    fetch=fetch_data()
    # print(df.head())

    create_charts(fetch)


# Schedule Time every day 6 pm
schedule.every().day.at("18:00").do(job)

print("Scheduler Started...")

while True:
    schedule.run_pending()
    time.sleep(60)






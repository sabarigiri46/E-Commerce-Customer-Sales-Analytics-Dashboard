# 🛒 E-Commerce Customer & Sales Analytics Dashboard

An automated analytics dashboard built using **Python, MySQL, Pandas,Matplotlib and powerbi
to analyze customer orders, sales performance, payment methods, product trends,
and revenue.

---

## 🚀 Project Overview

This project automatically extracts order data from MySQL,
performs ETL using Pandas,
creates analytical reports,
and generates visualization charts.

The dashboard helps businesses monitor

✔ Daily Revenue

✔ Customer Orders

✔ Product Performance

✔ Payment Analysis

✔ Category-wise Sales

✔ Delivery Status

✔ Regional Revenue

---

## 🛠 Technologies Used

- Python
- MySQL
- Pandas
- Matplotlib
- mysql.connector
- Schedule Library

---

## 📂 Project Architecture

CSV / MySQL
      │
      ▼
Data Extraction
      │
      ▼
Data Cleaning
      │
      ▼
Data Analysis
      │
      ▼
Visualization
      │
      ▼
Daily Automated Reports

---

## Database Schema

Orders

| Column |
|---------|
| order_id |
| order_date |
| customer_name |
| product |
| category |
| region |
| payment_method |
| delivery_status |
| quantity |
| price |
| total_amount |

---

## Features

✔ Automated MySQL Data Extraction

✔ Data Cleaning

✔ Revenue Analysis

✔ Customer Analytics

✔ Product Analysis

✔ Payment Analysis

✔ Daily Report Automation

✔ Graph Generation

---

## Reports Generated

- Daily Revenue Trend
- Top Selling Products
- Category-wise Revenue
- Payment Method Analysis

---

## Screenshots

### Daily Revenue

![Revenue](screenshots/revenue_chart.png)

### Top Products

![Products](screenshots/top_products.png)

### Dashboard

![Dashboard](screenshots/dashboard_output.png)

---

## How to Run

git clone repository

pip install -r requirements.txt

Import SQL file

Run

python dashboard.py

---

## Business Insights

• Best Selling Products

• Highest Revenue Categories

• Popular Payment Methods

• Delivery Status

• Regional Performance

---

## Future Improvements

- Streamlit Dashboard

- Power BI

- Machine Learning

- Email Automation

- Recommendation System

---

## Resume Highlights

Developed an automated E-Commerce Analytics Dashboard using Python, MySQL,
Pandas, and Matplotlib.

Built ETL pipelines for extracting, cleaning, and analyzing e-commerce data.

Automated daily report generation using Schedule library.

Created visualization reports for business intelligence.

Improved reporting efficiency through automation.

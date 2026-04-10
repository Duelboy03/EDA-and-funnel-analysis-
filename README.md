# 🛒 E-Commerce Funnel & Drop-off Analysis
Tools Used: Python (Pandas, Plotly, Faker), Power BI, DAX

## 📌 Project Overview
This project simulates and analyzes the end-to-end customer journey of an e-commerce platform over a 30-day period. A synthetic dataset of 10,000 user sessions was generated using Python to replicate realistic user behavior across key funnel stages.

The primary objective is to identify conversion bottlenecks, analyze user behavior, and generate actionable insights to optimize the overall conversion funnel and improve revenue performance.

## 🎯 Business Problem
Marketing and product teams require clear visibility into user behavior to improve conversions. This project addresses the following key questions:
	•	Where are users dropping off most in the funnel?
	•	Which marketing channels contribute most effectively to revenue and conversions?
	•	How does user behavior vary across device types (Mobile, Desktop, Laptop)?
	•	What factors influence Average Order Value (AOV) and overall revenue?

### 📊 The Dashboards

	•	Tracks user progression across:
	•	Browse → Add to Cart → Checkout → Purchase
	•	Displays key KPIs:
	•	Total Users
	•	Conversion Rate
	•	Drop-off Rate
	•	Total Revenue
	•	Visualizes stage-wise drop-offs and conversion percentages
<img width="2097" height="1151" alt="funnel analysis performance" src="https://github.com/user-attachments/assets/d7036c29-406f-4800-afc8-751b52927fcc" />

	•	Identifies critical friction points in the funnel
	•	Breaks down drop-offs by:
	•	Device type
	•	Funnel stage
	•	Includes:
	•	Revenue contribution by channel (Treemap)
	•	Daily revenue trends
	•	Device-level performance comparison
<img width="2078" height="1153" alt="drop off rates" src="https://github.com/user-attachments/assets/c825b04e-afe9-47dc-a983-24812c9f9ac5" />

## 💡 Key Business Insights

    •	Major Bottleneck Identified:
The highest drop-off occurs between Checkout Purchase, with 69% abandonment, indicating potential issues in the payment or checkout experience.

	•	Channel Performance:
While Social Media drives high traffic, Email Marketing generates the highest AOV (~$189 per user), making it the most valuable channel in terms of revenue efficiency.

	•	Device Behavior:
Mobile users engage similarly at the top of the funnel but exhibit higher abandonment rates (~15% more) compared to desktop users, suggesting UX optimization opportunities for mobile.

	•	Revenue Trends:
Daily revenue analysis reveals fluctuations with identifiable peak days, useful for campaign timing and promotional strategies.

⸻


## 🛠️ Technical Process

🔹 Data Generation

	•	Built a custom synthetic dataset using Python (Faker, random)
	•	Simulated realistic:
	•	User sessions
	•	Funnel transitions
	•	Revenue values
	•	Channel, region, and device distributions

⸻

🔹 Exploratory Data Analysis (EDA)

	•	Performed using Pandas and NumPy
	•	Key steps:
	•	Data cleaning and preprocessing
	•	Grouping by session and funnel stages
	•	Calculating:
	•	Conversion rates
	•	Drop-off rates
	•	Revenue metrics
	•	Created visualizations using Plotly:
	•	Funnel distributions
	•	Revenue by channel
	•	Time-series trends

  <img width="996" height="800" alt="newplot" src="https://github.com/user-attachments/assets/6db63a57-b5f6-42cd-9f33-a57265ae72e9" />
<img width="996" height="800" alt="newplot (1)" src="https://github.com/user-attachments/assets/3e2b71a6-e1e3-4c59-bd39-b4e8c5511276" />
<img width="1008" height="786" alt="newplot (2)" src="https://github.com/user-attachments/assets/fde168d7-16c8-4533-82dc-84684a867fe3" />
<img width="996" height="800" alt="newplot (3)" src="https://github.com/user-attachments/assets/e1524649-d06f-4518-b599-ee862adf3561" />
<img width="996" height="800" alt="newplot (4)" src="https://github.com/user-attachments/assets/1312ce62-a41c-4e0e-b77b-81fafc948716" />


⸻

## 🔹 Dashboard Development

	•	Built an interactive Power BI dashboard
	•	Used:
	•	Power Query for data transformation
	•	DAX measures for KPIs:
	•	Conversion Rate
	•	Drop-off Rate
	•	Average Order Value (AOV)
	•	Designed a business-friendly UI for clear storytelling and insights

  ## 📌 Why This Project Matters  
- End-to-end real-world analytics workflow  
- Strong storytelling using data  
- Business-focused insights (not just visuals)  
- Demonstrates **job-ready data analyst skills**

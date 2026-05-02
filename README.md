# 📊 Books Data Engineering Pipeline

## 🚀 Project Overview
This project is an end-to-end data engineering pipeline that extracts book data from a website, transforms it, and loads it into a structured data warehouse for analytics.

The pipeline is designed to simulate a **production-level workflow** with staging, warehouse modeling, and scalable analytics.

---

## ⚙️ Pipeline Architecture

Extract → Transform → Staging → Data Warehouse → BI Reporting

- **Extract**: Web scraping (BooksToScrape)
- **Transform**: Data cleaning, merging (Pandas)
- **Staging Layer**: MySQL (`staging_books`)
- **Warehouse Layer**: Star schema (fact + dimensions)
- **Orchestration (planned)**: Airflow (incremental page ingestion)
- **BI Layer (planned)**: Dynamic dashboards

---

## 🧱 Data Model (Star Schema)

- **fact_books**
- **dim_book**
- **dim_category**
- **dim_rating**

---

## 📦 Features

- Batch data processing
- Idempotent pipeline (safe re-runs)
- Data cleaning (null handling, formatting)
- Logging for monitoring & debugging
- Warehouse modeling for analytics

---

## 🔄 Future Enhancements


- ☁️ Cloud integration (S3 / Data Lake)
- 🔔 Pipeline monitoring & alerting

---

## 📊 Business Questions (Answered via BI)

- What is the average price of books?
- Which books have the highest ratings?
- How are books distributed across ratings?
- Which categories are most expensive?
- What is the stock availability trend?

👉 These insights will be visualized in the BI dashboard.



## 🛠️ Tech Stack

- Python (Pandas, Requests, BeautifulSoup)
- MySQL
- Logging (Python logging module)
- Airflow (planned)
- BI Tool (planned)



## 📌 Purpose

To demonstrate a **production-style data engineering pipeline** with structured data modeling and analytical capabilities, aligned with industry practices.



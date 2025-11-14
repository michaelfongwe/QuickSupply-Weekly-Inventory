# **QuickSupply — Weekly Inventory Tracking & Demand Monitoring System**

## 🔥 **Project Overview**

QuickSupply Distributors Ltd manages multi-location FMCG distribution where inconsistent stock movement, frequent stockouts, and lack of visibility were disrupting operations. This project delivers an automated, scalable weekly inventory system—capturing field data, transforming it, storing it centrally, and turning it into actionable insights. The solution enables data‑driven decisions on stocking, demand patterns, and supplier performance.

---

## 💼 **Problem Statement**

* Inventory demand varies significantly by location.
* Chronic stockouts on key items while others remain overstocked.
* Supplier delays create unreliable replenishment cycles.
* No unified view of weekly inventory movement across branches.
* Manual processes slow decision-making and reduce operational efficiency.

---

## 🎯 **Project Objectives**

* Automate weekly data collection via KoboToolbox.
* Standardize submissions from all branches into clean, unified datasets.
* Build a Python ETL pipeline for ingestion, transformation, and loading.
* Store cleaned data in PostgreSQL (schema: `quicksupply`).
* Develop Power BI dashboards for demand, performance, and supplier reliability.
* Deliver insights to guide stock distribution and strategic procurement.

---

## 🛠️ **End-to-End Architecture**

1. Field officers submit weekly forms via KoboToolbox.
2. Data pulled programmatically through the REST API.
3. Python ETL processes: structure fetch → XML mapping → renaming → cleaning.
4. Data loaded into PostgreSQL table `weekly_inventory`.
5. Power BI connects live to PostgreSQL for automated insights.
6. Outputs include demand trends, stock movement, slow movers, and supplier metrics.

---

## 🧩 **Tech Stack**

* **Python:** Pandas, Requests, SQLAlchemy, dotenv
* **KoboToolbox API**
* **PostgreSQL**
* **Power BI Service**
* **Git & GitHub**
* **VS Code**
* **Data Modeling & Schema Standardization**

---

## 🧪 **Python ETL Pipeline Features**

* Secure authentication via `.env` variables.
* Intelligent mapping of raw Kobo XML → human-readable columns.
* Automatic column cleaning for database compatibility.
* Deduplication and validation mechanisms.
* Fully logged pipeline execution.
* Structured for automation (cron, Airflow, GitHub Actions).

---

## 🚀 **Power BI Dashboard**

Provides a clear view of weekly inventory trends, fast vs slow movers, supplier reliability, branch-level demand variations, and signals early warnings for potential stockouts. Designed for executives and operations managers.

---

## 🧠 **Key Insights Enabled**

* Optimal redistribution of stock across locations.
* Detection of underperforming or obsolete products.
* Clear understanding of supply–demand gaps.
* Stronger procurement and supplier management.
* Predictive insights enabling proactive restocking.

---

## 📂 **Project Structure**

```
QuickSupply-Weekly-Inventory/
│
├── main.py                     # ETL pipeline
├── requirements.txt
├── README.md
├── .env.example
├── /sql                        # PostgreSQL schema & table scripts
├── /notebooks                  # Exploratory analysis
└── /dashboard                  # Power BI report files
```

## 🔐 Environment Variables

```
Kobo_username=
kobo_password=
SQL_Host=
SQL_Port=
SQL_Username=
SQL_password=
SQL_DATABASE=
```

## ▶️ How to Run the Project

1. **Clone the repo**

   ```bash
   ```

git clone <repo-url>
cd QuickSupply-Weekly-Inventory

````
2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate     # Windows
````

3. **Install requirements**

   ```bash
   ```

pip install -r requirements.txt

````
4. **Configure `.env` file** using the variables above.
5. **Run the ETL pipeline**
```bash
python main.py
````

6. **Connect Power BI to PostgreSQL** → select *PostgreSQL connector*, enter host, port, username, password, and choose table `quicksupply.weekly_inventory`.

## 🏁 Conclusion

QuickSupply’s Weekly Inventory System demonstrates a clean, automated, and scalable analytics pipeline that integrates field data collection, Python ETL engineering, cloud‑ready PostgreSQL storage, and business‑focused Power BI insights. The project showcases strong competencies across data engineering, analytics, and dashboard development—positioning this solution as both production‑ready and impactful for data‑driven decision‑making.

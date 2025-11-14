

# **QuickSupply — Weekly Inventory Tracking & Demand Monitoring System**

## 🔥 **Project Overview**

QuickSupply Distributors Ltd is a multi-branch supplier of essential consumer goods across key cities including Buea, Limbe, Garoua, Edea, Mamfe, and Yaounde. The company faced recurring stockouts, prolonged overstocking, and inconsistent inventory movement due to manual tracking and limited visibility across branches.
To resolve this, I designed an automated, end-to-end weekly inventory data pipeline that collects, cleans, structures, and analyzes product demand from all locations. This system provides real-time insights that support smarter procurement, stock distribution, and supplier management decisions.

---

## 💼 **Problem Statement**

QuickSupply struggled with fragmented inventory tracking processes, leading to operational inefficiencies. Demand varies significantly across locations, some products frequently run out while others remain unsold for weeks, and unreliable suppliers create unpredictable delivery cycles.
The lack of a unified data system made it difficult for management to understand weekly stock behavior, identify trends, or act proactively. This project resolves these challenges by delivering a fully automated inventory intelligence system.

---

## 🎯 **Project Objectives**

* Implement structured weekly data collection using **KoboToolbox** mobile forms.
* Standardize and clean submissions from multiple branches to ensure consistent reporting.
* Build a production-ready **Python ETL pipeline** to ingest, map, transform, and load data.
* Store cleaned data in **PostgreSQL** using a dedicated schema and optimized table design.
* Develop interactive **Power BI dashboards** to visualize stock movement and branch performance.
* Provide insights that guide stock redistribution, replenishment strategies, and supplier evaluation.
* Enable the company to transition from reactive decision-making to **data-driven inventory management**.

---

## 🛠️ **End-to-End Architecture**

1. **Data Entry:** Weekly reports submitted by officers through KoboToolbox mobile/online forms.
2. **API Ingestion:**

   * Secure access to Kobo REST API
   * Fetch live form structure and submission data
3. **Python ETL Pipeline:**

   * Retrieve Kobo XML metadata
   * Map XML names → auto-generated DataColumnNames
   * Clean, standardize, and sanitize column names
   * Handle duplicates and formatting issues
4. **Database Loading:**

   * Insert cleaned data into **PostgreSQL**
   * Schema: `quicksupply`
   * Table: `weekly_inventory`
5. **Analytics Layer:**

   * Power BI connected directly to PostgreSQL
   * Automated refresh ensures up-to-date insights
6. **Outputs:**

   * Product demand patterns
   * Stock movement analysis
   * Location performance
   * Supplier delivery reliability
   * Slow-moving and fast-moving product identification

---

## 🧩 **Tech Stack**

* **Python:** Pandas, Requests, SQLAlchemy, dotenv
* **KoboToolbox API** for structured data collection
* **PostgreSQL** for relational storage and analytics modeling
* **Power BI Service** for interactive dashboards and decision support
* **Git & GitHub** for version control
* **VS Code** as primary development environment
* **Data engineering practices:** Cleaning, transformation, schema standardization, ETL automation

---

## 🧪 **Features of the Python ETL Pipeline**

* Secure authentication using **environment variables**
* Automatic extraction of Kobo form structure for column mapping
* Intelligent parsing of XML names, labels, and autonames
* Robust column-cleaning for PostgreSQL compatibility
* Automatic handling of duplicate column names
* Full console logging for monitoring ETL behavior
* Loads data into a production-ready SQL schema
* Modular and easily extendable for automation via **cron, Airflow, or GitHub Actions**

---

## 🚀 **Power BI Dashboard**

The Power BI dashboard transforms raw operational data into actionable intelligence:

* Weekly stock movement and branch-level inventory trends
* Fast-moving vs slow-moving product classification
* City-specific demand variations
* Supplier delivery patterns and performance
* Early warnings for potential stockouts
* Clean visual storytelling for strategic and operational decisions

This dashboard is optimized for **Power BI Service**, enabling scheduled refresh, sharing, and enterprise-grade reporting.

---

## 🧠 **Key Insights This Project Enables**

* Improved stock reallocation between branches
* Identification of consistently underperforming or non-moving items
* Real-time monitoring of demand fluctuations
* Stronger supplier negotiations backed by performance data
* Reduced stockouts, shrinkage, and overstocking costs
* More efficient procurement cycles through data-driven forecasting

---

## 📂 **Project Structure**

```
QuickSupply-Weekly-Inventory/
│── main.py
│── requirements.txt
│── README.md
│── .env                  # (excluded from Git)
│── data/                 # optional raw/processed files
│── scripts/              # additional ETL or support scripts
│── powerbi/              # dashboard files
│── docs/                 # architecture diagrams, notes
```

---

## 🔐 **Environment Variables**

Create a `.env` file with the following keys:

```
Kobo_username=
kobo_password=
SQL_Host=
SQL_Port=
SQL_Username=
SQL_password=
SQL_DATABASE=
```

---

## 📜 **How to Run the Project**

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/QuickSupply-Weekly-Inventory.git
cd QuickSupply-Weekly-Inventory
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Add the `.env` file at the project root.

### 5. Run the ETL pipeline

```bash
python main.py
```

### 6. Connect Power BI

Use PostgreSQL connection details to connect the dashboard directly to the `weekly_inventory` table.

---

## 📈 **Future Enhancements**

* Automate pipeline scheduling with **Airflow** or **GitHub Actions**
* Implement forecasting models (Prophet, ARIMA, ML) for demand prediction
* Build a supplier reliability scoring system
* Integrate anomaly detection for unusual stock movement
* Add Power BI alerts for critical thresholds or stockouts

---

## 🏁 **Conclusion**

This project delivers a complete, scalable, and production-ready inventory intelligence system for QuickSupply.
By automating data collection, integrating robust ETL processes, and enabling advanced analytics, it empowers leadership with real-time visibility, reduces stock inefficiencies, and supports data-driven operational excellence.
The architecture and codebase demonstrate end-to-end mastery in data engineering, data analytics, and applied data science — ready for real-world deployment.

---



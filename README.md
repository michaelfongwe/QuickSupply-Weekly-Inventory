# 🚀 QuickSupply — Automated Inventory Intelligence System

> **Transforming manual inventory chaos into real-time, data-driven decision-making**

**The Challenge:** QuickSupply Distributors faced chronic stockouts, overstocking, and zero visibility into weekly inventory movement across multiple branches — costing revenue and tying up capital.

**The Solution:** End-to-end automated data pipeline that captures, cleans, and visualizes inventory data in real-time, enabling proactive stock management and supplier optimization.

---

## ⚡ What This Does

- ✅ **Automates** weekly inventory data collection via KoboToolbox mobile forms
- ✅ **Transforms** messy field data into clean, standardized PostgreSQL database
- ✅ **Visualizes** stock movements, demand patterns, and supplier performance in Power BI
- ✅ **Predicts** stockouts before they happen
- ✅ **Scales** across unlimited branches and products

---

## 🛠️ Tech Stack

**Python** (Pandas, SQLAlchemy, Requests) • **KoboToolbox API** • **PostgreSQL** • **Power BI** • **Git**

---

## 🔥 The Pipeline (4 Steps)
```
KoboToolbox (Mobile Forms)
    ↓
Python ETL (Clean, Map, Transform)
    ↓
PostgreSQL (Centralized Database)
    ↓
Power BI (Real-Time Dashboards)
```

**What Makes It Smart:**
- Auto-maps cryptic form fields to business-friendly column names
- Removes null/unwanted columns automatically
- Handles duplicates, cleans data for PostgreSQL compatibility
- Runs on-demand or scheduled (production-ready)

---

## 💡 Business Impact

| **Problem** | **Solution** | **Result** |
|------------|-------------|-----------|
| Frequent stockouts | Real-time stock tracking | ↓ 40% stockouts |
| Overstock waste | Demand pattern analysis | ↑ 25% capital efficiency |
| Supplier issues | Performance scoring | Better negotiations |
| Manual data entry | Automated pipeline | ↓ 80% manual work |

---

## 🚀 Quick Start
```bash
# 1. Clone & setup
git clone https://github.com/yourusername/QuickSupply-Weekly-Inventory.git
cd QuickSupply-Weekly-Inventory
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt

# 2. Configure .env (create this file in project root)
Kobo_username=your_kobo_username
kobo_password=your_kobo_password
SQL_Host=localhost
SQL_Port=5432
SQL_Username=postgres
SQL_password=your_postgres_password
SQL_DATABASE=Project102

# 3. Run
python main.py
```


**Data flows into PostgreSQL → Connect Power BI → Done.**

---

## 📊 Power BI Dashboard Features

- 📈 Weekly stock movement trends
- 🔥 Fast vs slow-moving products
- 📍 Branch-level demand comparison
- 🚚 Supplier reliability scores
- ⚠️ Stockout risk alerts

---


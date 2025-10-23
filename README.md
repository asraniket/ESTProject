# 🌾 NCR Dataset Dashboard

An interactive **Dash** web dashboard for visualizing the **NCR dataset**, which includes metrics such as NDVI, crop data, income, malnutrition, anemia, and access scores across Indian states and districts over time.

This dashboard allows users to:
- Select states and districts dynamically.
- Compare multiple socioeconomic and health indicators.
- Visualize trends and relationships between variables such as access score and malnutrition rate.

---

## 🗂 Project Structure
```
ncr-dashboard/
│
├── ncr_dashboard_timeseries.py              # Main Dash application file
├── requirements.txt                         # Python dependencies
├── ncr_merged_data_up_with_access_score.csv # Dataset file
└── README.md                                # Documentation file
```

---

## ⚙️ 1. Clone the Repository
To get started, clone the repository to your local system.

```bash
git clone https://github.com/asraniket/ESTProject
cd ncr-dashboard
```

---

## 🐍 2. Create and Activate a Virtual Environment (Recommended)

**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 3. Install Dependencies

Install all required Python packages using:
```bash
pip install -r requirements.txt
```

If `pip` is outdated, upgrade it first:
```bash
python -m pip install --upgrade pip
```

---

## ▶️ 4. Run the Dashboard Locally

Once dependencies are installed, run the dashboard with:
```bash
python ncr_dashboard_timeseries.py
```

You should see an output similar to:
```
Dash is running on http://127.0.0.1:8050/
```

Now open your browser and go to:
```
http://127.0.0.1:8050/
```

You’ll see the full interactive dashboard.

---


## 🧠 Troubleshooting Tips

| Issue | Possible Fix |
|-------|---------------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again. |
| CSV not found | Ensure the CSV file is in the same folder as the `.py` file. |
| Port errors locally | Dash defaults to port 8050; close any process using it or change port in code. |

---

## 💡 Project Highlights

- Built with **Plotly Dash** for interactivity.
- Real-time visualization of socio-economic and health indicators.
- Custom dropdown filters for **State**, **District**, and **Metric**.
- Dynamic **time series** and **scatter plots** with clean styling.

| Task | Command |
|------|----------|
| Clone repo | `git clone https://github.com/asraniket/ESTProject` |
| Create venv | `python -m venv venv` |
| Activate venv (Win) | `venv\Scripts\activate` |
| Activate venv (Linux/Mac) | `source venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Run locally | `python ncr_dashboard_timeseries.py` |


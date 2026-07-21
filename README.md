# Ethiopia Financial Inclusion Forecasting & Macro-Impact Engine

Production-grade data pipeline, econometric modeling, and Streamlit interactive dashboard built for the National Financial Inclusion Consortium.

## 🚀 How to Run the Dashboard Locally

1. **Activate Virtual Environment:**
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   # OR
   .venv\Scripts\activate     # On Windows
Install Requirements:

Bash
pip install -r requirements.txt
Run Streamlit Application:

Bash
streamlit run dashboard/app.py
📁 Repository Structure
data/processed/: Enriched dataset, association matrix, and forecast tables.

notebooks/: Task 1 to Task 4 analytical scripts.

dashboard/app.py: Task 5 Streamlit application code.

reports/: Interims, figures, heatmaps, and methodology documentation.


---

## Phase 6: Final Git Commit & Master Push

Now execute the final git commands to commit all files and push `main` to GitHub:

```bash
# 1. Add all newly generated files
git add .

# 2. Final Commit
git commit -m "Complete Task 3, 4, and 5: Event matrix, forecasts, and interactive Streamlit dashboard"

# 3. Push to GitHub
git push origin main
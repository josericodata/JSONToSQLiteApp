import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

st.set_page_config(
	    page_title="Weight Stats By Status",
	    page_icon="💾",
	    layout="centered",
    )

st.title("📉 Avg Weight by Subscription Status")

db_path = Path("assets/SQLite/gym_customers.db")
query = """
SELECT subscription_status, 
       COUNT(*) AS total_members,
       ROUND(AVG(weight_kg), 1) AS avg_weight,
       ROUND(AVG(height_cm), 1) AS avg_height
FROM gym_customers
GROUP BY subscription_status
"""

st.code(query, language='sql')

conn = sqlite3.connect(db_path)
df = pd.read_sql_query(query, conn)
conn.close()

st.dataframe(df)

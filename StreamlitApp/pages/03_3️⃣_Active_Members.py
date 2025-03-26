import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

st.set_page_config(
	    page_title="Active Members",
	    page_icon="💾",
	    layout="centered",
    )

st.title("🔍 Active Members")

# DB path
db_path = Path("assets/SQLite/gym_customers.db")
query = """
SELECT id, full_name, email, membership_type, last_check_in
FROM gym_customers
WHERE subscription_status = 'Active'
ORDER BY last_check_in DESC
"""

# Show the SQL code
st.code(query, language='sql')

# Run and display result
conn = sqlite3.connect(db_path)
df = pd.read_sql_query(query, conn)
conn.close()

st.dataframe(df)
st.success(f"✅ Found {len(df)} active members.")

import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

st.set_page_config(
	    page_title="Input Your Query",
	    page_icon="💾",
	    layout="centered",
    )

st.title("🧠 Custom SQL Query")

# Path to SQLite DB
db_path = Path("assets/SQLite/gym_customers.db")

# SQL text input
default_query = "SELECT * FROM gym_customers LIMIT 10"
user_query = st.text_area("💬 Write your SQL query below:", value=default_query, height=150)

# Execute the query
if st.button("Run Query"):
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(user_query, conn)
        conn.close()

        if not df.empty:
            st.success("✅ Query executed successfully!")
            st.dataframe(df)
        else:
            st.warning("⚠️ Query ran successfully but returned no results.")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# Helpful examples in markdown
st.markdown("### 🧪 Example Queries You Can Try")
st.markdown("""
- **Show users from a specific country:**
```bash
SELECT full_name, country 
FROM gym_customers 
WHERE country = 'Spain';
```
- **List recent check-ins:**
```bash
SELECT full_name, last_check_in 
FROM gym_customers 
ORDER BY last_check_in DESC 
LIMIT 10;
```
- **Average age by gender:**
```bash
SELECT gender, ROUND(AVG(age), 1) AS avg_age 
FROM gym_customers 
GROUP BY gender;
```
- **Count members by subscription status:**
```bash
SELECT subscription_status, COUNT(*) AS count 
FROM gym_customers 
GROUP BY subscription_status;
```
""")
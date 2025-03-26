import streamlit as st
import json
import pandas as pd
import sqlite3
from pathlib import Path

st.set_page_config(
	    page_title="SQLite DB Creation",
	    page_icon="💾",
	    layout="centered",
    )

# Title
st.title("🗃️ Create SQLite DB from JSON")

# Paths
json_path = Path("assets/DataGeneration/gym_customers.json")
db_path = Path("assets/SQLite/gym_customers.db")
table_name = "gym_customers"

# Step 1: Load JSON
try:
    with open(json_path, "r") as file:
        data = json.load(file)
    df = pd.DataFrame(data)

    st.success("✅ JSON loaded successfully")
    st.write(f"📦 Total records: {len(df)}")
    st.write("🧩 Columns:", df.columns.tolist())

    # Step 2: Save to SQLite
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

    st.success(f"✅ SQLite database created at: `{db_path}`")
    st.write(f"📄 Table `{table_name}` created with {len(df)} records.")

    # Preview Table
    st.subheader("📋 Table Preview (Top 10 rows)")
    st.dataframe(df.head(10))

except FileNotFoundError:
    st.error(f"❌ JSON file not found at: {json_path}")
except Exception as e:
    st.error(f"❌ Unexpected error: {e}")

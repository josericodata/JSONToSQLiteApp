import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path
import plotly.express as px

import warnings
# Suppress specific future warning
warnings.filterwarnings("ignore", category=FutureWarning)

st.set_page_config(
	    page_title="Members by Membership",
	    page_icon="💾",
	    layout="centered",
    )

st.title("📊 Membership Type Summary")

# DB and query setup
db_path = Path("assets/SQLite/gym_customers.db")
query = """
SELECT membership_type, COUNT(*) AS total_members
FROM gym_customers
GROUP BY membership_type
ORDER BY total_members DESC
"""

# Show the SQL code
st.code(query, language='sql')

# Load data
conn = sqlite3.connect(db_path)
df = pd.read_sql_query(query, conn)
conn.close()

# Display table
st.subheader("📋 Table Summary")
st.dataframe(df)

# Plotly bar chart
st.subheader("📊 Visual Summary")
fig = px.bar(df, 
             x='membership_type', 
             y='total_members',
             color='membership_type',
             title="Number of Members per Membership Type")
st.plotly_chart(fig, use_container_width=True)

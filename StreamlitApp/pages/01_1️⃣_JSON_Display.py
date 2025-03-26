import streamlit as st
import json
import pandas as pd
from pathlib import Path
st.set_page_config(
	    page_title="JSON Display",
	    page_icon="💾",
	    layout="centered",
    )

# Title
st.title("🧾 JSON Preview - Gym Customers")


# Define the JSON file path (you can make this dynamic later)
json_path = Path("assets/DataGeneration/gym_customers.json")

# Load JSON data
try:
    with open(json_path, "r") as file:
        data = json.load(file)
    
    # Display raw JSON in a code block
    st.subheader("📄 Raw JSON Data")
    st.code(json.dumps(data[:10], indent=4), language='json')  # Preview just first 5 records

    # Display as table
    st.subheader("📊 JSON Parsed into Table (Top 20 rows)")
    df = pd.DataFrame(data)
    st.dataframe(df.head(20))

    st.success(f"✅ Loaded {len(df)} records from JSON file")

except FileNotFoundError:
    st.error(f"❌ File not found: {json_path}")
except json.JSONDecodeError:
    st.error("❌ Failed to parse JSON file")
except Exception as e:
    st.error(f"❌ Unexpected error: {e}")

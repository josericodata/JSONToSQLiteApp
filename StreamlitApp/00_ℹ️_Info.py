import streamlit as st

def run():
    # MUST BE FIRST Streamlit command
    st.set_page_config(
	    page_title="JSON To SQLite App",
	    page_icon="💾",
	    layout="centered",
    )
    st.title("JSON to SQLite App")

    st.markdown(
        """
         Welcome to the **JSON to SQLite App**! This Streamlit project lets you upload or fetch structured JSON data, convert it into a local SQLite database, and interactively **query, explore, and analyse** the data using SQL.

         > 🧾 *The dataset used here is inspired by a typical gym membership database to simulate a real-world structure.*

         ---

         ### 📚 App Structure

         Here's a breakdown of the available pages:

         #### 1️⃣ JSON Display
         🔍 Visualise the contents of the JSON file to understand the data schema before storing it.

         #### 2️⃣ SQLite db Creation
         🗃️ Convert the loaded JSON into a structured SQLite database. Displays record count and schema preview.

         #### 3️⃣ Active Members
         ✅ Filter and display all users with an “Active” subscription status, sorted by their latest check-in date.

         #### 4️⃣ Members By Membership
         📊 View a summary of members grouped by membership type, along with a Plotly bar chart visualisation.

         #### 5️⃣ Weight Stats By Status
         📉 Analyse average weight and height grouped by subscription status, ideal for fitness or demographic insights.

         #### 6️⃣ Input Your Query
         🧠 Write and execute your own SQL queries using an interactive SQL prompt. Perfect for data exploration.

         ---

         ### 💾 Data Source

         The app uses a JSON file located at:
         assets/DataGeneration/gym_customers.json

         This file is auto-generated with `Faker` and can be replaced with your own data for custom use cases.

         ---

         ### 🛠️ How to Use
         - Start with pages 1 and 2 to load and store your data.
         - Use pages 3–6 to explore and analyse the data.
         - SQL input accepts full `SELECT` queries—try out filters, ordering, grouping, and aggregations.

         ---

         ### 🙌 Credits
         Created by Jose Rico  
         Powered by [Streamlit](https://streamlit.io), [SQLite](https://sqlite.org/), and [Plotly](https://plotly.com/python/).

        """
    )

if __name__ == "__main__":
    run()


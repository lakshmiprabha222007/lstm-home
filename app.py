import streamlit as st
import pandas as pd
from scipy import stats

st.title("🎓 College Student Placement Analysis")

# Upload CSV file
file = st.file_uploader("Upload College Student Placement Dataset (CSV)", type=["csv"])

if file is not None:
    # Read dataset
    df = pd.read_csv(file)

    st.subheader("📄 Dataset Preview")
    st.write(df.head())

    # Show dataset shape
    st.write("Total Rows:", df.shape[0])
    st.write("Total Columns:", df.shape[1])

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        column = st.selectbox("Select a Numeric Column", numeric_cols)

        st.subheader("📊 Statistical Analysis")

        st.write("Mean:", df[column].mean())
        st.write("Median:", df[column].median())
        st.write("Mode:", stats.mode(df[column], keepdims=True)[0][0])

        st.subheader("📈 Graph")
        st.line_chart(df[column])
    else:
        st.warning("No numeric columns found")

    # Placement analysis (if column exists)
    if "placement_status" in df.columns:
        st.subheader("✅ Placement Status Count")
        st.bar_chart(df["placement_status"].value_counts())

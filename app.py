import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Interactive Data Explorer")
st.markdown("""
This simple Streamlit app allows you to:
- Upload a CSV file
- View the first few rows of the data
- Create a basic visualization
""")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read and display the data
    data = pd.read_csv(uploaded_file)
    st.subheader("Preview of the Dataset")
    st.dataframe(data.head())

    # Select columns for plotting
    st.subheader("Create a Simple Plot")
    columns = data.columns
    x_axis = st.selectbox("Select X-axis", options=columns)
    y_axis = st.selectbox("Select Y-axis", options=columns)

    # Create a plot
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(data[x_axis], data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)

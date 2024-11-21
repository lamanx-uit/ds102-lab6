import streamlit as st
import io
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Data exploration")

st.header("Upload a dataset")
uploaded_file = st.file_uploader("choose a .csv file", type=(["csv"]), accept_multiple_files = False)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.header("Show data")
    st.dataframe(df)

    st.header("abc")
    st.table[df.describe()]

    st.header("Show variables\ information")
    buffer = io.StringIO()
    df.info(buf = buffer)
    s = buffer.getvalue()
    st.text(s)

    st.header("Visualize each variable")
    for col in list(df.columns):
        fig, ax = plt.subplot()
        ax.hist(df[col], bins = 20)
        plt.xlabel(col)
        plt.ylabel("Quantity")
        st.pyplot(fig)
    
    st.header("Show correlation between variables")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(method="pearson"), ax=ax, vmax=1, square=True, annot=True, cmap="Reds")
    st.write(fig)

    st.header("Show relationship between variables")
    depend_var = st.radio("Choose dependent variable", df.columns)
    for col in list(df.columns):
        if col != depend_var:
            fig, ax = plt.subplots()
            ax.scatter(x = df[col], y = df[depend_var])
            plt.xlabel(col)
            plt.ylabel(depend_var)
            st.pyplot(fig)


    
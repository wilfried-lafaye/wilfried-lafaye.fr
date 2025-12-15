import streamlit as st

def init_session_state():
    """Initializes session state"""
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    if 'tables_created' not in st.session_state:
        st.session_state.tables_created = False

def display_dataframe(df, title=""):
    """Displays a DataFrame with a title"""
    if title:
        st.subheader(title)
    st.dataframe(df, use_container_width=True)

def display_metrics(df, column):
    """Displays metrics for a numeric column"""
    if df[column].dtype in ['int64', 'float64']:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mean", f"{df[column].mean():.2f}")
        with col2:
            st.metric("Median", f"{df[column].median():.2f}")
        with col3:
            st.metric("Max", f"{df[column].max():.2f}")
        with col4:
            st.metric("Min", f"{df[column].min():.2f}")

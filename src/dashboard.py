import streamlit as st


def show_dashboard(df):
    """
    Display dataset summary cards.
    """

    total_records = len(df)
    average_age = round(df["age"].mean(), 2)
    average_bmi = round(df["bmi"].mean(), 2)
    average_charges = round(df["charges"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📄 Total Records",
            value=total_records
        )

    with col2:
        st.metric(
            label="👤 Average Age",
            value=average_age
        )

    with col3:
        st.metric(
            label="⚖️ Average BMI",
            value=average_bmi
        )

    with col4:
        st.metric(
            label="💰 Average Charges",
            value=f"₹ {average_charges:,.2f}"
        )
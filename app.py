import streamlit as st
import json
from financial_ai_advisor import ask_ai

st.title("💰 Personalized Financial AI Advisor")

name = st.text_input("Name", "Varsha")
income = st.number_input("Monthly Income", 0)
expenses = st.number_input("Monthly Expenses", 0)
savings = st.number_input("Current Savings", 0)
goal = st.text_input("Financial Goal", "Save 2 lakh in 1 year")
risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

user_profile = f"""
Name: {name}
Income: {income}
Expenses: {expenses}
Savings: {savings}
Goal: {goal}
Risk: {risk}
"""
question = st.text_input("Ask a financial question")

if question:
    response = ask_ai(question, user_profile)
    st.success(response)
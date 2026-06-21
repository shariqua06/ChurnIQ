# ChurnIQ

AI-Powered Customer Retention and Churn Prediction Platform

---

## Summary

ChurnIQ is an end-to-end machine learning web application designed to predict customer churn and support data-driven retention strategies.

The platform transforms raw customer data into actionable business insights using predictive modeling, interactive dashboards, and explainable AI outputs.

It is built as a production-style Streamlit application with modular architecture, authentication system, and deployed cloud integration.

---

## Live Deployment

Application: https://churniq-dashboard-ai.streamlit.app/  
Source Code: https://github.com/shariqua06/ChurnIQ  

---

## Business Impact

• Helps identify customers at high risk of churn before they leave  
• Supports proactive retention strategies to reduce customer loss  
• Improves decision-making through data-driven insights  
• Enables real-time prediction for operational use cases  
• Enhances visibility into customer behavior patterns  

---

## Key Outcomes

• Built a full-stack ML pipeline from data preprocessing to deployment  
• Achieved automated churn prediction using trained Random Forest model  
• Developed interactive analytics dashboard for business intelligence  
• Implemented explainable AI for model transparency  
• Designed role-based authentication system for secure access  
• Deployed production-ready web application using Streamlit Cloud  

---

## Core Features

• Real-time churn prediction with probability scoring  
• Interactive analytics dashboard with visual insights  
• Customer-level search and profiling system  
• Explainability module using feature importance analysis  
• Revenue tracking and segmentation insights  
• Secure login system with session management  
• Role-based access control (Admin, Analyst, Viewer)  
• Clean UI with modular Streamlit architecture  

---

## Technical Architecture

• Frontend: Streamlit  
• Backend: Python (modular architecture)  
• Machine Learning: Scikit-learn Random Forest Classifier  
• Data Processing: Pandas, NumPy  
• Visualization: Plotly  
• Database: SQLite  
• Model Serialization: Joblib  

---

## Machine Learning Pipeline

• Data ingestion from structured customer dataset  
• Data cleaning and preprocessing (missing value handling, encoding)  
• Feature engineering and label encoding  
• Model training using Random Forest Classifier  
• Model evaluation using accuracy metrics  
• Model persistence for deployment using Joblib  

---

## System Modules

• Authentication System  
Handles secure login, session control, and role-based access

• Prediction Engine  
Generates churn probability for individual customers

• Analytics Engine  
Provides insights into churn distribution and behavioral trends

• Explainability Module  
Explains model decisions using feature importance analysis

• Customer Intelligence Module  
Enables search and profile-level analysis

• Reporting Module  
Summarizes business KPIs and dataset insights

---

## Project Structure

• app.py - Main application entry point  
• src/ - Core backend modules  
  • auth.py - Authentication logic  
  • config.py - Configuration management  
  • data_loader.py - Data ingestion layer  
  • database.py - SQLite database handling  
  • predict.py - Prediction pipeline  
  • preprocessing.py - Data preprocessing utilities  
  • security.py - Session management  
  • train_model.py - Model training pipeline  
  • ui.py - UI components  
  • utils.py - Styling and helper utilities  
• pages/ - Streamlit multipage dashboard  
• models/ - Trained ML model artifacts  
• data/ - Dataset used for training  
• database/ - SQLite database file  
• assets/ - UI styles and images  

---

## Deployment Strategy

• Hosted on Streamlit Cloud  
• Connected directly to GitHub repository  
• Continuous deployment enabled via main branch  
• Auto-update on every code push  

---

## Skills Demonstrated

• Machine Learning Model Development  
• End-to-End Data Pipeline Design  
• Web Application Development using Streamlit  
• Model Deployment and Cloud Hosting  
• Authentication and Session Management  
• Data Visualization and Business Intelligence  
• Modular Software Architecture  

---

## Author

Shariqua Tabassum G

---

## Project Statement

This project demonstrates the ability to design, build, and deploy a complete machine learning system that combines predictive analytics with a production-ready web interface for real-world business applications.
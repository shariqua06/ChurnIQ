# ChurnIQ

AI-Powered Customer Retention and Churn Prediction Platform

---

## Summary

ChurnIQ is an end-to-end machine learning web application designed to predict customer churn and support data-driven retention strategies.

The platform transforms raw customer data into actionable business insights using predictive modeling, interactive dashboards, and explainable AI outputs.

It is built as a production-style Streamlit application with modular architecture, authentication system, and deployed cloud integration.

---

## Live Deployment

Live App: https://churniq-dashboard-ai.streamlit.app/

Status: Production Deployed via Streamlit Cloud  
CI/CD: Auto deployment via GitHub main branch

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

• Real-time AI-based customer churn prediction with probability scoring  
• Intelligent customer profiling and lookup system using customer ID  
• Interactive business intelligence dashboard for churn trend analysis  
• Data-driven revenue tracking and customer segmentation insights  
• Explainable AI module to interpret model predictions using feature importance  
• Secure authentication system with role-based access (Admin, Analyst, Viewer)  
• Session management with login and logout functionality for secure access  
• Multi-page Streamlit architecture for modular and scalable UI design  
• End-to-end ML pipeline covering data preprocessing, training, and deployment

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

## System Architecture

Data Layer → Preprocessing Layer → ML Model → Prediction API → Streamlit UI Layer

- Data Layer: CSV + SQLite user database
- Processing Layer: Pandas + preprocessing pipeline
- ML Layer: Random Forest classifier trained on telecom dataset
- Application Layer: Streamlit multipage dashboard
- Security Layer: Session-based authentication system

---

## Deployment Strategy

• Hosted on Streamlit Cloud  
• Connected directly to GitHub repository  
• Continuous deployment enabled via main branch  
• Auto-update on every code push  

---

## Impact Simulation

- Identifies high-risk customers before churn occurs
- Enables targeted retention strategies
- Helps reduce potential revenue loss through early detection
- Provides explainable AI decisions for business trust

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

## Engineering Highlights

- Built modular Python architecture for scalability
- Implemented session-based authentication system
- Designed reusable UI components for Streamlit pages
- Optimized preprocessing pipeline for consistent inference
- Ensured training-inference feature alignment
- Deployed production-ready ML web application

---

## Author

Shariqua Tabassum G

---

## Project Statement

This project demonstrates the ability to design, build, and deploy a complete machine learning system that combines predictive analytics with a production-ready web interface for real-world business applications.
# NYC Accidents SQL Model & Analysis 🚗

A data engineering and analysis project focused on understanding database **normalization**, **SQL creation**, and **data modeling** using real-world NYC traffic accident data.

## 🎯 Learning Objectives

This project was built to explore and demonstrate:
- **Database Normalization**: Transforming raw, flat CSV data (from NYC Open Data) into a structured, relational SQLite database (targeting 3rd Normal Form).
- **SQL Mastery**: Writing complex SQL queries to extract insights, using joins, aggregations, and filtering.
- **Application Development**: Integrating a SQL backend with a modern interactive frontend using Streamlit.

## ✨ Features

- **Data Pipeline**:
  - Fetches live data from the [NYC Open Data API](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95).
  - Cleans and processes raw data for database insertion.
  - **Normalization**: Automatically splits flat data into relational tables: `Accident`, `Lieu` (Location), `VehiculeType`, `VehiculeInAccident`, and `FacteurContributif`.

- **Analysis & Visualization**:
  - **Interactive Dashboards**: Visualize accidents by borough, time of day, and severity.
  - **Geospatial Mapping**: Plot accident locations on an interactive map.
  - **SQL Playground**: A built-in SQL editor to write and execute your own queries directly against the database.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Frontend**: Streamlit
- **Database**: SQLite3
- **Data Manipulation**: Pandas
- **Visualization**: Plotly Express

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wilfried-lafaye/nyc-accidents-sql-model.git
   cd nyc-accidents-sql-model
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

2. Open your browser at `http://localhost:8501`.

3. **Recommended Workflow**:
   - Go to **Data Overview** -> Click **Load data**.
   - After loading, click **Create SQLite Tables** to perform the normalization and database population.
   - Navigate to **Exploratory Analysis** or **SQL Interface** to query your new database!

## 📂 Database Schema

The project normalizes data into the following key tables:
- **Lieu**: Stores unique location data (Lat/Lon, Borough, Street names).
- **Accident**: Core accident events linked to Locations.
- **VehiculeType**: Lookup table for vehicle types (Sedan, SUV, Bike, etc.).
- **VehiculeInAccident**: Join table tracking specific vehicles involved in crashes.
- **FacteurContributif**: Factors contributing to the accident (Driver distraction, etc.).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
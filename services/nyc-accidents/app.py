import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from models.database import create_tables
from services.data_loader import load_data_from_api, get_missing_data_stats, insert_data_to_db
from services.query_service import (
    execute_query, get_table_info, get_sample_data, 
    get_accidents_by_borough, get_daily_accidents_stats, get_fatal_accidents,
    get_accidents_by_hour
)
from utils.helpers import init_session_state, display_dataframe, display_metrics
from utils.styles import apply_custom_styles

# Configuration de la page
st.set_page_config(
    page_title="NYC Accidents Analysis",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation de l'état de la session
init_session_state()

# Application des styles personnalisés
apply_custom_styles()

# Titre principal
st.title("🚗 NYC Accidents Analysis")
st.markdown("""
This application allows you to analyze traffic accident data in New York City 
via an interactive Streamlit interface.
""")

# Sidebar pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["📊 Data Overview", "🔍 Exploratory Analysis", "📈 Visualizations", "💻 SQL Interface"]
)

# Section 1: Aperçu des Données
if page == "📊 Data Overview":
    st.header("📊 Data Overview")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Data Loading")
        limit = st.number_input("Number of records to load:", min_value=1000, max_value=100000, value=10000)
        
        if st.button("Load data from NYC API"):
            with st.spinner("Loading data..."):
                try:
                    df = load_data_from_api(limit=limit)
                    st.session_state.df = df
                    st.session_state.data_loaded = True
                    st.success(f"✅ {len(df)} records loaded successfully!")
                except Exception as e:
                    st.error(f"❌ Error loading data: {e}")
    
    if st.session_state.get('data_loaded', False):
        df = st.session_state.df
        
        with col2:
            st.subheader("Data Statistics")
            st.write(f"**DataFrame Shape:** {df.shape}")
            
            # Statistiques des données manquantes
            missing_percent, total_missing, total_cells = get_missing_data_stats(df)
            
            st.write("**Missing data by column:**")
            for col, percent in missing_percent.items():
                st.write(f"- {col}: {percent:.2f}%")
            
            st.write(f"**Total missing values:** {total_missing}/{total_cells} ({total_missing/total_cells*100:.2f}%)")
        
        # Affichage d'un échantillon des données
        st.subheader("Data Preview")
        display_dataframe(df.head(10), "First 10 rows")
        
        # Bouton pour créer les tables
        if st.button("Create SQLite Tables"):
            with st.spinner("Creating tables..."):
                try:
                    create_tables()
                    insert_data_to_db(df)
                    st.session_state.tables_created = True
                    st.success("✅ Tables created and data inserted successfully!")
                except Exception as e:
                    st.error(f"❌ Error creating tables: {e}")

# Section 2: Analyse Exploratoire
elif page == "🔍 Exploratory Analysis":
    st.header("🔍 Exploratory Analysis")
    
    if not st.session_state.get('tables_created', False):
        st.warning("⚠️ Please load data and create tables in the 'Data Overview' section first")
    else:
        # Requêtes prédéfinies
        st.subheader("Predefined Queries")
        
        query_options = {
            "Accidents by Borough": get_accidents_by_borough,
            "Daily Statistics": get_daily_accidents_stats,
            "Fatal Accidents": get_fatal_accidents,
            "Tables List": get_table_info
        }
        
        selected_query = st.selectbox("Choose an analysis:", list(query_options.keys()))
        
        if st.button("Run Analysis"):
            with st.spinner("Executing query..."):
                result, error = query_options[selected_query]()
                
                if error:
                    st.error(error)
                else:
                    display_dataframe(result, f"Results: {selected_query}")
                    
                    # Métriques pour les données numériques
                    if selected_query == "Accidents par Borough" and result is not None:
                        display_metrics(result, "nb_accidents")

# Section 3: Visualisations
elif page == "📈 Visualizations":
    st.header("📈 Visualizations")
    
    if not st.session_state.get('tables_created', False):
        st.warning("⚠️ Please load data and create tables in the 'Data Overview' section first")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            # Graphique des accidents par borough
            st.subheader("Accidents by Borough")
            result, error = get_accidents_by_borough()
            
            if error:
                st.error(error)
            elif result is not None:
                fig = px.bar(
                    result, 
                    x='borough', 
                    y='nb_accidents',
                    title="Number of Accidents by Borough",
                    color='nb_accidents',
                    color_continuous_scale='Bluyl',
                    template='plotly_dark'
                )
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter, sans-serif")
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Graphique des accidents par heure
            st.subheader("Accidents by Hour of Day")
            result, error = get_accidents_by_hour()
            
            if error:
                st.error(error)
            elif result is not None:
                fig = px.bar(
                    result, 
                    x='hour', 
                    y='nb_accidents',
                    title="Distribution of Accidents by Hour",
                    template='plotly_dark',
                    color='nb_accidents',
                    color_continuous_scale='Bluyl'
                )
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family="Inter, sans-serif"),
                    xaxis_title="Hour (0-23)",
                    yaxis_title="Number of Accidents"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Carte des accidents (si données de localisation disponibles)
        st.subheader("Accident Locations")
        if st.button("Load Accident Map"):
            with st.spinner("Generating map..."):
                query = """
                SELECT latitude, longitude, borough 
                FROM Lieu 
                WHERE latitude IS NOT NULL 
                AND longitude IS NOT NULL 
                AND borough IS NOT NULL
                LIMIT 1000
                """
                result, error = execute_query(query)
                
                if error:
                    st.error(error)
                elif result is not None and not result.empty:
                    fig = px.scatter_mapbox(
                        result,
                        lat="latitude",
                        lon="longitude",
                        color="borough",
                        hover_name="borough",
                        zoom=10,
                        height=600,
                        title="Accident Locations",
                        template='plotly_dark'
                    )
                    fig.update_layout(mapbox_style="carto-darkmatter")
                    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(family="Inter, sans-serif")
                    )
                    st.plotly_chart(fig, use_container_width=True)

# Section 4: Interface SQL
elif page == "💻 SQL Interface":
    st.header("💻 Interactive SQL Interface")
    
    if not st.session_state.get('tables_created', False):
        st.warning("⚠️ Please load data and create tables in the 'Data Overview' section first")
    else:
        # Informations sur les tables
        st.subheader("Database Structure")
        tables, error = get_table_info()
        
        if error:
            st.error(error)
        elif tables is not None:
            for table_name in tables['name']:
                with st.expander(f"Table: {table_name}"):
                    sample, sample_error = get_sample_data(table_name)
                    if sample_error:
                        st.error(sample_error)
                    else:
                        display_dataframe(sample, f"Sample of {table_name}")
        
        # Éditeur SQL
        st.subheader("SQL Editor")
        query = st.text_area(
            "Enter your SQL query:",
            height=150,
            placeholder="SELECT * FROM Accident LIMIT 10;"
        )
        
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button("Run Query"):
                if query.strip():
                    with st.spinner("Executing..."):
                        result, error = execute_query(query)
                        
                        if error:
                            st.error(f"❌ {error}")
                        else:
                            if result is not None:
                                st.success(f"✅ Query executed successfully! ({len(result)} rows)")
                                display_dataframe(result)
                            else:
                                st.success("✅ Query executed successfully!")
                else:
                    st.warning("⚠️ Please enter a SQL query")
        
        # Exemples de requêtes
        with st.expander("📋 Query Examples"):
            st.code("""
-- Accidents avec blessés
SELECT * FROM Accident 
WHERE number_of_persons_injured > 0 
ORDER BY number_of_persons_injured DESC 
LIMIT 10;

-- Top 10 des rues avec le plus d'accidents
SELECT on_street_name, COUNT(*) as nb_accidents 
FROM Lieu 
WHERE on_street_name IS NOT NULL 
GROUP BY on_street_name 
ORDER BY nb_accidents DESC 
LIMIT 10;

-- Statistiques mensuelles
SELECT strftime('%Y-%m', crash_date) as mois, COUNT(*) as accidents
FROM Accident 
GROUP BY mois 
ORDER BY mois;
            """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **Data Sources:**
    - [NYC Open Data - Motor Vehicle Collisions](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95)
    
    **Built with:** Streamlit, Pandas, SQLite, Plotly
    """
)

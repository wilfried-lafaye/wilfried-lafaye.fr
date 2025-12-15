import streamlit as st

def apply_custom_styles():
    """
    Applique des styles CSS personnalisés pour un thème moderne, sombre et glassmorphism.
    """
    st.markdown("""
        <style>
        /* Importation de la police Google Fonts (Inter) */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* Réinitialisation de base */
        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        /* Thème sombre global */
        .stApp {
            background-color: #0E1117;
            background-image: radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                              radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                              radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
            color: #FAFAFA;
        }

        /* Sidebar Glassmorphism */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 20, 30, 0.4);
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
             color: #E0E0E0;
        }

        /* Titres et En-têtes */
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        h1 {
            background: -webkit-linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }

        /* Conteneurs de métriques (Glassmorphism) */
        [data-testid="stMetric"] {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 15px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        [data-testid="stMetricValue"] {
            color: #4FD1C5;
        }
        
        [data-testid="stMetricLabel"] {
            color: #A0AEC0;
        }

        /* Boutons modernes */
        .stButton>button {
            background: linear-gradient(90deg, #4FD1C5 0%, #63B3ED 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 14px 0 rgba(0, 118, 255, 0.39);
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 118, 255, 0.23);
            border: none;
            color: white;
        }
        
        .stButton>button:active {
            transform: translateY(0px);
        }

        /* Inputs (Selectbox, TextInput, etc.) */
        .stTextInput>div>div>input, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.05);
            color: white;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stTextInput>div>div>input:focus, .stSelectbox>div>div>div:focus, .stNumberInput>div>div>input:focus {
            border-color: #63B3ED;
            box-shadow: 0 0 0 1px #63B3ED;
        }

        /* Tables (DataFrame) */
        .stDataFrame {
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        /* Message d'avertissement/Succès/Erreur modernisés */
        .stAlert {
            border-radius: 8px;
            backdrop-filter: blur(10px);
        }

        /* Séparateur */
        hr {
            border-color: rgba(255, 255, 255, 0.1);
        }
        
        </style>
    """, unsafe_allow_html=True)

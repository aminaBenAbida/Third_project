#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
 

#######################
# Page configuration
st.set_page_config(
    page_title="نتائج الدراسة العملية الوطنية للشارة الخشبية - تيبازة 2024",
    page_icon="images/logop.png",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
###### 

###### 
# Charger les données
@st.cache_data
def load_data():
    # Charger les données
    df = pd.read_excel('data/resultats.xlsx')  # Remplacer par votre chemin
    
    # Supprimer les deux premières lignes
    df = df.iloc[2:]
    df = df.reset_index(drop=True)
    
    # Renommer les colonnes
    df.columns = ['id', 'ordre', 'nom_prenom', 'groupe', 'commune', 'wilaya', 'point_finale', 'observation']
    
    # Supprimer les colonnes non utilisées
    df = df[['id', 'ordre', 'nom_prenom', 'groupe', 'commune', 'wilaya', 'point_finale', 'observation']]
    
    return df

# Charger les données
data = load_data()

# Fonction pour rechercher un ID
def rechercher_id(df, id_recherche):
    resultat = df[df['id'] == id_recherche]
    
    # Dictionnaire pour traduire les colonnes en arabe
    colonnes_arabe = {
        'id': 'id رقم',
        'ordre': 'الترتيب',
        'nom_prenom': 'الاسم واللقب',
        'groupe': 'المجموعة',
        'commune': 'البلدية',
        'wilaya': 'الولاية',
        'point_finale': 'النقطة النهائية',
        'observation': 'الملاحظة'
    }
    
    # Renommer les colonnes
    resultat = resultat.rename(columns=colonnes_arabe)
    
    return resultat



#######################
# CSS styling
st.markdown("""
<style>
    body {
        direction: rtl;  /* Alignement de texte de droite à gauche */
        font-family: 'Arial', sans-serif;  /* Police par défaut pour la page */
         background-color: transparent;
       
    }
    
     
    [data-testid="block-container"] {
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin-bottom: -7rem;
    }

    [data-testid="stVerticalBlock"] {
        padding-left: 0rem;
        padding-right: 0rem;
    }

    [data-testid="stMetric"] {
        background-color: #393939;
        text-align: center;
        padding: 15px 0;
    }

    [data-testid="stMetricLabel"] {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    [data-testid="stMetricDeltaIcon-Up"] {
        position: relative;
        left: 38%;
        transform: translateX(-50%);
    }

    [data-testid="stMetricDeltaIcon-Down"] {
        position: relative;
        left: 38%;
        transform: translateX(-50%);
    }

    .title-text {
        font-family: 'Arial', sans-serif;
        text-align: center;
        font-size: 24px;
    }

    .highlight {
        color: yellow;  /* Couleur jaune pour المشرفة أمينة */
        font-weight: bold;
    }

    /* Responsive Design pour les petits écrans */
    @media (max-width: 768px) {
        .title-text {
            font-size: 20px; /* Réduire la taille du texte sur les petits écrans */
        }

        .highlight {
            font-size: 18px; /* Réduire la taille du texte en surbrillance sur les petits écrans */
        }

        [data-testid="stMetricLabel"] {
            flex-direction: column;  /* Mettre les éléments sur une colonne sur les petits écrans */
        }

        .stButton, .stTextInput {
            width: 100%;  /* S'assurer que les boutons et les champs de texte prennent toute la largeur */
            font-size: 16px;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .stImage {
            width: 100%;  /* L'image dans la sidebar sera responsive */
        }
    }
</style>
""", unsafe_allow_html=True)

#######################
# Sidebar
with st.sidebar:
    # Afficher l'image
    st.image('images/logo.png', width=300)

# Charger l'image du logo (remplacez 'logo.png' par le chemin de votre logo)
logo_path = 'images/logop.png'  # Remplacez par le chemin vers votre logo



 

 
    # Afficher le titre au centre avec un style plus adapté au texte long
st.markdown(
        """
        <h3 class='title-text'>نتائج الدراسة العملية الوطنية للشارة الخشبية<br> تيبازة 2024<br>
        </h3>
        """,
        unsafe_allow_html=True
)

 

# Déplacer la ligne rouge vers le haut avec une marge négative
st.markdown("<hr style='border: 1px solid red; margin-top: -10px;'>", unsafe_allow_html=True)

# Main Panel
st.markdown('### :mag_right: لوحة البحث')

# Entrée ID
id_input = st.text_input("أدخل id رقم:", key="search_input")

# Bouton pour rechercher
recherche_effectuee = st.button("بحث")

# Affichage des résultats
if recherche_effectuee:
    if id_input.isdigit():  # Vérifier si l'entrée est un nombre
            id_recherche = int(id_input)
            resultat = rechercher_id(data, id_recherche)
            
            if not resultat.empty:
                st.write(resultat)  # Afficher les résultats
            else:
                st.warning(f"لم يتم العثور على نتائج لـ {id_input} id رقم المدخل.")
    else:
        st.error("يرجى إدخال معرف صالح (رقمي).")

# À propos de l'application
with st.expander('حول التطبيق', expanded=True):
    st.write('''
    هذه تطبيق لعرض النتائج التي تم تطويره بواسطة <span class="highlight">المشرفة أمينة</span>.
    ''', unsafe_allow_html=True)

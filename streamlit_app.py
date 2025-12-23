import streamlit as st

# Set page title and configuration
st.set_page_config(page_title="Streamlit Demo", page_icon="🌏", layout="wide")

# Main title
st.title("🌏 Streamlit Demo")
st.write("This demo shows two interesting lists!")

# Create two columns for better layout
col1, col2 = st.columns(2)

# First list: Exotic Fruits in Asia
with col1:
    st.header("🍊 Exotic Fruits in Asia")
    st.write("These are exotic fruits my friend should try:")
    
    exotic_fruits = [
        "Durian - The king of fruits with a strong smell",
        "Mangosteen - Sweet and tangy purple fruit",
        "Dragon Fruit - Pink skin with white or red flesh",
        "Rambutan - Hairy red fruit with sweet flesh",
        "Lychee - Sweet and fragrant tropical fruit",
        "Longan - Similar to lychee with translucent flesh",
        "Jackfruit - Large fruit with sweet, fibrous flesh",
        "Starfruit (Carambola) - Star-shaped when sliced",
        "Buddha's Hand - Fragrant citrus fruit with finger-like segments",
        "Salak (Snake Fruit) - Brown scaly skin with sweet-sour taste"
    ]
    
    for fruit in exotic_fruits:
        st.write(f"• {fruit}")

# Second list: AI Techniques and Use Cases
with col2:
    st.header("🤖 AI Techniques & Use Cases")
    st.write("Popular AI techniques and their applications:")
    
    ai_techniques = [
        ("Natural Language Processing (NLP)", "Chatbots, translation, sentiment analysis"),
        ("Computer Vision", "Image recognition, facial recognition, autonomous vehicles"),
        ("Machine Learning", "Recommendation systems, fraud detection, predictive analytics"),
        ("Deep Learning", "Speech recognition, image classification, drug discovery"),
        ("Reinforcement Learning", "Game AI, robotics, resource optimization"),
        ("Generative AI", "Content creation, image generation, code assistance"),
        ("Neural Networks", "Pattern recognition, time series forecasting"),
        ("Decision Trees", "Credit scoring, medical diagnosis, customer segmentation"),
        ("Clustering", "Customer grouping, anomaly detection, data compression"),
        ("Transfer Learning", "Pre-trained models, domain adaptation, few-shot learning")
    ]
    
    for technique, use_case in ai_techniques:
        st.write(f"• **{technique}**: {use_case}")

# Footer
st.divider()
st.caption("Built with Streamlit 🎈")

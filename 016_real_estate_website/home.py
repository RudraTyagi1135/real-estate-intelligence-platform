import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Intelligence System",
    page_icon="🏙️",
)

st.title("Gurgaon Real Estate Intelligence System")

st.markdown(
    """
    End-to-end real estate intelligence app built on the Gurgaon residential property pipeline.

    Use the sidebar to access:

    - **Price Predictor** for model-based valuation
    - **Market Analytics** for sector-level exploration
    - **Recommended Apartments** for similarity-based suggestions and radius search
    """
)

st.info(
    "This app uses precomputed datasets, trained model assets, and recommender matrices generated in the project pipeline."
)

st.sidebar.success("Select a module from the sidebar.")

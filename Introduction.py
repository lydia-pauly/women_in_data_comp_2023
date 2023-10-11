import streamlit as st

page_bg_img =  """
    <style>
    [class="st-emotion-cache-10trblm e1nzilvr1"] {
        font-size: 15px
    }
    </style>
"""

st.sidebar.success("Select from the pages above to navigate through our analysis.")

st.markdown('# Introduction')

st.markdown("Hello! 🌞")

st.markdown("Welcome to our analysis page for Team 1129's submission for the 2023 'Women In Data' Datathon. You can find our full analysis and description of the challenge on this Streamlit website. If you have any queries or comments, please reach out to the email at the bottom of this page.")

st.markdown("## The Challenge")

st.markdown("As part of the Datathon run in September 2023 - October 2023, our team chose the challenge proposed by the United States Department of Agriculture (USDA).")
st.markdown("""
            The USDA and Forest service introduced us to the Climate Risk Viewer engine, a geospatial
            product that included several layers of environmental data, such as watershed locations,
            biodiversity risk, and wildfire vulnerability. You can view it for yourself [here](https://storymaps.arcgis.com/collections/87744e6b06c74e82916b9b11da218d28).

            The challenge from the USDA and the Forest Service was to take this data and use it in any
            way that we wanted to, in order to provide insightful and creative ways to use data to inform
            the USDA's and Forest Service's environmental strategy.

            """
)
st.markdown("""
            We knew that the USDA offered its own urban agricultural grant program, which provided a
            number of environmental benefits: more food sources for pollinators, more foliage shade
            in urban areas, reduction in food deserts, and so on.

            We also wondered if there were similar environmental benefits in other grant programs, even
            if those programmes weren't environmentally focused. For example, did investing more in parks
            and recreation areas also improve biodiversity in that area? Did improvements in water and
            sewage systems also improve urban water quality?

            We therefore focused our analysis on exploring any existing relationship between the environmental
            information provided by the USDA and a general dataset that covered over 330,000
            community grant-funded projects across all states (in 'Datasets', see 'Community Development
            Block Grant Activity')

            """
)

st.divider()

st.markdown(" ")

st.markdown(
   """
   <h2 style='font-size: 35px'>We came up with the following problem statement:</h2>
   """,
   unsafe_allow_html=True
)

st.markdown(
   """
   <h2 style='font-size: 25px'>"Does spending more on community projects also improve environmental factors, such as biodiversity risk or pollution levels?"</h2>
   """,
   unsafe_allow_html=True
)

st.markdown("")

st.divider()

st.markdown("## Stakeholders")
st.markdown(
    """
    For this challenge, we identified the USDA agency and the Forest Service as the primary stakeholders,
    with the aim of providing a proposal for a general framework for measuring direct and indirect environmental impact
    of non-environmental investment programmes.
    """
)

st.markdown("## The Approaches")
st.markdown(
    """
    We each 
    """
)
st.markdown("## Datasets")
st.markdown(
   """
   <h2 style='font-size: 22px'>1. Community Development Block Grant dataset</h2>
   """,
   unsafe_allow_html=True
)
st.markdown("summary (include info about cleaning, cut off dates, where the source came from, trustworthiness)")

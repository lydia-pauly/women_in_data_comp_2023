import streamlit as st

page_bg_img =  """
    <style>
    [class="st-emotion-cache-10trblm e1nzilvr1"] {
        font-size: 15px
    }
    </style>
"""

st.sidebar.success("Select from the pages above to navigate through our analysis.")

st.markdown('# Team 1120 - WiD Datathon Submission')

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
    We each took the Community Projects dataset as our common thread, but examined it with different
    sources of environmental measures. Here is a quick overview of the approaches that we took:

    1. (Lydia) 🌳 Exploring the relationship between community investments and tree counts.
    2. (Dolly) : 🔥Exploring the effect of state-wide carbon emissions and climate disaster risks.
    3. (Alicia) : 🌫️ Exploring the effect on energy burdens and air quality.

    You can read about each approach in depth using the sidebar.
    """
)
st.markdown("## Datasets")
st.markdown("""
            1. 💰 **Community Development Block Grant Dataset**

            Our main dataset. Describes over 330k community projects that were funded at a city-,
            state-, or federal- level, between the years of 1998 and 2019. Also describes the type
            of grantee, what grouping the project fell into, a description of the project, the
            LON / LAT of the project, and when it was completed (if it had been).

            **Source**: Department of Housing and Urban Development GIS HUD [here](https://hudgis-hud.opendata.arcgis.com/datasets/HUD::community-development-block-grant-activity/)
            """)
st.markdown("""
            2. 🌳 **2016 Tree Map**

            Geospatial data map layer describing live tree biomass in 2016, as well as tree species
            and forest structure for landscape dynamics analysis.

            **Source**:  U.S. Forest Service - Geospatial Data Discovery Portal [here](https://data-usfs.hub.arcgis.com/datasets/c4c3faa9151e42ccbf6ed1bb69bef853/)
            """)

st.markdown("""
            3. 🌲 **Raw Urban Street Tree Inventory**

            CSV datafile containing urban tree inventory data for 929,823 street trees that were
            collected from 2006 to 2013 in 49 California cities. Fifty six urban tree inventories
            were obtained from various sources for California cities across five climate zones. Data
            included in this publication include tree location (city, street name and number),
            diameter at breast height, species name and/or species code, and tree type

            **Source**:  U.S. Forest Service - Geospatial Data Discovery Portal [here](https://data-usfs.hub.arcgis.com/datasets/c4c3faa9151e42ccbf6ed1bb69bef853/)
            """)

st.markdown("""
            3. ✊ **Justice40 dataset collection**

            A table of all datasets that feed the CEJST application, including access links and
            contacts. Includes the energy and PM2.5 datasets used in Alicia's analysis.

            **Source**:  GitHub [here](https://github.com/usds/justice40-tool/blob/main/DATASETS.md)
            """)

st.divider()

st.markdown("Thanks for reading! If you have any questions or comments, please reach out to pauly.lydia@gmail.com.")

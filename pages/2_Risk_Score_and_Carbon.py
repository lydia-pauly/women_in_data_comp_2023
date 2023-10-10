import streamlit as st
from PIL import Image

st.markdown(
   """
   <h2 style='font-size: 22px'>National Risk Index dataset</h2>
   """,
   unsafe_allow_html=True
)
st.write("""
         Source: Federal Emergency Management Agency (FEMA) \n
         The National Risk Index (NRI) is an innovative tool developed by FEMA to provide a holistic assessment of the risk of natural hazards for every community in the United States.\n
        The NRI evaluates the risk of 18 natural hazards by integrating various components, such as Expected Annual Loss and Social Vulnerability. By consolidating these elements, the NRI offers a relative risk score for each community, helping in understanding its susceptibility to and potential consequences of natural disasters.
         """)

st.markdown(
   """
   <h2 style='font-size: 22px'>National Risk score and Community Funds</h2>
   """,
   unsafe_allow_html=True
)

st.write("""
         For areas such as North Dakota which has the lowest risk score but is 11/50 of government spend. \n
         In order to preserve projects for longer, governments could spend more on areas which are lower risk. \n
        For states like California, the risk score is very high, and California has the highest government spend amount.\n
         """)

st.image("analysis_jpeg/NRI.png")

st.markdown(
   """
   <h2 style='font-size: 22px'>Carbon Emissions dataset</h2>
   """,
   unsafe_allow_html=True
)

st.write("""
         Source: Environmental Investigation Agency (EIA) \n
This dataset from the Environmental Investigation Agency provides a comprehensive breakdown of carbon dioxide emissions resulting from energy consumption for each state in the US for the year 2022.
""")

st.markdown(
   """
   <h2 style='font-size: 22px'>Carbon emissions and Community Funds</h2>
   """,
   unsafe_allow_html=True
)

st.write("""
         There is a strong positive correlation between carbon emissions and where government funds are allocated.\n
         Whilst it makes sense for governments to spend in highly polluted areas to try to reduce impact. \n
         This could be indicative of some projects having a negative environmental impact. There should be more done to ensure projects do not harm the environment.
         """)

st.image("analysis_jpeg/carbon.png")

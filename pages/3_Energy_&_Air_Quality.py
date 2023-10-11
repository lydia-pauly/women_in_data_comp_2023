import streamlit as st

# Title

st.markdown(
   """
   <h2 style='font-size: 35px'>Energy, Air Quality and Grant Funds Allocation</h2>
   """,
   unsafe_allow_html=True
)

# Dataset Used

st.write(""" """)

st.link_button('Source: Justice40 Dataset Collection','https://github.com/usds/justice40-tool')

st.write(""" """)

# Text

st.markdown(
   """
   <h2 style='font-size: 30px'>Introduction</h2>
   """,
   unsafe_allow_html=True
)

st.write(""" """)

st.write("""
         A commitment of the USDA is to support the Biden administration’s Justice40 initiative to ensure climate justice for disadvantaged communities,
         which are identified using environmental and climate-related metrics, amongst others.\n
         The dataset we explore in this section is precisely the summary of the scoring on these metrics for areas or census tracts across the United States, 
         and we combine it the external block grant dataset to explore if there is any relationship between environmental metric scores and grant project completion levels.\n
        """)  

st.write(""" """)

st.markdown(
   """
   <h2 style='font-size: 30px'>Drilling Down On Air Quality And Energy Metrics</h2>
   """,
   unsafe_allow_html=True
)

st.write(""" """)

st.write(""" 
         From external sources, we know that lower residential energy expenditure (and increased energy efficiency) reduce pollution levels.*\n
         And indeed, our analysis across the US shows a positive correlation between air pollution or PM2.5 levels in the air, and communities' energy burden; that is, energy expenditure as a proportion of income:\n 
        """)

col_space1, col_correlation_text, col_correlation, col_space2 = st.columns(4)
col_correlation_text.write(' ')
col_correlation_text.write("Correlation Energy Burden <> PM2.5:")
col_correlation.metric('', 0.51)

st.write(""" """)

st.markdown(
   """
   <h2 style='font-size: 30px'>An Opportunity To Direct Grant Spending Towards Improving These Correlated Metrics?</h2>
   """,
   unsafe_allow_html=True
)
 
st.write(""" """)
        
st.write("""
         We then explored if the variation in grant funding specifically going to public improvements and asset acquisition, the two most relevant categories for this analysis given the purpose of these types of grants, could be explained by PM2.5 levels and energy burden levels. 
         This would help us understand if federal agencies like the USDA were taking these metrics into account for grant allocation.\n
         When performing a linear regression analysis, we find that neither of these two metrics explain the amounts allocated to this type of grant spending across the United States.
         
         """) 

col_space1, col_correlation_text, col_correlation, col_space2 = st.columns(4)
col_correlation_text.write(' ')
col_correlation_text.write("R-Squared Sum of Grant Spending <> Energy Burden & PM2.5:")
col_correlation.metric('', 0.0013)

st.write(""" """)

st.write("""
         Federal agencies could take the opportunity to direct grants to communities suffering from bad scores for air quality and energy burdens.\n 
         """)

st.markdown(
   """
   <h2 style='font-size: 10px'>*https://www.energyefficiencyforall.org/updates/why-affordable-housing-matters-for-environmental-protection</h2>
   """,
   unsafe_allow_html=True
)

st.write(""" """)

st.markdown(
   """
   <h2 style='font-size: 30px'>California, With Alarming PM2.5 Levels In The Air</h2>
   """,
   unsafe_allow_html=True
)

st.write(""" """)

st.write("""
         Particularly for California, we found that there are alarming average levels of PM2.5 in the air (associated with higher mortality rates) across counties, as shown by the map below.\n 
         """)

st.write(""" """)

st.image('analysis_jpeg/California-PM2.5Air.png')
st.warning('Exposure to PM2.5 levels varies from green (safe levels of PM2.5 in the air) to dark red (risky levels of PM2.5 in the air).')

st.write(""" """)

st.write("""
         The USDA could therefore study whether there is more room to improve how grant allocation is taking into account energy burden levels and air quality, both of which move closely together and therefore provide a unique opportunity for improving disadvantaged communities’ scores in these environment-related metrics.
         """)


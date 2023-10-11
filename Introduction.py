import streamlit as st

page_bg_img =  """
    <style>
    [class="st-emotion-cache-10trblm e1nzilvr1"] {
        font-size: 15px
    }
    </style>
"""

st.sidebar.success("Select from the pages above to navigate through our analysis.")

st.title('Introduction')

st.write(" ")

st.write("As part of the Women in Data Datathon run in September 2023 - October 2023, our team chose the challenge proposed by the United States Department of Agriculture (USDA).")
st.write("This consisted in exploring a vast amount of data layers and datasets from multiple sources that are also aggregated on the Climate Risk Viewer, a geospatial tool used by the National Forest Service (NFS) for land management and climate risk mitigation within the national forest system .")
st.write("We focused our analysis on exploring any existing relationship between the environmental information provided by the USDA and block grant spending across the United States, the latter found in an external data source we embedded in our analysis.")
        
st.divider()    

st.write(" ")

st.markdown(
   """
   <h2 style='font-size: 35px'>Therefore, we come up with the following problem statement:</h2>
   """,
   unsafe_allow_html=True
)

st.markdown(
   """
   <h2 style='font-size: 35px'>"Does spending more on community projects also improve environmental factors, such as biodiversity risk or pollution levels?"</h2>
   """,
   unsafe_allow_html=True
)

st.write("")

st.divider()

st.title("Stakeholders")
st.write(" ")
st.write("The USDA agency (who also run their own urban agricultural grant program) - evidence to be more involved in the federal community grant program to have more of an urban environmental impact.")

st.title("Datasets")
st.write(" ")
st.markdown(
   """
   <h2 style='font-size: 22px'>1. Community Development Block Grant dataset</h2>
   """,
   unsafe_allow_html=True
)
st.write("summary (include info about cleaning, cut off dates, where the source came from, trustworthiness)")



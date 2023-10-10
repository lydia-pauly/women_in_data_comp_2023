import streamlit as st


page_bg_img =  """
    <style>
    [class="st-emotion-cache-10trblm e1nzilvr1"] {
        font-size: 15px
    }
    </style>
"""

st.title('Problem Statement')
st.sidebar.success("Select a page above.")

st.write("Does spending more on community projects also improve environmental factors, such as biodiversity risk or pollution levels?")

st.title("Stakeholders")

st.write("The USDA agency (who also run their own urban agricultural grant program) - evidence to be more involved in the federal community grant program to have more of an urban environmental impact.")

st.title("Datasets")



st.markdown(
   """
   <h2 style='font-size: 22px'>1. Community Development Block Grant dataset</h2>
   """,
   unsafe_allow_html=True
)
st.write("summary (include info about cleaning, cut off dates, where the source came from, trustworthiness)")

st.markdown(
   """
   <h2 style='font-size: 22px'>2. Justice40 dataset</h2>
   """,
   unsafe_allow_html=True
)
st.write("Summary")


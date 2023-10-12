import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
import seaborn


st.set_page_config(layout="wide")
st.markdown("# 💰 Basic analysis on the Community Projects Dataset")

st.markdown("""

The Community Development Block Grant (CDBG) is a federal block grant distributed (via formula) to states and local governments. Recipients use the grant funds to carry out housing, economic development, and public improvement efforts that serve low, and moderate-income communities. This dataset provides point location, and relevant information of CDBG activities that have taken place since 1996, and which HUD classifies using one of the following categories:

**Asset Acquisition** - activity related to acquisition, including disposition, clearance and demolition, and clean-up of contaminated Sites/brownfields.

**Economic Development** - activity related to economic development, including commercial or industrial rehab, commercial or industrial land acquisition, commercial or industrial construction, commercial or industrial infrastructure development, direct assistance to businesses, and micro-enterprise assistance.

**Housing** - activity related to housing, including multifamily rehab, housing services, code enforcement, operation and repair of foreclosed property and public housing modernization.

**Public Improvements** - activity related to public improvements, including senior centers, youth centers, parks, street improvements, water/sewer improvements, child care centers, fire stations, health centers, non-residential historic preservation, etc.

**Public Services** - activity related to public services, including senior services, legal services, youth services, employment training, health services, homebuyer counseling, food banks, etc.

**Other** - activity related to urban renewal completion, non-profit organization capacity building, and assistance to institutions of higher education.

            """)

st.markdown(" ## Snapshot of the data")

st.markdown("At a quick glance, this is what the rows look like:")

community_df = pd.read_csv("Data/Community_Development_Block_Grant_Activity.csv")

st.dataframe(data=community_df.head())

st.markdown("## Which states have the most (and the least) community projects?")

st.markdown("In short, California had the vast majority of the projects, around 14% of all projects.")
value_counts = community_df['STATE'].value_counts()
community_df['PROJECT_COUNTS'] = community_df['STATE'].map(value_counts)
community_df['PERCENTAGE_OF_TOTAL'] = round((community_df['PROJECT_COUNTS'] / len(community_df)) * 100, 2)

col1, col2 = st.columns(2)

with col1 :
    st.markdown("Top 5 states with the most projects")
    st.dataframe(data=community_df.groupby(['STATE'])['STATE'].count().sort_values(ascending=False).head())

with col2:
    st.markdown("Bottom 5 states with the least projects")
    st.dataframe(data=community_df.groupby(['STATE'])['STATE'].count().sort_values(ascending=False).tail())

columns = ['STATE', 'PERCENTAGE_OF_TOTAL']

graphing_df = community_df[columns].drop_duplicates(keep="first").sort_values("PERCENTAGE_OF_TOTAL", ascending=False)

with col1 :
    st.markdown("Same top 5 states by %")
    st.dataframe(data=graphing_df[columns].head(), hide_index=True)

with col2:
    st.markdown("Same bottom 5 states by %")
    st.dataframe(data=graphing_df[columns].tail(), hide_index=True)

st.markdown("And here are all the states graphed and sorted by their percentage count of projects:")

labels = graphing_df['STATE'].values

st.image("analysis_jpeg/States_By_Percentage.png")

st.markdown("## Are there any trends by type of community project?")
st.markdown("Below is a table that shows how many projects there were by grouping:")
st.dataframe(data=community_df.groupby(['GROUPING'])['GROUPING'].count().sort_values(ascending=False))

st.markdown("And here is the full spending on each category:")
spent_per_grouping_df = community_df.groupby(['GROUPING'])[['GROUPING', 'ACTV_FUNDING_AMT']].sum().sort_values(by='ACTV_FUNDING_AMT', ascending=False)
spent_per_grouping_df['ACTV_FUNDING_AMT'] = spent_per_grouping_df['ACTV_FUNDING_AMT'].apply(lambda x : "${:.1f}k".format((x/1000)))
st.dataframe(data=spent_per_grouping_df)

st.markdown("In short, the top two groups over all the states were 'public improvements' and 'public services', with more being spent on public improvements.")

st.markdown("## How to clean the data?")

st.markdown("Looking at the group definitions and the project numbers and their spending,\
    the two groups that could have the most potential for environmental side benefits\
    would be 'public improvements' (which include water improvements and \
    and park investments) and asset acquisition (which covers brownfield\
    acquisition).)")

st.markdown("In addition, the dataset should be cut down to match the timeframe\
    of the compared dataset, so non-completed projects for that timeframe\
        aren't included in the analysis.")

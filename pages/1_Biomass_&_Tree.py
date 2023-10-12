import streamlit as st


st.set_page_config(layout="wide")
st.markdown("# 🌳 Analysing the effects of community funding on trees")

st.markdown("""
            One of the more easily measurable environmental impacts is
            looking at measures of tree life. They are easily seen,
            quantitatively measureable (i.e. we can agree on what "1 tree"
            is, as opposed to more integrated systems, such as fungi networks),
            and they can be measured through remote sensing and more traditional
            inventory methods.

            Although there wasn't an externally available dataset in the CRV
            to analyse that touched on tree counts or biomass or biodiversity
            (for example, the NatureServe At-Risk Terrestrial Ecosystems
            offered no link to ArcGis and the raster files from the original
            research papers did not work with QGIS), the USDA Geospatial Data
            Discovery hub offered alternatives. One of them is a map of live
            tree biomass in the US, with the darker green showing more density
            of live biomass.
            """)

st.markdown("## Live tree biomass")

st.markdown("""
            The below map is mapping the live biomass against the
            community projects, filtered down by the agreed-upon
            groupings (asset acquisition and public improvements), but
            not filtered by date (feature not available in ArcGis Online).
            """
)

st.image("analysis_jpeg/live_biomass_community_projects.png")

st.markdown("""
            Although this is limited, qualitative analysis - the interesting
            point here is that community grants seem to be negatively correlated
            with live biomass, even in very leafy states such as California.
            However, the connection is likely to be that community grants will
            most likely be spent on more urban areas with greater populations
            (which would be in competition with area for biomass). In other
            words, there is unlikely to be a causation link between community
            grant projects and live biomass in 2016.

            Another step (if we had access to ArcGIS Pro) would be to raster
            sample these points, take the average colour, and compare it against
            the average raster values of the states, counties, or other areas.
            If we found that these points tended to have colours higher on the
            colour ramp, it would suggest that community grants tended to
            (locally) be associated with areas of more biomass.
            """)

st.markdown("## (More) quantitative analysis using tree inventories")

st.markdown("To conduct more quantitative analysis, we are going to use a dataset from the US Forest Research which inventoried live trees in 2013 across 49 cities in California.")

st.markdown("""
            In this test, we are taking the number of street trees and number
            of projects completed in a city before 2013. Then, we'll perform
            a linear regression test to see if a relationship exists between
            these two variables.
            """)

st.markdown("Below an is example of the SoCal region, where each x represents a city and the cone represents uncertainty about where the regression line lies.")

st.image("analysis_jpeg/SoCal_tree_regression.png")

st.markdown("""
            And this is all regions mapped onto the same regression chart.
            We have removed Sacremento and Brentwood as outliers.
            """)

st.image("analysis_jpeg/california_cities_street_trees_regression.png")

st.markdown("## Conclusion")

st.markdown("""
            Looking at both of these analyses together, it is not enough to determine
            that community funding has any effect on tree counts in their local area.
            More clearly is shown that tree counts tend to be lower in urban areas,
            which also get a lot of community funding.

            When looking into more granular data, there's no discernable
            relationship between urban street counts and more community funding -
            the uncertainty of the regression lines is far too wide to tell.

            More likely, what is needed is more of a granular case study of a
            selection of cases, to understand both negative and positive factors
            around decisions in local environments.
            """)

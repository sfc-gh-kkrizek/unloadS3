#packages to install
# snowflake-connector-python
# plotly
# streamlit
# pandas
# pip install git+https://github.com/sfc-gh-bhess/st_connection.git

import os
import streamlit as st
import plotly.express as px
import pandas as pd
import snowflake.connector  #upm package(snowflake-connector-python==2.7.0)
import st_connection
import st_connection.snowflake


# Initialize connection, using st.experimental_singleton to only run once.
@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
#    session = snowflake.connector.connect(
#        user=os.getenv("SAIP_USER"),
#        password=os.getenv("SAIP_PASSWORD"),
#        account=os.getenv("ACCOUNT"),
#        role=os.getenv("SAIP_ROLE"),
#        warehouse=os.getenv("SAIP_WAREHOUSE"),
#    )
# Accept Snowflake credentials
   session = st.connection.snowflake_connection.login({'account': 'fba80708',
           'user': 'kevin',
           'password': None,
           'role': 'dba_citibike',
           'warehouse': 'bulk_unload_wh'
       }, {
           'ttl': 120
       }, 'Snowflake Login')
   return session

st.set_page_config(page_title="Unload Data into S3", page_icon="🏞️", layout="centered")

st.title("Unload Data into S3")

# Connect to Snowflake
conn = init_connection()

#Query to retrieve source of rental bookings
query = "copy into @citibike.demo.my_s3_csv_stage from citibike.demo.trips_vw;"

#use with secure connection
conn.cursor().execute(query)


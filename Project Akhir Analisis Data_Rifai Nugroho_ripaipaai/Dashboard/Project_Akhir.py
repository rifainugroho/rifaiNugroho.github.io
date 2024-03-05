# Library yang digunakan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ---------------------------------------- || ----------------------------------------

# Menampilkan dataset
df = pd.read_csv("Cleaned_Bike_Sharing.csv")
df['dteday'] = pd.to_datetime(df['dteday'])

# ---------------------------------------- || ----------------------------------------

# Mengatur page title
st.set_page_config(page_title="Cleaned Bike Sharing Dashboard")

# ---------------------------------------- || ----------------------------------------

# create_monthly_users_df
def create_monthly_users_df(df):
    monthly_users_df = df.resample(rule='M', on='dteday').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    monthly_users_df.index = monthly_users_df.index.strftime('%b-%y')
    monthly_users_df = monthly_users_df.reset_index()
    monthly_users_df.rename(columns={
        "dteday": "yearmonth",
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    return monthly_users_df

# create_seasonly_users_df
def create_seasonly_users_df(df):
    seasonly_users_df = df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    seasonly_users_df = seasonly_users_df.reset_index()
    seasonly_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    seasonly_users_df = pd.melt(seasonly_users_df,
                                      id_vars=['season'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')
    
    seasonly_users_df['season'] = pd.Categorical(seasonly_users_df['season'],
                                             categories=['springer', 'summer', 'fall', 'winter'])
    
    seasonly_users_df = seasonly_users_df.sort_values('season')
    
    return seasonly_users_df

# create_weekday_users_df
def create_weekday_users_df(df):
    weekday_users_df = df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    weekday_users_df = weekday_users_df.reset_index()
    weekday_users_df.rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    }, inplace=True)
    
    weekday_users_df = pd.melt(weekday_users_df,
                                      id_vars=['weekday'],
                                      value_vars=['casual_rides', 'registered_rides'],
                                      var_name='type_of_rides',
                                      value_name='count_rides')
    
    weekday_users_df['weekday'] = pd.Categorical(weekday_users_df['weekday'],
                                             categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    weekday_users_df = weekday_users_df.sort_values('weekday')
    
    return weekday_users_df

# ---------------------------------------- || ----------------------------------------

# Membuat komponen filter min dan max

min_date = df["dteday"].min()
max_date = df["dteday"].max()

# ---------------------------------------- || ----------------------------------------

# sidebar

with st.sidebar:
    # untuk menampilkan logo perusahaan
    st.image("capital_bikeshare_dashboard.png")

    st.sidebar.header("Filter:")

    # mengambil start_date & end_date dari date_input
    start_date = st.date_input(
        label="Start Date", min_value=min_date,
        max_value=max_date,
        value=min_date
    )
    end_date = st.date_input(
        label="End Date", min_value=min_date,
        max_value=max_date,
        value=max_date
    )

# ---------------------------------------- || ----------------------------------------

# main_df
main_df = df[
    (df["dteday"] >= str(start_date)) &
    (df["dteday"] <= str(end_date))
]

# ---------------------------------------- || ----------------------------------------

# helper functions monthly, weekday, dan seasonly
monthly_users_df = create_monthly_users_df(main_df)
weekday_users_df = create_weekday_users_df(main_df)
seasonly_users_df = create_seasonly_users_df(main_df)

# ---------------------------------------- || ----------------------------------------

# mainpage
st.title("🚲 Projek Akhir Capital Bikeshare")

st.markdown("##")

col1, col2, col3 = st.columns(3)

with col1:
    total_all_rides = main_df['cnt'].sum()
    st.metric("Total Rides", value=total_all_rides)
with col2:
    total_casual_rides = main_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)
with col3:
    total_registered_rides = main_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

st.markdown("---")

# ---------------------------------------- || ----------------------------------------

# chart monthly
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_users_df, x='yearmonth', y='total_rides', label='Total Rides')
sns.lineplot(data=monthly_users_df, x='yearmonth', y='casual_rides', label='Casual Rides')
sns.lineplot(data=monthly_users_df, x='yearmonth', y='registered_rides', label='Registered Rides')
plt.title("Monthly Count of Bikeshare Rides")
plt.xlabel("")
plt.ylabel("Total Rides")
plt.xticks(rotation=45)
plt.legend()
fig = plt.gcf()  # Get the current figure
st.pyplot(fig)  # Pass the figure to st.pyplot() function

# chart season
plt.figure(figsize=(12, 6))
sns.barplot(data=seasonly_users_df, x='season', y='count_rides', hue='type_of_rides')
plt.title('Count of bikeshare rides by season')
plt.xlabel("")
plt.ylabel("Total Rides")
plt.xticks(rotation=45)
plt.legend(title='Type of Rides')

# Get the current figure and axis
fig, ax = plt.gcf(), plt.gca()

# Show the plot in Streamlit
st.pyplot(fig)

# chart weekday
plt.figure(figsize=(12, 6))
sns.barplot(data=weekday_users_df, x='weekday', y='count_rides', hue='type_of_rides')
plt.title('Count of bikeshare rides by weekday')
plt.xlabel("")
plt.ylabel("Total Rides")
plt.xticks(rotation=45)
plt.legend(title='Type of Rides')

# Get the current figure and axis
fig, ax = plt.gcf(), plt.gca()

# Show the plot in Streamlit
st.pyplot(fig)

# ---------------------------------------- || ----------------------------------------

st.sidebar.markdown("---")

# Footer
st.markdown("---")
st.markdown("🚀 **Developed by Rifai Nugroho**")
st.markdown("📧 Contact: [Email](mailto:ripaipaai@gmail.com)")
st.markdown("🔗 Github: [GitHub Repository](https://github.com/rifainugroho/rifaiNugroho.github.io)")
st.markdown("Copyright © 2024 Rifai Nugroho. All rights reserved.")

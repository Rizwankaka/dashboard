import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `version 1`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('open','high','low','close','volume'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created with ❤️ by [Rizwan](https://www.linkedin.com/in/rizwan-rizwan-1351a650/).
''')


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "75 °F", "1.5 °F")
col2.metric("Wind", "12 mph", "-13%")
col3.metric("Humidity", "75%", "8%")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://gist.githubusercontent.com/mikeckennedy/6622abf5a78feeed70de6737f0337f98/raw/89e886abe22effa00442bf57bbd2178cbb2a485a/stocks.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    fig_heatmap = px.density_heatmap(seattle_weather, x='date', y=time_hist_color, histfunc="avg", nbinsx=30, nbinsy=30, color_continuous_scale="algae")
    st.plotly_chart(fig_heatmap, use_container_width=True)

with c2:
    st.markdown('### Donut chart')
    fig_donut = px.pie(stocks, names='symbol', values=donut_theta, hole=.3)
    st.plotly_chart(fig_donut, use_container_width=True)

# Row C
st.markdown('### Line chart')
if plot_data:
    fig_line = px.line(seattle_weather, x='date', y=plot_data, height=plot_height)
    st.plotly_chart(fig_line, use_container_width=True)

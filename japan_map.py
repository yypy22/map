#Choropleth map 
#first requirement pip install plotly==5.17.0
import plotly
import plotly.express as px

# create figure
fig = px.choropleth(locations=["United States","Japan","France", "United Kingdom","Germany","Canada","Italy"],locationmode="country names", color=[1,2,3,4,5,6,7], scope="world")

fig.show()
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.read_csv('detected_anomalies.csv')
fig = px.bar(df, x='EventID', title='Detected Anomalies by Event ID')

app.layout = html.Div(children=[
    html.H1(children='Windows Event Log Anomalies Dashboard'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_html_components as html
import pandas as pd
import dash_table
from tenbagger.src.scripts.tracker import track
import yaml


def main():

    # Print options
    pd.set_option('expand_frame_repr', False)
    with open(r'configs/trackers.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    with open(r'configs/ColorCodes.yaml') as file:
        colors = yaml.load(file, Loader=yaml.FullLoader)

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    df = track(config)
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


    app.layout = html.Div(
        children=[
        html.H1(children='Tracking sectors '),
        html.H2(children=f''),
        dash_table.DataTable(
            id='id_table',
            style_cell={
                'whiteSpace': 'normal',
                'height': 'auto',
                'minWidth': '90px', 'width': '90px', 'maxWidth': '90px',
                'whiteSpace': 'normal'
            },
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            editable=True,
            sort_action='native',
            filter_action="native",
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{0}}} > 2'.format(x),
                         'column_id': str(x),
                    },
                    'backgroundColor': '#008000',
                    'color': 'white'
                } for x in [x for x in list(df) if "Change" in x]
            ] + [
                {
                    'if': {
                        'filter_query': '{{{0}}} < -2'.format(x),
                        'column_id': str(x),
                    },
                    'backgroundColor': 'red',
                    'color': 'white'
                } for x in [x for x in list(df) if "Change" in x]
            ]
        )
    ],
    )

    app.run_server(debug=False)

import plotly.plotly 
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='lazywitt', api_key='MPfLndpSv8GtOUZ8UaCb')

class visuals():

    def Solid_gauge(self,data_val=80, max_data_val=100 ,data_label='Closing_price'):
        x=1*(data_val/max_data_val)
        base_chart={
        "values": [0,1,0,1],
        "labels": ['', "0", '' , str(max_data_val)],
        "domain": {"x": [0, .48]},
        "marker": {
            "colors": [
                'rgb(255, 255, 255)',
                'rgb(255, 255, 255)',
                'rgb(255, 255, 255)',
                'rgb(255, 255, 255)',
            ],
            "line": {
                "width": 1
            }
        },
        "name": "Gauge",
        "hole": .4,
        "type": "pie",
        "direction": "clockwise",
        "rotation": 180,
        "showlegend": False,
        "hoverinfo": "none",
        "textinfo": "label",
        "textposition": "outside"   
    }
        meter_chart = {
    "values": [1,x,1-x],
    "labels": [data_label, data_val,'.'],
    "marker": {
        'colors': [
            'rgb(255,255,255)',
            'rgb(226,126,64)',
            'rgb(232,226,202)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}
        layout = {
        'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    }

}
        base_chart['marker']['line']['width'] = 0
        fig = {"data": [base_chart, meter_chart],
               "layout": layout}
        plotly.plotly.iplot(fig, filename='gauge-meter-chart')


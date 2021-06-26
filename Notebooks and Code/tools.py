from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import plotly.graph_objects as go
import altair as alt

import warnings
warnings.filterwarnings('ignore')

def get_season_player(df,player_name, season):
    return df[(df.id.str.contains(season)) & df.player_name.str.contains(player_name)]

def get_player(df,player_name):
    return df[df.player_name.str.contains(player_name)]


def get_season(df,season):
    return df[df.id.str.contains(season)]

def get_players_position(df, pos):
    return df[df[pos] == 1]

def radar_chart(radar_df,dico_players, title):
    fig = go.Figure()

    for key, value in dico_players.items():
        fig.add_trace(go.Scatterpolar(
              r=radar_df.loc[value],
              theta=radar_df.columns,
              fill='toself',
              name=key
        ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 1]
        )),
      showlegend=True,
      title=title
    )
    fig.write_html("website/radar.html", full_html=False,include_plotlyjs='cdn')
    
    return fig
    
def ajusted_stats(radar_df):
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(radar_df), index=radar_df.index,columns=radar_df.columns)
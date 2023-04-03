import pandas as pd

def main():
    d = pd.read_csv('naves.csv')
    print(d.sort_values(by=['nombre','largo'],ascending=[True,False]))
    print(d[d['nombre'].isin(['Halcón Milenario','Estrella de la Muerte'])])
    print(d.sort_values(by=['pasajeros'],ascending=False).head(5))
    print(d[d['tripulacion']==d['tripulacion'].max()])
    print(d[d['nombre'].str.startswith('AT')])
    print(d[d['pasajeros']>=6])
    print(d[d['largo']==d['largo'].min()])
    print(d[d['largo']==d['largo'].max()])
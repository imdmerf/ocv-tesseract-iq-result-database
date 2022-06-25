import seaborn
from database import Database
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
db = Database('persons.db')

def visual():
    df = pd.read_sql_query("""SELECT result FROM persons""", db.connection)
    snsplot = seaborn.kdeplot(x=df['result'], shade=True)
    fig = snsplot.get_figure()
    plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

def get_data():
    df = pd.DataFrame({
        "Skill": [9, 9, 11],
        "Ages": [18, 19, 19],
        "Goals": [2, 4, 3]
    })

    plt.plot(df)
    fig, _ = plt.subplots()
    return mpld3.fig_to_dict(fig)

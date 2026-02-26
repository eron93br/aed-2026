import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Meu Primeiro Dashboard")

st.header("Cotacao de Ativos")

print("agora o bicho vai pegar!! ;)")
st.write("Agora estou fazendo um dashboard com a turma do CESAR 2025.2!!!!")

st.header("Sobre esse Dashboard")

st.write("O dashboard apresenta uma introducao ao framework streamlit")

code = '''    def plot_bar_group(ax, models, data, errors, show_ylabel=True):
        x = np.arange(len(models))
        for i, (clf, color) in enumerate(zip(classifiers, colors)):
            pos = x + (i - (n_bars - 1) / 2) * width

            # Added yerr and error_kw for the error bars
            bars = ax.bar(pos, data[clf], width, label=clf,
                          color=color, edgecolor='black', linewidth=0.5)

            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height:.1f}',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 8), # Increased offset for error bar clearance
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=14, fontweight='bold')'''
st.code(code, language="python")

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
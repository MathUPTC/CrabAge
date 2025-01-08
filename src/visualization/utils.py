import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# histogramas y caja de bigotes

def histogram_box(data,label):
    df = data
    variable=str(label)
    fig, ax = plt.subplots(1,2,figsize=(14,5))
    sns.histplot(df,x=variable,kde=True,ax=ax[0])
    sns.boxplot(df,x=variable,ax=ax[1])
    
    mean = df[variable].mean()
    variance = df[variable].var()
    kurtosis = df[variable].kurtosis().round(3)
    skewness = df[variable].skew().round(3)
    
    
    textstr = '\n'.join((r'mean=%.2f' % (mean, ), r'Variance=%.2f' % (variance, ),
                         r'Kurtosis=%.2f' % (kurtosis, ), r'Skewness=%.2f' % (skewness, )))
    
    ax[0].axvline(mean,color="red")
    ax[0].set_title(f'Histograma de {variable}')
    ax[0].set_ylabel('Frecuencia')
    ax[0].text(0.05, 0.95, textstr, transform=ax[0].transAxes, fontsize=10,
             verticalalignment='top')
    
    ax[1].set_title(f"Boxplot de {variable}")
    
    plt.show()
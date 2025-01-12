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

# curvas de entrenamiento
def history_curves(history):
    plt.figure(figsize=(13,5))

    train_loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = np.arange(1,len(train_loss)+1)
    # graph loss
    plt.subplot(1,2,1)
    plt.plot(epochs,train_loss,'ro-',label="train loss")
    plt.plot(epochs,val_loss,'bo-',label="valid loss")
    plt.legend()
    plt.title('train and validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')

    train_r2 = history.history['r2_score']
    val_r2 = history.history['val_r2_score']
    # graph mae
    plt.subplot(1,2,2)
    plt.plot(epochs,train_r2,'ro-',label="train R2score")
    plt.plot(epochs,val_r2 ,'bo-',label="valid R2score")
    plt.legend()
    plt.title('train and validation R2score')
    plt.xlabel('Epochs')
    plt.ylabel('R2score')
    plt.show()
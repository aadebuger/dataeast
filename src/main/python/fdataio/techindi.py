'''
Created on 2018年2月26日

@author: aadebuger
'''
import tushare as ts
import pandas as pd
import numpy as np
from matplotlib.pyplot import  plot
from matplotlib.pyplot import  show
from fdataio.gsrl import newdatav
def pc1():
         datav= ts.get_hist_data('600050')
         newlow = pd.Series(datav['low'].values,index=datav.index)
         newlow =  np.concatenate(([0],datav['low'].values[:-1]),axis=0)
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         pc = h[:-1]
         newpc =np.append([0],pc)    
         c1 = newpc-c
         print(len(c1))
         exp4 = lambda x: 1 if x>0  else 0 
         vfunc = np.vectorize(exp4)
         c2 = np.sign(c1)
         c3 = vfunc(c2)
         print(c3)
         datav['c2']=c2
         datav['c3']=c3
         print(datav)
         
         return datav
def  getData(datav):
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         v = datav['volume'].values
         o = datav['open'].values
         
         print(v)
         newdata= np.array([h,l,c,o,v]).transpose()
         return newdata
     
                   
def  pc():
         datav= ts.get_hist_data('600050')
         newlow = pd.Series(datav['low'].values,index=datav.index)
         newlow =  np.concatenate(([0],datav['low'].values[:-1]),axis=0)
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         o = datav['open'].values
         np.array([h,l,c,o]).transpose()
         
         pc = c[1:]
         newpc =np.append(pc,[0])    
         c1 = newpc-l
         return np.array([h,l,c,o]).transpose()

def  getData(datav):
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         o = datav['open'].values
         np.array([h,l,c,o]).transpose()
             
         
def stock():
         datav= ts.get_hist_data('600050')
         newlow = pd.Series(datav['low'].values,index=datav.index)
         newlow =  np.concatenate(([0],datav['low'].values[:-1]),axis=0)
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         previousclose = c[-20 -1: -1]
         N=20
         h = h[-N:]
         l = l [-N:]
         
         truerange = np.maximum(h -l , h- previousclose, previousclose -l )
         atr= np.zeros(N)
         atr[0]= np.mean(truerange)
         for i in range(1,N):
                atr[i]= (N-1)* atr[i-1]+ truerange[i]
                atr[i]/=N
         print(atr)
def ma():
         datav= ts.get_hist_data('600050')
         newlow = pd.Series(datav['low'].values,index=datav.index)
         newlow =  np.concatenate(([0],datav['low'].values[:-1]),axis=0)
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         N=5
         
         weights = np.ones(N)/N    
         print(weights)
         sma1 = np.convolve(weights,c)
         sma = np.convolve(weights,c)[N-1:-N+1]
         print("lenc",len(c))
         print("sma1 len",len(sma1))
         print("sma len",len(sma))
         t = np.arange(N - 1 ,len(c))
         print(t)
         print(c[N-1:])
         print("t shape",t.shape)
         print("c[N-1:]",c[N-1:].shape)
         plot(t, c[N-1:],lw =1.0)
         plot(t, sma , lw =2.0)
         print(sma)
         show()

def ema():
         datav= ts.get_hist_data('600050')
         newlow = pd.Series(datav['low'].values,index=datav.index)
         newlow =  np.concatenate(([0],datav['low'].values[:-1]),axis=0)
         h = datav['high'].values
         l = datav['low'].values
         c = datav['close'].values
         N=5
         
         weights = np.ones(N)/N    
         weights = np.exp(np.linspace(-1.,0.,N))
         weights = np.convolve(weights,c)[N-1: -N + 1]
         
         print(weights)
         ema = np.convolve(weights,c)[N-1:-N+1]
         print("lenc",len(c))
         t = np.arange(N - 1 ,len(c))
         print(t)
         print(c[N-1:])
         print("t shape",t.shape)
         print("c[N-1:]",c[N-1:].shape)
         plot(t, c[N-1:],lw =1.0)
         plot(t, ema , lw =2.0)
         print(ema)
         show()
def bollinger():
       deviation  =[]
       C  = len(c)
       for i in range(N-1,C):
            if i + N < C:
                    dev = c[i: i+N]
            else:
                dev = c[-N:]
             averages = np.zeros[N]
             averages.fill(sma[i -N -1])
             dev = dev - averages 
             dev = dev **2 
             dev - np.sqrt(np.mean(dev))
             deviation.append(dev)
        deviation = 2 * np.array( deviation)
        upperBB  = sma + deviation 
        lowerBB = sma - deviation 
def line():
        pivots = (h + l + c ) / 3
        t = np.arange(len(c))
        sa,sb = fit_line( t, pivots - ( h -l ))
        ra,rb = fit_line( t , pivots + ( h + l ))
        support = sa * t + sb
        resistance = ra * t + rb 
        
        condition = ( c > support ) & ( c < resistance)
        print("Conditions",conditon)
        between_bands = np.where( condition)
        

def fit_line(t,y):
        A = np.vstack([t, np.ones_like(t)]).T 
        return np.linalg.lstsq(A,y)[0]

        
if __name__ == '__main__':
    stock()
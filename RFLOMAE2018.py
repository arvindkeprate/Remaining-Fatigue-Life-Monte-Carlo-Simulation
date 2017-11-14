# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:18:38 2017

@author: ArvindKeprate
#"Crude Monte Carlo Simulation Code for Predicting Remaining Fatigue Life""

def my_RFL():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from tqdm import tqdm#package to plot progress bar
    from time import sleep
    EOL = []
    alist = []
    Clist = []
    sigmalist = []
    samples = int(input("Enter Number of Samples:"))
    for i in tqdm(range(samples)):
        a_initial = np.random.lognormal(-0.0653, 0.0533)#random initial crack size
        C = np.random.lognormal(-28.3518, 0.3708)#random value of parameter C
        m = 3
        sigma = np.random.lognormal(4.6002, 0.0998)#random value of stress
        Y = 0.952
        counter = 0
        a = a_initial
        alist.append(a_initial)
        Clist.append(C)
        sigmalist.append(sigma)
        while a < 12.567:
            counter = counter + 1
            del_K = sigma*Y*(3.14*a)**(0.5)# Paris Law
            a = a + C*del_K**m# Paris Law
        EOL.append(counter)
        sleep(1)
    #print(EOL)
    #data = EOL
    #sns.set_style('whitegrid')
    #sns.kdeplot(np.array(data), bw = 0.5)
    #plt.show()
    #print(("Mean of RFL is: %.2f")% np.mean(data))
    #print(("Median of RFL is: %.2f")% np.median(data))
    #print(("Standard Deviation of RFL is: %.2f")% np.std(data))
    #print(alist)
    #print(Clist)
    #print(sigmalist)
    CompList = [alist, Clist, sigmalist, EOL]# List of lists
    total = np.array(CompList)# 2D Numpy array
    trans_total = total.transpose()# transpose of 2D array
    #print(trans_total)
    df_trans_total = pd.DataFrame(trans_total, columns = ["Initial Crack Size", "C", "Sigma", "RFL"])# converting 2D array to dataframe
    print(df_trans_total)
    writer = pd.ExcelWriter("RFLOMAE2018.xlsx", engine = "xlsxwriter")#Create a Pandas Excel writer using XlsxWriter as the engine
    df_trans_total.to_excel(writer, sheet_name="Sheet1")# Convert the dataframe to an XlsxWriter Excel object
    writer.save()# Close the Pandas Excel writer and output the Excel file
    
    
    
    
    
    
    

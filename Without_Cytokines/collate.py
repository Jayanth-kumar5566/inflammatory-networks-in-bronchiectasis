from __future__ import division
import pandas

bac=pandas.read_csv("./../Data/Genus_rel.csv",index_col=0)
# 100 in percentange

#Dropping 0 columns
nsel=bac.sum(axis=0)
n=nsel[nsel==0].index
bac.drop(columns=n,inplace=True)

#Non-zero value in atleast 10 samples
nsel=bac>=1   #atleast 1%
nsel=nsel.sum(axis=0)
y=nsel[nsel<3].index #In atleast 3 patients
bac.drop(columns=y,inplace=True)

bac=bac.div(bac.sum(axis=1), axis=0) #Normalize

meta=pandas.read_csv("./../Data/necessary_variables.csv",index_col=0)
#l1=meta["PA_CI_PCR_Freq_ex2+"]
l2=meta["PA_CI_PCR_Freq_ex3+"]

#bac_1=pandas.merge(bac,l1,how="inner",left_index=True,right_index=True)
bac_2=pandas.merge(bac,l2,how="inner",left_index=True,right_index=True)

'''
y_bac1=bac[bac_1['PA_CI_PCR_Freq_ex2+']=="Yes"]
y_bac1.to_csv("./2+/Y/Microbes.csv")
n_bac1=bac[bac_1['PA_CI_PCR_Freq_ex2+']=="No"]
n_bac1.to_csv("./2+/N/Microbes.csv")
'''
y_bac2=bac[bac_2['PA_CI_PCR_Freq_ex3+']=="Yes"]
y_bac2.to_csv("./Y/Microbes.csv")
n_bac2=bac[bac_2['PA_CI_PCR_Freq_ex3+']=="No"]
n_bac2.to_csv("./N/Microbes.csv")

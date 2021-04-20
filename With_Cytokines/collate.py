from __future__ import division
import pandas

bac=pandas.read_csv("./../../Data/Genus_rel.csv",index_col=0)
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

meta=pandas.read_csv("./../../Data/necessary_variables.csv",index_col=0)
l1=meta["PA_CI_PCR_Freq_ex3+"]
#l2=meta["PA_CI_PCR_Freq_ex3+"]

bac_1=pandas.merge(bac,l1,how="inner",left_index=True,right_index=True)

cyto=pandas.read_csv("./../../Data/cyto.csv",index_col=0)
cyto=cyto.dropna()
cyto=cyto.div(cyto.sum(axis=1), axis=0)
m=pandas.merge(bac_1,cyto,how="inner",left_index=True,right_index=True)

m_y=m[m['PA_CI_PCR_Freq_ex3+']=="Yes"]
m_y=m_y.drop('PA_CI_PCR_Freq_ex3+',axis=1)
m_y=m_y.div(m_y.sum(axis=1), axis=0)
m_y.to_csv("./Y/Microbes.csv")

m_n=m[m['PA_CI_PCR_Freq_ex3+']=="No"]
m_n=m_n.drop('PA_CI_PCR_Freq_ex3+',axis=1)
m_n=m_n.div(m_n.sum(axis=1), axis=0)
m_n.to_csv("./N/Microbes.csv")

import pandas as pd
import numpy as np


df_samples = pd.read_csv("DataSets/Belly_Button_Biodiversity_samples.csv")
df_samples = df_samples.set_index("otu_id")
df_columns = list(df_samples)
results1 = df_columns
df_list = list(np.ravel(results1))


### def otu() ###

df_otu_id = pd.read_csv("DataSets/Belly_Button_Biodiversity_otu_id.csv")
df_otu_id = df_otu_id.set_index("otu_id")

### def meta() ###

df_meta = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv")
df_meta.head(2)
df_meta.index += 940
df_meta.head()
sample_id = 940
df_sample = df_meta.loc[940]
results2 = df_sample[["AGE","BBTYPE","ETHNICITY","GENDER","LOCATION","SAMPLEID"]]
results2 = results2.to_dict()
df_wfreq = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv")
df_wfreq.index += 940
df_wfreq["NAME"] = "BB_" + df_wfreq["SAMPLEID"].astype(str)
df_wfreq_sample = df_wfreq.loc[[940],["WFREQ"]]
results3 = df_wfreq_sample["WFREQ"].item()


### def sample()


df_samples2 = pd.read_csv("DataSets/Belly_Button_Biodiversity_Samples.csv")
sample = 'BB_940'
df_sample_filter = df_samples2.filter(items = [sample,'otu_id'])
df_sample_filter = df_sample_filter.sort_values(by=sample, ascending=False)
df_sample_sort = df_sample_filter.sort_values(by=sample, ascending=False)
df_sample_nozero_nan = df_sample_sort[df_sample_sort > 0]
df_sample_nozero = df_sample_nozero_nan.dropna()
sample_values = df_sample_nozero[sample].tolist()
otu_ids = df_sample_nozero['otu_id'].tolist()
df_sample_index = [{'otu_ids':otu_ids,'sample_values':sample_values}]


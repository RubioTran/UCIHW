# import necessary libraries
from sqlalchemy import func
import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_samples.csv")
    df = df.set_index('otu_id')
    results = list(DF_index)
    df_list = list(np.ravel(results))
    return render_template("index.html", DF_list = DF_list)


@app.route('/names')
def names():
    df_samples = pd.read_csv("DataSets/Belly_Button_Biodiversity_samples.csv")
    df_samples = df_samples.set_index("otu_id")
    df_columns = list(df_samples)
    results = df_columns
    df_list = list(np.ravel(results))
    return jsonify(DF_list)


@app.route('/otu')
def otu():
    df_otu_id = pd.read_csv("DataSets/Belly_Button_Biodiversity_otu_id.csv")
    df_otu_id = df_otu_id.set_index("otu_id")
    results = df_otu_id['lowest_taxonomic_unit_found']
    df_list = list(np.ravel(results))
    return jsonify(df_list)


@app.route('/metadata', defaults={'sample':'BB_940'})
@app.route('/metadata/<sample>')
def metadata(sample):
    df_meta = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv")
    df_meta.head(2)
    df_meta.index += 940
    df_meta.head()
    sample_id = 940
    df_sample = df_meta.loc[940]
    results = df_sample[["AGE","BBTYPE","ETHNICITY","GENDER","LOCATION","SAMPLEID"]]
    results = results.to_dict()
    df_wfreq = pd.read_csv("DataSets/Belly_Button_Biodiversity_Metadata.csv")
    df_wfreq.index += 940
    df_wfreq["NAME"] = "BB_" + df_wfreq["SAMPLEID"].astype(str)
    df_wfreq_sample = df_wfreq.loc[[940],["WFREQ"]]
    results = df_wfreq_sample["WFREQ"].item()
    return jsonify(df_list)

@app.route('/wfreq', defaults={'samplewf':'BB_940'})
@app.route('/wfreq/<samplewf>')
def wfreq(samplewf):
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
    return jsonify(results)

@app.route('/samples', defaults={'sample':'BB_940'})
@app.route('/samples/<sample>')
def sample(sample = 'BB_940'):
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_Samples.csv")
    DF_sample_filter = DF.filter(items = [sample,'otu_id'])
    DF_sample_sort = DF_sample_filter.sort_values(by=sample, ascending=False)
    DF_sample_nonzero_nan = DF_sample_sort[DF_sample_sort > 0]
    DF_sample_nonzero = DF_sample_nonzero_nan.dropna().head(10)
    sample_values = DF_sample_nonzero[sample].tolist()
    otu_ids = DF_sample_nonzero['otu_id'].tolist()
    results = [{'otu_ids':otu_ids,'sample_values':sample_values}]
    return jsonify(results)

if __name__ == '__main__':
    app.run()
#-*- coding: utf-8 -*-
import sys
import re
import pandas as pd
worm_gene_tran={}
worm_gene=[]# [elegans:20225,brenneri:30659,briggsae:22366,remanei:31436]
worm_tran=[]# [elegans:33334,brenneri:30744,briggsae:26169,remanei:31526]
specie=sys.argv[1]
input_file="genes_transcript_"+specie+".tsv"
output_file="worm_gene_"+specie+".csv"
with open(input_file, "r") as f:
	for row in f:
		row_list=row.rstrip('\r\n').split('\t')
		# print row_list
		info={}
		ID=row_list[0]
		gene=row_list[1]
		seq=row_list[2]
		trans=row_list[3]
		worm_tran.append(trans)		
		if ID not in worm_gene:
			worm_gene.append(ID)
			info["Gene_ID"]=ID
			info["Gene_Name"]=gene
			info["Transcripts_Name"]=trans
			info["Transcripts_Count"]=1
			worm_gene_tran[ID]=info
		else:
			worm_gene_tran[ID]["Transcripts_Name"]=worm_gene_tran[ID]["Transcripts_Name"]+","+trans
			worm_gene_tran[ID]["Transcripts_Count"]+=1

mydata_df=pd.DataFrame.from_dict(worm_gene_tran,orient='index',dtype=None).reset_index(level=None)
mydata_df=mydata_df[["Gene_ID","Gene_Name","Transcripts_Count","Transcripts_Name"]]
mydata_df.to_csv(output_file)
print("OK!")
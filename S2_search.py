import pandas as pd
import numpy as np

def S2():
    sheet = pd.read_excel('S2.xlsx', sheet_name = None)
    gene_id=['Intergenic' ,'TBX15' , 'ASPM' , 'PKDCC' , 'HOXD' ,'PAX3' , 'RAB7A' ,'ACAD9' , 'EPHB3' ,
            'DVL3' , 'DCHS2' , 'SUPT3H' , 'RPS12' , 'EYA4' , 'DLX6' , 'DYNC1L1', 'BC039327' ,'SOX9' ,'KCTD15']
    gene_data_sheet=['ENSEMBL_gene_id','HUGO_gene_id','chr','MASH beta','MASH sd','MASH LFSR']
    dict = {}

    for name in sheet.keys() :
        if name != 'README' and name != 'Replication':
            df = pd.read_excel('S2.xlsx', sheet_name=name)
            values = df.values
            # print(values)
            for j in range(len(gene_id)):
                try:

                    for i in range(len(values)):
                        if gene_id[j] in values[i][1]:
                            gene_data_sheet = np.vstack((gene_data_sheet, values[i]))


                except Exception as e:
                    pass

            dict[name]=gene_data_sheet
    return(dict)



print(S2())
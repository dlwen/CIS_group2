import pandas as pd
import numpy as np

def sheet2():

    data = pd.read_excel('S4.xlsx', sheet_name='Sex_differential_expression_dri')
    df = pd.DataFrame(data)

    values=df.values
    dict={}
    gene_data_sheet1=['ENSMBL_gene_id','HUGO_gene_id','chr','cluster','cluster_description','cluster_difference','cluster_effsize']

    gene_id=['Intergenic' ,'TBX15' , 'ASPM' , 'PKDCC' , 'HOXD' ,'PAX3' , 'RAB7A' ,'ACAD9' , 'EPHB3' ,
            'DVL3' , 'DCHS2' , 'SUPT3H' , 'RPS12' , 'EYA4' , 'DLX6' , 'DYNC1L1', 'BC039327' ,'SOX9' ,'KCTD15']


    for j in range(len(gene_id)):
        try:

            for i in range(len(values)):
                if gene_id[j] in values[i][1]:
                    gene_data_sheet1=np.vstack((gene_data_sheet1,values[i]))


        except Exception as e:
            pass
    dict['Sex_differential_expression_driver_genes']=gene_data_sheet1
    return dict

def sheet3():

    data = pd.read_excel('S4.xlsx', sheet_name='Expression_driver_genes')
    df = pd.DataFrame(data)

    # print(df)
    values=df.values
    # print(values)
    dict={}

    gene_data_sheet2=['ENSMBL_gene_id','HUGO_gene_id','chr','cluster','cluster_description','cluster_difference','cluster_meanexp']
    gene_id = ['Intergenic', 'TBX15', 'ASPM', 'PKDCC', 'HOXD', 'PAX3', 'RAB7A', 'ACAD9', 'EPHB3',
               'DVL3', 'DCHS2', 'SUPT3H', 'RPS12', 'EYA4', 'DLX6', 'DYNC1L1', 'BC039327', 'SOX9', 'KCTD15']

    for j in range(len(gene_id)):
        try:

            for i in range(len(values)):
                if gene_id[j] in values[i][1]:
                    # gene_data_sheet2.append(values[i])
                    gene_data_sheet2=np.vstack((gene_data_sheet2,values[i]))


        except Exception as e:
            pass
    dict['Expression_driver_genes']= gene_data_sheet2
    return dict



def sheet4():

    data = pd.read_excel('S4.xlsx', sheet_name='Driver_types')



    df = pd.DataFrame(data)

    values=df.values
    dict={}
    gene_data_sheet3=['ENSMBL_gene_id','HUGO_gene_id','chr','driver_type']
    gene_id = ['Intergenic', 'TBX15', 'ASPM', 'PKDCC', 'HOXD', 'PAX3', 'RAB7A', 'ACAD9', 'EPHB3',
               'DVL3', 'DCHS2', 'SUPT3H', 'RPS12', 'EYA4', 'DLX6', 'DYNC1L1', 'BC039327', 'SOX9', 'KCTD15']

    for j in range(len(gene_id)):
        try:

            for i in range(len(values)):
                if gene_id[j] in values[i][1]:
                    gene_data_sheet3=np.vstack((gene_data_sheet3,values[i]))


        except Exception as e:
            pass
    dict['Driver_types']=gene_data_sheet3

    print(dict)

print(sheet2())
print(sheet3())
print(sheet4())

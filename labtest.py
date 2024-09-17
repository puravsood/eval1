import numpy as np

def find_patient(d, pat_list):
    pat_list=pat_list.tolist()
    patient_name=[]
    j=0
    for i in pat_list:
        if i[2]==d:
            j+=1
            patient_name.insert(j,i[1])
    return patient_name

def no_of_patients(pat_list,doc_list):
    pat_list=pat_list.tolist()
    doc_list=doc_list.tolist()
    docs={}
    for i in pat_list:
        if i[2]  in docs:
            docs[i[2]]+=1
        else:
            docs[i[2]]==1
            
    return docs.max()

patient_list=np.array([['P1','A','D1',2000],['P2','B','D1',2500],['P3', 'C','D2',3500],['P4','D','D3',6000]])

doctor_list=np.array([['D1', 'G'],['D2', 'H'],['D3','I']])

find_patient('D2',patient_list)
a=no_of_patients(patient_list,doctor_list)

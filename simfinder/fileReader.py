__author__ = 'amir'
import numpy as np

def fileRead(input,delm):
    dic={}
    for line in input:
        toks=line.split(delm)
        dic[toks[0]]=" ".join(toks[1:]).replace('\n','')
    return dic


def normalize(mat):
    row_norms = np.sqrt(np.multiply(mat, mat).sum(1))
    row_norms = row_norms.astype(np.double)
    row_norms[row_norms != 0] = np.array(1.0/row_norms[row_norms != 0]).flatten()
    mat = np.multiply(mat, row_norms)
    return mat


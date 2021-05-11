#!/usr/bin/python

import streamlit as st
import pandas as pd
import numpy

def prepare_sum(np_matrix, Xstart, Xstop, Ystart, Ystop):
    submatrix_sum, plus_count = 0, 0
    for j in range(Ystart, Ystop+1):
        for i in range(Xstart, Xstop+1):
            submatrix_sum += np_matrix[i,j]
            plus_count +=1
    return submatrix_sum, plus_count    

def prepare_subsums(Xrange, Yrange):
    sub_sums = {}
    for j in range(Ystart, Ystop+1):
        for i in range(Xstart, Xstop+1):
            pass
    return sub_sums        


### MAIN ######################################################################
if __name__ != '__main__': sys.exit(0)

st.title(""" Big Table:
""")

Xrange = 100
Yrange = 100

### random table
np_matrix = numpy.random.randn(int(Xrange), int(Yrange))

st.write(np_matrix)


submatrix_sum = prepare_sum(np_matrix,1,1,1,1)
st.write(submatrix_sum)


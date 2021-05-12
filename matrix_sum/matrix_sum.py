#!/usr/bin/python

import streamlit as st
import pandas as pd
import numpy
import math
import copy


def prepare_sum(np_matrix, Xstart, Xstop, Ystart, Ystop):
    submatrix_sum, plus_count = 0, 0
    ### stop intend index +1  
    for j in range(Ystart, Ystop):
        for i in range(Xstart, Xstop):
            ### do nothing if index is outside of matrix, it is ok
            try: 
                submatrix_sum += np_matrix[i,j]
                plus_count +=1
            except: pass            
    return submatrix_sum, plus_count    


def prepare_subsums(np_matrix, Xmax, Ymax):
    sub_sums = {}

    maxXindex = Xmax
    maxYindex = Ymax

    halfX = copy.deepcopy(maxXindex)
    halfY = copy.deepcopy(maxYindex)

    ii = 0
    while 2**ii<=maxXindex/2:
        ii+=1
        for i in range(0, maxXindex, 2**ii):
            jj = 0
            while 2**jj<=maxYindex/2:
                jj+=1
                for j in range(0, maxYindex, 2**jj):
                    sub_sums['%s.%s.%s.%s' % (i, i+2**ii if i+2**ii < maxXindex else maxXindex, j, j+2**jj if j+2**jj < maxYindex else maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, i, i+2**ii if i+2**ii < maxXindex else maxXindex, j, j+2**jj if j+2**jj < maxYindex else maxYindex))
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


submatrix_sum = prepare_sum(np_matrix,0,Xrange,0,Yrange)
st.write('TOTAL: SUM, NUMBER_OF_ADDITIONS')
st.write(submatrix_sum)

submatrix_sum = prepare_sum(np_matrix,0,0,0,0)
st.write('ZERO: SUM, NUMBER_OF_ADDITIONS')
st.write(submatrix_sum)

submatrix_sum = prepare_sum(np_matrix,0,1,0,1)
st.write('ONE: SUM, NUMBER_OF_ADDITIONS')
st.write(submatrix_sum)

sub_sums = prepare_subsums(np_matrix,Xrange,Yrange)
st.write('PARIAL: SUM, NUMBER_OF_ADDITIONS_PER_SUBMATRIX')
st.write(sub_sums)


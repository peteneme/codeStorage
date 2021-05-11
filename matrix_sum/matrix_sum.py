#!/usr/bin/python

import streamlit as st
import pandas as pd
import numpy
import math
import copy

def prepare_sum(np_matrix, Xstart, Xstop, Ystart, Ystop):
    submatrix_sum, plus_count = 0, 0
    for j in range(Ystart, Ystop+1):
        for i in range(Xstart, Xstop+1):
            try: submatrix_sum += np_matrix[i,j]
            except: pass
            plus_count +=1
    return submatrix_sum, plus_count    

def prepare_subsums(np_matrix, Xmax, Ymax):
    sub_sums = {}

    maxXindex = Xmax-1
    maxYindex = Ymax-1

    halfX = copy.deepcopy(maxXindex)
    halfY = copy.deepcopy(maxYindex)

    ### last strips
    if maxXindex % 2:
        sub_sums['%s.%s.%s.%s' % (maxXindex, maxXindex, 0, maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, maxXindex, maxXindex, 0, maxYindex))
    if maxYindex % 2:
        sub_sums['%s.%s.%s.%s' % (0, maxXindex, maxYindex, maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, 0, maxXindex, maxYindex, maxYindex))


    ii = 0
    while 2**ii<=maxXindex/2:
        ii+=1
        for i in range(0, maxXindex, 2**ii):
            jj = 0
            while 2**jj<=maxYindex/2:
                jj+=1
                for j in range(0, maxYindex, 2**jj):
                    sub_sums['%s.%s.%s.%s' % (i, i+2**ii if i+2**ii < maxXindex else maxXindex, j, j+2**jj if j+2**jj < maxYindex else maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, i, i+2**ii if i+2**ii < maxXindex else maxXindex, j, j+2**jj if j+2**jj < maxYindex else maxYindex))


            #st.write(ii,2**ii,i)
            
    return sub_sums        


def make_subquadrants(np_matrix, Xx, Yy):
    sub_sums = {}

    maxXindex = Xmax-1
    maxYindex = Ymax-1

    halfX = copy.deepcopy(maxXindex)
    halfY = copy.deepcopy(maxYindex)

    ### last strips
    if maxXindex % 2:
        sub_sums['%s.%s.%s.%s' % (maxXindex, maxXindex, 0, maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, maxXindex, maxXindex, 0, maxYindex))
    if maxYindex % 2:
        sub_sums['%s.%s.%s.%s' % (0, maxXindex, maxYindex, maxYindex)] = copy.deepcopy(prepare_sum(np_matrix, 0, maxXindex, maxYindex, maxYindex))

    while halfX>=1 and halfY>=1:
        halfX = int(halfX/2)
        halfY = int(halfY/2)
        sub_sums['%s.%s.%s.%s' % (0, halfX, 0, halfY)] = copy.deepcopy(prepare_sum(np_matrix, 0, halfX, 0, halfY))
        sub_sums['%s.%s.%s.%s' % (halfX, 2*halfX, 0, halfY)] = copy.deepcopy(prepare_sum(np_matrix, halfX, 2*halfX, 0, halfY))
        sub_sums['%s.%s.%s.%s' % (0, halfX, halfY, 2*halfY)] = copy.deepcopy(prepare_sum(np_matrix, 0, halfX, halfY, 2*halfY))
        sub_sums['%s.%s.%s.%s' % (halfX, 2*halfX, halfY, 2*halfY)] = copy.deepcopy(prepare_sum(np_matrix, halfX, 2*halfX, halfY, 2*halfY))

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


submatrix_sum = prepare_sum(np_matrix,0,99,0,99)
st.write('TOTAL: SUM, NUMBER_OF_ADDITIONS')
st.write(submatrix_sum)

sub_sums = prepare_subsums(np_matrix,Xrange,Yrange)
st.write('PARIAL: SUM, NUMBER_OF_ADDITIONS')
st.write(sub_sums)


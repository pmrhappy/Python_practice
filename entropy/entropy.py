import os,sys
import numpy as np
import math,random

def entropy2(labels):
 #""" Computes entropy of label distribution. """
    n_labels = len(labels)
    print "n_labels= ",n_labels
    
    if n_labels <= 1:
        return 0


    counts = np.bincount(labels)
    print "counts= ",counts
    probs = counts / float(n_labels)
    print "probs= ",probs
    n_classes = np.count_nonzero(probs)
    print "n_classes =",n_classes
    if n_classes <= 1:
        return 0

    ent = 0.

    # Compute standard entropy.
    for i in probs:
        ent -= i * math.log(i,n_classes)

    return ent
    
label=np.array([0,0,0])
print "\nlabel=",label
result=entropy2(label)
print result
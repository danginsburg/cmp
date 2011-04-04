#!/usr/bin/env python
#
#
# NAME
#
#    compute_stats.py
#
# DESCRIPTION
#
#    Compute statistics for a connectivity matrix
#
# AUTHORS
#
#    Daniel Ginsburg
#    Rudolph Pienaar
#    Children's Hospital Boston, 2011

import cmp
import cfflib
import networkx as nx
import numpy as np

from optparse import OptionParser


def parseCommandLine():
    """Setup and parse command-line options"""
    
    parser = OptionParser(usage="%prog [options] inputfile.gpickle")
    # Add options    
    (options, args) = parser.parse_args()
    if len(args) == 0:
        parser.error("Wrong number of arguments")
    
    return options,args

   

def main():
    
    options,args = parseCommandLine()
    
    pickleFileName = args[0];
    outputFileName = None
    if (len(args) == 2):
        outputFileName = args[1]
                

    print ("Loading %s...\n") % (pickleFileName)
    g = nx.read_gpickle(pickleFileName);
    
    # Convert graph to matrix form
    for u,v,d in g.edges_iter(data=True):
        g.edge[u][v]['weight'] = g.edge[u][v]['number_of_fibers']
    cmat = nx.to_numpy_matrix(g)
    
    mean = np.mean(cmat)
    std = np.std(cmat) 
    print('Total number of connections: %d') % (np.sum(cmat))
    print('Connection Matrix Mean: %f Std: %f' ) % (mean, std)

    
    # Compute binarized stats
    binarized_cmat= np.zeros(cmat.shape)
    binarized_cmat[cmat>0] = 1
    print('Binarized connection matrix Mean: %f Std: %f' ) % (np.mean(binarized_cmat),
                                                                np.std(binarized_cmat))

    
    if outputFileName != None :
        f = open(outputFileName, 'at')
        f.write( ('%f,%f\n') % (mean, std) )
        f.close() 
    
if __name__ == '__main__':
    main()    


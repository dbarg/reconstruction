
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
     
import os
import time

from utils_slurm import *

    
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
     
def main():

    print()
    print("TMPDIR:       {0}".format(os.environ.get('TMPDIR')))
    print("SLURM_TMPDIR: {0}".format(os.environ.get('SLURM_TMPDIR')))
    print()

    return


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
     
if __name__ == '__main__':
    main()

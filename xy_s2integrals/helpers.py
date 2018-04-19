
####################################################################################################
####################################################################################################

def checkTrainingData(df_train_input, df_train_truth, nRows = 5):
    
    ##########################################################################################
    ##########################################################################################
    
    print()
    print("Input shape: " + str(df_train_input.shape))
    print("Truth shape: " + str(df_train_truth.shape))

    
    ####################################################################################################
    ####################################################################################################
   
    print()
    print("Input DataFrame: ")
    display(df_train_input[0:nRows][:])
    print()
    print("Truth DataFrame:")
    display(df_train_truth[0:nRows][:])
    print()
   
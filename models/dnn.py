
##########################################################################################
##########################################################################################

from keras import layers
from keras import regularizers
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Embedding
from keras.models import Sequential


##########################################################################################
##########################################################################################

def dnnModel(
    n_inputs,
    n_outputs,
    layers_hidden,
    activation='elu',
    keep_rate=0.00005):


    ######################################################################################
    ######################################################################################

    reg_scale  = 0.00100 # possibly bad
    bias_init  = 'zeros'
    bias_use   = True
    kern_reg   = regularizers.l2(reg_scale)
    
   
    ######################################################################################
    # Input Layer
    ######################################################################################
    
    model = Sequential()
    
    model.add(Dense(n_inpus, input_dim=n_inputs, activation=activation))

    
    ######################################################################################
    # Hidden Layers
    ######################################################################################
    
    for layer_dim in layers_hidden:
        
        ##################################################################################
        ##################################################################################
        
        model.add(Dense(
            layer_dim,
            activation         = activation,
            bias_initializer   = bias_init,
            use_bias           = bias_use#,
            #kernel_regularizer = kern_reg
        ))
        
        model.add(Dropout(keep_rate))

        
        ##################################################################################
        ##################################################################################

        continue
        
        
    ######################################################################################
    ######################################################################################
    
    #model.add(Dense(n_outputs, activation=activation))
    model.add(Dense(n_outputs))
    
     
    ######################################################################################
    ######################################################################################
    
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])
    
    
    ######################################################################################
    ######################################################################################
    
    return model




#------------------------------------------------------------------------------
# https://keras.io/getting-started/sequential-model-guide/
#------------------------------------------------------------------------------

from keras import backend as K
from keras import layers
from keras import regularizers
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
from keras.models import Sequential
from keras.utils import plot_model


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def lstmModel(
    n_channels,
    n_timesteps,
    n_outputs,
    #activation='sigmoid',
    activation='elu',
    keep_rate=0.00005,
    go_backwards=False,
    unroll=False):

    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    
    name = 'model_s2integrals_s2waveforms_lstm_' + activation


    #--------------------------------------------------------------------------
    # To Do: understand stateful, return_state
    #--------------------------------------------------------------------------

    lstm = LSTM(
        n_channels,
        #input_shape=(n_timesteps, n_channels),
        input_shape=(n_timesteps, 1)
        #return_sequences=True
        #go_backwards=go_backwards,
        #unroll=unroll
    )
    
    model = Sequential()
    model.add(lstm)
    #model.add(LSTM(1))
    model.add(Dropout(keep_rate))
    model.add(Dense(n_outputs, activation=activation))
    
    #model.compile(
    #    loss='binary_crossentropy',
    #    optimizer='rmsprop'#,
    #    #metrics=['accuracy']
    #)
    
    
    #--------------------------------------------------------------------------
    # Compile
    #--------------------------------------------------------------------------
    
    model.compile(loss='mean_squared_error', optimizer='adam')
    
    
    #--------------------------------------------------------------------------
    # Save Model
    #--------------------------------------------------------------------------
    
    folder   = "models/"    
    name_h5  = folder + name + ".h5"
    name_png = folder + name + ".png"
    
    plot_model(model, to_file=name_png, show_layer_names=True, show_shapes=True)
    model.save(name_h5, overwrite=True)

    #print()
    #display(Image.open(name_png))
    #print()

    
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    
    return model, name



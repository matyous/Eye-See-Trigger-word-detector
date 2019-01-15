# Eye-See-Trigger-word-detector
A deeplearning project to detect the word "Hey Eye See!" 

The model is an encoder-decoder RNN model taking as input the FFT of an audio clip of 3seconds and outputing a vector of format [1, 0] if the word "Hey Eye See!" is detected and [0, 1] if not.

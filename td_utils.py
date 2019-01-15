import matplotlib.pyplot as plt
from scipy.io import wavfile
import os
from pydub import AudioSegment

# Calculate and plot spectrogram for a wav audio file
def graph_spectrogram(wav_file):
    plt.ioff()
    rate, data = get_wav_info(wav_file)
    nfft = 200 # Length of each window segment
    fs = 8000 # Sampling frequencies
    noverlap = 120 # Overlap between windows
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap = noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:,0], nfft, fs, noverlap = noverlap)
    return pxx

# Load a wav file
def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

# Used to standardize volume of audio clip
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

# Load raw audio files for speech synthesis
def load_raw_audio():
    activates = []
    backgrounds = []
    negatives = []
    for filename in os.listdir("./VoiceRecorder/pos"):
        if filename.endswith("wav"):
            activate = AudioSegment.from_wav("./VoiceRecorder/pos/"+filename)
            activates.append(activate)
    for filename in os.listdir("./VoiceRecorder/back"):
        if filename.endswith("wav"):
            background = AudioSegment.from_wav("./VoiceRecorder/back/"+filename)
            backgrounds.append(background)
    for filename in os.listdir("./VoiceRecorder/neg"):
        if filename.endswith("wav"):
            negative = AudioSegment.from_wav("./VoiceRecorder/neg/"+filename)
            negatives.append(negative)
    return activates, negatives, backgrounds

def load_test_audio():
    activates = []
    backgrounds = []
    negatives = []
    for filename in os.listdir("./test_data/pos"):
        if filename.endswith("wav"):
            activate = AudioSegment.from_wav("./test_data/pos/"+filename)
            activates.append(activate)
    for filename in os.listdir("./test_data/back"):
        if filename.endswith("wav"):
            background = AudioSegment.from_wav("./test_data/back/"+filename)
            backgrounds.append(background)
    for filename in os.listdir("./test_data/neg"):
        if filename.endswith("wav"):
            negative = AudioSegment.from_wav("./test_data/neg/"+filename)
            negatives.append(negative)
    return activates, negatives, backgrounds
import pyaudio
import librosa
import numpy as np 

# define the length of the audio recordings in seconds
record_time = 3

# define the n_mfcc to extract
n_mfcc = 13
# define the sampling rate
samp_rate = 16000

# define the set of speech commands to recognize
commands = ['yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off']

# record audio samples for each command and extract MFCC features
for command in commands:
    print('speak the command {} now...'.format(command))
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=samp_rate, 
        input=True, 
        frames_per_buffer=1024
        )
    frames = []
    for i in range(0, int(samp_rate/1024 * record_time)):
        data = stream.read(1024) # no of frames to read
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate() # object to release port audio resources

    # start the extrcation
    y, sr = librosa.load(np.frombuffer(b''.join(frames), dtype=np.int16), sr=samp_rate)
    mfcc = librosa.feature.mfcc(
        y,
        sr=samp_rate,
        n_mfcc = n_mfcc
    )

    np.save('{}_mfcc.npy'.format(command), mfcc)
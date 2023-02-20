# make use of pvreorder from pico voice
# https://picovoice.ai/blog/how-to-record-audio-using-python/

from pvrecorder import PvRecorder

import wave 
import struct

for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")

recorder = PvRecorder(device_index=0, frame_length=512)
audio = []

try:
    recorder.start()

    while True:
        frame = recorder.read()# read audio frame and return the list containing the frames
        audio.extend(frame)
except KeyboardInterrupt:
    recorder.stop()
    # save to file
    path = '/home/ix502iv/Documents/Hardware/HMM/'
    with wave.open(path, 'w') as f:
        f.setparams(
            1,
            2,
            16000,
            512,
            "NONE",
            "NONE"
        )
        f.writeframes(struct.pack("h"*len(audio), *audio))
finally:
    recorder.delete() # release resoourcea used by PV
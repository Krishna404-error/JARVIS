from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

model=WhisperModel(
    "base",
    device="cpu",
    compute_type="int8")

duration=5
sample_rate=16000

print("Jarvis is listening....")
print("Speak Now")

audio=sd.rec(
    int(duration*sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype=np.float32
)

sd.wait()

print("Audio captured!")
print("Audio Shape:", audio.shape)

segments, info=model.transcribe(audio.flatten())

text=""

for segment in segments:
    text += segment.text

print("You:", text.strip())
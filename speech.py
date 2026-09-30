import sounddevice as sd
import numpy as np
import keyboard
from faster_whisper import WhisperModel


# Load Whisper once
whisper_model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def listen():
    sample_rate = 16000
    audio_chunks = []

    print("\nHold SPACE and speak...")

    # Wait for Space
    keyboard.wait("space")

    print("Listening...")

    # Record while Space is held
    with sd.InputStream(
        device=1,
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
        callback=lambda indata, frames, time, status:
            audio_chunks.append(indata.copy())
    ):
        while keyboard.is_pressed("space"):
            sd.sleep(50)

    print("Recording stopped.")

    if not audio_chunks:
        return ""

    # Combine audio chunks
    audio = np.concatenate(audio_chunks, axis=0).flatten()

    # --------------------------------
    # Normalize audio volume
    # --------------------------------

    max_amplitude = np.max(np.abs(audio))

    if max_amplitude > 0:
        audio = audio / max_amplitude

    print("Audio normalized.")
    print("Converting speech to text...")

    # --------------------------------
    # Whisper transcription
    # --------------------------------

    segments, info = whisper_model.transcribe(
        audio,
        language="en",
        vad_filter=True
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()
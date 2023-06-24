import torch, time, random
import sounddevice as sd

language = 'ru'
model_id = "ru_v3"
saplerate = 48000
speaker = "aidar"
device = torch.device("cpu")

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)

model.to(device)

def Lux(text: str):
    audio = model.apply_tts(text=text, speaker=speaker, sample_rate=saplerate,
                            put_accent = True, put_yo = True)
    print(text)

    sd.play(audio, saplerate)
    time.sleep(len(audio) / saplerate * 2)
    sd.stop()
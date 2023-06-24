import vosk, sys, queue, json
import sounddevice as sd

model = vosk.Model('model-small')
samplerate = 16000
device = 1
channel = 1
dtype= 'int16'
blocksize = 8000

q = queue.Queue()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=blocksize,device=device, dtype=dtype, channels=channel, callback=q_callback):
        r =vosk.KaldiRecognizer(model, samplerate)
        while True:
            data =q.get()
            if r.AcceptWaveform(data):
                callback(json.loads(r.Result())["text"])
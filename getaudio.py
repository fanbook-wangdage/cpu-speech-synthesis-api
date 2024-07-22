import wave
import numpy as np
import pyaudio
from TTService import TTService

def generateAudio(speakContent: str, output_file: str, m:list) -> None:
    config_combo = [
        m
    ]
    for cfg, model in config_combo:
        a = TTService(cfg, model, 'test', 1)
        p = pyaudio.PyAudio()
        audio = a.read(speakContent)
        #禁用自动播放
        #stream = p.open(format=pyaudio.paFloat32, channels=1,
        #                rate=a.hps.data.sampling_rate, output=True)
        #data = audio.astype(np.float32).tostring()
        #stream.write(data)
        # Set the audio properties
        num_channels = 1
        sample_width = 2  # Assuming 16-bit audio
        frame_rate = a.hps.data.sampling_rate
        # Convert audio data to 16-bit integers
        audio_int16 = (audio * np.iinfo(np.int16).max).astype(np.int16)
        # Open the output file in write mode
        with wave.open(output_file, 'wb') as wav_file:
            # Set the audio properties
            wav_file.setnchannels(num_channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(frame_rate)
            # Write audio data to the file
            wav_file.writeframes(audio_int16.tobytes())


if __name__ == '__main__':
    import sys
    sys.path.append('vits')
    from TTService import TTService
    generateAudio("你好啊，我是派蒙。  ", "output.wav",m=("models/paimon6k.json", "models/paimon6k_390k.pth"))#提前结束的话在文本末尾加空格

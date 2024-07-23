import wave

import numpy as np
import pyaudio

from TTService import TTService

config_combo = [
        # ("models/CyberYunfei3k.json", "models/yunfei3k_69k.pth"),
         ("models/paimon6k.json", "models/paimon6k_390k.pth"),
        # ("models/ayaka.json", "models/ayaka_167k.pth"),
        # ("models/ningguang.json", "models/ningguang_179k.pth"),
        # ("models/nahida.json", "models/nahida_129k.pth"),
        # ("models/miko.json", "models/miko_139k.pth"),
        # ("models/yoimiya.json", "models/yoimiya_102k.pth"),
        # ("models/noelle.json", "models/noelle_337k.pth"),
        # ("models/yunfeimix.json", "models/yunfeimix_122k.pth"),
        # ("models/yunfeineo.json", "models/yunfeineo_25k.pth"),
        # ("models/yunfeimix2.json", "models/yunfeimix2_47k.pth")
        #("models/zhongli.json", "models/zhongli_44k.pth"),
    ]
for cfg, model in config_combo:
    a = TTService(cfg, model, 'test', 1)
    TTService.read_save(text="你好",filename='output.wav',self='你好',sr=None)
    #p = pyaudio.PyAudio()
    # audio = a.read('旅行者，今天是星期四，能否威我五十')
    # stream = p.open(format=pyaudio.paInt16,
    #                 channels=1,
    #                 rate=a.hps.data.sampling_rate,
    #                 output=True
    #                 )
    # data = audio.astype(np.int16).tobytes()
    # stream.write(data)
    # # Set the output file name
    # output_file = "output.wav"

    # # Set the audio properties
    # num_channels = 1
    # sample_width = 2  # Assuming 16-bit audio
    # frame_rate = a.hps.data.sampling_rate

    # # Convert audio data to 16-bit integers
    # audio_int16 = (audio * np.iinfo(np.int16).max).astype(np.int16)

    # # Open the output file in write mode
    # with wave.open(output_file, 'wb') as wav_file:
    #     # Set the audio properties
    #     wav_file.setnchannels(num_channels)
    #     wav_file.setsampwidth(sample_width)
    #     wav_file.setframerate(frame_rate)

    #     # Write audio data to the file
    #     wav_file.writeframes(audio_int16.tobytes())
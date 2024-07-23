import wave
import numpy as np
import pyaudio
from TTService import TTService

def generateAudio(speakContent: str, output_file: str, m:list) -> None:
    config_combo = [
        m
    ]
    import sys
    sys.path.append('vits')
    from TTService import TTService
    # generateAudio("你好啊，我是派蒙。  ", "output.wav",m=("models/paimon6k.json", "models/paimon6k_390k.pth"))#提前结束的话在文本末尾加空格
    # Paths to the configuration and model files
    # Initialize the TTService object
    tts_service = TTService(*m)

    # Text to be synthesized
    text = speakContent

    # Call the read function
    audio_output = tts_service.read(text)

    # Save the output to a file
    output_filename = output_file
    sample_rate = 48000
    tts_service.read_save(text, output_filename, sample_rate)


if __name__ == '__main__':
    import sys
    sys.path.append('vits')
    from TTService import TTService
    # generateAudio("你好啊，我是派蒙。  ", "output.wav",m=("models/paimon6k.json", "models/paimon6k_390k.pth"))#提前结束的话在文本末尾加空格
    # Paths to the configuration and model files
    cfg_path = "models\\paimon6k.json"
    model_path = "models\\paimon6k_390k.pth"
    char = 'character_name'  # e.g., 'en'
    speed = 1  # speed of speech, 1.0 means normal speed

    # Initialize the TTService object
    tts_service = TTService(cfg_path, model_path, char, speed)

    # Text to be synthesized
    text = "你好啊"

    # Call the read function
    audio_output = tts_service.read(text)

    # Save the output to a file
    output_filename = 'output.wav'
    sample_rate = 48000
    tts_service.read_save(text, output_filename, sample_rate)

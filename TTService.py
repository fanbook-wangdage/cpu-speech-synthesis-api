import sys
import time

sys.path.append('TTS/vits')

import soundfile
import os
os.environ["PYTORCH_JIT"] = "0"
import torch

import vits.commons as commons
import vits.utils as utils

from vits.models import SynthesizerTrn
from vits.text.symbols import symbols
from vits.text import text_to_sequence

import logging
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = torch.LongTensor(text_norm)
    return text_norm


class TTService():
    def __init__(self, cfg, model, char, speed):
        logging.info('Initializing TTS Service for %s...' % char)
        self.hps = utils.get_hparams_from_file(cfg)
        self.speed = speed
        self.net_g = SynthesizerTrn(
            len(symbols),
            self.hps.data.filter_length // 2 + 1,
            self.hps.train.segment_size // self.hps.data.hop_length,
            **self.hps.model).cpu()
        _ = self.net_g.eval()
        _ = utils.load_checkpoint(model, self.net_g, None)

    def read(self, text):
        text = text.replace('~', '！')
        stn_tst = get_text(text, self.hps)
        with torch.no_grad():
            x_tst = stn_tst.cpu().unsqueeze(0)
            x_tst_lengths = torch.LongTensor([stn_tst.size(0)]).cpu()
            audio = self.net_g.infer(x_tst, x_tst_lengths, noise_scale=.667, noise_scale_w=0.2, length_scale=self.speed)[0][
                0, 0].data.cpu().float().numpy()
        return audio

    def read_save(self, text, filename, sr):
        stime = time.time()
        au = self.read(text)
        soundfile.write(filename, au, sr)
        logging.info('VITS Synth Done, time used %.2f' % (time.time() - stime))




# # Paths to the configuration and model files
# cfg_path = "models/catmix.json"
# model_path ="models/catmix_107k.pth"
# char = 'character_name'  # e.g., 'en'
# speed = 1.0  # speed of speech, 1.0 means normal speed

# # Initialize the TTService object
# tts_service = TTService(*['models/catmix.json', 'models/catmix_107k.pth', 'character_catmaid', 1.2])

# # Text to be synthesized
# text = "喵~主人，你回来啦！有想我了吗？"

# # Call the read function
# audio_output = tts_service.read(text)

# # Save the output to a file
# output_filename = 'output.wav'
# sample_rate = 48000  # Sample rate, e.g., 22050 Hz
# tts_service.read_save(text, output_filename, sample_rate)
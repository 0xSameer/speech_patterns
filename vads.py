import os
import subprocess
import sys

corpus = "ainu"

wav_path = "../corpora/emnlp2017/ainu/test-wavs/"
vad_path = "../corpora/emnlp2017/ainu/test-evads/"

for wav_file in [f for f in os.listdir(wav_path) if f.endswith(".wav")]:
    vad_fname = os.path.join(vad_path, wav_file.replace(".wav", ".vad"))
    mono_wav_fname = os.path.join(wav_path, wav_file)
    #print(" ".join(map(str, ["python", "scripts/mark_energy.py", "-i",
    #                 mono_wav_fname, "-o", vad_fname, "-s", "0.4", "-e", "0"])))
    subprocess.call(["python", "scripts/mark_energy.py", "-i",
                      mono_wav_fname, "-o", vad_fname, "-s", "0.4", "-e", "0"])






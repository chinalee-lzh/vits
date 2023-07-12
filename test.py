import os
import utils

def main():
  dirs = os.listdir('wavs_small')
  for v in dirs:
    print(v)
  # utils.load_wav_to_torch

main()
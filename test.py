import os
import utils

def main():
  utils.load_wav_only('wavs/chapter1_10_mar7th_230.wav')
  # dirs = os.listdir('wavs')
  # for v in dirs:
  #   print('file', v)
  #   utils.load_wav_only('wavs/'+v)

main()
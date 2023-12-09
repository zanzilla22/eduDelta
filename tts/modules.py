from langdetect import detect 
from gtts import gTTS


# def chatTranscribe(audio_path):

#   # audio_path = os.path.join(".\\", "sample.wav") --for testing
#   if not key_setup[0]:
#     openai.api_key = getOpenAiKey()
#     key_setup[0] = True

#   with open(audio_path, "rb") as audio_file:
#     transcript = (openai.Audio.transcribe("whisper-1", audio_file))['text']


#   print("transcript:", transcript)

#   return transcript


def chatSpeak(input_text): #text to speech with free google libs B)
  
  lang_code = detect(input_text)
  print("Detected language:", lang_code)

  tts = gTTS(text = input_text, lang = lang_code)  # Specify the language ('en' for English)
  tts.save("output.mp3")  # Save to an MP3 file

  return(".\\output.mp3")

chatSpeak("Aditya est venu 124 minutes en retard")

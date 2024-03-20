import whisper

def transcribe(audio_file, model):
  """Transcribe an audio file using Whisper."""
  model = whisper.load_model(model)
  result = model.transcribe(audio_file)
  transcription = result["text"]
  return transcription


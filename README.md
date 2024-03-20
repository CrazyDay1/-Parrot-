# Athena 🏛️ - Streamlit Application



## Introduction

Athena is a Streamlit-based application designed to transcribe audio files and summarize text content. Leveraging state-of-the-art language models, Athena provides users with a user-friendly interface to upload audio or text files, select desired models for processing, and interact with the application through a chat function. 



## Features

* **File Upload**: Supports uploading of .wav, .mp3, .m4a, and .txt files for transcription or direct text summarization.
* **Model Selection**: Choose from a variety of Whisper and LLM (Large Language Models) options for audio transcription and text summarization.
* **Interactive Chat**: Engage with Athena through a chat interface to request summarizations and other text-based operations.
* **Real-time Transcription and Summarization**: Watch as your audio and text files are processed in real-time, providing immediate feedback and results.

> **Note**: All models are run locally on your machine. Therefore, the speed and performance of Athena depend on your hardware capabilities.
  
## Setup and Installation


### Prerequisites
* Python 3.6 or newer

  
### Installation Steps

1. Clone the repository:
```
git clone https://github.com/CrazyDay1/Athena.git
```
2. Go to repository folder:
```
cd Athena/Athena
```
3. Install the required Python packages:
```
pip install -r requirements.txt
```
4. Download and set up Ollama:
* Follow the instructions on the [Ollama Setup Page](https://ollama.com/download) to download and setup Ollama.
* Ensure Ollama is properly configured as per your project's needs.
5. Run the Streamlit application (Run it on your terminal):
```
streamlit run homepage.py
```


## Usage

1. Navigate to the application URL provided by Streamlit upon running the script.
2. Use the sidebar to upload an audio or text file for processing.
3. Select the desired Whisper model for audio transcription or LLM for text summarization.
4. Click the "Transcribe" button to process the uploaded file.
5. Interact with Athena through the chat interface for additional text processing tasks.


## Known Issues

* Summarization quality may vary depending on the input format and model selection.
* Long audio files may take significant time to transcribe.


## Contributing

Contributions to Athena are welcome! Feel free to fork the repository, make your changes, and submit a pull request.


## License

MIT 


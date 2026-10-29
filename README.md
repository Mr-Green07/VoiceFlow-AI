# VoiceFlow-AI

A collection of voice-enabled AI experiments: a Windows voice assistant, an AI trainer/coach powered by local LLMs (Ollama), a Llama 3 conversational chatbot, and a text-based Gemini chatbot.

> Built with Python, `pyttsx3` (text-to-speech), `SpeechRecognition` (speech-to-text), Ollama, Hugging Face Transformers, and the Google Gemini API.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Supported Voice Commands (audio_samples.py)](#supported-voice-commands-audio_samplespy)
- [Notes & Tips](#notes--tips)
- [License](#license)

## Overview

VoiceFlow-AI explores conversational voice assistants and AI trainers. It contains several standalone scripts/notebooks, each demonstrating a different approach:

- A simple **voice assistant** (`audio_samples.py`) that listens via microphone, speaks back responses, and can control Windows Wi-Fi.
- An **AI Trainer** (`trainer_ollama.py`) that generates learning plans, quizzes, and feedback using a locally running Ollama model, with optional TTS.
- A lightweight **Ollama response wrapper** (`audio.py`).
- A **Jupyter notebook** (`chatbot_using_llama.ipynb`) that loads a local Llama 3 model for chat.
- A **Gemini text chatbot** (`first.py` / `file1.py`) using the Google Generative AI API.

## Project Structure

```
VoiceFlow-AI/
├── audio.py                      # Ollama generate() helper (llama3.2:11b)
├── audio_samples.py              # Windows voice assistant (speak + listen + Wi-Fi control)
├── trainer_ollama.py             # Ollama-based AI trainer/coach (plans, quizzes, feedback)
├── chatbot_using_llama.ipynb     # Notebook: Llama 3 chat via Hugging Face Transformers
├── first.py                      # Gemini chatbot (google-generativeai)
├── file1.py                      # Legacy/scratchpad (commented OpenAI/Vertex code)
├── apikey.py                     # (Legacy) Google API key container
├── requirement.txt               # Python dependencies
├── library_header.jpg            # (asset)
└── README.md
```

## Features

- **Text-to-Speech** via `pyttsx3` (Windows SAPI5 voices).
- **Speech-to-Text** via `SpeechRecognition` (Google recognition, `en-in` locale).
- **Voice-controlled Wi-Fi** toggle/check on Windows (`netsh`).
- **Time-based greetings** (good morning/afternoon/evening).
- **Local LLM integration** with Ollama (`gemma3:4b` by default, configurable).
- **Curriculum planning**, quiz generation, and answer evaluation (AI Trainer).
- **Conversational memory** (history maintained across turns).
- **Optional TTS** fallback when `pyttsx3` is unavailable.

## Prerequisites

- Python 3.8+ (recommended 3.10/3.11)
- Windows (scripts use Windows-only features such as SAPI5 TTS and `netsh`; some voice/Wi-Fi features may not work on other OSes)
- Microphone (for voice input)
- Ollama installed and running (for `trainer_ollama.py`, `audio.py`): https://ollama.com/download
- (Optional) A Hugging Face local Llama 3 checkpoint (for the notebook)
- (Optional) A Google API key (for `first.py`)

## Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd VoiceFlow-AI
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirement.txt
   pip install pyttsx3 speechrecognition pyaudio ollama google-generativeai transformers torch accelerate
   ```

   > `pyaudio` can be tricky on Windows; install a prebuilt wheel if needed (`pip install pipwin && pipwin install pyaudio`).

4. Pull an Ollama model (for trainer scripts):

   ```bash
   ollama pull gemma3:4b
   # or
   ollama serve
   ```

## Configuration

- **Ollama model**: `trainer_ollama.py` reads `LLAMA_MODEL` from the environment, defaulting to `gemma3:4b`.

  ```bash
  # Windows
  set LLAMA_MODEL=llama3.2:3b
  # macOS/Linux
  export LLAMA_MODEL=llama3.2:3b
  ```

- **Google API key**: `first.py` reads `GOOGLE_API_KEY` from the environment; if unset, it prompts for input.

  ```bash
  set GOOGLE_API_KEY=your_key_here
  ```

- **Llama 3 checkpoint path** (notebook): edit `model_id` in `chatbot_using_llama.ipynb` to point to your local checkpoint.

## Usage

### 1. Voice Assistant (`audio_samples.py`)

Runs a loop that listens for voice commands and responds via TTS.

```bash
python audio_samples.py
```

On start it greets based on the current hour, then listens continuously for commands (see below). Say "exit"/"quit"/"goodbye" to stop.

### 2. AI Trainer (`trainer_ollama.py`)

```bash
python trainer_ollama.py
```

- Enter a topic and your level.
- It prints a learning plan and (optionally) speaks it.
- Type messages to chat; type `quiz` to get a quiz question and feedback; type `exit` to quit.

### 3. Ollama response helper (`audio.py`)

```bash
python audio.py
```

Generates a one-off response using `llama3.2:11b` (ensure that model is pulled).

### 4. Gemini text chatbot (`first.py`)

```bash
python first.py
```

Starts an interactive text chat using Gemini; type `exit`/`quit` to end.

### 5. Llama 3 notebook

Open in Jupyter:

```bash
jupyter notebook chatbot_using_llama.ipynb
```

Edit the model path and run cells to chat with a local Llama 3 model.

## Supported Voice Commands (audio_samples.py)

- `wish me` — greet based on time of day.
- `turn on wifi` / `enable wifi` / `connect wifi`
- `turn off wifi` / `disable wifi` / `disconnect wifi`
- `check wifi` / `wifi status`
- `exit` / `quit` / `goodbye` — stop the assistant.

## Notes & Tips

- `audio.py` and `trainer_ollama.py` require the Ollama daemon to be running. Start it with `ollama serve` if not already.
- Windows SAPI5 voices may need to be installed/enabled for `pyttsx3` to speak.
- `pyaudio` is required by `SpeechRecognition` for microphone capture.
- The `requirement.txt` file includes many generic data-science libraries; the core runtime needs `pyttsx3`, `SpeechRecognition`, `pyaudio`, `ollama`, `google-generativeai` (for `first.py`), and `transformers`/`torch` (for the notebook).
- `apikey.py` stores a (legacy) Google API key in source; prefer environment variables instead. Do not commit real keys.

## License

No license file is currently included. Add one before distributing or open-sourcing this project.
```bash
tts --text "Hello Stackies and welcome to Getting Started with Speech Synthesis Campaign" --model_name tts_models/en/ek1/tacotron2 --out_path output/output.wav
```
Play the `output.wav` file using any audio player and listen to it say "Hello Stackies! Welcome to Getting Started with Speech Synthesis Campaign!".

Code Breakdown:

- tts --text "<text>": The Coqui TTS command to generate speech from the provided text.
- --model_name <model>: Specifies the model to use for speech synthesis. In the demo, the Tacotron 2 model is used.
- --out_path <file_path>: Saves the generated speech to a file.


#### Project structure
Here’s a breakdown of the directory structure for the project:

- output/ - This is where the synthesized audio files will be saved.
- models.py- The script for fetching available TTS models from Cocqui.
- speakers.py - The script for fetching available speakers in a selected TTS model. Coqui models use a parameter called “speaker” to select what type of “voice” to use in generating speeches.
- languages.py- The script for fetching available languages in a selected TTS model.
- tts-script.py - The main file where you will create the TTS script for speech synthesis.'
- requirements.txt - This contains the dependencies needed to run the scripts.
- tts-app.py - The main file where you will create the TTS app with a Gradio Interface.  
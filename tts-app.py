# TODO#1 - Importing Required Libraries

# TODO#2 - Loading the Coqui TTS Model

# TODO#3 - Defining Voice Selection

# TODO#4 - Defining Localization Options

# TODO#5 - Defining Variables to Hold Selected Voice and Localization

# TODO#6 - Managing Outputs

# TODO#7 - Implementing the Trim Function.

# Main Speech Synthesis Function
def generate_speech_with_timestamps(text, speaker, language):
    global last_generated_audio, last_generated_text
    output_path = "output/generated_speech.wav"
    start_time = time.time()

    # TODO#8 - Implementing the Main TTS Function

    # TODO#9 - Managing Duration and Tracking Variables

    # TODO#10 - Extracting Audio Information

    # TODO#11 - Return Audio Information

# Waveform Function
def generate_waveform():
    global last_generated_audio, last_generated_text

    if not last_generated_audio or not os.path.exists(last_generated_audio):
        return None, "No valid audio file found to generate waveform."

    samplerate, data = wavfile.read(last_generated_audio)
    time_axis = np.linspace(0, len(data) / samplerate, num=len(data))

    # Modern waveform style with gradient color
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='#1E1E1E')  # Dark background

    # Plot waveform with gradient
    ax.plot(time_axis, data, color='cyan', alpha=0.8, linewidth=1.2)

    # Styling grid and axes for a modern look
    ax.set_facecolor('#2E2E2E')  # Darker plot background
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_xlabel("Time (seconds)", color='white')
    ax.set_ylabel("Amplitude", color='white')

    # Set the title with trimmed text
    trimmed_text = trim_text(last_generated_text)
    ax.set_title(f"Waveform for text input: '{trimmed_text}'", color='white', fontsize=14)

    waveform_image_path = "output/waveform.png"
    plt.savefig(waveform_image_path, transparent=True)
    plt.close()

    return waveform_image_path, "Waveform generated successfully!"

# Button Click Event Handler
def on_generate_click(text, speaker, language):
    if not text:
        return None, "Please enter some text to generate speech.", "", gr.update(interactive=False)

    audio_path, word_count, speaker_name, lang, speech_length, duration = generate_speech_with_timestamps(text, speaker, language)

    # Format the text box content
    data_info = f"Word Count: {word_count}\nVoice: {speaker_name}\nLocalization: {lang}\nLength of Speech: {speech_length} seconds\nGeneration Duration: {duration} seconds"

    return audio_path, data_info, "Speech generation successful!", gr.update(interactive=True)

# Gradio Interface Setup
def setup_interface():
    with gr.Blocks() as app:
        # TODO#12 - Adding Title and Description
        gr.Markdown("# 🗣️ Text-to-Speech GenAI with Coqui TTS")
        gr.Markdown("Convert text to speech using Coqui TTS with support for different languages and speakers.")
        
        with gr.Row():
            with gr.Column():
                # TODO#13 - Creating Text Input and Selection Options

            with gr.Column():
                # TODO#14 - Displaying Data Information and Status


        with gr.Row():
            with gr.Column():
                # TODO#15 - Adding Audio Output and "Generate Speech" Button


            with gr.Column():
                # TODO#16 - Adding Waveform Display and "Generate Waveform" Button


        generate_button.click(
            on_generate_click, 
            inputs=[text_input, speaker_dropdown, language_radio], 
            outputs=[audio_output, data_info_display, status_message, generate_waveform_button]
        )

        generate_waveform_button.click(
            generate_waveform, 
            outputs=[waveform_output, status_message]
        )

    return app

# TODO#17 - Launching the App
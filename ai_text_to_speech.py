from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile as wavfile
import tempfile
import os
import winsound
import re

# Load AI Text-to-Speech model
print("Loading AI model...")

model = VitsModel.from_pretrained(
    "facebook/mms-tts-eng"
)

tokenizer = AutoTokenizer.from_pretrained(
    "facebook/mms-tts-eng"
)

print("AI model loaded successfully!")

while True:

    # Get text from user
    text = input(
        "\nEnter your text (or type 'exit' to quit): "
    ).strip()

    if text.lower() == "exit":
        print("\n👋 Program closed.")
        break

    if not text:
        print("Please enter some text.")
        continue

    # Generate AI voice
    print("\nGenerating AI voice...")

    inputs = tokenizer(
        text,
        return_tensors="pt"
    )

    with torch.no_grad():
        output = model(**inputs)

    audio = output.waveform[0].cpu().numpy()

    print("Voice generated successfully!")

    # Create temporary audio file
    temp_file = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    temp_path = temp_file.name
    temp_file.close()

    # Save generated audio temporarily
    wavfile.write(
        temp_path,
        model.config.sampling_rate,
        audio
    )

    # Ask whether to play
    play_choice = input(
        "\nPress Y to play the voice or N to skip: "
    ).strip().lower()

    if play_choice == "y":

        print("Playing voice...")

        winsound.PlaySound(
            temp_path,
            winsound.SND_FILENAME
        )

    elif play_choice == "n":

        print("Voice playback skipped.")

    else:

        print("Invalid choice. Voice playback skipped.")

    # Ask whether to save
    save_choice = input(
        "\nDo you want to save this audio? (Y/N): "
    ).strip().lower()

    if save_choice == "y":

        while True:

            file_name = input(
                "Enter a file name: "
            ).strip()

            if not file_name:
                print("Please enter a file name.")
                continue

            # Remove invalid Windows filename characters
            safe_name = re.sub(
                r'[<>:"/\\|?*]',
                '_',
                file_name
            )

            # Prevent names ending with dot or space
            safe_name = safe_name.rstrip(". ")

            if not safe_name:
                print("Invalid file name.")
                continue

            break

        # Save permanently in current project folder
        saved_file = f"{safe_name}.wav"

        wavfile.write(
            saved_file,
            model.config.sampling_rate,
            audio
        )

        print(
            f"\nAudio saved successfully!"
        )

        print(
            f"🎧 File: {saved_file}"
        )

    elif save_choice == "n":

        print(
            "Audio not saved."
        )

    else:

        print(
            "Invalid choice. Audio will not be saved."
        )

    # Delete temporary file
    if os.path.exists(temp_path):

        os.remove(temp_path)

        print(
            "Temporary audio deleted."
        )
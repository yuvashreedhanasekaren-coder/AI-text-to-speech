# AI Text-to-Speech

An AI-powered Text-to-Speech application built with Python, PyTorch, Hugging Face Transformers, and the Facebook MMS-TTS English model.

This project converts user-provided text into speech using a pre-trained AI model. The generated voice can be played directly through the computer or saved as a `.wav` audio file.

---

## 📌 About This Project

This is a **small AI project created mainly for learning and educational purposes**.

The purpose of this project is not to build a large production-level Text-to-Speech system, but to understand how an existing AI model can be integrated into a Python application and used to generate human-like speech from text.

The idea behind the project is also connected to learning.

Some students may find it difficult to understand a concept when studying completely on their own. Sometimes, learning becomes easier when **someone explains the concept to them in a simple way**.

This project explores a small version of that idea:

```text
Student enters text
        ↓
AI processes the text
        ↓
AI generates a voice
        ↓
Student listens to the explanation
````

Instead of only reading the text on the screen, the learner can listen to the AI-generated voice.

This makes the project a simple exploration of how **AI and voice-based learning** can work together.

---

## 🎯 Project Purpose

The main purposes of this project are:

* To learn how AI Text-to-Speech works
* To understand how pre-trained AI models can be used
* To practice Hugging Face Transformers
* To understand basic PyTorch inference
* To generate speech from text
* To experiment with audio processing
* To explore how AI can support learning
* To build a small practical AI application from scratch

This project was intentionally kept simple so that the underlying AI workflow is easy to understand.

---

# ✨ Features

### 📝 Text Input

Users can enter text directly through the terminal.

```text
Enter your text (or type 'exit' to quit):
```

---

### 🤖 AI Voice Generation

The entered text is processed using the pre-trained:

```text
facebook/mms-tts-eng
```

model.

The model converts the text into an audio waveform.

---

### 🔊 Voice Playback

After generating the voice, the application asks:

```text
Press Y to play the voice or N to skip:
```

If the user enters:

```text
Y
```

the generated voice is played.

If the user enters:

```text
N
```

the playback is skipped.

---

## 💡 A Small Personal Meaning Behind "Y"

There is also a small personal touch hidden inside this project.

Normally:

```text
Y = Yes
N = No
```

So when the application asks:

```text
Press Y to play the voice or N to skip:
```

`Y` naturally means **Yes**.

But for me, `Y` also has another meaning:

```text
Y = Yuvashree
```

So the simple `Y` button has a small personal connection to the creator of this project.

It is a tiny detail, but it makes the project a little more personal. ❤️

---

### 💾 Save Generated Audio

Users can choose to permanently save the generated voice.

Example:

```text
Do you want to save this audio? (Y/N): Y

Enter a file name: introduction
```

Output:

```text
introduction.wav
```

---

### 🛡️ Filename Validation

The application automatically handles invalid Windows filename characters.

Characters such as:

```text
< > : " / \ | ? *
```

are replaced with underscores.

The application also prevents filenames from ending with a period or space.

---

### 🔄 Continuous Generation

The application runs continuously and allows users to generate multiple audio files during the same session.

The user can type:

```text
exit
```

to close the application.

---

### 🗑️ Temporary File Cleanup

Generated audio is temporarily stored for playback.

After the operation is completed, the temporary audio file is automatically deleted.

This prevents unnecessary temporary files from accumulating inside the project.

---

# 🛠️ Technologies Used

| Technology                | Purpose                          |
| ------------------------- | -------------------------------- |
| Python                    | Main programming language        |
| PyTorch                   | Deep learning framework          |
| Hugging Face Transformers | AI model integration             |
| Facebook MMS-TTS          | Pre-trained Text-to-Speech model |
| SciPy                     | WAV audio generation             |
| Windows `winsound`        | Audio playback                   |
| `tempfile`                | Temporary audio file handling    |
| `re`                      | Filename validation              |

---

# 🤖 AI Model

This project uses the pre-trained Hugging Face model:

```text
facebook/mms-tts-eng
```

The model is loaded using:

```python
model = VitsModel.from_pretrained(
    "facebook/mms-tts-eng"
)
```

The corresponding tokenizer is loaded using:

```python
tokenizer = AutoTokenizer.from_pretrained(
    "facebook/mms-tts-eng"
)
```

The model generates an audio waveform from the tokenized text input.

---

# 🔄 Application Workflow

```text
User enters text
        ↓
Text is tokenized
        ↓
AI Text-to-Speech model
        ↓
Audio waveform generated
        ↓
Temporary WAV file created
        ↓
User chooses whether to play
        ↓
Voice is played
        ↓
User chooses whether to save
        ↓
Optional permanent WAV file
        ↓
Temporary file deleted
```

---

# 🧠 Learning Concept Behind the Project

The project demonstrates a simple AI pipeline:

```text
Text
 ↓
Tokenizer
 ↓
Pre-trained AI Model
 ↓
Audio Waveform
 ↓
WAV File
 ↓
Voice Playback
```

The important idea is that we do not need to train a complete Text-to-Speech model ourselves.

Instead, a pre-trained model can be loaded and integrated into our own Python application.

This provides practical experience with using existing AI models in real applications.

---

# ⚙️ How It Works

## 1. Load the AI Model

The application loads the pre-trained VITS model and tokenizer.

```python
model = VitsModel.from_pretrained(
    "facebook/mms-tts-eng"
)

tokenizer = AutoTokenizer.from_pretrained(
    "facebook/mms-tts-eng"
)
```

---

## 2. Get User Input

The program asks the user to enter text.

```python
text = input(
    "\nEnter your text (or type 'exit' to quit: "
).strip()
```

If the user enters:

```text
exit
```

the application closes.

---

## 3. Tokenize the Text

The entered text is converted into a format that the AI model can process.

```python
inputs = tokenizer(
    text,
    return_tensors="pt"
)
```

---

## 4. Generate Speech

The tokenized input is passed to the AI model.

```python
with torch.no_grad():
    output = model(**inputs)
```

The generated waveform is extracted:

```python
audio = output.waveform[0].cpu().numpy()
```

---

## 5. Create Temporary Audio

A temporary WAV file is created for playback.

```python
temp_file = tempfile.NamedTemporaryFile(
    suffix=".wav",
    delete=False
)
```

The generated waveform is written using SciPy:

```python
wavfile.write(
    temp_path,
    model.config.sampling_rate,
    audio
)
```

---

## 6. Play the Generated Voice

On Windows, the generated audio is played using:

```python
winsound.PlaySound(
    temp_path,
    winsound.SND_FILENAME
)
```

---

## 7. Save the Audio

If the user chooses to save the audio, the waveform is written to a permanent WAV file.

Example:

```text
my_voice.wav
```

---

## 8. Delete Temporary Audio

After playback and optional saving, the temporary file is deleted.

```python
if os.path.exists(temp_path):
    os.remove(temp_path)
```

---

## 🎥 Demo

The following video demonstrates the final working output of the AI Text-to-Speech application.

▶️ **[Watch the Demo Video](./final_result.mp4)**

The demonstration shows the working AI Text-to-Speech application and its generated voice output.

The video is included as a project demonstration and learning reference.

---
 
## 🖥️ Example Workflow

```text
Loading AI model...
AI model loaded successfully!

Enter your text:
Artificial Intelligence helps computers perform tasks that normally require human intelligence.

Generating AI voice...
Voice generated successfully!

Press Y to play the voice or N to skip:
Y

Playing voice...

Do you want to save this audio? (Y/N):
Y

Enter a file name:
ai-explanation

Audio saved successfully!
File: ai-explanation.wav
```
---

# 📂 Project Structure

```text
AI-text-to-speech/
│
├── ai_text_to_speech.py
├── requirements.txt
├── .gitignore
└── final_result.mp4
```

### `ai_text_to_speech.py`

Main Python application containing:

* AI model loading
* Text tokenization
* Speech generation
* Audio playback
* Audio saving
* Filename validation
* Temporary file handling
* User interaction

### `requirements.txt`

Contains the required Python dependencies.

```text
transformers
torch
scipy
```

### `.gitignore`

Prevents unnecessary generated and development files from being tracked.

### `final_result.mp4`

Final demonstration video showing the working output of the project.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yuvashreedhanasekaren-coder/AI-text-to-speech.git
```

Navigate into the project:

```bash
cd AI-text-to-speech
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

```text
transformers
torch
scipy
```

---

# ▶️ Run the Application

Run:

```bash
python ai_text_to_speech.py
```

The application will first load the AI model.

Example:

```text
Loading AI model...
AI model loaded successfully!
```

---

# 💻 Example Usage

### Enter Text

```text
Enter your text (or type 'exit' to quit): Hello, welcome to my AI project.
```

### Generate Voice

```text
Generating AI voice...
Voice generated successfully!
```

### Play Voice

```text
Press Y to play the voice or N to skip: Y
```

The generated voice will be played through the system's default audio output.

### Save Voice

```text
Do you want to save this audio? (Y/N): Y

Enter a file name: welcome
```

Output:

```text
Audio saved successfully!
File: welcome.wav
```

---

# 🎧 Output

The generated speech is saved in:

```text
.wav
```

format.

Example:

```text
welcome.wav
```

Generated WAV files are excluded from Git using:

```gitignore
*.wav
```

---

# 🧠 Learning Outcomes

Through this project, I practiced:

* Python programming
* Artificial Intelligence
* Pre-trained AI models
* Hugging Face Transformers
* PyTorch inference
* Text tokenization
* Text-to-Speech generation
* Audio waveform processing
* WAV file generation
* Temporary file handling
* File validation
* User input handling
* Python dependency management
* Git and GitHub

---

# 📚 What I Learned

This project helped me understand how a pre-trained AI model can be integrated into a Python application without training a complete speech synthesis model from scratch.

I also learned how the following components work together:

```text
Python
   ↓
Transformers
   ↓
Pre-trained AI Model
   ↓
PyTorch
   ↓
Audio Waveform
   ↓
WAV File
   ↓
Voice Playback
```

Most importantly, the project gave me an idea of how a simple AI feature can be connected to a practical learning use case.

---

# 🎓 Educational Idea

One of the ideas behind this project is simple:

> Sometimes learning becomes easier when someone explains a concept instead of only giving written information.

For some students, reading a topic independently may not always be enough to understand it clearly.

A voice-based explanation can provide another way of learning.

This project explores that concept at a very small and basic level by allowing text to be converted into an AI-generated voice.

It is **not intended to replace teachers or human explanations**.

Instead, it is a small experiment to understand how AI voice technology could potentially support different learning styles.

---

# 🔮 Future Improvements

Possible future improvements include:

* 🌍 Multi-language Text-to-Speech
* 🖥️ Graphical User Interface
* 🌐 Web-based learning interface
* 📖 Educational explanation mode
* 🎚️ Voice speed control
* 🎵 Voice pitch control
* 🎤 Multiple voice options
* 📁 Multiple audio format support
* 📜 Text-to-Speech history
* 📦 Batch text-to-speech generation
* 🔊 Advanced audio controls
* 💻 Cross-platform audio playback

---

# 👩‍💻 AI Project Learning Series

This project is part of my **AI Project Learning Series**.

The purpose of this series is to build small practical AI projects, understand different AI libraries and models, and gradually move toward larger real-world AI applications.

```text
AI Project Learning Series

        │
        ├── Project 1 → OpenCV Face Detection ✅
        │
        └── Project 2 → AI Text-to-Speech ✅
```

Each project is intentionally focused on learning a specific concept rather than immediately building a large production-level application.

---

# 📈 Project Progress

```text
Project Setup                  ✅
AI Model Integration           ✅
Text Input                     ✅
Speech Generation              ✅
Voice Playback                 ✅
Audio Saving                   ✅
Filename Validation            ✅
Temporary File Cleanup         ✅
Demo Output                    ✅
GitHub Repository              ✅
README Documentation           🚧
```

---

# 🗂️ Git History

### Commit 1

```text
Add AI Text-to-Speech project
```

Added:

* Python application
* Requirements
* Git configuration

### Commit 2

```text
Add project output video
```

Added the final project demonstration video.

### Commit 3

```text
Add README documentation
```

Added complete project documentation, setup instructions, workflow explanation, learning purpose, and project details.

---

# 🖥️ System Requirements

* Windows operating system
* Python 3.x
* Internet connection for downloading the pre-trained AI model
* Working audio output device
* Required Python dependencies

> **Note:** The current implementation uses Python's `winsound` module for audio playback and is therefore designed for Windows.

---

# 📌 Project Status

```text
Project Status: Completed ✅
```

The AI Text-to-Speech application was created as a **small learning and educational project** to understand AI model integration and explore how AI-generated voice can support learning.

---

GitHub:

[https://github.com/yuvashreedhanasekaren-coder](https://github.com/yuvashreedhanasekaren-coder)

---

# 📄 License

This project was created for **learning and educational purposes**.

It is a small experimental AI project developed to understand Text-to-Speech technology, AI model integration, and practical Python application development.
# 🌐 Anuvaad Setu

### Your Language Bridge, Wherever You Go

## 1. Project Overview

Anuvaad Setu is a web-based language translation application developed using Python and Streamlit.

The application helps users translate text between different languages through a simple and interactive interface.

It aims to reduce language barriers and make communication easier for people who speak different languages.

## 2. Objectives

* To develop a user-friendly language translation application.
* To provide automatic text translation.
* To support multiple Indian and international languages.
* To allow users to copy translated text.
* To provide an easy language-swapping feature.

## 3. Key Features

### Automatic Translation

The application automatically translates text after the user stops typing.

### Multiple Language Support

Supports 11 languages, including English, Hindi, Marathi, Bengali, Tamil, Telugu, Gujarati, Spanish, French, German, and Japanese.

### Language Swap

Users can interchange the source and target languages using the swap button.

### Copy Translation

Users can copy the translated text to their clipboard.

### Multiline Text Input

Users can enter sentences and paragraphs for translation.

### Responsive Interface

The application provides a clean interface with a blue-purple theme.

## 4. Technologies Used

| Technology               | Purpose                        |
| ------------------------ | ------------------------------ |
| Python                   | Backend programming            |
| Streamlit                | Web application interface      |
| MyMemory Translation API | Language translation           |
| Requests                 | API communication              |
| Streamlit Code Editor    | Automatic multiline text input |
| HTML & CSS               | Interface styling              |

## 5. Project Structure

```text
translationtool/
│
├── app.py
├── requirements.txt
└── README.md
```

## 6. Installation and Execution

**Step 1:** Open the project folder in VS Code.

**Step 2:** Open the terminal.

**Step 3:** Install the required libraries.

```bash
python -m pip install -r requirements.txt
```

**Step 4:** Run the application.

```bash
python -m streamlit run app.py
```

**Step 5:** Open the local URL displayed in the terminal.

## 7. How It Works

1. The user selects the source language.
2. The user selects the target language.
3. The user enters text in the input box.
4. The application sends the text to the translation API.
5. The translated text appears in the output box.
6. The user can copy the translation or swap languages.

## 8. Limitations

* An internet connection is required for translation.
* Translation accuracy depends on the external API.
* API usage limits may affect availability.
* Voice and image translation are not included in the current version.

## 9. Future Scope

* Voice translation using speech recognition.
* Image translation using OCR.
* Text-to-speech functionality.
* Translation history.
* Additional language support.

## 10. Conclusion

Anuvaad Setu demonstrates the integration of Python, Streamlit, and a translation API to develop a practical language translation application.

The project provides automatic text translation, multiple language support, and a user-friendly interface to help overcome language barriers.

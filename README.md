# Latecript

Latecript is a Python application that transcribes and translates audio from your input devices in real-time using the Speechmatics API. The application provides a Textual-based TUI for an interactive experience.

## Features

- **Real-Time Transcription:** Capture audio and transcribe speech in real-time.
- **Translation:** Translate transcribed text into different languages.
- **TUI Interface:** Interactive Textual UI for settings and displaying logs.
- **Configurable Settings:** Read credentials and configuration from a local JSON file.

## Requirements

- Python 3.12 or above
- [Uv](https://github.com/uv-org/uv) (for dependency management)
- [Speechmatics Python SDK](https://github.com/speechmatics/speechmatics-python)
- [Textual](https://github.com/Textualize/textual)


## Getting your audio output as a usable input. 

### MacOs 

You can use BlackHole for audio loopback. It can be installed via brew: 
```bash
brew install blackhole-2ch
```

## Speechmatics API key 

You can generate your speechmatics API key from your user account in speechmatics. 

## Installation

2. Install the dependencies using uv:

   ```bash
   uv install
   ```

   To install development dependencies, run:

   ```bash
   uv install -e dev
   ```

3. To run Latecript, execute:

   ```bash
   uv run latecript --settings_file [path to your settings file]
   ```

## Usage

Create a `.settings.json` with the following structure:

```json
{
  "speechmatics_api_key": "Your Speechmatics API Key",
  "output_device": "Blackhole 2ch",
  "transcription_language": "fr-FR",
  "translation_language": "en-US"
}
```

You can provide an alternative settings file via the command line:

```bash
uv run latecript --settings_file /path/to/your/settings.json
```

If no settings file is providedn, you will land on the settings tab. 

## Usage

To run Latecript, simply execute:

```bash
python -m latecript
```

This will launch the TUI application where you can select audio devices and manage transcription/translation settings.


## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please open issues and submit pull requests for improvements and bug fixes.

## Acknowledgements

- [Speechmatics](https://www.speechmatics.com/) for the API and SDK.
- [Textual](https://github.com/Textualize/textual) for the TUI framework.
- [BlackHole](https://existential.audio/blackhole/) for audio loopback driver for mac. 

(Developped quick and dirty with the help of Copilot)
# AudioToText
Converts an audio file to a text file.

## Dependencies

Run the following command to install the dependencies:

    $ pip install -r requirements

## Usage

    usage: audio_to_text.py [-h] [-o OUTPUT] [-l LANGUAGE] input

    Converts an audio file to text.

    positional arguments:
        input                           The input audio file.

    optional arguments:
        -h, --help                      show this help message and exit
        -o OUTPUT, --output OUTPUT
                                        The output file for the text. Default 'outputText.txt'
        -l LANGUAGE, --language LANGUAGE
                                        See 'https://cloud.google.com/speech-to-text/docs/languages'
                                        for all possible language codes, Default is en-GB.

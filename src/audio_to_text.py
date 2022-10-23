#!/usr/bin/env python3

import argparse
import os
import pathlib
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence


class AudioToText:
    """ Converts an audio file to text. """

    def __init__(self, fileInput, fileOutput, language):
        """ Initialize. """
        self.input = fileInput
        self.output = fileOutput
        self.language = language
        self.minSilenceLen = 500                # The minimum length for silent sections in milliseconds.
        self.silenceThresh = 14                 # The upper bound for how quiet silent in dBFS.
        self.keepSilence = 500                  # How much silence to keep in ms or a bool.

        self.__check_files_valid()

        # Create a speech recognition object
        self.rec = sr.Recognizer()


    def get_text(self):
        """ Returns the text recognized from the input file. """
        self.__check_files_valid()

        # Open audio file
        sound = AudioSegment.from_file(self.input, format=pathlib.Path(self.input).suffix.replace(".", ""))

        print(f"Running script on file: {self.input}")
        print(f"Length of audio file:     {int(len(sound) / 1000.0)} seconds.")

        # Split audio into chunks
        silenceThresh = sound.dBFS - self.silenceThresh
        print("Splitting file into chunks...")
        chunks = split_on_silence(  sound,
                                    min_silence_len=self.minSilenceLen,
                                    silence_thresh=silenceThresh,
                                    keep_silence=self.keepSilence)

        fullText = ""
        print("Translating chunks into text...")
        for i in range(len(chunks)):
            chunk = chunks[i]
            obj = chunk.export(format="wav")

            with sr.AudioFile(obj) as source:
                audioListened = self.rec.record(source)

                try:
                    text = self.rec.recognize_google(audioListened, language=self.language)
                except sr.UnknownValueError as e:
                    pass
                else:
                    text = f"{text.capitalize()}. "
                    fullText += text

        return fullText


    def write_to_text_file(self, text):
        """ Write a text to a file. """
        print(f"Writing text to file: {self.output}")
        with open(self.output, "w") as f:
            f.write(text)


    def __check_files_valid(self):
        """ Check to see if the files are valid. """
        if not isinstance(self.input, str):
            raise Exception(f"{self.input} is not of type str.")
        if not os.path.exists(self.input):
            raise Exception(f"{self.input} path does not exist.")

        if not isinstance(self.output, str):
            raise Exception(f"{self.output} is not of type str.")
        dirname = os.path.dirname(self.output)
        if not dirname == "" and not os.path.exists(dirname):
            raise Exception(f"Some directories may be missing in path: {self.output}.")



if __name__ == "__main__":
    description = "Converts an audio file to text."
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__), description=description)

    # parser.add_argument(dest="input", help="The input audio file.")
    # parser.add_argument("-i", "--input", help="The input audio file.", required=True)
    parser.add_argument("-o", "--output", help="The output file for the text. Default 'outputText.txt'")
    parser.add_argument("-l", "--language", help="See 'https://cloud.google.com/speech-to-text/docs/languages' \
                                                for all possible language codes, Default is en-GB.")
    args = parser.parse_args()

    inputFile = 'videoplayback.wav'
    outputFile = args.output
    language = args.language

    if outputFile == None:
        outputFile = "outputText.txt"

    if language == None:
        language = "en-GB"

    obj = AudioToText(inputFile, outputFile, language)
    text = obj.get_text()
    obj.write_to_text_file(text)

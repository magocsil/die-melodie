# Die Melodie

This application is created by the students from FH Technikum Wien in hopes to fill a challenging daily life with joy and melody.

## Description
The goal of this project is to recognize the content of a music sheets and convert it to ABC notation, that can be read with a screen reader.
- ### Goals and their states in the project
   - [x] The program reads a .pdf file, containing the music sheets.
   - [x] The program recognizes the sets of staffs.
         - Note: if the staffs are not completely horizontal, the recognition is buggy.
   - [x] The program recognizes the clef.
   - [x] The application recognizes the time signature.
   - [ ] The application recognizes the notes correctly.
         - The notes in the output go a bit below or above the actual notes.
         - Note: the current program output doesn't yet uses the format of the sample below.
   - [x] The application has a readaloud part (like a screen reader).
   - [x] The application converts the notes into audible files.
   - [x] The application runs on a locally hosted server.
   - [ ] Bars and voices can be selected while playing the music.

- ### The used musical notation
The output looks like this:
```Default 8. 4/4. 1#. 3D5. 1C5. 2B4. 1A4. 1G4. | 2F#4. 2G4. 4F#4. | 3B4. 1C4. 2D4. 1C4. 1B4. | 2A4. 2G4. 2A4. | 2G4. 4G4. 2C4. | 2D4. 2E4. 4D4. :||```
- [x] `3D5` defines a musical note where `3` is its length times the default (reference) rythmic value, `D` is the name of the ABC note and `4` is the octave selection, where
      - 4 is the middle octave,
      - 3 is the octave below that,
      - 5 is the octave above that,
      - and so on.
- [x] `|` defines a bar, `:||` and `||:` encapsulate a repeat sign, `||` signs the end of the piece.
- [x] `1#` defines the key signature. `1` is the number of the modulations, which can be `#` for a sharp or `b` for a flat.
- [x] `4/4` defines the time signature.
- [x] `Default 8` defines the lowest rhythmic value appearing in the music sheet. This is a reference, and every note's length marker (their first digit) is relative to this number.
- In this case, `3D5` is a dotted two-lined D quarter note.

## Setting up the project

- ### Install Python
- ### Running the server
   - [x] Open your project folder in a command line
   - [x] Run the following command to get the dependencies (mainly `Flask`) installed
      - Open your project folder in a command line and run the following command:
        - ```python -m pip install flask```
   - [x] Run the following command to start the server
      - Open your project folder in a command line and run the following command:
        - ```python app.py```
   - [x] Go to the website to see the app running
      - http://127.0.0.1:4949/ 
      - http://localhost:4949/

- ### Running the different parts of the application
   - [x] Run the conversion tool only
         - Open your project folder in a command line and run the following command:
            - ```python src/main.py [input file path] [output folder]```
   - [x] Run the music player tool only
         - Open your project folder in a command line and run the following command:
            - ```python src/play.py [music file path]```

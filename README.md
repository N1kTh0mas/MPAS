# MPAS - Microscreen Public Address System

© Nik Thomas 2024

## Completed Items

- **Basic HTML Layout** using Bootstrap
- **Client-Side Python Script for TTS**:
    - **arg 1**: Text for Text-to-Speech (str)
    - **arg 2**: 0 for English-only Speech, 1 for English and Spanish Speech (int)
    - **arg 3**: List of speaker IDs that the server wants to play the message on (list)
    - **arg 4**: Speaker Mode: 
        - 1 for Announcement
        - 2 for Alarm with Announcement
        - 3 for Alarm only
    - **arg 5 (Optional)**: If in Speaker Mode 2 or 3, specify which alarm will be played
    - **arg 6 (Optional)**: If in Speaker Mode 2 or 3, specify how many times the alarm should replay

    ### Example:

    ```bash
    python SoundHandler.py "Hello World" 1 [100, 101, 105, 107]
    ```

    This will play "Hello World" in both English and Spanish over speakers 100, 101, 105, and 107.

## Things To Do

- Add the ability to play audio files in place of TTS for alarm sounds, etc.
- Connect HTML JavaScript variables to the server
- Create a server to communicate with `SoundHandler.py` and pass arguments
- Create a client-server to run `SoundHandler.py` on Raspberry Pis and pass arguments

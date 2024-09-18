# MPAS
 Microscreen Public Adress System




Copyright Nik Thomas 2024


Completed Items:

Basic HTML Layout using bootstrap
Client Side Py script for tts
    Current args
    arg 1: Text for Text to speech (str)
    arg 2: 0 for English only Speech, 1 for English and Spanish Speech (int)
    arg 3: List of speaker ids that server wants to play message. (list)

    Example SoundHandler.py "Hello World" 1 [100,101,105,107]
    This will play Hello World in Spanish and English over speakers 100, 101, 105, and 107

Things to do:

Add the ability to play audio files that in TTS for alarm sounds etc

Need to connect HTML js vars to server

Create server to communicate to SoundHandler and pass args

Create client server to run SoundHandler and pass args on pis

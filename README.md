# MPAS
 Microscreen Public Adress System




Copyright Nik Thomas 2024


Completed Items:

Basic HTML Layout using bootstrap
Client Side Py script for tts
    #arg 1: Text for Text to speech (str)
    #arg 2: 0 for English only Speech, 1 for English and Spanish Speech (int)
    #arg 3: List of speaker ids that server wants to play message. (list)
    #arg 4: Speaker Mode 1 for Annoucement, 2 for Alarm with Anoucement, 3 Just Alarm
    #arg 5(Opt): If in Speaker Mode 2 or 3. Which Alarm will be played. 
    #arg 6(Opt): If in Speaker Mode 2 or 3. How many times do you want alarm replayed

    Example SoundHandler.py "Hello World" 1 [100,101,105,107]
    This will play Hello World in Spanish and English over speakers 100, 101, 105, and 107

Things to do:

Add the ability to play audio files that in TTS for alarm sounds etc

Need to connect HTML js vars to server

Create server to communicate to SoundHandler and pass args

Create client server to run SoundHandler and pass args on pis

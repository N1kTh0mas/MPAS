import asyncio
import edge_tts
import pygame
import sys
from googletrans import Translator
import ast

SPEAKER_ID = 100
if len(sys.argv) < 4:
    print("Argument 3 is missing. Exiting the script.")
    sys.exit(1) 

arg_as_list = ast.literal_eval(sys.argv[3])


if SPEAKER_ID in arg_as_list:


    pygame.init()

    def playSound(file):
        sound = pygame.mixer.Sound(file)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

    TEXT = "Error No Text Provided"

    SPEAK_BOTH = 0

    VOICES = [ 'es-MX-DaliaNeural', 'en-CA-LiamNeural']
    TEXT = sys.argv[1]
    VOICE = VOICES[1]
    VOICE_ES = VOICES[0]
    OUTPUT_FILE = "pa.mp3"
    OUTPUT_FILE_ES = "pa_es.mp3"

    SPEAK_BOTH = sys.argv[2]

    async def amain():
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(OUTPUT_FILE)
    
    asyncio.run(amain())

    playSound(OUTPUT_FILE)

    if (int(SPEAK_BOTH) == 1):
        translator = Translator()
        TEXT_ES_TRANS = translator.translate(TEXT, dest='es')
        TEXT_ES = TEXT_ES_TRANS.text
        async def esmain():
            communicate_es = edge_tts.Communicate(TEXT_ES, VOICE_ES)
            await communicate_es.save(OUTPUT_FILE_ES)   
        asyncio.run(esmain())
        playSound(OUTPUT_FILE_ES)


else:
    print('ERROR with SPEAKER ID')

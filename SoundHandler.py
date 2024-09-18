import asyncio
import edge_tts
import pygame
import sys , time
from googletrans import Translator
import ast


#arg 1: Text for Text to speech (str)
#arg 2: 0 for English only Speech, 1 for English and Spanish Speech (int)
#arg 3: List of speaker ids that server wants to play message. (list)
#arg 4: Speaker Mode 1 for Annoucement, 2 for Alarm with Anoucement, 3 Just Alarm
#arg 5(Opt): If in Speaker Mode 2 or 3. Which Alarm will be played. 
#arg 6(Opt): If in Speaker Mode 2 or 3. How many times do you want alarm replayed

#Sets Speaker ID
SPEAKER_ID = 100
#Starts Pygame
pygame.init()

#Function to play an mp3 via pygame
def playSound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))


#Checks for 3 Arguments
if len(sys.argv) < 5:
    print("Argument 4 is missing. Exiting the script.")
    sys.exit(1) 

#Sets speaker mode from arg 4
S_Mode = sys.argv[4]

print("S_mode: "+S_Mode)

match S_Mode:
    case "1":
        #Converts arg3 into a list
        arg_as_list = ast.literal_eval(sys.argv[3])
        if SPEAKER_ID in arg_as_list:


            #Defines Text with default values then overwrites args
            TEXT = "Error No Text Provided"
            SPEAK_BOTH = 0
            VOICES = [ 'es-MX-DaliaNeural', 'en-CA-LiamNeural']
            TEXT = sys.argv[1]
            VOICE = VOICES[1]
            VOICE_ES = VOICES[0]
            OUTPUT_FILE = "MPAS/pa.mp3"
            OUTPUT_FILE_ES = "MPAS/pa_es.mp3"
            SPEAK_BOTH = sys.argv[2]

            #Processes English TTS Text to mp3
            async def amain():
                communicate = edge_tts.Communicate(TEXT, VOICE)
                await communicate.save(OUTPUT_FILE)
            
            asyncio.run(amain())

            playSound("MPAS/audio/DingDong.mp3")
            time.sleep(1)
            #Plays English TTS mp3
            playSound(OUTPUT_FILE)

            #Checks if Spanish Annoucement was requested. If so repeats English Sound playing
            if (int(SPEAK_BOTH) == 1):
                translator = Translator()
                TEXT_ES_TRANS = translator.translate(TEXT, dest='es')
                TEXT_ES = TEXT_ES_TRANS.text
                async def esmain():
                    communicate_es = edge_tts.Communicate(TEXT_ES, VOICE_ES)
                    await communicate_es.save(OUTPUT_FILE_ES)   
                asyncio.run(esmain())
                playSound(OUTPUT_FILE_ES)


            
            playSound("MPAS/audio/DingDong.mp3")
            #Error Checking
        else:
            print('Speaker not in ID list')

    case "2":
        #Mode 2
        #Converts arg3 into a list
        arg_as_list = ast.literal_eval(sys.argv[3])
        if SPEAKER_ID in arg_as_list:


            #Defines Text with default values then overwrites args
            TEXT = "Error No Text Provided"
            SPEAK_BOTH = 0
            VOICES = [ 'es-MX-DaliaNeural', 'en-CA-LiamNeural']
            TEXT = sys.argv[1]
            VOICE = VOICES[1]
            VOICE_ES = VOICES[0]
            OUTPUT_FILE = "MPAS/pa_m2.mp3"
            OUTPUT_FILE_ES = "MPAS/pa_es_m2.mp3"
            SPEAK_BOTH = sys.argv[2]
            ALARM_TYPE = sys.argv[5]
            ALARM_AMT = int(sys.argv[6])

            ALARM_FILE = "MPAS/audio/"+ALARM_TYPE+".mp3"

            #Processes English TTS Text to mp3
            async def amain():
                communicate = edge_tts.Communicate(TEXT, VOICE)
                await communicate.save(OUTPUT_FILE)
            
            asyncio.run(amain())

            

            #Checks if Spanish Annoucement was requested. If so repeats English Sound playing
            if (int(SPEAK_BOTH) == 1):
                translator = Translator()
                TEXT_ES_TRANS = translator.translate(TEXT, dest='es')
                TEXT_ES = TEXT_ES_TRANS.text
                async def esmain():
                    communicate_es = edge_tts.Communicate(TEXT_ES, VOICE_ES)
                    await communicate_es.save(OUTPUT_FILE_ES)   
                asyncio.run(esmain())
                
                for x in range(ALARM_AMT):
                    playSound(ALARM_FILE)
                    playSound(ALARM_FILE)
                    playSound(OUTPUT_FILE)
                    playSound(OUTPUT_FILE_ES)
                    playSound(ALARM_FILE)
                    playSound(ALARM_FILE)
                    x = x + 1

            else:
                
                for x in range(ALARM_AMT):
                    playSound(ALARM_FILE)
                    playSound(ALARM_FILE)
                    #Plays English TTS mp3
                    playSound(OUTPUT_FILE)
                    playSound(ALARM_FILE)
                    playSound(ALARM_FILE)
                    print("Sound")
                    x = x + 1



            
            #Error Checking
        else:
            print('Speaker not in ID list')
    
    case "3":
        ALARM_TYPE = sys.argv[5]
        ALARM_AMT = int(sys.argv[6])

        ALARM_FILE = "MPAS/audio/"+ALARM_TYPE+".mp3"

        for x in range(ALARM_AMT):
            playSound(ALARM_FILE)
            x = x + 1


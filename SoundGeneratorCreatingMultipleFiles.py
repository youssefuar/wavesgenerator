import wave
import math
import binascii
import winsound
import os

x=str(input("enter une chaine de caractere"))

#define parameters of files to create
nbCanal = 1   
nbOctet = 2    
fech = 44100
frequence = 409
niveau = 1
duree = 1
nbEchantillon = int(duree*fech)
parametres = (nbCanal,nbOctet,fech,nbEchantillon,'NONE','not compressed')
amplitude = 127.5*niveau
j=0

#Do the magic and create my waves
for i in range(len(x)):
    if x[i]=="a" :
        Filename= "MySound"+ str(j) + ".wav"
        j+=1
        Monson = wave.open(Filename,'w')
        Monson.setparams(parametres)
        for i in range(0,nbEchantillon):
                val = wave.struct.pack('B',int(128.0 + amplitude*math.sin(2.0*math.pi*frequence*i/fech)))
                Monson.writeframes(val)
        Monson.close()

#iterate over working directory and play created files
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".wav"):
        winsound.PlaySound(filename,winsound.SND_FILENAME)

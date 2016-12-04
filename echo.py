from pyechonest import config
config.ECHO_NEST_API_KEY="U8DREGOBOZJ2RPDKU"
import sys
import os
import subprocess
import glob
from os import path
from pyechonest import track
import pandas as pd
import socket

#f = open('results.txt','w')
#sys.stdout = f
socket.setdefaulttimeout(300)


audio_files = glob.glob('*.mp3')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
I=[]
J=[]
K=[]
L=[]
M=[]
N=[]
O=[]
P=[]
Q=[]
R=[]
try:

    for audio_file in audio_files:
        pytrack = track.track_from_filename(audio_file, timeout=300, force_upload=True)
        artist = pytrack.artist
        title = pytrack.title
        tempo = pytrack.tempo
        energy = pytrack.energy
        #if not pytrack.valence:
            # Track hasn't had latest attributes computed. Force an upload.
            #pytrack = track.track_from_filename(audio_file, timeout=150, force_upload=True)
        valence = pytrack.valence
        acousticness = pytrack.acousticness
        danceability = pytrack.danceability
        duration = pytrack.duration
        key = pytrack.key
        liveness = pytrack.liveness
        loudness = pytrack.loudness
        mode = pytrack.mode
        speechiness = pytrack.speechiness
        time_signature = pytrack.time_signature
        pytrack.get_analysis()
        key_confidence = pytrack.key_confidence
        mode_confidence = pytrack.mode_confidence
        tempo_confidence = pytrack.tempo_confidence
        time_signature_confidence = pytrack.time_signature_confidence

        A.append(artist)
        B.append(title)
        C.append(tempo)
        D.append(energy)
        E.append(valence)
        F.append(acousticness)
        G.append(danceability)
        H.append(duration)
        I.append(key)
        J.append(liveness)
        K.append(loudness)
        L.append(mode)
        M.append(speechiness)
        N.append(time_signature)
        O.append(key_confidence)
        P.append(mode_confidence)
        Q.append(tempo_confidence)
        R.append(time_signature_confidence)
        df = pd.DataFrame(A,columns=['Artist'])
        df['Title']=B
        df['Tempo']=C
        df['Energy']=D
        df['Valence']=E
        df['Acousticness']=F
        df['Danceability']=G
        df['Duration']=H
        df['Key']=I
        df['Liveness']=J
        df['Loudness']=K
        df['Mode']=L
        df['Speechiness']=M
        df['Time_signature']=N
        df['Key_confidence']=O
        df['Mode_confidence']=P
        df['Tempo_confidence']=Q
        df['Time_signature_confidence']=R
        
        df
        df.to_csv('echo.csv', encoding='utf-8')
except socket.timeout:
    print "Timed out!"

#f.close()
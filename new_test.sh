#!/bin/bash

# Das Datum und die Zeit erfassen
date=$(date +"%d-%m-%Y")
time=$(date +"%H-%M-%S")

dos2unix title.txt
dos2unix streamer.txt

# Titel und Streamer aus den Textdateien lesen
title=$(<title.txt)
stream=$(<streamer.txt)

# Entfernen der Textdateien
rm title.txt
rm streamer.txt
# Neuer Dateiname für das Video erstellen
newfile="$stream/$stream"_"$date"_"$time".mkv

# Streamlink aufrufen, um das Video herunterzuladen
streamlink -o "$newfile" twitch.tv/"$stream" best

# Python-Skript aufrufen, um das Video hochzuladen
python3 upload_video.py --file="$newfile" \
                        --title="$title - VoD | Panikfee" \
                        --description="VoD vom $date Youtube: https://youtube.com/Panikfee Twitch: https://www.twitch.tv/Panikfee" \
                        --keywords="Grand Theft Auto 5,GTA RP, Roleplay" \
                        --category="20" \
                        --privacyStatus="private" \
			--noauth_local_webserver

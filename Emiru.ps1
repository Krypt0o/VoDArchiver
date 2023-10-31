$fileToCheck = "C:\Twitch_Rec\Emiru.mkv"
$date=(get-date -Format d) -replace("/")
$time=(get-date -Format t) -replace(":")
$newfile = "Emiru"+"_"+"$date"+"_"+"$time"+".mkv"
streamlink -o Emiru.mkv twitch.tv/Emiru best
Rename-Item "C:\Twitch_Rec\Emiru.mkv" -NewName $newfile
$fileToCheck = "C:\Twitch_Rec\me.mkv"
$date=(get-date -Format d) -replace("/")
$time=(get-date -Format t) -replace(":")
$newfile = "me"+"_"+"$date"+"_"+"$time"+".mkv"
streamlink -o me.mkv twitch.tv/Kry_pt0 best
Rename-Item "C:\Twitch_Rec\me.mkv" -NewName $newfile
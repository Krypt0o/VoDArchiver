$fileToCheck = "C:\Twitch_Rec\EmiruBot.mkv"
$date=(get-date -Format d) -replace("/")
$time=(get-date -Format t) -replace(":")
$newfile = "EmiruBot"+"_"+"$date"+"_"+"$time"+".mkv"
streamlink -o EmiruBot.mkv twitch.tv/EmiruBot best
Rename-Item "C:\Twitch_Rec\EmiruBot.mkv" -NewName $newfile

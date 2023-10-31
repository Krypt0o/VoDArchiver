$date=(get-date -Format d) -replace("/")
$time=(get-date -Format t) -replace(":")
$streamer = Get-Content -Path .\streamer.txt
#Remove-Item D:\Twitch_Rec_Dev\streamer.txt
$stream = $streamer
$streamer = "$streamer"+".mkv"
$newfile = "$stream"+"_"+"$date"+"_"+"$time"+".mkv"
streamlink -o "$newfile" twitch.tv/"$stream" best

#streamlink -o Emiru.mkv twitch.tv/ best
#Rename-Item "$streamer" -NewName $newfile

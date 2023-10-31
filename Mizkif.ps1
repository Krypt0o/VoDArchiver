$fileToCheck = "C:\Users\KameraPC\Twitch_Rec\Mizkif.mkv"
$date=(get-date -Format d) -replace("/")
$time=(get-date -Format t) -replace(":")
$newfile = "Mizkif"+"_"+"$date"+"_"+"$time"+".mkv"
if (Test-Path $fileToCheck -PathType leaf)
{
    Rename-Item "C:\Users\KameraPC\Twitch_Rec\Mizkif.mkv" -NewName $newfile
    streamlink -o Mizkif.mkv twitch.tv/Mizkif best
}
else
{
    streamlink -o Mizkif.mkv twitch.tv/Mizkif best
}
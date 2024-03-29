# Splash Animation

Just some simple notes here.

Information on how to swap OpenAuto's splash animation here  
https://bluewavestudio.io/community/thread-987.html

Use this to convert from Android-style boot animation ZIP to MP4 if you need  
https://forum.xda-developers.com/t/tool-win-v1-86b-updated-bootanimation-zip-to-mp4-video-and-converter-porter.2651044/

[original](original/) contains the original OpenAutoPro boot animation. If you wish, this can be converted to MP4 like so:

```bash
for i in {1..2}; do ffmpeg -framerate 24 -i splash${i}.h264 -c copy splash${i}.mp4; done
```

Rough conversion process from Android-style boot animation ZIP to OpenAutoPro's expected H264 format below. I'm sure there's an easier way to do this, I just didn't bother trying 👀

* Use 'Boot Animation 2 mp4' (source linked above) to convert to MP4
  * Extract 'Boot Animation 2 mp4' to a directory. We'll call it `ba2mp4`, for the sake of example.
  * Place ZIP (source linked above) in `ba2mp4/zips`.
  * Launch the batch file in the `ba2mp4` directory. For the version I used, this was called `RUNba2mp4v186b.bat`.
  * Select option 2 to convert ZIP from `zips` directory.
  * Select your file.
  * Choose your loop options (I used `t0`).
  * If you wish, choose "5 - Change The Fps".  
    I changed the input and output FPS to 30 as the source's original FPS of 15 was too slow for my liking.
  * Choose "7 - Export As A Mp4 Style Bootanimation".
  * Choose the last few options (I stuck with the defaults).
  * Find converted ZIP file in `ba2mp4/Made_Zips`.
* Extract the MP4 files in the resulting ZIP. They're called `0x_google.mp4`, where `x` is the part.
* Assuming your animation has two parts, you can convert them to `h264` files like so:

```bash
for i in {1..2}; do ffmpeg -i 0${i}_google.mp4 -an -vcodec libx264 -crf 23 custom_splash${i}.h264; done
```

## My Animation

I sourced an animation from here  
https://forum.xda-developers.com/t/mod-boot-animations-taking-requests.3351617/ but didn't like it in the end.

I now use a cut of this https://www.youtube.com/shorts/9mE7AAkkdq8

```bash
yt-dlp https://www.youtube.com/shorts/9mE7AAkkdq8 -f 299 -o "Downloads/audi.%(ext)s"
ffmpeg -i Downloads/audi.mp4 -filter:v "crop=1024:600" Downloads/audi.mp4
ffmpeg -to 00:03 -i Downloads/audi.mp4 -c copy Downloads/audi-1.mp4
ffmpeg -ss 00:03 -i Downloads/audi.mp4 -c copy Downloads/audi-2.mp4
for i in {1..2}; do ffmpeg -i audi-${i}.mp4 -an -vcodec libx264 -crf 23 audi_splash${i}.h264; done
```

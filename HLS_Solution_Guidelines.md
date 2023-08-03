# HLS Local Solution

Here is an outline on how to replicate the local HLS solution on your own device, using some tools, our script and a video you choose or the default video we provide.

Prerequisites:
 - FFMPEG
 - Python
 - Git Bash
 - Running on Windows
**

## FFMPEG Installation

**
1.  Download FFmpeg:
  
    -   Go to the FFmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    -   Scroll down to the "Windows Builds" section.
    -   You'll see various options, but for simplicity, it's recommended to choose the "Static Builds" under the "Get the packages" section.
2.  Choose the 32-bit or 64-bit version:
    
    -   If your Windows version is 32-bit, download the 32-bit version.
    -   If your Windows version is 64-bit, download the 64-bit version.
3.  Extract the downloaded archive:
    
    -   Once the download is complete, extract the contents of the downloaded archive (zip file) to a location on your computer, for example, C:\ffmpeg.
4.  Set up environment variables (Optional, but recommended):
    
    -   To use FFmpeg conveniently from any command prompt window, you can set up environment variables.
    -   Right-click on "This PC" or "My Computer" and select "Properties."
    -   Click on "Advanced system settings" on the left-hand side.
    -   In the System Properties window, click the "Environment Variables" button.
    -   In the Environment Variables window, under "System variables," find the "Path" variable, and click "Edit."
    -   Click "New" and enter the path to the "bin" folder inside the extracted FFmpeg directory (e.g., C:\ffmpeg\bin).
    -   Click "OK" to save your changes.
5.  Verify the installation:
    
    -   Open a new Command Prompt window and type "ffmpeg" (without quotes) and press Enter.
    -   If everything is set up correctly, you should see the FFmpeg version information displayed in the command prompt.

FFmpeg should now be installed on your Windows machine, and you can use it for various multimedia tasks, such as video and audio conversion, editing, and more, directly from the command prompt or by using it in other programs or scripts.

**

## Cloning our Github Repository onto your local machine

**

To clone a GitHub repository onto your Windows computer, you can use either the command-line interface (CLI) or graphical user interface (GUI) options. Here's how to do it using both methods:

Method 1: Command-Line Interface (CLI) using Git

1.  Install Git: If you haven't already installed Git on your Windows computer, you can download and install it from the official website: [https://git-scm.com/downloads](https://git-scm.com/downloads)
    
2.  Open Command Prompt or Git Bash:
    
    -   Press `Win + R`, type "cmd," and press Enter to open Command Prompt.
    -   Alternatively, if you installed Git, you can open Git Bash by right-clicking in a folder and selecting "Git Bash Here."
3.  Navigate to the directory where you want to clone the repository: Use the `cd` command to change to the desired directory. For example:
    
    bashCopy code
    
    `cd C:\Users\YourUsername\Documents` 
    
4.  Clone the repository: In the Command Prompt or Git Bash, use the `git clone` command followed by the URL of the GitHub repository. For example:
    
    bashCopy code
    
    `git clone https://github.com/username/repository.git` 
    
    Replace "username" with the GitHub username and "repository" with the name of the repository you want to clone.
    
5.  Authenticate (if required): If the repository is private or requires authentication, Git will prompt you to enter your GitHub credentials.
    
6.  The repository will be cloned to your local machine: After cloning, you will see a new folder in the directory you navigated to, containing the cloned repository's files.
    

Method 2: Graphical User Interface (GUI) using GitHub Desktop

1.  Install GitHub Desktop: Download and install GitHub Desktop from the official website: [https://desktop.github.com/](https://desktop.github.com/)
    
2.  Open GitHub Desktop: Launch GitHub Desktop on your Windows computer.
    
3.  Sign in to your GitHub account (if required): If you have a GitHub account, sign in to GitHub Desktop with your credentials.
    
4.  Click "File" > "Clone Repository": In GitHub Desktop, go to the "File" menu and select "Clone Repository."
    
5.  Select the repository to clone: In the "Clone a repository" window, you'll see a list of your GitHub repositories. If the repository you want to clone is listed, select it. Otherwise, click the "URL" tab and enter the repository's URL manually.
    
6.  Choose the local path for cloning: Select the directory on your Windows computer where you want to clone the repository.
    
7.  Click "Clone": Click the "Clone" button, and GitHub Desktop will start cloning the repository to your local machine.
    

After completing the steps in either method, the GitHub repository will be cloned onto your Windows computer, and you can start working with the code locally.
**

## Selecting a Video

**
With the installed tools and the cloned repository, you can now decide which video you want to watermark. By default there is a video in the solution labeled "video", so you may use that or select your own by following these steps:
1. Make sure the video you wish to use is in the MP4 format
<a href="https://ibb.co/W6Z9wYd"><img src="https://i.ibb.co/t4gftWN/Selecting-A-Video-image-1.jpg" alt="Selecting-A-Video-image-1" border="0"></a>
3. Delete the default video named "video" from the folder
4. Move your MP4 video into the same folder and be sure to rename it to "video"
**

## Navigating the Directory and Packaging the video

**
Now that you have your video selected, we need to package the video by navigating the directory and running an FFMPEG command.
1. Open your Git Bash terminal
2. Type `ls` to list the directory you are in
3. Use `cd <folder_name>` to navigate through your folders until you are within the HLS solution folder. To ensure youre in the correct folder, use `ls` to list the contents and you should only see the `HLSmain.py` script, and your video
<a href="https://imgbb.com/"><img src="https://i.ibb.co/yd1J5Sy/Image-2.jpg" alt="Image-2" border="0"></a>
5. Now that you are in the correct folder, copy and paste the following FFMPEG command into the terminal and hit enter

ffmpeg -i video.mp4 \
-filter_complex \  "[0:v]split=3[v1][v2][v3]; \  [v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out];  [v3]scale=w=640:h=360[v3out]" \
-map "[v1out]" -c:v:0 libx264 -x264-params "nal-hrd=cbr:force- cfr=1" -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M 
-preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map "[v2out]" -c:v:1 libx264 -x264-params "nal-hrd=cbr:force- cfr=1" -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M 
-preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map "[v3out]" -c:v:2 libx264 -x264-params "nal-hrd=cbr:force- cfr=1" -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M 
-preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
-map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
-map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
-map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
-f hls \
-hls_time 2 \
-hls_playlist_type vod \
-hls_flags independent_segments \
-hls_segment_type mpegts \
-hls_segment_filename stream_%v/data%02d.ts \
-master_pl_name master.m3u8 \
-var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" stream_%v.m3u8
<a href="https://ibb.co/D97pbnD"><img src="https://i.ibb.co/R3CySWp/FFMPEG-PACKAGING-COMMAND.jpg" alt="FFMPEG-PACKAGING-COMMAND" border="0"></a>
<a href="https://imgbb.com/"><img src="https://i.ibb.co/yFtnZq0/Image-3.jpg" alt="Image-3" border="0"></a>
Now the video is packaged and you are ready to run our solution. Packaging is very important, it simulates the format that we would receive an HLS VOD in, if this were a cloud based system. What this packaging does is it takes the video, converts the video into 3 different video quality streams(360p, 720p, and 1080p), where each stream contains the video stored as segments. When streaming a video over the internet, the video is sent in segments and received in segments. 

The contents of this folder will now contain: the chosen video.mp4, 3 folders labeled stream_0, stream_1, and stream_2 containing the video segments, and 4 M3U8 playlists labeled master, stream_0, stream_1, and stream_2. The master playlist will contain a header for metadata and also point to each of the video quality stream playlists. Within each of the video quality stream playlists, they will point to the video segments for their respective video quality.
**

## Running the Script and Validating

**
To demo the solution and run the script you need to access git bash and do the following steps:
1. Use `ls` to list the contents of the current directory. If you are in the correct solution folder as before then you are ready, otherwise, use `cd` to navigate into the folder that has the solution
2. Run the command `python HLSmain.py`
3. Once you run the script, you will see printed to the terminal that each of the processes are complete.
4. In the terminal you will be prompted to enter the filename to validate. To test for a positive result and retrieve the UUID enter the filename output. To test for the negative result enter the filename master and the terminal will not print a result because there is no UUID in the playlist named master.
Positive Case
<a href="https://ibb.co/LRsBmSs"><img src="https://i.ibb.co/sRXcnjX/Positive-Case-Image.jpg" alt="Positive-Case-Image" border="0"></a>
Negative Case
<a href="https://imgbb.com/"><img src="https://i.ibb.co/NKkVdcr/Negative-Case-Image.jpg" alt="Negative-Case-Image" border="0"></a>
5. Looking at the contents of the folder using `ls` you can see the existence of new playlists. output which contains the watermark, and the output_stream playlists that contain the necessary pathing.
<a href="https://ibb.co/gTJt7S3"><img src="https://i.ibb.co/swqsPK2/Solution-Folder-Contents-Final.jpg" alt="Solution-Folder-Contents-Final" border="0"></a>
So, when running the script, our solution is taking the master playlist as an input and then generating a duplicate of the master playlist known as output, within output we insert our UUID into the header following the HLS metadata standard. To complete the output file, we must write into the output playlist, setting the paths between the output master playlist and each of the stream quality playlists. Next what is happening is that each of the stream quality playlists must have their paths set to point to the video segments for their respective resolution. So for stream_0, stream_1, and stream_2, we are creating duplicates of each playlist labeled output_stream_0, output_stream_1, output_stream_2, where the output versions of each playlists contain the set paths to their respective media segments. 

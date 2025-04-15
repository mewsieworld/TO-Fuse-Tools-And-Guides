[Original Thread](https://forum.ragezone.com/threads/re-how-to-use-pyros-nori-tool.1243705/)

Using the tool is easy.
Try following these steps, first, to begin to run it (TO-Fuse-Tools-And-Guides/guides/RunningTNT.txt)

You will see [a prompt like this come up](https://imgur.com/7cdf7cd7-3733-413d-9ae7-a8780671bf5c). This is how you dissect it.

So let's say you want to analyze all nri files in `C:/Path/To/Trickster/Data/Equip`
The command is `java -jar TNT.jar a C:/Path/To/Trickster/Data/Equip/*.nri`
You use * to symbolize what's called a wildcard, meaning it will match anything in the folder that matches before and after the *
If you want to do an individual .nri file, you would do the same process, except instead of `*.nri` you would put the nri file name like the following: `java -jar TNT.jar a C:/Path/To/Trickster/Data/Equip/example.nri`

It's really simple. Much of what you'll want to do with this tool, however, is extract bmps (I say this since my process is the same way where I create the cfg outside of this tool), meaning you will use the "e" mode most likely. My .bat files, especially the run_bulk4.bat, will help with running the tool for you and/or extracting them all from a directory for you.

Additionally:
How to use run_bulk4.bat:
1. Copy the path to the Trickster data folder (or any specific folder in the data folder, but the Data folder is a great place to just get it all done in one swoop; I like to use the general `C:/Path/To/Trickster/Data` [make sure to change the `C:/Path/To/` to the proper subfolders of your Trickster directory!!! Rookie mistake I've made a few times since it's not always obvious when a dev writes it :( ] to export them all at once)
2. Double click run_bulk4.bat
3. Paste (Ctrl+V) the Trickster Data Folder (or whatever folder) in the command prompt and press enter
4. Write Y if you want it to do subfolders (recurse; recommended for the main Data folder) or N if you don't (recommended for standalone folders)
5. Watch the magic happen! (It will take a while with this tool hahaha, it does it one by one, but it's still perfect for our purposes!)

# Manual Center Image Resizer

A tiny desktop app that lets you manually center images for batch standardization — no cropping, no stress.

Perfect for fuse assets, sprites, or literally any image that needs to fit inside a 200x200 square without losing anything.

## 🧠 What It Does

- Load a whole folder (recursively) of images
- Click where you want the center of each image to be
- Right-click to sample the background color
- Pads the image to fit perfectly inside a 200x200 canvas
- Saves as `.bmp` in a mirrored output folder

No cropping. No auto-alignment weirdness. Just your eye and your click.

## 🎯 Why?

I made this because I was importing a bunch of fuses that weren’t made with the same resolution or alignment. I needed a way to batch process them, but I also wanted precise manual control — especially over centering and background matching.

This fixes that.

When you're making bulk fuses, often, you will have different resolutions for your cropped files. If you didn't and used a template, you can more easily bulk import the animations. This tool is for people who want to do that but did not use a template, or already made the existing assets and want to have it transferrable easily.

This is not to say it will not require manual adjustment in your fuse tool, but it should negate a lot of the stress you would've otherwise had if you were doing all of these by hand like I was.

## 🧰 Features

- ✅ Manual center selection (left-click)
- ✅ Background color sampling (right-click)
- ✅ Resolution-agnostic batch import
- ✅ Consistent output (200x200 BMP)
- ✅ Mirror original folder structure
- ✅ Clean GUI with no terminal popping up

## 📸 How to Use

1. Run the app (`manual_resizer.exe` or the Python script)
2. Select the parent folder containing all your images
3. For each image:
   - 🖱 Left-click where you want the center to be
   - 🖱 Right-click on the background to set the padding color
   - ➡️ Automatically moves to the next image
4. Find your processed images in the `output_resized/` folder

## 🐍 If You're Using the Python Script

Make sure you have these installed/run this ahead of time in your terminal:

```pip install pillow```

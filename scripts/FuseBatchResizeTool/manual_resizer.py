import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Config
TARGET_SIZE = (200, 200)
OUTPUT_FOLDER = "output_resized"

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manual Center Image Resizer")

        self.image_paths = []
        self.base_folder = ""
        self.current_index = 0
        self.current_image = None
        self.tk_image = None
        self.display_image = None
        self.bg_color = (255, 255, 255)  # default background (white)

        self.canvas = tk.Canvas(root, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)

        root.bind("<Right>", self.next_image)
        root.bind("<Left>", self.prev_image)

        self.load_images()

    def load_images(self):
        self.base_folder = filedialog.askdirectory(title="Select Folder of Images")
        if not self.base_folder:
            self.root.quit()

        for root_dir, _, files in os.walk(self.base_folder):
            for file in files:
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                    self.image_paths.append(os.path.join(root_dir, file))

        if not self.image_paths:
            messagebox.showerror("Error", "No images found in the selected folder.")
            self.root.quit()

        self.show_image()

    def show_image(self):
        if not self.image_paths:
            return
        img_path = self.image_paths[self.current_index]
        self.current_image = Image.open(img_path).convert("RGB")  # ensure RGB mode

        self.display_image = self.current_image.copy()
        max_display_size = (600, 600)

        try:
            resample_filter = Image.Resampling.LANCZOS
        except AttributeError:
            resample_filter = Image.ANTIALIAS

        self.display_image.thumbnail(max_display_size, resample_filter)

        self.tk_image = ImageTk.PhotoImage(self.display_image)
        self.canvas.delete("all")
        self.canvas.config(width=self.tk_image.width(), height=self.tk_image.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def on_left_click(self, event):
        if not self.current_image or not self.display_image:
            return

        disp_w, disp_h = self.display_image.size
        orig_w, orig_h = self.current_image.size

        scale_x = orig_w / disp_w
        scale_y = orig_h / disp_h

        center_x = int(event.x * scale_x)
        center_y = int(event.y * scale_y)

        self.process_image(center_x, center_y)
        self.next_image()

    def on_right_click(self, event):
        if not self.current_image or not self.display_image:
            return

        disp_w, disp_h = self.display_image.size
        orig_w, orig_h = self.current_image.size

        scale_x = orig_w / disp_w
        scale_y = orig_h / disp_h

        sample_x = int(event.x * scale_x)
        sample_y = int(event.y * scale_y)

        # Clamp to image bounds
        sample_x = max(0, min(sample_x, orig_w - 1))
        sample_y = max(0, min(sample_y, orig_h - 1))

        self.bg_color = self.current_image.getpixel((sample_x, sample_y))
        print(f"Sampled background color: {self.bg_color}")

    def process_image(self, cx, cy):
        img = self.current_image
        orig_w, orig_h = img.size
        target_w, target_h = TARGET_SIZE

        canvas_cx = target_w // 2
        canvas_cy = target_h // 2

        offset_x = canvas_cx - cx
        offset_y = canvas_cy - cy

        # Use sampled background color
        result = Image.new("RGB", (target_w, target_h), self.bg_color)

        paste_x = offset_x
        paste_y = offset_y

        from_x = max(0, -paste_x)
        from_y = max(0, -paste_y)
        to_x = min(orig_w, target_w - paste_x)
        to_y = min(orig_h, target_h - paste_y)

        cropped = img.crop((from_x, from_y, to_x, to_y))
        final_paste_x = max(paste_x, 0)
        final_paste_y = max(paste_y, 0)

        result.paste(cropped, (final_paste_x, final_paste_y))

        original_path = self.image_paths[self.current_index]
        relative_path = os.path.relpath(original_path, self.base_folder)
        output_dir = os.path.join(OUTPUT_FOLDER, os.path.dirname(relative_path))
        os.makedirs(output_dir, exist_ok=True)

        name, _ = os.path.splitext(os.path.basename(original_path))
        output_path = os.path.join(output_dir, f"{name}_resized.bmp")
        result.save(output_path, format="BMP")

    def next_image(self, event=None):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.show_image()
        else:
            messagebox.showinfo("Done", "All images processed!")
            self.root.quit()

    def prev_image(self, event=None):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()

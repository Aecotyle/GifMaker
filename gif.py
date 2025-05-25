import tkinter as tk
from tkinter import filedialog, messagebox
import imageio.v3 as iio
from PIL import Image, ImageTk
import os

class GifMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Maker")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")
        self.font_name = "Segoe UI"
        try:
            self.root.iconbitmap("interaction.ico")
        except Exception as e:
            print(f"Warning: Could not set icon: {e}")

        self.filenames = []
        self.preview_label = None

        # Frame for file selection
        file_frame = tk.LabelFrame(root, text="Select Images", bg="#f0f0f0", font=(self.font_name, 12, "bold"))
        file_frame.pack(padx=15, pady=10, fill=tk.BOTH, expand=False)

        self.file_listbox = tk.Listbox(file_frame, height=6, font=(self.font_name, 10))
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10,0), pady=10)

        scrollbar = tk.Scrollbar(file_frame, orient="vertical")
        scrollbar.config(command=self.file_listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y, pady=10, padx=(0,10))
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        select_button = tk.Button(file_frame, text="Select Images", command=self.select_files, bg="#4CAF50", fg="white", font=(self.font_name, 10, "bold"), relief="flat", padx=10, pady=5)
        select_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Frame for output options
        options_frame = tk.LabelFrame(root, text="Output Options", bg="#f0f0f0", font=(self.font_name, 12, "bold"))
        options_frame.pack(padx=15, pady=10, fill=tk.BOTH, expand=False)

        tk.Label(options_frame, text="Output GIF Filename:", bg="#f0f0f0", font=(self.font_name, 10)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.output_entry = tk.Entry(options_frame, font=(self.font_name, 10))
        self.output_entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=5)
        self.output_entry.insert(0, "team.gif")

        tk.Label(options_frame, text="Duration (ms):", bg="#f0f0f0", font=(self.font_name, 10)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.duration_entry = tk.Entry(options_frame, font=(self.font_name, 10))
        self.duration_entry.grid(row=1, column=1, sticky=tk.EW, padx=10, pady=5)
        self.duration_entry.insert(0, "500")

        tk.Label(options_frame, text="Loop Count (0=infinite):", bg="#f0f0f0", font=(self.font_name, 10)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.loop_entry = tk.Entry(options_frame, font=(self.font_name, 10))
        self.loop_entry.grid(row=2, column=1, sticky=tk.EW, padx=10, pady=5)
        self.loop_entry.insert(0, "0")

        options_frame.columnconfigure(1, weight=1)

        # Generate button
        generate_button = tk.Button(root, text="Generate GIF", command=self.generate_gif, bg="#2196F3", fg="white", font=(self.font_name, 12, "bold"), relief="flat", padx=10, pady=10)
        generate_button.pack(pady=15)

        # Label for preview
        preview_frame = tk.LabelFrame(root, text="GIF Preview", bg="#f0f0f0", font=(self.font_name, 12, "bold"))
        preview_frame.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

        self.preview_label = tk.Label(preview_frame, bg="white", relief="sunken", width=300, height=300)
        self.preview_label.pack(padx=10, pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
        )
        if files:
            self.filenames = list(files)
            self.file_listbox.delete(0, tk.END)
            for f in self.filenames:
                self.file_listbox.insert(tk.END, f)

    def generate_gif(self):
        if not self.filenames:
            messagebox.showerror("Error", "No image files selected.")
            return

        output_file = self.output_entry.get().strip()
        if not output_file:
            messagebox.showerror("Error", "Please specify an output GIF filename.")
            return

        try:
            duration = int(self.duration_entry.get().strip())
            loop = int(self.loop_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Duration and loop count must be integers.")
            return

        try:
            images = [iio.imread(filename) for filename in self.filenames]
            iio.imwrite(output_file, images, duration = duration, loop = loop)
            messagebox.showinfo("Success", f"GIF saved as {output_file}\nOutput directory: {os.path.abspath(os.path.dirname(output_file))}")
            self.show_preview(output_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create GIF: {e}")

    def show_preview(self, gif_path):
        try:
            self.frames = []
            img = Image.open(gif_path)
            # Load all frames
            try:
                while True:
                    frame = img.copy()
                    frame.thumbnail((300, 300))
                    self.frames.append(ImageTk.PhotoImage(frame))
                    img.seek(img.tell() + 1)
            except EOFError:
                pass

            self.frame_index = 0
            self.animate()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load GIF preview: {e}")

    def animate(self):
        if self.frames:
            frame = self.frames[self.frame_index]
            self.preview_label.config(image=frame)
            self.preview_label.image = frame
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.root.after(100, self.animate)  # Adjust delay as needed

if __name__ == "__main__":
    root = tk.Tk()
    app = GifMakerApp(root)
    root.mainloop()

import tkinter as tk
from PIL import Image, ImageDraw

class CoordinateDrawer:
    def __init__(self, root):
        self.root = root
        self.coordinates = []
        
        self.canvas = tk.Canvas(root, width=540, height=960, bg="white")
        self.canvas.pack()

        self.read_coordinates_from_file("DS7.txt")

        self.draw_coordinates()

        self.save_drawing()
    def read_coordinates_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    x, y = map(int, line.split())
                    self.coordinates.append((x, y))
        except (IOError, ValueError) as e:
            print(f"Error reading coordinates from file: {e}")

    def draw_coordinates(self):
        for x, y in self.coordinates:
            self.canvas.create_oval(x, y, x + 5, y + 5, fill="black")

    def save_drawing(self):
        file_path = "drawing540_960.png"
        img = Image.new("RGB", (960, 540), "white")
        draw = ImageDraw.Draw(img)

        for x, y in self.coordinates:
            draw.ellipse([x, y, x + 5, y + 5], fill="black")

        img.save(file_path, "PNG")
        print(f"Drawing saved to {file_path}")
if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateDrawer(root)
    root.mainloop()

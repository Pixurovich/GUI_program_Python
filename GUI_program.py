import tkinter as tk
from tkinter import ttk

class GUIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Графическая программа") 
        self.geometry("1024x768") 
        self.resizable(True, True)  

        self.ID = _______ 
        self.button_text = ""  
        self.triangle_color = "red" 
        self.axis_color = "black"
        self.x1, self.x2, self.x3 = 19, 81, 20
        self.y1, self.y2, self.y3 = 39, 93, 73

        self.create_widgets()  
        self.text_widget.bind("<Button-1>", self.change_text_widget_text) 
        self.update_button.config(command=self.update_triangle_coords)  
        self.bind("<Configure>", self.on_resize) 

    def create_widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)  

        self.top_frame = ttk.Frame(self.main_frame)
        self.top_frame.pack(side="top", fill="x")
        self.text_widget = tk.Label(self.top_frame, text=self.button_text, font=("Arial", 20), bg="light grey")
        self.text_widget.pack(side="top", fill="x", expand=True)

        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(self.left_frame)
        self.canvas.pack(pady=10, fill="both", expand=True)

        self.coord_frame = ttk.Frame(self.left_frame)
        self.coord_frame.pack(pady=10, fill="x")

        labels = ["X1", "X2", "X3", "Y1", "Y2", "Y3"]
        self.entries = {label: ttk.Entry(self.coord_frame) for label in labels}
        for i, label in enumerate(labels):
            row = i // 3  
            ttk.Label(self.coord_frame, text=f"{label}:").grid(row=row, column=i % 3 * 2, padx=5, pady=5, sticky="w")
            self.entries[label].grid(row=row, column=i % 3 * 2 + 1, padx=5, pady=5, sticky="ew")

        self.update_button = ttk.Button(self.coord_frame, text="Обновить")
        self.update_button.grid(row=2, column=2, columnspan=2, pady=10, sticky="ew")

        self.right_frame = ttk.Frame(self.main_frame)
        self.right_frame.pack(side="right", fill="y")

        self.color_frame = ttk.LabelFrame(self.right_frame, text="Выбор цвета треугольника")
        self.color_frame.pack(pady=10, fill="y", expand=True)

        self.selected_color = tk.StringVar(value=self.triangle_color)
        colors = ["red", "green", "blue", "gray", "orange", "purple", "pink", "cyan"]
        for color in colors:
            ttk.Radiobutton(self.color_frame, text=color, variable=self.selected_color, value=color,
                            command=lambda c=color: self.set_triangle_color(c)).pack(anchor="w")

        self.axis_color_frame = ttk.LabelFrame(self.right_frame, text="Выбор цвета оси координат")
        self.axis_color_frame.pack(pady=10, fill="y", expand=True)
        self.selected_axis_color = tk.StringVar(value=self.axis_color)
        for color in colors:
            ttk.Radiobutton(self.axis_color_frame, text=color, variable=self.selected_axis_color, value=color,
                            command=lambda c=color: self.set_axis_color(c)).pack(anchor="w")

        self.draw_coordinate_system() 
        self.draw_triangle() 

    def draw_coordinate_system(self):
        self.canvas.delete("axis")
        self.canvas.delete("axis_labels")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height() 
        origin_x, origin_y = 50, height - 50  
        line_width = 5  

        self.canvas.create_line(origin_x, origin_y, width - 10, origin_y, arrow=tk.LAST, tags="axis", width=line_width,
                                fill=self.axis_color)
        self.canvas.create_line(origin_x, origin_y, origin_x, 10, arrow=tk.LAST, tags="axis", width=line_width,
                                fill=self.axis_color)

        self.canvas.create_text(width - 30, origin_y + 30, text="X", fill=self.axis_color, tags="axis_labels",
                                font=("Arial", 12, "bold"))
        self.canvas.create_text(origin_x - 30, 30, text="Y", fill=self.axis_color, tags="axis_labels",
                                font=("Arial", 12, "bold"))

        for i in range(0, 101, 10):
            x_position = origin_x + i * (width - 60) / 100
            self.canvas.create_line(x_position, origin_y - 5, x_position, origin_y + 5, fill=self.axis_color,
                                    tags="axis_labels")
            self.canvas.create_text(x_position, origin_y + 15, text=str(i), fill=self.axis_color, tags="axis_labels",
                                    font=("Arial", 8))

        for i in range(0, 101, 10):
            y_position = origin_y - i * (origin_y - 10) / 100
            self.canvas.create_line(origin_x - 5, y_position, origin_x + 5, y_position, fill=self.axis_color,
                                    tags="axis_labels")
            self.canvas.create_text(origin_x - 15, y_position, text=str(i), fill=self.axis_color, tags="axis_labels",
                                    font=("Arial", 8))

        self.draw_triangle() 

    def draw_triangle(self):
        self.canvas.delete("triangle")
        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()  
        origin_x, origin_y = 150, height - 30 

        max_x = max(self.x1, self.x2, self.x3, 1)
        max_y = max(self.y1, self.y2, self.y3, 1)
        scale_factor = min((width - origin_x + 400) / max_x, (height - origin_y + 400) / max_y)

        scaled_cords = [(origin_x + x * scale_factor, origin_y - y * scale_factor) for x, y in [(self.x1, self.y1),
                                                                                                (self.x2, self.y2),
                                                                                                (self.x3, self.y3)]]
        self.canvas.create_polygon(*scaled_cords, tags="triangle", fill=self.triangle_color)

    def change_text_widget_text(self, event):
        current_text = self.text_widget.cget("text")  
        # Переключение текста между ID и button_text
        self.text_widget.config(text=str(self.ID) if current_text == self.button_text else self.button_text)

    def set_triangle_color(self, color):
        self.triangle_color = color
        self.draw_triangle()  

    def set_axis_color(self, color):
        self.axis_color = color
        self.draw_coordinate_system()  

    def update_triangle_coords(self):
        try:
            self.x1 = int(self.entries["X1"].get())  # Получение значения X1
            self.y1 = int(self.entries["Y1"].get())  # Получение значения Y1
            self.x2 = int(self.entries["X2"].get())  # Получение значения X2
            self.y2 = int(self.entries["Y2"].get())  # Получение значения Y2
            self.x3 = int(self.entries["X3"].get())  # Получение значения X3
            self.y3 = int(self.entries["Y3"].get())  # Получение значения Y3
            self.draw_triangle() 
        except ValueError:
            print("Ошибка: Введите правильные числовые значения") 

    def on_resize(self, event):
        self.draw_coordinate_system()  

if __name__ == "__main__":
    app = GUIApp() 
    app.mainloop() 

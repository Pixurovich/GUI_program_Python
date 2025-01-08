# GUI_program_Python
GUI program in Python

Description
This program is a graphical application created using the Tkinter library. It allows the user to:

Interact with a graphical user interface.
Manage the coordinates of a triangle displayed on a canvas.
Change the colors of the triangle and coordinate axes.
Dynamically update the interface when resizing the window.
Key Features
Triangle Drawing:

Displays a triangle on a coordinate system.
Allows changing the triangle's coordinates through input fields.
Coordinate System:

Automatically scales the axes and triangle to fit the window size.
Allows changing the color of the axes.
Triangle Color Customization:

Select a color for the triangle from predefined options using radio buttons.
Interactive Text Widget:

A text widget that toggles between a predefined name and an identifier when clicked.
Adaptability:

The program automatically updates interface elements when the window size changes.
Installation and Launch
Ensure you have Python version 3.6 or later installed.
Download or copy the program code into a file, e.g., gui_app.py.
Run the program using the following command:
bash
Копировать код
python gui_app.py
Usage
Main Window:

Upon launching the program, a window opens with several sections:
Text Widget: Displays a name or identifier, which can be toggled by clicking.
Canvas: An area for drawing the triangle and coordinate system.
Coordinate Input Fields: For specifying triangle coordinates.
Update Button: To apply new coordinates.
Radio Buttons: For selecting colors for the triangle and axes.
Changing Triangle Coordinates:

Enter values in the X1, Y1, X2, Y2, X3, Y3 fields.
Click the "Update" button to apply the changes.
Changing Colors:

Use the radio buttons to select the triangle or axis colors.
Dynamic Adaptation:

When resizing the window, the coordinate system and triangle are automatically scaled.
Code Structure

Class GUIApp:
The main application class, inheriting from tk.Tk.
Implements the program's logic and interface.

Methods:
create_widgets: Creates all interface widgets.
draw_coordinate_system: Draws the coordinate system.
draw_triangle: Draws the triangle.
change_text_widget_text: Changes the text in the text widget.
set_triangle_color: Sets the triangle's color.
set_axis_color: Sets the axis color.
update_triangle_coords: Updates the triangle's coordinates.
on_resize: Handles window resizing events.

Main Loop:
The application runs via app.mainloop().

Requirements
Python 3.6 or later.
Tkinter library (included in the standard Python library).
Example Workflow
After launching the program, a window opens with a text widget, canvas, and control elements.
The user can:
Click on the text widget to toggle the displayed text.
Enter triangle coordinates and click "Update."
Change the triangle or axis colors.
Resize the window to adapt the interface.
Additional Notes
If invalid coordinate values are entered, the program outputs an error message in the console.
The program uses scaling to ensure the triangle always fits within the canvas, regardless of its dimensions.

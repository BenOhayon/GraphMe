import tkinter as tk
import DrawSettings as ds


def draw_axis(canvas_param):
    canvas_param.update()
    width_half = canvas_param.winfo_width() / 2
    height_half = canvas_param.winfo_height() / 2
    canvas_param.configure(scrollregion=(-width_half, -height_half, width_half, height_half))
    canvas_param.create_line(-width_half, 0, width_half, 0, fill='black')
    canvas_param.create_line(0, height_half, 0, -height_half, fill='black')


def _draw(canvas_param, func, draw_set):
    canvas_param.delete('all')
    draw_axis(canvas_param)
    for x in draw_settings.get_range():
        y = ds.calculate(x, func, draw_set)
        canvas.create_line(x, -y, x+1, -y-1, fill=draw_settings.get_color(), width=4)


def draw_graph():
    key = func_value.get()
    function_to_execute = draw_settings.get_options()[key]
    draw_settings.set_color(color_var.get())
    _draw(canvas, function_to_execute, draw_settings)


if __name__ == "__main__":
    window_main = tk.Tk()
    window_main.title("Graph Me")
    window_main.geometry("640x580")

    # Defining the settings of the drawings
    draw_settings = ds.DrawSettings(150, 'blue')

    # Creating the canvas to draw the graphs
    canvas = tk.Canvas(window_main, width=640, height=480)
    canvas.grid(row=0, column=0)

    # Drawing the axis of the graph
    draw_axis(canvas)

    # Creating a frame to hold the buttons
    bottom_frame = tk.Frame(window_main)
    bottom_frame.grid(row=1, column=0)

    tk.Label(bottom_frame, text="f(x) = ").grid(row=0, column=0)

    # Adding the option menu
    func_value = tk.StringVar()
    func_value.set('X^2')
    option_menu = tk.OptionMenu(bottom_frame, func_value, *(draw_settings.get_options().keys()))
    option_menu.grid(row=0, column=1)

    # Adding the color option menu
    colors = ['blue', 'red', 'green', 'black', 'pink', 'grey']
    color_var = tk.StringVar()
    color_var.set(colors[0])
    tk.Label(bottom_frame, text="Color:").grid(row=1, column=0)
    color_menu = tk.OptionMenu(bottom_frame, color_var, *colors)
    color_menu.grid(row=1, column=1)

    # Adding the drawing button
    tk.Button(bottom_frame, text="DRAW", command=draw_graph).grid(row=0, column=2)

    window_main.mainloop()

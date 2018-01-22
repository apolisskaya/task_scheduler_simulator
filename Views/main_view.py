import tkinter as tk


def init_main_view():
    main_window = tk.Tk()

    greeting = tk.Text(main_window)
    greeting.insert(tk.INSERT, "Task Scheduler Simulator")
    greeting.pack()

    main_window.mainloop()
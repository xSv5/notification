import tkinter as tk

def create_window():
    # Create the main window
    root = tk.Tk()

    # Set the window attributes
    root.overrideredirect(True)  # Remove window borders and title bar
    root.attributes('-topmost', True)  # Keep the window on top

    # Get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the desired window size (10% width and 7% height)
    window_width = int(screen_width * 0.1)   # 10% of screen width
    window_height = int(screen_height * 0.07)  # 7% of screen height

    # Calculate the Y coordinate with a gap of 8% from the bottom
    y_coordinate = screen_height - window_height - int(screen_height * 0.08)  # 8% gap from bottom

    # Set the geometry to position it off-screen to the right
    root.geometry('{}x{}+{}+{}'.format(
        window_width,
        window_height,
        screen_width,  # Start off-screen to the right
        y_coordinate  # Y coordinate with 20% gap from the bottom
    ))

    root.config(bg='black')  # Set the background color to black

    # Create a label to display the message
    message_label = tk.Label(root, text="Message Sent!", bg='black', fg='white', font=("Helvetica", 12))
    message_label.pack(expand=True, padx=10, pady=5)  # Center the label in the window

    # Function to glide the window into view
    def glide_window(step=0, delay=50):
        if step <= window_width:
            root.geometry('{}x{}+{}+{}'.format(
                window_width,
                window_height,
                screen_width - step,  # Move left
                y_coordinate  # Keep Y coordinate the same
            ))
            # Increase speed by decreasing delay as step increases
            root.after(delay, glide_window, step + 1, max(1, delay - 2))  # Minimum delay of 1 ms
        else:
            # Start a timer to hide the window after 5 seconds
            root.after(5000, lambda: glide_out(0, 50))  # Call glide_out after 5 seconds

    # Function to glide the window out of view
    def glide_out(step=0, delay=50):
        if step <= window_width:
            root.geometry('{}x{}+{}+{}'.format(
                window_width,
                window_height,
                screen_width - (window_width - step),  # Move right
                y_coordinate  # Keep Y coordinate the same
            ))
            # Increase speed by decreasing delay as step increases
            root.after(delay, glide_out, step + 1, max(1, delay - 2))  # Minimum delay of 1 ms
        else:
            root.destroy()  # Close the window after it's fully out of view

    # Bind mouse click to glide out function
    root.bind("<Button-1>", lambda event: glide_out(0, 50))  # On left mouse click

    # Start the glide animation
    glide_window()

    # Run the application
    root.mainloop()

if __name__ == '__main__':
    create_window()

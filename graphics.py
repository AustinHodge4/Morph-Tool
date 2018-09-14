from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Application():
    def __init__(self):
        # Create the window
        self.window = Tk()
        self.build_window()

    def build_window(self):
        def open_file(event):
            ''' Callback for select file boxes '''
            entry = event.widget
            initial_value = entry.get()
            entry.delete(0, "end")
            # Open dialog box to select only ppm file
            file_path = filedialog.askopenfilename(filetypes=(("PPM files", "*.ppm *.PPM"),))
            if file_path:
                # Change text box to file path
                entry.insert(0, file_path)
            else:
                entry.insert(0, initial_value)
        def morph(root, first_image_entry, second_image_entry, steps_entry, max_steps=500):
            ''' Morphs two images based on the number of steps '''
            default_value = 'Select PPM file'
            # Input validation
            if first_image_entry.get() == default_value or second_image_entry.get() == default_value or (first_image_entry.get() == '' and second_image_entry.get() == ''):
                messagebox.showerror(title='Hold up', message='Select two images!')
                print('Select two images!!')
                return
            if first_image_entry.get() == second_image_entry.get():
                messagebox.showerror(title='Hold up', message='The two images are the same!')
                print('Two images are the same!!')
                return
            if steps_entry.get() == '':
                messagebox.showerror(title='Hold up', message='Enter the Number of Steps!')
                print('Enter the number of steps!')
                return
            try:
                number_of_steps = int(steps_entry.get().replace(' ', ''))
                # Check if number of steps is over max steps
                if number_of_steps > max_steps:
                    messagebox.showerror(title='Hold up', message='The max Number of Steps is {}!'.format(max_steps))
                    print('Max number of steps reached!')
                    return
            except Exception:
                messagebox.showerror(title='Hold up', message='The Number of Steps is invalid!')
                print('The number of steps are invalid!')
                return

            # Start morphing
            print("Morphing")
            from formatPPM import format_images
            format_images(first_image_entry.get(), second_image_entry.get())
            from morph import morph_images
            morph_images(number_of_steps-2)
            messagebox.showinfo(title="Complete", message='Images exported to morph-images in current directory')

        # Set title, screen size, disable resizable window
        self.window.title('PPM Morph-Tool')
        self.window.geometry('{}x{}'.format(800, 230))
        self.window.resizable(0, 0)

        # First image label and input field
        first_image_label = Label(self.window, text="First Image", font='Helvetica 12 bold', anchor='w')
        first_image_label.place(x = 20, y = 30, width=120, height=25)
        # Input field
        first_image_entry = Entry(self.window)
        first_image_entry.insert(END, 'Select PPM file')
        # Setup callback on click
        first_image_entry.bind("<Button-1>", open_file)
        first_image_entry.place(x=20, y=60, width=350, height=32)

        # First image label and input field
        second_image_label = Label(self.window, text="Second Image", font='Helvetica 12 bold', anchor='w')
        second_image_label.place(x = 400, y = 30, width=120, height=25)
        # Input field
        second_image_entry = Entry(self.window)
        second_image_entry.insert(END, 'Select PPM file')
        # Setup callback on click
        second_image_entry.bind("<Button-1>", open_file)
        second_image_entry.place(x=400, y=60, width=380, height=32)

        # Number of Steps label and input field
        steps_label = Label(self.window, text="Number of Images (Inclusive)", font='Helvetica 12 bold', anchor='w')
        steps_label.place(x = 20, y = 96, width=350, height=25)
        steps_entry = Spinbox(self.window, from_=2, to=100)
        steps_entry.place(x=20, y=126, width=350, height=32)

        # Create Morph button and pass in the input field to the morph method on click
        button = Button(self.window, text='Morph!', width=25, command=lambda : morph(self.window, first_image_entry, second_image_entry, steps_entry))
        button.place(x=680, y=180, width=100)

        # Draw gui
        self.window.mainloop()



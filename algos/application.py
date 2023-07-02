from tkinter import Frame, Tk, Button
from typing import NoReturn

class Application(Frame):
    def __init__(
            self,
            name: str,
            fg_color: str,
            bg_color: str,
            font: tuple,
            root=Tk()
    ):
        # Get tk instance and
        super().__init__(root)
        self.root = root

        # Get application Data
        self.name = name
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.font = font

        # Pack and Run the main loop
        self._run()

    # Pack and execute the main frame and main loop
    def _run(self):
        # Packing application frame
        self.pack()

        # Pack sub components with determined style
        # Use Preferred rendering (packing) method
        self.pack_buttons()
        self.pack_entries()
        self.pack_labels()
        self.pack_texts()

        # Start main application loop
        self.mainloop()

    # Basic Components Packing functions by component classification
    def pack_buttons(self, ) -> NoReturn: pass
    def pack_entries(self) -> NoReturn: pass
    def pack_texts(self) -> NoReturn: pass
    def pack_labels(self) -> NoReturn: pass

    # Global Commands used for app-wise functionality
    def exit(self):
        return self.root.destroy

    # Online sync data capabilities for application usage
    def pull(self) -> dict: pass
    def push(self) -> NoReturn: pass








class MyApp(Application):
    # Define components here
    quit: Button

    # Implement the packing functions
    def pack_buttons(self):
        #QUIT BUTTON
        self.quit = Button(self, text="QUIT",
                            fg=self.fg_color,
                              command=self.exit())
        self.quit.pack(side="bottom")


    # Define commands in this subclass


app = MyApp()

import pygetwindow


class DetectWindow:
    def detect_window(self):

       # Get a list of all currently open windows
        windows = pygetwindow.getAllWindows()

        # Iterate through the windows and check if the title matches the desired window title
        for window in windows:
            if window.title == "Dofus Retro":
                window.activate()
                print("Activated Dofus Retro window")
                break

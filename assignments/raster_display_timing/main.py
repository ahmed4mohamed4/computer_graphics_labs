# Name: Ahmed Mohamed Sayedahmed
# ID: 245318

def read_number (prompt : str, min_num : float, include_min : bool = True) -> float:
    while True:
        try:
            value = float (input (prompt))

            if include_min:
                if value < min_num:
                    raise ValueError
            else:
                if value <= min_num:
                    raise ValueError

            return value
        except ValueError:
            print (f"Enter a number greater than or equal to {min_num}")


def frame (h : float) -> tuple:
    scan_lines = h
    horizontal_retrace = h - 1
    VERTICAL_RETRACES = 0

    return scan_lines, horizontal_retrace, VERTICAL_RETRACES


FRAME_RATE = 24  # frames per second

def video (h : float, t : float) -> tuple:
    frames = FRAME_RATE * t
    scan_lines = frames * h
    horizontal_retrace = frames * (h - 1)
    vertical_retraces = frames - 1

    return frames, scan_lines, horizontal_retrace, vertical_retraces


width = read_number (prompt= "Screen width (pixels): ", min_num= 1)
height = read_number (prompt= "Screen height (pixels): ", min_num= 1)
num_of_sec = read_number (prompt= "Video duration (seconds): ", min_num= 0, include_min= False)

# One frame
scan_lines, horizontal_retrace, vertical_retraces = frame (h= height)
print ("\n-> One frame")
print ("Scan lines:", scan_lines)
print ("Horizontal retrace:", horizontal_retrace)
print ("Vertical rate", vertical_retraces)


# Video
frames, scan_lines, horizontal_retrace, vertical_retraces = video (h= height, t= num_of_sec)
print ("\n-> Video")
print ("Frames:", frames)
print ("Scan lines:", scan_lines)
print ("Horizontal retrace:", horizontal_retrace)
print ("Vertical rate", vertical_retraces)
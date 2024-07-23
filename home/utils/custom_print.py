import inspect

def custom_print(*args, sep='\n'):
    # Get the caller's frame (the frame of the function that called this)
    caller_frame = inspect.currentframe().f_back
    # Get the file path and line number
    file_path = caller_frame.f_code.co_filename
    line_number = caller_frame.f_lineno
    # Print the values along with file path and line number
    print(f'File "{file_path}", line {line_number}', *args, sep=sep)
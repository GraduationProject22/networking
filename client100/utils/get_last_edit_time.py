def get_last_edit_time(file_name):
    import os
    return os.path.getmtime(file_name)

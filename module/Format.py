def path_formatting(file_path):
    if file_path.startswith('"') and file_path.endswith('"'):
        return file_path[1:-1]
    else:
        return file_path

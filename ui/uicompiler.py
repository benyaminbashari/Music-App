from PyQt5.uic import compileUi


def comp(ui_path, py_path):
    compileUi(ui_path, open(py_path, 'w'))


if __name__ == "__main__":
    comp('manage_playlist.ui', 'manage_playlist_form.py')


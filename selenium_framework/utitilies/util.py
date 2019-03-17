import os


def remove_png_from_screenshots_dir():
    """Cleanup function. Removes all .png files from screenshots dir
    before tests execution.
    """

    current_dir = os.path.dirname(__file__)
    screenshots_dir = os.path.join(current_dir, '../screenshots/')
    if os.path.exists(screenshots_dir):
        screenshots_dir_content = os.listdir(screenshots_dir)
        for file_name in screenshots_dir_content:
            if file_name.endswith('.png'):
                file_path = os.path.join(screenshots_dir, file_name)
                os.remove(file_path)

import pytest
from unittest import mock
import os

from Organize import file_type, file_move  # Replace with your actual filename (no .py)

@pytest.fixture
def fake_files():
    """Fake files to simulate inside directory."""
    return [
        "photo.jpg",         # Should go to Images
        "movie.mp4",         # Should go to Videos
        "song.mp3",          # Should go to Audio
        "report.pdf",        # Should go to Documents
        "archive.zip",       # Should go to Archives
        "script.py",         # Should go to Code
        "installer.exe",     # Should go to Applications
        "font.ttf",          # Should go to Fonts
        "driver.dll",        # Should go to System
        "unknown.xyz"        # Should go to Others
    ]

def test_file_type_full_mock(fake_files):
    # Arrange
    fake_dir = "/fake/dir"

    # Mock everything: os.listdir, os.path.exists, os.mkdir, shutil.move
    with mock.patch("os.listdir", return_value=fake_files), \
         mock.patch("os.path.isdir", return_value=False), \
         mock.patch("os.path.exists") as mocked_exists, \
         mock.patch("os.mkdir") as mocked_mkdir, \
         mock.patch("shutil.move") as mocked_move:

        # Simulate that no folders exist yet
        mocked_exists.return_value = False

        # Act
        file_type(fake_dir)

        # Assert
        expected_calls = [
            mock.call(os.path.join(fake_dir, "Images")),
            mock.call(os.path.join(fake_dir, "Videos")),
            mock.call(os.path.join(fake_dir, "Audio")),
            mock.call(os.path.join(fake_dir, "Documents")),
            mock.call(os.path.join(fake_dir, "Archives")),
            mock.call(os.path.join(fake_dir, "Code")),
            mock.call(os.path.join(fake_dir, "Applications")),
            mock.call(os.path.join(fake_dir, "Fonts")),
            mock.call(os.path.join(fake_dir, "System")),
            mock.call(os.path.join(fake_dir, "Others")),
        ]
        # Folder creation
        mocked_mkdir.assert_has_calls(expected_calls, any_order=True)

        # File moving
        expected_move_calls = [
            mock.call(os.path.join(fake_dir, "photo.jpg"), os.path.join(fake_dir, "Images", "photo.jpg")),
            mock.call(os.path.join(fake_dir, "movie.mp4"), os.path.join(fake_dir, "Videos", "movie.mp4")),
            mock.call(os.path.join(fake_dir, "song.mp3"), os.path.join(fake_dir, "Audio", "song.mp3")),
            mock.call(os.path.join(fake_dir, "report.pdf"), os.path.join(fake_dir, "Documents", "report.pdf")),
            mock.call(os.path.join(fake_dir, "archive.zip"), os.path.join(fake_dir, "Archives", "archive.zip")),
            mock.call(os.path.join(fake_dir, "script.py"), os.path.join(fake_dir, "Code", "script.py")),
            mock.call(os.path.join(fake_dir, "installer.exe"), os.path.join(fake_dir, "Applications", "installer.exe")),
            mock.call(os.path.join(fake_dir, "font.ttf"), os.path.join(fake_dir, "Fonts", "font.ttf")),
            mock.call(os.path.join(fake_dir, "driver.dll"), os.path.join(fake_dir, "System", "driver.dll")),
            mock.call(os.path.join(fake_dir, "unknown.xyz"), os.path.join(fake_dir, "Others", "unknown.xyz")),
        ]
        mocked_move.assert_has_calls(expected_move_calls, any_order=True)

def test_file_move_full_mock():
    # Arrange
    fake_dir = "/fake/dir"
    filename = "testfile.txt"
    folder_name = "TestFolder"

    # Patch os.path.exists, os.mkdir, shutil.move
    with mock.patch("os.path.exists", return_value=False) as mocked_exists, \
         mock.patch("os.mkdir") as mocked_mkdir, \
         mock.patch("shutil.move") as mocked_move:

        # Act
        file_move(fake_dir, filename, folder_name)

        # Assert
        mocked_mkdir.assert_called_once_with(os.path.join(fake_dir, folder_name))
        mocked_move.assert_called_once_with(
            os.path.join(fake_dir, filename),
            os.path.join(fake_dir, folder_name, filename)
        )

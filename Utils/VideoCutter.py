import cv2
import os
from pathlib import Path
from typing import List

def get_files_from_folder(path: Path) -> List[Path]:
    """
    Recursively lists and returns file paths in the given directory.

    This function iterates through the contents of the specified directory.
    If a file is found, its path is added to the list. If a directory is found,
    the function is called recursively to process its contents.
    If an entry is neither a file nor a directory, an OSError is raised.

    Parameters:
    path (Path): The directory path to search, as a pathlib.Path object.

    Returns:
    List[Path]: A list of file paths found in the directory.

    Raises:
    OSError: If an entry is neither a file nor a directory.
    """
    file_list = []
    
    try:
        for entry in path.iterdir():
            if entry.is_file():
                file_list.append(entry)
            elif entry.is_dir():
                file_list.extend(get_files_from_folder(entry))
            else:
                raise OSError(f"The path {entry} is neither a file nor a directory!")
    except OSError as e:
        print(f"An error occurred while processing {path}: {e}")
        raise
    
    return file_list


def extract_frames(video_path: Path, frames_per_minute: int, output_dir: Path) -> None:
    """
    Extracts a specified number of frames per minute from a video and saves them as image files.

    Parameters:
    video_path (Path): Path to the video file.
    frames_per_minute (int): Number of frames to extract per minute.
    output_dir (Path): Directory to save the extracted frames.
    """
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Open the video file
    video = cv2.VideoCapture(str(video_path))

    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames
    duration = total_frames / fps  # Duration of the video in seconds

    frames_per_second = frames_per_minute / 60
    frame_interval = int(fps / frames_per_second)

    frame_count = 0
    extracted_count = 0

    while video.isOpened():
        ret, frame = video.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            output_file = output_dir / f"frame_{extracted_count:06d}.jpg"
            cv2.imwrite(str(output_file), frame)
            extracted_count += 1

        frame_count += 1

    video.release()
    print(f"Extracted {extracted_count} frames to {output_dir}")


if __name__ == "__main__":
    input_path = Path(r"D:\Apps\Videos\4k")
    output_path = Path(r"D:\Apps\Frames")
    frames_per_minute = 1
    
    if not input_path.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    try:
        files = get_files_from_folder(input_path)
        print(f"Found {len(files)} files in the given path")
        
        for file in files:
            extract_frames(file, frames_per_minute, output_path)
    except OSError as e:
        print(f"Error: {e}")

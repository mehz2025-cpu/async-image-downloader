# Async Image Downloader

A Python project that downloads multiple images concurrently using asynchronous programming.

## Features

* Downloads multiple images concurrently
* Uses `asyncio` and `aiohttp`
* Displays download progress when the server provides the file size
* Reports downloaded bytes when the file size is unknown
* Tracks the number of completed downloads
* Handles download errors

## Technologies

* Python
* `asyncio`
* `aiohttp`

## Requirements

Python 3. Install the required package with:

```bash id="cf6x1j"
pip install -r requirements.txt
```

## Usage

Run the script:

```bash id="bg7tq2"
python image_downloader.py
```

The downloaded images are saved in the current working directory.

## Note

The image URLs are currently defined in the source code. The program attempts to download three images concurrently.

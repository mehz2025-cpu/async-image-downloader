# Async Image Downloader
import asyncio
import aiohttp


async def main():
    counter = [0]    
    await asyncio.gather(
        download_image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/FullMoon2010.jpg/330px-FullMoon2010.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail", "image1.jpg", counter, 3),
        download_image("https://placehold.co/300x300.jpg", "image2.jpg", counter, 3),
        download_image("https://placehold.co/800x200.jpg", "image3.jpg", counter, 3),
    )



async def download_image(url, filename, counter, total):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                total_size = int(response.headers.get("Content-Length", 0))
                downloaded = 0
                with open(filename, "wb") as f:
                    async for chunk in response.content.iter_chunked(1024):
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            percent = downloaded / total_size * 100
                            bar_length = 20
                            filled = int(bar_length * downloaded / total_size)
                            bar = "█" * filled + "░" * (bar_length - filled)
                            print(f"\r{filename}: [{bar}] {percent:.0f}%", end="")
                        else:
                            print(f"\r{filename}: {downloaded} bytes downloaded (size unknown)", end="")

                print()
                counter[0] += 1
                print(f"Overall: {counter[0]}/{total} files done")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")


asyncio.run(main())
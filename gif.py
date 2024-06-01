import imageio
import os
import imageio_ffmpeg as ffmpeg

ffmpeg_path = '/opt/homebrew/bin/ffmpeg'

os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

clip = os.path.abspath("File_path")

def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'Converting {inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for i, image in enumerate(reader):
        writer.append_data(image)
        print(f"Frame {i}")

    print("Done!")
    writer.close()

gifMaker(clip, '.gif')

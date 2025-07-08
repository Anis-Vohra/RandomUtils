"""
GIF Creator Script
Author: Anis Vohra
Date: 2025-07-08

Description:
This script takes a folder of JPG images and creates an animated GIF using Pillow.
Usage:
    python gif_creator.py --input "path/to/folder" --duration 50 --output "output.gif"
"""

from PIL import Image
import os
import argparse

def create_gif(input_folder, output_gif, duration=50):
    # Collect and sort all .jpg files in the folder
    jpg_files = sorted(
        [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    )

    if not jpg_files:
        print("❌ No JPG files found in the input folder.")
        return

    # Load images into a list of frames
    frames = [Image.open(os.path.join(input_folder, file)) for file in jpg_files]

    # Save the images as an animated GIF
    frames[0].save(
        output_gif,
        format='GIF',
        append_images=frames[1:],
        save_all=True,
        duration=duration,
        loop=0
    )

    print(f"✅ GIF created successfully: {output_gif}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create an animated GIF from JPG images.")
    parser.add_argument("--input", required=True, help="Path to folder containing JPG files.")
    parser.add_argument("--output", default="output.gif", help="Filename for the output GIF.")
    parser.add_argument("--duration", type=int, default=50, help="Frame duration in ms (default: 50ms).")

    args = parser.parse_args()
    create_gif(args.input, args.output, args.duration)

# Image Palettizer
![](https://img.shields.io/github/license/pureasbestos/image-palettizer.svg) ![](https://img.shields.io/github/languages/code-size/pureasbestos/image-palettizer.svg) ![](https://img.shields.io/badge/version-3.0.0--dev-mediumpurple.svg)

A program that applies a .gpl palette to an image by finding the nearest color in the palette for each pixel using the CIECAM02 UCS color space. This provides more accurate-to-eye results than can be achieved with a run of the mill graphics editor.

## Requirements
Requires Python 3 and the following packages to run from source:
- numpy
- imageio
- colorspacious
- psutil

Or, on Windows 64-bit, there are no additional requirements when using the binary version (found in releases).

## Installation
If you want to run from source, just download the repository and unzip it, or clone with `git clone https://github.com/PureAsbestos/Image-palettizer.git`. 

To run from binary on Windows 64-bit, simply download the executable from releases, or, for slightly faster startup times, use the portable installation.

## Usage
To begin, you’ll need two things: a palette in .gpl format, and an image (png, jpeg, etc.) When you run main.py (or the executable), you’ll have some options on screen, allowing you to select specifically what you want to do (dithering, etc.). You can click the `Browse` buttons to provide paths for the palette and image (it's worth noting that the image location can be a URL). You can also click the `Get palette from Lospec` button to quickly grab a palette from [Lospec's excellent palette list](https://lospec.com/palette-list). When you are ready to begin, click `Apply`. You should see some loading bars, and then a preview window will pop up, allowing you to save your image (Note that the preview image may be of reduced quality, but this will not affect the final output). Click `Save As...` to choose where to save the file (and what to call it), then click `Save` to save it. See *Features* for specific capabilities.

### Example
![Mona Lisa Palettization](https://github.com/PureAsbestos/Image-palettizer/blob/master/mona-lisa.png)
Palette can be found here: [Dawnbringer's 16 color palette](http://pixeljoint.com/forum/forum_posts.asp?TID=12795)

## Features
Besides the core features that have been discussed, this program offers:
- The ability to dither with 9 common error-diffusion methods
- The ability to dither with 4 sizes of Bayer matrix (2x2, 3x3, 4x4, 8x8)
- Integration with [Lospec](https://lospec.com/palette-list) for easy retrieval and use of color palettes
- The ability to dither using a loaded image as the threshold matrix (this is especially useful for dithering with a blue-noise texture, but any texture can be used) **This has not yet been implemented in the GUI version**
- The ability to work with large images (note that *extremely* wide images may take up too much RAM)

## To-do
- Improve code commentary
- Add the ability to run with command-line arguments
- Add a Bayer matrix generator
- Add the ability to work with multiple images, videos, and animated gifs (encode videos as gifs?)
- Add an optimized color palette generator
- Add GUI examples

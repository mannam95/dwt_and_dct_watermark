# Combined DWT-DCT Digital Image Watermarking

* This is the un-official implementation of the paper titled [Combined DWT-DCT Digital Image Watermarking](https://www.researchgate.net/publication/26621646_Combined_DWT-DCT_digital_image_watermarking) by Ali Al-Haj.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites

* How to setup Python environment
* Knowledge in signal processing
    * Discrete Cosine Transform(DCT),
    * Discrete Wavelet Transform(DWT),
    * Discrete Fourier Transform(DFT),
    * Singular Value Decomposition(SVD)
* How watermarking algorithms work?.

## Installing

* Clone the repository or download and unzip it.    
* Install the packages mentioned in `env.yml`
   ```
    #Do this in the project folder console.
    conda env create -f env.yml
  ```

## Usage
 * Watermark Embedding
   - `python main.py --emb --wat_dir_path="watermark-image" --emb_dir_path="images-directory" --save_emb_dir_path="save-directory"`
 * Watermark Extraction
   - `python main.py --ext --ext_dir_path="embeded-images-directory" --save_ext_dir_path="extracted-images-directory"`
* Apart from the above options, onw can check additional options by running
   - `python main.py --help`


## Code structure
- Most of the files are self-understood by name.
- Every function has the documentation.
- The documentation is followed by `docstring` pattern

## Pull Request
- You are always welcome to contribute to this repository by sending a [pull request](https://help.github.com/articles/about-pull-requests/).
- Please also add the documentation for the implementations/corrections.

## Citation
If you use this code for your research, please cite the paper, as this code is based on: <a href="https://www.researchgate.net/publication/26621646_Combined_DWT-DCT_digital_image_watermarking">Combined DWT-DCT Digital Image Watermarking</a>:


```
@article{alhajali,
author = {Al-Haj, Ali},
year = {2007},
month = {09},
pages = {},
title = {Combined DWT-DCT digital image watermarking},
volume = {3(9)},
journal = {Journal of Computer Science},
doi = {10.3844/jcssp.2007.740.746}
}
```
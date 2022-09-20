# Combined DWT-DCT Digital Image Watermarking

* This is the un-official implementation.


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
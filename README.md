# NeoPolyp Segmentation <a name="neopolyp-segmentation"></a>

## Table of Contents
* [NeoPolyp Segmentation](#neopolyp-segmentation)
	* [About](#about)
	* [Usage](#usage)


## About <a name="about"></a>

This package contains my submission to [BKAI-IGH NeoPolyp competition](https://www.kaggle.com/c/bkai-igh-neopolyp/overview) on Kaggle.


## Usage <a name="usage"></a>
To infer an image, follow these steps:

1. Clone the repository:\
   ```git clone https://github.com/ankhanhtran02/NeoPolyp-Segmentation.git```
2. Navigate to the project directory:\
   ```cd NeoPolyp-Segmentation```
3. Download the model at [this link](https://drive.google.com/file/d/1bRVc1ANpCVF4XSimFy3Gf-W8kgunfFm4/view?usp=sharing) and add it to the "model" directory.
4. Infer an image:\
   ```python3 infer.py --image_path image.jpeg```

The output will be saved as "prediction.png" in your working directory.

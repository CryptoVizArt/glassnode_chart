# Glassnode Watermark Plotting

This repository contains code to generate plots with watermarks using two popular plotting libraries in Python: Matplotlib and Plotly.

## Files

There are two Jupyter notebooks:

1. `glassnode_watermark_plot_matplotlib.ipynb`: This notebook includes code to generate a line plot with a watermark using Matplotlib. It also includes functions to customize the plot's appearance and apply a watermark with specified position. The watermark is applied using the Python Imaging Library (PIL).

2. `glassnode_watermark_plot_plotly.ipynb`: This notebook includes code to generate a line plot with a watermark using Plotly. It includes a function to add a watermark to the plot and set its position, size, and transparency. The watermark is added using Plotly's built-in image handling.

## Usage

To use these notebooks, simply run each cell from top to bottom. You'll need to have the required packages installed, including Matplotlib, Plotly, and PIL. You can install these with pip:

```bash
pip install matplotlib plotly pillow
```

## Examples
Both notebooks include an example where a line plot is generated from a series of random data points. A watermark is then applied to the plot.

In glassnode_watermark_plot_matplotlib.ipynb, the plot is saved as a .png file. In glassnode_watermark_plot_plotly.ipynb, the plot is displayed inline in the Jupyter notebook.

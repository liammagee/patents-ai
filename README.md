# patents-ai

Code for analysing scientific papers in PDF format (e.g. downloaded from arXiv.org).

All meaningful code is in the Jupyter notebook, *analysis.ipynb*. 

To launch, first install dependencies, then run:

    jupyter notebook



## Installation

To install, setting up a conda environment first is recommended. 

To do so:

    conda create --name patents-ai python=3.9
    
Then activate the environment:

    conda activate patents-ai

Then install dependencies, as follows:

    conda install pytorch torchvision torchaudio -c pytorch
    pip install -r requirements.txt

Once the dependencies are installed, run Jupyter:

    jupyter notebook

And navigate to the *analysis.ipynb*.


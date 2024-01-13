This folder contains all code, notebooks, scripts and input/output files used during the course of the Project by Team 32. 

Description:
1. input - This contains the scripts we used to pull the data using the Spotify API.
2. outputs - This folder contains the actual output files containing the predicted songs and acoustic features, that is used by the visualization code.
3. ML Model - This folder contains the Jupyter Notebook which splits the data into regions and trains the model, running the final predictions. We have used solely python and scikit learn libraries for this project. 
4. Visualization Code - This folder contains all the d3 code needed for visualization.
5. lib - This folder contains the d3 libraries used for the visualization.


Installation:
1. DATASET - For accessing the spotify API, you can follow the setup in the spotify api documentation (https://developer.spotify.com/documentation/web-api). Use client id and client secret from the setup to update spotify_pull.py and then run the 2 scripts spotify_pull.py and spotify_merge.py in succession (usage: python spotify_pull.py). We also need to install pandas for the above scripts to work as expected - https://pandas.pydata.org/docs/getting_started/install.html.
2. PYTHON/JUPYTER NOTEBOOK - For the Modeling half of this project, one needs to install python 3.8.5 on the local machine. We have used this version, and the code may or may not work with older versions of python. For installation, follow - https://www.python.org/downloads/. We have also used jupyter notebook which can be installed using - https://jupyter.org/install. Python is also needed to run a local server for the visualization. 
3. D3 - We have included all the required files for D3 in this zip, and no further installation is needed.


Execution:
1. MODEL - For running the model, simply run `jupyter notebook` and run the cells in the notebook `Random_Forest.ipynb` in succession. 
2. VISUALIZATION - To run the visualization, open a command prompt and navigate to be inside of the "CODE" folder. Start a local server with Python here using "python -m http.server 8000". Navigate to "localhost:8000" in a web browser, click "Visualization Code", click "Team_32_Visualization.html", and the user will be able to interact with our visualization.

##########################################################################################
################################## ReadME ###############################################
#Instructions for executing the SEIRHD spatial mobility model

1) Make sure all the required code files are in the current working directory
	This includes the files 'covid_19_numbers.py', 'origin-destination-matrix.ipynb' and 'Spatio_Temporal_SEIR_Modelling_beta_T_Final.ipynb'

2) Make sure you have installed all the required libraries in your new conda environment or in Google Colab (Colab module installations are automatic
	and will be done by the notebook

3) Make sure all the required datasets are in the 'Important Data' folder. I have packaged all required datasets with this zip file. However, GPW v4 dataset the TfL NUMBAT2020 datasets are too big to be included in the zip file. If you need this data, please feel free to get it from my Google Drive folder - "https://drive.google.com/drive/folders/1ImWnFODK3ZHQLqhdNhbn2QjNCGHFn5Qb?usp=drive_link". GPW v4 data is also available here - "https://sedac.ciesin.columbia.edu/data/collection/gpw-v4" You can download the dataset by creating a user account in this website. 
	NUMBAT2020 dataset is available here - "http://crowding.data.tfl.gov.uk/" . No user account required.
	Uber Mobility dataset can be downloaded from here - "https://movement.uber.com/explore/london/mobility-heatmap/query?lat.=51.51262&lng.=-0.1658002&z.=12&lang=en-GB"
	Please make sure all the datasets are inside the "Important Data" folder in the working directory when running the notebooks.

4) The descartes installation has a bug which has not been patched yet. This was manually done by me in my anaconda environment to make the code work.
	If you are using Google Colab, I have added in the code to automatically find the file and fix the error. I recommend using Google Colab for executing the code.
	Please comment out any irrelavant code if you are running on your local anaconda environment.

5) The 'origin-destination-matrix.ipynb' notebook contains an API key that has access to the Google Maps Geocoding API. For now, it will connect to my Google cloud account
	to pull data. However, API calls are chargeable after a certain quota is crossed. Therefore, I will be decommissionining this API key at the end of the course when
	the results are published. Till then, the code will work and it should run fine.






Thank you! I am proud of what I have accomplished with this project. 
I have covered the pre-requisite instructions. I hope you will face no issues executing the code!.
Thanks again!
# team4
Authors: Richard Ky, Amelia Jobe, Akshay Dhamsania, and Sandra Luo
Mentors: Edoardo Serra, Sumit Purohit

# Naval Vessels

## MMSIs of Blacklisted Vessels in AIS dataset
Putting them here cause I don't know where else to:
- 2021
    - 319133800
    - 248233000
    - 374811000
    - 574004860
- 2022
    - 319133800
    - 477237100

## Git ignore files
AISVesselTracks2022 and 2021 are not included because they're each like 10 gigs, so if you want to use that data you have to upload it yourself. Download it [here](https://marinecadastre.gov/ais/).

## Files

<!-- Feel free to rename any of these files, I suck at naming things -->

[EDA.ipynb](/EDA.ipynb)
Google colab for exploratory data analysis of 12/31/2022 AIS tracking data

[MMSI.csv](/MMSI.csv)
Is the list of MMSIs for the blacklisted vessels from the SDN dataset

[477237100.csv](/output/477237100.csv)
Is the trackline data on one of the blacklisted vessels (not sure how to process or interpret it)

[output2021.csv](/output2021.csv)
Is the list of MMSIs from the entirety of the 2021 dataset

[output2022.csv](/output2022.csv)
Is the list of MMSIs from the entirety of the 2022 dataset

[compare.py](/compare.py)
Python file for comparing SDN to AIS dataset

[2022.py](/2022.py)
(formerly test.py) Exploring the 2022 track dataset

[2021.py](/2021.py)
(formerly test1.py) Exploring the 2021 track dataset

The test markdown files are just the results of exploring the track dataset

Overview

This project analyzes the forests dataset which includes weather and fire risk variables for locations in Algerian forests from two regions: Bejaia (northeast Algeria) and Sidi Bel-abbes (northwest Algeria). By leveraging data visualization and multiple linear regression models, this analysis explores the relationships among various environmental factors and fire risk.

Dataset

The dataset includes the following variables:

temp: Maximum temperature in degrees Celsius.
humid: Relative humidity as a percentage.
region: Indicates location in either Bejaia or Sidi Bel-abbes.
fire: Whether a fire occurred (True) or didn’t (False).
FFMC: Fine Fuel Moisture Code – a measure of forest litter fuel moisture.
ISI: Initial Spread Index – estimates the potential spread of a fire.
BUI: Buildup Index – estimates the potential heat release during a fire.
FWI: Fire Weather Index – a comprehensive measure of fire intensity potential.
The dataset is sourced from the study by Faroudja ABID et al., "Predicting Forest Fire in Algeria using Data Mining Techniques: Case Study of the Decision Tree Algorithm," presented at the AI2SD 2019 conference in Marrakech, Morocco.

Project Structure

forestfirescript.py: Contains the main analysis code.
forests.csv: Sample data file used for the analysis.
README.md: This file.
requirements.txt: Lists Python dependencies.

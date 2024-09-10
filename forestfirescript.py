#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

#load data
forests = pd.read_csv('forests.csv')

#check multicollinearity with a heatmap
corr_grid = forests.corr()
sns.heatmap(corr_grid, xticklabels=corr_grid.columns, yticklabels=corr_grid.columns, annot=True)
plt.show()
plt.clf()

#plot humidity vs temperature
sns.lmplot(x='temp', y='humid', hue='region', data=forests, fit_reg=False)
plt.show()
plt.clf()

#model predicting humidity
modelH = sm.OLS.from_formula('humid ~ temp + region', data=forests).fit()
print(modelH.params)

#plot regression lines
sns.lmplot(x='temp', y='humid', hue='region', data=forests, fit_reg=False)
plt.plot(forests.temp, modelH.params[0] + modelH.params[1] * 0 + modelH.params[2] * forests.temp, color='blue', linewidth=5, label='Bejaia')
plt.plot(forests.temp, modelH.params[0] + modelH.params[1] * 1 + modelH.params[2] * forests.temp, color='orange', linewidth=5, label='Sidi Bel-abbes')
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs temperature
sns.lmplot(x='temp', y='FFMC', hue='fire', data=forests, fit_reg=False)
plt.show()
plt.clf()

#model predicting FFMC with interaction
modelF = sm.OLS.from_formula('FFMC ~ temp + fire + temp:fire', data=forests).fit()
print(modelF.params)

#plot regression lines
sns.lmplot(x='temp', y='FFMC', hue='fire', data=forests, fit_reg=False)
plt.plot(forests.temp, modelF.params[0] + modelF.params[1] * 0 + modelF.params[2] * forests.temp + modelF.params[3] * forests.temp * 0, color='blue', linewidth=5, label='No Fire')
plt.plot(forests.temp, modelF.params[0] + modelF.params[1] * 1 + modelF.params[2] * forests.temp + modelF.params[3] * forests.temp * 1, color='orange', linewidth=5, label='Fire')
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs humid
sns.lmplot(x='humid', y='FFMC', data=forests, fit_reg=False)
plt.show()
plt.clf()

#polynomial model predicting FFMC
modelP = sm.OLS.from_formula('FFMC ~ humid + np.power(humid, 2)', data=forests).fit()
print(modelP.params)

#multiple variables to predict FFMC
modelFFMC = sm.OLS.from_formula('FFMC ~ temp + rain + wind + humid', data=forests).fit()
print(modelFFMC.params)

#predict FWI from ISI and BUI
modelFWI = sm.OLS.from_formula('FWI ~ ISI + BUI', data=forests).fit()
print(modelFWI.params)

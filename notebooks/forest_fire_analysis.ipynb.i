{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Forest Fire Analysis\n",
    "\n",
    "This notebook provides an interactive analysis of forest fire data, complementing the automated pipeline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load and Explore Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load the data\n",
    "df = pd.read_csv('../results/preprocessed_data.csv')\n",
    "print(df.head())\n",
    "print(df.info())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Visualize Relationships"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Correlation heatmap\n",
    "plt.figure(figsize=(12, 10))\n",
    "sns.heatmap(df.corr(), annot=True, cmap='coolwarm')\n",
    "plt.title('Correlation Heatmap of Forest Fire Features')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pairplot of key features\n",
    "sns.pairplot(df, hue='fire', vars=['temp', 'RH', 'wind', 'rain'])\n",
    "plt.suptitle('Pairplot of Key Features', y=1.02)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Model Training and Evaluation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Prepare data for modeling\n",
    "X = df.drop(['fire', 'region'], axis=1)\n",
    "y = df['fire']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train Random Forest model\n",
    "rf_model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "rf_model.fit(X_train, y_train)\n",
    "\n",
    "# Evaluate the model\n",
    "y_pred = rf_model.predict(X_test)\n",
    "print(classification_report(y_test, y_pred))\n",
    "\n",
    "# Plot confusion matrix\n",
    "plt.figure(figsize=(8, 6))\n",
    "sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')\n",
    "plt.title('Confusion Matrix')\n",
    "plt.xlabel('Predicted')\n",
    "plt.ylabel('Actual')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Feature Importance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot feature importance\n",
    "feature_importance = pd.DataFrame({'feature': X.columns, 'importance': rf_model.feature_importances_})\n",
    "feature_importance = feature_importance.sort_values('importance', ascending=False)\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.barplot(x='importance', y='feature', data=feature_importance)\n",
    "plt.title('Feature Importance in Predicting Forest Fires')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
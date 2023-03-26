import pandas as pd
from sklearn.linear_model import LinearRegression

class LinearRegressionAnalysis:
    """
    A class to perform linear regression analysis on a given dataset.

    Attributes:
    -----------
    data : pandas DataFrame
        The input data for analysis

    Methods:
    --------
    load_data(filename)
        Loads the data from the given file

    perform_analysis(feature_cols, target_col)
        Performs linear regression analysis on the data using the given
        feature columns and target column
    """
    def __init__(self):
        self.data = None

    def load_data(self, filename):
        """
        Loads the data from the given file.

        Parameters:
        -----------
        filename : str
            The name of the CSV file containing the data.

        Returns:
        --------
        None
        """
        self.data = pd.read_csv(filename)

    def perform_analysis(self, feature_cols, target_col):
        """
        Performs linear regression analysis on the data using the given
        feature columns and target column.

        Parameters:
        -----------
        feature_cols : list
            A list of strings representing the names of the columns to be used as
            the independent variables for regression analysis.

        target_col : str
            A string representing the name of the column to be used as the dependent
            variable for regression analysis.

        Returns:
        --------
        results : pandas DataFrame
            A DataFrame containing the regression results for each feature column.
        """
        results = pd.DataFrame(columns=[
            'Feature',
            'Intercept',
            'Coefficient',
            'R-squared']
        )

        for col in feature_cols:
            X = self.data[[col]]
            y = self.data[target_col]

            model = LinearRegression()
            model.fit(X, y)

            results = results.append({
                'Feature': col,
                'Intercept': model.intercept_,
                'Coefficient': model.coef_[0],
                'R-squared': model.score(X, y)
            }, ignore_index=True)

        return results

# Example usage
lr = LinearRegressionAnalysis()
lr.load_data('example.csv')
results = lr.perform_analysis(['Unit Cost', 'Quantity'], 'Revenue')
print(results)


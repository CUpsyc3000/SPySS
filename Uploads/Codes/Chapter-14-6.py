np.random.seed(42) # to make the random numbers replicable

df = pd.DataFrame({"x": [3, 5, 8, 10, 12],
                   "y": np.array([3, 5, 8, 10, 12]) * 1 + 1 + np.random.randn(5) * 1})

ols_result=smf.ols("y ~ x", data=df).fit()

mse = np.mean(ols_result.resid**2)
rmse = np.sqrt(mse)
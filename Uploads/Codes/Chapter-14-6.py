np.random.seed(42) # to make the random numbers replicable

df = pd.DataFrame({"x": [3, 5, 8, 10, 12],
                   "y": 1 + 1 * np.array([3, 5, 8, 10, 12]) + np.random.randn(5) * 1})

sl.code(sm.OLS(df["x"],df["y"]).fit().summary().as_text())
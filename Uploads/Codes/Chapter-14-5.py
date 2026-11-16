df = pd.DataFrame({"x": [3, 5, 8, 10, 12],
                   "y": np.array([3, 5, 8, 10, 12]) * 1 + 1 + np.random.randn(5) * 1})
result = pg.linear_regression(df[['x']], df['y'])
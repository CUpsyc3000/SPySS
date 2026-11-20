
df = pd.DataFrame({
    "studyTime": [0.67, 1.00, 1.67, 2.00, 2.00, 2.67, 3.33, 4.00],
    "grade": [77, 85, 84, 80, 90, 77, 98, 93],
    "intercept": [1,1,1,1,1,1,1,1] #1
})

#df["intercept"] = 1


# Y vector
Y = df["grade"].to_numpy().reshape(-1, 1)

# create 8 x 2 matrix of zeros
X = np.zeros((8, 2))

# first column = studyTime
X[:, 0] = df["studyTime"]

# second column = constant 1
X[:, 1] = 1

# beta hat
beta_hat = np.linalg.pinv(X) @ Y

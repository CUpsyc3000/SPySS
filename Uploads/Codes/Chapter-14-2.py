
df = pd.DataFrame({
    "studyTime": [0.67, 1.00, 1.67, 2.00, 2.00, 2.67, 3.33, 4.00],
    "grade": [77, 85, 84, 80, 90, 77, 98, 93]
})

result= pg.linear_regression(df["studyTime"], df["grade"])
sns.regplot(data=df, x="studyTime", y="grade", scatter_kws={"color": "red"}, line_kws={"color": "blue"})

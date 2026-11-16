df = pd.DataFrame({
    "study_time": [0.67, 1.00, 1.67, 2.00, 2.00, 2.67, 3.33, 4.00],
    "grade": [77, 85, 84, 80, 90, 77, 98, 93]
})

result=pg.corr(df["study_time"],df["grade"])
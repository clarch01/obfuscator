def redactor(df, fields):
    def censor(x):
        return "xxx"
    for field in fields:
        new_column = df.apply(censor, axis=1)
        df[field] = new_column
    return df
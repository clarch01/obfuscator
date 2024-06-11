def redactor(df, fields):
    def censor(x):
        return "xxx"
    columns = list(df)
    for field in fields:
        if field not in columns:
            raise Exception(f"The column '{field}' does not exist")
        new_column = df.apply(censor, axis=1)
        df[field] = new_column
    return df

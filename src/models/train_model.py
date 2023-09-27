from sklearn.model_selection import train_test_split
def sep_X_de_y(df_num):
    X = df_num.drop('price',axis=1)
    y = df_num['price'].copy()
    return X,y


def train_val_test_split(df_num):
    train_set, df_test_val = train_test_split(df_num, test_size=0.4, train_size=None, random_state=42, shuffle=True, stratify=None)
    test_set, val_set = train_test_split (df_test_val, test_size = 0.5, random_state = 42, shuffle = False, stratify = None)
    return train_set, val_set, test_set
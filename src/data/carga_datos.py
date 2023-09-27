def carga_datos(ruta_csv):
    import pandas as pd
    df = pd.read_csv(ruta_csv)
    return df

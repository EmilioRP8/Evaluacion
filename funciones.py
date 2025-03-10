import pandas as pd
def cargar_dataset(archivo):
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import json as js
    import numpy as np
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df= pd.read_excel(archivo)
        return (df)
    else:
            raise ValueError(f"“Este formato no esta soportado para esta función: .formato”")

def limpiar_valores_nulos(df):
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import json as js
    import numpy as np
        # Reemplaza los valores nulos según las reglas dadas
    for i, col in enumerate(df.columns):
        if df[col].dtype in ['int64', 'float64']:
            if i % 2 == 0:
                df[col] = df[col].fillna(df[col].mean())  
            else:
                df[col] = df[col].fillna(99)  
        else:
            df[col] = df[col].fillna("Este_es_un_valor_nulo")  
    return df

def identificar_valores_nulos(df):
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import json as js
    import numpy as np
        # Muestra cuántos valores nulos hay en cada columna y en total
    return df.isnull().sum(), df.isnull().sum().sum()

def limpiar_valores_atipicos(df):
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import json as js
    import numpy as np
        # Reemplaza valores atípicos con el método del rango intercuartílico
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df[col] = df[col].mask((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)), df[col].median())
    return df
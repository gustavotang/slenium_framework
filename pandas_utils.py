import pandas as pd

def ler_csv(caminho, sep=',', encoding='utf-8'):
    """Lê um arquivo CSV e retorna um DataFrame."""
    return pd.read_csv(caminho, sep=sep, encoding=encoding)

def ler_excel(caminho, sheet_name=0):
    """Lê um arquivo Excel e retorna um DataFrame."""
    return pd.read_excel(caminho, sheet_name=sheet_name)

def salvar_csv(df, caminho, sep=',', index=False, encoding='utf-8'):
    """Salva um DataFrame em um arquivo CSV."""
    df.to_csv(caminho, sep=sep, index=index, encoding=encoding)

def salvar_excel(df, caminho, sheet_name='Sheet1', index=False):
    """Salva um DataFrame em um arquivo Excel."""
    df.to_excel(caminho, sheet_name=sheet_name, index=index)

def editar_celula(df, linha, coluna, valor):
    """Edita o valor de uma célula específica."""
    df.at[linha, coluna] = valor

def filtrar_linhas(df, coluna, valor):
    """Filtra linhas onde a coluna tem o valor especificado."""
    return df[df[coluna] == valor]

def adicionar_coluna(df, nome_coluna, valores):
    """Adiciona uma nova coluna ao DataFrame."""
    df[nome_coluna] = valores

def remover_coluna(df, nome_coluna):
    """Remove uma coluna do DataFrame."""
    return df.drop(columns=[nome_coluna])

def agrupar_por(df, coluna, funcao_agregacao):
    """Agrupa o DataFrame por uma coluna e aplica uma função de agregação."""
    return df.groupby(coluna).agg(funcao_agregacao)

def ordenar_por(df, coluna, crescente=True):
    """Ordena o DataFrame por uma coluna."""
    return df.sort_values(by=coluna, ascending=crescente)

def juntar_dataframes(df1, df2, on, como='inner'):
    """Realiza o merge (junção) de dois DataFrames."""
    return pd.merge(df1, df2, on=on, how=como)

def remover_linhas_nulas(df):
    """Remove linhas com valores nulos."""
    return df.dropna()

def preencher_nulos(df, valor):
    """Preenche valores nulos com um valor específico."""
    return df.fillna(valor)
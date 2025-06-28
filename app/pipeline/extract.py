import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função que lê dados de
    uma pasta de arquivos 'data/input' e consolida em um arquivo .xlsx

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(data_frame_list)
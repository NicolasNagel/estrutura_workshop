from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> List[pd.DataFrame]:
    """
    Função para transformar uma lista de DataFrame em um único DataFrame
    """
    return pd.concat(data_frame_list, ignore_index=True)
import pandas as pd
import logging

def logger_basic_conf(logger: logging.Logger | None = None) -> logging.Logger:
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        if logger.hasHandlers():
            logger.handlers.clear()
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def drop_cols_by_null_percent(
    df: pd.DataFrame,
    null_limit: float = 0.5,
    safe_col_prefix: str = "SAFE_",
    logger: logging.Logger | None = None,
):
    logger = logger_basic_conf(logger)

    for col in df.columns:
        na_count = df[col].isna().sum()
        total_count = len(df[col])

        null_percent = na_count / total_count

        if null_percent >= null_limit and not col.startswith(safe_col_prefix):
            df = df.drop(columns=col)
            logger.warning(
                "%s %.2f%% nulos >= limite %.2f%% REPROVADO",
                col,
                null_percent * 100,
                null_limit * 100,
            )
            continue

        logger.info(
            "%s %.2f%% nulos < limite %.2f%%: APROVADO",
            col,
            null_percent * 100,
            null_limit * 100,
        )

    return df

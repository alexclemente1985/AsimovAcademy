import time
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

# Permite conversão do dataset gigantesco em csv para algo em torno de 1/8 do tamanho e 20x mais rápido no .parquet
def parquet():
    datasets = Path.joinpath(Path.cwd(), 'datasets')
    # df = pd.read_csv(Path.joinpath(datasets, 'petr4_ticks.csv', sep=';', decimal=',')

    #Writer - convertendo os dados obtidos em .csv em .parquet
    t0 = time.time()

    # table = pa.Table.from_pandas(df)
    # writer = pq.ParquetWriter(petr4.parquet, table.schema)
    # writer.write_table(table)
    # writer.close()
    t1 = time.time()
    print(f"Tempo para escrita com parquet: {t1 - t0}")

    # Reader

    #df_pq = pq.ParquetFile("petr4.parquet").read().to_pandas()

parquet()
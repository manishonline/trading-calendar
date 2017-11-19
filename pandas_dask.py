import dask.dataframe as dd
import time

def parse_file(filename):
    df = dd.read_csv(filename)
    print(df.npartitions)
    print(df.columns)
    print(df.dtypes)
    t1 = time.time()
    df = df.persist()
    print(str(t1))
    size = df.size.compute()
    print('filesize='+str(size))
    t2 = time.time()
    print(str(t2))
    print('Calculating size took '+str(t2-t1)+' seconds')

def start_parse():
    parse_file(r"C:\Users\mkumar\Downloads\yellow_tripdata_2017-01.csv")

if __name__ == '__main__':
    start_parse();



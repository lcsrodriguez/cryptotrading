# Pre-processed datasets


The pre-processed financial datasets, which are outputs of the `notebooks/processing.ipyb` Jupyter notebook, have been stored under three different formats:
- **`csv/`**: for general tasks
- **`parquet/`**: compressed format
- **`feather/`**: compressed format **(Not implemented)**


To check the folder size of each solution, run
```
du -sh assets/<extension>
```
where `<extension>` is either: `csv`, `parquet` or `feather`


## References:

1. **CSV**: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
2. **Apache Parquet**: https://arrow.apache.org/docs/python/parquet.html
3. **Apache Feather**: https://arrow.apache.org/docs/python/feather.html

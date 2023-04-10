# Pre-processed datasets

The pre-processed financial datasets, which are outputs of the `notebooks/processing.ipyb` Jupyter notebook, have been stored under three different formats:
- **`csv/`**: for general tasks
- **`parquet/`**: compressed format
- **`feather/`**: compressed format


To check the folder size of each solution, run
```
du -sh assets/<extension>
```
where `<extension>` is either: `csv`, `parquet` or `feather`
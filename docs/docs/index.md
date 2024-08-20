# ticker_analysis documentation!

## Description

A dasbhoard with alerts for stock investment and analysis

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `strg4tickeranalizer_1724019028656/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `strg4tickeranalizer_1724019028656/data/` to `data/`.



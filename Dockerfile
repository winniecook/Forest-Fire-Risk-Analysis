FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "forest-fire-env", "/bin/bash", "-c"]

COPY . .

CMD ["conda", "run", "-n", "forest-fire-env", "python", "scripts/01_data_preprocessing.py"]
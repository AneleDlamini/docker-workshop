FROM python:3.13.11
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
# copy dependencies 
COPY  pyproject.toml .python-version uv.lock ./

# sync dependencies to docker
RUN uv sync --locked --no-install-project

RUN pip install pandas pyarrow

COPY ingest-data.py .

ENTRYPOINT ["python", "ingest-data.py"]
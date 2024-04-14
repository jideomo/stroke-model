FROM python:3.11-slim-bookworm 
ENV PYTHONUNBUFFERED=TRUE 
RUN pip --no-cache-dir install pipenv
WORKDIR /app 
COPY ["prediction-service/Pipfile", "prediction-service/Pipfile.lock", "./"] 
RUN pipenv install --deploy --system && \
    rm -rf /root/.cache
COPY ["prediction-service/model-service.py", "prediction-service/stroke-model-1.bin", "./"]
EXPOSE 8443
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8443", "model-service:app"]
FROM python:3.12-slim

WORKDIR ${LAMBDA_TASK_ROOT}

#requiriments.txt
COPY requirements.txt ./


RUN pip install -r requirements.txt --upgrade

EXPOSE 8000

COPY src ${LAMBDA_TASK_ROOT}/src
COPY src/promptior_presentation.pdf ${LAMBDA_TASK_ROOT}/src/

ENV PYTHONPATH="${LAMBDA_TASK_ROOT}/src"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
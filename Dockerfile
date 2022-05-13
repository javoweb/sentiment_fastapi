FROM pytorch/pytorch:latest
RUN pip install -U pip --no-cache-dir
WORKDIR /workspaces/midterm
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY main.py main.py
EXPOSE 8000
CMD ["uvicorn","--host", "0.0.0.0", "--port", "8000", "main:app" ]
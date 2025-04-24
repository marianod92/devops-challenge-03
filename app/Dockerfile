FROM python:3.10.5

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"]
# CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
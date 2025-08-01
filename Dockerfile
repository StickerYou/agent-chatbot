# Dockerfile

FROM syqaaichatbotregistry.azurecr.io/autogen-chatbot-base:1.6

WORKDIR /app

COPY . .

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "main_server:app", "--host", "0.0.0.0", "--port", "8000"]

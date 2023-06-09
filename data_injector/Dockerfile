FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY data_injector.py .

RUN pip install --no-cache-dir -r requirements.txt

COPY cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN touch /var/log/cron.log

EXPOSE 80

CMD cron && tail -f /var/log/cron.log
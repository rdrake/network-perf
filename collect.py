from celery import Celery

app = Celery("collect", include=["tasks"])
app.config_from_object("celery")

if __name__ == "__main__":
    app.start()

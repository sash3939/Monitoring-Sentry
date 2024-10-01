import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask

# Инициализация Sentry
sentry_sdk.init(
    dsn="https://053ed31c47cae94db7b6379755ea7fcd@o4508043825184768.ingest.de.sentry.io/4508048572743760",  # Замените на ваш DSN из Sentry
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0  # Отправка всех событий
)

app = Flask(__name__)

@app.route('/error')
def trigger_error():
    division_by_zero = 1 / 0  # Создаем ошибку для тестирования
    return "This will never be reached"

@app.route('/test-event')
def test_event():
    sentry_sdk.capture_message("This is a test event")  # Отправка тестового события
    return "Test event sent!"

if __name__ == "__main__":
    app.run(debug=True)

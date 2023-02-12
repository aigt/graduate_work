from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/api/v1/add_notification", methods=["POST"])
def notification() -> Response:
    """Ендпоинт имитация сервиса уведомлений.

    Returns:
        response(tuple): response
    """
    body = request.json
    request_in_notification = {
        "meta": {"urgency": "immediate", "scale": "individual", "periodic": False},
        "type": "info",
        "fields": {"user_id": "ae24e74b-dc2d-407b-a4b3-a60e445d7a98"},
    }
    if body == request_in_notification:
        return {"message": "notification added"}, 200
    return {"message": "fail, notification don't added"}, 400


app.run()

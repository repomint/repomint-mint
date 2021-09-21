from json import loads
from flask import jsonify, make_response, request

from . import bp


@bp.route("/mint", methods=["POST"])
def mint():
    body = loads(request.data)

    # TODO: without auth for hack
    try:
        if not request.headers.get("Authorization"):
            raise ValueError("Unauthorized request")

        return make_response(
            jsonify(loads(f"TODO something but here's {body}")), 200
        )

    except Exception as e:

        return make_response(jsonify(e), 500)

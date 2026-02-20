from flask import Blueprint, jsonify
bp = Blueprint("goals", __name__)
@bp.get("/milestones")
def get_milestones():
    return jsonify({"milestones": [], "message": "Goals feature skeleton ready"})

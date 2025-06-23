from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date.isoformat(), "number": e.number} for e in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    return jsonify({
        "id": e.id,
        "date": e.date.isoformat(),
        "number": e.number,
        "appearances": [{"id": a.id, "rating": a.rating, "guest_id": a.guest_id} for a in appearances]
    })

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({"message": "Episode deleted"})

from flask import Blueprint, request, jsonify
from app.models.leave_model import Leave
from app.utils.decorators import token_required, employer_required

leave_bp = Blueprint('leaves', __name__)

@leave_bp.route('/', methods=['POST'])
@token_required
def apply_leave(current_user):
    data = request.get_json()
    required_fields = ['leave_type', 'start_date', 'end_date', 'reason']
    if not data or not all(k in data for k in required_fields):
        return jsonify({"message": "Missing required fields"}), 400

    Leave.create_leave(
        current_user['_id'],
        data['leave_type'],
        data['start_date'],
        data['end_date'],
        data['reason']
    )
    return jsonify({"message": "Leave application submitted successfully"}), 201

@leave_bp.route('/my_leaves', methods=['GET'])
@token_required
def get_my_leaves(current_user):
    leaves = Leave.get_leaves_by_employee(current_user['_id'])
    return jsonify(leaves), 200

@leave_bp.route('/all', methods=['GET'])
@token_required
@employer_required
def get_all_leaves(current_user):
    leaves = Leave.get_all_leaves()
    return jsonify(leaves), 200

@leave_bp.route('/<leave_id>/status', methods=['PUT'])
@token_required
@employer_required
def update_leave_status(current_user, leave_id):
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"message": "Missing status field"}), 400
        
    status = data['status']
    if status not in ['Approved', 'Rejected']:
        return jsonify({"message": "Invalid status"}), 400

    result = Leave.update_leave_status(leave_id, status)
    if result.modified_count == 0:
        return jsonify({"message": "Leave not found or status unchanged"}), 404

    return jsonify({"message": f"Leave {status.lower()} successfully"}), 200

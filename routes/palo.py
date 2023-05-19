from flask import Blueprint
from controllers.palo import test_fw_policy

palo_blueprint = Blueprint('blueprint', __name__)

palo_blueprint.route('/test-fw-policy', methods=['POST'])(test_fw_policy)

from flask import Blueprint, request, jsonify
import json
from controller.main_controller import get_all_teams,get_team_member,get_team,create_team,delete_team_member,add_team_member,update_team,delete_team,delete_all_team_members

teams = Blueprint('teams', __name__, url_prefix='/teams')


@teams.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@teams.route('/', methods=['GET', 'POST'])
def teams_view():
    if request.method == 'GET':  # get all teams
        all_teams = get_all_teams()

        response_body = [t.to_dict() for t in all_teams]
        return jsonify(response_body), 200

    if request.method == 'POST':  # create a new team
        # mention validation issues
        print("DEBUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUG")
        print(request.json)
        body = json.loads(request.json)
        print(body.keys)
        created = create_team(body)
        return jsonify(created), 201


@teams.route('/<string:team_uuid>', methods=['GET', 'PUT', 'DELETE'])
def single_team_view(team_uuid):
    if request.method == 'GET':  # get the team
        team = get_team(team_uuid)
        if team is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        response_body = team.to_dict()
        return jsonify(response_body), 200

    if request.method == 'PUT':  # update the team
        body = json.loads(request.json)
       
        updated = update_team(body)
        if updated is None:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        return jsonify(updated), 200

    if request.method == 'DELETE':  # remove the team
        success = delete_team(team_uuid)

        if not success:
            return jsonify({'error': 'team with unique id {} not found'.format(team_uuid)}), 404

        return jsonify({}), 204

    
@teams.route('/user/<int:team_member_id>', methods=['DELETE','POST','PUT','GET'])    
def single_user_view(team_member_id):
    
    if request.method == 'DELETE' :   #remove one member

        deleted = delete_team_member(team_member_id)
        if not deleted:
            return jsonify({'error': 'user with unique id {} not found'.format(team_member_id)}), 404

        return jsonify({'status':'success! user with id {} found and deleted '.format(str(team_member_id))}), 204
    
    if request.method == 'POST':  #add new member inot the team
        body = json.loads(request.json)
        created = add_team_member(body)
        return jsonify(created), 201
    
    if request.method == 'GET':   #get one specific member data
        userData = get_team_member(team_member_id)

        response_body = [t.to_dict() for t in userData]
        return jsonify(response_body), 200
    
    if request.method == 'PUT': #change user data by its ID
        body = json.loads(request.json)
        userNewData = update_team_member(body)#ID and changable things requiered!
         
        response_body = [t.to_dict() for t in userData]
        if userData == None:
            return jsonify(response_body), 204
        return jsonify(response_body), 200

        

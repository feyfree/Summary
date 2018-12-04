import os

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

#定义全局变量
channel_list = {"general": []}
present_channel = {"initial": "general"}

@app.route("/", methods=["POST", "GET"])
def index():
	if request.method == "GET":
		return render_template("index.html", channel_list=channel_list)
	if request.method == "POST":
		channel = request.form.get("channel_name")
		user = request.form.get("username")

		# 添加新的频道
		if channel and (channel not in channel_list):
			channel_list[channel] = []
			return jsonify({"Success": True})
		# 切换频道
		elif channel in channel_list:
			print(f"Switch to {channel}")
			present_channel[user] = channel
			channel_data = channel_list[present_channel[user]]
			return jsonify(channel_data)
		else:
			return jsonify({"Success": False})

@socketio.on("create channel")
def create_channel(new_channel):
	emit("new channel", new_channel, broadcast=True)

@socketio.on("send message")
def send_message(message_data):
	channel = message_data["current_channel"]
	channel_message_count = len(channel_list[channel])
	del message_data["current_channel"]
	channel_list[channel].append(message_data)
	message_data["delete_message"] = False
	if channel_message_count >= 100:
		del channel_list[channel][0]
		message_data["deleted_message"] = True
	emit("receive message", message_data, broadcast=True, room=channel)

@socketio.on("delete channel")
def delete_channel(message_data):
	channel = message_data["current_channel"]
	user = message_data["user"]
	present_channel[user] = "general"
	del message_data["current_channel"]
	del channel_list[channel]
	channel_list["general"].append(message_data)
	message_data = {"data": channel_list["general"], "deleted_channel": channel}
	emit("announce channel deletion", message_data, broadcast=True)

@socketio.on("leave")
def on_leave(room_to_leave):
	print("leaving room")
	emit("leave channel ack", room=room_to_leave)

@socketio.on("join")
def on_join(room_to_join):
	print("joining room")
	join_room(room_to_join)
	emit("join channel ack", room=room_to_join)

if __name__ == '__main__':
	socketio.run(app)
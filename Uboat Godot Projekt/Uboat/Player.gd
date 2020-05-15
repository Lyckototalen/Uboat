extends RigidBody2D

export var thrust_strength_sideways = 150
export var thrust_strength_upwards = 400
var thrust = Vector2.ZERO

onready var audio_stream_player = $AudioStreamPlayer

func _integrate_forces(_state):
	
	if Input.is_action_pressed("force_left") && Input.is_action_pressed("force_right"):		
		play_thrust_sfx()
		thrust = Vector2(0, -thrust_strength_upwards * 2)
	
	elif Input.is_action_pressed("force_left"):		
		play_thrust_sfx()
		thrust = Vector2(-thrust_strength_sideways, -thrust_strength_upwards)
		apply_torque_impulse(-200)
		
	elif Input.is_action_pressed("force_right"):		
		play_thrust_sfx()
		thrust = Vector2(thrust_strength_sideways, -thrust_strength_upwards)
		apply_torque_impulse(200)
		
	else:
		thrust = Vector2.ZERO	
		
	apply_thrust(thrust)

func apply_thrust(thrust):
	set_applied_force(thrust)
	if rotation_degrees <= -1 or rotation_degrees >= 1:
		apply_torque_impulse(-rotation_degrees * 10)		

func play_thrust_sfx():
	if !audio_stream_player.playing:
		audio_stream_player.play(0)
	elif audio_stream_player.get_playback_position() >= 3:
		audio_stream_player.play(0)
	elif audio_stream_player.get_playback_position() >= 1.6:
		audio_stream_player.play(1.2)

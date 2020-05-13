extends RigidBody2D


export var force_sideways = 200
export var force_upwards = 300

func _integrate_forces(_state):
	if Input.is_action_just_pressed("force_left"):
		apply_impulse(Vector2(10,0), Vector2(-force_sideways,-force_upwards))

	elif Input.is_action_just_pressed("force_right"):
		apply_impulse(Vector2(-10,0), Vector2(force_sideways,-force_upwards))

	if rotation_degrees <= -1 or rotation_degrees >= 1:
		apply_torque_impulse(-rotation_degrees * 10)

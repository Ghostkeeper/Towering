extends Node2D

var wave_interval = 100
var time_to_next_wave = wave_interval
var wave_nr = 0

onready var Robot = load("res://objects/Robot.tscn")

func _ready():
	print("Starting!")
	$WaveTimer.start()
	$WaveTimer.connect("timeout", self, "new_wave")

func new_wave():
	wave_nr += 1
	for i in range(0, wave_nr): #TODO: This is a hard-coded difficulty curve.
		var mob = Robot.instance()
		add_child(mob)
		mob.position = $SpawnLocation.position
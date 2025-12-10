"""
Audio effects module for the Audio Vocoder application.

This module contains all audio processing effects including:
- Robot effect (phase vocoder)
- Pitch shifting
- Speed adjustment  
- Echo/reverb effects

Provides modular effect classes that can be easily extended.
"""

from .base_effect import BaseEffect
from .robot_effect import RobotEffect
from .pitch_effect import PitchEffect
from .speed_effect import SpeedEffect
from .echo_effect import EchoEffect

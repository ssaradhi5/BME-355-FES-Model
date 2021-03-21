import matplotlib as plt





class FESModel:
  def __init__(self):
    # Model constants for an average subject (75kg - 1.75m)
    self.Tact = 0.01 # Activation constant time [sec]
    self.Tdeact = 0.04 # Relaxation constant time [sec]
    self.J = 0.0197 # Inertia of the foot around ankle [kg * m^2]
    self.d = 3.7 # Moment arm of TA w.r.t the ankle [cm]
    self.B = 0.82 # Viscosity parameters
    self.cF = 11.45 # COM location w.r.t the ankle [cm]
    self.mF = 1.0275 # Mass of the foot [kg]
    self.aV = 1.33 # First force-velocity parameter
    self.fv1 = 0.18 # Second force-velocity parameter
    self.fv2 = 0.023 # Third force-veloctiy parameter
    self.vMax = -0.9 # Maximal contraction speed (shortnening) [m/sec]
    self.FMax = 600 # Maximal isometric force [N]
    self.W = 0.56 # Shape parameter of f-fl
    self.lT = 22.3 # Constant tendon length [cm]
    self.lMT0 = 32.1 # Muscle-tendon length at rest [cm]
    self.a = [2.10, -0.08, -7.97, 0.19, -1.79] # Parameters of elastic torque T-Elastic




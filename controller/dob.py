class PDController:
    """
    PD Controller
    """

    def __init__(self, band_width: float, mass: float, torque_const: float, sampling_time: float):
        self.mass = mass
        self.torque_const = torque_const
        self.sampling_time = sampling_time
        self.k1 = self.band_width * self.band_width
        self.k2 = 2.0 * self.band_width
        self.previous_position = 0.0
        self.previous_current = 0.0

    def get_output(self, input_value: float):
        output_value = ((2.0 - self.band_width) * self.previous_output + self.proportional_gain * (
                2.0 * (input_value - self.previous_input) + self.band_width * self.sampling_time * (
                    input_value + self.previous_input)) + 2.0 * self.differential_gain * self.band_width * (
                                input_value - self.previous_input)) / (2.0 + self.band_width * self.sampling_time)

        self.previous_input = input_value
        self.previous_output = output_value
        return output_value

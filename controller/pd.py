class PDController:
    """
    PD Controller
    """

    def __init__(self, proportional_gain: float, differential_gain: float, band_width: float, sampling_time: float):
        self.proportional_gain = proportional_gain
        self.differential_gain = differential_gain
        self.band_width = band_width
        self.sampling_time = sampling_time
        self.previous_input = 0.0
        self.previous_output = 0.0

    def get_output(self, input_value: float):
        output_value = ((2.0 - self.band_width) * self.previous_output + self.proportional_gain * (
                2.0 * (input_value - self.previous_input) + self.band_width * self.sampling_time * (
                    input_value + self.previous_input)) + 2.0 * self.differential_gain * self.band_width * (
                                input_value - self.previous_input)) / (2.0 + self.band_width * self.sampling_time)

        self.previous_input = input_value
        self.previous_output = output_value
        return output_value

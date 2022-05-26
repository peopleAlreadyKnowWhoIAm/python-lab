from typing import Tuple

class BasicElement:
    """_summary_
    """
    def __init__(self, max_working_voltage: float, min_working_voltage: float) -> None:
        self.max_working_voltage = max_working_voltage
        self.min_working_voltage = min_working_voltage

    def __str__(self) -> str:
        return 'Something'

class Analog(BasicElement):
    """_summary_
    """
    def __init__(self,
                 accuracy: float, max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(max_working_voltage, min_working_voltage)
        self.accuracy = accuracy

    def __str__(self) -> str:
        return 'Something analog'

class Digit(BasicElement):
    """_summary_
    """
    def __init__(self, logic_one_min_voltage: float, logic_zero_max_voltage:float,
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(max_working_voltage, min_working_voltage)
        self.logic_one_min_voltage = logic_one_min_voltage
        self.logic_zero_max_level = logic_zero_max_voltage

    def __str__(self) -> str:
        return 'Something digit'

class Impulse(Analog):
    """_summary_
    """
    def __init__(self, max_frequency: int, accuracy: float,
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(accuracy, max_working_voltage, min_working_voltage)
        self.max_frequency = max_frequency

    def __str__(self) -> str:
        return 'Something impulse'


class OperationalAmplifier(Analog):
    """_summary_
    """
    def __init__(self, input_voltage: float, ampliefing_coef: float, accuracy: float,
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(accuracy, max_working_voltage, min_working_voltage)
        self.input_voltage = input_voltage
        self.ampliefing_coef = ampliefing_coef
        self.output_voltage = input_voltage * ampliefing_coef

    def __str__(self) -> str:
        return 'This is a operational ampliefier.'\
            f' Input {self.input_voltage}, output {self.output_voltage}'


class CurrentSource(Analog):
    """_summary_
    """
    def __init__(self, current:float, accuracy: float,
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(accuracy, max_working_voltage, min_working_voltage)
        self.current = current

    def __str__(self) -> str:
        return f"This is a current source. Output {self.current} amperes."

class VoltageSource(Analog):
    """_summary_
    """
    def __init__(self, voltage:float, accuracy: float,
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(accuracy, max_working_voltage, min_working_voltage)
        self.voltage = voltage
    
    def __str__(self) -> str:
        return f"This is a voltage source. Output {self.voltage} volts."


class BinaryToUnaryDecoder(Digit):
    """_summary_
    """
    def __init__(self, input_values: Tuple[bool], logic_one_min_voltage: float,
                 logic_zero_max_voltage: float, max_working_voltage: float,
                 min_working_voltage: float) -> None:
        super().__init__(logic_one_min_voltage, logic_zero_max_voltage,
                         max_working_voltage, min_working_voltage)
        self.input = input_values
        output = 0
        for index, value in list(zip(range(len(input_values)), input_values)):
            output += (2**index)*int(value)
        self.output = 2**input_values.count(True)

    def __str__(self) -> str:
        return f"This is a binnary-unary decoder. Input {self.input}. Output {self.output}."

class BinarySummator(Digit):
    """_summary_
    """
    def __init__(self, input_1: Tuple[bool], input_2: Tuple[bool],
                 logic_one_min_voltage: float, logic_zero_max_voltage: float, 
                 max_working_voltage: float, min_working_voltage: float) -> None:
        super().__init__(logic_one_min_voltage, logic_zero_max_voltage,
                         max_working_voltage, min_working_voltage)
        self.input_1 = input_1
        self.input_2 = input_2
        if len(input_1) != len(input_2):
            raise AttributeError('Length of inputs must be equals')
        output = []
        carry = False
        for a, b in zip(reversed(input_1), reversed(input_2)):
            if a and b:
                output.append(bool(carry))
                carry = True
            elif (a and not b) or (not a and b):
                output.append(bool(not carry))
            elif not a and not b:
                output.append(bool(carry))
                carry = False
        self.output = tuple(reversed(output))

    def __str__(self) -> str:
        return f"This is a binnary summator. Inputs {self.input_1} {self.input_2}."\
            f"Output {self.output}"

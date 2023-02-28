#class that implement look-up tables for the motors coordinates, translating from motor position to the real position of the motors
class MotorsCoordinates:
    def __init__(self, motors_dict):
        self.motors_dict = motors_dict
        self.motors_coordinates = dict()
        self.motors_coordinates['x'] = dict()
        self.motors_coordinates['y'] = dict()
        self.motors_coordinates['z'] = dict()
        self.motors_coordinates['x']['id'] = 1
        self.motors_coordinates['y']['id'] = 2
        self.motors_coordinates['z']['id'] = 3
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')
        self.motors_coordinates['x']['table'] = self.create_table('x')
        self.motors_coordinates['y']['table'] = self.create_table('y')
        self.motors_coordinates['z']['table'] = self.create_table('z')

    def create_table(self, axis):
        motor = self.motors_dict[self.motors_coordinates[axis]['id']]
        table = dict()
        for i in range(0, 100):
            table[motor.actual_pos] = i
            motor.move(1)
        return table
    
    def get_motor_position(self, axis, position):
        return self.motors_coordinates[axis]['table'][position]
    
    def get_motor_positions(self, x, y, z):
        return self.get_motor_position('x', x), self.get_motor_position('y', y), self.get_motor_position('z', z)
    
    def get_motor_positions_from_dict(self, positions_dict):
        return self.get_motor_positions(positions_dict['x'], positions_dict['y'], positions_dict['z'])
    
    def get_motor_positions_from_list(self, positions_list):
        return self.get_motor_positions(positions_list[0], positions_list[1], positions_list[2])
    
    def get_motor_positions_from_tuple(self, positions_tuple):
        return self.get_motor_positions(positions_tuple[0], positions_tuple[1], positions_tuple[2])
    
    def get_motor_positions_from_array(self, positions_array):
        return self.get_motor_positions(positions_array[0], positions_array[1], positions_array[2])
    
    def get_motor_positions_from_numpy_array(self, positions_numpy_array):
        return self.get_motor_positions(positions_numpy_array[0], positions_numpy_array[1], positions_numpy_array[2])
    
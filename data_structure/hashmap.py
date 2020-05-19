class HashMap:
    """Hashmap implementaion with open addressing"""

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        """ function for adding key, value pair in the hashmap"""
        array_index = self.compressor(self.hash(key))  # produce index via hash
        # retrieve the contents at the index
        current_array_value = self.array[array_index]

        if current_array_value is None:     # It's empty so assign
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:   # same key, overwrite the value
            self.array[array_index] = [key, value]
            return

        # Collision! since none of above matched

        number_collisions = 1   # set collision factor

        # while key and new locations's key is not the same,
        # that is, keep colliding, continue to search for a new location.
        while(current_array_value[0] != key):
            new_array_index = self.new_array_index(key, number_collisions)
            current_array_value = self.array[new_array_index]

            # if find empty space or the same key, assign or overwrite
            if (current_array_value is None) or current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            # Otherwise, increment collision factor try next spot
            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        # Collision!

        while (possible_return_value != key):

            new_array_index = self.new_array_index(key, retrieval_collisions)
            possible_return_value = self.array[new_array_index]

            # new spot is empty which means the key doesn't exist
            if possible_return_value is None:
                return None

            # found it!
            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return

    def new_array_index(self, key, collision_factor):
        new_hash_code = self.hash(key, collision_factor)
        new_array_index = self.compressor(new_hash_code)
        return new_array_index


hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))

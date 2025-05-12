class Bone:
    """
    Represents a single bone in the human skeletal system.

    Attributes:
        name (str): The name of the bone.
        type (str): The type of bone (e.g., long, short, flat, irregular).
        location (str): The general location of the bone in the body.
        function (str): The primary function of the bone.
        connected_bones (list): A list of bones that this bone articulates with.
        landmarks (dict): A dictionary of bony landmarks (e.g., processes, depressions).
    """

    def __init__(self, name, bone_type, location, function, connected_bones=[], landmarks={}):
        self.name = name
        self.type = bone_type
        self.location = location
        self.function = function
        self.connected_bones = connected_bones
        self.landmarks = landmarks

    def add_connected_bone(self, bone):
        """Adds a connected bone to the list."""
        self.connected_bones.append(bone)

    def add_landmark(self, name, description):
        """Adds a bony landmark to the dictionary."""
        self.landmarks[name] = description

    def __str__(self):
        """Returns a string representation of the bone."""
        return f"Bone: {self.name}\n" \
               f"Type: {self.type}\n" \
               f"Location: {self.location}\n" \
               f"Function: {self.function}\n" \
               f"Connected Bones: {', '.join(self.connected_bones)}\n" \
               f"Landmarks: {self.landmarks}"


class Cartilage:
    """
    Represents a type of connective tissue found in the human body.

    Attributes:
        type (str): The type of cartilage (e.g., hyaline, fibrocartilage, elastic).
        location (str): The general location of the cartilage in the body.
        function (str): The primary function of the cartilage.
    """

    def __init__(self, cartilage_type, location, function):
        self.type = cartilage_type
        self.location = location
        self.function = function

    def __str__(self):
        """Returns a string representation of the cartilage."""
        return f"Cartilage Type: {self.type}\n" \
               f"Location: {self.location}\n" \
               f"Function: {self.function}"


class SkeletalSystem:
    """
    Represents the entire human skeletal system.

    Attributes:
        bones (list): A list of Bone objects.
        cartilages (list): A list of Cartilage objects.
    """

    def __init__(self):
        self.bones = []
        self.cartilages = []

    def add_bone(self, bone):
        """Adds a Bone object to the list."""
        self.bones.append(bone)

    def add_cartilage(self, cartilage):
        """Adds a Cartilage object to the list."""
        self.cartilages.append(cartilage)

    def get_bone_by_name(self, name):
        """Returns the Bone object with the given name."""
        for bone in self.bones:
            if bone.name == name:
                return bone
        return None

    def get_cartilage_by_type(self, cartilage_type):
        """Returns the Cartilage object with the given type."""
        for cartilage in self.cartilages:
            if cartilage.type == cartilage_type:
                return cartilage
        return None

    def __str__(self):
        """Returns a string representation of the skeletal system."""
        bones_str = "\n".join([str(bone) for bone in self.bones])
        cartilages_str = "\n".join([str(cartilage) for cartilage in self.cartilages])
        return f"Skeletal System:\n\nBones:\n{bones_str}\n\nCartilages:\n{cartilages_str}"
import skeleton
from skeleton import Bone, Cartilage , SkeletalSystem

# Create bone objects
humerus = Bone("Humerus", "Long", "Upper Arm", "Movement of the arm", 
              connected_bones=["Scapula", "Radius", "Ulna"])
radius = Bone("Radius", "Long", "Forearm", "Movement of the forearm", 
              connected_bones=["Humerus", "Ulna", "Carpal bones"])

# Create cartilage object
hyaline_cartilage = Cartilage("Hyaline", "Articular surfaces of bones", 
                             "Reduces friction and absorbs shock")

# Create skeletal system object
skeleton = SkeletalSystem()

# Add bone and cartilage objects to the skeletal system
skeleton.add_bone(humerus)
skeleton.add_bone(radius)
skeleton.add_cartilage(hyaline_cartilage)

# Access and print information about specific bones
humerus_bone = skeleton.get_bone_by_name("Humerus")
print(humerus_bone) 

# Print the entire skeletal system information
print(skeleton)
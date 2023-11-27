class GardenPlant:
    def __init__(self, plant_id, disease_name, alias, scientific_name, morphology, cultivation_tips, pest_control_tips, application_value, image_ids):
        self.plant_id = plant_id
        self.disease_name = disease_name
        self.alias = alias
        self.scientific_name = scientific_name
        self.morphology = morphology
        self.cultivation_tips = cultivation_tips
        self.pest_control_tips = pest_control_tips
        self.application_value = application_value
        self.image_ids = image_ids

class PlantImage:
    def __init__(self, image_id, plant_id, image_data):
        self.image_id = image_id
        self.plant_id = plant_id
        self.image_data = image_data

class PestControlStrategy:
    def __init__(self, strategy_id, plant_id, strategy_description):
        self.strategy_id = strategy_id
        self.plant_id = plant_id
        self.strategy_description = strategy_description

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

class PlantView:
    def __init__(self, view_id, plant_id, view_name):
        self.view_id = view_id
        self.plant_id = plant_id
        self.view_name = view_name

class Maintenance:
    def __init__(self, maintenance_id, plant_id, date):
        self.maintenance_id = maintenance_id
        self.plant_id = plant_id
        self.date = date

class PlantManager:
    def __init__(self):
        self.plants = []  # Assuming a simple in-memory storage for demonstration

    def add_plant(self, plant):
        self.plants.append(plant)

    def update_plant(self, plant_id, new_plant_data):
        for plant in self.plants:
            if plant.plant_id == plant_id:
                # Update plant attributes based on new_plant_data
                plant.__dict__.update(new_plant_data)

    def delete_plant(self, plant_id):
        self.plants = [plant for plant in self.plants if plant.plant_id != plant_id]

    def get_plant_by_property(self, property_name, value):
        return [plant for plant in self.plants if getattr(plant, property_name, None) == value]

    def get_plant_count_by_scientific_name(self, scientific_name):
        return sum(1 for plant in self.plants if plant.scientific_name == scientific_name)

    def generate_plant_view(self, scientific_name):
        return [plant for plant in self.plants if plant.scientific_name == scientific_name]

class UserManager:
    def __init__(self):
        self.users = []  # Similarly, a simple in-memory storage

    def add_user(self, user):
        self.users.append(user)

# Example Usage:
garden_plant_management_system = PlantManager()
user_manager = UserManager()

# Adding a user (assuming user authentication)
user_manager.add_user(User(1, "admin", "admin123"))

# Adding a plant
garden_plant_management_system.add_plant(GardenPlant(1, "Leaf Spot", "Rose", "Rosaceae", "Rosa", "Deciduous shrub", "Water regularly", "Use fungicides", "Ornamental", [1, 2]))

# Modifying a plant
garden_plant_management_system.update_plant(1, {"disease_name": "Powdery Mildew", "alias": "Rosa Gallica"})

# Deleting a plant
garden_plant_management_system.delete_plant(1)

# Querying plants by property
result_plants = garden_plant_management_system.get_plant_by_property("scientific_name", "Rosa")

# Counting plants by scientific name
plant_count = garden_plant_management_system.get_plant_count_by_scientific_name("Rosaceae")

# Generating a plant view
view_plants = garden_plant_management_system.generate_plant_view("Rosaceae")

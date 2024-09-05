# owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return a list of all pets belonging to this owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner after validating that it is a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet. Must be an instance of Pet.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by name."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # If owner is provided, add this pet to the owner's list
        if owner:
            owner.add_pet(self)

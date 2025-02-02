class RelationshipManager:
    """Manages character relationship points (RP) for Cloud."""
    
    def __init__(self):
        self.relationships = {
            "Barret": 0,
            "Tifa": 0,
            "Jessie": 0
        }

    def adjust_relationship(self, character, points):
        """Modify relationship points for a character."""
        if character in self.relationships:
            self.relationships[character] += points
            print(f"\n[{character}] relationship changed by {points}. Current RP: {self.relationships[character]}")
        else:
            print(f"\nError: {character} not found in relationship system.")

    def get_relationship(self, character):
        """Retrieve relationship points for a character."""
        return self.relationships.get(character, None)

# Create a global instance
relationship_manager = RelationshipManager()

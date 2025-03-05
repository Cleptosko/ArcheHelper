class Database:
    def __init__(self):
        # Exemple de données de base pour les catégories et objets
        self.categories = [
            {"id": 1, "nom": "Agriculture"},
            {"id": 2, "nom": "Alchimie"},
            {"id": 3, "nom": "Armement"},
            {"id": 4, "nom": "Composition"},
            {"id": 5, "nom": "Confection"},
            {"id": 6, "nom": "Construction"},
            {"id": 7, "nom": "Cuisine"},
            {"id": 8, "nom": "Élevage"},
            {"id": 9, "nom": "Fabrication"},
            {"id": 10, "nom": "Forge"},
            {"id": 11, "nom": "Imprimerie"},
            {"id": 12, "nom": "Larcin"},
            {"id": 13, "nom": "Maçonnerie"},
            {"id": 14, "nom": "Mécanique"},
            {"id": 15, "nom": "Menuiserie"},
            {"id": 16, "nom": "Négoce"},
            {"id": 17, "nom": "Tannerie"}
        ]
        self.objects = [
            {"id": 1, "nom": "Brique de pierre", "categorie_id": 13, "coefficient": 3, "mat": 1}
        ]

    def get_categories(self):
        return self.categories

    def get_category_id(self, category_name):
        for category in self.categories:
            if category["nom"] == category_name:
                return category["id"]
        return None

    def get_objects(self, category_id):
        return [obj for obj in self.objects if obj["categorie_id"] == category_id]

    def get_object(self, object_id):
        for obj in self.objects:
            if obj["id"] == object_id:
                return obj
        return None
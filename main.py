import tkinter as tk
from tkinter import ttk
from database import Database

class ArcheHelperApp:
    def show_info(self):
        info_window = tk.Toplevel(self.root)
        info_window.title("Informations")
        tk.Label(info_window, text="ArcheHelper - Version Alpha 2 (A2)", font=("Arial", 12)).pack(pady=10)
        tk.Button(info_window, text="OK", command=info_window.destroy).pack(pady=5)

    def __init__(self, root, db):
        self.root = root
        self.root.title("ArcheHelper")
        self.root.configure(bg='#A9A9A9')  # Définir la couleur de fond de la fenêtre principale
        self.db = db

        # Ajouter le logo
        self.root.iconphoto(False, tk.PhotoImage(file="assets/logo.png"))

        self.create_selection_page()
        self.create_calculator_page()
        self.show_selection_page()

    def create_selection_page(self):
        self.frame_selection = tk.Frame(self.root, bg='#A9A9A9')  # Définir la couleur de fond du cadre
        
        # Barre de séparation au-dessus de "Choisir une catégorie"
        self.separator_top = tk.Frame(self.frame_selection, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_top.pack(fill=tk.X, pady=5)
        
        self.label_selection = tk.Label(self.frame_selection, text="Choisir une catégorie :", font=("Arial", 14), bg='#A9A9A9')
        self.label_selection.pack(pady=10)
        
        # Barre de séparation en dessous de "Choisir une catégorie"
        self.separator_middle = tk.Frame(self.frame_selection, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_middle.pack(fill=tk.X, pady=5)
        
        categories = self.db.get_categories()
        self.selected_category = tk.StringVar()
        self.dropdown = ttk.Combobox(self.frame_selection, textvariable=self.selected_category, values=[c['nom'] for c in categories])
        self.dropdown.pack(pady=10)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_objects)

        self.buttons_frame = tk.Frame(self.frame_selection, bg='#A9A9A9')
        self.buttons_frame.pack(pady=10)
        
        # Barre de séparation
        self.separator = tk.Frame(self.frame_selection, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator.pack(fill=tk.X, pady=5)
        
        self.info_button = tk.Button(self.frame_selection, text="Info", command=self.show_info, bg='#77DD77', fg='white')
        self.info_button.pack(pady=5)
        
        self.quit_button = tk.Button(self.frame_selection, text="Quitter", command=self.root.quit, bg='#FF6961', fg='white')
        self.quit_button.pack(pady=5)
        
        # Barre de séparation en dessous du bouton "Quitter"
        self.separator_bottom = tk.Frame(self.frame_selection, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_bottom.pack(fill=tk.X, pady=5)

    def update_objects(self, event):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        category_name = self.selected_category.get()
        category_id = self.db.get_category_id(category_name)
        objects = self.db.get_objects(category_id)
        
        for obj in objects:
            button = tk.Button(self.buttons_frame, text=obj['nom'], command=lambda obj=obj: self.show_calculator_page(obj), bg='#D8BFD8', fg='black')
            button.pack(pady=5)

    def create_calculator_page(self):
        self.frame_calculator = tk.Frame(self.root, bg='#A9A9A9')  # Définir la couleur de fond du cadre
        self.selected_object = tk.StringVar()
        
        # Barre de séparation au-dessus de "Brique de pierre"
        self.separator_top = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_top.pack(fill=tk.X, pady=5)
        
        self.label_calculator = tk.Label(self.frame_calculator, textvariable=self.selected_object, font=("Arial", 14), bg='#A9A9A9')
        self.label_calculator.pack(pady=10)
        
        # Barre de séparation en dessous de "Brique de pierre"
        self.separator_middle = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_middle.pack(fill=tk.X, pady=5)

        self.label_quantity = tk.Label(self.frame_calculator, text="Nombre de briques à vendre :", font=("Arial", 12), bg='#A9A9A9')
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(self.frame_calculator)
        self.entry_quantity.pack(pady=5)
        
        # Barre de séparation en dessous de "Nombre de briques à vendre"
        self.separator_quantity_bottom = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_quantity_bottom.pack(fill=tk.X, pady=5)
        
        self.label_cost = tk.Label(self.frame_calculator, text="Coût d'une pierre :", font=("Arial", 12), bg='#A9A9A9')
        self.label_cost.pack()

        self.frame_cost = tk.Frame(self.frame_calculator, bg='#A9A9A9')
        self.frame_cost.pack(pady=5)

        self.entry_cost_po = tk.Entry(self.frame_cost, width=5)
        self.entry_cost_po.insert(0, "0")
        self.entry_cost_po.pack(side=tk.LEFT)
        tk.Label(self.frame_cost, text="PO", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_cost_pa = tk.Entry(self.frame_cost, width=5)
        self.entry_cost_pa.insert(0, "0")
        self.entry_cost_pa.pack(side=tk.LEFT)
        tk.Label(self.frame_cost, text="PA", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_cost_pc = tk.Entry(self.frame_cost, width=5)
        self.entry_cost_pc.insert(0, "0")
        self.entry_cost_pc.pack(side=tk.LEFT)
        tk.Label(self.frame_cost, text="PC", bg='#A9A9A9').pack(side=tk.LEFT)
        
        # Barre de séparation en dessous de "Coût d'une pierre"
        self.separator_cost_bottom = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_cost_bottom.pack(fill=tk.X, pady=5)
        
        self.label_price = tk.Label(self.frame_calculator, text="Prix de vente d'une brique :", font=("Arial", 12), bg='#A9A9A9')
        self.label_price.pack()

        self.frame_price = tk.Frame(self.frame_calculator, bg='#A9A9A9')
        self.frame_price.pack(pady=5)

        self.entry_price_po = tk.Entry(self.frame_price, width=5)
        self.entry_price_po.insert(0, "0")
        self.entry_price_po.pack(side=tk.LEFT)
        tk.Label(self.frame_price, text="PO", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_price_pa = tk.Entry(self.frame_price, width=5)
        self.entry_price_pa.insert(0, "0")
        self.entry_price_pa.pack(side=tk.LEFT)
        tk.Label(self.frame_price, text="PA", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_price_pc = tk.Entry(self.frame_price, width=5)
        self.entry_price_pc.insert(0, "0")
        self.entry_price_pc.pack(side=tk.LEFT)
        tk.Label(self.frame_price, text="PC", bg='#A9A9A9').pack(side=tk.LEFT)
        
        # Barre de séparation en dessous de "Prix de vente d'une brique"
        self.separator_price_bottom = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_price_bottom.pack(fill=tk.X, pady=5)
        
        self.label_labor = tk.Label(self.frame_calculator, text="Coût de la main-d'œuvre :", font=("Arial", 12), bg='#A9A9A9')
        self.label_labor.pack()

        self.frame_labor = tk.Frame(self.frame_calculator, bg='#A9A9A9')
        self.frame_labor.pack(pady=5)

        self.entry_labor_po = tk.Entry(self.frame_labor, width=5)
        self.entry_labor_po.insert(0, "0")
        self.entry_labor_po.pack(side=tk.LEFT)
        tk.Label(self.frame_labor, text="PO", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_labor_pa = tk.Entry(self.frame_labor, width=5)
        self.entry_labor_pa.insert(0, "0")
        self.entry_labor_pa.pack(side=tk.LEFT)
        tk.Label(self.frame_labor, text="PA", bg='#A9A9A9').pack(side=tk.LEFT)

        self.entry_labor_pc = tk.Entry(self.frame_labor, width=5)
        self.entry_labor_pc.insert(0, "0")
        self.entry_labor_pc.pack(side=tk.LEFT)
        tk.Label(self.frame_labor, text="PC", bg='#A9A9A9').pack(side=tk.LEFT)
        
        # Barre de séparation en dessous de "Coût de la main-d'œuvre"
        self.separator_labor_bottom = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_labor_bottom.pack(fill=tk.X, pady=5)
        
        self.calculate_button = tk.Button(self.frame_calculator, text="Lancer", command=self.calculate_result, bg='#4682B4', fg='white')
        self.calculate_button.pack(pady=10)

        self.back_button = tk.Button(self.frame_calculator, text="Retour au menu", command=self.show_selection_page, bg='#4682B4', fg='white')
        self.back_button.pack(pady=10)
        
        # Barre de séparation au-dessus de "Résultat"
        self.separator_result_top = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_result_top.pack(fill=tk.X, pady=5)

        self.label_result = tk.Label(self.frame_calculator, text="Résultat :", font=("Arial", 14), bg='#A9A9A9')
        self.label_result.pack(pady=10)
        
        # Barre de séparation en dessous de "Résultat"
        self.separator_result_bottom = tk.Frame(self.frame_calculator, height=2, bd=1, relief=tk.SUNKEN, bg='black')
        self.separator_result_bottom.pack(fill=tk.X, pady=5)

    def show_selection_page(self):
        self.frame_calculator.pack_forget()
        self.frame_selection.pack(fill=tk.BOTH, expand=True)

    def show_calculator_page(self, obj):
        self.frame_selection.pack_forget()
        self.frame_calculator.pack(fill=tk.BOTH, expand=True)
        self.selected_object.set(obj['nom'])
        self.selected_object_id = obj['id']
        self.coefficient = obj['coefficient']

    def po_pa_pc_to_value(self, po, pa, pc):
        """Convertit PO, PA, PC en une valeur unique."""
        return po + (pa / 100) + (pc / 10000)

    def value_to_po_pa_pc(self, value):
        """Convertit une valeur unique en PO, PA, PC."""
        po = int(value // 1)
        remaining = (value % 1) * 100
        pa = int(remaining // 1)
        pc = round((remaining % 1) * 100)
        
        if pc >= 100:
            pa += pc // 100
            pc = pc % 100
        
        if pa >= 100:
            po += pa // 100
            pa = pa % 100
        
        return po, pa, pc

    def calculate_result(self):
        try:
            quantity = int(self.entry_quantity.get())
        
            cost_po = int(self.entry_cost_po.get())
            cost_pa = int(self.entry_cost_pa.get())
            cost_pc = int(self.entry_cost_pc.get())
            cost_total = self.po_pa_pc_to_value(cost_po, cost_pa, cost_pc)

            price_po = int(self.entry_price_po.get())
            price_pa = int(self.entry_price_pa.get())
            price_pc = int(self.entry_price_pc.get())
            price_total = self.po_pa_pc_to_value(price_po, price_pa, price_pc)

            labor_po = int(self.entry_labor_po.get())
            labor_pa = int(self.entry_labor_pa.get())
            labor_pc = int(self.entry_labor_pc.get())
            labor_total = self.po_pa_pc_to_value(labor_po, labor_pa, labor_pc)
        
            # Calcul des dépenses
            A = cost_total * self.coefficient * quantity
            B = price_total * quantity
            total_cost = labor_total + A
            final_profit = B - total_cost - (0.05 * (B - total_cost))
        
            # Conversion des gains finaux en PO, PA, PC
            po, pa, pc = self.value_to_po_pa_pc(final_profit)
        
            # Définir la couleur du texte en fonction du résultat
            if final_profit > 0:
                text = f"Bénéfices : {po} PO, {pa} PA, {pc} PC"
                color = 'green'
            else:
                text = f"Pertes : {po} PO, {pa} PA, {pc} PC"
                color = 'red'
        
            self.label_result.config(text=text, fg=color)
        except ValueError:
            self.label_result.config(text="Veuillez entrer des valeurs valides.", fg='red')

def main():
    root = tk.Tk()
    db = Database()
    app = ArcheHelperApp(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()
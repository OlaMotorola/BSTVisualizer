import tkinter as tk
from tkinter import Canvas, Entry, Button, simpledialog
from bst import BST


class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=800, height=400)
        self.canvas.pack()

        self.tree = BST()

        self.message_label = tk.Label(self.root, text="", fg="white")
        self.message_label.pack()
        self.node_input = Entry(root)
        self.node_input.pack()

        self.insert_button = Button(root, text="Wstaw węzeł", command=self.insert_node)
        self.insert_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = Button(root, text="Usuń węzeł", command=self.delete_node)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.balance_button = Button(root, text="Zrównoważ drzewo", command=self.balance_tree)
        self.balance_button.pack(side=tk.LEFT, padx=5)

        find_button = tk.Button(root, text="Znajdź węzeł", command=self.find_node)
        find_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(self.root, text="Edytuj węzeł", command=self.edit_node)
        edit_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(self.root, text="Wyczyść drzewo", command=self.clear_tree)
        clear_button.pack(side=tk.LEFT, padx=5)

        stats_button = tk.Button(self.root, text="Statystyki", command=self.show_stats)
        stats_button.pack(side=tk.LEFT, padx=5)

    def _get_input(self):
        try:
            return int(self.node_input.get())
        except ValueError:
            self.message_label.config(text="Proszę wprowadzić liczbę całkowitą.", fg="red")
            return None

    def insert_node(self):
        data = self._get_input()
        if data is None:
            return
        self.tree.insert(data)
        self.message_label.config(text=f"Węzeł {data} dodany!", fg="green")
        self.node_input.delete(0, tk.END)
        self.draw_tree()

    def delete_node(self):
        data = self._get_input()
        if data is None:
            return
        found_node = self.tree.find(data)
        if found_node:
            self.message_label.config(text=f"Węzeł {data} usunięty!", fg="green")
            self.tree.delete(data)
            self.draw_tree()
            self.node_input.delete(0, tk.END)
            self.tree.delete(data)
        else:
            self.message_label.config(text=f"Węzeł {data} nie istnieje.", fg="red")

    def find_node(self):
        data = self._get_input()
        if data is None:
            return
        found_node = self.tree.find(data)
        if found_node:
            self.message_label.config(text=f"Węzeł {data} znaleziony!", fg="green")
            self.tree.last_inserted = found_node
            self.node_input.delete(0, tk.END)
            self.draw_tree()
        else:
            self.message_label.config(text=f"Węzeł {data} nie istnieje.", fg="red")

    def edit_node(self):
        data = self._get_input()
        if data is None:
            return
        found_node = self.tree.find(data)
        if not found_node:
            self.message_label.config(text=f"Węzeł {data} nie istnieje.", fg="red")
            return
        new_data = simpledialog.askinteger("Edytuj węzeł", f"Nowa wartość dla węzła {data}:")
        if new_data is not None:
            self.tree.delete(data)
            self.tree.insert(new_data)
            self.message_label.config(text=f"Węzeł {data} zmieniony na {new_data}.", fg="green")
            self.node_input.delete(0, tk.END)
            self.draw_tree()

    def clear_tree(self):
        self.tree.clear()
        self.draw_tree()

    def balance_tree(self):
        self.tree.dsw_balance()
        self.draw_tree()

    def show_stats(self):
        height = self.tree.height()
        size = self.tree.size()
        min_val = self.tree.min_value()
        max_val = self.tree.max_value()
        stats = ("Statystyki:\n"
                 f"Wysokość drzewa: {height}\n"
                 f"Liczba węzłów: {size}\n"
                 f"Minimalna wartość: {min_val}\n"
                 f"Maksymalna wartość: {max_val}")
        self.message_label.config(text=stats, fg="white")

    def draw_tree(self):
        self.canvas.delete("all")
        self.draw_node(self.tree.root, 400, 50, 150)

    def draw_node(self, node, x, y, x_offset):
        if node is None:
            return
        r = 20
        y_vec = 50
        if node.left:
            x_child = x - x_offset
            y_child = y + y_vec
            self.canvas.create_line(
                x, y,
                x_child, y_child - r,
                width=2
            )
            self.draw_node(node.left, x_child, y_child, x_offset / 2)
        if node.right:
            x_child = x + x_offset
            y_child = y + y_vec
            self.canvas.create_line(
                x, y,
                x_child, y_child - r,
                width=2
            )
            self.draw_node(node.right, x_child, y_child, x_offset / 2)

        fill_color = "orange" if node == self.tree.last_inserted else "lightblue"
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill_color, outline="black")
        self.canvas.create_text(x, y, text=str(node.data), font=('Helvetica', 12), fill="black")

    def reset_last_inserted(self):
        self.tree.last_inserted = None
        self.draw_tree()

    def run(self):
        self.root.mainloop()


def balance_tree(bst):
    bst.dsw_balance()


def main():
    root = tk.Tk()
    root.title("Wizualizacja Drzewa BST")
    visualizer = BSTVisualizer(root)
    visualizer.run()


if __name__ == "__main__":
    main()

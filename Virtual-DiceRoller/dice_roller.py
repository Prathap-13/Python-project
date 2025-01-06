import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import matplotlib.pyplot as plt
from tkinter import messagebox
import time

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roller")
        self.root.configure(bg='aqua')  # Set the background color to aqua

        # Load dice images
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"images/dice{i}.png")) for i in range(1, 7)
        ]

        # Dictionary to store player scores
        self.player_scores = {self.get_player_name(1): 0, self.get_player_name(2): 0}

        # Labels to display dice images for each player
        self.player1_dice_label = ttk.Label(self.root, image=self.dice_images[0])
        self.player1_dice_label.pack(side=tk.LEFT, padx=10)

        self.player2_dice_label = ttk.Label(self.root, image=self.dice_images[0])
        self.player2_dice_label.pack(side=tk.RIGHT, padx=10)

        self.create_widgets()

    def create_widgets(self):
        
    # Create a custom style for the buttons with the desired font size
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 16))

    # Labels and entry widgets for player names and number of rolls
        self.player1_name_label = ttk.Label(self.root, text="Player 1:")
        self.player1_name_label.pack(pady=5)
        self.player1_name_entry = ttk.Entry(self.root)
        self.player1_name_entry.pack()

        self.player2_name_label = ttk.Label(self.root, text="Player 2:")
        self.player2_name_label.pack(pady=5)
        self.player2_name_entry = ttk.Entry(self.root)
        self.player2_name_entry.pack()

        self.roll_label = ttk.Label(self.root, text="Enter the number of rolls:")
        self.roll_label.pack(pady=5)
        self.roll_entry = ttk.Entry(self.root)
        self.roll_entry.pack()

    # Button to roll the dice
        self.roll_button = ttk.Button(self.root, text="Roll Dice", command=self.roll_dice, style="TButton")
        self.roll_button.pack(pady=10)

    # Text widget to display results
        self.results_text = tk.Text(self.root, height=10, width=30)
        self.results_text.pack(pady=10)

    # Buttons to plot line and bar charts
        self.plot1_button = ttk.Button(self.root, text="Plot Line Chart", command=self.plot_line_chart, style="TButton")
        self.plot1_button.pack(pady=5)

        self.plot2_button = ttk.Button(self.root, text="Plot Bar Chart", command=self.plot_bar_chart, style="TButton")
        self.plot2_button.pack(pady=5)


    def roll_dice_animation(self, player_dice_label):
        # Animate the dice rolling
        for _ in range(5):  # Simulate rolling effect
            for i in range(1, 7):
                player_dice_label.configure(image=self.dice_images[i - 1])
                self.root.update()  # Update the window
                time.sleep(0.05)  # Reduced delay time
        # Set the final dice image
        player_dice_label.configure(image=self.dice_images[random.randint(0, 5)])

    def roll_dice(self):
        try:
            num_rolls = int(self.roll_entry.get())
        except ValueError:
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, "Please enter a valid number.")
            return

        player1_name = self.get_player_name(1)
        player2_name = self.get_player_name(2)

        self.results_text.delete("1.0", tk.END)
        for _ in range(num_rolls):
            # Animate the dice rolling for each player
            self.roll_dice_animation(self.player1_dice_label)
            self.roll_dice_animation(self.player2_dice_label)

            # Roll the dice
            player1_roll = random.randint(1, 6)
            player2_roll = random.randint(1, 6)

            # Update the dice images
            self.player1_dice_label.configure(image=self.dice_images[player1_roll - 1])
            self.player2_dice_label.configure(image=self.dice_images[player2_roll - 1])

            # Determine the winner
            if player1_roll > player2_roll:
                self.player_scores[player1_name] += 1
                winner = player1_name
            elif player1_roll < player2_roll:
                self.player_scores[player2_name] += 1
                winner = player2_name
            else:
                winner = "Draw"

            # Display the result
            if winner != "Draw":
                self.results_text.insert(tk.END, f"{winner} wins\n")
                self.display_congratulations(winner)
            else:
                self.results_text.insert(tk.END, f"Draw\n")

        self.results_text.insert(tk.END, "Rolls completed.")

    def get_player_name(self, player_number):
        return f"Player {player_number}"

    def display_congratulations(self, winner):
        messagebox.showinfo("Congratulations!", f"Congratulations, {winner}! Keep playing!")

    def plot_line_chart(self):
        players = list(self.player_scores.keys())
        wins = list(self.player_scores.values())
        plt.plot(players, wins, marker='o')
        plt.ylabel("Wins")
        plt.title("Dice Roller Line Chart")
        plt.show()

    def plot_bar_chart(self):
        fig, ax = plt.subplots()
        players = list(self.player_scores.keys())
        wins = list(self.player_scores.values())

        ax.bar(players, wins, color=["skyblue", "salmon"])
        ax.set_ylabel("Wins")
        ax.set_title("Dice Roller Bar Chart")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

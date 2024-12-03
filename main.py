import tkinter as tk
from vote_manager import VoteManager


class VoteApp:
    """Voting App built with tkinter """

    def __init__(self, root: tk.Tk):
        """Starts the VoteApp"""
        self.root = root
        self.root.title("Vote Manager")
        self.manager = VoteManager()

        #Start of GUI elements
        self.results_label = tk.Label(root, text=self._get_results_text(), font=("Arial", 14))
        self.results_label.pack(pady=10)

        self.vote_status_label = tk.Label(root, text="No votes yet", font=("Arial", 12), fg="blue")
        self.vote_status_label.pack(pady=5)

        vote_john_button = tk.Button(root, text="Vote for John", command=lambda: self.cast_vote("John"), font=("Arial", 12))
        vote_john_button.pack(pady=5)

        vote_jane_button = tk.Button(root, text="Vote for Jane", command=lambda: self.cast_vote("Jane"), font=("Arial", 12))
        vote_jane_button.pack(pady=5)

        done_button = tk.Button(root, text="Done", command=self.show_summary, font=("Arial", 12), bg="green", fg="white")
        done_button.pack(pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
        exit_button.pack(pady=10)
        # End of GUI elements

    def cast_vote(self, candidate_name: str) -> None:
        """Handles logic with the buttons when clicked"""
        try:
            self.manager.cast_vote(candidate_name)
            self.results_label.config(text=self._get_results_text())
            self.vote_status_label.config(text=f"You voted for {candidate_name}")
        except ValueError as e:
            self.vote_status_label.config(text=str(e), fg="red")

    def show_summary(self) -> None:
        """Displays a summary of the votes in the main window. Shows the total votes for each candidate and the combined total"""
        results = self.manager.get_results()
        total_votes = results["John"] + results["Jane"]
        summary_text = (
            f"Voting Complete!\n"
            f"John: {results['John']} votes\n"
            f"Jane: {results['Jane']} votes\n"
            f"Total Votes: {total_votes}"
        )
        self.results_label.config(text=summary_text)
        self.vote_status_label.config(text="Thank you for voting!", fg="green")

    def _get_results_text(self) -> str:
        """
        Formats the current vote tally for display in the results label. Then it returns the total amount of votes for each"""
        results = self.manager.get_results()
        return f"John: {results['John']} votes, Jane: {results['Jane']} votes"


if __name__ == "__main__":
    root = tk.Tk()
    app = VoteApp(root)
    root.mainloop()

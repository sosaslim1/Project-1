import pytest
import tkinter as tk
from main import VoteApp


@pytest.fixture
def app():
    """Create a Tkinter root and the VoteApp for testing."""
    root = tk.Tk()
    app_instance = VoteApp(root)
    yield app_instance
    root.destroy()


def test_initial_display(app):
    """Test that the initial display shows zero votes."""
    assert app.results_label.cget("text") == "John: 0 votes, Jane: 0 votes"
    assert app.vote_status_label.cget("text") == "No votes yet"


def test_cast_vote_updates_display(app):
    """Test that voting updates the display correctly."""
    app.cast_vote("John")
    assert app.results_label.cget("text") == "John: 1 votes, Jane: 0 votes"
    assert app.vote_status_label.cget("text") == "You voted for John"

    app.cast_vote("Jane")
    assert app.results_label.cget("text") == "John: 1 votes, Jane: 1 votes"
    assert app.vote_status_label.cget("text") == "You voted for Jane"


def test_show_summary(app):
    """Test that the summary updates correctly after voting."""
    app.cast_vote("John")
    app.cast_vote("Jane")
    app.show_summary()
    expected_summary = "Voting Complete!\nJohn: 1 votes\nJane: 1 votes\nTotal Votes: 2"
    assert app.results_label.cget("text") == expected_summary
    assert app.vote_status_label.cget("text") == "Thank you for voting!"

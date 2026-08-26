import pytest

from src.yo_momma_agent.yo_momma_jokes_agent import Joke, YoMommaJokesAgent


class TestYoMommaJokesAgent:
    def test_default_agent_loads_jokes(self):
        agent = YoMommaJokesAgent()
        assert len(agent) > 0

    def test_get_best_joke_returns_highest_rated(self):
        agent = YoMommaJokesAgent()
        best = agent.get_best_joke()
        assert all(best.rating >= joke.rating for joke in agent._heap)

    def test_get_best_jokes_is_sorted_descending(self):
        agent = YoMommaJokesAgent()
        top_jokes = agent.get_best_jokes(3)
        ratings = [joke.rating for joke in top_jokes]
        assert ratings == sorted(ratings, reverse=True)
        assert len(top_jokes) == 3

    def test_get_best_jokes_caps_at_collection_size(self):
        agent = YoMommaJokesAgent(jokes=[Joke(5.0, "one"), Joke(7.0, "two")])
        assert len(agent.get_best_jokes(10)) == 2

    def test_add_joke_can_become_the_best(self):
        agent = YoMommaJokesAgent(jokes=[Joke(1.0, "meh")])
        agent.add_joke(Joke(10.0, "Yo momma's so cracked, we made her an agent."))
        assert agent.get_best_joke().rating == 10.0

    def test_empty_agent_raises_on_best_joke(self):
        agent = YoMommaJokesAgent(jokes=[])
        with pytest.raises(IndexError):
            agent.get_best_joke()

    def test_get_random_joke_returns_a_joke_from_the_collection(self):
        agent = YoMommaJokesAgent()
        joke = agent.get_random_joke()
        assert joke in agent._heap

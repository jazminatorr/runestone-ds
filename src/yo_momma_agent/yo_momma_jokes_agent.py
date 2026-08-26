"""
###########################################################################################
########## Yo Momma Jokes Agent
###########################################################################################
A small "agent" that keeps a curated collection of yo momma jokes, each with a rating,
and can hand back the best ones on request.

Ranking is backed by a binary max-heap (via heapq, negated for max-heap behavior) so that
fetching the single best joke is O(1) amortized and fetching the top-n is O(n log k),
rather than re-sorting the whole collection every time.
"""
import heapq
import random
from dataclasses import dataclass, field


@dataclass(order=True)
class Joke:
    rating: float
    text: str = field(compare=False)

    def __str__(self) -> str:
        return f"{self.text} ({self.rating}/10)"


DEFAULT_JOKES: list[Joke] = [
    Joke(9.5, "Yo momma's so old, she has a picture of Moses in her yearbook."),
    Joke(9.2, "Yo momma's so short, she can dangle her legs off a curb."),
    Joke(9.0, "Yo momma's so smart, she used to be a lion tamer for a living."),
    Joke(8.8, "Yo momma's so old, her birth certificate says 'expired.'"),
    Joke(8.5, "Yo momma's so slow, it takes her two hours to watch 60 Minutes."),
    Joke(8.3, "Yo momma's so tall, she can shake hands with God."),
    Joke(8.0, "Yo momma's so nice, she waves at the TV when her show comes on."),
    Joke(7.5, "Yo momma's so bright, she could be a lighthouse."),
    Joke(7.2, "Yo momma's so forgetful, she brought a spoon to the movies."),
    Joke(6.8, "Yo momma's so friendly, she introduces herself to her own reflection."),
]


class YoMommaJokesAgent:
    """Curates yo momma jokes and serves up the best ones, ranked by rating."""

    def __init__(self, jokes: list[Joke] | None = None):
        self._heap: list[Joke] = []
        for joke in jokes if jokes is not None else DEFAULT_JOKES:
            self.add_joke(joke)

    def add_joke(self, joke: Joke) -> None:
        # heapq is a min-heap, so push the joke with its natural ordering and
        # pop from the "small" end reversed at read time to simulate a max-heap.
        heapq.heappush(self._heap, joke)

    def get_best_joke(self) -> Joke:
        """Return the single highest-rated joke without removing it."""
        if not self._heap:
            raise IndexError("No jokes available")
        return max(self._heap, key=lambda j: j.rating)

    def get_best_jokes(self, n: int = 5) -> list[Joke]:
        """Return the top-n highest-rated jokes, best first."""
        return heapq.nlargest(n, self._heap, key=lambda j: j.rating)

    def get_random_joke(self) -> Joke:
        if not self._heap:
            raise IndexError("No jokes available")
        return random.choice(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

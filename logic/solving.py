import math
from typing import Tuple, Union

class QuadraticSolver:
    """Résout une équation du second degré : ax² + bx + c = 0 (solutions réelles uniquement)."""

    """ Constructor """
    def __init__(self):
        pass

    """ Calcul logic """
    def solve(self, value_a: float, value_b: float, value_c: float) -> Union[str, Tuple[float, float, float]]:
        """Retourne (delta, x1, x2) ou un message d'erreur."""
        if value_a == 0:
            raise ValueError("Le coefficient 'a' ne peut pas être 0 (sinon ce n'est pas une équation du second degré).")

        delta = value_b**2 - 4*value_a*value_c

        if delta < 0:
            return f"Pas de racines réelles (Δ = {delta:.2f})."

        elif delta == 0:
            x = -value_b/ (2 * value_a)
            return (delta, x, x)

        else:
            sqrt_delta = math.sqrt(delta)
            x1 = (-value_b + sqrt_delta) / (2 * value_a)
            x2 = (-value_b - sqrt_delta) / (2 * value_a)
            return (delta, x1, x2)

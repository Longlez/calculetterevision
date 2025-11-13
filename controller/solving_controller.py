from logic.solving import QuadraticSolver

class SolverController:
    """Contrôleur : gère la logique métier et formate le résultat pour l'UI."""

    def __init__(self, solver: QuadraticSolver):
        self.solver = solver

    """ Fonction qui fera le calcul principal """
    def compute(self, a_text: str, b_text: str, c_text: str) -> str:
        try:
            value_a = float(a_text)
            value_b = float(b_text)
            value_c = float(c_text)

            result = self.solver.solve(value_a, value_b, value_c)

            if isinstance(result, tuple):
                delta, x1, x2 = result
                if delta == 0:
                    return f"Δ = {delta:.2f}\nRacine double : x = {x1:.2f}"
                else:
                    return f"Δ = {delta:.2f}\nx₁ = {x1:.2f}\nx₂ = {x2:.2f}"
            else:
                # cas où solver renvoie un message (pas de racines réelles)
                return result

        except ValueError as e:
            return f"Erreur : {e}"
        except Exception:
            return "Erreur inattendue. Vérifiez vos entrées."

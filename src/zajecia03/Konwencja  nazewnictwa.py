_internal_var = "To jest zmienna wewnętrzna"


def _internal_function():
    return "To jest funkcja wewnętrzna"


def public_function():
    return "To jest funkcja publiczna"


class ExampleClass:
    def __init__(self, value):
        self.value = (
            value  # Funkcja __init__ jest wywoływana przy tworzeniu obiektu tej klasy
        )

    def __str__(self):
        return f"ExampleClass with value: {self.value}"  # __str__ definiuje, jak obiekt będzie reprezentowany w formie tekstu


obj = ExampleClass(10)
print(obj)

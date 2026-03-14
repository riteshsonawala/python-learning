from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


if __name__ == "__main__":
    user = User(name="Alice", age=30)
    print(user.greet())
    user = User(name="Bob", age="Twenty-five")
    print(user.greet())
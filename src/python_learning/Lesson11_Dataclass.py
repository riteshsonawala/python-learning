from dataclasses import dataclass

@dataclass
class student:
    name: str
    age: int

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age}) from __repr__"

if __name__ == "__main__":
    student1 = student("Ritesh", 25)
    print(student1)

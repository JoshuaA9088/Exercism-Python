class Garden(object):
    default_students = ["Alice", "Bob", "Charlie", "David",
                        "Eve", "Fred", "Ginny", "Harriet",
                        "Ileana", "Joseph", "Kincaid", "Larry"]
    

    def __init__(self, diagram, students=default_students):
        self.students = students
        self.students.sort()
        self.process_diagram(diagram)
        self.abbreviations = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def process_diagram(self, diagram):
        self.row_0 = diagram.split()[0]
        self.row_1 = diagram.split()[1]

    def plants(self, name):
        students_plants = ""
        offset = self.students.index(name)
        row_0 = [self.row_0[2 * offset], self.row_0[2 * offset + 1]]
        row_1 = [self.row_1[2 * offset], self.row_1[2 * offset + 1]]
        # Process output to convert letter to full name
        students_plants = [self.abbreviations[plant] for plant in row_0]
        students_plants += [self.abbreviations[plant] for plant in row_1]

        return students_plants
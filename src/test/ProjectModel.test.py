import sys, os, unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../main'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../main/fileParser'))

from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener

class ProjectModelTest(unittest.TestCase):

    path = "./ExampleJavaClass.java"
    project_name = "ExampleJavaClass"
    project_output_file = project_name + ".json"
    project_model: ProjectModel = None
    project_print = None

    def setUp(self):
        self.project_model = ProjectModel(self.path, self.project_name)
        self.project_model.parse_file()
        self.project_print = self.project_model.to_print()
        FileOpener().save_file_as_json(self.project_print, self.project_output_file)

    def test_project_has_1_file(self):
        self.assertEqual(len(self.project_model.files), 1)

    def test_file_has_correct_path(self):
        file = self.project_model.files[0]
        self.assertEqual(file.path, self.path)

    def test_identifier_types_has_correct_length(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_model.to_print()), 4)

    def test_file_has_1_class_name(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_model.class_names), 1)

    def test_file_has_correct_class_name(self):
        file = self.project_model.files[0]
        class_name = file.identifier_model.class_names[0]
        self.assertEqual(class_name.name, "ExampleJavaClass")   

    def test_file_has_correct_class_name_line(self):
        file = self.project_model.files[0]
        class_name = file.identifier_model.class_names[0]
        self.assertEqual(class_name.line, 3)   

if __name__ == '__main__':
    unittest.main()
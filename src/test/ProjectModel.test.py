import sys, os, unittest, warnings

sys.path.append(os.path.join(os.path.dirname(__file__), '../main'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../main/parser'))

from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener

class ProjectModelTest(unittest.TestCase):

    path = "./ExampleJavaClass.java"
    project_name = "ExampleJavaClass"
    project_output_file = project_name + ".json"
    project_model: ProjectModel = None
    project_print = None

    @classmethod
    def setUpClass(cls):
        cls.ignore_numpy_warning()
        cls.project_model = ProjectModel(cls.path, cls.project_name)
        cls.project_model.parse_file()
        cls.project_print = cls.project_model.to_print()
        FileOpener().save_file_as_json(cls.project_print, cls.project_output_file)

    @classmethod
    def ignore_numpy_warning(cls):
        warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

    def test_project_has_1_file(self):
        self.assertEqual(len(self.project_model.files), 1)

    def test_file_has_correct_path(self):
        file = self.project_model.files[0]
        self.assertEqual(file.path, self.path)

    def test_file_has_4_identifier_types(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_list_model.to_print()), 4)

    def test_file_has_1_class_name(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_list_model.class_names), 1)

    def test_file_has_correct_class_name(self):
        file = self.project_model.files[0]
        class_name = file.identifier_list_model.class_names[0]
        self.assertEqual(class_name.name, "ExampleJavaClass")   

    def test_file_has_correct_class_name_line(self):
        file = self.project_model.files[0]
        class_name = file.identifier_list_model.class_names[0]
        self.assertEqual(class_name.line, 3)

    def test_file_has_4_method_names(self):
        method_names = self.project_model.files[0].identifier_list_model.method_names
        self.assertEqual(len(method_names), 4)

    def test_file_has_9_dictionary_entries(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        self.assertEqual(len(dictionary), 9)

    def test_dictionary_contains_correct_class_name(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        class_identifier = dictionary.get(self.project_name)
        self.assertEqual(class_identifier.line_numbers[0], 3)
        self.assertEqual(len(class_identifier.separated_words), 3)

    def test_dictionary_contains_correct_foo_identifier(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        foo_identifier = dictionary.get("foo")
        self.assertEqual(len(foo_identifier.line_numbers), 2)
        self.assertEqual(len(foo_identifier.separated_words), 1)


if __name__ == '__main__':
    unittest.main()
import sys, os, unittest, warnings

sys.path.append(os.path.join(os.path.dirname(__file__), '../main'))

from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener
from model.IdentifierType import IdentifierType

class ProjectModelTest(unittest.TestCase):

    path = "./ExampleJavaClass.java"
    project_name = "ExampleJavaClass"
    project_output_file = project_name + ".json"
    project_model: ProjectModel = None
    project_print = None

    @classmethod
    def setUpClass(cls):
        cls.ignore_numpy_warning()
        cls.project_model = ProjectModel(cls.path)
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

    def test_file_has_10_identifiers_in_list(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_list_model.to_print()), 10)

    def test_file_has_1_class_identifier(self):
        file = self.project_model.files[0]
        self.assertEqual(len(file.identifier_list_model.get_filtered_identfiers(IdentifierType.Class)), 1)

    def test_file_has_correct_class_name(self):
        file = self.project_model.files[0]
        first_class_identifier = file.identifier_list_model.get_filtered_identfiers(IdentifierType.Class)[0]
        self.assertEqual(first_class_identifier.get("name"), "ExampleJavaClass")   

    def test_file_has_correct_class_name_line(self):
        file = self.project_model.files[0]
        first_class_identifier = file.identifier_list_model.get_filtered_identfiers(IdentifierType.Class)[0]
        self.assertEqual(first_class_identifier.get("line"), 3)

    def test_file_has_4_method_names(self):
        method_identifiers = self.project_model.files[0].identifier_list_model.get_filtered_identfiers(IdentifierType.Method)
        self.assertEqual(len(method_identifiers), 4)

    def test_file_has_9_dictionary_entries(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        self.assertEqual(len(dictionary), 9)

    def test_dictionary_contains_correct_class_name(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        class_identifier = dictionary.get(self.project_name)
        self.assertEqual(class_identifier.frequency, 1)
        self.assertEqual(len(class_identifier.separated_words), 3)

    def test_dictionary_contains_correct_foo_identifier(self):
        dictionary = self.project_model.files[0].identifier_dictionary_model.dictionary
        foo_identifier = dictionary.get("foo")
        self.assertEqual(foo_identifier.frequency, 2)
        self.assertEqual(len(foo_identifier.separated_words), 1)


if __name__ == '__main__':
    unittest.main()
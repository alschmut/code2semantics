import re
from antlr4 import Lexer
from fileParser.Language import Language
from fileParser.Java.JavaLexer import JavaLexer
from fileParser.Java9.Java9Lexer import Java9Lexer
from fileParser.Kotlin.KotlinLexer import KotlinLexer

class LanguageKeywords(object):
    keywords = []

    def get_all_keywords(self):
        return self.keywords

    def get_java_keywords(self):
        return LanguageKeywords.get_keywords(self, JavaLexer())

    def get_java9_keywords(self):
        return LanguageKeywords.get_keywords(self, Java9Lexer())

    def get_kotlin_keywords(self):
        return LanguageKeywords.get_keywords(self, KotlinLexer())

    def get_keywords(self, lexer: Lexer):
        return [word.replace("'", "").replace('"', '') for word in lexer.literalNames if re.search('[a-zA-Z]', word) and len(word) > 0]

    def parse_file(self, used_extensions: []):
        for extension in used_extensions:
            if extension == Language.Java.value:
                return LanguageKeywords.get_java_keywords(self)
            elif extension == Language.Kotlin.value:
                return LanguageKeywords.get_kotlin_keywords(self)



from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self, category: Category):
        storage_category = self.__find_category_by_id(category.id)
        if storage_category is None:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        topic_category = self.__find_topic_by_id(topic.id)
        if topic_category is None:
            self.topics.append(topic.id)

    def add_document(self, document: Document):
        storage_document = self.__find_document_by_id(document.id)
        if storage_document is None:
            self.documents.append(document)

    def __find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def __find_document_by_id(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def edit_category(self, category_id: int, new_name: str):
        storage_edit_category = self.__find_category_by_id(category_id)
        storage_edit_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        storage_edit_topic = self.__find_topic_by_id(topic_id)
        storage_edit_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        storage_edit_document = self.__find_document_by_id(document_id)
        storage_edit_document.edit(new_file_name)

    def delete_category(self, category_id):
        del_category = self.__find_category_by_id(category_id)
        self.categories.remove(del_category)

    def delete_topic(self, topic_id):
        del_topic = self.__find_topic_by_id(topic_id)
        self.topics.remove(del_topic)

    def delete_document(self, document_id):
        del_document = self.__find_document_by_id(document_id)
        self.documents.remove(del_document)

    def get_document(self, document_id):
        get_doc = self.__find_document_by_id(document_id)
        return get_doc

    def __repr__(self):
        return "\n".join([x.__repr__() for x in self.documents])

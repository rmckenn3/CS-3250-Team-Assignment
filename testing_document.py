import unittest
from class_document import Document

class TestAccount(unittest.TestCase):    
    def test_edit_document(self):
        doc = Document("Word", "Initial content")
        old_date = doc.date
        doc.edit("Updated content")
        self.assertEqual(doc.data, "Updated content")
        self.assertNotEqual(doc.date, old_date)

    def test_create_document_valid(self):
        doc = Document.create_document("Text", "New document")
        self.assertEqual(doc.type, "Text")
        self.assertEqual(doc.data, "New document")

    def test_create_document_invalid_type_empty(self):
        with self.assertRaises(ValueError):
            Document.create_document("", "Content")

    def test_create_document_invalid_type_nonstring(self):
        with self.assertRaises(ValueError):
            Document.create_document(123, "Content")

    def test_send_document_valid(self):
        doc = Document("PDF", "Sendable doc")
        try:
            doc.send_document("Recipient Name")
        except Exception as e:
            self.fail(f"send_document raised an exception unexpectedly: {e}")

    def test_send_document_invalid_empty(self):
        doc = Document("PDF", "Sendable doc")
        with self.assertRaises(ValueError):
            doc.send_document("")

    def test_send_document_invalid_type(self):
        doc = Document("PDF", "Sendable doc")
        with self.assertRaises(ValueError):
            doc.send_document(123)

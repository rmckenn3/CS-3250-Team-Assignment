"""
Records document data.
"""
#imports
from datetime import datetime

# Document class
class Document:
    # Static variable to track document IDs
    index = 0

    # Initialize variables for a document
    def __init__(self, type, data=None):
        Document.index += 1  # Increment the document ID
        self.id = Document.index  # Assign a unique ID to the document
        self.type = type  # Type of the document (e.g., "PDF", "Word")
        self.data = data  # Content of the document
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")  # Timestamp of the document creation
    #end __init__

    # Edit the document content
    def edit(self, data):
        self.data = data  # Update the document content
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")  # Update the timestamp
        print(f"Document {self.id} edited successfully.")
    #end edit

    # Create a new document
    @staticmethod
    def create_document(type, data):
        # Validate the document type
        if not isinstance(type, str) or not type.strip():
            raise ValueError("Document type must be a non-empty string.")
        # Create and return a new document
        document = Document(type, data)
        print(f"Document of type '{type}' created successfully.")
        return document
    #end create_document

    # Send the document to a recipient
    def send_document(self, recipient):
        # Validate the recipient
        if not isinstance(recipient, str) or not recipient.strip():
            raise ValueError("Recipient must be a non-empty string.")
        print(f"Document {self.id} sent to {recipient}.")
    #end send_document

    # Retract the document
    def retract_document(self):
        print(f"Document {self.id} retracted successfully.")
    #end retract_document
#end Document class
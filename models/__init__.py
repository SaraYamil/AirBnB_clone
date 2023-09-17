#!/usr/bin/python3

""" initializes the application's file storage"""

from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Command the reload() method to populate __objects from the JSON file
storage.reload()

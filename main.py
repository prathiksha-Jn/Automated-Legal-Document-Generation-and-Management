import os
import sys

# Add src folder to Python path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)

from document_management import DocumentManager


def generate_document():
    print("\nGenerating document...\n")

    # Existing SLM generator execute pannum
    os.system(f'python "{os.path.join(SRC_DIR, "slm_document_generator.py")}"')


def view_documents():
    manager = DocumentManager()
    manager.list_documents()


def search_documents():
    manager = DocumentManager()

    keyword = input("Enter keyword: ")

    manager.search_document(keyword)


def delete_document():
    manager = DocumentManager()

    doc_id = input("Enter Document ID: ")

    manager.delete_document(doc_id)


def statistics():
    manager = DocumentManager()

    manager.statistics()


while True:

    print("\n" + "=" * 55)
    print(" AI LEGAL DOCUMENT GENERATION SYSTEM ")
    print("=" * 55)

    print("1. Generate Legal Document")
    print("2. View Documents")
    print("3. Search Documents")
    print("4. Delete Document")
    print("5. Statistics")
    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        generate_document()

    elif choice == "2":
        view_documents()

    elif choice == "3":
        search_documents()

    elif choice == "4":
        delete_document()

    elif choice == "5":
        statistics()

    elif choice == "6":
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice")
        
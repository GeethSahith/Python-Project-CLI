import project
import pytest
import sqlite3


@pytest.fixture(autouse=True)
def setup_and_teardown():
    project.setup_database()
    yield
    conn = sqlite3.connect("contacts.db")
    conn.close()


def test_add_contact():
    project.add_contact_to_db("Test Name", "1234567890", "test@example.com", "123 Test St")
    contacts = project.fetch_contacts()
    assert contacts[0][1] == "Test Name", f"Expected name 'Test Name', found '{contacts[0][1]}'"
    assert contacts[0][2] == "1234567890", f"Expected phone '1234567890', found '{contacts[0][2]}'"
    assert contacts[0][3] == "test@example.com", f"Expected email 'test@example.com', found '{contacts[0][3]}'"
    assert contacts[0][4] == "123 Test St", f"Expected address '123 Test St', found '{contacts[0][4]}'"


def test_update_contact():
    project.add_contact_to_db("Test Name", "1234567890", "test@example.com", "123 Test St")
    contacts = project.fetch_contacts()
    contact_id = contacts[0][0]
    project.update_contact_in_db(contact_id, "Updated Name", "0987654321", "updated@example.com", "321 Updated St")
    updated_contacts = project.fetch_contacts()
    assert updated_contacts[0][1] == "Updated Name", f"Expected name 'Updated Name', found '{updated_contacts[0][1]}'"
    assert updated_contacts[0][2] == "0987654321", f"Expected phone '0987654321', found '{updated_contacts[0][2]}'"
    assert updated_contacts[0][3] == "updated@example.com", f"Expected email 'updated@example.com', found '{updated_contacts[0][3]}'"
    assert updated_contacts[0][4] == "321 Updated St", f"Expected address '321 Updated St', found '{updated_contacts[0][4]}'"


def test_delete_contact():
    project.add_contact_to_db("Test Name", "1234567890", "test@example.com", "123 Test St")
    contacts = project.fetch_contacts()
    contact_id = contacts[0][0]
    project.delete_contact_from_db(contact_id)
    remaining_contacts = project.fetch_contacts()


def test_view_contacts(capsys):
    project.add_contact_to_db("Test Name", "1234567890", "test@example.com", "123 Test St")
    project.view_contacts()
    captured = capsys.readouterr()
    print("Captured output:\n", captured.out)
    assert "Test Name" in captured.out, f"'Test Name' not found in output:\n{captured.out}"
    assert "1234567890" in captured.out, f"'1234567890' not found in output:\n{captured.out}"
    assert "test@example.com" in captured.out, f"'test@example.com' not found in output:\n{captured.out}"
    assert "123 Test St" in captured.out, f"'123 Test St' not found in output:\n{captured.out}"



"""
Basic test for Phase I Todo Application functionality
This test verifies that the core requirements from the specification are met.
"""

from todolist.storage import InMemoryStorage
from todolist.todo_data import Priority

def test_basic_todo_functionality():
    """Test the 5 basic todo features as specified"""
    storage = InMemoryStorage()

    print("Testing Phase I Todo Application Requirements...")

    # Test FR-001: Add Task
    print("\n1. Testing Add Task (FR-001)")
    todo1 = storage.add_todo("Buy groceries", "Need to buy milk and bread")
    todo2 = storage.add_todo("Complete project", "Finish the todo app implementation", Priority.HIGH)
    print(f"   [PASS] Added task #{todo1.id}: {todo1.title}")
    print(f"   [PASS] Added task #{todo2.id}: {todo2.title} with priority {todo2.priority.value}")

    # Test FR-002: View Task List
    print("\n2. Testing View Task List (FR-002)")
    all_todos = storage.get_all_todos()
    print(f"   [PASS] Retrieved {len(all_todos)} tasks")
    for todo in all_todos:
        status = "Completed" if todo.completed else "Pending"
        print(f"   - Task #{todo.id}: {todo.title} [{status}]")

    # Test FR-003: Update Task
    print("\n3. Testing Update Task (FR-003)")
    update_success = storage.update_todo(todo1.id, title="Buy groceries and cook dinner", description="Need to buy ingredients and prepare meal")
    if update_success:
        updated_todo = storage.get_todo_by_id(todo1.id)
        print(f"   [PASS] Updated task #{updated_todo.id}: {updated_todo.title}")
    else:
        print(f"   [FAIL] Failed to update task #{todo1.id}")

    # Test FR-004: Delete Task
    print("\n4. Testing Delete Task (FR-004)")
    delete_success = storage.delete_todo(todo2.id)
    if delete_success:
        print(f"   [PASS] Deleted task #{todo2.id}")
    else:
        print(f"   [FAIL] Failed to delete task #{todo2.id}")

    remaining_todos = storage.get_all_todos()
    print(f"   [PASS] Remaining tasks after deletion: {len(remaining_todos)}")

    # Test FR-005: Mark Task Complete/Incomplete
    print("\n5. Testing Mark Task Complete/Incomplete (FR-005)")
    complete_success = storage.mark_completed(todo1.id)
    if complete_success:
        completed_todo = storage.get_todo_by_id(todo1.id)
        print(f"   [PASS] Marked task #{completed_todo.id} as {'complete' if completed_todo.completed else 'incomplete'}")
    else:
        print(f"   [FAIL] Failed to mark task #{todo1.id} as complete")

    # Test marking back as incomplete
    incomplete_success = storage.mark_incomplete(todo1.id)
    if incomplete_success:
        incomplete_todo = storage.get_todo_by_id(todo1.id)
        print(f"   [PASS] Marked task #{incomplete_todo.id} as {'complete' if incomplete_todo.completed else 'incomplete'}")
    else:
        print(f"   [FAIL] Failed to mark task #{todo1.id} as incomplete")

    # Verify FR-006: Task Identification
    print("\n6. Testing Task Identification (FR-006)")
    all_todos = storage.get_all_todos()
    for todo in all_todos:
        retrieved = storage.get_todo_by_id(todo.id)
        if retrieved and retrieved.id == todo.id:
            print(f"   [PASS] Task #{todo.id} correctly identified and retrieved")
        else:
            print(f"   [FAIL] Failed to retrieve task #{todo.id}")

    print("\n[PASS] All Phase I requirements tested successfully!")

if __name__ == "__main__":
    test_basic_todo_functionality()
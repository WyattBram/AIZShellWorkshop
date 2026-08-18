from app.api import create_task, get_task


def test_create_and_get():
    created = create_task("write slides")
    task, status = get_task(created["id"])
    assert status == 200
    assert task["title"] == "write slides"


if __name__ == "__main__":
    test_create_and_get()
    print("ok")

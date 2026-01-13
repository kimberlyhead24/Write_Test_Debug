def filter_users(users, *, min_age=None, status=None):
    results = []
    for user in users:
        matches = True

        if min_age is not None and user["age"] < min_age:
            matches = False

        if status is not None and user["status"] != status:
            matches = False

        if matches:
            results.append(user)

    return results

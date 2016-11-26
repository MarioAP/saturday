# Here are some issue objects, like we use in issues and ambulancia
issues = [
    {'id': 1, 'description': "Hello", 'category': 'Dengue', 'created_by': 'Peter'},
    {'id': 2, 'description': "Hello World", 'category': 'Diabetes', 'created_by': 'Anders'},
    {'id': 3, 'description': "Bondia World", 'category': 'Drogue', 'created_by': 'Ony'},
    {'id': 4, 'description': "Bondia Mundo", 'category': 'Malaria', 'created_by': 'Ano'},
    {'id': 5, 'description': "Goodbye", 'category': 'Dengue', 'created_by': 'Nando'},
    {'id': 6, 'description': "Ate aban", 'category': 'Diabetes', 'created_by': 'Niko'},
    {'id': 7, 'description': "Ate hasoru malu", 'category': 'Drogue', 'created_by': 'Mario'},
    {'id': 8, 'description': "Hello", 'category': 'Malaria', 'created_by': 'Peter'},
    {'id': 9, 'description': "Asu", 'category': 'Ran Fakar', 'created_by': 'Anders'},
    {'id': 10, 'description': "Busa", 'category': 'PArtus', 'created_by': 'David'},
]

# Write a function that counts issues in a category
def count_category(issues, category):
    count = 0
    for issue in issues:
        if str(issue['category']) == category:
            count += 1


def test_count_category():
    assert count_category(issues, 'Dengue') == 2
    assert count_category(issues, 'Ran Fakar') == 1
    assert count_category(issues[3:9], 'Diabetes') == 1


# Write a function that counts issues created by a person
def count_created_by(issues, created_by):
    count=0
    for issue in issues:
        if created_by == str(issue['created_by']):
            count += 1
    if created_by.count(created_by) == count:
        return created_by.count(created_by)
    else:
        return count


def test_count_created_by():
    assert count_created_by(issues, 'Peter') == 2
    assert count_created_by(issues, 'David') == 1
    assert count_created_by(issues, 'David') == 1
    assert count_created_by(issues, 'Wicher') == 0


# Write a function that reurns the number of issues that are of a category AND created by someone
def count_category_and_created_by(issues, category, created_by):
    count = 0
    for issue in issues:
        if (created_by == str(issue['created_by'])) & (category == str(issue['category'])):
            count += 1
    if category.count(category) == count:
        return category.count(category)
    else:
        return count


def test_count_category_and_created_by():
    assert count_category_and_created_by(issues, 'Dengue', 'Nando') == 1
    assert count_category_and_created_by(issues, 'Dengue', 'David') == 0
    assert count_category_and_created_by(issues, 'Drogue', 'Ony') == 1
    assert count_category_and_created_by(issues, 'Drogue', 'Mario') == 1


# Write a function that reurns the number of issues that are of a category OR created by someone
def count_category_or_created_by(issues, category, created_by):
    count = 0
    for issue in issues:
        if (created_by == str(issue['created_by'])) | (category == str(issue['category'])):
            count += 1
    if category.count(category) == count:
        return category.count(category)
    else:
        return count


def test_count_category_or_created_by():
    assert count_category_or_created_by(issues, 'Dengue', 'Nando') == 2
    assert count_category_or_created_by(issues, 'Dengue', 'David') == 3
    assert count_category_or_created_by(issues, 'Drogue', 'Ony') == 2
    assert count_category_or_created_by(issues, 'Drogue', 'Mario') == 2

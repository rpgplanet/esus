from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from ella.core.models import Category
from esus.phorum.models import Table

__all__ = ("user_super", "users_usual", "table_simple")

def user_super(case):
    case.user_super = User.objects.create(
        username = "superuser",
        password = "sha1$aaa$b27189d65f3a148a8186753f3f30774182d923d5",
        first_name = "Esus",
        last_name = "master",
        is_staff = True,
        is_superuser = True,
    )

def users_usual(case):
    case.user_tester = User.objects.create(
        username = "Tester",
        password = "sha1$aaa$b27189d65f3a148a8186753f3f30774182d923d5",
        first_name = "I",
        last_name = "Robot",
        is_staff = False,
        is_superuser = False,
    )

    case.user_john_doe = User.objects.create(
        username = "JohnDoe",
        password = "sha1$aaa$b27189d65f3a148a8186753f3f30774182d923d5",
        first_name = "John",
        last_name = "Doe",
        is_staff = False,
        is_superuser = False,
    )

    case.user_staff = User.objects.create(
        username = "Gnome",
        password = "sha1$aaa$b27189d65f3a148a8186753f3f30774182d923d5",
        first_name = "Wiki",
        last_name = "Gnome",
        is_staff = True,
        is_superuser = False,
    )

def get_default_site():
    return Site.objects.get_or_create(
        name = 'localhost',
        domain = 'localhost.local'
    )[0]

def table_simple(case, table_owner=None):
    case.category = Category.objects.create(
        title = u"Category",
        slug = u"category",
        site = get_default_site(),
        tree_path = '',
        tree_parent = None
    )

    case.subcategory = Category.objects.create(
        title = u"Subcategory",
        slug = u"subcategory",
        site = get_default_site(),
        tree_path = 'subcategory',
        tree_parent = case.category
    )

    case.table = Table.objects.create(
        title = u"Table",
        owner = table_owner or case.user_tester,
        category = case.category
    )

def comment_simple(case, table=None, author=None):
    table = table or case.table
    author = author or case.user_john_doe

    case.comment_doe = case.table.add_comment(
        author = author,
        text = u"Humble user's comment"
    )

    case.comment_owner = case.table.add_comment(
        author = table.owner,
        text = u"Table 0wn3rz comment"
    )


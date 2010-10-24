# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from ella.core.models import Category

from esus.phorum.models import Table

def get_default_site():
    return Site.objects.get_or_create(
        name = 'localhost',
        domain = 'localhost.local'
    )[0]

def create_international_categories(case, commit=True):

    case.category_root = Category.objects.create(
        title = u'Root',
        slug = u'root',
        site = get_default_site(),
        tree_path = '',
        tree_parent = None
    )

    # nested Czech category
    case.category_cooking = Category.objects.create(
        title = u"Vaření",
        slug = u"vareni",
        site = get_default_site(),
        tree_path = 'vareni',
        tree_parent = case.category_root
    )

    case.category_cooking_cakes = Category.objects.create(
        title = u"Vaření dortů",
        slug = u"vareni-dortu",
        tree_parent = case.category_cooking,
        site = get_default_site(),
        tree_path = 'vareni/vareni-dortu'
    )

    # nested unicode category with multiple childrens
    case.category_languages = Category.objects.create(
        title = u"Jazyky",
        slug = u"jazyky",
        site = get_default_site(),
        tree_path = 'jazyky',
        tree_parent = case.category_root
    )

    case.category_languages_chinese = Category.objects.create(
        title = u"汉语",
        slug = u"han-yu",
        tree_parent = case.category_languages,
        site = get_default_site(),
        tree_path = 'jazyky/han-yu'
    )

    case.category_languages_chinese_confucius = Category.objects.create(
        title = u"孔夫子得哲学",
        slug = u"kong-fuzi-de-zhexue",
        tree_parent = case.category_languages_chinese,
        site = get_default_site(),
        tree_path = 'jazyky/han-yu/kong-fuzi-de-zhexue'
    )

    case.category_languages_japanese = Category.objects.create(
        title = u"日本語",
        slug = u"japanese",
        tree_parent = case.category_languages,
        site = get_default_site(),
        tree_path = 'jazyky/japanese'
    )

    case.category_languages_hindu = Category.objects.create(
        title = u"हिन्दी",
        slug = u"hindonese",
        tree_parent = case.category_languages,
        site = get_default_site(),
        tree_path = 'jazyky/jazyky'
    )

    # flat category

    case.category_sex = Category.objects.create(
        title = u"Sex",
        slug = u"sex",
        site = get_default_site(),
        tree_path = 'sex',
        tree_parent = case.category_root
    )

    if commit:
        case.transaction.commit()

def create_tables(case, commit=True):

    case.table_disciples = Table.objects.create(
        owner = User.objects.get(username="Tester"),
        title = u"孔夫子得学徒",
        slug = u"kong-fuzi-de-xuetu",
        category = case.category_languages_chinese_confucius,
        description = u"About disciples of Confucius",
    )

    case.table_admin = Table.objects.create(
        owner = User.objects.get(username="superuser"),
        title = u"Administration",
        slug = u"administration",
        category = case.category_sex,
        description = u"Discussion with administrators",
    )

    if commit:
        case.transaction.commit()

import json

from database import queries
from database.utils import execute_select_query, execute_update_query


def add_user(pool, user_id):
    execute_update_query(
        pool,
        queries.add_user,
        user_id=user_id
    )


def get_user(pool, user_id):
    result = execute_select_query(pool, queries.get_user, user_id=user_id)

    if len(result) != 1:
        return None
    return result[0]


def get_state(pool, user_id):
    results = execute_select_query(pool, queries.get_user_state, user_id=user_id)
    if len(results) == 0:
        return None
    if results[0]["state"] is None:
        return None
    return json.loads(results[0]["state"])


def set_state(pool, user_id, state):
    execute_update_query(
        pool, queries.set_user_state, user_id=user_id, state=json.dumps(state)
    )


def clear_state(pool, user_id):
    execute_update_query(pool, queries.set_user_state, user_id=user_id, state=None)


def add_film(pool, user_id, name):
    execute_update_query(pool, queries.add_film, user_id=user_id, name=name)


def get_film(pool, user_id, name):
    result = execute_select_query(pool, queries.get_film, user_id=user_id, name=name)

    if len(result) != 1:
        return None
    return result[0]


def delete_film(pool, user_id, name):
    execute_update_query(pool, queries.delete_film, user_id=user_id, name=name)


def update_film(pool, user_id, name, type, year, country, note):
    execute_update_query(pool, queries.update_film,
                         user_id=user_id, name=name, type=type, year=year, country=country, note=note)


def get_films(pool, user_id):
    return execute_select_query(pool, queries.get_films, user_id=user_id)


def get_films_order_by_name(pool, user_id):
    return execute_select_query(pool, queries.get_films_order_by_name, user_id=user_id)


def get_films_order_by_type(pool, user_id):
    return execute_select_query(pool, queries.get_films_order_by_type, user_id=user_id)


def get_films_order_by_year(pool, user_id):
    return execute_select_query(pool, queries.get_films_order_by_year, user_id=user_id)


def get_films_order_by_country(pool, user_id):
    return execute_select_query(pool, queries.get_films_order_by_country, user_id=user_id)


def get_films_filter_by_type(pool, user_id, type):
    return execute_select_query(pool, queries.get_films_filter_by_type,
                                user_id=user_id, type=type)


def get_films_filter_by_year(pool, user_id, year):
    return execute_select_query(pool, queries.get_films_filter_by_year,
                                user_id=user_id, year=year)


def get_films_filter_by_country(pool, user_id, country):
    return execute_select_query(pool, queries.get_films_filter_by_country,
                                user_id=user_id, country=country)


def get_films_order_by_name_filter_by_type(pool, user_id, type):
    return execute_select_query(pool, queries.get_films_order_by_name_filter_by_type,
                                user_id=user_id, type=type)


def get_films_order_by_type_filter_by_type(pool, user_id, type):
    return execute_select_query(pool, queries.get_films_order_by_type_filter_by_type,
                                user_id=user_id, type=type)


def get_films_order_by_year_filter_by_type(pool, user_id, type):
    return execute_select_query(pool, queries.get_films_order_by_year_filter_by_type,
                                user_id=user_id, type=type)


def get_films_order_by_country_filter_by_type(pool, user_id, type):
    return execute_select_query(pool, queries.get_films_order_by_country_filter_by_type,
                                user_id=user_id, type=type)


def get_films_order_by_name_filter_by_year(pool, user_id, year):
    return execute_select_query(pool, queries.get_films_order_by_name_filter_by_year,
                                user_id=user_id, year=year)


def get_films_order_by_type_filter_by_year(pool, user_id, year):
    return execute_select_query(pool, queries.get_films_order_by_type_filter_by_year,
                                user_id=user_id, year=year)


def get_films_order_by_year_filter_by_year(pool, user_id, year):
    return execute_select_query(pool, queries.get_films_order_by_year_filter_by_year,
                                user_id=user_id, year=year)


def get_films_order_by_country_filter_by_year(pool, user_id, year):
    return execute_select_query(pool, queries.get_films_order_by_country_filter_by_year,
                                user_id=user_id, year=year)


def get_films_order_by_name_filter_by_country(pool, user_id, country):
    return execute_select_query(pool, queries.get_films_order_by_name_filter_by_country,
                                user_id=user_id, country=country)


def get_films_order_by_type_filter_by_country(pool, user_id, country):
    return execute_select_query(pool, queries.get_films_order_by_type_filter_by_country,
                                user_id=user_id, country=country)


def get_films_order_by_year_filter_by_country(pool, user_id, country):
    return execute_select_query(pool, queries.get_films_order_by_year_filter_by_country,
                                user_id=user_id, country=country)


def get_films_order_by_country_filter_by_country(pool, user_id, country):
    return execute_select_query(pool, queries.get_films_order_by_country_filter_by_country,
                                user_id=user_id, country=country)


def get_films_check(pool, user_id):
    return execute_select_query(pool, queries.get_films_check, user_id=user_id)

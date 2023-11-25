# USERS_INFO_TABLE_PATH = "user_personal_info"
USERS_TABLE_PATH = "users"
FILMS_TABLE_PATH = "films"


add_user = f"""
    DECLARE $user_id AS Uint64;

    INSERT INTO `{USERS_TABLE_PATH}` (user_id, state)
    VALUES ($user_id, null);
"""

get_user = f"""
    DECLARE $user_id AS Int64;

    SELECT *
    FROM `{USERS_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

get_user_state = f"""
    DECLARE $user_id AS Uint64;

    SELECT state
    FROM `{USERS_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

set_user_state = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $state AS Utf8?;

    UPSERT INTO `{USERS_TABLE_PATH}` (user_id, state)
    VALUES ($user_id, $state);
"""

add_film = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;

    INSERT INTO `{FILMS_TABLE_PATH}` (user_id, name, type, year, country, note)
    VALUES ($user_id, $name, null, null, null, null);
"""

get_film = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    AND name = $name;
"""

delete_film = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;

    DELETE FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    AND name = $name;;
"""

update_film = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $name AS Utf8;
    DECLARE $type AS Utf8?;
    DECLARE $year AS Uint64?;
    DECLARE $country AS Utf8?;
    DECLARE $note AS Utf8?;

    UPSERT INTO `{FILMS_TABLE_PATH}` (user_id, name, type, year, country, note)
    VALUES ($user_id, $name, $type, $year, $country, $note);
"""


get_films = f"""
    DECLARE $user_id AS Uint64;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

get_films_order_by_name = f"""
    DECLARE $user_id AS Uint64;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    ORDER BY name ASC;
"""


get_films_order_by_type = f"""
    DECLARE $user_id AS Uint64;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    ORDER BY type ASC, name ASC;
"""


get_films_order_by_year = f"""
    DECLARE $user_id AS Uint64;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    ORDER BY year DESC, name ASC;
"""


get_films_order_by_country = f"""
    DECLARE $user_id AS Uint64;

    SELECT *
    FROM `{FILMS_TABLE_PATH}`
    WHERE user_id == $user_id
    ORDER BY country ASC, name ASC;
"""

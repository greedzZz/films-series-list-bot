# USERS_INFO_TABLE_PATH = "user_personal_info"
USERS_TABLE_PATH = "users"


get_user_state = f"""
    DECLARE $user_id AS Uint64;

    SELECT state
    FROM `{USERS_TABLE_PATH}`
    WHERE user_id == $user_id;
"""

set_user_state = f"""
    DECLARE $user_id AS Uint64;
    DECLARE $state AS Utf8?;

    UPSERT INTO `{USERS_TABLE_PATH}` (`user_id`, `state`)
    VALUES ($user_id, $state);
"""

# get_user_info = f"""
#     DECLARE $user_id AS Int64;
#
#     SELECT
#         user_id,
#         age,
#         first_name,
#         last_name
#     FROM `{USERS_INFO_TABLE_PATH}`
#     WHERE user_id == $user_id;
# """
#
# add_user_info = f"""
#     DECLARE $user_id AS Uint64;
#     DECLARE $first_name AS Utf8;
#     DECLARE $last_name AS Utf8;
#     DECLARE $age AS Uint64;
#
#     INSERT INTO `{USERS_INFO_TABLE_PATH}` (user_id, first_name, last_name, age)
#     VALUES ($user_id, $first_name, $last_name, $age);
# """
#
# delete_user_info = f"""
#     DECLARE $user_id AS Uint64;
#
#     DELETE FROM `{USERS_INFO_TABLE_PATH}`
#     WHERE user_id == $user_id;
#
#     DELETE FROM `{USERS_TABLE_PATH}`
#     WHERE user_id == $user_id;
# """
#
# update_user_info = f"""
#     DECLARE $user_id AS Uint64;
#     DECLARE $first_name AS Utf8;
#     DECLARE $last_name AS Utf8;
#     DECLARE $age AS Uint64;
#
#     REPLACE INTO `{USERS_INFO_TABLE_PATH}`
#     SELECT
#         $user_id AS user_id,
#         $first_name AS first_name,
#         $last_name AS last_name,
#         $age AS age,
#     FROM `{USERS_INFO_TABLE_PATH}`
#     WHERE user_id == $user_id;
# """
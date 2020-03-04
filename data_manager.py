import database_common
from psycopg2 import sql
import psycopg2

@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nick_name(cursor, city):
    cursor.execute("""
                    SELECT nick_name, city FROM mentors
                    WHERE city = %(city)s 
                   """,
                   {'city': city})
    nick_names = cursor.fetchall()
    return nick_names

@database_common.connection_handler
def get_carol_name(cursor,name):
    cursor.execute("""
                   SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number FROM applicants
                   WHERE first_name = %(name)s ;     
    """,
                   {'name': name})
    details = cursor.fetchall()
    return details

@database_common.connection_handler
def get_mistery_name(cursor):
    cursor.execute("""
                   SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number, email FROM applicants
                   WHERE email LIKE '%@adipiscingenimmi.edu';     
    """)
    details = cursor.fetchall()
    return details
#
# @database_common.connection_handler
# def insert_data(cursor):
#     cursor.execute("INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) \
#                     VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);")


@database_common.connection_handler
def append_to_database(cursor, table_name, user_input):
    cursor.execute(
        sql.SQL("""
                 INSERT INTO {table} (first_name, last_name, phone_number, email, application_code)
                 VALUES (%s, %s, %s, %s, %s)
                """)
            .format(table=sql.Identifier(table_name)),
        [user_input.get('first_name'),
         user_input.get('last_name'),
         user_input.get('phone_number'),
         user_input.get('email'),
         user_input.get('application_code')]
    )

@database_common.connection_handler
def show_all(cursor):
    cursor.execute("""
                    SELECT * FROM applicants 
                    Order BY id    
        """)
    details = cursor.fetchall()
    return details


@database_common.connection_handler
def update_applicant(cursor, first_name, last_name, phone_number):
        cursor.execute(f"""
                        UPDATE applicants 
                        SET phone_number = '{phone_number}'
                        WHERE first_name = '{first_name}' AND last_name = '{last_name}';
                       """)
        return f"The phone number of {first_name} {last_name}, was successfully changed to {phone_number}."


@database_common.connection_handler
def show_applicant(cursor, id):
    cursor.execute(f"""
                        SELECT * FROM applicants
                        WHERE id = '{id}';
                       """
                   )
    names = cursor.fetchall()
    return names

@database_common.connection_handler
def delete_after_emai(cursor, part_email):
    cursor.execute(f""" 
                    DELETE  FROM applicants
                    WHERE email LIKE '%{part_email}'
                    """)
    return f"Applicants with ' {part_email} ' email were deleted"
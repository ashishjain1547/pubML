from sugarcrm.client import Client

session = Client('https://suitecrmdemo.dtbc.eu/service/v4/rest.php', 
                'Demo', 
                'Demo')


modules = session.get_available_modules('Leads')

from sqlalchemy import create_engine
connection_string = "mysql+mysqlconnector://ash:password@localhost/leadsdb"
engine = create_engine(connection_string, echo=True)

with engine.connect() as connection:
    el = session.get_entry_list('Leads')['entry_list']
    offset = 0
    while len(el) > 0:
        for i in el:
            connection.execute(
                """INSERT INTO leads (first_name, last_name, phone_work) 
                VALUES ( '{0}', '{1}', '{2}' )""".format(
                    i['name_value_list']['first_name']['value'],
                    i['name_value_list']['last_name']['value'],
                    i['name_value_list']['phone_work']['value']
                )
            )

        offset += 1
        el = session.get_entry_list('Leads', offset = offset)['entry_list']

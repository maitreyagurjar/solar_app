import logging
import random
from datetime import datetime, timedelta

from sqlalchemy.exc import NoResultFound

from app import alchemy_fw
from app.controllers.countries import find_country
from app.controllers.security import create_user
from app.controllers.security import find_user
from app.errors.exceptions import AppError
from app.messages.error.controllers import INTERNAL_SERVER_ERROR, PaymentMessages
from app.messages.error.orm import ORMErrors
from app.orm.manager import get_session
from app.orm.models.countries import Country
from app.orm.models.funds import Funds

DATA_FOLDER = "data"

__author__ = "mmgurjar1@sheffield.ac.uk"
LOGGER = logging.getLogger(__name__)


def find_fund_by_id(fund_id):
    """
       Method to find the fund transaction in the database and return the Funds object

       :param fund_id: The id of the fund to be searched
       :type fund_id: int

       :return: An instance of the Fund if found, None otherwise
       :rtype: Union[:class:`app.orm.models.funds.Funds`, None]
       """
    try:
        return Funds.query.filter_by(id=fund_id).first()  # type: ignore
    except NoResultFound:
        LOGGER.error("No results found", exc_info=True)
        raise AppError(*ORMErrors.NO_RESULTS_FOUND)
    except Exception as exc:
        LOGGER.error("Could not execute query", exc_info=True)
        raise AppError(*ORMErrors.QUERY_FAILED, data=exc.args) from exc


def add_funds(username, emission_current, emission_offset, country_of_choice, donated_amount, donated_panels):
    """
       Method to find add fund data to the database for a transaction

       :param username: The username for the donor
       :type username: str

       :param emission_current: current emission of the user
       :type emission_current: float

       :param emission_offset: The emission the user is offsetting
       :type emission_offset: float

       :param country_of_choice: The name of the country to be searched
       :type country_of_choice: str

       :param donated_amount: The amount donated by the user
       :type donated_amount: float

       :param donated_panels: The number of solar panels donated by the user
       :type donated_panels: float

       :return: None
       :rtype: None
       """
    fund_data = Funds()
    user = find_user(user=username)
    fund_data.user_id = user.id
    country = find_country(country=country_of_choice)
    fund_data.country_id = country.id
    fund_data.emission_current = emission_current
    fund_data.emission_offset = emission_offset
    fund_data.donated_amount = donated_amount
    fund_data.donated_panels = donated_panels
    with get_session() as t_session:
        fund_data.save(session=t_session)


def read_funds():
    """
            Method to query the database to get the funds data

            :return: The cumulative fund data as a list
            :rtype: list
            """
    return_list = list()
    fund_dict = Funds.load_funds_as_dict(session=alchemy_fw.session)
    for key, value in fund_dict.items():
        return_list.append(value.to_dict())
    return return_list


def delete_fund_by_id(fund_id):
    """
           Method to find the fund transaction in the database and delete it

           :param fund_id: The id of the fund to be searched
           :type fund_id: int

           :return: None
           :rtype: None
           """
    try:
        fund = find_fund_by_id(fund_id=fund_id)

        if fund is None:
            raise AppError(*PaymentMessages.PAYMENT_NOT_FOUND)

        alchemy_fw.session.delete(fund)
        alchemy_fw.session.commit()

    except Exception as exc:
        raise AppError(*INTERNAL_SERVER_ERROR)


def aggregate_fund_by_country():
    """
    Method to query the data for dashboard

    :rtype: dict
    """
    results = Funds.qry_sum_by_country()

    return results


def aggregate_funds_by_date():
    """
    Method to query the data for dashboard

    :rtype: dict
    """
    results = Funds.qry_sum_by_date()

    return results


def get_landing_page_stats():
    """
    Method to query and return the statistics for the landing page

    :rtype: dict
    """
    results = Funds.qry_landing_stats()

    return results


def populate_synthetic_data():
    """
    Method to populate some synthetic users for demonstration purposes


    :return: Nothing
    :rtype: None
    """
    first_names = ["Alice", "Bob", "Carla", "Devon"]
    last_names = ["Thomas", "James", "William", "John"]
    rolelist = ["USER", "LEVEL-1", "LEVEL-2"]
    countries_dict = Country.load_countries_as_dict(session=alchemy_fw.session)

    for i in range(3):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{name}@google.com"
        role = random.choice(rolelist)
        try:
            create_user(email=email, username=name, password="Sheffield@2023", role=role)
        except Exception:
            continue

        country = random.choice(list(countries_dict.keys()))
        add_synthetic_funds(username=name,
                            country_of_choice=country)


def add_synthetic_funds(username, country_of_choice):
    sdate = datetime.now() - timedelta(3)
    edate = datetime.now() + timedelta(3)
    datelist = [sdate + timedelta(days=x) for x in range((edate - sdate).days)]

    fund_data = Funds()

    user = find_user(user=username)
    fund_data.user_id = user.id

    country = find_country(country=country_of_choice)
    fund_data.country_id = country.id
    fund_data.emission_current = random.randint(1, 1000),
    fund_data.emission_offset = random.randint(0, 500),
    fund_data.donated_amount = random.randint(50, 500),
    fund_data.donated_panels = random.randint(0, 100)

    fund_data.created_on = random.choice(datelist)

    with get_session() as t_session:
        fund_data.save(session=t_session)

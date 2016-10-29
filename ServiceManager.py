from createsend import *
from CampaignExceptions import *

# Parameters used for testing with my own account
API_key = '35e30789cd6c5e86fe4b2ee9c9951107'
API_list_id = 'ed8e5bf0ea232fb5f7a4c7f453bb08b2'
client_default_name = 'Stefanos Georgakis'
name = 'main_list'


class ServiceManager:

    def __init__(self, api_key, client):
        """
         (String) -> ServiceManager
         Constructor. Authorization is made by the API Key
         that the user must pass as an argument.
         The constructor saves the API Key and the Client ID
         in private variables in order to be used later.
        """
        self.__api_key = api_key
        self.__client_id = self.__get_client_id(client)

    def __get_client_id(self, client_name):
        """
         (String) -> String
         We make the assumption that the user can only pass
         the name of the client,
         so the function searches for the client id.
        """
        try:
            clients = CreateSend({'api_key': self.__api_key}).clients()
            for client in clients:
                if client.Name == client_name:
                    return client.ClientID
            raise NoClientFound('No Client with this name was found')
        except Unauthorized:
            print (
                'Unauthorized Error. Check the API Key: {0}'
                .format(self.__api_key)
                )
            exit(-1)
        except NoClientFound:
            print (
                'No client with this name was found. Check the name Key: {0}'
                .format(client_name)
                )
            exit(-1)

    def __get_list_id(self, list_name):
        """
         (String) -> String
         Again, we make the assumption that the user can only pass
         the name of the list that will be modified,
         so the function searches for the list id.
        """
        try:
            client = Client(
                auth={'api_key': self.__api_key},
                client_id=self.__client_id
                )
            for campaign_list in client.lists():
                if campaign_list.Name == list_name:
                    return campaign_list.ListID
            raise NoListFound('No list with this name was found')
        except NoListFound:
            print (
                'No list found with this name. Check the list name: {0}'
                .format(list_name)
                )
            exit(-1)

    def get_list(self, list_name):
        """
         (String) -> List
         The user passes as argument the list name
         and the list is returned,
         containing all the availiable information.
        """
        return List(
            auth={'api_key': self.__api_key},
            list_id=self.__get_list_id(list_name)
            )

    def get_active_subscribers(self, campaign_list):
        """
         (String) -> list
         The user passes as argument the list containing
         all the available data and the function
         returns a list containing the name and the e-mail
         of all the active subscribers in the list
         in a dictionary.
        """
        subscribers = []
        results = campaign_list.active().Results
        for i in range(len(results)):
            subscriber = {
                'name': results[i].Name,
                'e-mail': results[i].EmailAddress
                }
            subscribers.append(subscriber)
        return subscribers

    def add_subscriber(self, list_name, email, name=None):
        """
         (String, String, String) -> None
         The user passes as arguments the name of the list,
         the name of the subscriber (can be empty)
         and the email and the subscriber is added in the list.
        """
        try:
            subscriber = Subscriber(auth={'api_key': self.__api_key})
            subscriber.add(
                self.__get_list_id(list_name),
                email, name, [], True
                )
        except BadRequest:
            print 'Bad Request. Please check your parameters.'
        except ClientError:
            print 'Client error.'
        except ServerError:
            print 'Server error.'

    def delete_subscriber(self, list_name, email):
        """
         (String, String) -> None
         Thw user passes as arguments the name of the list
         and the email of the subscriber
         and the subscriber is deleted from the list.
        """
        try:
            subscriber = Subscriber(
                auth={'api_key': self.__api_key},
                list_id=self.__get_list_id(list_name),
                email_address=email
                )
            subscriber.delete()
        except BadRequest:
            print 'Bad Request. Please check your parameters.'
        except ClientError:
            print 'Client error.'
        except ServerError:
            print 'Server error.'
        except NotFound:
            print (
                'Subscriber not found. Please check the email address: {0}'
                .format(email)
                )

if __name__ == "__main__":
    service_manager = ServiceManager(API_key, client_default_name)
    l = service_manager.get_list(name)
    # service_manager.add_subscriber(name, 'Steve', 's_georgakis@yahoo.com')
    service_manager.delete_subscriber(name, "s_georgakis@yahoo.com")
    subscribers = service_manager.get_active_subscribers(l)
    for i in range(len(subscribers)):
        print 'name: {0}, e-mail: {1}'.format(
            subscribers[i]['name'],
            subscribers[i]['e-mail']
            )

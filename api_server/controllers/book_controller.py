import warnings

import connexion

from api_server.entities.ws_hotel_prob.body import Body
from api_server.entities.ws_hotel_prob.inline_response200 import InlineResponse200
from api_server.entities.ws_hotel_prob.inline_response200_probabilities import InlineResponse200Probabilities
from api_server.repository.mongo.model_repository import get_current_model

warnings.filterwarnings('ignore')


def prob_hotel_request(body):
    """
    Request hotel booking probability
    
    :param body: Object that needs to get probability
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    current_model = get_current_model()

    if current_model is not None:
        model = current_model.get_model_instance()
    else:
        raise Exception("Error loading model: Model not found...")

    if model is None:
        raise Exception("Error loading model: Model not found...")
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())

    model_request = [
        {"hotel_code": hotel_code, "nights": body.nights, "advance": body.advance, "children": body.num_children,
         "adults": body.num_adults} for hotel_code in set(body.hotels)]
    (unknown_hotel_codes, hotel_book_probability_df) = model.run_model(model_request)
    list_of_probabilities = []
    if hotel_book_probability_df is not None:
        probability_group_by = hotel_book_probability_df.groupby(['prob'])
        for booking_probability, group in probability_group_by:
            hotel_codes = [int(hotel_code) for hotel_code in group['hotel_code']]
            probability_item = InlineResponse200Probabilities(probability=booking_probability, hotels=hotel_codes)
            list_of_probabilities.append(probability_item)

    return InlineResponse200(current_model.name, list_of_probabilities, [int(item) for item in unknown_hotel_codes])

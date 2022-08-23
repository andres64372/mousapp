from models.model import Barberies, Barbers

from request_objects import Response

def get_barberies(city) -> Response:
    data = []
    if not city:
        return Response(data={"error":"City is required"}, status=400)
    barberies = Barberies.query.filter_by(city=city, status=True).all()
    for barbery in barberies:
        data.append({
            "key": barbery.id, 
            "title": barbery.title, 
            "location": barbery.location,
            "stars": barbery.stars, 
            "url": barbery.url, 
            "longitude": barbery.longitude, 
            "latitude": barbery.latitude
        })
    response = Response(data=data, status=200)
    if not data:
        response.status = 404
    return response

def get_barbers(city) -> Response:
    data = []
    if not city:
        return Response(data={"error":"City is required"}, status=400)
    barbers = Barbers.query.filter_by(city=city).all()
    for barber in barbers:
        data.append({
            "key": barber.id, 
            "title": f"{barber.first_name} {barber.last_name}", 
            "stars": barber.stars, 
            "url": barber.url, 
        })
    response = Response(data=data, status=200)
    if not data:
        response.status = 404
    return response
from django.shortcuts import render

from .models import HousePrediction
from .ml_model import predict_house


def house_predict(request):

    result = None

    if request.method == "POST":

        bedrooms = int(request.POST.get("bedrooms"))
        bathrooms = float(request.POST.get("bathrooms"))
        sqft_living = int(request.POST.get("sqft_living"))
        sqft_lot = int(request.POST.get("sqft_lot"))
        floors = float(request.POST.get("floors"))
        waterfront = int(request.POST.get("waterfront"))
        view = int(request.POST.get("view"))
        condition = int(request.POST.get("condition"))
        sqft_above = int(request.POST.get("sqft_above"))
        sqft_basement = int(request.POST.get("sqft_basement"))
        yr_built = int(request.POST.get("yr_built"))
        yr_renovated = int(request.POST.get("yr_renovated"))

        street = request.POST.get("street")
        city = request.POST.get("city")
        statezip = request.POST.get("statezip")
        country = request.POST.get("country")


        # Data for ML model
        house_data = {
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sqft_living": sqft_living,
            "sqft_lot": sqft_lot,
            "floors": floors,
            "waterfront": waterfront,
            "view": view,
            "condition": condition,
            "sqft_above": sqft_above,
            "sqft_basement": sqft_basement,
            "yr_built": yr_built,
            "yr_renovated": yr_renovated,
            "street": street,
            "city": city,
            "statezip": statezip,
            "country": country
        }


        # Prediction
        predicted_price = predict_house(house_data)


        # Save prediction in MySQL
        HousePrediction.objects.create(
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            sqft_living=sqft_living,
            sqft_lot=sqft_lot,
            floors=floors,
            waterfront=waterfront,
            view=view,
            condition=condition,
            sqft_above=sqft_above,
            sqft_basement=sqft_basement,
            yr_built=yr_built,
            yr_renovated=yr_renovated,
            street=street,
            city=city,
            statezip=statezip,
            country=country,
            predicted_price=float(predicted_price)
        )


        result = round(predicted_price, 2)


    return render(
        request,
        "Predict.html",
        {
            "result": result
        }
    )
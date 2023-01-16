from django.shortcuts import render
from django.db import transaction
from rest_framework import status as response_status
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from colors.models import Color


class RenderColorSwatches(APIView):

    @transaction.atomic()
    def post(self, request, format=None):
        data = request.data

        if type(data) is not list:
            return Response({'error':'Payload is not a list'}, response_status.HTTP_400_BAD_REQUEST)
        if len(data) != 5:
            return Response({'error': 'Payload is not 5'}, response_status.HTTP_400_BAD_REQUEST)

        return_colors = list()

        for param in data:
            color = Color(type=param['type'], input=json.dumps(param))
            if color.type not in Color.choices:
                return Response({'error': 'Type of color space [{}] is not supported'.format(color.type)},
                                response_status.HTTP_400_BAD_REQUEST)
            param.pop('type')
            color_params = tuple(p for p in param.values())
            return_colors.append('{color_space_type}{params}'
                         .format(color_space_type=color.type,
                                 params=str(color_params).replace("'", ''))
                                 )

        return Response(return_colors, response_status.HTTP_200_OK)

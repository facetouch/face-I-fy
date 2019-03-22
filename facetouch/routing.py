# from channels.routing import route
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({})
# channel_routing = [
#     route("http.request", "facetouch.consumers.http_consumer"),
# ]
# # ASGI_APPLICATION = "facetouch.routing.application"
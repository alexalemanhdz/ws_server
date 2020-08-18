from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import WebsocketConsumer

class chatConsumer(WebsocketConsumer):
  def connect(self):
    async_to_sync(self.channel_layer.group_add)(
      'chat',
      self.channel_name
    )

    self.accept()

  def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
      'chat',
      self.channel_name
    )

  def receive(self, text_data):
    text_data_json = json.loads(text_data)

    async_to_sync(self.channel_layer.group_send)(
      'chat',
      {
        'type': 'message',
        'msg': text_data_json['msg'],
        'user': text_data_json['user'],
        'hora': '12:00',
        'categoria': 6,
        'lugar': 'Calle Falsa #123',
        'prioridad': 3,
      }
    )

  def message(self, event):
    self.send(text_data=json.dumps(event))
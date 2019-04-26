import sys
import time
import json
import pygame
import pygame.camera
from io import BytesIO
from PIL import Image as pil_image

from is_wire.core import Channel, Message, Logger
from is_msgs.image_pb2 import Image

log = Logger(name="CameraGateway")

options_file = "options.json" if len(sys.argv) < 2 else sys.argv[1]
with open(options_file, 'r') as f:
    options = json.load(f)

log.info("Options loaded from '{}'\n{}", options_file, json.dumps(options))

pygame.camera.init()
devices = pygame.camera.list_cameras()
if options['device'] not in devices:
    log.critical("Device '{}' not found.", options['device'])

cam = pygame.camera.Camera(options['device'], options['resolution'])
cam.start()

while True:
    try:
        channel = Channel(options['broker_uri'])
        log.info("Connected to {}", options['broker_uri'])

        while True:
            t0 = time.time()

            img = cam.get_image()
            data = pygame.image.tostring(img, 'RGB')
            pil_img = pil_image.frombytes('RGB', options['resolution'], data)

            if options['flip_v']:
                pil_img = pil_img.transpose(pil_image.FLIP_TOP_BOTTOM)
            if options['flip_h']:
                pil_img = pil_img.transpose(pil_image.FLIP_LEFT_RIGHT)

            bdata = BytesIO()
            pil_img.save(bdata, 'jpeg')

            pb_image = Image()
            pb_image.data = bdata.getvalue()
            msg = Message(content=pb_image)
            channel.publish(msg, topic="CameraGateway.{}.Frame".format(options['camera_id']))

            dt = time.time() - t0
            log.debug("took_ms={:.1f}", dt * 1e3)
            interval = max(0.0, 1.0 / options['fps'] - dt)
            time.sleep(interval)

    except:
        pass

cam.stop()
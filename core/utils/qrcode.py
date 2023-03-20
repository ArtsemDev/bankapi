from io import BytesIO

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

from .mail import send_mail


def generate_qrcode(payload: str):
    qr = qrcode.QRCode()
    qr.add_data(payload)

    img_1 = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=RadialGradiantColorMask()
    )
    file = BytesIO()
    img_1.save(file)
    file.seek(0)
    send_mail('pratayeu.a@gmail.com', 'qrcode', 'qrcode from code', file=file.read())

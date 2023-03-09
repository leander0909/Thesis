import cv2
import numpy as np

def draw_text(img, text,
          font=cv2.FONT_HERSHEY_SIMPLEX,
          pos=(0, 0),
          font_scale=1,
          font_thickness=2,
          text_color=(0, 255, 0),
          text_color_bg=(0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size


image = 127 * np.ones((100, 200, 3), dtype="uint8")
pos = (10, 10)
w, h = draw_text(image, "leander", pos=(10, 10))
draw_text(image, "gwapo", font_scale=1, pos=(10, 20 + h), text_color_bg=(255, 0, 0))
cv2.imshow("image", image)
cv2.waitKey()
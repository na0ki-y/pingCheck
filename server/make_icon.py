import cv2
import numpy as np
def make_icon(u_name):
    img = np.full((135, 135, 3), 255, dtype=np.uint8)
    
    cv2.putText(img, u_name[0], (40, 90), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (150, 150, 150), thickness=5)
    cv2.putText(img, u_name, (35, 115), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (150, 150, 150), thickness=2)
    
    img_on=img.copy()
    cv2.rectangle(img_on, (125, 10), (10, 125), (10, 150, 10), thickness=8, lineType=cv2.LINE_4)
    img_off=img.copy()
    cv2.rectangle(img_off, (125, 10), (10, 125), (150, 150, 150), thickness=8, lineType=cv2.LINE_4)

    return {1:img_on,0:img_off}
def save_icon(icons,fig_name="sample"):
    cv2.imwrite('./icon/{}_icon_on.png'.format(fig_name), icons[1])     
    cv2.imwrite('./icon/{}_icon_off.png'.format(fig_name), icons[0])       

def load_icon(f_path):
    img=cv2.imread(f_path)
    print(img)

if __name__ == '__main__':
    icons=make_icon("Alice")
    save_icon(icons,fig_name="Alice")
    load_icon('./icon/Alice_icon_on.png')

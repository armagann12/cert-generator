import cv2

# You can add the names in the array via excel, txt etc.
names = []

def generate():
    # Params:
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontsize = 3
    thickness = 5
    color = (255, 255, 255)

    # Point where the text starts
    # Open the certificate in Paint and choose the point
    position = (1200, 785)

    for name in names:
        template = cv2.imread("cert.png")
        cv2.putText(template, name, position, font, fontsize, color, thickness, cv2.LINE_AA)
        cv2.imwrite(f'new-cert/{name}.png', template)


generate()

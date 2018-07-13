import carly

def main():
  # Ask what image the user wants to edit
  filename = input("Enter the name of the image file to edit: ")

  # Load the image from the specified file
  img = carly.load_img(filename)

  # Apply filters!
  newimg = carly.carly(filename)

  # Save the final image
  carly.save_img(newimg, "recolored.jpg")

if __name__ == '__main__':
  main()

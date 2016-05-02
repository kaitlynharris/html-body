def createPage(bodytext):
    sale = open("sale.html", "w+")

    sale.write('<html>\n\t<body>\n\t' +bodytext+ '\n\t</body>\n</html>')

    sale.close()

def main():
    createPage("Stay tuned for our amazing summer sale!")


if __name__ == '__main__':
    main()

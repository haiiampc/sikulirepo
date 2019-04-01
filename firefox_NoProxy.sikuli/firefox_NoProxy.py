#How to create a desktop shortcut
#C:\SikuliX\runsikulix.cmd -r "C:\Users\py266t\Dropbox\Official\All ATT Data\Trainings\Sikuli\Sikuli Repo\firefox_NoProxy.sikuli"


# Click on Start Button
click("1553175784070.png")

# Sleep for 1 Sec - to match delay - adjust this as needed
wait(1)
type("firefox")

type(Key.ENTER)

click("1554025644397.png")

type("about:preferences")
type(Key.ENTER)


click("1554025712811.png")
type("proxy")
click("1554025741894.png")
click(Pattern("1554025759049.png").targetOffset(-115,20))

click(Pattern("1554025904660.png").targetOffset(-111,1))


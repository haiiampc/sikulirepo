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

click("1554026190434.png")

click(Pattern("1554025904660.png").targetOffset(-111,1))

click("1554087965517.png")

# Keep the AOTS Dashboard ready for you
type("https://aotswl.it.att.com:14205/AOTSWeb/app/worklist/html/worklistControlPanel.html")
type(Key.ENTER)


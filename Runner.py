from GUI_pages import master,home,play,settings,variants,sign_in

import time


# runner that collects all GUI elements to assembles them into the interface
window = master.Window()

window.add_frame(home.Home_page(window),"Home")
window.add_frame(play.Chess_game(window,"ascii"),"Play")
window.add_frame(variants.Variants_page(window),"Variants")
window.add_frame(settings.Settings_page(window),"Settings")
window.add_frame(sign_in.Sign_in_page(window),"Sign in")


window.show_frame("Home")

window.mainloop() 

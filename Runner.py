from GUI_pages import master,home,play,settings,variants,sign_in

import time


# runner that collects all GUI elements to assembles them into the interface
window = master.Window()

window.add_frame(home.Home_page(window),"Home")
window.add_frame(play.Chess_game(window,"periodic"),"Play")
window.add_frame(variants.Variants_page(window),"Variants")
window.add_frame(settings.Settings_page(window),"Settings")
window.add_frame(sign_in.Sign_in_page(window),"Sign in")


window.show_frame("Home")

window.mainloop() 



"""
Using SIMD instructions to do bit-wise operations on multiple bit-boards at the same time.
Using Kogge-Stone Generators when calculating slider moves for multiple pieces at the same time (e.g. calculating king danger squares or pin rays).
Using the o^(o-2r) trick when calculating moves for individual sliding pieces, using the intel PSHUFB instruction to do byte-swaps on 128-bit registers to calculate diagonal attacks.

use gmpy2 for bitwise???? 1/ten mil of a second to update
V good - based in c
well kept doccumentation

"""

#pgzero
import random
TITLE = "Fnaf 1"
FPS = 240
WIDTH = 1280
HEIGHT = 720
mode = "menu"
doorL = False
lightL = False
doorR = False
lightR = False
Bonnie_here = False
Chicka_here = False
Freddy_here = False
Foxy_attacks = False
Animatronics_active = False
monik = 0
bonnie = Actor("301")
chicka = Actor("281")
bonnie_attacking = False
speed = 10
someone_walking = False
v = 0
h = 0
m = 0
n = 0.03
p = 9
r = 0
b = 0
o = 0
c = 0
f = 0
im = 0
lo = 0.1
fred = 0
freddy = 0
feddyV = 0
freddy_fazbear = 0
Feddy = 0.1
vent_sp = ["57", "60", "59"]
buttons1_sp = ["122", "124", "125", "130"]
buttons2_sp = ["134", "135", "131", "47"]
monitor_sp = ["142", "144", "132", "133", "136", "137", "138", "139", "140", "141"]
cameras_sp = ["19", "48", "66", "337", "0", "62", "67", "49", "83", "42", "41"]
cur_camera = 0

main_view = Actor("39", center = (640, 360))
vent = Actor("57", center = (689, 401))
buttons1 = Actor("122", topleft = (-170, 250))
buttons2 = Actor("134", topleft = (1320, 250))
doorLeft = Actor("102", center = (30, -400))
doorRight = Actor("118", center = (1230, -400))
nose = Actor("590", center = (517, 240))
pomehi = Actor("18")
pomehi_sp = ["12", "13", "14", "15", "16", "17", "18", "20"]
pomehi_cam = Actor("12")

monitor = Actor("142")
mon_open = Actor("420", center = (600, 680))
powerspeed = 3


#ambiences = ["ambience2.wav", "coldpresc b.wav"]
camera_navigation = Actor("164", center = (1050, 470))

cam1A = Actor("170", (1000, 300))
cam1A.point = 1
cam1B = Actor("171", (980, 350))
cam1B.point = 2
cam1C = Actor("177", (940, 450))
cam1C.point = 3
cam2A = Actor("172", (980, 560))
cam2A.point = 4
cam2B = Actor("165", (980, 598))
cam2B.point = 5
cam3 = Actor("168", (900, 550))
cam3.point = 6
cam4A = Actor("169", (1090, 560))
cam4A.point = 7
cam4B = Actor("173", (1090, 598))
cam4B.point = 8
cam5 = Actor("174", (860, 400))
cam5.point = 9
cam6 = Actor("175", (1180, 540))
cam6.point = 10
cam7 = Actor("176", (1200, 400))
cam7.point = 11
cams_buttons = [cam1A, cam1B, cam1C, cam2A, cam2B, cam3, cam4A, cam4B, cam5, cam6, cam7]
cams_buttons_sp = ["170_", "171_", "177_", "172_", "165_", "168_", "169_", "173_", "174_", "175_", "176_"]
cams_buttons_sp_n = ["170", "171", "177", "172", "165", "168", "169", "173", "174", "175", "176"]
camera_name = Actor("54", center = (1000, 250))
camera_names = ["54_", "72_", "70_", "74_", "76_", "50_", "79_", "75_", "71_", "78_", "77_"]
bonnie_screamer_sp = ["301", "300", "299", "291", "303", "293", "294", "295", "296", "297", "298", "299", "300", "301", "300", "299", "291", "303", "293", "294", "295", "296", "297", "298"]
chicka_screamer_sp = ["281", "65", "69", "216", "228", "230", "231", "232", "233", "234", "235", "236", "237", "239", "279", "239", "237", "236", "235", "234", "233", "232", "231", "230", "228"]

monitor.y = 440

office_sp = ["39", "58", "127", "225", "227"]
battery = Actor("212", center = (170, 680))
whiteColor = (255, 255, 255)
camera_outliine = Rect(20, 20, 1240, 690)
usagepic = Actor("209", center = (70, 680))
battery_sp = ["212", "213", "214", "456", "455"]
usage = 1
record_sign = Actor("7(1)", center = (60, 60))
record_sp = ["7(1)", "7_"]

power_left_pic = Actor("207", center = (103, 640))
powerleft = 100
night_pic = Actor("447", center = (1180, 90))
night = 2
AM = Actor("251", center = (1220, 50))
hour = 0

views_with_Bonnie = ["68", ["90", "120"], "205", "190", "206", "188"]
views_with_Chicka = ["224", ["215", "222"], ["217", "219"], ["221", "226"], "220"]
bonnie_step = 0
bonnie_wait_speed = 2
bonnie_seen = False
lightAllowed = True
bon_cadr = 0

chicka_step = 0
chicka_wait_speed = 3
chicka_seen = False
chicka_attacking = False
chi_cadr = 0

Freddy = Actor("307")
Freddy_attacking = False
ambiences2 = []
mouse_location = 0

old_cam_image = "19"

five = Actor("350_", center = (560, 360))
six = Actor("351_", center = (560, 440))
AM2 = Actor("352_", center = (660, 360))
star_win = False
star = Actor("Star", topleft = (100, 380))

menu_view = Actor("431")
menu_sp = ["431", "440", "441", "442"]
new_game = Actor("448_", topleft = (100, 500))
continue_button = Actor("449_", topleft = (100, 550))
arrow = Actor("450_", topleft = (20, 500))
arrow_collide = False
demo = Actor("572_", topleft = (20, 680))
start_hello = Actor("453_", center = (640, 360))
fnaf = Actor("444_", topleft = (100, 150))
feddy = Actor("304")
feddy_sp = ["304", "305"]
fredbear = 0.001
fedyy_screamer_sp = ["307", "348", "308", "309", "310", "311", "312", "313", "314", "315", "316", "317", "318", "319", "320", "321", "322", "323", "324", "325"]
def draw():
    screen.fill("black")
    if mode == "game":
        if bonnie_attacking == False and chicka_attacking == False:
            main_view.draw()
            if doorL == True:
                doorLeft.draw()
            if doorR == True:
                doorRight.draw()
            if monik == 0:
                mon_open.draw()
            nose.draw()
            vent.draw()
            buttons1.draw()
            buttons2.draw()
            if doorL == True:
                doorLeft.draw()
            if doorR == True:
                doorRight.draw()
            monitor.draw()
            battery.draw()
            usagepic.draw()
            power_left_pic.draw()
            night_pic.draw()
            AM.draw()
            screen.draw.text(str(powerleft), center = (210, 635), fontname = "fnaf_font", color = "white", bold = True)
            screen.draw.text(str(hour), center = (1175, 47), fontname = "fnaf_font", color = "white", fontsize = 32, bold = True)
            screen.draw.text(str(night), center = (1238, 86), fontname = "fnaf_font", color = "white", fontsize = 24, bold = True)
        elif bonnie_attacking == True:
            bonnie.draw()
            monitor.draw()
        elif chicka_attacking == True:
            chicka.draw()
            monitor.draw()
    elif mode == "cameras":
        screen.fill("black")
        main_view.draw()
        pomehi_cam.draw()
        camera_navigation.draw()
        if monik == 0:
            mon_open.draw()
        if main_view.image != cameras_sp[cur_camera] and someone_walking == False:
            main_view.image = cameras_sp[cur_camera]
        for j in range(len(cams_buttons)):
            cams_buttons[j].draw()
            if cams_buttons[cur_camera].image != cams_buttons_sp[cur_camera]:
                cams_buttons[cur_camera].image = cams_buttons_sp[cur_camera]
            for q in range(len(cams_buttons)):
                if cams_buttons[q] != cams_buttons[cur_camera]:
                    if cams_buttons[q].image != cams_buttons_sp_n[cams_buttons[q].point - 1]:
                        cams_buttons[q].image = cams_buttons_sp_n[cams_buttons[q].point - 1]
        screen.draw.rect(camera_outliine, whiteColor)
        battery.draw()
        record_sign.draw()
        usagepic.draw()
        screen.draw.text(str(powerleft), center = (210, 635), fontname = "fnaf_font", color = "white", bold = True)
        screen.draw.text(str(hour), center = (1175, 47), fontname = "fnaf_font", color = "white", fontsize = 32, bold = True)
        screen.draw.text(str(night), center = (1238, 86), fontname = "fnaf_font", color = "white", fontsize = 24, bold = True)
        power_left_pic.draw()
        night_pic.draw()
        AM.draw()
        camera_name.draw()
    elif mode == "lose":
        screen.fill("black")
        pomehi_cam.draw()
    elif mode == "menu":
        menu_view.draw()
        continue_button.draw()
        demo.draw()
        screen.draw.text("©Тимофей Бобров, 2022. Оригинальная игра: ©Scott Cawthon, 2014", topleft = (510, 680), color = "white", fontsize = 24)
        pomehi_cam.draw()
        new_game.draw()
        fnaf.draw()
        if arrow_collide == True:
            arrow.draw()
        if star_win == True:
            star.draw()
    elif mode == "transition":
        screen.fill("black")
        start_hello.draw()
    elif mode == "outpower":
        if Freddy_attacking == False:
            feddy.draw()
            monitor.draw()
        elif Freddy_attacking == True:
            Freddy.draw()
    elif mode == "win":
        screen.fill("black")
        five.draw()
        six.draw()
        AM2.draw()
        screen.draw.filled_rect(Rect(520, 440, 75, 82), (0, 0, 0))
        screen.draw.filled_rect(Rect(520, 182, 75, 100), (0, 0, 0))


def update(dt):
    global powerspeed, mode, powerleft, hour
    #musicbg2()
    if mode == "game":
        if lightL == True:
            if main_view.image != office_sp[1]:
                main_view.image = office_sp[1]
        if lightL == True and Bonnie_here == True:
            if main_view.image != office_sp[3]:
                main_view.image = office_sp[3]
        elif lightL == False and lightR == False:
            if main_view.image != office_sp[0]:
                main_view.image = office_sp[0]
        if lightR == True:
            if main_view.image != office_sp[2]:
                main_view.image = office_sp[2]
        if lightR == True and Chicka_here == True:
            if main_view.image != office_sp[4]:
                main_view.image = office_sp[4]
        elif lightR == False and lightL == False:
            if main_view.image != office_sp[0]:
                main_view.image = office_sp[0]
        if mouse_location < 580 and main_view.x < 810:
            main_view.x += speed
            vent.x += speed
            buttons1.x += speed
            buttons2.x += speed
            doorLeft.x += speed
            doorRight.x += speed
            nose.x += speed
        elif mouse_location > 700 and main_view.x > 490:
            main_view.x -= speed
            vent.x -= speed
            buttons1.x -= speed
            buttons2.x -= speed
            doorLeft.x -= speed
            doorRight.x -= speed
            nose.x -= speed
        feddy.x = main_view.x
    elif mode == "cameras":
        if camera_name.image != camera_names[cur_camera]:
            camera_name.image = camera_names[cur_camera]
        if mouse_location < 580 and main_view.x < 810:
            main_view.x += speed
            vent.x += speed
            buttons1.x += speed
            buttons2.x += speed
            doorLeft.x += speed
            doorRight.x += speed
            nose.x += speed
        elif mouse_location > 700 and main_view.x > 490:
            main_view.x -= speed
            vent.x -= speed
            buttons1.x -= speed
            buttons2.x -= speed
            doorLeft.x -= speed
            doorRight.x -= speed
            nose.x -= speed
        change_cam_for_Bonnie()
        change_cam_for_Chicka()
        feddy.x = main_view.x
    elif mode == "outpower":
        if mouse_location < 580 and feddy.x < 810:
            feddy.x += 3
        elif mouse_location > 700 and feddy.x > 490:
            feddy.x -= 3
    if battery.image != battery_sp[usage - 1]:
        battery.image = battery_sp[usage - 1]
    if usage == 1:
        powerspeed = 3
    elif usage == 2:
        powerspeed = 2
    elif usage == 3:
        powerspeed = 1.5
    elif usage == 4:
        powerspeed = 1.1
    elif usage == 5:
        powerspeed = 0.9
    if powerleft == -1:
        clock.schedule_unique(change_mode, 0.001)
        powerleft -= 1
    if hour == 6:
        clock.schedule_unique(change_mode, 0.0001)
        hour += 1
    


def on_mouse_move(pos):
    global mode, monik, n, mouse_location, arrow_collide
    mouse_location = pos[0]
    if mode == "game":
        n = 0.03
        if not(mon_open.collidepoint(pos)):
            monik = 0
        if mon_open.collidepoint(pos) and monik == 0:
            schedule_unique(change_mode, 0.32)
            monitor.y = 360
            monitor.image = monitor_sp[0]
            #music.play_once("put_down.wav")
            for i in range(len(monitor_sp) - 1):
                schedule(mon_anim, n)
                n += 0.03
            monik = 1
    if mode == "cameras":
        n = 0.03
        if not(mon_open.collidepoint(pos)):
            monik = 0
        if mon_open.collidepoint(pos) and monik == 0:
            schedule_unique(change_mode, 0.01)
            #music.play_once("put_down.wav")
            monitor.y = 360
            monik = 1
    if mode == "menu":
        if new_game.collidepoint(pos) and arrow_collide == False:
            arrow_collide = True
            arrow.y = new_game.y
        if not(new_game.collidepoint(pos)):
            arrow_collide = False
        
def on_mouse_down(button, pos):
    global doorL, doorR, lightL, lightR, mode, cur_camera, old_image, old_button, usage, bonnie_seen, chicka_seen
    if mode == "game":
        if (button == mouse.LEFT and buttons1.collidepoint(pos) and pos[1] < 358 and pos[1] > 300 and doorL == False):
            if lightAllowed:
                buttons1.image = buttons1_sp[1]
                doorL = True
                usage += 1
                #music.play_once("doorclose.wav")
                animate(doorLeft, tween = "decelerate", duration = 0.4, y = 435)
            #else:
                #music.play_once("error.wav")
        elif (button == mouse.LEFT and buttons1.collidepoint(pos) and pos[1] < 358 and pos[1] > 300 and doorL == True):
            buttons1.image = buttons1_sp[0]
            schedule_unique(doorLF, 0.4)
            #music.play_once("doorclose.wav")
            animate(doorLeft, tween = "accelerate", duration = 0.4, y = -400)
        elif (button == mouse.LEFT and buttons2.collidepoint(pos) and pos[1] < 358 and pos[1] > 300 and doorR == False):
            if lightAllowed:
                buttons2.image = buttons2_sp[1]
                doorR = True
                usage += 1
                #music.play_once("doorclose.wav")
                animate(doorRight, tween = "decelerate", duration = 0.4, y = 435)
            #else:
                #music.play_once("error.wav")
        elif (button == mouse.LEFT and buttons2.collidepoint(pos) and pos[1] < 358 and pos[1] > 300 and doorR == True):
            buttons2.image = buttons2_sp[0]
            schedule_unique(doorRF, 0.4)
            #music.play_once("doorclose.wav")
            animate(doorRight, tween = "accelerate", duration = 0.4, y = -400)
        elif (button == mouse.LEFT and buttons1.collidepoint(pos) and pos[1] < 437 and pos[1] > 380 and lightL == False and doorL == False):
            if lightAllowed:
                buttons1.image = buttons1_sp[2]
                usage += 1
                lightL = True
                if Bonnie_here == True and bonnie_seen == False:
                    #music.play_once("windowscare.wav")
                    bonnie_seen = True
            #else:
                #music.play_once("error.wav")

        elif (button == mouse.LEFT and buttons2.collidepoint(pos) and pos[1] < 437 and pos[1] > 380 and lightL == False and doorR == False):
            if lightAllowed:
                buttons2.image = buttons2_sp[2]
                usage += 1
                lightR = True
                if Chicka_here == True and chicka_seen == False:
                    #music.play_once("windowscare.wav")
                    chicka_seen = True
            #else:
                #music.play_once("error.wav")
        elif (button == mouse.LEFT and buttons2.collidepoint(pos) and pos[1] < 437 and pos[1] > 380 and lightL == False and doorR == True):
            if lightAllowed:
                buttons2.image = buttons2_sp[3]
                usage += 1
                lightR = True
            #else:
                #music.play_once("error.wav")
        elif (button == mouse.LEFT and buttons1.collidepoint(pos) and pos[1] < 437 and pos[1] > 380 and lightL == False and doorL == True):
            if lightAllowed:
                buttons1.image = buttons1_sp[3]
                usage += 1
                lightL = True
            #else:
                #music.play_once("error.wav")
        #if (button == mouse.LEFT and nose.collidepoint(pos)):
            #music.play_once("partyfavorraspypart_ac01__3.wav")
    elif mode == "cameras":
        for i in range(len(cams_buttons)):
            if cams_buttons[i].collidepoint(pos) and button == mouse.LEFT and cur_camera != cams_buttons[i].point - 1:
                cur_camera = cams_buttons[i].point - 1
                #music.play_once("blip3.wav")
    elif mode == "menu":
        if new_game.collidepoint(pos) and button == mouse.LEFT:
            mode = "transition"
            #music.play_once("blip3.wav")
            schedule_unique(change_mode, 3)
def on_mouse_up(button, pos):
    global lightL, lightR, usage
    if (button == mouse.LEFT and lightL == True and doorL == False):
        buttons1.image = buttons1_sp[0]
        usage -= 1
        lightL = False
    elif (button == mouse.LEFT and lightR == True and doorR == False):
        buttons2.image = buttons2_sp[0]
        usage -= 1
        lightR = False
    elif (button == mouse.LEFT and lightL == True and doorL == True):
        buttons1.image = buttons1_sp[1]
        usage -= 1
        lightL = False
    elif (button == mouse.LEFT and lightR == True and doorR == True):
        buttons2.image = buttons2_sp[1]
        usage -= 1
        lightR = False


def vent_anim():
    global v
    vent.image = vent_sp[v]
    v += 1
    if v == 3:
        v = 0
def doorLF():
    global doorL, usage
    usage -= 1
    doorL = False
def doorRF():
    global doorR, usage
    usage -= 1
    doorR = False




#def musicbg2():
    #if mode == "game" or mode == "cameras":
        #if len(ambiences2) == 0:
           # if (music.is_playing("buzz_fan_florescent2.wav") == False) and (music.is_playing("eerieambiencelargesca_mv005.wav") == False):
               # music.play_once("buzz_fan_florescent2.wav")
          #  if Animatronics_active == True:
            #    music.play_once("eerieambiencelargesca_mv005.wav")
             #   ambiences2.append("eerieambiencelargesca_mv005.wav")
      #  else:
          #  if (music.is_playing("buzz_fan_florescent2.wav") == False) and (music.is_playing("eerieambiencelargesca_mv005.wav") == False):
          #      music.play_once("buzz_fan_florescent2.wav")
   # elif mode == "menu":
      #  if (music.is_playing("darkness music.wav") == False):
       #     music.play_once("darkness music.wav")




def change_mode():
    global mode, m, usage, lightL, lightR, o, speed, bonnie_attacking, chicka_attacking, bon_cadr, chi_cadr, bonnie_step, chicka_step, Animatronics_active, doorL, doorR, lightAllowed, powerleft, hour, Bonnie_here,  bonnie_seen, Chicka_here, chicka_seen
    unschedule(vent_anim)
    unschedule(record_anim)
    unschedule(pomehi_cam_anim)
    m = 0
    o = 0
    if (lightL == True and doorL == False):
        buttons1.image = buttons1_sp[0]
        usage -= 1
        lightL = False
    elif (lightR == True and doorR == False):
        buttons2.image = buttons2_sp[0]
        usage -= 1
        lightR = False
    elif (lightL == True and doorL == True):
        buttons1.image = buttons1_sp[1]
        usage -= 1
        lightL = False
    elif (lightR == True and doorR == True):
        buttons2.image = buttons2_sp[1]
        usage -= 1
        lightR = False
    if mode == "game" and hour < 6:
        schedule_interval(record_anim, 0.5)
        schedule_interval(pomehi_cam_anim, 0.07)
        #music.set_volume(0.6)
        mode = "cameras"
        speed = 5
        usage += 1
        unschedule(mon_anim)
    elif mode == "cameras" and powerleft > -1 and hour < 6:
        usage -= 1
        animate(monitor, tween = "accel_decel", duration = 0.32, y = 1080)
        #music.set_volume(1)
        schedule_interval(vent_anim, 0.03)
        speed = 10
        mode = "game"
    elif mode == "lose":
        usage = 1
        unschedule(vent_anim)
        unschedule(timer)
        unschedule(power_minus)
        unschedule(BonnieAI)
        unschedule(ChickaAI)
        schedule(feddy_v_menu, Feddy)
        schedule_interval(pomehi_cam_anim, 0.07)
        o = 0
        speed = 10
        bonnie_attacking = False
        bon_cadr = 0
        chicka_attacking = False
        chi_cadr = 0
        usage = 1
        doorL = False
        doorLeft.y = -400
        doorR = False
        doorRight.y = -400
        Animatronics_active = False
        bonnie_step = 0
        chicka_step = 0
        lightAllowed = True
        powerleft = 100
        hour = 0
        Bonnie_here = False
        bonnie_seen = False
        Chicka_here = False
        chicka_seen = False
        buttons1.image = buttons1_sp[0]
        buttons2.image = buttons2_sp[0]
        #if "eerieambiencelargesca_mv005.wav" in ambiences2:
            #ambiences2.remove("eerieambiencelargesca_mv005.wav")
        mode = "menu"
    elif mode == "transition":
        schedule_interval(vent_anim, 0.03)
        schedule_interval(timer, 43)
        unschedule(feddy_v_menu)
        schedule(power_minus, powerspeed)
        schedule(BonnieAI, 20)
        schedule(ChickaAI, 32)
        mode = "game"
    if powerleft < 0 and hour < 6:
        powerleft -= 1
        if mode == "cameras":
            animate(monitor, tween = "accel_decel", duration = 0.32, y = 1080)
            #music.set_volume(1)
            #music.play_once("put_down.wav")
        #music.play_once("powerdown.wav")
        mode = "outpower"
        schedule(feddy_anim, 10)
    if hour >= 6:
        #music.play_once("chimes 2.wav")
        usage = 1
        unschedule(vent_anim)
        unschedule(timer)
        unschedule(power_minus)
        unschedule(BonnieAI)
        unschedule(ChickaAI)
        unschedule(feddy_v_menu)
        schedule_interval(pomehi_cam_anim, 0.07)
        o = 0
        speed = 10
        bonnie_attacking = False
        bon_cadr = 0
        chicka_attacking = False
        chi_cadr = 0
        usage = 1
        doorL = False
        doorLeft.y = -400
        doorR = False
        doorRight.y = -400
        Animatronics_active = False
        bonnie_step = 0
        chicka_step = 0
        lightAllowed = True
        powerleft = 100
        hour = 0
        Bonnie_here = False
        bonnie_seen = False
        Chicka_here = False
        chicka_seen = False
        buttons1.image = buttons1_sp[0]
        buttons2.image = buttons2_sp[0]
       # if "eerieambiencelargesca_mv005.wav" in ambiences2:
          #  ambiences2.remove("eerieambiencelargesca_mv005.wav")
        schedule_unique(hours_anim, 1)
        schedule_unique(winned, 8)
        mode = "win"

def mon_anim():
    global m
    if m == len(monitor_sp):
        m = 0
    else:
        m += 1
    monitor.image = monitor_sp[m]
def record_anim():
    global r
    record_sign.image = record_sp[r]
    r += 1
    if r == 2:
        r = 0
def pomehi_cam_anim():
    global o
    pomehi_cam.image = pomehi_sp[o]
    o += 1
    if o == len(pomehi_sp):
        o = 0
def timer():
    global hour
    hour += 1
def power_minus():
    global powerleft
    unschedule(power_minus)
    powerleft -= 1
    schedule(power_minus, powerspeed)
def BonnieAI():
    global bonnie_step, Animatronics_active, Bonnie_here, bonnie_wait_speed, old_cam_image, someone_walking
    if powerleft > 0:
        unschedule(BonnieAI)
        Animatronics_active = True
        if night == 1:
            bonnie_wait_speed = random.triangular(12, 20)
        elif night == 2:
            bonnie_wait_speed = random.triangular(5, 10)
      #  if bonnie_step > 0 and bonnie_step < 7:
           # music.play_once("deep_steps.wav")
        if bonnie_step < 7:
            main_view.image = "591"
            bonnie_step += 1
            if mode == "cameras":
                old_cam_image = main_view.image
            someone_walking = True
            clock.schedule_unique(anti_pomeh, 1.1)
            schedule(BonnieAI, bonnie_wait_speed)
        if bonnie_step == 7:
            Bonnie_here = True
            schedule_unique(bonnie_waiting_to_scream, bonnie_wait_speed)
def ChickaAI():
    global chicka_step, Animatronics_active, Chicka_here, chicka_wait_speed, old_cam_image, someone_walking
    if powerleft > 0:
        unschedule(ChickaAI)
        Animatronics_active = True
        if night == 1:
            chicka_wait_speed = random.triangular(14, 22)
        elif night == 2:
            chicka_wait_speed = random.triangular(6, 12)
        #if chicka_step > 0 and chicka_step < 9:
            #music.play_once("deep_steps.wav")
        if chicka_step < 9:
            chicka_step += 1
            if mode == "cameras":
                old_cam_image = main_view.image
            someone_walking = True
            main_view.image = "591"
            schedule_unique(anti_pomeh, 1.1)
            schedule(ChickaAI, chicka_wait_speed)
        if chicka_step == 9:
            Chicka_here = True
            schedule_unique(chicka_waiting_to_scream, random.triangular(5, chicka_wait_speed + 2))
def change_cam_for_Bonnie():
    if cur_camera == 0:
            if bonnie_step > 0:
                if main_view.image != views_with_Bonnie[0] and someone_walking == False:
                    main_view.image = views_with_Bonnie[0]
    elif cur_camera == 1:
        if chicka_step == 1 and bonnie_step == 1:
            if main_view.image != "592" and someone_walking == False:
                main_view.image = "592"
        elif bonnie_step == 1:
            if main_view.image != views_with_Bonnie[1][0] and someone_walking == False:
                main_view.image = views_with_Bonnie[1][0]
        elif bonnie_step == 2 and chicka_step != 2:
            if main_view.image != views_with_Bonnie[1][1] and someone_walking == False:
                main_view.image = views_with_Bonnie[1][1]
    elif cur_camera == 3:
        if bonnie_step == 5:
            if main_view.image != views_with_Bonnie[4] and someone_walking == False:
                main_view.image = views_with_Bonnie[4]
    elif cur_camera == 4:
        if bonnie_step == 6:
            if main_view.image != views_with_Bonnie[5] and someone_walking == False:
                main_view.image = views_with_Bonnie[5]
    elif cur_camera == 5:
        if bonnie_step == 4:
            if main_view.image != views_with_Bonnie[3] and someone_walking == False:
                main_view.image = views_with_Bonnie[3]
    elif cur_camera == 8:
        if bonnie_step == 3:
            if main_view.image != views_with_Bonnie[2] and someone_walking == False:
                main_view.image = views_with_Bonnie[2]
def change_cam_for_Chicka():
    if cur_camera == 0:
            if chicka_step > 0:
                if main_view.image != views_with_Chicka[0] and someone_walking == False:
                    main_view.image = views_with_Chicka[0]
    elif cur_camera == 1:
        if chicka_step == 1 and bonnie_step == 1:
            if main_view.image != "592" and someone_walking == False:
                main_view.image = "592"
        elif chicka_step == 1:
            if main_view.image != views_with_Chicka[1][0] and someone_walking == False:
                main_view.image = views_with_Chicka[1][0]
        elif chicka_step == 2:
            if main_view.image != views_with_Chicka[1][1] and someone_walking == False:
                main_view.image = views_with_Chicka[1][1]
    elif cur_camera == 6:
        if chicka_step == 6:
            if main_view.image != views_with_Chicka[3][0] and someone_walking == False:
                main_view.image = views_with_Chicka[3][0]
        elif chicka_step == 7:
            if main_view.image != views_with_Chicka[3][1] and someone_walking == False:
                main_view.image = views_with_Chicka[3][1]
    elif cur_camera == 7:
        if chicka_step == 8:
            if main_view.image != views_with_Chicka[4] and someone_walking == False:
                main_view.image = views_with_Chicka[4]
    elif cur_camera == 10:
        if chicka_step == 3:
            if main_view.image != views_with_Chicka[2][0] and someone_walking == False:
                main_view.image = views_with_Chicka[2][0]
        elif chicka_step == 4:
            if main_view.image != views_with_Chicka[2][1] and someone_walking == False:
                main_view.image = views_with_Chicka[2][1]
def bonnie_waiting_to_scream():
    global lightAllowed, Bonnie_here, bonnie_step, someone_walking
    if powerleft > 0:
        if doorL == True:
            #music.play_once("deep_steps.wav")
            bonnie_step = random.randint(1, 3)
            Bonnie_here = False
            someone_walking = True
            main_view.image = "591"
            schedule_unique(anti_pomeh, 1.1)
            schedule(BonnieAI, bonnie_wait_speed)
        else:
            lightAllowed = False
            schedule(bonnie_screamer, 4)
def chicka_waiting_to_scream():
    global lightAllowed, Chicka_here, chicka_step, someone_walking
    if powerleft > 0:
        if doorR == True:
            #music.play_once("deep_steps.wav")
            chicka_step = random.randint(1, 3)
            Chicka_here = False
            someone_walking = True
            main_view.image = "591"
            schedule_unique(anti_pomeh, 1.1)
            schedule(ChickaAI, chicka_wait_speed)
        else:
            lightAllowed = False
            schedule(chicka_screamer, 4)
def bonnie_screamer():
    global mode, bon_cadr, b, bonnie_attacking, usage, speed
    if powerleft > 0:
        unschedule(bonnie_screamer)
        bonnie_attacking = True
        b += 0.001
        if mode != "game":
            usage -= 1
            animate(monitor, tween = "accel_decel", duration = 0.32, y = 1080)
            #music.set_volume(1)
            speed = 10
            mode = "game"
        #if bon_cadr == 0:
            #music.play_once("xscream.wav")
        bonnie.image = bonnie_screamer_sp[bon_cadr]
        bon_cadr += 1
        schedule(bonnie_screamer, b)
        if bon_cadr == len(bonnie_screamer_sp):
            unschedule(bonnie_screamer)
            bon_cadr = 0
            mode = "lose"
            #music.play_once("static.wav")
            schedule_interval(pomehi_cam_anim, 0.07)
            schedule_unique(change_mode, 4)
            unschedule(vent_anim)
            unschedule(timer)
            unschedule(feddy_v_menu)
            unschedule(power_minus)
            unschedule(BonnieAI)
            unschedule(ChickaAI)
def chicka_screamer():
    global mode, chi_cadr, c, chicka_attacking, usage, speed
    if powerleft > 0:
        unschedule(chicka_screamer)
        chicka_attacking = True
        c += 0.001
        if mode != "game":
            usage -= 1
            animate(monitor, tween = "accel_decel", duration = 0.32, y = 1080)
            #music.set_volume(1)
            speed = 10
            mode = "game"
        #if chi_cadr == 0:
            #music.play_once("xscream.wav")
        chicka.image = chicka_screamer_sp[chi_cadr]
        chi_cadr += 1
        schedule(chicka_screamer, c)
        if chi_cadr == len(chicka_screamer_sp):
            clock.unschedule(chicka_screamer)
            chi_cadr = 0
            mode = "lose"
            #music.play_once("static.wav")
            schedule_interval(pomehi_cam_anim, 0.07)
            schedule_unique(change_mode, 4)
            unschedule(vent_anim)
            unschedule(timer)
            unschedule(feddy_v_menu)
            unschedule(power_minus)
            unschedule(BonnieAI)
            unschedule(ChickaAI)
def anti_pomeh():
    global someone_walking
    someone_walking = False
    #main_view.image = old_cam_image
def feddy_anim():
    global f, fred, freddy
    unschedule(feddy_anim)
    fred = random.choice([0.04, 0.2])
    feddy.image = feddy_sp[f]
    f += 1
    if f == 2:
        f = 0
    #if freddy == 0:
        #music.play_once("music box.wav")
    freddy += 1
    if freddy == 125:
        unschedule(feddy_anim)
        feddy.image = feddy_sp[0]
        #music.play_once("running fast3.wav")
        schedule(feddy_screamer, 3)
    else:
        schedule(feddy_anim, fred)

def feddy_v_menu():
    global feddyV, Feddy
    unschedule(feddy_v_menu)
    Feddy = random.choice([0.1, 0.6])
    feddyV = random.randint(0, len(menu_sp) - 1)
    menu_view.image = menu_sp[feddyV]
    schedule(feddy_v_menu, Feddy)


def feddy_screamer():
    global freddy_fazbear, Freddy_attacking, fredbear, mode, usage, speed
    unschedule(feddy_screamer)
    Freddy_attacking = True
    Freddy.image = fedyy_screamer_sp[freddy_fazbear]
    #if freddy_fazbear == 0:
        #music.play_once("xscream.wav")
    freddy_fazbear += 1
    fredbear += 0.001
    if freddy_fazbear == len(fedyy_screamer_sp):
            clock.unschedule(feddy_screamer)
            freddy_fazbear = 0
            mode = "lose"
           # music.play_once("static.wav")
            schedule_interval(pomehi_cam_anim, 0.07)
            schedule_unique(change_mode, 4)
            unschedule(vent_anim)
            unschedule(timer)
            unschedule(power_minus)
            unschedule(BonnieAI)
            unschedule(ChickaAI)
    else:
        schedule(feddy_screamer, fredbear)
def hours_anim():
    animate(five, tween = "linear", duration = 3, y = five.y - 80)
    animate(six, tween = "linear", duration = 3, y = six.y - 80)
def winned():
    global mode, m, usage, lightL, lightR, o, speed, bonnie_attacking, chicka_attacking, bon_cadr, chi_cadr, bonnie_step, chicka_step, Animatronics_active, doorL, doorR, lightAllowed, powerleft, hour, Bonnie_here,  bonnie_seen, Chicka_here, chicka_seen, star_win
    if mode == "win":
        usage = 1
        unschedule(vent_anim)
        unschedule(timer)
        unschedule(power_minus)
        unschedule(BonnieAI)
        unschedule(ChickaAI)
        schedule_interval(pomehi_cam_anim, 0.07)
        o = 0
        speed = 10
        bonnie_attacking = False
        bon_cadr = 0
        chicka_attacking = False
        chi_cadr = 0
        usage = 1
        doorL = False
        doorLeft.y = -400
        doorR = False
        doorRight.y = -400
        Animatronics_active = False
        bonnie_step = 0
        chicka_step = 0
        lightAllowed = True
        powerleft = 100
        hour = 0
        Bonnie_here = False
        bonnie_seen = False
        Chicka_here = False
        chicka_seen = False
        buttons1.image = buttons1_sp[0]
        buttons2.image = buttons2_sp[0]
        #if "eerieambiencelargesca_mv005.wav" in ambiences2:
            #ambiences2.remove("eerieambiencelargesca_mv005.wav")
        star_win = True
        schedule(feddy_v_menu, Feddy)
        mode = "menu"




def image_load():
    global lo
    for i in range(len(views_with_Bonnie)):
        if i == 1:
            for j in range(len(views_with_Bonnie[1])):
                menu_view.image = views_with_Bonnie[1][j]
                print("Загрузка ", lo, "%")
                lo += 0.2
        else:
            menu_view.image = views_with_Bonnie[i]
            lo += 0.2
            print("Загрузка ", lo, "%")
    for i in range(len(views_with_Chicka)):
        if i == 1 or i == 2 or i == 3:
            for j in range(len(views_with_Chicka[i])):
                menu_view.image = views_with_Chicka[i][j]
                lo += 0.2
                print("Загрузка ", lo, "%")
        else:
            menu_view.image = views_with_Chicka[i]
            lo += 0.2
            print("Загрузка ", lo, "%")
    for i in range(len(bonnie_screamer_sp)):
        lo += 0.2
        menu_view.image = bonnie_screamer_sp[i]
        print("Загрузка ", lo, "%")
    for i in range(len(chicka_screamer_sp)):
        menu_view.image = chicka_screamer_sp[i]
        lo += 0.2
        print("Загрузка ", lo, "%")
    for i in range(len(fedyy_screamer_sp)):
        menu_view.image = fedyy_screamer_sp[i]
        lo += 0.2
        print("Загрузка ", lo, "%")
    lo += 0.2
    for i in range(len(cameras_sp)):
        lo += 0.2
        menu_view.image = cameras_sp[i]
        print("Загрузка ", lo, "%")
    for i in range(len(monitor_sp)):
        lo += 0.2
        menu_view.image = monitor_sp[i]
        print("Загрузка ", lo, "%")
    for i in range(len(office_sp)):
        lo += 0.2
        menu_view.image = office_sp[i]
        print("Загрузка ", lo, "%")
    menu_view.image = "591"
    menu_view.image = "102"
    menu_view.image = "118"
    menu_view.image = "431"
    print("Загрузка завершена!")
image_load()
schedule(feddy_v_menu, 
class conf():

    token = "token"
    prefix1 = "y_"
    prefix2 = "Y_"
    name = "Yuri"
    version = "1.0L Biscuit"
    sharding = False
    cogd = "Cogs"
    type_speed = 2
    playing_msg = ["Type 'y_help' for help!","Doki Doki Literature Club","With knives!","Everlasting Summer","Yandere Simulator"]
    admins = [480580173431832577, 279732337971953664, 332271541859647498, 218085039768993803, 310496481435975693, 270057011251642368]
    test_mode = True
    
    ''' Just wanted to clear out that these hex codes bellow are for embed colours so i don't have to keep changing them in every single fucking file '''
    err = 0xC91313 # The Error Embed Colour
    norm = 0x8524c8 # The Normal or Yeah sure i did this command heres an embed color Embed Colour
    warn = 0xff42e2 # The Warning Embed Colour
    suc = 0xff42e2 # The Success i did a thing Embed Colour

    ''' Special thing for yuri as she holds the act command, on startup this list will be empty though if using act1 or 2 they will have ID's added, once again if a startup was to occur, even if there was ID's in this list, the list itself would be wiped '''
    act1 = []
    act2 = []

    ''' These are just some error quotes so i can change them really quickly instead of doing the same quote for each error in every file '''
    everyone_tag = "Hey! Do you **WANT** everyone to freak out in the chat?! Because I won't let you do that!"
    econfused = "Uh... What?"

    ''' These are for the chat trigger'''
    w_tog_on = []
    w_tog_off = [] 

    ''' Doki Bot's ID'S '''
    if test_mode is True:
        natsuki_id = 531555963908653076
        monika_id = 531556928732528670 
        sayori_id = 531554745337249792
        yuri_id = 531556397746356224

    elif test_mode is False:
        natsuki_id = 433834936450023424
        monika_id = 436351740787294208 
        sayori_id = 425696108455657472
        yuri_id = 436350586670153730

    else:
        print("fail")



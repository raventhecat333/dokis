class conf():

    token = "token"
    prefix1 = "mc_"
    prefix2 = "Mc_"
    name = "MC"
    cogd = "Cogs"
    type_speed = 2
    playing_msg = [f"Type 'mc_help' for help!","Doki Doki Literature Club","with a shoe lace","aloof","in a dark void"]
    admins = [480580173431832577, 310496481435975693, 270057011251642368]
    #         Tsumiki             IDroid              Cole 
    test_mode = False  #To enable this function, use any value that is NOT "False" Otherwise you would be disabling this function

    if test_mode is False:
        sharding = True
        version = "2.3L Club Sandwich"
    else:
        sharding = False
        version = "2.3B Club Sandwich" # Testing mode should be beta.
    #L|Launch    B|Beta


    ''' Just wanted to clear out that these hex codes bellow are for embed colours so i don't have to keep changing them in every single fucking file '''
    err = 0xC91313 # The Error Embed Colour
    norm = 0xdb7915 # The Normal or Yeah sure i did this command heres an embed color, Embed Colour
    warn = 0xff42e2 # The Warning Embed Colour
    suc = 0xff42e2 # The Success (i did a thing) Embed Colour

    ''' These are just some error quotes so i can change them really quickly instead of doing the same quote for each error in every file '''
    everyone_tag = "Did you try to make me ping everyone? Well, uhh... Nice try, I suppose."

    ''' These are for the chat trigger'''
    w_tog_on = []

    ''' Doki Bot's ID'S '''
    if test_mode is True:
        natsuki_id = 531555963908653076
        monika_id = 531556928732528670 
        sayori_id = 531554745337249792
        yuri_id = 531556397746356224
        mc_id = 596409849131171870

    else:
        natsuki_id = 433834936450023424
        monika_id = 436351740787294208 
        sayori_id = 425696108455657472
        yuri_id = 436350586670153730
        mc_id = 596407346176065552


from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3111_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_102B",         # 01, 1
        "Function_2_106F",         # 02, 2
        "Function_3_109F",         # 03, 3
        "Function_4_10CF",         # 04, 4
        "Function_5_10FF",         # 05, 5
        "Function_6_1463",         # 06, 6
        "Function_7_1644",         # 07, 7
        "Function_8_2AC0",         # 08, 8
        "Function_9_2BE9",         # 09, 9
        "Function_10_33CC",        # 0A, 10
        "Function_11_3862",        # 0B, 11
        "Function_12_3E38",        # 0C, 12
        "Function_13_46E1",        # 0D, 13
        "Function_14_4739",        # 0E, 14
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -116560, -4000, -111330, 180)
    SetChrPos(0xF7, -115650, -4000, -111150, 180)
    SetChrPos(0xF8, -116560, -4000, -110220, 180)
    SetChrPos(0xF9, -115500, -4000, -110020, 180)
    OP_8C(0xE, 0, 0)
    OP_4A(0xE, 0)
    OP_69(0x101, 0x0)
    OP_6D(-116200, -4000, -111770, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 3)), scpexpr(EXPR_END)), "loc_1F9")

    ChrTalk(    #0
        0x101,
        "#1011FHey, Faye, got a sec?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Need to talk about a job or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1006FYeah, basically.\x02\x03",

            "There's something I wanna ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Go ahead.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EC")

    label("loc_1F9")


    ChrTalk(    #6
        0xFE,
        "Oh, hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Been a while. How ya been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1001FAh, Faye!\x02\x03",

            "#1000FIt's been all right.\x01",
            "How about you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Haha, things are crazy busy here as always.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_30F")

    ChrTalk(    #10
        0xFE,
        "And thanks to you I made up with Brahm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "So, I'd say my life's pretty good at the moment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36F")

    label("loc_30F")


    ChrTalk(    #12
        0xFE,
        (
            "Lately exports have been going great,\x01",
            "so the basement factory hasn't had\x01",
            "a moment of rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F")


    ChrTalk(    #13
        0xFE,
        "You here on the job too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006FYeah, basically.\x02\x03",

            "So, there's something we'd like\x01",
            "to ask you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Oh, what's that?\x02",
    )

    CloseMessageWindow()

    label("loc_3EC")


    ChrTalk(    #16
        0x101,
        "#1015FCould you look at this?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #17
        "\x07\x05Estelle showed Faye the memo left by Bleublanc.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #18
        0xFE,
        (
            "Hmm... 'The quiet earth...chant to the\x01",
            "Goddess...' and a text string.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "...What about it?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_563")

    ChrTalk(    #20
        0x106,
        (
            "#050FWe think it's talkin' about this spot,\x01",
            "but there's parts we don't understand.\x02\x03",

            "We're askin' you since we thought\x01",
            "you might have an idea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EE")

    label("loc_563")


    ChrTalk(    #21
        0x103,
        (
            "#020FWe think it's indicating this spot, but\x01",
            "there are parts we don't understand.\x02\x03",

            "We thought we'd ask you to see if you\x01",
            "had an idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE")


    ChrTalk(    #22
        0xFE,
        (
            "So, you think this message is about the\x01",
            "basement factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "If that's the case, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002FDid you think of something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "C-Could this 'Goddess' be me?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x101,
        (
            "#1016FEr, uh...\x02\x03",

            "We're not too worried about that part.\x02\x03",

            "It's the bit below that. The number thingy.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #27
        0xFE,
        "Ah... R-Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Right, this text string...C-26D-E.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "From the look of it, I'd say\x01",
            "it's a product ID code.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1011FA product code?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #31
        0x107,
        (
            "#064FI don't know that much about them,\x01",
            "but...\x02\x03",

            "Basically it's a code attached\x01",
            "to stuff in the warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Yeah, all the things in the warehouse\x01",
            "are organized by those codes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "So, as long as you know the code we should\x01",
            "be able to call it up by using the conveyor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_993")

    label("loc_8ED")


    ChrTalk(    #34
        0xFE,
        (
            "Yeah, all the things in the warehouse\x01",
            "are organized by those codes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "So, as long as you know the code we should\x01",
            "be able to call it up by using the conveyor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_993")


    ChrTalk(    #36
        0x101,
        "#1015FSo, could you call out this number?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Sure. Wanna give it a try?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A0A")

    ChrTalk(    #38
        0x106,
        "#050FYeah, if you would.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2A")

    label("loc_A0A")


    ChrTalk(    #39
        0x103,
        "#020FPlease, if you would.\x02",
    )

    CloseMessageWindow()

    label("loc_A2A")


    ChrTalk(    #40
        0xFE,
        "No problem! Gimme one second...\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_A56():
        OP_6D(-114050, -4000, -110140, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A56)

    def lambda_A6E():

        label("loc_A6E")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_A6E")

    QueueWorkItem2(0x101, 1, lambda_A6E)

    def lambda_A7F():

        label("loc_A7F")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_A7F")

    QueueWorkItem2(0xF7, 1, lambda_A7F)

    def lambda_A90():

        label("loc_A90")

        TurnDirection(0xF8, 0xE, 400)
        OP_48()
        Jump("loc_A90")

    QueueWorkItem2(0xF8, 1, lambda_A90)

    def lambda_AA1():

        label("loc_AA1")

        TurnDirection(0xF9, 0xE, 400)
        OP_48()
        Jump("loc_AA1")

    QueueWorkItem2(0xF9, 1, lambda_AA1)
    OP_8E(0xFE, 0xFFFE3A40, 0xFFFFF060, 0xFFFE48F0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE4512, 0xFFFFF060, 0xFFFE4DC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0xE, 0x1)
    Sleep(400)

    ChrTalk(    #41
        0xFE,
        "This is Faye. Got a moment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "I'd like you to send item C-26D-E over here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Yeah, C-26D-E...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        "...Thanks, appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #45
        0xFE,
        (
            "Well, you're in luck. They said they found\x01",
            "something under that number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "They're sending it out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1004FI-It really WAS here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Seems like the person in charge over\x01",
            "there was pretty shocked too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Now, then, let's see what we get...\x02",
    )

    CloseMessageWindow()
    OP_22(0xA0, 0x1, 0x64)
    OP_76(0xFF, 0x16, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)

    def lambda_CB4():
        OP_6D(-109200, -4000, -110660, 4000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_CB4)

    def lambda_CCC():
        OP_67(0, 6920, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_CCC)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x1, 0x2)
    Sleep(600)
    OP_43(0x101, 0x1, 0x1, 0x1)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x1, 0x3)
    Sleep(1000)
    OP_43(0xF9, 0x1, 0x1, 0x4)
    WaitChrThread(0xF9, 0x1)
    OP_44(0xE, 0x0)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_43(0xE, 0x3, 0x1, 0xD)
    OP_A6(0x11)

    def lambda_D3B():

        label("loc_D3B")

        TurnDirection(0x0, 0x13, 400)
        OP_48()
        Jump("loc_D3B")

    QueueWorkItem2(0x0, 1, lambda_D3B)

    def lambda_D4C():

        label("loc_D4C")

        TurnDirection(0x1, 0x13, 400)
        OP_48()
        Jump("loc_D4C")

    QueueWorkItem2(0x1, 1, lambda_D4C)

    def lambda_D5D():

        label("loc_D5D")

        TurnDirection(0x2, 0x13, 400)
        OP_48()
        Jump("loc_D5D")

    QueueWorkItem2(0x2, 1, lambda_D5D)

    def lambda_D6E():

        label("loc_D6E")

        TurnDirection(0x3, 0x13, 400)
        OP_48()
        Jump("loc_D6E")

    QueueWorkItem2(0x3, 1, lambda_D6E)

    def lambda_D7F():

        label("loc_D7F")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_D7F")

    QueueWorkItem2(0xFE, 1, lambda_D7F)

    ChrTalk(    #50
        0x101,
        "#1011FAh, looks like it's coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Huh? The heck is that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Seems kinda familiar...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x3)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_44(0xFE, 0x1)
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        "#1007F*sigh* Thank goodness. FINALLY found it.\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #54
        0xFE,
        "Oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Isn't that the Bracer Guild...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #56
        0x101,
        "#1007F#4PYup.\x02",
    )

    CloseMessageWindow()

    def lambda_EA6():
        OP_6D(-109730, -4000, -110940, 1000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EA6)

    def lambda_EBE():
        TurnDirection(0xF7, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_EBE)
    Sleep(150)

    def lambda_ED1():
        TurnDirection(0xF8, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_ED1)
    Sleep(100)
    TurnDirection(0xF9, 0xE, 400)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F22")

    ChrTalk(    #57
        0x106,
        "#051F#4PThanks. 'Preciate the help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F44")

    label("loc_F22")


    ChrTalk(    #58
        0x103,
        "#021F#4PThanks for the help.\x02",
    )

    CloseMessageWindow()

    label("loc_F44")

    TurnDirection(0xE, 0xF7, 400)

    ChrTalk(    #59
        0xFE,
        "#1PIt was nothing, really, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "#1PWhy the heck was the guild sign in our warehouse?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1016F#4PAh...haha... Where to even start...?\x02\x03",

            "I'd sit down if I were you. It's a long story.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x142B)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_102B(): pass

    label("Function_1_102B")

    OP_8E(0xFE, 0xFFFE4580, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE53F4, 0xFFFFF060, 0xFFFE4E40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE5570, 0xFFFFF060, 0xFFFE4FBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_1_102B end

    def Function_2_106F(): pass

    label("Function_2_106F")

    OP_8E(0xFE, 0xFFFE4580, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE50D4, 0xFFFFF060, 0xFFFE4FBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_2_106F end

    def Function_3_109F(): pass

    label("Function_3_109F")

    OP_8E(0xFE, 0xFFFE424C, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE5570, 0xFFFFF060, 0xFFFE49CC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_3_109F end

    def Function_4_10CF(): pass

    label("Function_4_10CF")

    OP_8E(0xFE, 0xFFFE424C, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE50D4, 0xFFFFF060, 0xFFFE49CC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_10CF end

    def Function_5_10FF(): pass

    label("Function_5_10FF")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #62
        0x8,
        "Welcome to the central factory maintenance desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "Are you looking for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1015F#6PEr, aren't you the one looking for us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "Me looking for...? Wait.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #66
        0x8,
        "Ah, are you guys bracers, then?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1232")

    ChrTalk(    #67
        0x106,
        "#050F#3PYeah, we saw your request on the board.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1266")

    label("loc_1232")


    ChrTalk(    #68
        0x103,
        "#020F#3PYes, we saw your request on the board.\x02",
    )

    CloseMessageWindow()

    label("loc_1266")


    ChrTalk(    #69
        0x8,
        (
            "Ah, th-thanks for coming.\x01",
            "I really am in a bit of a fix.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "Anyway, do you have time to hear\x01",
            "about the problem?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_138F")

    ChrTalk(    #71
        0x101,
        (
            "#1006F#6PYeah, sure.\x02\x03",

            "To get right to it, it sounds like\x01",
            "you're looking for something.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x4)
    Call(1, 7)
    Jump("loc_1462")

    label("loc_138F")


    ChrTalk(    #72
        0x101,
        (
            "#1007F#6PAh, sorry. Actually we're kind of busy right now.\x02\x03",

            "We'll come back again when we have some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "Ah, I see. That's fine. I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Well, I'll speak to you again at that time.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x1, 0x8000)
    EventEnd(0x0)

    label("loc_1462")

    Return()

    # Function_5_10FF end

    def Function_6_1463(): pass

    label("Function_6_1463")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #75
        0x8,
        "Ah, everyone. Hello again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "Umm, so do you have time for my request yet?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1573")

    ChrTalk(    #77
        0x101,
        (
            "#1006F#6PYeah, no problem.\x02\x03",

            "To get right to it, it sounds like\x01",
            "you're looking for something.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x4)
    Call(1, 7)
    Jump("loc_1643")

    label("loc_1573")


    ChrTalk(    #78
        0x101,
        "#1007F#6PS-Sorry... We're actually still kinda busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "Hmm, guess you guys have a lot on your plate,\x01",
            "huh. Well, there's nothing for it, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "Well, please come back when\x01",
            "you do have time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_1643")

    Return()

    # Function_6_1463 end

    def Function_7_1644(): pass

    label("Function_7_1644")

    EventBegin(0x0)

    ChrTalk(    #81
        0x8,
        "Yes, I'm looking for some small orbment parts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "I was going around checking to see if\x01",
            "the equipment in here was unharmed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "And I guess they all spilled out of\x01",
            "the hole in my pocket while I was moving around.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #84
        0x101,
        (
            "#1004F#6PYou had a hole in your pocket?\x02\x03",

            "#1016FYeah, that'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        "Y-Yeah... This is totally my mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        "I knew it was starting to tear, but, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "I was freaking out when the earthquake happened,\x01",
            "and I just stuffed them in my pocket without\x01",
            "thinking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CC")

    ChrTalk(    #88
        0x108,
        (
            "#070FSo, they all fell out while\x01",
            "you were walking around...\x02\x03",

            "I see, I think we get the gist of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D6")

    label("loc_18CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(    #89
        0x105,
        (
            "#040FSo, they all fell out while\x01",
            "you were walking around...\x02\x03",

            "I see, I think we get the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D6")

    label("loc_1944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D6")

    ChrTalk(    #90
        0x104,
        (
            "#030FSo, they tumbled from your person while\x01",
            "you were walking around...\x02\x03",

            "Yes, I believe we grasp the particulars\x01",
            "of this case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A0F")

    ChrTalk(    #91
        0x106,
        "#050F#3PSo the job's to find those parts?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A45")

    label("loc_1A0F")


    ChrTalk(    #92
        0x103,
        "#020F#3PSo the job is to search for those parts?\x02",
    )

    CloseMessageWindow()

    label("loc_1A45")


    ChrTalk(    #93
        0x8,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF0")

    ChrTalk(    #94
        0x105,
        (
            "#043FBut, many orbment parts are very small.\x02\x03",

            "Searching for them sounds like\x01",
            "it could be quite the task.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C15")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B89")

    ChrTalk(    #95
        0x104,
        (
            "#032FBut, many orbment parts are delicate\x01",
            "little things.\x02\x03",

            "Seeking them out sounds like quite\x01",
            "the arduous task.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C15")

    label("loc_1B89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C15")

    ChrTalk(    #96
        0x107,
        (
            "#063FMmmm, a lot of orbment parts are really\x01",
            "tiny, though.\x02\x03",

            "Searching for them sounds kinda tough...\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C15")


    def lambda_1C1B():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1C1B)

    def lambda_1C29():
        TurnDirection(0xF8, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1C29)

    def lambda_1C37():
        TurnDirection(0xF9, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1C37)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #97
        0x101,
        (
            "#1015F#4PNow that you mention it, that does\x01",
            "sound like a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        "Yeah, I think so too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        "But fear not! I have a secret weapon for you.\x02",
    )

    CloseMessageWindow()

    def lambda_1CDE():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1CDE)

    def lambda_1CEC():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1CEC)

    def lambda_1CFA():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1CFA)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #100
        0x101,
        "#1011F#6PA secret weapon...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        "Please use this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x07\x00Received #898i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x382, 1)

    ChrTalk(    #103
        0x101,
        "#1004F#6PWhat's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "Er, so this is a bit of an oddball\x01",
            "metal detector we've invented.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "This metal detector can pinpoint specific metals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "In other words, you can select a\x01",
            "specific material to search for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1015F#6PTh-That does sound pretty incredible, but...\x02\x03",

            "#1000FWhat does it have to do with the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "A lot, of course.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F74")

    ChrTalk(    #109
        0x107,
        (
            "#060FI think I get it.\x02\x03",

            "If we set it to search just for the\x01",
            "kinds of metals used in the parts...\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A4")

    label("loc_1F74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(    #110
        0x104,
        (
            "#030FAh! I believe I understand.\x02\x03",

            "If we set it to search just for the\x01",
            "kinds of metals used in the parts...\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A4")

    label("loc_2009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A4")

    ChrTalk(    #111
        0x105,
        (
            "#040FI believe I see how this could help.\x02\x03",

            "If we set it to search just for the\x01",
            "kinds of metals used in the parts...\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2129")

    def lambda_20B8():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_20B8)

    def lambda_20C6():
        TurnDirection(0x108, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_20C6)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #112
        0x108,
        (
            "#070FI see.\x02\x03",

            "So in other words, we can set it to\x01",
            "only respond to the parts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_221A")

    label("loc_2129")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2193")

    def lambda_213D():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_213D)

    def lambda_214B():
        TurnDirection(0x105, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_214B)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #113
        0x105,
        "#040FSo it will only respond to the parts, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_221A")

    label("loc_2193")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221A")

    def lambda_21A7():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_21A7)

    def lambda_21B5():
        TurnDirection(0x104, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21B5)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #114
        0x104,
        (
            "#030FHeh, I see.\x02\x03",

            "So in other words, it can be set to\x01",
            "respond only to the parts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221A")


    ChrTalk(    #115
        0x101,
        "#1018F#4PAh, okay. So that's how it works.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "Get close to something that looks promising,\x01",
            "then use the detector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "If there are any parts, there should\x01",
            "be some kind of response.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22F0():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_22F0)

    def lambda_22FE():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_22FE)
    Sleep(30)

    def lambda_2311():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2311)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #119
        0x101,
        "#1006F#6PYeah, got it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23E3")

    ChrTalk(    #120
        0x106,
        (
            "#050F#3PThe machine'll help, but we'd like to cut\x01",
            "down the areas we have to search, too.\x02\x03",

            "When you dropped the parts, do you\x01",
            "remember where you'd been?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_248D")

    label("loc_23E3")


    ChrTalk(    #121
        0x103,
        (
            "#020F#3PThis machine will be a big help, but we'd still\x01",
            "like to cut down the areas we have to search.\x02\x03",

            "When you dropped the parts, do you\x01",
            "remember where you'd been?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_248D")


    ChrTalk(    #122
        0x8,
        (
            "Hmm... I was in the workshop on the\x01",
            "third floor and the lab on the fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "I've already checked the elevator and hallways.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "So please just focus your search\x01",
            "on those two rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25BA")

    ChrTalk(    #125
        0x106,
        (
            "#050F#3PThe third floor workshop and the lab\x01",
            "on the fourth floor.\x02\x03",

            "...All right, got it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261E")

    label("loc_25BA")


    ChrTalk(    #126
        0x103,
        (
            "#020F#3PThe third floor workshop and the lab\x01",
            "on the fourth floor, hmm?\x02\x03",

            "All right, understood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261E")


    ChrTalk(    #127
        0x8,
        (
            "I think there should be about eight\x01",
            "parts that I lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "If you could find at least half,\x01",
            "it'd be a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1000F#6PWell, we'll do our best.\x02\x03",

            "If we find any parts, we'll come back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        "I'll also ask you return the detector then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2771")

    ChrTalk(    #132
        0x106,
        (
            "#050F#3PGot any other info?\x01",
            "If not, we'll be going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D1")

    label("loc_2771")


    ChrTalk(    #133
        0x103,
        (
            "#027F#3PDo you have any other information to share\x01",
            "with us? If not, we'll begin searching.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D1")


    ChrTalk(    #134
        0x8,
        "Ah, yeah, there is one more thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "Give the Lab on the fourth floor a\x01",
            "real one-over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "I played with Antoine while\x01",
            "I was up there for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "I'm sure I probably dropped\x01",
            "a bunch of parts there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1011F#6PAntoine... You mean the cat\x01",
            "living in the factory?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        "Yeah, that Antoine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        (
            "He can be pretty cute, but this time\x01",
            "I'm kinda annoyed with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "Well, I mean, I'm not trying to blame him,\x01",
            "but I'm sure I lost a lot of parts playing\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1016F#6PAwww, now I feel kinda bad for Antoine.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A15")

    ChrTalk(    #143
        0x106,
        "#053F#3PWell, let's get movin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A39")

    label("loc_2A15")


    ChrTalk(    #144
        0x103,
        "#020F#3PWell, let's get to it.\x02",
    )

    CloseMessageWindow()

    label("loc_2A39")


    ChrTalk(    #145
        0x8,
        "Good luck! I'm counting on you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1006F#6PRoger that. We'll be back when we\x01",
            "find something.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x8)
    OP_28(0x6F, 0x1, 0x1)
    OP_28(0x6F, 0x1, 0x2)
    OP_28(0x6F, 0x1, 0x4)
    OP_A2(0xC)
    EventEnd(0x0)
    Return()

    # Function_7_1644 end

    def Function_8_2AC0(): pass

    label("Function_8_2AC0")


    ChrTalk(    #147
        0x8,
        (
            "The places I want you to search for parts\x01",
            "in are the Workshop on the third floor and\x01",
            "the Lab on the fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "Once you've found somewhere that looks\x01",
            "likely, go use the detector there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        (
            "If there are any parts in the area,\x01",
            "it should respond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        "Well, then, I'm counting on you.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_8_2AC0 end

    def Function_9_2BE9(): pass

    label("Function_9_2BE9")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #151
        0x8,
        "Hey, everyone. Did you find any parts?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2C3E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_2C57")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_2C70")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_2C89")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_2CA2")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_2CBB")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_2CD4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_2CED")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D54")

    ChrTalk(    #152
        0x101,
        (
            "#1007F#6PHmmm, no, not yet.\x02\x03",

            "We'll come back and report once\x01",
            "we've found some.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2D54")


    ChrTalk(    #153
        0x101,
        (
            "#1015F#6PIt's going okay...I guess.\x02\x03",

            "For now we'll report what we've got.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (1, "loc_2DD8"),
        (2, "loc_2E00"),
        (3, "loc_2E29"),
        (4, "loc_2E54"),
        (5, "loc_2E7E"),
        (6, "loc_2EA8"),
        (7, "loc_2ED1"),
        (8, "loc_2EFC"),
        (SWITCH_DEFAULT, "loc_2F27"),
    )


    label("loc_2DD8")


    AnonymousTalk(    #154
        "\x07\x05Reported about finding one part.\x02",
    )

    Jump("loc_2F27")

    label("loc_2E00")


    AnonymousTalk(    #155
        "\x07\x05Reported about finding two parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2E29")


    AnonymousTalk(    #156
        "\x07\x05Reported about finding three parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2E54")


    AnonymousTalk(    #157
        "\x07\x05Reported about finding four parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2E7E")


    AnonymousTalk(    #158
        "\x07\x05Reported about finding five parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2EA8")


    AnonymousTalk(    #159
        "\x07\x05Reported about finding six parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2ED1")


    AnonymousTalk(    #160
        "\x07\x05Reported about finding seven parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2EFC")


    AnonymousTalk(    #161
        "\x07\x05Reported about finding eight parts.\x02",
    )

    Jump("loc_2F27")

    label("loc_2F27")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F44")
    Return()

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_331B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_30CC")

    ChrTalk(    #162
        0x8,
        "I think you've done enough, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        "How about it? Want to keep investigating?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "End Investigation\x01",           # 0
            "Continue Investigation\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306B")

    ChrTalk(    #164
        0x101,
        (
            "#1015F#6PWell, if the client says so,\x01",
            "I guess we'll call it there.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_306B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C9")

    ChrTalk(    #165
        0x101,
        "#1006F#6PYeah, I want to keep going for a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        "Well, then, good luck\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_30C9")

    Jump("loc_3318")

    label("loc_30CC")


    ChrTalk(    #167
        0x8,
        "Ah, seems like you've found a bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        "Yeah, I think that's plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1004F#6PBut aren't there parts left?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        "Yeah, there are, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "Umm, do you want to keep investigating?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "End Investigation\x01",           # 0
            "Continue Investigation\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3245")

    ChrTalk(    #172
        0x101,
        (
            "#1015F#6PWell, if the client says so,\x01",
            "I guess we'll call it there.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_3245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3318")

    ChrTalk(    #173
        0x101,
        (
            "#1015F#6PI appreciate you saying that, but...\x02\x03",

            "#1000FI'd like to keep going a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        "Oh, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        "Well, then, good luck with the search.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#1006F#6PYeah, I'll be off then.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x1, 0x800)
    EventEnd(0x0)

    label("loc_3318")

    Jump("loc_33CB")

    label("loc_331B")


    ChrTalk(    #177
        0x8,
        (
            "Yeah, the search seems to be going\x01",
            "well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        "There's still not enough parts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1011F#6PAh, I thought so.\x02\x03",

            "#1006FWelp, I'll get back to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        "Yes, please.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_33CB")

    Return()

    # Function_9_2BE9 end

    def Function_10_33CC(): pass

    label("Function_10_33CC")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #181
        0x8,
        "Huh?! You want to cancel the job?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3803")

    ChrTalk(    #182
        0x101,
        (
            "#1007F#6P*sigh* I'm really sorry.\x02\x03",

            "I don't mean to bail out like this, but\x01",
            "we had an urgent job come up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "Oh... Well, I guess there's nothing for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "Right, understood, then.\x01",
            "I'll try to do it myself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_353E")

    ChrTalk(    #185
        0x106,
        "#552F#3PYeah, sorry.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3562")

    label("loc_353E")


    ChrTalk(    #186
        0x103,
        "#025F#3PYes, we're very sorry.\x02",
    )

    CloseMessageWindow()

    label("loc_3562")


    ChrTalk(    #187
        0x8,
        "No, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "This was my mistake to begin with,\x01",
            "so it's only natural I clean it up myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "Well, if you could give me any parts you've\x01",
            "found up till now and the detector...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1015F#6PAh, right.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #191
        "\x07\x00Handed over #898i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36DD")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #192
        "\x07\x00Handed over #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_36DD")

    OP_3F(0x382, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_375C")

    ChrTalk(    #193
        0x106,
        (
            "#050F#3PWell, then, if you'll excuse us.\x02\x03",

            "Sorry again about today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A8")

    label("loc_375C")


    ChrTalk(    #194
        0x103,
        (
            "#020F#3PWell, then, if you'll pardon us.\x02\x03",

            "Apologies again about today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A8")


    ChrTalk(    #195
        0x8,
        "No, not at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x8,
        "Take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1000F#6PYeah, later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x40)
    OP_28(0x6F, 0x4, 0x80)
    OP_28(0x6F, 0x3, 0x8)
    OP_28(0x6F, 0x1, 0x4000)
    OP_A2(0xD)
    Jump("loc_385F")

    label("loc_3803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385F")

    ChrTalk(    #198
        0x8,
        "Phew! Don't scare me like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        "Well, then, I'll be counting on you.\x02",
    )

    CloseMessageWindow()

    label("loc_385F")

    EventEnd(0x0)
    Return()

    # Function_10_33CC end

    def Function_11_3862(): pass

    label("Function_11_3862")


    ChrTalk(    #200
        0x8,
        "Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "Well, then, if you could give me any parts\x01",
            "you've found and the detector...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #202
        "\x07\x00Handed over #898i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #203
        "\x07\x00Handed over #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x382, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)

    ChrTalk(    #204
        0x8,
        "Phew! Thanks so much for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x8,
        (
            "Sorry to have taken up so much of\x01",
            "your time with my mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006F#6PNo, don't worry about it.\x02\x03",

            "#1015FBut, are you really okay with\x01",
            "ending it here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x8,
        "Haha, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        (
            "With this many parts I should\x01",
            "be okay for the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B04")

    ChrTalk(    #209
        0x107,
        (
            "#064FThat's good, but...\x02\x03",

            "#560FUm, you should really fix the hole\x01",
            "in your pocket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_3B04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B65")

    ChrTalk(    #210
        0x105,
        (
            "#047FThat's good, but...\x02\x03",

            "#045FUm, you should fix the hole in your pocket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BE2")

    label("loc_3B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BE2")

    ChrTalk(    #211
        0x104,
        (
            "#035FThat's good and all, however...\x02\x03",

            "#030FA gentleman would also consider fixing\x01",
            "the hole in his pocket.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE2")

    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #212
        0x8,
        "Ah, y-yeah, I probably should.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x8,
        "Guess I'd better find a sewing kit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1006F#6PIf you need help with that,\x01",
            "just contact the guild.\x02\x03",

            "We'll arrive any time, thread and\x01",
            "needle in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        "Ahaha, thanks for your thoughtfulness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "Anyway, thanks again for today.\x01",
            "I hope to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "...You can leave the thread\x01",
            "and needle behind, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3D89")

    ChrTalk(    #218
        0x106,
        "#051F#3PYeah, next time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DB0")

    label("loc_3D89")


    ChrTalk(    #219
        0x103,
        "#020F#3PYes, we'll see you, then.\x02",
    )

    CloseMessageWindow()

    label("loc_3DB0")


    ChrTalk(    #220
        0x101,
        "#1018F#6PWell then, later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x10)
    OP_28(0x6F, 0x1, 0x1000)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #221
        "Quest #2C[Parts Search] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    EventEnd(0x0)
    Return()

    # Function_11_3862 end

    def Function_12_3E38(): pass

    label("Function_12_3E38")


    ChrTalk(    #222
        0x8,
        "Wait, did you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        "D-Did you really find all eight parts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1011F#6POh, did we get them all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        "I-Incredible. I'd totally given up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        (
            "A-Anyway, if you could give me\x01",
            "the parts and the detector.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #227
        "\x07\x00Handed over #898i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #228
        "\x07\x00Handed over all #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x382, 1)
    OP_3F(0x233, 8)

    ChrTalk(    #229
        0x8,
        "*pheeew* Thank you so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x8,
        "I didn't think all the parts would be found.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        (
            "#1017F#6PAhaha, glad we could find them for you.\x02\x03",

            "Will this be enough for the job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x8,
        "Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x8,
        "I kind of feel bad making you go this far.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x8,
        "Ah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x8,
        "That reminds me, I had that...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)
    OP_8E(0x8, 0x2A62, 0x0, 0xFFFFF678, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    OP_8C(0x8, 315, 400)
    OP_8E(0x8, 0x21CA, 0x0, 0xFFFFFA6A, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #236
        0x8,
        "Here, please, take this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x8,
        (
            "It may not be much, but think of it as a symbol\x01",
            "of my sincere and super relieved thanks.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #238
        "\x07\x00Received #342i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x156, 1)
    Sleep(500)

    ChrTalk(    #239
        0x101,
        "#1001F#6PWow, thank you!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_425D")

    ChrTalk(    #240
        0x106,
        "#052F#3PAre you sure we can have it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4289")

    label("loc_425D")


    ChrTalk(    #241
        0x103,
        "#023F#3PAre you sure we can take this?\x02",
    )

    CloseMessageWindow()

    label("loc_4289")


    ChrTalk(    #242
        0x8,
        (
            "Yes, don't worry about it.\x01",
            "You really saved my butt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x8,
        "Anyway, thanks again for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x8,
        (
            "Thanks to you guys I should be able to\x01",
            "catch back up on the work I was doing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43A3")

    ChrTalk(    #245
        0x107,
        (
            "#064FThat's good, but...\x02\x03",

            "#560FUm, you should really fix the hole\x01",
            "in your pocket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4481")

    label("loc_43A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4404")

    ChrTalk(    #246
        0x105,
        (
            "#047FThat's good, but...\x02\x03",

            "#045FUm, you should fix the hole in your pocket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4481")

    label("loc_4404")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4481")

    ChrTalk(    #247
        0x104,
        (
            "#035FThat's good and all, however...\x02\x03",

            "#030FA gentleman would also consider fixing\x01",
            "the hole in his pocket.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4481")

    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #248
        0x8,
        "Ah, y-yeah, I probably should.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        "Guess I'd better find a sewing kit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        (
            "#1006F#6PIf you need help with that,\x01",
            "just contact the guild.\x02\x03",

            "We'll arrive any time, thread and\x01",
            "needle in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        "Ahaha, thanks for your thoughtfulness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x8,
        (
            "Anyway, thanks again for today.\x01",
            "I hope to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x8,
        (
            "...You can leave the thread\x01",
            "and needle behind, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4628")

    ChrTalk(    #254
        0x106,
        "#050F#3PYeah, next time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_464F")

    label("loc_4628")


    ChrTalk(    #255
        0x103,
        "#020F#3PYes, we'll see you, then.\x02",
    )

    CloseMessageWindow()

    label("loc_464F")


    ChrTalk(    #256
        0x101,
        "#1018F#6PWell then, later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x10)
    OP_28(0x6F, 0x1, 0x2000)
    OP_2B(0x6F, 0x1)
    OP_2C(0x6F, 0x3E8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #257
        "Quest #2C[Parts Search] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    EventEnd(0x0)
    Return()

    # Function_12_3E38 end

    def Function_13_46E1(): pass

    label("Function_13_46E1")

    OP_A1(0x13, 0x19)
    SetChrPos(0x13, -95360, -3200, -109100, 14)
    OP_72(0x19, 0x4)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)

    def lambda_470C():
        OP_8F(0xFE, 0xFFFE5304, 0xFFFFF380, 0xFFFE55D4, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_470C)
    Sleep(2500)
    OP_A2(0x11)
    WaitChrThread(0x13, 0x1)
    OP_75(0xFF, 0x16, 0x5)
    OP_23(0xA0)
    Return()

    # Function_13_46E1 end

    def Function_14_4739(): pass

    label("Function_14_4739")

    Fade(1000)
    SetChrPos(0x8, 8650, 0, -1430, 270)
    SetChrPos(0x101, 6570, 0, -1750, 90)
    SetChrPos(0xF7, 6440, 0, -780, 90)
    SetChrPos(0xF8, 5430, 0, -1590, 90)
    SetChrPos(0xF9, 5190, 0, -570, 90)
    OP_6D(7540, 0, -1430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Return()

    # Function_14_4739 end

    SaveToFile()

Try(main)

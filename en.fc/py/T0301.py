from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0301   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0301.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Joshua',                               # 9
        'Cassius',                              # 10
        'Glass',                                # 11
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = -6000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 9600,
        Unknown_04              = 875,
        Unknown_08              = 300,
        Unknown_0C              = 4,
        Unknown_0E              = 118,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00010 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT06/CH20030 ._CH',             # 02
        'ED6_DT06/CH20011 ._CH',             # 03
        'ED6_DT06/CH20021 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH00010P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT06/CH20030P._CP',             # 02
        'ED6_DT06/CH20011P._CP',             # 03
        'ED6_DT06/CH20021P._CP',             # 04
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 450,
        Y                   = -1200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262148,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_32E",          # 01, 1
        "Function_2_352",          # 02, 2
        "Function_3_46A",          # 03, 3
        "Function_4_DC4",          # 04, 4
        "Function_5_E0D",          # 05, 5
        "Function_6_E26",          # 06, 6
        "Function_7_E27",          # 07, 7
        "Function_8_1952",         # 08, 8
        "Function_9_1995",         # 09, 9
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_208")
    Jump("loc_20F")

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20F")

    label("loc_20F")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_223"),
        (2, "loc_28E"),
        (3, "loc_326"),
        (SWITCH_DEFAULT, "loc_32D"),
    )


    label("loc_223")

    ClearMapFlags(0x1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0x8, -6220, 3450, 4390, 180)
    SetChrFlags(0x8, 0x4)

    def lambda_249():

        label("loc_249")

        OP_99(0xFE, 0x0, 0x7, 0x320)
        OP_48()
        Jump("loc_249")

    QueueWorkItem2(0x8, 1, lambda_249)
    ClearChrFlags(0x8, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(7170, 3450, -16520, 0)
    OP_6C(308000, 0)
    FadeToBright(2000, 0)
    Event(0, 3)
    Jump("loc_32D")

    label("loc_28E")

    ClearMapFlags(0x1)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x102, 6021, 450, 3014, 90)
    SetChrPos(0x9, 9600, 500, -2310, 90)
    SetChrChipByIndex(0x9, 10)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xA, 10000, 1100, -3300, 0)
    ClearChrFlags(0xA, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2924, 0, -6598, 0)
    OP_6C(48000, 0)
    FadeToBright(500, 0)
    Event(0, 7)
    Jump("loc_32D")

    label("loc_326")

    Event(0, 2)
    Jump("loc_32D")

    label("loc_32D")

    Return()

    # Function_0_1FE end

    def Function_1_32E(): pass

    label("Function_1_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_33F")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_33F")

    label("loc_33F")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x30003)
    Return()

    # Function_1_32E end

    def Function_2_352(): pass

    label("Function_2_352")

    EventBegin(0x0)
    OP_22(0x1CF, 0x0, 0x64)
    OP_A2(0x390)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_3B7():
        OP_6D(4000, 0, -1000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B7)

    def lambda_3CF():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CF)

    def lambda_3E7():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E7)
    Sleep(8000)

    def lambda_3FC():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FC)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CF, 0x5F)
    Sleep(100)
    OP_24(0x1CF, 0x5A)
    Sleep(100)
    OP_24(0x1CF, 0x55)
    Sleep(100)
    OP_24(0x1CF, 0x50)
    Sleep(100)
    OP_24(0x1CF, 0x4B)
    Sleep(100)
    OP_24(0x1CF, 0x46)
    Sleep(100)
    OP_24(0x1CF, 0x3C)
    Sleep(100)
    OP_23(0x1CF)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_352 end

    def Function_3_46A(): pass

    label("Function_3_46A")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_1F(0x64, 0x12C)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0x101, 0x40)
    OP_43(0x101, 0x0, 0x0, 0x4)
    OP_43(0x8, 0x0, 0x0, 0x5)
    OP_43(0x9, 0x0, 0x0, 0x6)
    OP_6D(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    def lambda_4E5():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4E5)

    def lambda_4F5():
        OP_67(0, 5000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4F5)
    OP_6B(2940, 10000)

    def lambda_516():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_516)
    OP_6B(2800, 5000)
    Sleep(4000)
    OP_70(0x2, 0x3C)
    Sleep(500)
    OP_A2(0x0)
    OP_A5(0x0)
    OP_21()
    OP_44(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#001FNice, Joshua!\x02\x03",

            "Bravo!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_1D(0xF)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(400)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #1
        0x8,
        (
            "#010FGood morning, Estelle.\x02\x03",

            "I hope I didn't wake you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FNah, I was already up when I heard\x01",
            "you start to play.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_612():
        OP_6D(-6350, 3450, 3460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_612)
    OP_8E(0x101, 0xFFFFE7B4, 0xD7A, 0xB2C, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(100)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #3
        0x101,
        (
            "#001F#4PI can't believe how awake you are,\x01",
            "though. Even the roosters still have\x01",
            "bags under their eyes!\x02\x03",

            "Not that I mind, what with that siren\x01",
            "song of yours gently lulling this\x01",
            "beautiful woman from her slumber!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#017F#6PWhat do you mean, 'woman'? We're\x01",
            "the same age and I'm hardly a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#502FTsk, tsk, tsk.\x01",
            "How wrong you are, Joshua!\x02\x03",

            "We may be the same age, but I\x01",
            "am clearly THE woman of the\x01",
            "house.\x02\x03",

            "And that makes you something\x01",
            "like my loyal follower, wouldn't\x01",
            "you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#010FYeah, yeah.\x01",
            "How fortunate for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#009F#4PYou could at least try and sound\x01",
            "a TINY bit sincere...\x02\x03",

            "#001FIt really is a nice tune, though.\x02\x03",

            "#001FCheerful, yet somehow wistful...\x02\x03",

            "I like your other songs too,\x01",
            "of course, but this one's\x01",
            "my favorite.\x02\x03",

            "#000FEr...what's it called again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "#010F'The Whereabouts of Light.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#000FThat's right,\x01",
            "'The Whereabouts of Light.'\x02\x03",

            "#007FI wish I could play the harmonica like you,\x01",
            "Joshua.\x02\x03",

            "Sadly, it's a lot harder than it looks...\x02\x03",

            "When I try to play I just can't seem\x01",
            "to get my hands and my mouth to work\x01",
            "together... They get confused...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#019F#6PCompared to what it takes to use a staff,\x01",
            "I think the harmonica is much easier.\x02\x03",

            "#019FIt's really just a matter of concentration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#009FYou're probably right. I guess my problem\x01",
            "is just that if I don't do something that uses\x01",
            "my whole body, I start to feel drowsy.\x02\x03",

            "#009FHow should I explain it? It's like,\x01",
            "'in spring one sleeps a sleep that\x01",
            "knows no dawn.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#018FUh, I'm pretty sure that's not what you're\x01",
            "trying to say. Unless it's not just your\x01",
            "mouth and hands that are confused...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrPos(0x9, -6050, 0, -2610, 0)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #13
        0x9,
        "Man's Voice",
        "Hey, Estelle! Joshua!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(-6400, 3450, -400, 2000)

    ChrTalk(    #14
        0x101,
        "#001FMorning, Dad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#019FGood morning, Dad.\x01",
            "Is breakfast ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#080FIt's ready and waiting!\x02\x03",

            "#080FWhy don't the both of you hurry on down\x01",
            "before it gets cold?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#000FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#010FI'm on my way!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    NewScene("ED6_DT01/T0310   ._SN", 2, 0, 0)
    IdleLoop()
    Return()

    # Function_3_46A end

    def Function_4_DC4(): pass

    label("Function_4_DC4")

    OP_A6(0x0)
    SetChrPos(0x101, -1860, 3450, 930, 270)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF3D0, 0xD7A, 0x3DE, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x40)
    OP_A3(0x0)
    OP_A6(0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_4_DC4 end

    def Function_5_E0D(): pass

    label("Function_5_E0D")

    OP_A6(0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_5_E0D end

    def Function_6_E26(): pass

    label("Function_6_E26")

    Return()

    # Function_6_E26 end

    def Function_7_E27(): pass

    label("Function_7_E27")

    EventBegin(0x0)
    OP_6B(3000, 0)
    OP_43(0x102, 0x0, 0x0, 0x8)
    OP_43(0x9, 0x0, 0x0, 0x9)
    OP_22(0x1CF, 0x0, 0x64)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, 0, 0, 0, 0)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 9600, 620, -2310, 90)
    OP_A2(0x2)
    OP_6D(7500, 450, 1022, 8000)
    OP_A5(0x2)
    OP_67(0, 6710, -10000, 4000)
    OP_0D()
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_A2(0x1)
    Sleep(1000)
    OP_72(0x1, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x1, 0x0)
    OP_A5(0x1)
    OP_71(0x1, 0x800)

    ChrTalk(    #19
        0x102,
        "#015FDad...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 1)
    Sleep(300)

    ChrTalk(    #20
        0x9,
        "#080FAre you still awake, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_6D(10020, 450, -790, 2000)
    OP_A5(0x1)

    ChrTalk(    #21
        0x102,
        (
            "#010F#4PYou'd better hold off on the\x01",
            "liquor or Estelle will get mad\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#080FThis is just my way of lifting my spirits\x01",
            "before I travel. How about yourself?\x01",
            "Would you like to join me for a drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#017F#4PI'll pass. Actually, what I should\x01",
            "be saying here is: don't offer\x01",
            "alcohol to minors!\x02\x03",

            "#018FI'm not like Schera, who would\x01",
            "jump at any chance to enjoy\x01",
            "a drink or ten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#081FHa ha...that's because she holds\x01",
            "her liquor much better than I do.\x02\x03",

            "#080F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#015F#4P...\x02\x03",

            "#012FThere's something really serious\x01",
            "happening, isn't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        (
            "#085FThere's no conclusive evidence,\x01",
            "but there appears to be some sort\x01",
            "of movement within the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#014F#4PThe Erebonian Empire...?\x02\x03",

            "#012FThat sounds pretty suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#082FThis movement doesn't appear to\x01",
            "be overt, but that's what has me\x01",
            "worried...\x02\x03",

            "I intend to do a little probing at\x01",
            "the Erebonian embassy to see\x01",
            "what turns up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010F#4PUnderstood.\x01",
            "I'll make sure to look after\x01",
            "Estelle while you're gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#080FDon't you spoil that girl,\x01",
            "you hear me?\x02\x03",

            "Now that she's become a bracer,\x01",
            "she needs to learn to look after\x01",
            "herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#010F#4PEstelle will be fine.\x02\x03",

            "#010FShe's got good instincts, and despite\x01",
            "being a bit rough around the edges,\x01",
            "she has talent with the staff as well.\x02\x03",

            "#019FThere's no doubt in my mind that\x01",
            "she'll be a first-class bracer\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#085FYet at present, she's like a babe in\x01",
            "arms who knows nothing about the\x01",
            "realities of the world around her.\x02\x03",

            "#085FAt some point in time, she'll\x01",
            "have to choose which path to\x01",
            "follow in life.\x02\x03",

            "#082FAnd, Joshua...\x01",
            "The same thing can be said\x01",
            "for you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#013F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#080FIt's already been 5 years since\x01",
            "you became a part of this family,\x01",
            "hasn't it?\x02\x03",

            "How time does fly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#015F#4PYes...\x02\x03",

            "#010FIt sure does seem that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#082FAbout what you said back then...\x01",
            "Are you sure you won't reconsider\x01",
            "taking those words back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#013F#4P...\x02\x03",

            "#013FFor me, keeping my word is\x01",
            "what defines who I am.\x02\x03",

            "#013FIf I can't do something as simple\x01",
            "as that...I don't know how I could\x01",
            "live with myself.\x02\x03",

            "#015FI know this may sound stubborn,\x01",
            "but I can't take back what I said.\x01",
            "I'm sorry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#085FThere's no need to apologize...\x02\x03",

            "#080FBut, I'd like you to remember this.\x02\x03",

            "#080FNo matter what path you choose\x01",
            "in life, you can't erase these \x01",
            "past 5 years.\x02\x03",

            "#080FEstelle and I will always be\x01",
            "your family.\x02\x03",

            "#080FNo matter what may befall you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#013F#4P*nod*\x02\x03",

            "#015F...\x02\x03",

            "#010F#50WThanks...Dad...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CF, 0x5F)
    Sleep(100)
    OP_24(0x1CF, 0x5A)
    Sleep(100)
    OP_24(0x1CF, 0x55)
    Sleep(100)
    OP_24(0x1CF, 0x50)
    Sleep(100)
    OP_24(0x1CF, 0x4B)
    Sleep(100)
    OP_24(0x1CF, 0x46)
    Sleep(100)
    OP_24(0x1CF, 0x3C)
    Sleep(100)
    OP_23(0x1CF)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x4003C, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT01/T0700   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_7_E27 end

    def Function_8_1952(): pass

    label("Function_8_1952")

    OP_A6(0x1)
    OP_8E(0xFE, 0x212C, 0x1C2, 0xAB5, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0x2710, 0x1C2, 0xFFFFFF56, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 400)
    OP_A3(0x1)
    Return()

    # Function_8_1952 end

    def Function_9_1995(): pass

    label("Function_9_1995")

    OP_A6(0x2)
    OP_6C(315000, 8000)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_9_1995 end

    SaveToFile()

Try(main)

from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Butler Dario',                         # 9
        'Steward Gilbert',                      # 10
        'Cup',                                  # 11
        'Cup',                                  # 12
        'Pot',                                  # 13
        'Target Camera',                        # 14
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


    AddCharChip(
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH02420 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH02420P._CP',             # 01
    )

    DeclNpc(
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67820,
        Z                   = -30,
        Y                   = -5200,
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
        X                   = 35510,
        Z                   = 750,
        Y                   = 27280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35450,
        Z                   = 750,
        Y                   = 26890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638400,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35490,
        Z                   = 750,
        Y                   = 26520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703936,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -475,
        TriggerZ            = 0,
        TriggerY            = 3173,
        TriggerRange        = 800,
        ActorX              = -475,
        ActorZ              = 800,
        ActorY              = 3173,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -63800,
        TriggerZ            = 0,
        TriggerY            = 50790,
        TriggerRange        = 900,
        ActorX              = -63800,
        ActorZ              = -300,
        ActorY              = 50790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -62370,
        TriggerZ            = 0,
        TriggerY            = -43110,
        TriggerRange        = 500,
        ActorX              = -62370,
        ActorZ              = 2000,
        ActorY              = -43110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59500,
        TriggerZ            = 250,
        TriggerY            = -36760,
        TriggerRange        = 800,
        ActorX              = -59500,
        ActorZ              = 1250,
        ActorY              = -36760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_220",          # 01, 1
        "Function_2_234",          # 02, 2
        "Function_3_3B1",          # 03, 3
        "Function_4_422",          # 04, 4
        "Function_5_F26",          # 05, 5
        "Function_6_1021",         # 06, 6
        "Function_7_102B",         # 07, 7
        "Function_8_1035",         # 08, 8
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_21F")

    Return()

    # Function_0_20A end

    def Function_1_220(): pass

    label("Function_1_220")

    OP_72(0x1010, 0x0)
    ExitThread()
    OP_72(0x810, 0x0)
    ExitThread()
    OP_6F(0x10, 360)
    Return()

    # Function_1_220 end

    def Function_2_234(): pass

    label("Function_2_234")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_259")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_39B")

    label("loc_259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_272")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_39B")

    label("loc_272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_39B")

    label("loc_28B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_39B")

    label("loc_2A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_39B")

    label("loc_2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_39B")

    label("loc_2D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_39B")

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_39B")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_39B")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_39B")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_39B")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_39B")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_39B")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_39B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_39B")

    label("loc_3B0")

    Return()

    # Function_2_234 end

    def Function_3_3B1(): pass

    label("Function_3_3B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_421")
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFEAA2, 0x3E8, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_8C(0xFE, 90, 400)
    Sleep(3500)
    OP_8E(0xFE, 0xFFFFEE6C, 0x0, 0xFFFFF204, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(4500)
    Jump("Function_3_3B1")

    label("loc_421")

    Return()

    # Function_3_3B1 end

    def Function_4_422(): pass

    label("Function_4_422")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(72840, -2000, -12380, 0)
    OP_67(0, 4840, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 68100, 0, -9000, 90)
    SetChrPos(0x11, 66600, -30, -7100, 90)
    SetChrPos(0x105, 70000, -3750, -14500, 90)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)

    def lambda_4C2():
        OP_6D(68060, -30, -7600, 6800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_4C2)

    def lambda_4DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4DA)

    def lambda_4EC():
        OP_8E(0xFE, 0x11D8C, 0xFFFFF830, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4EC)
    WaitChrThread(0x105, 0x1)

    def lambda_50C():
        OP_8E(0xFE, 0x11D8C, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_50C)
    WaitChrThread(0x105, 0x1)

    def lambda_52C():
        OP_8E(0xFE, 0x111AC, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52C)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x105,
        (
            "#543F#12PUmm... Excuse me.\x02\x03",

            "#040FI'm a student of Jenis Royal Academy\x01",
            "here on Student Council business.\x02\x03",

            "Would it be possible for me to meet with\x01",
            "Mayor Dalmore?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#5PI'm afraid not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        "#5PHe's currently not in, you see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#5PIf your business isn't urgent, might I recommend\x01",
            "coming back another day?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(    #4
        0x11,
        "Voice",
        "#2PI'll be happy to hear what you have to say.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(1000)
    SetChrPos(0x11, 65500, -30, -7100, 90)

    def lambda_6DF():

        label("loc_6DF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6DF")

    QueueWorkItem2(0x105, 2, lambda_6DF)

    def lambda_6F0():

        label("loc_6F0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6F0")

    QueueWorkItem2(0x10, 2, lambda_6F0)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    Sleep(300)

    def lambda_716():
        OP_8E(0xFE, 0x109DC, 0xFFFFFFE2, 0xFFFFE444, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_716)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_72(0xB, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_70(0xB, 0x0)
    Sleep(300)
    OP_8C(0x11, 130, 400)
    Sleep(500)
    OP_44(0x105, 0x2)
    OP_44(0x11, 0x2)

    NpcTalk(    #5
        0x11,
        "Eloquent Young Man",
        (
            "#678F#5PI'm the mayor's steward, Gilbert, and I act as\x01",
            "his representative during his absence.\x02\x03",

            "#670FSo you're a student of Jenis Royal Academy,\x01",
            "are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#044F#6PThat's correct, sir.\x02\x03",

            "#040FI've come to deliver an envelope from the\x01",
            "Student Council to the mayor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Kloe handed over the envelope to the steward.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #8
        0x11,
        (
            "#672F#5PAh, I see. It's the list of all the academy's\x01",
            "students for the current year.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x11,
        (
            "#670F#5PAs you know, students generally live in dorms...\x01",
            "and obviously, there are large numbers of them\x01",
            "coming and going year after year.\x02\x03",

            "It makes keeping track of all the residents of the\x01",
            "region that much easier when the school submits\x01",
            "a list of students like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        "#542F#6POh, that's interesting... I wasn't aware of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#678F#5PHaha. To tell you the truth, I was once a student\x01",
            "of the academy.\x02\x03",

            "Not just any student, either. I was part of the\x01",
            "Student Council as well!\x02\x03",

            "#670FJenis' council is a fine organization.\x02\x03",

            "#673FThey're proud as they are nobleminded, with a\x01",
            "true dedication to carrying out their duties and\x01",
            "bettering the academy they serve and belong to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#044F#6PI-I see...\x02\x03",

            "#047F(It's hard to believe that was ever the case\x01",
            "looking at the current Student Council...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#670F#5PThe experience I gained there continues to be\x01",
            "valuable to me to this very day.\x02\x03",

            "I'm sure the same will be true for you in your\x01",
            "adult life, too, so do continue to work as part\x01",
            "of it the best you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#045F#6PTh-Thank you... I will.\x02\x03",

            "(I'm not actually a member, though...)\x02\x03",

            "#542FWell, if you will excuse me. I wouldn't\x01",
            "want to keep you any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#670F#5POh, it was no trouble.\x02\x03",

            "If I can do anything else to help you in\x01",
            "the future, by all means stop by.\x02\x03",

            "#678FI might be able to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        "#543F#6PThank you very much.\x02",
    )

    CloseMessageWindow()

    def lambda_E90():

        label("loc_E90")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_E90")

    QueueWorkItem2(0x11, 2, lambda_E90)

    def lambda_EA1():

        label("loc_EA1")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_EA1")

    QueueWorkItem2(0x10, 2, lambda_EA1)
    OP_8C(0x105, 90, 600)

    def lambda_EB9():
        OP_8E(0xFE, 0x11D8C, 0xFFFFFFE2, 0xFFFFDECC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EB9)
    WaitChrThread(0x105, 0x1)

    def lambda_ED9():
        OP_8E(0xFE, 0x11D8C, 0xFFFFF830, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ED9)
    WaitChrThread(0x105, 0x1)

    def lambda_EF9():
        OP_8E(0xFE, 0x11170, 0xFFFFF15A, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EF9)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_422 end

    def Function_5_F26(): pass

    label("Function_5_F26")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #17
        (
            "\x07\x05'Sapphire Glim'\x01",
            "Said to be the culmination of early orbal arts.\x01",
            "Given to House Dalmore by the citizens of Ruan\x01",
            "immediately after the Orbal Revolution, as\x01",
            "thanks for contributions to the city's growth.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_F26 end

    def Function_6_1021(): pass

    label("Function_6_1021")

    NewScene("ED6_DT21/T2210   ._SN", 123, 1, 0)
    IdleLoop()
    Return()

    # Function_6_1021 end

    def Function_7_102B(): pass

    label("Function_7_102B")

    NewScene("ED6_DT21/T2210   ._SN", 121, 1, 0)
    IdleLoop()
    Return()

    # Function_7_102B end

    def Function_8_1035(): pass

    label("Function_8_1035")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05There's a drawbridge control unit here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1035 end

    SaveToFile()

Try(main)

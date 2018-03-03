from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
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
        'Tio',                                  # 10
        'Elissa',                               # 11
        'Wasp',                                 # 12
        'Target Camera',                        # 13
        'Elize Highway',                        # 14
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
        'ED6_DT07/CH02750 ._CH',             # 00
        'ED6_DT07/CH02740 ._CH',             # 01
        'ED6_DT07/CH02730 ._CH',             # 02
        'ED6_DT09/CH10270 ._CH',             # 03
        'ED6_DT07/CH02220 ._CH',             # 04
        'ED6_DT26/CH20339 ._CH',             # 05
        'ED6_DT26/CH20787 ._CH',             # 06
        'ED6_DT26/CH20788 ._CH',             # 07
        'ED6_DT26/CH20789 ._CH',             # 08
        'ED6_DT26/CH20794 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02750P._CP',             # 00
        'ED6_DT07/CH02740P._CP',             # 01
        'ED6_DT07/CH02730P._CP',             # 02
        'ED6_DT09/CH10270P._CP',             # 03
        'ED6_DT07/CH02220P._CP',             # 04
        'ED6_DT26/CH20339P._CP',             # 05
        'ED6_DT26/CH20787P._CP',             # 06
        'ED6_DT26/CH20788P._CP',             # 07
        'ED6_DT26/CH20789P._CP',             # 08
        'ED6_DT26/CH20794P._CP',             # 09
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
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
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
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

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1BA",          # 00, 0
        "Function_1_22D",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_3B7",          # 03, 3
        "Function_4_1993",         # 04, 4
        "Function_5_3779",         # 05, 5
        "Function_6_37CA",         # 06, 6
        "Function_7_383F",         # 07, 7
        "Function_8_388C",         # 08, 8
        "Function_9_38F4",         # 09, 9
        "Function_10_3969",        # 0A, 10
        "Function_11_39B6",        # 0B, 11
        "Function_12_3A6E",        # 0C, 12
        "Function_13_3A85",        # 0D, 13
        "Function_14_3C7D",        # 0E, 14
        "Function_15_5674",        # 0F, 15
        "Function_16_56EC",        # 10, 16
        "Function_17_579F",        # 11, 17
        "Function_18_5824",        # 12, 18
        "Function_19_58D2",        # 13, 19
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1DC")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_22C")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1FB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_22C")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_22C")

    label("loc_21A")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_22C")

    Return()

    # Function_0_1BA end

    def Function_1_22D(): pass

    label("Function_1_22D")

    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    Return()

    # Function_1_22D end

    def Function_2_23A(): pass

    label("Function_2_23A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3A1")

    label("loc_25F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3A1")

    label("loc_278")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3A1")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3A1")

    label("loc_2AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3A1")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3A1")

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3A1")

    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3A1")

    label("loc_30E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3A1")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3A1")

    label("loc_340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3A1")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3A1")

    label("loc_372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3A1")

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3A1")

    label("loc_3B6")

    Return()

    # Function_2_23A end

    def Function_3_3B7(): pass

    label("Function_3_3B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(450)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x101, -3600, 0, -5600, 0)
    OP_6D(-17750, 0, -430, 0)
    OP_67(0, 5550, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    Sleep(2000)
    Sleep(500)

    def lambda_44E():
        OP_6B(3130, 5000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_44E)

    def lambda_45E():
        OP_67(0, 6050, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_45E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #0
        0x10,
        (
            "#1676F#5P#40W...\x02\x03",

            "#1675FI...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4AC():
        OP_6D(-12270, 0, -3050, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4AC)

    def lambda_4C4():
        OP_6C(160000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4C4)
    Sleep(3500)

    NpcTalk(    #1
        0x101,
        "Cheery Voice",
        "#4PHuh? I can't find him anywhere...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x101,
        "Cheery Voice",
        (
            "#4PHe's supposed to be hurt and resting,\x01",
            "not out wandering around!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #3
        0x101,
        "Cheery Voice",
        "#4PJoshua! Where the heck are you?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x101,
        "Cheery Voice",
        "#4PJoshuaaa!\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x101, -3600, 0, -7600, 90)

    def lambda_5D6():
        OP_8E(0xFE, 0xFFFFE796, 0x0, 0xFFFFE336, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D6)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 160, 400)
    Sleep(700)
    OP_8C(0x101, 340, 400)
    Sleep(300)

    def lambda_60E():
        OP_8E(0xFE, 0xFFFFD814, 0x0, 0xFFFFF7D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60E)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 25, 400)
    Sleep(700)
    TurnDirection(0x101, 0x10, 400)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#293F#5POh. THERE you are.\x02\x03",

            "#292FWhat're you doing out here? You've gotta\x01",
            "start taking it easy!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C2():
        OP_6D(-16780, 0, -260, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6C2)

    def lambda_6DA():
        OP_6C(168000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6DA)

    def lambda_6EA():
        OP_8E(0xFE, 0xFFFFCACC, 0x0, 0xFFFFFE34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EA)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #6
        0x10,
        (
            "#1676F#5P...\x02\x03",

            "#1676FWhy? I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#293F#5PAre you suuure?\x02\x03",

            "Is your fever gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#1676F#5PIt was just a temporary one as a result of my\x01",
            "injuries.\x02\x03",

            "My temperature went back down this morning.\x01",
            "I'm fine now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#293F#5PReally?\x02\x03",

            "#290FWhew... Yay. That's good.\x02\x03",

            "You were moaning over and over in your sleep.\x02\x03",

            "I was worried about you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #10
        0x10,
        (
            "#1671F#5P...\x02\x03",

            "Did I say anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#293F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1675F#5P...Forget I asked.\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8CC():
        OP_6B(3030, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8CC)

    def lambda_8DC():
        OP_8E(0xFE, 0xFFFFC7FC, 0x0, 0x82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8DC)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_906():
        OP_96(0xFE, 0xFFFFC324, 0x3B6, 0x44C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_906)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_92E():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92E)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #13
        0x101,
        (
            "#290FSo, umm...\x02\x03",

            "If you're feeling better, do you wanna\x01",
            "play together?\x02\x03",

            "It must've been pretty boring to sleep\x01",
            "all the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #14
        0x10,
        "#1674F#11P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#291FI know it's boring for me when\x01",
            "I'm stuck in bed with a fever!\x02\x03",

            "I hate not having anything to do.\x02\x03",

            "#293FOh, but you probably shouldn't be\x01",
            "running around with your foot all\x01",
            "messed up...\x02\x03",

            "#296FI guess tag and kick the can won't\x01",
            "work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        "#1676F#11P...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #17
        0x10,
        (
            "#1676F#5PIf you want to play, play by yourself.\x02\x03",

            "#1671FJust stay away from me.\x02\x03",

            "#1671FBecause it's probably going to get\x01",
            "dangerous here soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#293FIt is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1676F#5PI'm grateful to you for taking care of me.\x02\x03",

            "...Pass that on to Cassius Bright, too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #20
        0x101,
        (
            "#293F...\x02\x03",

            "#292F#3SNo gloomy faces allowed!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #21
        0x10,
        "#1678F#11P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#290FWhen you're feeling down, the best thing to\x01",
            "do is to do something you enjoy! That'll pick\x01",
            "you right up!\x02\x03",

            "#291FWait here, okay? I'll bring you stuff you'll\x01",
            "really like! Pinky swear!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D34():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D34)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_D59():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D59)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_D81():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0xFFFFEF70, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D81)
    WaitChrThread(0x101, 0x1)

    def lambda_DA1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DA1)
    Sleep(500)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(3000)
    OP_63(0x10)

    ChrTalk(    #23
        0x10,
        (
            "#1675F#5P(There still don't seem to be any signs that\x01",
            "anyone's going to come after me...)\x02\x03",

            "#1676F(But it's bound to happen eventually. I've got\x01",
            "two or three days at most before they find\x01",
            "this place.)\x02\x03",

            "(Two or three days...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x10, 1)
    Sleep(800)

    def lambda_EDB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EDB)

    def lambda_EED():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EED)
    Sleep(700)

    ChrTalk(    #24 op#A
        0x101,
        "#291F#12A#12PJoshua!\x02",
    )

    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_F30():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F30)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_F58():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F58)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #25
        0x101,
        (
            "#290FHere you go! A present from me!\x02\x03",

            "So cheer up, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Estelle proudly presented Joshua with a couple of roly polies.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #27
        0x10,
        (
            "#1671F#11P...?\x02\x03",

            "(What is she doing?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#291FAren't they cute?\x02\x03",

            "They curl up if you poke them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#1676F#11PI'm fine, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#293FWhaaat? How come? They're so cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1670F#11PBecause I don't.\x02\x03",

            "Also, stop coming over here. Stay away from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#296FSo you want another kind of bug, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "#1678F#11PThat wasn't what I was trying to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#291FHold on! I know LOTS of bugs!\x02",
    )

    CloseMessageWindow()

    def lambda_11C9():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C9)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_11EE():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11EE)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1216():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0xFFFFEF70, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1216)
    WaitChrThread(0x101, 0x1)

    def lambda_1236():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1236)

    ChrTalk(    #35
        0x10,
        "#1674F#11P...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    Sleep(1000)

    def lambda_1270():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1270)

    def lambda_1282():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1282)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_12A7():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A7)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_12CF():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12CF)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #36
        0x101,
        "#292FHow about THIS?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#291F#3SIt's a dragonfly!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#1676F#5PI don't want one of these, either...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#292FOkay, but how about THIS?! \x02\x03",

            "You've gotta like these!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x101,
        "#291F#3SBehold! A Malgan monitor lizard!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#1676F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #42
        0x101,
        "#294F#3SWhat?! You're one tough cookie...\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(800)

    ChrTalk(    #43
        0x10,
        (
            "#1675F#11PLook, this isn't about what I like. I don't want\x01",
            "any kind of bug or lizard or anything you have\x01",
            "to offer me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14E0():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14E0)
    Sleep(500)

    ChrTalk(    #44
        0x101,
        (
            "#292FAaargh!\x02\x03",

            "#294FThis one's my favorite, too!\x01",
            "What's wrong with you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1671F#11P(What's wrong with YOU?)\x02\x03",

            "(I'm feeling more and more like there's\x01",
            "something I'm missing, here...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#292FSit down for a minute, Joshua. I've got a\x01",
            "serious question to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#1671F#11P...I'm already sitting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#290FWhat kinda bugs do you like?\x02",
    )

    CloseMessageWindow()

    def lambda_1658():
        OP_6B(2980, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1658)

    ChrTalk(    #49
        0x101,
        "#291FBig ones? Pretty ones?\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_169A():
        OP_6B(2930, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_169A)

    ChrTalk(    #50
        0x101,
        "#291F#3SOnes with lots of legs? Ones with long feelers?\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_16F8():
        OP_6B(2880, 100)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_16F8)

    ChrTalk(    #51
        0x101,
        "#291F#4SOnes with shells? Wings? Webbed feet?\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1671F#11P...\x02\x03",

            "I don't want any bugs at all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_177E():
        OP_6B(3030, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_177E)

    ChrTalk(    #53 op#A
        0x101,
        "#293F#5S#12AWhaaaaaaaaat?!#2S#240W\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        (
            "#295F...I'm gonna have to pull out all the stops.\x02\x03",

            "I need something so surprising, you'll change\x01",
            "your mind...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#294FDon't move a muscle!\x02\x03",

            "I'll find something! I will!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1881():
        OP_6D(-14780, 0, -2260, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1881)

    def lambda_1899():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1899)

    def lambda_18B1():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18B1)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_18D6():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D6)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_18FE():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18FE)
    WaitChrThread(0x101, 0x1)

    def lambda_191E():
        OP_8E(0xFE, 0xFFFFE228, 0x0, 0xFFFFC8EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191E)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #56
        0x10,
        (
            "#1674F#11P...\x02\x03",

            "She sure likes bugs, doesn't she?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3B7 end

    def Function_4_1993(): pass

    label("Function_4_1993")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrPos(0x101, -8029, 0, -8280, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_6D(-16780, 0, -260, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(168000, 0)
    OP_6E(262, 0)
    OP_1D(0xB7)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x10,
        (
            "#1675F#5P...\x02\x03",

            "(It's so...quiet here.)\x02\x03",

            "(Even after all I've been through, this is the\x01",
            "first time I've been in a situation like this...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #58
        0x101,
        "Cheery Voice",
        "#4P#3SJoshua! #2S\x02",
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x96, 0x1)
    Sleep(1200)

    ChrTalk(    #59
        0x10,
        "#1671F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_1B12():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B12)
    WaitChrThread(0x101, 0x1)

    def lambda_1B32():
        OP_8E(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B32)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #60 op#A
        0x101,
        "#290F#10A#6PHiyaaa!\x02",
    )

    SetChrFlags(0x101, 0x4)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1B74():
        OP_96(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B74)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1B9C():
        OP_8E(0xFE, 0xFFFFBBCC, 0x3A2, 0xB0E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B9C)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #61
        0x101,
        "#291FLook! Look at this one's face!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #62
        0x10,
        (
            "#1670F#11PHow many times do I have to tell you I don't\x01",
            "want any bugs before it gets through?\x02\x03",

            "Are you even listening?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#294FLook, though! I hereby name this the\x01",
            "Human Moth, 'cause the pattern on its\x01",
            "wings looks like a human face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#1678F#11P...\x02\x03",

            "(What the heck?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#291FAhahaha! I knew this'd surprise you!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(150)
    SetChrSubChip(0x10, 16)
    Sleep(500)

    ChrTalk(    #66
        0x10,
        "#1677F#5PExcept it didn't.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #67
        0x101,
        (
            "#291FI knew my efforts would pay off big time! ☆\x02\x03",

            "#290FNext time, I'm gonna bring back something\x01",
            "even MORE awesome!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DF8():
        OP_6D(-14780, 0, -2260, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1DF8)

    def lambda_1E10():
        OP_67(0, 5350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E10)

    def lambda_1E28():
        OP_8E(0xFE, 0xFFFFC388, 0x3B6, 0x5BE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E28)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_1E4D():
        OP_96(0xFE, 0xFFFFC892, 0x0, 0x33E, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E4D)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_1E75():
        OP_8E(0xFE, 0xFFFFCF86, 0x0, 0xFFFFFE2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E75)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #68 op#A
        0x101,
        "#291F#6P#15AWheeeeee!\x02",
    )


    def lambda_1EAF():
        OP_8E(0xFE, 0xFFFFE228, 0x0, 0xFFFFC8EC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EAF)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #69
        0x10,
        "#1675F#5PShe's so obnoxious...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8029, 0, -8280, 0)
    SetChrSubChip(0x10, 1)
    OP_6D(-16780, 0, -260, 0)
    OP_67(0, 6050, -10000, 0)
    SoundLoad(373)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #70
        0x101,
        "Cheery Voice",
        "#4PJo...a...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #71
        0x10,
        "#1677F#5POh, great. She's back.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 3100, -500, -37490, 0)
    SetChrPos(0x101, 3100, -1000, -37490, 0)
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1FFD():
        OP_6D(1870, -1000, -24530, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1FFD)

    def lambda_2015():
        OP_6C(180000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2015)
    Sleep(4000)

    def lambda_202A():
        OP_8E(0xFE, 0x7A8, 0xFFFFFC18, 0xFFFFB55A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_202A)
    Sleep(1000)

    ChrTalk(    #72 op#A
        0x101,
        "#294F#15A#6P#3SJoshuaaa!\x02",
    )


    def lambda_2066():
        OP_8E(0xFE, 0x7A8, 0x1F4, 0xFFFFD1DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2066)
    OP_43(0x13, 0x2, 0x0, 0xC)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_2092():
        OP_96(0xFE, 0x7A8, 0x0, 0xFFFFC005, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2092)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_20BA():
        OP_8E(0xFE, 0x7A8, 0x0, 0xFFFFCA0E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20BA)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x13, 0x1)
    Fade(1000)
    OP_6D(-14050, 0, 450, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(192000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -9970, 0, -11460, 335)
    SetChrPos(0x13, -9970, 500, -11460, 335)

    def lambda_2143():
        OP_8E(0xFE, 0xFFFFC950, 0x0, 0x53C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2143)
    Sleep(600)
    OP_43(0x13, 0x3, 0x0, 0xB)
    Sleep(200)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x64, 0x1)
    SetChrSubChip(0x10, 8)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #73 op#A
        0x101,
        "#15A#3SGeronimooo!#2S\x02",
    )

    SetChrFlags(0x101, 0x4)

    def lambda_21AE():
        TurnDirection(0xFE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21AE)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_21C1():
        OP_96(0xFE, 0xFFFFC1C6, 0x3B6, 0x6B8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21C1)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_21E9():
        OP_8F(0xFE, 0xFFFFBB90, 0x3B6, 0x776, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21E9)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(    #74 op#A
        0x10,
        "#6A#2PH-Hey...!\x02",
    )

    LoadEffect(0x0, "map\\mp012_00.eff")
    LoadEffect(0x1, "map\\sibuki0.eff")
    LoadEffect(0x2, "map\\mp013_02.eff")

    def lambda_225C():
        OP_6D(-15600, -3000, 4510, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_225C)

    def lambda_2274():
        OP_6C(180000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2274)

    def lambda_2284():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2284)

    def lambda_2292():
        OP_8E(0xFE, 0xFFFFBD02, 0x3B6, 0xE7E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2292)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrPos(0x10, -18120, 800, 1800, 315)

    def lambda_22CD():
        OP_8F(0xFE, 0xFFFFBAAA, 0x3B6, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_22CD)
    WaitChrThread(0x101, 0x1)

    def lambda_22ED():
        OP_8C(0xFE, 215, 100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22ED)

    def lambda_22FB():
        OP_8C(0xFE, 215, 100)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_22FB)
    OP_22(0xA3, 0x0, 0x5A)

    def lambda_230E():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF448, 0x26B6, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_230E)

    def lambda_232C():
        OP_96(0xFE, 0xFFFFC0EB, 0xFFFFF448, 0x2472, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_232C)
    Sleep(200)
    ClearChrFlags(0x101, 0x1)
    Sleep(100)
    ClearChrFlags(0x10, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -15040, -2500, 9910, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -16149, -2500, 9330, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 700, 700, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xFF, -16149, -1700, 9330, 0, 0, 0, 700, 700, 500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    Sleep(6000)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x4, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0xFF, -16149, -1700, 9330, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Sleep(4000)

    def lambda_24D2():
        OP_6D(-15660, -3000, 6510, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_24D2)
    Sleep(4000)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_43(0x101, 0x0, 0x0, 0x6)

    ChrTalk(    #75
        0x101,
        (
            "#293F#6PHwah!\x02\x03",

            "#291FAhahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, -16149, -2200, 9330, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xFF, -16149, -1700, 9330, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_43(0x10, 0x0, 0x0, 0x9)

    ChrTalk(    #76
        0x10,
        (
            "#1673F#5P...Gah!\x02\x03",

            "#1677F*pant* *pant*\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    OP_8C(0x10, 35, 400)
    Sleep(500)

    ChrTalk(    #77
        0x10,
        "#1672F#11P#3SWhat was THAT for?!\x02",
    )

    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#293F#6PWhat was what for?\x02\x03",

            "#291FAhahaha!\x02\x03",

            "I'm gonna splash you!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x0)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15540, -2200, 9610, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2773():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2773)
    Sleep(500)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -15040, -2200, 9910, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -15540, -2200, 9610, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x7, 0xFF, -15040, -1700, 9910, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    def lambda_283A():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_283A)
    WaitChrThread(0xEE, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x7)
    OP_82(0x2, 0x2)

    ChrTalk(    #79
        0x10,
        "#1675F#11P...Ugh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#290F#6PAhhh... The water feels so nice.\x02\x03",

            "#291FOh, I know! Wanna go fishing?\x02\x03",

            "Playing in the water's fun, but real fishing's\x01",
            "even more fun!\x02\x03",

            "#292FLet's go catch today's lunch!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2935():

        label("loc_2935")

        TurnDirection(0xFE, 0x101, 500)
        OP_48()
        Jump("loc_2935")

    QueueWorkItem2(0x10, 3, lambda_2935)
    OP_8C(0x101, 135, 400)
    OP_82(0x7, 0x2)
    OP_44(0x101, 0x0)

    def lambda_2954():
        OP_8E(0xFE, 0xFFFFC996, 0xFFFFF6A0, 0x2012, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2954)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x101, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_82(0x7, 0x2)
    Sleep(500)
    OP_82(0x6, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x13, 0x0)
    OP_82(0x5, 0x2)
    OP_43(0x101, 0x0, 0x0, 0x8)
    PlayEffect(0x2, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x4, 0x2)
    TurnDirection(0x101, 0x10, 500)
    OP_44(0x10, 0x3)

    ChrTalk(    #81
        0x101,
        (
            "#290F#5PC'mon, Joshua! We're getting out!\x02\x03",

            "You'll catch a cold if you stay in those wet\x01",
            "clothes too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#1670F#12P...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x10, 0x20)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x10, 0x1)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrPos(0x101, -12550, 0, 7600, 135)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)

    def lambda_2AF3():

        label("loc_2AF3")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2AF3")

    QueueWorkItem2(0x101, 2, lambda_2AF3)
    OP_6D(-15360, 0, 4470, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(178000, 0)
    OP_6E(262, 0)
    SoundLoad(450)
    LoadEffect(0x7, "map\\mp013_02.eff")
    LoadEffect(0x2, "map\\mp071_01.eff")
    LoadEffect(0x3, "map\\mp071_02.eff")
    LoadEffect(0x4, "map\\mp071_03.eff")
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2BFB():
        OP_99(0xFE, 0x4, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BFB)
    OP_22(0x18, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #83
        0x101,
        (
            "#291FYAY! Caught a big one!\x02\x03",

            "This one's for you, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #84
        0x10,
        "#1676F#6PYou don't need to catch anything for me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#291FNow I'm gonna catch one for me!\x02\x03",

            "#294FIf I don't catch anything, I'll have to go \x01",
            "without lunch. And that would suck.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_2D9D():

        label("loc_2D9D")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2D9D")

    QueueWorkItem2(0x101, 2, lambda_2D9D)
    Sleep(300)
    OP_22(0x19, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #86
        0x10,
        (
            "#1674F#6P...\x02\x03",

            "#1677F(She doesn't listen to a word anyone says\x01",
            "to her, does she?)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x0, 0x2)

    def lambda_2E6E():

        label("loc_2E6E")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_2E6E")

    QueueWorkItem2(0x101, 2, lambda_2E6E)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #87
        0x101,
        (
            "#292FOooh, I got a bite!\x02\x03",

            "#294FHaaah!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2EF1():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EF1)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    OP_82(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #88
        0x101,
        (
            "#293FOh, it's a dace.\x02\x03",

            "#296FAnd it's tiny... Daddy's getting this one.\x02\x03",

            "#292FHe probably just spent the day messing around\x01",
            "instead of working, anyway. He doesn't deserve\x01",
            "a cool fish.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x96, 0x1)
    Sleep(1200)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #89
        0x10,
        "#1678F#12P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#291FOkay, next one I catch is definitely mine!\x02\x03",

            "Hi-ho!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_30C1():

        label("loc_30C1")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_30C1")

    QueueWorkItem2(0x101, 2, lambda_30C1)
    Sleep(300)
    OP_22(0x19, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x10)

    ChrTalk(    #91
        0x10,
        "#1678F#12P(She doesn't know anything about Cassius Bright?)\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #92
        0x10,
        (
            "#1675F#6P(So he tells his daughter nothing about what he\x01",
            "does... It fits his profile, I suppose.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31EA():

        label("loc_31EA")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_31EA")

    QueueWorkItem2(0x101, 2, lambda_31EA)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_323E():

        label("loc_323E")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_323E")

    QueueWorkItem2(0x101, 2, lambda_323E)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    OP_82(0x0, 0x2)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 400, 400, 250, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #93
        0x101,
        (
            "#293FAww. It got away.\x02\x03",

            "#294FThe next one's not gonna be so lucky, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 8)
    Sleep(500)

    ChrTalk(    #94
        0x10,
        "#1671F...\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x7, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)

    ChrTalk(    #95
        0x101,
        (
            "#293FAh! A tug!\x02\x03",

            "#296FOkay, maybe not...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_20(0x1F40)
    Sleep(2000)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #96
        0x10,
        "#1678F#6P...?\x02",
    )

    CloseMessageWindow()

    def lambda_33CA():
        OP_6D(-17520, 400, 2520, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_33CA)

    def lambda_33E2():
        OP_6C(198000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33E2)
    WaitChrThread(0x14, 0x0)
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #97
        0x10,
        "#1675FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#293FMm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #99
        0x101,
        "#290F...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        "#1675FNo, it's nothing...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(500)
    OP_59()
    Fade(250)
    SetChrSubChip(0x10, 16)
    OP_0D()

    def lambda_348F():
        OP_6D(-20940, 0, -1000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_348F)

    def lambda_34A7():
        OP_6C(194000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_34A7)
    Sleep(3000)
    OP_63(0x101)
    WaitChrThread(0x14, 0x0)
    Fade(3000)
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -21270, 800, 2220, 0)
    SetChrFlags(0x101, 0x8)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(3000)
    OP_23(0x1C2)
    Sleep(1500)

    ChrTalk(    #101
        0x10,
        (
            "#1678F#40W(Was it always so...#5W#40Wbright...?)\x02\x03",

            "#1675F#40W(The greenery's hurting my eyes...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(1000)
    Fade(1000)
    OP_6D(-14110, 0, 4950, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(178000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -12550, 0, 7600, 135)
    ClearChrFlags(0x101, 0x8)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_35F8():

        label("loc_35F8")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_35F8")

    QueueWorkItem2(0x101, 2, lambda_35F8)
    OP_43(0x101, 0x3, 0x0, 0xD)
    PlayEffect(0x7, 0x0, 0xFF, -13600, -1700, 7900, 0, 0, 0, 500, 500, 300, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #102
        0x101,
        "#294FGot'cha! This one's gonna be HUGE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#292FCome to me, lunchy fishy!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_36A1():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A1)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, -13930, -1700, 8210, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #104
        0x101,
        "#293F#3SWhat the heck?! It's a baby!#2S\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1B, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    Call(0, 14)
    Return()

    # Function_4_1993 end

    def Function_5_3779(): pass

    label("Function_5_3779")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37C9")
    OP_22(0x18, 0x0, 0x50)
    OP_22(0x22, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0x101, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_5_3779")

    label("loc_37C9")

    Return()

    # Function_5_3779 end

    def Function_6_37CA(): pass

    label("Function_6_37CA")

    SetChrFlags(0xFE, 0x20)

    def lambda_37D5():
        OP_96(0xFE, 0xFFFFC540, 0xFFFFF6A0, 0x26B6, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D5)
    WaitChrThread(0xFE, 0x1)

    label("loc_37F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_383E")

    def lambda_3801():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3801)
    WaitChrThread(0xFE, 0x1)

    def lambda_3821():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3821)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_37F2")

    label("loc_383E")

    Return()

    # Function_6_37CA end

    def Function_7_383F(): pass

    label("Function_7_383F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_388B")

    def lambda_384E():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_384E)
    WaitChrThread(0xFE, 0x1)

    def lambda_386E():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_386E)
    WaitChrThread(0xFE, 0x1)
    Jump("Function_7_383F")

    label("loc_388B")

    Return()

    # Function_7_383F end

    def Function_8_388C(): pass

    label("Function_8_388C")


    def lambda_3892():
        OP_8F(0xFE, 0xFFFFCC34, 0xFFFFF6A0, 0x1C02, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3892)

    label("loc_38A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38F3")

    def lambda_38B6():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38B6)
    WaitChrThread(0xFE, 0x1)

    def lambda_38D6():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38D6)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_38A7")

    label("loc_38F3")

    Return()

    # Function_8_388C end

    def Function_9_38F4(): pass

    label("Function_9_38F4")

    SetChrFlags(0xFE, 0x20)

    def lambda_38FF():
        OP_96(0xFE, 0xFFFFC0EB, 0xFFFFF6A0, 0x2472, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38FF)
    WaitChrThread(0xFE, 0x1)

    label("loc_391C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3968")

    def lambda_392B():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_392B)
    WaitChrThread(0xFE, 0x1)

    def lambda_394B():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_394B)
    WaitChrThread(0xFE, 0x1)
    Jump("loc_391C")

    label("loc_3968")

    Return()

    # Function_9_38F4 end

    def Function_10_3969(): pass

    label("Function_10_3969")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39B5")

    def lambda_3978():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3978)
    WaitChrThread(0xFE, 0x1)

    def lambda_3998():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3998)
    WaitChrThread(0xFE, 0x1)
    Jump("Function_10_3969")

    label("loc_39B5")

    Return()

    # Function_10_3969 end

    def Function_11_39B6(): pass

    label("Function_11_39B6")


    def lambda_39BC():
        OP_8E(0xFE, 0xFFFFC75C, 0x1F4, 0x1A4A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39BC)
    WaitChrThread(0xFE, 0x1)

    def lambda_39DC():
        OP_8E(0xFE, 0xFFFFC022, 0xFFFFF830, 0x1766, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39DC)
    WaitChrThread(0xFE, 0x1)
    OP_97(0xFE, 0xFFFFC3C4, 0x1DB0, 0xAFC80, 0x898, 0x1)
    OP_43(0xFE, 0x2, 0x0, 0x2)

    def lambda_3A18():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_3A18)
    Sleep(2000)
    OP_44(0xFE, 0x2)

    def lambda_3A2F():
        OP_8E(0xFE, 0xFFFFC75C, 0x1F4, 0x1A4A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A2F)
    WaitChrThread(0xFE, 0x1)

    def lambda_3A4F():
        OP_8E(0xFE, 0xFFFFDE9A, 0x1F4, 0xFFFFCC48, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A4F)
    OP_44(0xFE, 0x2)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_11_39B6 end

    def Function_12_3A6E(): pass

    label("Function_12_3A6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A84")
    OP_22(0x175, 0x0, 0x64)
    Sleep(3500)
    Jump("Function_12_3A6E")

    label("loc_3A84")

    Return()

    # Function_12_3A6E end

    def Function_13_3A85(): pass

    label("Function_13_3A85")

    PlayEffect(0x2, 0xFF, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3ABA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C7C")
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    OP_22(0x22, 0x0, 0x5A)
    OP_22(0x23, 0x0, 0x50)
    OP_22(0x24, 0x0, 0x50)
    PlayEffect(0x1, 0x1, 0xFF, -13600, -1700, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Jump("loc_3ABA")

    label("loc_3C7C")

    Return()

    # Function_13_3A85 end

    def Function_14_3C7D(): pass

    label("Function_14_3C7D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x101, 10730, 0, -9920, 245)
    OP_6D(3330, -1000, -32130, 0)
    OP_67(0, 7980, -10000, 0)
    OP_6B(2660, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #105 op#A op#5
        "\x18\x07\x00#35A#40WThe second week...\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0xF)
    SetChrPos(0x11, 4410, -1000, -40080, 0)
    SetChrPos(0x12, 3370, -1000, -40080, 0)

    def lambda_3D59():
        OP_8E(0xFE, 0x79E, 0xFFFFFC18, 0xFFFFAAB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3D59)
    Sleep(100)

    def lambda_3D79():
        OP_8E(0xFE, 0xBEA, 0xFFFFFC18, 0xFFFFAAB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D79)
    Sleep(2000)

    def lambda_3D99():
        OP_6D(3310, -1000, -22600, 7500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3D99)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #106 op#A
        0x12,
        "#11P#20ADo you think she's okay?\x02",
    )

    Sleep(2000)

    ChrTalk(    #107
        0x12,
        (
            "#11PShe didn't come over to the shop yesterday,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #108
        0x11,
        "#5PI still think you're worried about nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        (
            "#5PEstelle's okay! She always does whatever\x01",
            "she wants, when she wants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        "#11PBut she used to come over to play every day...\x02",
    )

    CloseMessageWindow()

    def lambda_3EF5():
        OP_8E(0xFE, 0x5AA, 0x0, 0xFFFFC9F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3EF5)
    OP_8C(0x11, 0, 400)

    def lambda_3F17():
        OP_8E(0xFE, 0x9F6, 0x0, 0xFFFFC9F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3F17)
    Sleep(1000)
    Fade(1000)
    OP_6D(2000, 0, -9910, 0)
    OP_67(0, 4380, -10000, 0)
    OP_6B(3760, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3F79():
        OP_6D(2000, 0, -5910, 2500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3F79)

    def lambda_3F91():
        OP_67(0, 3880, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3F91)
    Sleep(1000)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #111
        0x12,
        "#5P#3SESTEEELLE! IT'S ELISSA!\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #112
        0x12,
        "#5P#3SEsteeeeeelle! Come outside!\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x12, 315, 400)
    Sleep(600)
    OP_8C(0x12, 45, 400)
    Sleep(600)
    OP_8C(0x12, 0, 400)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0x11, 400)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #113
        0x12,
        (
            "#1PY-You don't think she's been ab-dock-ted,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        (
            "#2PI think I'd buy 'she got attacked by monsters\x01",
            "in the woods and ended up experiencing a slow, \x01",
            "drawn-out death' more than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        "#2P...That sounds like the way she'd go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x12,
        "#1P#3SThat's so gross!\x02",
    )

    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #117
        0x11,
        (
            "#2PThat's what she gets for going into the\x01",
            "woods all the time to play.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #118
        0x12,
        "#1PO-Oh, no... Poor Estelle...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #119
        0x11,
        "#2P...You do know I'm joking, right?\x02",
    )

    CloseMessageWindow()

    def lambda_42A0():
        OP_8E(0xFE, 0x9F6, 0x0, 0xFFFFD152, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_42A0)
    Sleep(100)
    OP_8C(0x12, 0, 100)
    WaitChrThread(0x11, 0x1)
    Sleep(300)

    ChrTalk(    #120
        0x11,
        "#2PCome on out, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        "#2PElissa's going to cry if you don't!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x10, -9980, 0, -2130, 245)

    NpcTalk(    #122
        0x10,
        "Boy's Voice",
        (
            "#4PIf you're looking for Estelle, she's out at\x01",
            "the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 4)
    SetChrPos(0x10, -17800, 940, 1840, 0)
    TurnDirection(0x12, 0x10, 500)
    Sleep(50)
    TurnDirection(0x11, 0x10, 500)

    def lambda_43ED():
        OP_6D(-18040, 0, 2040, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_43ED)

    def lambda_4405():
        OP_67(0, 5000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4405)

    def lambda_441D():
        OP_6C(304000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_441D)

    def lambda_442D():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_442D)
    Sleep(2500)
    SetChrPos(0x11, -5820, 0, -5220, 305)
    SetChrPos(0x12, -6840, 0, -5940, 305)

    def lambda_4464():
        OP_8E(0xFE, 0xFFFFCBC6, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4464)
    Sleep(100)

    def lambda_4484():
        OP_8E(0xFE, 0xFFFFC87E, 0x0, 0xFFFFFC36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4484)
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x11,
        "You're a boy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x12,
        "Huh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        "#1676F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #126
        0x11,
        "Who're you?!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        "Yeah!!\x02",
    )

    CloseMessageWindow()

    def lambda_4545():
        OP_6B(3300, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4545)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrSubChip(0x10, 1)
    SetChrPos(0x10, -17820, 940, 1500, 315)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -16460, 950, 820, 315)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -16480, 950, 2450, 250)
    ClearParty()
    AddParty(0x54, 0xEE, 0xFF)
    ClearChrFlags(0x155, 0x2)
    SetChrPos(0x155, 3070, -1000, -43370, 0)
    OP_6D(2990, -1000, -31230, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SoundLoad(142)

    def lambda_45FD():
        OP_6D(0, 0, -13320, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_45FD)

    def lambda_4615():
        OP_6C(134000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4615)
    OP_43(0x155, 0x3, 0x0, 0xF)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #128 op#A
        0x155,
        "#290F#15A#3S#6PJoshuaaa!\x02",
    )

    Sleep(2700)

    ChrTalk(    #129 op#A
        0x155,
        "#291F#20A#3S#5PI caught something AMAZING!\x02",
    )

    Sleep(2000)
    OP_59()
    Sleep(1000)
    OP_44(0x155, 0xFF)
    Fade(1000)
    OP_6D(-15700, 0, -1170, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(163000, 0)
    OP_6E(262, 0)
    SetChrPos(0x155, -5500, 0, -6460, 270)
    Sleep(1000)

    def lambda_46EE():
        OP_8E(0xFE, 0xFFFFC87E, 0x0, 0xFFFFFC22, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_46EE)
    WaitChrThread(0x155, 0x1)
    TurnDirection(0x155, 0x10, 500)
    OP_62(0x155, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #130
        0x155,
        (
            "#293F#5PHuh?\x02\x03",

            "#290FWhat are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x12, 0x155, 400)
    Sleep(50)
    OP_8C(0x11, 115, 400)

    ChrTalk(    #131
        0x12,
        "#2PEstelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x12,
        "#2PWhere have you BEEN all this time?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x12,
        "#2PI was so worried about you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x11,
        "#12PWho's this boy, anyway? Someone you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x11,
        (
            "#12PWe've been trying to talk to him for ages now,\x01",
            "but he won't tell us anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x11,
        (
            "#12PKeeps telling us everything we ask is 'none of\x01",
            "our business.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1500, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(    #137
        0x10,
        (
            "#1676F#5P...Estelle.\x02\x03",

            "#1671FAre these your friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x155,
        "#293F#5PY-Yeah, they are...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #139
        0x10,
        (
            "#1676F#5P(It seems they're not lying about that part,\x01",
            "then.)\x02\x03",

            "(They don't seem to have undergone any kind\x01",
            "of training, either, and their guard is virtually\x01",
            "nonexistent...)\x02\x03",

            "#1675F(I figure it's about time THEY found me...)\x02\x03",

            "(...but it doesn't look like these two have\x01",
            "anything to do with them.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #140
        0x11,
        "#12PHe's barely talked ever since we got here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        (
            "#12PI've never seen him around Rolent before.\x01",
            "How do you even know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x155,
        (
            "#293F#5POh, 'cause Daddy gave him to me as a present.\x02\x03",

            "#291F#3SHe's my new little brother!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 1500, 0x2, 0x7, 0x64, 0x1)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #143
        0x10,
        "#1674F#5P(...?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12,
        "#2PHe is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x12,
        "#2PW-Wow... I sure wouldn't have guessed that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x11,
        "#12PNeither would I...because it doesn't make sense!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        "#12PThat's not how getting a little brother works!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x155,
        (
            "#291F#5PBut it's true!\x02\x03",

            "Right, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        "#1676F#5P...No, it isn't.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrPos(0x10, -17820, 950, 1500, 315)
    Sleep(500)

    def lambda_4D05():
        OP_6D(-13920, 0, -3730, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4D05)

    def lambda_4D1D():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4D1D)
    OP_43(0x10, 0x3, 0x0, 0x10)

    def lambda_4D34():

        label("loc_4D34")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4D34")

    QueueWorkItem2(0x155, 2, lambda_4D34)
    Sleep(50)

    def lambda_4D4A():

        label("loc_4D4A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4D4A")

    QueueWorkItem2(0x11, 2, lambda_4D4A)
    Sleep(50)

    def lambda_4D60():

        label("loc_4D60")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4D60")

    QueueWorkItem2(0x12, 2, lambda_4D60)
    Sleep(3000)

    ChrTalk(    #150 op#A
        0x155,
        "#294F#11P#25AHey! Wait a minute!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #151 op#A
        0x155,
        (
            "#292F#12P#15AListen, young man!\x02\x03",

            "Listen to what your older sister tells you!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #152
        0x10,
        "#1675F#5P#40WAs if someone like you could be my older sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x155,
        "#293F#12P...Huh? Why?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(-13280, 0, -2140, 0)
    OP_67(0, 4040, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(    #154
        0x10,
        (
            "#1676F#6PI'm not here to be friends with you.\x02\x03",

            "The only reason I'm here at all is that \x01",
            "'things just worked out that way.'\x02\x03",

            "#1671FThat was what Cassius Bright said, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #155
        0x155,
        "#293F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10,
        (
            "#1675F#6POh, and one more thing.\x02\x03",

            "Can you stop bringing me bugs?\x02\x03",

            "#1676FI don't know what your obsession with them is,\x01",
            "but being too much of a meddler is just going to\x01",
            "end with you getting hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x155, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x155)
    OP_8C(0x10, 140, 300)

    def lambda_5073():
        OP_8E(0xFE, 0xFFFFDAC6, 0x0, 0xFFFFE656, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5073)
    Sleep(900)

    def lambda_5093():
        OP_6D(-11530, 0, -5430, 1000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5093)

    def lambda_50AB():
        OP_6C(286000, 1000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_50AB)

    def lambda_50BB():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_50BB)

    def lambda_50CB():
        OP_8E(0xFE, 0xFFFFD35A, 0x0, 0xFFFFEF34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_50CB)
    WaitChrThread(0x155, 0x1)
    SetChrFlags(0x155, 0x4)

    ChrTalk(    #157 op#A
        0x155,
        "#294F#10A#2PHaaah!\x02",
    )

    OP_22(0xA3, 0x0, 0x46)

    def lambda_510C():
        OP_96(0xFE, 0xFFFFDAC6, 0x3E8, 0xFFFFE656, 0x578, 0x1388)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_510C)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8E, 0x0, 0x55)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 3)

    ChrTalk(    #158 op#A
        0x10,
        "#1673F#3P#10AOww!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_5165():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_5165)
    Sleep(50)

    def lambda_5184():
        OP_96(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5184)
    WaitChrThread(0x155, 0x1)
    Sleep(2000)
    OP_43(0x155, 0x3, 0x0, 0x11)
    Sleep(500)

    ChrTalk(    #159
        0x155,
        "#294F#11PTake that! And that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10,
        "#1673FOw! Owww!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x155,
        (
            "#292F#11PIn this house, I'm the older one!\x02\x03",

            "#294FThat means you have to listen to what I say!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        "#1675FO-Ow...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x4)
    OP_A2(0x0)
    WaitChrThread(0x155, 0x3)

    def lambda_5273():
        OP_8E(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_5273)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_52B9():
        OP_96(0xFE, 0xFFFFDAC6, 0x12C, 0xFFFFE656, 0x12C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_52B9)
    WaitChrThread(0x10, 0x1)

    def lambda_52DC():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_52DC)
    Sleep(300)

    ChrTalk(    #163
        0x155,
        (
            "#291F#11POkay?\x02\x03",

            "#100WO k a y,  J o s h u a?\x01",
            "#20WGo on! Answer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        "#1670FN-No!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x155,
        "#294F#11P#3SExcuse me?!#2S\x02",
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)
    ClearChrFlags(0x10, 0x4)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_538A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_538A)

    def lambda_53A8():
        OP_8F(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_53A8)
    WaitChrThread(0x155, 0x1)
    OP_A3(0x0)
    OP_43(0x155, 0x3, 0x0, 0x12)
    Sleep(3000)
    OP_A2(0x0)
    Fade(1000)
    OP_6D(-18550, 0, 2390, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(294000, 0)
    OP_6E(262, 0)
    OP_44(0x12, 0xFF)
    OP_44(0x11, 0xFF)
    OP_8C(0x12, 160, 0)
    OP_8C(0x11, 160, 0)

    def lambda_5432():
        OP_8F(0xFE, 0xFFFFC23E, 0x3B6, 0x618, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5432)
    Sleep(1000)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #166
        0x12,
        "#5PWell, those two sure get along well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x11,
        "#11PSo it seems...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_44(0x155, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrFlags(0x155, 0x4)
    SetChrPos(0x155, -10400, 500, -5390, 114)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -10400, 500, -5390, 114)

    ChrTalk(    #168
        0x10,
        "#1670F#2PYou two can shut up any time.\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #169
        0x155,
        "#291F#3S#2PGot you!\x02",
    )

    CloseMessageWindow()
    OP_22(0x8E, 0x0, 0x55)
    OP_59()
    SetChrFlags(0x155, 0x800)
    SetChrPos(0x155, -10340, 400, -5310, 160)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 1)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -10290, -100, -4900, 160)

    def lambda_5593():
        OP_6D(-11800, 0, -4660, 2000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5593)
    Sleep(1000)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_55B5():
        OP_96(0xFE, 0xFFFFD558, 0x0, 0xFFFFEDE0, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_55B5)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x5A)
    Sleep(500)
    WaitChrThread(0x14, 0x0)

    ChrTalk(    #170
        0x155,
        (
            "#290F#5PI win! From today until forever,\x01",
            "I'm your big sister!\x02\x03",

            "#291FNo backsies allowed!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5645():
        OP_6B(2870, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5645)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3C7D end

    def Function_15_5674(): pass

    label("Function_15_5674")

    SetChrFlags(0x101, 0x4)

    def lambda_567F():
        OP_8E(0xFE, 0x7D0, 0xFFFFFC18, 0xFFFFB55A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_567F)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_56A4():
        OP_96(0xFE, 0x7D0, 0x0, 0xFFFFC005, 0x4B0, 0x1770)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_56A4)
    WaitChrThread(0x155, 0x1)
    OP_22(0xA4, 0x0, 0x5A)

    def lambda_56CC():
        OP_8E(0xFE, 0xFFFFD8AA, 0x0, 0xFFFFF24A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_56CC)
    WaitChrThread(0x155, 0x1)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_15_5674 end

    def Function_16_56EC(): pass

    label("Function_16_56EC")


    def lambda_56F2():
        OP_8E(0xFE, 0xFFFFBC44, 0x3B6, 0xDE8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56F2)
    WaitChrThread(0x10, 0x1)

    def lambda_5712():
        OP_8E(0xFE, 0xFFFFC180, 0x3B6, 0xBF4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5712)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA3, 0x0, 0x46)

    def lambda_5737():
        OP_96(0xFE, 0xFFFFC798, 0x0, 0xAAA, 0x190, 0x708)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5737)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x5A)
    ClearChrFlags(0x10, 0x4)

    def lambda_5764():
        OP_8E(0xFE, 0xFFFFCAC2, 0x0, 0xA1E, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5764)
    WaitChrThread(0x10, 0x1)

    def lambda_5784():
        OP_8E(0xFE, 0xFFFFD35A, 0x0, 0xFFFFEF34, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5784)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_16_56EC end

    def Function_17_579F(): pass

    label("Function_17_579F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5823")

    def lambda_57AE():
        OP_8F(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_57AE)
    WaitChrThread(0x155, 0x1)
    OP_22(0x8E, 0x0, 0x55)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 3)

    def lambda_57DD():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_57DD)

    def lambda_57F7():
        OP_8F(0xFE, 0xFFFFD62A, 0x0, 0xFFFFEBEC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_57F7)
    WaitChrThread(0x155, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5820")
    Jump("loc_5823")

    label("loc_5820")

    Jump("Function_17_579F")

    label("loc_5823")

    Return()

    # Function_17_579F end

    def Function_18_5824(): pass

    label("Function_18_5824")


    def lambda_582A():
        OP_8F(0xFE, 0xFFFFD936, 0x0, 0xFFFFE854, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_582A)
    WaitChrThread(0x155, 0x1)
    SetChrFlags(0x10, 0x20)

    label("loc_5849")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58D1")
    OP_22(0x84, 0x0, 0x64)

    def lambda_585D():
        OP_97(0xFE, 0xFFFFD936, 0xFFFFE854, 0xFFFA81C0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_585D)

    def lambda_5879():
        OP_8C(0xFE, 69, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_5879)
    WaitChrThread(0x155, 0x2)

    def lambda_588C():
        OP_8C(0xFE, 339, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_588C)
    WaitChrThread(0x155, 0x2)

    def lambda_589F():
        OP_8C(0xFE, 249, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_589F)
    WaitChrThread(0x155, 0x2)

    def lambda_58B2():
        OP_8C(0xFE, 159, 500)
        ExitThread()

    QueueWorkItem(0x155, 2, lambda_58B2)
    WaitChrThread(0x155, 0x2)
    WaitChrThread(0x10, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_58CE")
    Jump("loc_58D1")

    label("loc_58CE")

    Jump("loc_5849")

    label("loc_58D1")

    Return()

    # Function_18_5824 end

    def Function_19_58D2(): pass

    label("Function_19_58D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2140, 450, -1440, 180)
    SetChrPos(0x101, -5190, 0, -16790, 180)
    OP_6D(2800, 450, -4000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_5962():
        OP_6D(2480, 0, -12740, 6000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5962)

    def lambda_597A():
        OP_6B(2980, 6000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_597A)

    def lambda_598A():
        OP_67(0, 7500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_598A)

    def lambda_59A2():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFCC70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_59A2)
    Sleep(1200)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_6F(0x0, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x0, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_20(0x3E8)

    NpcTalk(    #171
        0x101,
        "Scared Voice",
        "#5PAaaaaah!\x02",
    )

    OP_7C(0x5, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 225, 400)
    OP_1D(0x98)
    Sleep(500)

    ChrTalk(    #172
        0x10,
        (
            "#1678F#5PThat sounded like Estelle!\x02\x03",

            "#1670FDid something happen to her?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)

    ChrTalk(    #173
        0x10,
        (
            "#1677F#5P(...No, it might not have. It's Estelle.\x01",
            "She probably just tripped.)\x02\x03",

            "#1675F(But...)\x02\x03",

            "(...)\x02\x03",

            "#1676F(No. Whatever may or may not have happened\x01",
            "to her, it's got nothing to do with me anymore.)\x02\x03",

            "(She's got nothing to do with me anymore...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10, 9)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #174
        0x10,
        "#1672F#5P#4S...Damn it!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C0302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_58D2 end

    SaveToFile()

Try(main)

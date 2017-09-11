from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1100   ._SN',
        MapName             = 'Bose',
        Location            = 'T1100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Royal Army Soldier',                   # 9
        'Royal Army Soldier',                   # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Officer',                   # 13
        'Officer in Black',                     # 14
        'Female Officer',                       # 15
        'Nial',                                 # 16
        'Dorothy',                              # 17
        'New Ansel Path',                       # 18
        'Bose - North Block',                   # 19
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH02030 ._CH',             # 02
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH02030P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48683,
        Z                   = -3000,
        Y                   = 29357,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48626,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47692,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47970,
        Z                   = -3000,
        Y                   = 4220,
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

    DeclNpc(
        X                   = 48070,
        Z                   = 0,
        Y                   = 48590,
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


    DeclEvent(
        X                   = 41890,
        Y                   = -6000,
        Z                   = 37580,
        Range               = 56300,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x4A88,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53090,
        Y                   = -3000,
        Z                   = 20940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 55320,
        Y                   = -3000,
        Z                   = 33040,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_29A",          # 00, 0
        "Function_1_332",          # 01, 1
        "Function_2_39A",          # 02, 2
        "Function_3_3B0",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_456",          # 05, 5
        "Function_6_50D",          # 06, 6
        "Function_7_5D1",          # 07, 7
        "Function_8_68A",          # 08, 8
        "Function_9_75C",          # 09, 9
        "Function_10_873",         # 0A, 10
        "Function_11_24D0",        # 0B, 11
        "Function_12_24FE",        # 0C, 12
        "Function_13_2AD8",        # 0D, 13
        "Function_14_2E98",        # 0E, 14
        "Function_15_307B",        # 0F, 15
        "Function_16_307F",        # 10, 16
    )


    def Function_0_29A(): pass

    label("Function_0_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 48000, -3000, 30522, 180)
    SetChrPos(0x9, 49200, -3000, 30522, 180)
    SetChrPos(0xA, 48000, -3000, 31900, 180)
    SetChrPos(0xB, 49200, -3000, 31900, 180)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_331")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_331")

    Return()

    # Function_0_29A end

    def Function_1_332(): pass

    label("Function_1_332")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFE7960, 0x30040)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A")
    OP_1B(0xD, 0x0, 0xD)
    Jump("loc_367")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367")
    OP_1B(0xD, 0x0, 0xD)

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_387")
    OP_1B(0xD, 0x0, 0xD)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0xE)
    OP_1B(0x2, 0x0, 0xE)

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399")
    OP_10(0xE, 0x1)
    OP_10(0x5, 0x0)

    label("loc_399")

    Return()

    # Function_1_332 end

    def Function_2_39A(): pass

    label("Function_2_39A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_39A")

    label("loc_3AF")

    Return()

    # Function_2_39A end

    def Function_3_3B0(): pass

    label("Function_3_3B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_431")
    OP_8E(0xFE, 0xBBF8, 0xFFFFF448, 0x7DC8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 500)
    Sleep(500)
    OP_8C(0xFE, 270, 500)
    Sleep(500)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xBBE4, 0xFFFFF448, 0x4D26, 0x7D0, 0x0)
    Sleep(300)
    Sleep(500)
    OP_8C(0xFE, 90, 500)
    Sleep(500)
    OP_8C(0xFE, 270, 500)
    Sleep(500)
    OP_8C(0xFE, 0, 500)
    Jump("Function_3_3B0")

    label("loc_431")

    Return()

    # Function_3_3B0 end

    def Function_4_432(): pass

    label("Function_4_432")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_455")
    OP_8D(0xFE, 75166, 31996, 63100, 26500, 2000)
    Jump("Function_4_432")

    label("loc_455")

    Return()

    # Function_4_432 end

    def Function_5_456(): pass

    label("Function_5_456")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50C")
    Sleep(2000)
    OP_8E(0xFE, 0x5442, 0x0, 0x416B, 0x7D0, 0x0)
    Sleep(1000)
    OP_8E(0xFE, 0x4EDE, 0xBB8, 0x7DB6, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x4FC4, 0xBB8, 0x6ECA, 0x7D0, 0x0)
    Sleep(1000)
    OP_8E(0xFE, 0x5B04, 0xBB8, 0x6C06, 0x7D0, 0x0)
    Sleep(4000)
    OP_8E(0xFE, 0x548D, 0xBB8, 0x6706, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5442, 0x0, 0x416B, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x8D5E, 0x0, 0x416E, 0x7D0, 0x0)
    Jump("Function_5_456")

    label("loc_50C")

    Return()

    # Function_5_456 end

    def Function_6_50D(): pass

    label("Function_6_50D")

    TalkBegin(0x8)

    ChrTalk(    #0
        0xFE,
        (
            "Are you the bracers we heard\x01",
            "about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Since the mayor has asked you to look into things,\x01",
            "I have no choice but to allow it. Just don't get\x01",
            "in the way of the army's investigation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_6_50D end

    def Function_7_5D1(): pass

    label("Function_7_5D1")

    TalkBegin(0x9)

    ChrTalk(    #2
        0xFE,
        (
            "I can't believe these sky bandits managed to\x01",
            "circumvent our search and just walked right\x01",
            "into town and burglarized a bunch of places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "We were really outdone this time.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_7_5D1 end

    def Function_8_68A(): pass

    label("Function_8_68A")

    TalkBegin(0xA)

    ChrTalk(    #4
        0xFE,
        (
            "It seems that the group of sky bandits\x01",
            "in the old mine consisted of two females\x01",
            "and a male.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Rumor has it that they've even got\x01",
            "children in the mix.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "What, those people weren't\x01",
            "sky bandits?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_68A end

    def Function_9_75C(): pass

    label("Function_9_75C")

    TalkBegin(0xB)

    ChrTalk(    #7
        0xFE,
        (
            "General Morgan may be stubborn,\x01",
            "but he's running the show, and he's\x01",
            "a very capable leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I wouldn't expect any less from\x01",
            "the man who defeated the Imperial\x01",
            "Army in the war a decade ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "But what gets me is why he's having\x01",
            "so much trouble this time around.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_9_75C end

    def Function_10_873(): pass

    label("Function_10_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24CF")
    OP_A2(0x339)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    def lambda_8B3():

        label("loc_8B3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8B3")

    QueueWorkItem2(0xC, 1, lambda_8B3)

    def lambda_8C4():

        label("loc_8C4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8C4")

    QueueWorkItem2(0x8, 1, lambda_8C4)

    def lambda_8D5():

        label("loc_8D5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8D5")

    QueueWorkItem2(0x9, 1, lambda_8D5)

    def lambda_8E6():

        label("loc_8E6")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8E6")

    QueueWorkItem2(0xA, 1, lambda_8E6)

    def lambda_8F7():

        label("loc_8F7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8F7")

    QueueWorkItem2(0xB, 1, lambda_8F7)

    ChrTalk(    #10
        0xC,
        "#1PHey! You there!\x02",
    )

    CloseMessageWindow()

    def lambda_920():

        label("loc_920")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_920")

    QueueWorkItem2(0x0, 2, lambda_920)
    Sleep(100)
    Fade(1000)

    def lambda_93B():

        label("loc_93B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_93B")

    QueueWorkItem2(0x1, 2, lambda_93B)

    def lambda_94C():

        label("loc_94C")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_94C")

    QueueWorkItem2(0x2, 2, lambda_94C)

    def lambda_95D():

        label("loc_95D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_95D")

    QueueWorkItem2(0x3, 2, lambda_95D)

    def lambda_96E():
        OP_69(0xC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_96E)

    def lambda_97C():
        OP_6C(0, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_97C)

    def lambda_98C():
        OP_6B(2800, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_98C)
    SetChrPos(0x102, 47362, -3000, 27682, 0)
    SetChrPos(0x101, 48132, -3000, 27051, 0)
    SetChrPos(0x103, 49152, -3000, 27309, 0)
    SetChrPos(0x104, 49977, -3000, 28146, 0)
    OP_0D()

    ChrTalk(    #11
        0x101,
        "#501FWhat? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xC,
        (
            "#6PI thought I'd better give you a word\x01",
            "of advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        (
            "#6PEven if you are representing the\x01",
            "mayor, at the end of the day,\x01",
            "you are all still civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "#6PWe cannot have you wandering\x01",
            "around here in the middle of our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        (
            "#509FWho do you think you're talking\x01",
            "to?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#017FYour 'advice' seems rather more\x01",
            "like a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "#6PI'm just saying you need to know\x01",
            "your place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "#6PBut if you're so adamant about investigating\x01",
            "the matter, then do it after we've cleared\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "#6PIf we get any more trouble out of you,\x01",
            "then I'm going to have to give you a\x01",
            "personal invitation...to jail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#009F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#027FForget about it, Estelle. There's no\x01",
            "use arguing with these...gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x104,
        (
            "#035FHa, for an ass in a lion's skin, you\x01",
            "sure know how to throw your weight\x01",
            "around, Mr. Soldier.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0xC,
        "What did you just say?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0xD,
        "Man's Voice",
        (
            "#6PMay I ask what's going on\x01",
            "here...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x65)
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 0, 400)

    def lambda_DF1():
        OP_6D(48924, -3000, 31700, 2000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_DF1)
    OP_44(0xC, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_E2D():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E2D)

    def lambda_E3B():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E3B)

    def lambda_E49():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E49)

    def lambda_E57():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E57)

    def lambda_E65():

        label("loc_E65")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E65")

    QueueWorkItem2(0x0, 1, lambda_E65)

    def lambda_E76():

        label("loc_E76")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E76")

    QueueWorkItem2(0x1, 1, lambda_E76)

    def lambda_E87():

        label("loc_E87")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E87")

    QueueWorkItem2(0x2, 1, lambda_E87)

    def lambda_E98():

        label("loc_E98")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E98")

    QueueWorkItem2(0x3, 1, lambda_E98)
    Sleep(1000)

    def lambda_EAE():
        OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x79F9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EAE)
    Sleep(600)

    def lambda_ECE():
        OP_8E(0xE, 0xBA4C, 0xFFFFF448, 0x7CA5, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_ECE)

    def lambda_EE9():

        label("loc_EE9")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_EE9")

    QueueWorkItem2(0x8, 2, lambda_EE9)

    def lambda_EFA():

        label("loc_EFA")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_EFA")

    QueueWorkItem2(0x9, 2, lambda_EFA)

    def lambda_F0B():

        label("loc_F0B")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_F0B")

    QueueWorkItem2(0xA, 2, lambda_F0B)

    def lambda_F1C():

        label("loc_F1C")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_F1C")

    QueueWorkItem2(0xB, 2, lambda_F1C)
    Sleep(900)

    def lambda_F32():
        OP_8F(0xFE, 0xC2C7, 0xFFFFF448, 0x7D5F, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F32)

    def lambda_F4D():
        OP_8F(0xFE, 0xC727, 0xFFFFF448, 0x7D5F, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F4D)
    Sleep(500)

    def lambda_F6D():
        OP_8F(0xFE, 0xC2C7, 0xFFFFF448, 0x7869, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F6D)

    def lambda_F88():
        OP_8F(0xFE, 0xC727, 0xFFFFF448, 0x7869, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F88)
    WaitChrThread(0xE, 0x1)

    ChrTalk(    #25
        0xC,
        "C-Colonel?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        (
            "#112F#6PFor a soldier in the prestigious\x01",
            "Royal Army to be threatening our\x01",
            "good citizens...\x02\x03",

            "That is an outright embarrassment\x01",
            "to us all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "#6PB-But these aren't just civilians, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        "They're members of the Bracer Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "#113F#6POh, is that so...?\x02\x03",

            "#112FThen I ask you once again. What is going\x01",
            "on here? The army is supposed to be\x01",
            "working closely with the guild.\x02\x03",

            "What do you intend to accomplish\x01",
            "by being rude to our allies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xC,
        (
            "#6PB-But as far as the general is\x01",
            "concerned...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        (
            "#115F#6PAh, yes... That side of the general\x01",
            "really concerns me.\x02\x03",

            "#110FI'll take over the investigation\x01",
            "from here, so please take your\x01",
            "men and clear out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        "B-But, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xD,
        (
            "#110F#6PYour men have been here since early this morning,\x01",
            "so I presume that a sufficient investigation has\x01",
            "been conducted by now, yes?\x02\x03",

            "I'll smooth things over with the\x01",
            "general later.\x02\x03",

            "Is there anything else you wish\x01",
            "me to address?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        "N-No, sir...\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 45, 400)

    def lambda_1362():

        label("loc_1362")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1362")

    QueueWorkItem2(0x8, 2, lambda_1362)

    def lambda_1373():

        label("loc_1373")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1373")

    QueueWorkItem2(0x9, 2, lambda_1373)

    def lambda_1384():

        label("loc_1384")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1384")

    QueueWorkItem2(0xA, 2, lambda_1384)

    def lambda_1395():

        label("loc_1395")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1395")

    QueueWorkItem2(0xB, 2, lambda_1395)
    Sleep(400)

    ChrTalk(    #35
        0xC,
        (
            "#6PAll right, men! Pack it up! We're\x01",
            "returning to the Haken Gate!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13F2():
        OP_6D(48683, -3000, 30000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_13F2)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)
    OP_43(0xC, 0x1, 0x0, 0xB)
    Sleep(700)
    OP_43(0x9, 0x1, 0x0, 0xB)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0xB)
    Sleep(400)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(400)
    OP_43(0xA, 0x1, 0x0, 0xB)
    Sleep(1500)

    ChrTalk(    #36
        0xD,
        "#115F#6PIt looks like that's that...\x02",
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x72AD, 0x7D0, 0x0)

    ChrTalk(    #37
        0xD,
        (
            "#110F#5PIt seems that some of our personnel\x01",
            "were rather impolite.\x02\x03",

            "Please allow me to apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#020FI appreciate the gesture.\x02\x03",

            "But we made some slightly inflammatory\x01",
            "remarks as well, so how about we let\x01",
            "bygones be bygones?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "#110F#5PThat suits me just fine.\x02\x03",

            "As I stated before, the army is supposed\x01",
            "to be working closely with the guild...\x02\x03",

            "I think our two organizations working\x01",
            "together grants us each the ability to\x01",
            "make up for the other's shortcomings.\x02\x03",

            "I'm looking forward to any progress\x01",
            "you make with this recent series of\x01",
            "events.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        "#021FThank you. We'll do what we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#008F(He seems like a decent guy...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#010F(Yeah...I wonder who he is.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "#181FColonel... It's almost the\x01",
            "appointed time...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #44
        0xD,
        (
            "#113F#5POh, already?\x02\x03",

            "#110FExcuse me...but it appears\x01",
            "I must take my leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x7611, 0x7D0, 0x0)
    Sleep(400)

    ChrTalk(    #45
        0xD,
        (
            "#115F#6POh, but before I do, it looks like I\x01",
            "haven't properly introduced myself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)
    Sleep(400)

    NpcTalk(    #46
        0xD,
        "Colonel Richard",
        (
            "#110F#6PI am Alan Richard, a colonel in the\x01",
            "Royal Army.\x02\x03",

            "If there is anything I can do to assist\x01",
            "you, please don't hesitate to contact\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_8C(0xD, 0, 400)

    def lambda_190E():
        OP_8E(0xD, 0xBDF2, 0x0, 0x99DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_190E)
    Sleep(900)
    OP_8C(0xE, 0, 400)

    def lambda_1935():
        OP_8E(0xE, 0xBA4C, 0x0, 0x99DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1935)
    OP_21()
    OP_1E()
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    ChrTalk(    #47
        0x101,
        (
            "#505FColonel Richard...? I feel like\x01",
            "I've heard that name somewhere\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        (
            "#010FNial was the one who mentioned\x01",
            "his name earlier.\x02\x03",

            "He said something about him being a\x01",
            "sharp, young officer who leads the\x01",
            "Royal Army's Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#506FOh, right.\x02\x03",

            "#006FWow. For someone in the military, he\x01",
            "sure knows how to listen to others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#021FHmm...probably in his mid-thirties,\x01",
            "and he's not hard on the eyes\x01",
            "either...\x02\x03",

            "He seems like he's more fit to be\x01",
            "a politician than a service member\x01",
            "in the army.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 55617, -2500, 33010, 270)
    SetChrPos(0x10, 55617, -2500, 33010, 270)

    NpcTalk(    #51
        0xF,
        "Man's Voice",
        "#3PHey, you guys!\x02",
    )

    CloseMessageWindow()

    def lambda_1BCA():
        OP_6D(49974, -3000, 30500, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1BCA)

    def lambda_1BE2():

        label("loc_1BE2")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1BE2")

    QueueWorkItem2(0x0, 1, lambda_1BE2)

    def lambda_1BF3():

        label("loc_1BF3")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1BF3")

    QueueWorkItem2(0x1, 1, lambda_1BF3)

    def lambda_1C04():

        label("loc_1C04")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1C04")

    QueueWorkItem2(0x2, 1, lambda_1C04)

    def lambda_1C15():

        label("loc_1C15")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1C15")

    QueueWorkItem2(0x3, 1, lambda_1C15)

    def lambda_1C26():
        OP_8E(0xFE, 0xC45E, 0xFFFFF448, 0x7A19, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C26)
    ClearChrFlags(0x10, 0x80)
    Sleep(500)

    def lambda_1C4B():
        OP_8E(0xFE, 0xC8DC, 0xFFFFF448, 0x78E9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C4B)
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0x101, 400)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #52
        0xF,
        (
            "#140F#4PWho was that you were just talking\x01",
            "to in the black uniform?\x02\x03",

            "I could swear I've seen him\x01",
            "somewhere before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#006F#1PAre you trying to tell me you\x01",
            "didn't recognize him at all?\x02\x03",

            "That was Colonel Richard of the\x01",
            "Intelligence Division. You know,\x01",
            "the guy you mentioned earlier.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0xF,
        (
            "#143F#4PWh-What?\x02\x03",

            "You're not pulling my leg,\x01",
            "are you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#004F#1PAs fun as that would be...nope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#010F#1PHe said so himself, so I'm fairly\x01",
            "confident he is who he says he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        (
            "#141F#4PTo think that the legend himself\x01",
            "would show up here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #58
        0xF,
        (
            "#144FWe can't wait around here like\x01",
            "this any longer, Dorothy! Let's\x01",
            "see if we can catch up to him!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #59
        0x10,
        (
            "#151FAye, aye, sir! ...Although I'm really\x01",
            "not sure why we're chasing after\x01",
            "anyone...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FD5():
        OP_8E(0xF, 0xBAA4, 0x0, 0x99DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1FD5)
    Sleep(300)
    OP_8E(0x10, 0xBAA4, 0x0, 0x99DE, 0x1770, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    ChrTalk(    #60
        0x101,
        (
            "#008F#1PDid you see his eyes light up?\x01",
            "I wonder if he's going to do an\x01",
            "interview or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x103,
        (
            "#021F#2PHa ha. Anyone else in the army\x01",
            "would brush him off, but I'm sure\x01",
            "the colonel will oblige him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        "#032F#2PHmm...\x02",
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_2106():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2106)

    def lambda_2114():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2114)

    def lambda_2122():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2122)

    def lambda_2130():
        OP_6D(48950, -3000, 29000, 1200)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2130)
    Sleep(1200)

    ChrTalk(    #63
        0x101,
        (
            "#004FWhat's the matter with you, Olivier?\x01",
            "You look serious...and I gotta say,\x01",
            "I find it creepy coming from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x104,
        (
            "#032F#2PI was just thinking about the\x01",
            "colonel.\x02\x03",

            "I'll be the first to admit that he's\x01",
            "quite the specimen of a man...\x02\x03",

            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#014FBut...what?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 225, 400)
    OP_62(0x104, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(    #66
        0x104,
        (
            "#031F#2PI can say with confidence that he\x01",
            "doesn't stand a chance against\x01",
            "me when it comes to the ladies.\x02\x03",

            "But I'd like to see him try just a\x01",
            "little harder... It's no fun without\x01",
            "a romantic rival...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        (
            "#007F...\x01",
            "You just HAD to ask, didn't you,\x01",
            "Joshua...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#019F...I'll regret it for the rest of\x01",
            "my life.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104)

    ChrTalk(    #69
        0x103,
        (
            "#020FHa ha ha...\x01",
            "All right, let's see here...\x02\x03",

            "Now that the soldiers are gone,\x01",
            "how about we resume our own\x01",
            "investigation?\x02\x03",

            "Let's start by talking to all the\x01",
            "people we couldn't talk to earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#006FGood idea.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_24CF")

    Return()

    # Function_10_873 end

    def Function_11_24D0(): pass

    label("Function_11_24D0")

    OP_8E(0xFE, 0xCE6C, 0xFFFFF448, 0x70AC, 0x1388, 0x0)
    OP_8E(0xFE, 0xDB2C, 0xFFFFFB1E, 0x70E9, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_24D0 end

    def Function_12_24FE(): pass

    label("Function_12_24FE")

    EventBegin(0x0)
    OP_6D(44480, -3000, 27780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 43850, -3000, 27070, 45)
    SetChrPos(0x102, 45240, -3000, 27130, 270)
    SetChrPos(0x103, 45170, -3000, 28450, 225)
    SetChrPos(0x104, 43750, -3000, 28620, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #71
        0x103,
        (
            "#020FThough there weren't any definitive\x01",
            "clues related to the incident...\x02\x03",

            "We did manage to hear a few\x01",
            "interesting bits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x104,
        (
            "#035FI concur.\x02\x03",

            "I especially liked the one that\x01",
            "described all the delicious\x01",
            "food at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#007FThat's not what we're talking\x01",
            "about here!\x02\x03",

            "#000F...Although I did find the fishing\x01",
            "part to be rather interesting...\x02\x03",

            "Unfortunately, if there's nothing going\x01",
            "on there then I guess it wouldn't be\x01",
            "worth investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#015FActually, I think it's quite the\x01",
            "opposite.\x02\x03",

            "If someone had been careless and caused a\x01",
            "problem, the army would've thoroughly\x01",
            "investigated it.\x02\x03",

            "Conversely, the possibility of the\x01",
            "sky bandits appearing where there's\x01",
            "nothing happening is rather high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#002FOh...well, I guess that's one way\x01",
            "to think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#022FAnd in light of this series of\x01",
            "incidents...\x02\x03",

            "There's either a spy in the army,\x01",
            "or the sky bandits are a really\x01",
            "clever bunch of thieves.\x02\x03",

            "It'll be extremely difficult to corner\x01",
            "them only by investigating the\x01",
            "incidents which have occurred.\x02\x03",

            "We'll need to get one step ahead of\x01",
            "them by tracking their movements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#006FI see...so what you're saying is that\x01",
            "we should take an offensive stance\x01",
            "rather than a defensive one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x104,
        (
            "#035FHmm. Then how about we get\x01",
            "going?\x02\x03",

            "Off to the beautiful Valleria Lake,\x01",
            "extolled in many a rhyme as the 'pearl\x01",
            "of Liberl'...\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0xD, 0x0, 0xFFFF)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x1, 0x0, 0xFFFF)
    OP_1B(0x2, 0x0, 0xFFFF)
    EventEnd(0x0)
    Return()

    # Function_12_24FE end

    def Function_13_2AD8(): pass

    label("Function_13_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D01")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFC")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2B03")

    label("loc_2AFC")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2BAE")

    ChrTalk(    #79
        0x103,
        (
            "#027FGoing somewhere else to investigate\x01",
            "isn't going to help us right now.\x02\x03",

            "We should first start by talking\x01",
            "to all the people we couldn't\x01",
            "talk to earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CAB")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5A")
    OP_A2(0x0)

    ChrTalk(    #80
        0x103,
        (
            "#020FThere's probably still some important\x01",
            "information we haven't gathered.\x02\x03",

            "We should continue to ask around\x01",
            "a bit longer and see what we come\x01",
            "up with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CAB")

    label("loc_2C5A")


    ChrTalk(    #81
        0x103,
        (
            "#020FCome on, let's keep asking around\x01",
            "for details regarding the incidents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CAB")

    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)
    Jump("loc_2E97")

    label("loc_2D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB4")
    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(    #82
        0x134,
        (
            "#620FWhere are you all headed?\x02\x03",

            "The mayor is in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)
    Jump("loc_2E97")

    label("loc_2DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E97")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD4")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2DDB")

    label("loc_2DD4")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2DDB")


    ChrTalk(    #83
        0x103,
        (
            "#020FLet's first stop by the guild and find\x01",
            "out about the ongoing situation.\x02\x03",

            "The Bose branch is in the north\x01",
            "block.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)

    label("loc_2E97")

    Return()

    # Function_13_2AD8 end

    def Function_14_2E98(): pass

    label("Function_14_2E98")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB0")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2EB7")

    label("loc_2EB0")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2F62")

    ChrTalk(    #84
        0x103,
        (
            "#027FGoing somewhere else to investigate\x01",
            "isn't going to help us right now.\x02\x03",

            "We should first start by talking\x01",
            "to all the people we couldn't\x01",
            "talk to earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305F")

    label("loc_2F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300E")
    OP_A2(0x0)

    ChrTalk(    #85
        0x103,
        (
            "#020FThere's probably still some important\x01",
            "information we haven't gathered.\x02\x03",

            "We should continue to ask around\x01",
            "a bit longer and see what we come\x01",
            "up with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_305F")

    label("loc_300E")


    ChrTalk(    #86
        0x103,
        (
            "#020FCome on, let's keep asking around\x01",
            "for details regarding the incidents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_305F")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_2E98 end

    def Function_15_307B(): pass

    label("Function_15_307B")

    SetPlaceName(0x22)
    Return()

    # Function_15_307B end

    def Function_16_307F(): pass

    label("Function_16_307F")

    SetPlaceName(0x24)
    Return()

    # Function_16_307F end

    SaveToFile()

Try(main)

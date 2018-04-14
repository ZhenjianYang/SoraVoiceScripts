from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0811   ._SN',
        MapName             = 'Event',
        Location            = 'E0811.x',
        MapIndex            = 1,
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
        '艾丝蒂尔',                             # 9
        '约修亚',                               # 10
        '乔丝特',                               # 11
        '吉尔',                                 # 12
        '多伦',                                 # 13
        '结社艇',                               # 14
        '结社艇右',                             # 15
        '空贼艇',                               # 16
        '空贼艇右',                             # 17
        '提妲',                                 # 18
        '科洛丝',                               # 19
        '阿加特',                               # 20
        '雪拉扎德',                             # 21
        '金',                                   # 22
        '凯文神父',                             # 23
        '拉赛尔博士',                           # 24
        '尤莉亚上尉',                           # 25
        '目标',                                 # 26
        '目标',                                 # 27
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
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT26/CH20370 ._CH',             # 02
        'ED6_DT26/CH20400 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT27/CH03015 ._CH',             # 05
        'ED6_DT26/CH20401 ._CH',             # 06
        'ED6_DT27/CH03101 ._CH',             # 07
        'ED6_DT26/CH20398 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT07/CH00040 ._CH',             # 0A
        'ED6_DT07/CH00050 ._CH',             # 0B
        'ED6_DT07/CH00020 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT27/CH03080 ._CH',             # 0E
        'ED6_DT07/CH02020 ._CH',             # 0F
        'ED6_DT27/CH03580 ._CH',             # 10
        'ED6_DT07/CH00061 ._CH',             # 11
        'ED6_DT07/CH00041 ._CH',             # 12
        'ED6_DT07/CH00051 ._CH',             # 13
        'ED6_DT07/CH00021 ._CH',             # 14
        'ED6_DT07/CH00071 ._CH',             # 15
        'ED6_DT27/CH03081 ._CH',             # 16
        'ED6_DT27/CH03001 ._CH',             # 17
        'ED6_DT27/CH03011 ._CH',             # 18
        'ED6_DT26/CH20327 ._CH',             # 19
        'ED6_DT26/CH20398 ._CH',             # 1A
        'ED6_DT27/CH03000 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT26/CH20370P._CP',             # 02
        'ED6_DT26/CH20400P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT27/CH03015P._CP',             # 05
        'ED6_DT26/CH20401P._CP',             # 06
        'ED6_DT27/CH03101P._CP',             # 07
        'ED6_DT26/CH20398P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT07/CH00040P._CP',             # 0A
        'ED6_DT07/CH00050P._CP',             # 0B
        'ED6_DT07/CH00020P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT27/CH03080P._CP',             # 0E
        'ED6_DT07/CH02020P._CP',             # 0F
        'ED6_DT27/CH03580P._CP',             # 10
        'ED6_DT07/CH00061P._CP',             # 11
        'ED6_DT07/CH00041P._CP',             # 12
        'ED6_DT07/CH00051P._CP',             # 13
        'ED6_DT07/CH00021P._CP',             # 14
        'ED6_DT07/CH00071P._CP',             # 15
        'ED6_DT27/CH03081P._CP',             # 16
        'ED6_DT27/CH03001P._CP',             # 17
        'ED6_DT27/CH03011P._CP',             # 18
        'ED6_DT26/CH20327P._CP',             # 19
        'ED6_DT26/CH20398P._CP',             # 1A
        'ED6_DT27/CH03000P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x1C4,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x1CC,
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
        NpcIndex            = 0x1CC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -100290,
        Y                   = 5150,
        Z                   = -94850,
        Range               = -98290,
        Unknown_10          = 0x1BEE,
        Unknown_14          = 0xFFFE954E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_40A",          # 00, 0
        "Function_1_57B",          # 01, 1
        "Function_2_581",          # 02, 2
        "Function_3_621",          # 03, 3
        "Function_4_14F7",         # 04, 4
        "Function_5_1511",         # 05, 5
        "Function_6_1555",         # 06, 6
        "Function_7_15D2",         # 07, 7
        "Function_8_1738",         # 08, 8
        "Function_9_19AA",         # 09, 9
        "Function_10_1FAC",        # 0A, 10
        "Function_11_1FEB",        # 0B, 11
        "Function_12_2124",        # 0C, 12
        "Function_13_2151",        # 0D, 13
        "Function_14_217E",        # 0E, 14
        "Function_15_3070",        # 0F, 15
        "Function_16_30D2",        # 10, 16
        "Function_17_3114",        # 11, 17
        "Function_18_31B6",        # 12, 18
        "Function_19_3275",        # 13, 19
        "Function_20_32DF",        # 14, 20
        "Function_21_3349",        # 15, 21
        "Function_22_3488",        # 16, 22
        "Function_23_35C7",        # 17, 23
        "Function_24_3640",        # 18, 24
        "Function_25_36B9",        # 19, 25
        "Function_26_3750",        # 1A, 26
        "Function_27_37E7",        # 1B, 27
        "Function_28_391D",        # 1C, 28
        "Function_29_3A2B",        # 1D, 29
        "Function_30_3C5E",        # 1E, 30
        "Function_31_3E91",        # 1F, 31
        "Function_32_417E",        # 20, 32
        "Function_33_41DC",        # 21, 33
        "Function_34_423A",        # 22, 34
        "Function_35_4267",        # 23, 35
        "Function_36_4294",        # 24, 36
        "Function_37_43E9",        # 25, 37
        "Function_38_45CE",        # 26, 38
        "Function_39_47DD",        # 27, 39
        "Function_40_4AEE",        # 28, 40
        "Function_41_4BD6",        # 29, 41
        "Function_42_4CE8",        # 2A, 42
        "Function_43_52B0",        # 2B, 43
        "Function_44_531F",        # 2C, 44
        "Function_45_53AA",        # 2D, 45
        "Function_46_53EE",        # 2E, 46
        "Function_47_5439",        # 2F, 47
        "Function_48_5484",        # 30, 48
        "Function_49_54CF",        # 31, 49
        "Function_50_551A",        # 32, 50
        "Function_51_5565",        # 33, 51
        "Function_52_55A9",        # 34, 52
        "Function_53_55DE",        # 35, 53
        "Function_54_5613",        # 36, 54
        "Function_55_569D",        # 37, 55
    )


    def Function_0_40A(): pass

    label("Function_0_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_41B")
    OP_A3(0x10F0)
    Event(0, 3)
    Jump("loc_57A")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_435")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 9)
    Jump("loc_57A")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_44F")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_57A")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_469")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 31)
    Jump("loc_57A")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_47A")
    OP_A3(0x10F4)
    Event(0, 37)
    Jump("loc_57A")

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_494")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 8)
    Jump("loc_57A")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_4AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    Event(0, 2)
    Jump("loc_57A")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_4C8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F7)
    Event(0, 39)
    Jump("loc_57A")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_51E")
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_A3(0x10F8)
    Event(0, 41)
    Jump("loc_57A")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_57A")
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    Event(0, 42)

    label("loc_57A")

    Return()

    # Function_0_40A end

    def Function_1_57B(): pass

    label("Function_1_57B")

    OP_71(0x5, 0x4)
    Return()

    # Function_1_57B end

    def Function_2_581(): pass

    label("Function_2_581")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-213310, -10000, -14980, 0)
    OP_67(0, -2490, -10000, 0)
    OP_6B(43240, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    FadeToBright(2000, 0)

    def lambda_5ED():
        OP_67(0, -3300, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5ED)
    Sleep(7000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1211   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_581 end

    def Function_3_621(): pass

    label("Function_3_621")

    EventBegin(0x0)
    ClearParty()
    AddParty(0x1, 0xF6, 0xFF)
    SetChrFlags(0x102, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xF, 0x3)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    OP_48()
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 400)
    OP_70(0x3, 0x1C2)
    OP_6D(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    OP_6B(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    OP_BB(0x1, 0x1, 0x1)
    OP_BD()
    FadeToBright(2000, 0)

    def lambda_6D5():
        OP_6D(-99550, 5550, -94010, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D5)

    def lambda_6ED():
        OP_6B(2800, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_6ED)

    def lambda_6FD():
        OP_6E(334, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FD)
    Sleep(6000)
    OP_72(0x3, 0x20)

    def lambda_717():
        OP_6C(35000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_717)
    OP_67(0, 7540, -10000, 4000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x4)
    SetChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -99440, 5550, -91440, 0)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFE7B72, 0x15A4, 0xFFFE90F8, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    ChrTalk(    #0
        0xA,
        "#213F咦……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(500)
    OP_8C(0xA, 180, 400)
    OP_8C(0xA, 270, 400)
    Sleep(500)
    OP_8C(0xA, 180, 400)
    Sleep(500)
    OP_8C(0xA, 90, 400)
    Sleep(200)
    SetChrPos(0x102, -100000, 5550, -89650, 0)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 2)
    SetChrSubChip(0x102, 2)
    OP_43(0xA, 0x1, 0x0, 0x5)

    def lambda_81A():
        OP_6D(-98020, 5550, -89450, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_81A)
    OP_6C(300000, 5000)
    OP_6C(212000, 5000)

    ChrTalk(    #1
        0xA,
        "#210F怎么，原来在这里啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)

    ChrTalk(    #2
        0x102,
        (
            "#1030F……这边可以\x01",
            "比较清楚地看到月亮呢。\x02\x03",

            "肌肤也能感到风的流动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        (
            "#210F哈哈，又～开始\x01",
            "装模作样了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FD():
        OP_6D(-99380, 5550, -89630, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8FD)

    def lambda_915():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_915)

    def lambda_925():
        OP_8E(0xA, 0xFFFE7D34, 0x15AE, 0xFFFEA296, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_925)
    Sleep(300)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    WaitChrThread(0xA, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x102, 0x1)
    Fade(250)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(    #4
        0xA,
        (
            "#210F……哟。\x02\x03",

            "其实你这并不是在\x01",
            "装模作样的吧……\x02\x03",

            "这也是必要的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1030F因为月光、云的位置、风的流向\x01",
            "都变得相当重要了。\x02\x03",

            "我希望把失败的可能性\x01",
            "尽量降到最低。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "#210F尽、尽量？……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 4)
    Sleep(100)

    ChrTalk(    #7
        0xA,
        (
            "#210F我说你啊……\x01",
            "可别说什么能尽力而为的话哦！\x02\x03",

            "失败了就是死路一条哦！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1030F没关系，失败的可能性很小。\x02\x03",

            "这种程度的任务，\x01",
            "以前每天都在做。\x02\x03",

            "倒不如说更大的危险……\x01",
            "是在任务成功之后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "#210F………………………………\x02\x03",

            "……我说，约修亚。\x02\x03",

            "你真的\x01",
            "有必要做到这一步吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(100)

    ChrTalk(    #10
        0x102,
        "#1030F嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "#210F你也和我们一样\x01",
            "是埃雷波尼亚出身的吧。\x02\x03",

            "虽然说彼此或许各有隐情\x01",
            "而不能返回故乡……\x02\x03",

            "但就算是这样，你也没必要\x01",
            "为这个国家尽什么义务不是吗？\x02\x03",

            "『结社』要做什么，\x01",
            "放着不管不就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1030F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#210F好不好，现在还来得及。\x02\x03",

            "就这样，与我们一起\x01",
            "离开利贝尔……\x02\x03",

            "去找个自治州\x01",
            "揭竿而起怎么样？\x02\x03",

            "如果不想做空贼\x01",
            "也可以找其他的工作。\x02\x03",

            "我和哥哥们也说过了，\x01",
            "利用这艘船的速度\x01",
            "来做运输业应该不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 6)
    Sleep(100)

    ChrTalk(    #14
        0x102,
        (
            "#1030F用飞船做运输业吗……\x02\x03",

            "今后的需求也会陆续增加，\x01",
            "或许是相当有前途的行业呢。\x02\x03",

            "至少应该能赚得\x01",
            "比当空贼还多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "#210F那、那就！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(100)

    ChrTalk(    #16
        0x102,
        (
            "#1030F是啊……\x02\x03",

            "粉碎了『结社』的阴谋之后\x01",
            "如果我还活着\x01",
            "就考虑考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        "#210F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1030F嗯，你不必担心\x01",
            "我们的契约到此就结束了。\x02\x03",

            "只要配合这个作战计划，\x01",
            "之前欠我的人情就一笔勾销了。\x02\x03",

            "你们随时都可以出发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        "#210F……够了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1030F咦。\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    Fade(500)
    OP_8C(0xA, 270, 0)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(    #21
        0xA,
        (
            "#210F笨蛋！\x01",
            "谁在说什么欠人情的事！\x02\x03",

            "不用说了！\x01",
            "谁知道你是谁啊！\x02\x03",

            "爱跳火坑就跳\x01",
            "你愿意见鬼就见鬼去吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xA, 0xFFFE8E3C, 0x15AE, 0xFFFEA070, 0x1388, 0x0)
    OP_8E(0xA, 0xFFFE8DA6, 0x15AE, 0xFFFE94FE, 0x1388, 0x0)
    OP_8E(0xA, 0xFFFE7BC2, 0x15AE, 0xFFFE910C, 0x1388, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    SetChrFlags(0xA, 0x80)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(100)

    ChrTalk(    #22
        0x102,
        (
            "#1030F………………………………\x02\x03",

            "……对不起，乔丝特。\x02",
        )
    )

    CloseMessageWindow()
    SetChrBattleFlags(0xB, 0x20)
    SetChrPos(0xB, -103120, 13050, -91360, 10)
    Sleep(300)

    NpcTalk(    #23
        0xB,
        "青年的声音",
        (
            "#3P真是的……\x01",
            "假装迟钝可真没意思啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_6F(0x3, 90)
    SetChrPos(0xB, -103120, 9050, -91360, 10)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    Fade(500)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    OP_8C(0x102, 270, 400)

    def lambda_10EB():
        OP_6D(-100330, 5550, -92350, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10EB)

    def lambda_1103():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1103)
    OP_6C(144000, 4000)
    Sleep(300)

    ChrTalk(    #24
        0x102,
        "#1030F……吉尔先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        (
            "#200F那家伙也是一样，\x01",
            "脱离不了小孩子个性……\x02\x03",

            "不过，刚才毕竟是\x01",
            "你的说话方式不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1030F……是啊。\x02\x03",

            "虽然并不打算道歉，\x01",
            "但还是觉得对不起她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#200F真是的……\x01",
            "虽然知道这就是你\x01",
            "关心别人的方式。\x02\x03",

            "不过，刚才的话\x01",
            "还是认真考虑一下吧。\x02\x03",

            "等一切都了结之后，\x01",
            "要是你不打算回那个\x01",
            "游击士小姑娘身边的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1030F哈哈……不会的。\x02\x03",

            "毕竟，我和她\x01",
            "生存的世界差距太大了。\x02\x03",

            "不可能再有交集了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#200F嗯……\x01",
            "嗯，那也好。\x02\x03",

            "既然这样就\x01",
            "更好说话了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1030F是啊……\x01",
            "我会积极考虑的。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAB, 0x1, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(2200)
    OP_23(0xAB)

    ChrTalk(    #31
        0xB,
        "#200F……出现了吗！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    SetChrPos(0xB, -103120, 8900, -91360, 270)
    Sleep(500)

    ChrTalk(    #32
        0xB,
        "#200F大哥，来了吗！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, -103120, 6550, -91360, 270)

    NpcTalk(    #33
        0xC,
        "多伦的声音",
        (
            "哟！\x01",
            "正如小子预料的一样！\x02\x03",

            "从东北方向\x01",
            "不断接近中呢！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -103120, 9050, -91360, 270)
    OP_8C(0xB, 10, 400)

    ChrTalk(    #34
        0xB,
        (
            "#200F你听到了吧。\x01",
            "马上过来舰桥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1030F明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_43(0xB, 0x1, 0x0, 0x4)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 90)
    OP_70(0x3, 0xA0)
    OP_A2(0x1C00)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x00◆这个剧情使用的临时地图。\x01",
            "　进入船内的时候请按DEBUG键『J』来接触入口附近。\x01",
            "　接触临时入口就能进入里面。\x02",
        )
    )

    Sleep(1000)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_621 end

    def Function_4_14F7(): pass

    label("Function_4_14F7")

    OP_8F(0xFE, 0xFFFE6D30, 0x17A2, 0xFFFE9B20, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_14F7 end

    def Function_5_1511(): pass

    label("Function_5_1511")

    OP_8E(0xFE, 0xFFFE8F54, 0x15AE, 0xFFFE951C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8EC8, 0x15AE, 0xFFFE9FC6, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8C52, 0x15AE, 0xFFFEA0FC, 0x5DC, 0x0)
    OP_8C(0xFE, 305, 400)
    Return()

    # Function_5_1511 end

    def Function_6_1555(): pass

    label("Function_6_1555")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00◆临时入口【≡ 空贼艇内部夜用（E0110）】\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BC")
    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_15D1")

    label("loc_15BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D1")
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_15D1")

    Return()

    # Function_6_1555 end

    def Function_7_15D2(): pass

    label("Function_7_15D2")

    EventBegin(0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    SetChrFlags(0x102, 0x80)
    OP_A1(0xD, 0x2)
    OP_A1(0xF, 0x3)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    OP_6D(43700, -10000, 9730, 0)
    OP_67(0, 640, -10000, 0)
    OP_6B(43830, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)

    def lambda_16AD():
        OP_6B(32830, 4000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16AD)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xB, 0x1)
    OP_22(0x7C, 0x0, 0x64)
    OP_6D(116270, -10000, 41470, 0)
    OP_67(0, 1020, -10000, 0)
    OP_6B(18860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    SetMapFlags(0x2000000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AE(0x1388)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_15D2 end

    def Function_8_1738(): pass

    label("Function_8_1738")

    EventBegin(0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    SetChrFlags(0x102, 0x80)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 100000, 4000, 0, 270)
    SetChrPos(0xE, 100000, 4000, 0, 90)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_11(0x38, 0x44, 0x58, 0x4E20, 0xF4240, 0x0)
    OP_6D(1000, 2700, 2800, 0)
    OP_67(0, 680, -10000, 0)
    OP_6B(36240, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x1E)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    FadeToBright(500, 0)

    def lambda_1856():
        OP_6B(22830, 6000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1856)

    def lambda_1866():
        OP_8F(0xFE, 0x0, 0xFA0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1866)

    def lambda_1881():
        OP_8F(0xFE, 0x0, 0xFA0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1881)
    Sleep(6400)
    FadeToDark(100, 0, -1)
    OP_0D()
    Sleep(200)
    OP_22(0x7C, 0x0, 0x64)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    SetChrPos(0xD, 10000, 4000, 0, 270)
    SetChrPos(0xE, 10000, 4000, 0, 270)
    OP_6D(116270, -10000, 41470, 0)
    OP_67(0, 1320, -10000, 0)
    OP_6B(19860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    SetMapFlags(0x2000000)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    Sleep(400)

    def lambda_194E():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_194E)

    def lambda_1969():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1969)
    FadeToBright(100, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AE(0x1388)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1738 end

    def Function_9_19AA(): pass

    label("Function_9_19AA")

    EventBegin(0x0)
    OP_71(0x1, 0x4)
    OP_6D(-105420, 5550, -91410, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x3C)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    SetChrPos(0x10, -99500, 0, -91500, 270)
    FadeToBright(1000, 0)

    def lambda_1A69():
        OP_6D(-95530, 5550, -92450, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A69)

    def lambda_1A81():
        OP_67(0, 6080, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A81)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x1)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(1700)
    SetChrFlags(0xA, 0x4)
    SetChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -99420, 5550, -90790, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xA, 0xFFFE7BE0, 0x15AE, 0xFFFE9152, 0xFA0, 0x0)
    OP_8E(0xA, 0xFFFE86D0, 0x15AE, 0xFFFE9382, 0xFA0, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 6)
    SetChrSubChip(0xA, 1)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #38
        0x102,
        "#1034F#5P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_1B40():
        OP_6B(2900, 12000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1B40)

    ChrTalk(    #39
        0xA,
        (
            "#214F到了最后的最后，\x01",
            "还是个一点都不可爱的家伙！\x02\x03",

            "还一本正经地说什么\x01",
            "『这段时间谢谢你们了』。\x02\x03",

            "#215F听到这种话，\x01",
            "我一点也高兴不起来！\x02\x03",

            "我不想听你说这种话！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#1033F#5P……乔丝特……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0xA,
        (
            "#413F……答应我啊。\x02\x03",

            "绝对不能勉强自己……\x02\x03",

            "你一定要活着回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1033F#5P………………………………\x02\x03",

            "#1035F我不能够\x01",
            "轻易承诺你的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "#417F……！………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1031F#5P不过……有一点我可以答应你。\x02\x03",

            "即使我的目的\x01",
            "没能达成……\x02\x03",

            "#1053F我也一定会活着回来，\x01",
            "找个时间再次向你们道谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "#414F啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x3)
    Fade(250)
    SetChrSubChip(0xA, 1)
    OP_0D()

    def lambda_1D5E():
        OP_6D(-95030, 5550, -92450, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D5E)
    OP_8E(0x102, 0xFFFE89B4, 0x15AE, 0xFFFE9404, 0x1F4, 0x0)
    Sleep(500)
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #46
        0x102,
        "#1031F#2P……这样可以了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        "#416F#6P嗯……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 0)
    TurnDirection(0xA, 0x102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0xA,
        (
            "#415F#6P别忘记啦！\x01",
            "这是我们约定好的哦！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-1880, 5550, -1900, 0)
    OP_67(0, 1380, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(66000, 0)
    OP_6E(861, 0)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 150000, 6000, 150000, 270)
    SetChrPos(0xE, 150000, 6000, 150000, 270)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x1E)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 180000, 0, 0)
    OP_D1(14, 0, 180000, 0, 0)
    OP_43(0xD, 0x0, 0x0, 0xB)
    Sleep(3800)
    OP_1D(0x51)
    FadeToBright(2000, 0)
    Sleep(6000)

    def lambda_1F68():
        OP_6D(-19030, 5550, -4550, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F68)

    def lambda_1F80():
        OP_6C(310000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F80)
    Sleep(3200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_19AA end

    def Function_10_1FAC(): pass

    label("Function_10_1FAC")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -99420, 5550, -90790, 180)
    OP_8E(0xFE, 0xFFFE7BE0, 0x15AE, 0xFFFE9152, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE88A6, 0x15AE, 0xFFFE93B4, 0x7D0, 0x0)
    Return()

    # Function_10_1FAC end

    def Function_11_1FEB(): pass

    label("Function_11_1FEB")


    def lambda_1FF1():
        OP_D1(254, 0, 230000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1FF1)

    def lambda_200B():
        OP_D1(254, 0, 230000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_200B)

    def lambda_2025():
        OP_8F(0xFE, 0x249F0, 0xFA0, 0xC350, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2025)

    def lambda_2040():
        OP_8F(0xFE, 0x249F0, 0xFA0, 0xC350, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2040)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)
    OP_43(0xD, 0x1, 0x0, 0xC)
    OP_43(0xE, 0x1, 0x0, 0xD)

    def lambda_2073():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2073)

    def lambda_208D():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_208D)

    def lambda_20A7():
        OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_20A7)

    def lambda_20C3():
        OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_20C3)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)

    def lambda_20E9():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_20E9)

    def lambda_2104():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2104)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)
    Return()

    # Function_11_1FEB end

    def Function_12_2124(): pass

    label("Function_12_2124")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2145")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_12_2124")

    label("loc_2145")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_2124 end

    def Function_13_2151(): pass

    label("Function_13_2151")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2172")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_13_2151")

    label("loc_2172")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2151 end

    def Function_14_217E(): pass

    label("Function_14_217E")

    EventBegin(0x0)
    LoadEffect(0x1, "map\\mp091_00.eff")
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_71(0x1, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 50000, 0, 0, 270)
    SetChrPos(0xE, 50000, 0, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 20000, 0, 50000, 270)
    SetChrPos(0x10, 20000, 0, 50000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_6F(0x3, 360)
    OP_6F(0x4, 360)
    OP_6D(-36160, -10000, -5660, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(4740, 0)
    OP_6C(252000, 0)
    OP_6E(1357, 0)
    OP_D0(10000, 0)
    FadeToBright(1000, 0)

    def lambda_2319():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2319)

    def lambda_2334():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2334)
    Sleep(4000)
    OP_43(0xF, 0x0, 0x0, 0x19)
    OP_43(0x10, 0x0, 0x0, 0x1A)
    Sleep(9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(31120, -9250, -10030, 0)
    OP_67(0, 3530, -10000, 0)
    OP_6B(4740, 0)
    OP_6C(96000, 0)
    OP_6E(1357, 0)
    OP_D0(340000, 0)
    OP_44(0xD, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0x10, 0x0)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0xF, 60000, 7000, -30000, 270)
    SetChrPos(0x10, 60000, 7000, -30000, 270)
    OP_D1(15, 0, 290000, -25000, 0)
    OP_D1(16, 0, 290000, -25000, 0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 360)
    OP_70(0x4, 0x1CC)
    OP_43(0xF, 0x0, 0x0, 0x1B)
    OP_43(0x10, 0x0, 0x0, 0x1C)
    FadeToBright(1000, 0)
    Sleep(4500)

    def lambda_2474():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2474)

    def lambda_248F():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_248F)
    Sleep(100)

    def lambda_24AF():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_24AF)

    def lambda_24CA():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_24CA)
    Sleep(100)

    def lambda_24EA():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_24EA)

    def lambda_2505():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2505)
    Sleep(100)

    def lambda_2525():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2525)

    def lambda_2540():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2540)
    Sleep(100)

    def lambda_2560():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2560)

    def lambda_257B():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_257B)
    Sleep(100)

    def lambda_259B():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_259B)

    def lambda_25B6():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_25B6)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-49540, -6000, 10420, 0)
    OP_6C(337000, 0)
    OP_67(0, 2080, -10000, 0)
    OP_6E(1357, 0)
    OP_6B(4740, 0)
    OP_D0(370000, 0)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    SetChrPos(0xD, 0, -1000, 0, 270)
    SetChrPos(0xE, 0, -1000, 0, 270)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 40000, 4000, 30000, 270)
    SetChrPos(0x10, 40000, 4000, 30000, 270)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 260000, 0, 0)
    FadeToBright(1000, 0)
    OP_43(0xD, 0x0, 0x0, 0x15)
    OP_43(0xE, 0x0, 0x0, 0x16)
    OP_43(0xF, 0x0, 0x0, 0x1D)
    OP_43(0x10, 0x0, 0x0, 0x1E)
    Sleep(5000)

    def lambda_2701():
        OP_6D(-76150, -4350, -6420, 4400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2701)

    def lambda_2719():
        OP_6C(224000, 4400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2719)

    def lambda_2729():
        OP_D0(350000, 4400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2729)

    def lambda_2739():
        OP_D1(254, 0, 270000, -15000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2739)

    def lambda_2753():
        OP_D1(254, 0, 270000, -15000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2753)

    def lambda_276D():
        OP_D1(254, 0, 270000, -45000, 6000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_276D)

    def lambda_2787():
        OP_D1(254, 0, 270000, -45000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2787)
    WaitChrThread(0x102, 0x0)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)

    def lambda_27B6():
        OP_D1(254, 0, 270000, -45000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_27B6)

    def lambda_27D0():
        OP_D1(254, 0, 270000, -45000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_27D0)
    Sleep(100)

    def lambda_27EF():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27EF)

    def lambda_280A():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_280A)
    Sleep(100)

    def lambda_282A():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_282A)

    def lambda_2845():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2845)
    Sleep(100)

    def lambda_2865():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2865)

    def lambda_2880():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2880)
    Sleep(100)

    def lambda_28A0():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28A0)

    def lambda_28BB():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_28BB)
    Sleep(100)

    def lambda_28DB():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28DB)

    def lambda_28F6():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_28F6)
    Sleep(100)

    def lambda_2916():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2916)

    def lambda_2931():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2931)
    Sleep(100)

    def lambda_2951():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2951)

    def lambda_296C():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_296C)
    Sleep(2000)
    OP_44(0xD, 0x1)
    OP_44(0xD, 0x3)
    OP_44(0xE, 0x1)
    OP_44(0xE, 0x3)
    SetChrPos(0xD, -200000, -2000, 110000, 270)
    SetChrPos(0xE, -200000, -2000, 110000, 270)
    OP_D1(13, 0, 270000, 10000, 0)
    OP_D1(14, 0, 270000, 10000, 0)
    Sleep(2000)
    Fade(1000)
    OP_6D(-223070, -10000, 89110, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6C(273000, 0)
    OP_D0(370000, 0)
    OP_0D()
    OP_43(0x102, 0x0, 0x0, 0xF)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_44(0x102, 0x0)
    OP_89(0x102, -187360, 5630, 81990, 316)
    Fade(1000)
    OP_6D(-187360, 5630, 81990, 0)
    OP_67(0, 3240, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(174000, 0)
    OP_6E(429, 0)
    OP_D0(360000, 0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x102,
        "#1035F#6P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(2000, 500)
    OP_0D()

    ChrTalk(    #50
        0x102,
        "#1032F#6P好……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2B1A():
        OP_6D(-192600, 5630, 84510, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2B1A)

    def lambda_2B32():
        OP_67(0, 2960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B32)

    def lambda_2B4A():
        OP_6C(248000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2B4A)

    def lambda_2B5A():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2B5A)
    WaitChrThread(0xA, 0x0)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 0)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x2)

    def lambda_2B83():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B83)
    OP_8E(0x102, 0xFFFD189A, 0x15FE, 0x14230, 0x2710, 0x0)
    OP_44(0x102, 0x1)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 8)
    Sleep(200)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x102, 0x4)

    def lambda_2BCC():
        OP_99(0xFE, 0x8, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BCC)

    def lambda_2BDC():
        OP_96(0xFE, 0xFFFD0FF8, 0x14D2, 0x151C6, 0x4E2, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2BDC)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)

    def lambda_2C04():
        OP_99(0xFE, 0x10, 0x12, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C04)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2C23():
        OP_D1(254, 0, 270000, -4000, 100)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2C23)

    def lambda_2C3D():
        OP_D1(254, 0, 270000, -4000, 100)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2C3D)
    SetChrPos(0x102, -193320, 5330, 86470, 316)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 8)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2C7C():
        OP_D1(254, 0, 270000, 2000, 400)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2C7C)

    def lambda_2C96():
        OP_D1(254, 0, 270000, 2000, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2C96)

    def lambda_2CB0():
        OP_99(0xFE, 0x9, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CB0)

    def lambda_2CC0():
        OP_96(0xFE, 0xFFFCD966, 0xDCA, 0x1AB62, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CC0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10)
    OP_44(0x102, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x2)
    OP_44(0x102, 0x3)
    ClearChrBattleFlags(0x102, 0x20)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrPos(0xD, 136000, 1000, 50000, 270)
    SetChrPos(0xE, 136000, 1000, 50000, 270)
    OP_D1(13, 0, 260000, 10000, 0)
    OP_D1(14, 0, 260000, 10000, 0)
    SetChrPos(0x102, 0, 5000, 0, 270)
    SetChrPos(0x19, -350, 5900, 0, 270)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, -24650, 5900, 0, 270)
    ClearChrFlags(0x1A, 0x80)
    OP_6D(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)
    FadeToBright(1000, 0)
    OP_43(0x102, 0x0, 0x0, 0x12)

    def lambda_2DEF():
        OP_9E(0xFE, 0xA, 0xA, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DEF)

    def lambda_2E09():
        OP_6B(3260, 3750)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2E09)

    def lambda_2E19():
        OP_6D(-10900, 5000, -1600, 3750)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E19)

    def lambda_2E31():
        OP_67(0, 2040, -10000, 3750)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2E31)

    def lambda_2E49():
        OP_6C(246000, 3750)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2E49)

    def lambda_2E59():
        OP_8F(0xFE, 0xFFFA7220, 0x3E8, 0xFFFE7960, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E59)

    def lambda_2E74():
        OP_8F(0xFE, 0xFFFA7220, 0x3E8, 0xFFFE7960, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2E74)
    Sleep(2500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    OP_82(0x1, 0x0)
    Fade(500)
    OP_22(0xD6, 0x0, 0x64)
    OP_44(0x102, 0xFF)
    ClearChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x8000)
    SetChrChipByIndex(0x102, 25)
    SetChrSubChip(0x102, 0)
    OP_8C(0x102, 270, 0)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    SetChrPos(0x19, 100000, 0, 0, 270)
    SetChrPos(0x1A, 101000, 0, 0, 270)
    OP_43(0x102, 0x0, 0x0, 0x11)
    PlayEffect(0x1, 0x1, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    OP_D1(13, 0, 270000, 10000, 0)
    OP_D1(14, 0, 270000, 10000, 0)
    SetChrPos(0xD, 40000, 1000, 0, 270)
    SetChrPos(0xE, 40000, 1000, 0, 270)
    OP_6D(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)

    def lambda_2FB9():
        OP_8F(0xFE, 0xFFF9E580, 0x3E8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2FB9)

    def lambda_2FD4():
        OP_8F(0xFE, 0xFFF9E580, 0x3E8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2FD4)

    def lambda_2FEF():
        OP_6D(2880, 10000, 6720, 4000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2FEF)

    def lambda_3007():
        OP_67(0, 1320, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3007)

    def lambda_301F():
        OP_6C(268000, 4500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_301F)
    Sleep(15)
    WaitChrThread(0xA, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x8000)
    OP_82(0x1, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetMapFlags(0x2000000)
    SetMapFlags(0x10)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_217E end

    def Function_15_3070(): pass

    label("Function_15_3070")

    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x102, 0x1000)
    SetChrBattleFlags(0x102, 0x20)
    OP_8C(0x102, 316, 0)

    label("loc_3090")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30D1")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA50), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15FE), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7C6), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("loc_3090")

    label("loc_30D1")

    Return()

    # Function_15_3070 end

    def Function_16_30D2(): pass

    label("Function_16_30D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3113")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x988), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBCC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_16_30D2")

    label("loc_3113")

    Return()

    # Function_16_30D2 end

    def Function_17_3114(): pass

    label("Function_17_3114")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B5")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_17_3114")

    label("loc_31B5")

    Return()

    # Function_17_3114 end

    def Function_18_31B6(): pass

    label("Function_18_31B6")

    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    SetChrSubChip(0x102, 12)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x102, 13)
    PlayEffect(0x1, 0x1, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(80)
    SetChrSubChip(0x102, 14)
    OP_7D(0x0, 0x102, 0x32, 0xC8)
    Return()

    # Function_18_31B6 end

    def Function_19_3275(): pass

    label("Function_19_3275")

    Sleep(500)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0xFFFFEC78, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFD8F0, 0x82C8, 0x4650, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0xFFFFEC78, 0x30C0, 0x3E80, 0x0)
    OP_8F(0xFE, 0xFFFCF220, 0x7D0, 0x5C8, 0x36B0, 0x0)
    Return()

    # Function_19_3275 end

    def Function_20_32DF(): pass

    label("Function_20_32DF")

    Sleep(500)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0xFFFFEC78, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFD8F0, 0x82C8, 0x4650, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0xFFFFEC78, 0x30C0, 0x3E80, 0x0)
    OP_8F(0xFE, 0xFFFCF220, 0x7D0, 0x5C8, 0x36B0, 0x0)
    Return()

    # Function_20_32DF end

    def Function_21_3349(): pass

    label("Function_21_3349")


    def lambda_334F():
        OP_D1(254, 0, 270000, 60000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_334F)

    def lambda_3369():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3369)
    Sleep(400)

    def lambda_338A():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_338A)
    Sleep(300)

    def lambda_33AB():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33AB)
    Sleep(200)

    def lambda_33CC():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33CC)
    Sleep(100)

    def lambda_33ED():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33ED)
    Sleep(4600)

    def lambda_340E():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_340E)
    Sleep(300)

    def lambda_342F():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_342F)
    Sleep(200)

    def lambda_3450():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3450)
    Sleep(100)

    def lambda_3471():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3471)
    Return()

    # Function_21_3349 end

    def Function_22_3488(): pass

    label("Function_22_3488")


    def lambda_348E():
        OP_D1(254, 0, 270000, 60000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_348E)

    def lambda_34A8():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34A8)
    Sleep(400)

    def lambda_34C9():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34C9)
    Sleep(300)

    def lambda_34EA():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34EA)
    Sleep(200)

    def lambda_350B():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_350B)
    Sleep(100)

    def lambda_352C():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_352C)
    Sleep(4600)

    def lambda_354D():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_354D)
    Sleep(300)

    def lambda_356E():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_356E)
    Sleep(200)

    def lambda_358F():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_358F)
    Sleep(100)

    def lambda_35B0():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35B0)
    Return()

    # Function_22_3488 end

    def Function_23_35C7(): pass

    label("Function_23_35C7")

    OP_8F(0xFE, 0x5EEC, 0x0, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0x0, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFEC78, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0x0, 0x4060, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD05A8, 0xFFFFD120, 0xD98, 0x4E20, 0x0)
    Return()

    # Function_23_35C7 end

    def Function_24_3640(): pass

    label("Function_24_3640")

    OP_8F(0xFE, 0x5EEC, 0x0, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0x0, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFEC78, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0x0, 0x4060, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD05A8, 0xFFFFD120, 0xD98, 0x4E20, 0x0)
    Return()

    # Function_24_3640 end

    def Function_25_36B9(): pass

    label("Function_25_36B9")

    OP_8F(0xFE, 0x0, 0x0, 0x4E20, 0x36B0, 0x0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFE2B40, 0x0, 0x0)

    def lambda_36F3():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F3)

    def lambda_3703():
        OP_D1(254, 0, 270000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3703)
    WaitChrThread(0xFE, 0x3)

    def lambda_3722():
        OP_D1(254, 0, 270000, -25000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3722)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x4E20, 0x36B0, 0x0)
    Return()

    # Function_25_36B9 end

    def Function_26_3750(): pass

    label("Function_26_3750")

    OP_8F(0xFE, 0x0, 0x0, 0x4E20, 0x36B0, 0x0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFE2B40, 0x0, 0x0)

    def lambda_378A():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_378A)

    def lambda_379A():
        OP_D1(254, 0, 270000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_379A)
    WaitChrThread(0xF, 0x3)

    def lambda_37B9():
        OP_D1(254, 0, 270000, -25000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_37B9)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x4E20, 0x36B0, 0x0)
    Return()

    # Function_26_3750 end

    def Function_27_37E7(): pass

    label("Function_27_37E7")

    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x88B8, 0xBB8, 0xFFFFB1E0)
    OP_98(0x1, 0x7530, 0x3E8, 0x5DC0)

    def lambda_380D():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_380D)
    Sleep(2000)

    def lambda_3822():
        OP_D1(254, 6000, 240000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3822)

    def lambda_383C():
        OP_6D(29550, -10000, -1500, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_383C)

    def lambda_3854():
        OP_D0(370000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3854)
    WaitChrThread(0xFE, 0x3)
    OP_44(0xFE, 0x1)

    def lambda_386D():
        OP_D1(254, 6000, 240000, 45000, 2500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_386D)

    def lambda_3887():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3887)
    Sleep(100)

    def lambda_38A7():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38A7)
    Sleep(100)

    def lambda_38C7():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38C7)
    Sleep(100)

    def lambda_38E7():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38E7)
    Sleep(100)

    def lambda_3907():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3907)
    Return()

    # Function_27_37E7 end

    def Function_28_391D(): pass

    label("Function_28_391D")

    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x88B8, 0xBB8, 0xFFFFB1E0)
    OP_98(0x1, 0x7530, 0x3E8, 0x5DC0)

    def lambda_3943():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3943)
    Sleep(2000)

    def lambda_3958():
        OP_D1(254, 6000, 240000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3958)
    WaitChrThread(0xFE, 0x3)
    OP_44(0xFE, 0x1)

    def lambda_397B():
        OP_D1(254, 6000, 240000, 45000, 2500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_397B)

    def lambda_3995():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3995)
    Sleep(100)

    def lambda_39B5():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39B5)
    Sleep(100)

    def lambda_39D5():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39D5)
    Sleep(100)

    def lambda_39F5():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39F5)
    Sleep(100)

    def lambda_3A15():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A15)
    Return()

    # Function_28_391D end

    def Function_29_3A2B(): pass

    label("Function_29_3A2B")


    def lambda_3A31():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A31)
    Sleep(400)

    def lambda_3A52():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A52)
    Sleep(300)

    def lambda_3A73():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A73)
    Sleep(200)

    def lambda_3A94():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A94)
    Sleep(100)

    def lambda_3AB5():
        OP_D1(254, 0, 270000, 60000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3AB5)

    def lambda_3ACF():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ACF)
    Sleep(7500)

    def lambda_3AF0():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AF0)
    Sleep(200)

    def lambda_3B11():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B11)
    Sleep(200)

    def lambda_3B32():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B32)
    Sleep(2000)

    def lambda_3B53():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B53)

    def lambda_3B6D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x35E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B6D)
    Sleep(100)

    def lambda_3B8D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x39D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B8D)
    Sleep(100)

    def lambda_3BAD():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x41A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BAD)
    Sleep(100)

    def lambda_3BCD():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x4970, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BCD)
    Sleep(100)

    def lambda_3BED():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x5528, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BED)
    Sleep(100)

    def lambda_3C0D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C0D)
    Sleep(4600)

    def lambda_3C2D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3C2D)

    def lambda_3C48():
        OP_8F(0xFE, 0xFFFD19D0, 0xFFFFF830, 0x186A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3C48)
    Return()

    # Function_29_3A2B end

    def Function_30_3C5E(): pass

    label("Function_30_3C5E")


    def lambda_3C64():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C64)
    Sleep(400)

    def lambda_3C85():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C85)
    Sleep(300)

    def lambda_3CA6():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA6)
    Sleep(200)

    def lambda_3CC7():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CC7)
    Sleep(100)

    def lambda_3CE8():
        OP_D1(254, 0, 270000, 60000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3CE8)

    def lambda_3D02():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D02)
    Sleep(7500)

    def lambda_3D23():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D23)
    Sleep(200)

    def lambda_3D44():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D44)
    Sleep(200)

    def lambda_3D65():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D65)
    Sleep(2000)

    def lambda_3D86():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3D86)

    def lambda_3DA0():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x35E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA0)
    Sleep(100)

    def lambda_3DC0():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x39D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DC0)
    Sleep(100)

    def lambda_3DE0():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x41A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DE0)
    Sleep(100)

    def lambda_3E00():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x4970, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E00)
    Sleep(100)

    def lambda_3E20():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x5528, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E20)
    Sleep(100)

    def lambda_3E40():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E40)
    Sleep(4600)

    def lambda_3E60():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E60)

    def lambda_3E7B():
        OP_8F(0xFE, 0xFFFD19D0, 0xFFFFF830, 0x186A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3E7B)
    Return()

    # Function_30_3C5E end

    def Function_31_3E91(): pass

    label("Function_31_3E91")

    EventBegin(0x0)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 0, 3000, 0, 270)
    SetChrPos(0xE, 0, 3000, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 110000, 4000, -20000, 270)
    SetChrPos(0x10, 110000, 4000, -20000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_71(0x1, 0x4)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 360)
    OP_70(0x4, 0x1CC)
    OP_6D(42110, -10000, -9480, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(7610, 0)
    OP_6C(105000, 0)
    OP_6E(1076, 0)
    OP_D0(370000, 0)
    FadeToBright(1000, 0)

    def lambda_4031():
        OP_8F(0xFE, 0x186A0, 0xFA0, 0xFFFFB1E0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_4031)

    def lambda_404C():
        OP_8F(0xFE, 0x186A0, 0xFA0, 0xFFFFB1E0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_404C)
    WaitChrThread(0xF, 0x0)

    def lambda_406C():
        OP_6D(21040, -10000, 44720, 4000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_406C)

    def lambda_4084():
        OP_67(0, 3620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4084)

    def lambda_409C():
        OP_6C(24000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_409C)

    def lambda_40AC():
        OP_D0(360000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_40AC)
    OP_43(0xF, 0x0, 0x0, 0x20)
    OP_43(0x10, 0x0, 0x0, 0x21)
    OP_43(0xF, 0x1, 0x0, 0x22)
    OP_43(0x10, 0x1, 0x0, 0x23)
    StopSound(0x186A0, 0x493E0, 0x2710)
    Sleep(1000)

    def lambda_40EA():
        OP_D1(254, 0, 260000, 30000, 2400)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_40EA)

    def lambda_4104():
        OP_D1(254, 0, 260000, 30000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4104)
    WaitChrThread(0xD, 0x3)

    def lambda_4123():
        OP_D1(254, 0, 270000, 15000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4123)

    def lambda_413D():
        OP_D1(254, 0, 270000, 15000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_413D)

    def lambda_4157():
        OP_6B(9610, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4157)
    Sleep(5000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_3E91 end

    def Function_32_417E(): pass

    label("Function_32_417E")


    def lambda_4184():
        OP_D1(254, 0, 290000, -40000, 3500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4184)
    OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)

    def lambda_41B3():
        OP_D1(254, 0, 310000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_41B3)
    OP_8F(0xFE, 0xFFFFB1E0, 0x4E20, 0x493E0, 0x5DC0, 0x0)
    Return()

    # Function_32_417E end

    def Function_33_41DC(): pass

    label("Function_33_41DC")


    def lambda_41E2():
        OP_D1(254, 0, 290000, -40000, 3500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_41E2)
    OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)

    def lambda_4211():
        OP_D1(254, 0, 310000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4211)
    OP_8F(0xFE, 0xFFFFB1E0, 0x4E20, 0x493E0, 0x5DC0, 0x0)
    Return()

    # Function_33_41DC end

    def Function_34_423A(): pass

    label("Function_34_423A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_425B")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_34_423A")

    label("loc_425B")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_423A end

    def Function_35_4267(): pass

    label("Function_35_4267")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4288")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_35_4267")

    label("loc_4288")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_4267 end

    def Function_36_4294(): pass

    label("Function_36_4294")

    EventBegin(0x0)
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 6180, 15930, 17690, 0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_A1(0xD, 0x2)
    SetChrPos(0xD, 4780, 14000, 10550, 45)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_6D(6550, 15930, 18080, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(124000, 0)
    OP_6E(438, 0)
    FadeToBright(1000, 0)

    def lambda_433A():
        OP_6D(7530, 15930, 13960, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_433A)

    def lambda_4352():
        OP_67(0, 6750, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4352)
    OP_6E(778, 4000)

    def lambda_4373():
        OP_6D(-53670, 15930, -95210, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4373)

    def lambda_438B():
        OP_67(0, 5450, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_438B)

    def lambda_43A3():
        OP_6B(4780, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_43A3)

    def lambda_43B3():
        OP_6C(67000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_43B3)

    def lambda_43C3():
        OP_6E(834, 10000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_43C3)
    Sleep(9000)
    FadeToDark(1000, 0, -1)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_36_4294 end

    def Function_37_43E9(): pass

    label("Function_37_43E9")

    EventBegin(0x0)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x28)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x28)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 6)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x1000)
    SetChrBattleFlags(0x102, 0x20)
    SetChrPos(0x102, 810, 3380, -2950, 180)
    OP_6D(-6990, 3340, -40, 0)
    OP_67(0, 1430, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(100000, 0)
    OP_6E(438, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_453B():
        OP_6D(-7310, 3340, 410, 8000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_453B)

    def lambda_4553():
        OP_6C(300000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4553)

    def lambda_4563():
        OP_6B(2260, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4563)
    Sleep(5000)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 1)
    WaitChrThread(0x102, 0x0)
    Sleep(1000)
    OP_43(0xD, 0x0, 0x0, 0x26)

    def lambda_4593():
        OP_6C(280000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4593)
    Sleep(3000)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 2)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_43E9 end

    def Function_38_45CE(): pass

    label("Function_38_45CE")


    def lambda_45D4():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_45D4)

    def lambda_45EF():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_45EF)
    Sleep(400)

    def lambda_460F():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_460F)

    def lambda_462A():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_462A)
    Sleep(400)

    def lambda_464A():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_464A)

    def lambda_4665():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4665)
    Sleep(300)

    def lambda_4685():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4685)

    def lambda_46A0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_46A0)
    Sleep(300)

    def lambda_46C0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46C0)

    def lambda_46DB():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_46DB)
    Sleep(200)

    def lambda_46FB():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46FB)

    def lambda_4716():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4716)
    Sleep(200)

    def lambda_4736():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4736)

    def lambda_4751():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4751)
    Sleep(100)

    def lambda_4771():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4771)

    def lambda_478C():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_478C)
    Sleep(100)

    def lambda_47AC():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_47AC)

    def lambda_47C7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_47C7)
    Return()

    # Function_38_45CE end

    def Function_39_47DD(): pass

    label("Function_39_47DD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F7")
    Call(0, 54)
    Call(0, 55)
    RemoveParty(0x0, 0xFF)

    label("loc_47F7")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(220, -15000, 60940, 0)
    OP_67(0, -3800, -10000, 0)
    OP_6B(1220, 0)
    OP_6C(0, 0)
    OP_6E(667, 0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_A1(0xD, 0x2)
    SetChrPos(0xD, -38450, -5000, 63740, 45)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 680)
    OP_70(0x2, 0x30C)
    OP_72(0x5, 0x4)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -38450, -5000, 63740, 45)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 680)
    OP_70(0x5, 0x30C)
    OP_22(0x79, 0x1, 0x4B)
    FadeToBright(2000, 0)

    def lambda_48B8():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48B8)
    OP_43(0xD, 0x0, 0x0, 0x28)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_490D")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #51 op#A op#5
        "\x07\x00#068F#4S#18A姐姐──！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A68")

    label("loc_490D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4953")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #52 op#A op#5
        "\x07\x00#046F#4S#12A艾丝蒂尔……！！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A68")

    label("loc_4953")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_499B")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #53 op#A op#5
        "\x07\x00#024F#4S#18A艾丝蒂尔──！！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A68")

    label("loc_499B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E1")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #54 op#A op#5
        "\x07\x00#054F#4S#13A艾丝蒂尔──！！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A68")

    label("loc_49E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A29")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #55 op#A op#5
        "\x07\x00#530F#4S#10A艾丝蒂尔……！！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4A68")

    label("loc_4A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A68")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #56 op#A op#5
        "\x07\x00#076F#4S#10A艾丝蒂尔……！！\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4A68")

    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    FadeToDark(3000, 0, -1)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x41)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x37)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x2D)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x23)
    Sleep(300)
    OP_23(0x79)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_39_47DD end

    def Function_40_4AEE(): pass

    label("Function_40_4AEE")


    def lambda_4AF4():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4AF4)

    def lambda_4B0F():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B0F)
    Sleep(500)

    def lambda_4B2F():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4B2F)

    def lambda_4B4A():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B4A)
    Sleep(500)

    def lambda_4B6A():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4B6A)

    def lambda_4B85():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B85)
    Sleep(500)

    def lambda_4BA5():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4BA5)

    def lambda_4BC0():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4BC0)
    Return()

    # Function_40_4AEE end

    def Function_41_4BD6(): pass

    label("Function_41_4BD6")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_6D(5080, 2500, 55830, 0)
    OP_67(0, 4010, -10000, 0)
    OP_6B(8300, 0)
    OP_6C(47000, 0)
    OP_6E(337, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x1)
    SetChrPos(0xD, 20000, 0, 55000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_B0(0x1, 0x1E)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 330)
    OP_70(0x1, 0x1AE)
    FadeToBright(2000, 0)

    def lambda_4C79():
        OP_6D(24700, 2500, 55500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4C79)

    def lambda_4C91():
        OP_67(0, 8240, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4C91)

    def lambda_4CA9():
        OP_6C(317000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4CA9)

    def lambda_4CB9():
        OP_6E(447, 8000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CB9)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_41_4BD6 end

    def Function_42_4CE8(): pass

    label("Function_42_4CE8")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(16329, 4250, 57660, 0)
    OP_67(0, 8380, -10000, 0)
    OP_6B(5340, 0)
    OP_6C(57000, 0)
    OP_6E(476, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x1)
    SetChrPos(0xD, 20000, 0, 55000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_B0(0x1, 0x14)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 330)
    OP_70(0x1, 0x1AE)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(22780, 500, 70340, 0)
    OP_67(0, 9440, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(57000, 0)
    OP_6E(375, 0)
    OP_43(0x8, 0x1, 0x0, 0x2C)
    OP_43(0x9, 0x1, 0x0, 0x2D)
    OP_43(0x14, 0x1, 0x0, 0x2E)
    OP_43(0x13, 0x1, 0x0, 0x2F)
    OP_43(0x11, 0x1, 0x0, 0x30)
    OP_43(0x15, 0x1, 0x0, 0x31)
    OP_43(0x16, 0x1, 0x0, 0x32)
    OP_43(0x12, 0x1, 0x0, 0x33)
    OP_43(0x18, 0x1, 0x0, 0x34)
    OP_43(0x17, 0x1, 0x0, 0x35)
    OP_48()
    OP_0D()
    WaitChrThread(0x9, 0x2)
    Sleep(300)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #57
        0x8,
        "#1002F#5P哪、哪里……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #58
        0x9,
        (
            "#1043F#6P从前方甲板\x01",
            "看得最清楚的方向……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x16, 0x1)
    Sleep(500)
    OP_20(0x7D0)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x16, 270, 600)
    Sleep(400)

    ChrTalk(    #59
        0x16,
        "#1069F#2P……就是那个！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x82)
    Sleep(500)

    def lambda_4ED2():
        OP_6D(-23010, 2450, 64140, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4ED2)

    def lambda_4EEA():
        OP_6C(81000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4EEA)

    def lambda_4EFA():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4EFA)

    def lambda_4F08():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F08)
    Sleep(50)

    def lambda_4F1B():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F1B)

    def lambda_4F29():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4F29)
    Sleep(50)

    def lambda_4F3C():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F3C)

    def lambda_4F4A():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F4A)
    Sleep(50)

    def lambda_4F5D():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F5D)

    def lambda_4F6B():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4F6B)
    Sleep(50)

    def lambda_4F7E():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4F7E)
    Sleep(3500)
    OP_43(0x16, 0x3, 0x0, 0x2B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    OP_0D()
    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x1)

    label("loc_4FC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FE2")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_4FDF")
    Jump("loc_4FE2")

    label("loc_4FDF")

    Jump("loc_4FC8")

    label("loc_4FE2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_6D(19920, 2450, 67640, 0)
    OP_67(0, 6610, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\mp092_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, -40000, 8000, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0x44C, 0xFC72, 0xFF88, 0x6E, 0x1)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x125, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #60
        0x8,
        "#1020F#5P什、什、什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#043F#5P难不成那就是……\x01",
            "……那巨大的城市是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        "#1042F#5P嗯……没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x16,
        (
            "#1069F#5P『辉之环』……\x01",
            "果然是辉之环啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x17,
        "#102F#5P──不好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 600)
    Sleep(300)

    ChrTalk(    #65
        0x17,
        (
            "#105F#2P尤莉亚上尉！\x01",
            "赶快让军舰降落！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)

    ChrTalk(    #66
        0x18,
        "#173F#6P……啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x17,
        (
            "#105F#2P不是有卡西乌斯发布的\x01",
            "紧急指令吗！\x02\x03",

            "再不动就来不及了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x18,
        "#177F#6P#3S！！！\x02",
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x2B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    OP_0D()
    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x1)

    label("loc_526C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5286")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5283")
    Jump("loc_5286")

    label("loc_5283")

    Jump("loc_526C")

    label("loc_5286")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/C5413   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_4CE8 end

    def Function_43_52B0(): pass

    label("Function_43_52B0")

    OP_24(0x1C3, 0x5A)
    OP_24(0x125, 0x41)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x125, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x125, 0x37)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x125, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x125, 0x2D)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x125, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    OP_24(0x125, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x125)
    Return()

    # Function_43_52B0 end

    def Function_44_531F(): pass

    label("Function_44_531F")

    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0x5082, 0x992, 0x11288, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_44_531F end

    def Function_45_53AA(): pass

    label("Function_45_53AA")

    Sleep(500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 24)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4BDC, 0x992, 0x10DC4, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_45_53AA end

    def Function_46_53EE(): pass

    label("Function_46_53EE")

    Sleep(1000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x5320, 0x992, 0x10E32, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_46_53EE end

    def Function_47_5439(): pass

    label("Function_47_5439")

    Sleep(1500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 19)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x5546, 0x992, 0x10914, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_47_5439 end

    def Function_48_5484(): pass

    label("Function_48_5484")

    Sleep(2000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 17)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4EE8, 0x992, 0x10892, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_48_5484 end

    def Function_49_54CF(): pass

    label("Function_49_54CF")

    Sleep(2500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x54E2, 0x992, 0x1027A, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_49_54CF end

    def Function_50_551A(): pass

    label("Function_50_551A")

    Sleep(3000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 22)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4894, 0x992, 0x10716, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_50_551A end

    def Function_51_5565(): pass

    label("Function_51_5565")

    Sleep(3500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 18)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4862, 0x992, 0x10216, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_51_5565 end

    def Function_52_55A9(): pass

    label("Function_52_55A9")

    Sleep(4000)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4E8E, 0x992, 0x1034C, 0xFA0, 0x0)
    Return()

    # Function_52_55A9 end

    def Function_53_55DE(): pass

    label("Function_53_55DE")

    Sleep(4500)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4F10, 0x992, 0xFEA6, 0xFA0, 0x0)
    Return()

    # Function_53_55DE end

    def Function_54_5613(): pass

    label("Function_54_5613")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5690"),
        (1, "loc_5696"),
        (SWITCH_DEFAULT, "loc_569C"),
    )


    label("loc_5690")

    OP_A2(0x1200)
    Jump("loc_569C")

    label("loc_5696")

    OP_A2(0x1201)
    Jump("loc_569C")

    label("loc_569C")

    Return()

    # Function_54_5613 end

    def Function_55_569D(): pass

    label("Function_55_569D")

    ClearMapFlags(0x1)
    OP_6D(-551720, -10000, -227160, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_55_569D end

    SaveToFile()

Try(main)

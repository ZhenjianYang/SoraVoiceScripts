from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5408   ._SN',
        MapName             = 'Other',
        Location            = 'C5408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '结社艇',                               # 9
        '结社艇',                               # 10
        '结社艇',                               # 11
        '结社艇',                               # 12
        '结社艇',                               # 13
        '强化猎兵',                             # 14
        '强化猎兵',                             # 15
        '强化猎兵',                             # 16
        '强化猎兵',                             # 17
        '基尔巴特',                             # 18
        '约修亚',                               # 19
        '约修亚残像',                           # 20
        '剑帝莱维',                             # 21
        '布卢布兰',                             # 22
        '幻惑之铃露茜奥拉',                     # 23
        '瘦狼瓦鲁特',                           # 24
        '歼灭天使玲',                           # 25
        '小丑肯帕雷拉',                         # 26
        '怀斯曼教授',                           # 27
        '目标用照相机',                         # 28
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
        'ED6_DT27/CH04610 ._CH',             # 00
        'ED6_DT27/CH03750 ._CH',             # 01
        'ED6_DT27/CH04750 ._CH',             # 02
        'ED6_DT27/CH03610 ._CH',             # 03
        'ED6_DT27/CH04000 ._CH',             # 04
        'ED6_DT27/CH04002 ._CH',             # 05
        'ED6_DT27/CH04004 ._CH',             # 06
        'ED6_DT27/CH04610 ._CH',             # 07
        'ED6_DT27/CH04611 ._CH',             # 08
        'ED6_DT27/CH04614 ._CH',             # 09
        'ED6_DT26/CH20501 ._CH',             # 0A
        'ED6_DT27/CH04754 ._CH',             # 0B
        'ED6_DT27/CH04612 ._CH',             # 0C
        'ED6_DT27/CH03650 ._CH',             # 0D
        'ED6_DT26/CH20385 ._CH',             # 0E
        'ED6_DT26/CH20397 ._CH',             # 0F
        'ED6_DT07/CH02040 ._CH',             # 10
        'ED6_DT27/CH04540 ._CH',             # 11
        'ED6_DT26/CH20364 ._CH',             # 12
        'ED6_DT27/CH03530 ._CH',             # 13
        'ED6_DT27/CH03520 ._CH',             # 14
        'ED6_DT27/CH03500 ._CH',             # 15
        'ED6_DT27/CH03510 ._CH',             # 16
        'ED6_DT27/CH03600 ._CH',             # 17
        'ED6_DT27/CH03550 ._CH',             # 18
        'ED6_DT29/CH12390 ._CH',             # 19
        'ED6_DT27/CH04751 ._CH',             # 1A
        'ED6_DT27/CH04613 ._CH',             # 1B
        'ED6_DT27/CH04753 ._CH',             # 1C
        'ED6_DT27/CH04001 ._CH',             # 1D
        'ED6_DT26/CH20386 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT27/CH04610P._CP',             # 00
        'ED6_DT27/CH03750P._CP',             # 01
        'ED6_DT27/CH04750P._CP',             # 02
        'ED6_DT27/CH03610P._CP',             # 03
        'ED6_DT27/CH04000P._CP',             # 04
        'ED6_DT27/CH04002P._CP',             # 05
        'ED6_DT27/CH04004P._CP',             # 06
        'ED6_DT27/CH04610P._CP',             # 07
        'ED6_DT27/CH04611P._CP',             # 08
        'ED6_DT27/CH04614P._CP',             # 09
        'ED6_DT26/CH20501P._CP',             # 0A
        'ED6_DT27/CH04754P._CP',             # 0B
        'ED6_DT27/CH04612P._CP',             # 0C
        'ED6_DT27/CH03650P._CP',             # 0D
        'ED6_DT26/CH20385P._CP',             # 0E
        'ED6_DT26/CH20397P._CP',             # 0F
        'ED6_DT07/CH02040P._CP',             # 10
        'ED6_DT27/CH04540P._CP',             # 11
        'ED6_DT26/CH20364P._CP',             # 12
        'ED6_DT27/CH03530P._CP',             # 13
        'ED6_DT27/CH03520P._CP',             # 14
        'ED6_DT27/CH03500P._CP',             # 15
        'ED6_DT27/CH03510P._CP',             # 16
        'ED6_DT27/CH03600P._CP',             # 17
        'ED6_DT27/CH03550P._CP',             # 18
        'ED6_DT29/CH12390P._CP',             # 19
        'ED6_DT27/CH04751P._CP',             # 1A
        'ED6_DT27/CH04613P._CP',             # 1B
        'ED6_DT27/CH04753P._CP',             # 1C
        'ED6_DT27/CH04001P._CP',             # 1D
        'ED6_DT26/CH20386P._CP',             # 1E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
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
        NpcIndex            = 0xC5,
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
        NpcIndex            = 0xC5,
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
        NpcIndex            = 0xC5,
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
        NpcIndex            = 0xC5,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -8100,
        Y                   = 0,
        Z                   = -65500,
        Range               = 9750,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFEF854,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_442",          # 00, 0
        "Function_1_4BA",          # 01, 1
        "Function_2_52B",          # 02, 2
        "Function_3_5EF",          # 03, 3
        "Function_4_75F",          # 04, 4
        "Function_5_8D0",          # 05, 5
        "Function_6_98E",          # 06, 6
        "Function_7_AA1",          # 07, 7
        "Function_8_B5F",          # 08, 8
        "Function_9_C72",          # 09, 9
        "Function_10_D30",         # 0A, 10
        "Function_11_E43",         # 0B, 11
        "Function_12_F01",         # 0C, 12
        "Function_13_1014",        # 0D, 13
        "Function_14_10D2",        # 0E, 14
        "Function_15_11E5",        # 0F, 15
        "Function_16_14BC",        # 10, 16
        "Function_17_22FC",        # 11, 17
        "Function_18_2325",        # 12, 18
        "Function_19_234E",        # 13, 19
        "Function_20_2372",        # 14, 20
        "Function_21_2396",        # 15, 21
        "Function_22_23B0",        # 16, 22
        "Function_23_23CA",        # 17, 23
        "Function_24_47C4",        # 18, 24
        "Function_25_4869",        # 19, 25
        "Function_26_4941",        # 1A, 26
        "Function_27_496A",        # 1B, 27
        "Function_28_4993",        # 1C, 28
        "Function_29_49BC",        # 1D, 29
        "Function_30_49E5",        # 1E, 30
        "Function_31_4A16",        # 1F, 31
        "Function_32_4A6F",        # 20, 32
        "Function_33_4AC8",        # 21, 33
        "Function_34_4B21",        # 22, 34
        "Function_35_4B7A",        # 23, 35
        "Function_36_4BB9",        # 24, 36
        "Function_37_4BE6",        # 25, 37
        "Function_38_4C61",        # 26, 38
        "Function_39_4CDC",        # 27, 39
        "Function_40_4D57",        # 28, 40
        "Function_41_4D9D",        # 29, 41
        "Function_42_4DFC",        # 2A, 42
        "Function_43_4E6B",        # 2B, 43
        "Function_44_4ECE",        # 2C, 44
        "Function_45_4FDA",        # 2D, 45
        "Function_46_5148",        # 2E, 46
        "Function_47_5259",        # 2F, 47
        "Function_48_540E",        # 30, 48
        "Function_49_549C",        # 31, 49
        "Function_50_5510",        # 32, 50
        "Function_51_559E",        # 33, 51
        "Function_52_5626",        # 34, 52
        "Function_53_56B4",        # 35, 53
        "Function_54_573C",        # 36, 54
    )


    def Function_0_442(): pass

    label("Function_0_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_453")
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_4B9")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_46D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 4)
    Jump("loc_4B9")

    label("loc_46D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_487")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    Event(0, 45)
    Jump("loc_4B9")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_4A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    Event(0, 47)
    Jump("loc_4B9")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    Event(0, 15)

    label("loc_4B9")

    Return()

    # Function_0_442 end

    def Function_1_4BA(): pass

    label("Function_1_4BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D8")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D8")

    OP_22(0x131, 0x1, 0x46)
    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500")
    OP_72(0x6, 0x4)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x8)
    OP_6F(0x6, 0)

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    OP_72(0x7, 0x4)
    OP_72(0x7, 0x20)
    OP_72(0x7, 0x8)
    OP_6F(0x7, 0)
    Jump("loc_525")

    label("loc_521")

    Call(0, 25)

    label("loc_525")

    OP_71(0x8, 0x4)
    Return()

    # Function_1_4BA end

    def Function_2_52B(): pass

    label("Function_2_52B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    OP_6D(-31440, 0, -23410, 0)
    OP_67(0, 8400, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(62000, 0)
    OP_6E(445, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_57F():
        OP_6D(-12320, 0, -61450, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_57F)

    def lambda_597():
        OP_67(0, 28780, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_597)

    def lambda_5AF():
        OP_6B(5130, 12000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5AF)

    def lambda_5BF():
        OP_6C(61000, 12000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5BF)
    OP_6E(600, 12000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_2_52B end

    def Function_3_5EF(): pass

    label("Function_3_5EF")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    OP_6D(-10950, -35000, -43730, 0)
    OP_67(0, 13010, -10000, 0)
    OP_6B(5540, 0)
    OP_6C(99000, 0)
    OP_6E(1092, 0)
    OP_A1(0x8, 0x0)
    OP_A1(0x9, 0x1)
    OP_A1(0xA, 0x2)
    OP_A1(0xB, 0x3)
    OP_A1(0xC, 0x4)
    SetChrPos(0x8, -10730, -30000, -40850, 0)
    SetChrPos(0x9, -10730, -30000, -80850, 0)
    SetChrPos(0xA, -10730, -30000, -45850, 0)
    SetChrPos(0xB, -7730, -30000, -75850, 0)
    SetChrPos(0xC, -7730, -30000, -50850, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_6B1():
        OP_6D(-12280, -35000, -43960, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6B1)

    def lambda_6C9():
        OP_67(0, 6270, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6C9)

    def lambda_6E1():
        OP_6B(6200, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6E1)

    def lambda_6F1():
        OP_6C(79000, 14000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6F1)

    def lambda_701():
        OP_6E(1092, 10000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_701)
    OP_43(0x8, 0x1, 0x0, 0x5)
    Sleep(1500)
    OP_43(0x9, 0x1, 0x0, 0x7)
    Sleep(2500)
    OP_43(0xA, 0x1, 0x0, 0x9)
    Sleep(1500)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(2500)
    OP_43(0xC, 0x1, 0x0, 0xD)
    WaitChrThread(0xC, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5EF end

    def Function_4_75F(): pass

    label("Function_4_75F")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x0, 0x4)
    SetChrPos(0x0, 0, -70000, -50000, 0)
    OP_6D(5150, -16850, -28970, 0)
    OP_67(0, 20020, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(49000, 0)
    OP_6E(964, 0)
    OP_A1(0x8, 0x0)
    OP_A1(0x9, 0x1)
    OP_A1(0xA, 0x2)
    OP_A1(0xB, 0x3)
    OP_A1(0xC, 0x4)
    SetChrPos(0x8, 0, -30000, -50000, 0)
    SetChrPos(0x9, 0, -30000, -50000, 0)
    SetChrPos(0xA, 0, -30000, -50000, 0)
    SetChrPos(0xB, 0, -30000, -50000, 0)
    SetChrPos(0xC, 0, -30000, -50000, 0)
    FadeToBright(1000, 0)

    def lambda_836():
        OP_6D(-37950, -32049, -28670, 10000)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_836)

    def lambda_84E():
        OP_67(0, 7860, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_84E)

    def lambda_866():
        OP_6B(4000, 10000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_866)

    def lambda_876():
        OP_6C(49000, 10000)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_876)

    def lambda_886():
        OP_6E(964, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_886)
    OP_43(0x8, 0x0, 0x0, 0x6)
    OP_43(0x9, 0x0, 0x0, 0x8)
    OP_43(0xA, 0x0, 0x0, 0xA)
    OP_43(0xB, 0x0, 0x0, 0xC)
    OP_43(0xC, 0x0, 0x0, 0xE)
    Sleep(10000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_4_75F end

    def Function_5_8D0(): pass

    label("Function_5_8D0")

    OP_71(0x0, 0x2)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x4)
    OP_6F(0x0, 800)
    OP_8F(0x8, 0xFFFFD616, 0xFFFF6E7E, 0xFFFF606E, 0x2710, 0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    Sleep(500)

    def lambda_918():
        OP_D1(254, 0, 0, 7000, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_918)
    OP_8F(0x8, 0xFFFF880A, 0xFFFF7748, 0xFFFF4CE6, 0x1F40, 0x0)

    def lambda_946():
        OP_D1(254, 0, 0, 0, 800)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_946)
    Sleep(200)
    OP_98(0x0, 0x8)
    OP_98(0x1, 0xFFFF6B0E, 0xFFFF955C, 0xFFFFD788)
    OP_98(0x1, 0xFFFF434A, 0xFFFFC4D2, 0x50DC)
    OP_98(0x2, 0x8, 0x61A8, 0x6)
    OP_71(0x0, 0x4)
    Return()

    # Function_5_8D0 end

    def Function_6_98E(): pass

    label("Function_6_98E")

    Sleep(8000)
    OP_71(0x0, 0x2)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x4)
    OP_6F(0x0, 800)
    OP_D1(254, 10000, 360000, 0, 0)

    def lambda_9C2():
        OP_D1(254, 0, 360000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_9C2)

    def lambda_9DC():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DC)
    Sleep(1100)

    def lambda_9FC():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FC)
    Sleep(100)

    def lambda_A1C():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1C)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0x0, 0xFFFEEE90, 0xFFFF3CB0, 0xFA0, 0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)

    def lambda_A63():
        OP_D1(254, 0, 350000, 10000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A63)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFFC180, 0xFFFEEE90, 0x186A0)
    OP_98(0x1, 0xFFFF63C0, 0xFFFEEE90, 0x30D40)
    OP_98(0x2, 0xFE, 0x9C40, 0x0)
    Return()

    # Function_6_98E end

    def Function_7_AA1(): pass

    label("Function_7_AA1")

    OP_71(0x1, 0x2)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x4)
    OP_6F(0x1, 800)
    OP_8F(0x9, 0xFFFFD616, 0xFFFF6E7E, 0xFFFEC42E, 0x2710, 0x0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x384)
    Sleep(500)

    def lambda_AE9():
        OP_D1(254, 0, 0, 7000, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AE9)
    OP_8F(0x9, 0xFFFF880A, 0xFFFF7748, 0xFFFEB0A6, 0x1F40, 0x0)

    def lambda_B17():
        OP_D1(254, 0, 0, 0, 800)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B17)
    Sleep(200)
    OP_98(0x0, 0x9)
    OP_98(0x1, 0xFFFF633E, 0xFFFF955C, 0xFFFFD788)
    OP_98(0x1, 0xFFFF3B7A, 0xFFFFC4D2, 0x50DC)
    OP_98(0x2, 0x9, 0x61A8, 0x6)
    OP_71(0x1, 0x4)
    Return()

    # Function_7_AA1 end

    def Function_8_B5F(): pass

    label("Function_8_B5F")

    Sleep(10000)
    OP_71(0x1, 0x2)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x4)
    OP_6F(0x1, 800)
    OP_D1(254, -10000, 360000, 0, 0)

    def lambda_B93():
        OP_D1(254, 0, 360000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_B93)

    def lambda_BAD():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAD)
    Sleep(1100)

    def lambda_BCD():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCD)
    Sleep(100)

    def lambda_BED():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BED)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0x0, 0xFFFEEE90, 0xFFFF3CB0, 0xFA0, 0x0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x384)

    def lambda_C34():
        OP_D1(254, 0, 340000, 20000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C34)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFFA240, 0xFFFEEE90, 0x15F90)
    OP_98(0x1, 0xFFFF15A0, 0xFFFEEE90, 0x2BF20)
    OP_98(0x2, 0xFE, 0x9C40, 0x0)
    Return()

    # Function_8_B5F end

    def Function_9_C72(): pass

    label("Function_9_C72")

    OP_71(0x2, 0x2)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x4)
    OP_6F(0x2, 800)
    OP_8F(0xA, 0xFFFFD616, 0xFFFF6E7E, 0xFFFF4CE6, 0x2710, 0x0)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    Sleep(500)

    def lambda_CBA():
        OP_D1(254, 0, 0, 7000, 400)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CBA)
    OP_8F(0xA, 0xFFFF880A, 0xFFFF7748, 0xFFFF395E, 0x1F40, 0x0)

    def lambda_CE8():
        OP_D1(254, 0, 0, 0, 800)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CE8)
    Sleep(200)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0xFFFF6B0E, 0xFFFF89A4, 0xFFFFD788)
    OP_98(0x1, 0xFFFF434A, 0xFFFFB91A, 0x50DC)
    OP_98(0x2, 0xA, 0x61A8, 0x6)
    OP_71(0x2, 0x4)
    Return()

    # Function_9_C72 end

    def Function_10_D30(): pass

    label("Function_10_D30")

    Sleep(12000)
    OP_71(0x2, 0x2)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x4)
    OP_6F(0x2, 800)
    OP_D1(254, 0, 360000, 10000, 0)

    def lambda_D64():
        OP_D1(254, 0, 360000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_D64)

    def lambda_D7E():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7E)
    Sleep(1100)

    def lambda_D9E():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9E)
    Sleep(100)

    def lambda_DBE():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBE)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0x0, 0xFFFEEE90, 0xFFFF3CB0, 0xFA0, 0x0)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)

    def lambda_E05():
        OP_D1(254, 0, 330000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_E05)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF8300, 0xFFFEEE90, 0x13880)
    OP_98(0x1, 0xFFFEC780, 0xFFFEEE90, 0x27100)
    OP_98(0x2, 0xFE, 0x9C40, 0x0)
    Return()

    # Function_10_D30 end

    def Function_11_E43(): pass

    label("Function_11_E43")

    OP_71(0x3, 0x2)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x4)
    OP_6F(0x3, 800)
    OP_8F(0xB, 0xFFFFE1CE, 0xFFFF6E7E, 0xFFFED7B6, 0x2710, 0x0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    Sleep(500)

    def lambda_E8B():
        OP_D1(254, 0, 0, 7000, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E8B)
    OP_8F(0xB, 0xFFFF93C2, 0xFFFF7748, 0xFFFEC42E, 0x1F40, 0x0)

    def lambda_EB9():
        OP_D1(254, 0, 0, 0, 800)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EB9)
    Sleep(200)
    OP_98(0x0, 0xB)
    OP_98(0x1, 0xFFFF5F56, 0xFFFF955C, 0xFFFFD788)
    OP_98(0x1, 0xFFFF3792, 0xFFFFC4D2, 0x50DC)
    OP_98(0x2, 0xB, 0x61A8, 0x6)
    OP_71(0x3, 0x4)
    Return()

    # Function_11_E43 end

    def Function_12_F01(): pass

    label("Function_12_F01")

    Sleep(14000)
    OP_71(0x3, 0x2)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x4)
    OP_6F(0x3, 800)
    OP_D1(254, 0, 360000, -10000, 0)

    def lambda_F35():
        OP_D1(254, 0, 360000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_F35)

    def lambda_F4F():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F4F)
    Sleep(1100)

    def lambda_F6F():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F6F)
    Sleep(100)

    def lambda_F8F():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F8F)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0x0, 0xFFFEEE90, 0xFFFF3CB0, 0xFA0, 0x0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)

    def lambda_FD6():
        OP_D1(254, 0, 320000, 40000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_FD6)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF6B90, 0xFFFEEE90, 0x11170)
    OP_98(0x1, 0xFFFE7960, 0xFFFEEE90, 0x222E0)
    OP_98(0x2, 0xFE, 0x9C40, 0x0)
    Return()

    # Function_12_F01 end

    def Function_13_1014(): pass

    label("Function_13_1014")

    OP_71(0x4, 0x2)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x4)
    OP_6F(0x4, 800)
    OP_8F(0xC, 0xFFFFE1CE, 0xFFFF6E7E, 0xFFFF395E, 0x2710, 0x0)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    Sleep(500)

    def lambda_105C():
        OP_D1(254, 0, 0, 7000, 400)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_105C)
    OP_8F(0xC, 0xFFFF93C2, 0xFFFF7748, 0xFFFF25D6, 0x1F40, 0x0)

    def lambda_108A():
        OP_D1(254, 0, 0, 0, 800)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_108A)
    Sleep(200)
    OP_98(0x0, 0xC)
    OP_98(0x1, 0xFFFF6B0E, 0xFFFF89A4, 0xFFFFD788)
    OP_98(0x1, 0xFFFF434A, 0xFFFFB91A, 0x50DC)
    OP_98(0x2, 0xC, 0x61A8, 0x6)
    OP_71(0x4, 0x4)
    Return()

    # Function_13_1014 end

    def Function_14_10D2(): pass

    label("Function_14_10D2")

    Sleep(16000)
    OP_71(0x4, 0x2)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x4)
    OP_6F(0x4, 800)
    OP_D1(254, 0, 360000, -10000, 0)

    def lambda_1106():
        OP_D1(254, 0, 360000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1106)

    def lambda_1120():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1120)
    Sleep(1100)

    def lambda_1140():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1140)
    Sleep(100)

    def lambda_1160():
        OP_8F(0xFE, 0x0, 0xFFFEEC9C, 0xFFFF3CB0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1160)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0x0, 0xFFFEEE90, 0xFFFF3CB0, 0xFA0, 0x0)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)

    def lambda_11A7():
        OP_D1(254, 0, 310000, 40000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11A7)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF5420, 0xFFFEEE90, 0xEA60)
    OP_98(0x1, 0xFFFE2B40, 0xFFFEEE90, 0x1D4C0)
    OP_98(0x2, 0xFE, 0x9C40, 0x0)
    Return()

    # Function_14_10D2 end

    def Function_15_11E5(): pass

    label("Function_15_11E5")

    EventBegin(0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 1130, 150, -13000, 180)
    OP_6D(1440, 150, -16820, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(7000, 0)
    OP_6E(329, 0)
    OP_72(0x6, 0x4)

    def lambda_124B():
        OP_6B(2820, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_124B)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x6, 0)
    OP_70(0x6, 0xE6)
    OP_22(0x133, 0x0, 0x64)
    OP_73(0x6)

    def lambda_127B():
        OP_6D(1170, 150, -19540, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_127B)

    def lambda_1293():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1293)
    OP_8F(0x101, 0x3FC, 0x0, 0xFFFFAFCE, 0x1388, 0x0)
    WaitChrThread(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        "#1020F#5P啊啊……！\x02",
    )

    CloseMessageWindow()
    StopSound(0xF424, 0xC3500, 0x1F40)

    def lambda_1300():
        OP_6D(-2500, 0, -43740, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1300)

    def lambda_1318():
        OP_67(0, 26980, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1318)

    def lambda_1330():
        OP_6B(7990, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1330)

    def lambda_1340():
        OP_6C(44000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1340)

    def lambda_1350():
        OP_6E(338, 8000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1350)
    Sleep(4000)
    OP_8C(0x101, 135, 400)
    OP_8E(0x101, 0x2CD8, 0x0, 0xFFFF9F52, 0xBB8, 0x0)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(500)
    StopSound(0xF424, 0x6BC9C, 0x0)
    OP_6D(12590, 0, -23580, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(3110, 0)
    OP_6C(44000, 0)
    OP_6E(324, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x101,
        (
            "#1007F#6P糟糕了……\x01",
            "不知不觉好像跑到甲板上了。\x02\x03",

            "#1019F话说回来……\x01",
            "这里还真是大得离谱啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#1010F#5P看来要想逃出去的话，\x01",
            "必须要寻找到降落伞，\x01",
            "或者直接夺取飞艇……\x02\x03",

            "#1002F不管了，总之先前进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C26)
    EventEnd(0x0)
    Return()

    # Function_15_11E5 end

    def Function_16_14BC(): pass

    label("Function_16_14BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x384, 7)), scpexpr(EXPR_END)), "loc_14C4")
    Return()

    label("loc_14C4")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 980, 0, -65550, 180)
    OP_6D(1030, 150, -68450, 0)
    OP_67(0, 8150, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x12C)
    OP_0D()
    OP_22(0x133, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    SetChrPos(0xD, 2000, -3900, -76440, 0)
    SetChrPos(0xE, -180, -3900, -76440, 0)

    NpcTalk(    #3
        0xD,
        "男人的声音",
        "#1P在这里了！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_1599():
        OP_8F(0xFE, 0x3D4, 0x0, 0xFFFF09E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1599)

    def lambda_15B4():
        OP_6D(1120, 0, -66000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15B4)

    def lambda_15CC():
        OP_6B(2870, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15CC)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 8)

    def lambda_15F0():
        OP_90(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15F0)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 8)

    def lambda_161A():
        OP_90(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_161A)
    WaitChrThread(0xD, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 7)
    WaitChrThread(0xE, 0x1)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 7)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #4
        0x101,
        "#1020F#5P糟了……！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, 2000, 0, -35250, 180)
    SetChrPos(0x10, -180, 0, -35250, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_8C(0x101, 0, 600)

    def lambda_16B3():
        OP_6D(980, 0, -53000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16B3)

    def lambda_16CB():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16CB)

    def lambda_16E3():
        OP_6E(369, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16E3)

    def lambda_16F3():
        OP_6B(2510, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16F3)

    def lambda_1703():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1703)
    OP_43(0xF, 0x0, 0x0, 0x11)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0xE, 0x0, 0x0, 0x12)
    Sleep(100)
    OP_43(0xD, 0x0, 0x0, 0x12)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xD, 0x0)
    Sleep(800)

    ChrTalk(    #5
        0x101,
        "#1009F#6P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#4P呼……\x01",
            "看你还能往哪里跑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "#5P不愧是Ｓ级游击士——\x01",
            "『剑圣』卡西乌斯的女儿啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        "#5P竟然在这种状况下还敢逃走。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1002F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        (
            "#6P你应该明白才对，\x01",
            "徒劳的抵抗是没有用的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xE,
        "#6P还是乖乖投降吧。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x11, 950, 0, -37920, 180)
    ClearChrFlags(0x11, 0x80)
    Sleep(500)

    NpcTalk(    #12
        0x11,
        "青年的声音",
        (
            "#4P哈哈，真是丢脸啊。\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_18E6():
        OP_6D(1570, 0, -49360, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18E6)

    def lambda_18FE():
        OP_67(0, 5240, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18FE)
    OP_8E(0x11, 0x424, 0x0, 0xFFFF4B6A, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        "#1026F#4P……？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x11,
        "强化猎兵",
        (
            "#5P哼哼，戴上面具\x01",
            "就认不出我了吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #15
        0x11,
        "强化猎兵",
        (
            "#5P没办法了。\x01",
            "特别优待，让你看看我的真面目吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x101,
        "#1004F#4P咦……！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x11,
        "青年",
        (
            "#1226F#5P呵呵……\x01",
            "看来总算想起来了。\x02\x03",

            "#1220F做梦也没想到\x01",
            "会在这种地方见到我吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x18\x07\x05青年的真正身份是……？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【……您是哪位？】\x01",          # 0
            "【卡普亚空贼团的次子】\x01",      # 1
            "【戴尔蒙市长的秘书】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B1E"),
        (1, "loc_1BB9"),
        (2, "loc_1C76"),
        (SWITCH_DEFAULT, "loc_1D51"),
    )


    label("loc_1B1E")


    ChrTalk(    #19
        0x101,
        (
            "#1025F#4P唔……\x01",
            "见好像是见过。\x02\x03",

            "#1016F您是……哪位来着？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x11,
        "青年",
        (
            "#1225F#5P是戴尔蒙市长的前秘书，\x01",
            "基尔巴特！\x02\x03",

            "你自己逮捕过的人\x01",
            "好歹也该记清楚吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1BB9")


    ChrTalk(    #21
        0x101,
        (
            "#1025F#4P唔……\x01",
            "好像是有些眼熟…\x02\x03",

            "#1016F啊！是那个男人婆\x01",
            "的二哥吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x11,
        "青年",
        (
            "#1224F#5P那是谁啊！？\x02\x03",

            "#1225F我是戴尔蒙市长的前秘书——基尔巴特！\x02\x03",

            "你自己逮捕过的人\x01",
            "好歹也该记清楚吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1C76")


    ChrTalk(    #23
        0x101,
        (
            "#1016F#4P唔……\x01",
            "好像是在哪里见过，\x02\x03",

            "#1008F……是不是戴尔蒙市长的\x01",
            "那个秘书……？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x11,
        "青年",
        (
            "#1224F#5P干嘛那么\x01",
            "没自信的样子啊！\x02\x03",

            "#1225F对，我就是戴尔蒙市长的前秘书，\x01",
            "基尔巴特！\x02\x03",

            "你自己逮捕过的人\x01",
            "好歹也该记清楚吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1D51")


    ChrTalk(    #25
        0x101,
        (
            "#1020F#4P因、因为太意外了啦！\x02\x03",

            "#1019F你不是已经被\x01",
            "我们交给王国军关押了吗？\x02\x03",

            "为什么会在这种地方！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "#1226F#5P哼哼，发生政变事件的时候，\x01",
            "我趁乱逃脱了。\x02\x03",

            "#1221F之后我被『结社』收留，\x01",
            "并发誓从今以后永远效忠于『结社』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1007F#4P该、该说你执着\x01",
            "还是顽固不化呢……\x02\x03",

            "#1002F看你那身打扮，\x01",
            "莫非是想战斗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#1221F#5P我参加战斗很奇怪吗？\x02\x03",

            "#1226F哼，我虽然是个有文化的才子，\x01",
            "但毕竟也是个文武双全的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1015F#4P但你以前在灯塔被特务兵射中\x01",
            "的时候还大声惨叫来着……\x02\x03",

            "所以说，像你这样的人\x01",
            "实在不太适合战斗呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #30
        0x11,
        (
            "#1225F#5P啰、啰嗦！\x02\x03",

            "加入『结社』之后\x01",
            "我接受了战斗强化程序！\x02\x03",

            "身体能力被大幅度强化，\x01",
            "还学会了最高水平的战斗技术！\x02\x03",

            "区区一个游击士，别妄想打败我！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_200E():
        OP_6D(1530, 0, -51170, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_200E)

    def lambda_2026():
        OP_6E(450, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2026)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #31
        0xF,
        "#5P哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "#6P没办法了……\x01",
            "那就稍微陪你玩一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#1221F#5P好了……\x01",
            "艾丝蒂尔·布莱特。\x02\x03",

            "你还是跪下求饶吧。\x02\x03",

            "那样的话\x01",
            "我倒还可以饶过你哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007F#4P那可太谢谢了。\x01",
            "我高兴得连眼泪都要流出来了。\x02\x03",

            "#1006F不过不好意思，\x01",
            "我可是很执着的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x1F4, 0x0, 0x64)
    SetChrChipByIndex(0x101, 5)

    def lambda_217D():
        OP_99(0x101, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_217D)
    Sleep(200)

    def lambda_2192():
        OP_6D(1530, 0, -50500, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2192)

    def lambda_21AA():
        OP_6E(400, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21AA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #35
        0x11,
        "#1224F#5P唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1022F#4P『执行者』暂且不提，\x01",
            "我怎么可能会输给小喽啰嘛！\x02\x03",

            "#1005F好了──\x01",
            "放马过来吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2237():
        OP_6D(1170, 0, -52450, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2237)

    def lambda_224F():
        OP_6B(1800, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_224F)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0xF, 12)
    OP_43(0xF, 0x0, 0x0, 0x15)
    Sleep(50)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 12)
    OP_43(0x10, 0x0, 0x0, 0x15)
    SetChrChipByIndex(0x11, 26)

    def lambda_228B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_228B)
    Sleep(50)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 12)
    OP_43(0xD, 0x0, 0x0, 0x16)
    Sleep(50)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xE, 12)
    OP_43(0xE, 0x0, 0x0, 0x16)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    Battle(0x42A, 0x30000E, 0x0, 0x0, 0xFF)
    Call(0, 23)
    Return()

    # Function_16_14BC end

    def Function_17_22FC(): pass

    label("Function_17_22FC")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFCC70, 0x1388, 0x0)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_17_22FC end

    def Function_18_2325(): pass

    label("Function_18_2325")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0x3390, 0x1388, 0x0)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_18_2325 end

    def Function_19_234E(): pass

    label("Function_19_234E")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_19_234E end

    def Function_20_2372(): pass

    label("Function_20_2372")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0x4B0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_20_2372 end

    def Function_21_2396(): pass

    label("Function_21_2396")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF380, 0x1F40, 0x0)
    Return()

    # Function_21_2396 end

    def Function_22_23B0(): pass

    label("Function_22_23B0")

    SetChrChipByIndex(0xFE, 8)
    OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
    Return()

    # Function_22_23B0 end

    def Function_23_23CA(): pass

    label("Function_23_23CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_23FF"),
        (7, "loc_240C"),
        (1, "loc_2419"),
        (SWITCH_DEFAULT, "loc_2426"),
    )


    label("loc_23FF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2426")

    label("loc_240C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2426")

    label("loc_2419")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2426")

    label("loc_2426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2476")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇胜了】\x01",            # 0
            "【◇超过数回合】\x01",      # 1
            "【◇输了】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)

    label("loc_2476")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2494"),
        (1, "loc_27E5"),
        (2, "loc_2A2A"),
        (SWITCH_DEFAULT, "loc_2BFC"),
    )


    label("loc_2494")

    OP_2B(0x98, 0x5)
    OP_6D(1360, 0, -52330, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    OP_6D(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, 980, 0, -53200, 0)
    SetChrPos(0x11, 980, 0, -48100, 180)
    SetChrPos(0xD, 3500, 0, -56070, 315)
    SetChrPos(0xE, -1160, 0, -56070, 45)
    SetChrPos(0xF, 3300, 0, -50340, 225)
    SetChrPos(0x10, -1160, 0, -50440, 135)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xD, 9)
    SetChrSubChip(0xD, 3)
    SetChrChipByIndex(0xE, 9)
    SetChrSubChip(0xE, 3)
    SetChrChipByIndex(0xF, 9)
    SetChrSubChip(0xF, 3)
    SetChrChipByIndex(0x10, 9)
    SetChrSubChip(0x10, 3)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)

    def lambda_25D4():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_25D4)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x11,
        (
            "#1224F#5P不、不可能……\x01",
            "面对这么多人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1005F#4P呼……呼……\x01",
            "见识到游击士的力量了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "#2P不愧是『剑圣』的女儿……\x01",
            "好像有点小看你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xF,
        (
            "#5P……唔。\x01",
            "看来有必要解除禁制了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x1E)
    Sleep(50)
    OP_43(0x10, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x1E)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x1E)
    WaitChrThread(0xF, 0x1)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)

    ChrTalk(    #41
        0x11,
        (
            "#1221F#5P哈哈，大吃一惊吗？\x02\x03",

            "我们都是经由『结社』的技术\x01",
            "将身体能力进行了大幅度的强化，\x02\x03",

            "远比一般的人类强韧哟！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x0, 0x0, 0x1A)
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0x1B)
    Sleep(100)
    OP_43(0xF, 0x0, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0x1D)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #42
        0x101,
        "#1002F#4P可恶……\x02",
    )

    CloseMessageWindow()
    OP_28(0x99, 0x1, 0x20)
    Jump("loc_2BFC")

    label("loc_27E5")

    OP_2B(0x98, 0x2)
    OP_6D(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, 980, 0, -53200, 0)
    SetChrPos(0x11, 980, 0, -48100, 180)
    SetChrPos(0xD, 3500, 0, -56070, 315)
    SetChrPos(0xE, -1160, 0, -56070, 45)
    SetChrPos(0xF, 3300, 0, -50340, 225)
    SetChrPos(0x10, -1160, 0, -50440, 135)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xE, 7)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xF, 7)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_71(0x7, 0x4)

    def lambda_28ED():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28ED)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x101,
        (
            "#1022F#4P呼……呼……\x02\x03",

            "#1003F真、真是难对付啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#1224F#5P好、好顽强的小丫头……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "#2P不过看起来……\x01",
            "你也已经气喘吁吁了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xF,
        (
            "#5P游戏到此为止。\x01",
            "现在就要缩小包围圈了！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x0, 0x0, 0x1A)
    Sleep(100)
    OP_43(0xE, 0x0, 0x0, 0x1B)
    Sleep(100)
    OP_43(0xF, 0x0, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0x1D)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #47
        0x101,
        "#1002F#4P可恶……\x02",
    )

    CloseMessageWindow()
    OP_28(0x99, 0x1, 0x40)
    Jump("loc_2BFC")

    label("loc_2A2A")

    OP_6D(1450, 0, -51300, 0)
    OP_67(0, 5350, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(270, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, 980, 0, -53200, 0)
    SetChrPos(0x11, 980, 0, -48100, 180)
    SetChrPos(0xD, 3000, 0, -55570, 315)
    SetChrPos(0xE, -660, 0, -55570, 45)
    SetChrPos(0xF, 2850, 0, -50940, 225)
    SetChrPos(0x10, -660, 0, -50940, 135)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xE, 7)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0xF, 7)
    SetChrSubChip(0xF, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)

    def lambda_2B28():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B28)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #48
        0x101,
        "#1021F#4P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#1226F哼，只会逞口舌之利的小丫头。\x02\x03",

            "虽然我不会杀你，\x01",
            "但总要让你稍微吃点苦头。\x02\x03",

            "#1221F哼哼哼……\x01",
            "让我高兴一下如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1002F#4P……………………………\x02",
    )

    CloseMessageWindow()
    OP_28(0x99, 0x1, 0x80)
    Jump("loc_2BFC")

    label("loc_2BFC")

    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1000, 0, -65850, 0)
    Sleep(500)

    NpcTalk(    #51
        0x12,
        "男人的声音",
        "#1P……我没来晚吧！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    SetChrFlags(0x101, 0x800)
    OP_6D(920, 0, -55380, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(181000, 0)
    OP_6E(270, 0)

    def lambda_2CF1():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFF1A1E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2CF1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D33")
    Sleep(100)
    SetChrFlags(0x101, 0x20)
    OP_8C(0x101, 180, 400)
    ClearChrFlags(0x101, 0x20)

    label("loc_2D33")

    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    NpcTalk(    #52
        0x12,
        "强化猎兵",
        "#5P似乎陷入苦战了啊。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #53
        0x12,
        "强化猎兵",
        "#5P让我来助你一臂之力吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E18")

    ChrTalk(    #54
        0x11,
        (
            "#1221F#6P哈哈，没那个必要。\x02\x03",

            "虽然是个顽强的丫头，\x01",
            "但让她彻底屈服也只是时间问题。\x02\x03",

            "你就待在那里好好看着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E6E")

    label("loc_2E18")


    ChrTalk(    #55
        0x11,
        (
            "#1221F#6P哈哈，没那个必要。\x02\x03",

            "好戏现在才刚刚\x01",
            "要开始呢！\x02\x03",

            "你就站在那里安静看着吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6E")


    NpcTalk(    #56
        0x12,
        "强化猎兵",
        (
            "#5P……我可不是\x01",
            "在和你说话哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#1224F#6P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 14)
    OP_0D()
    Sleep(100)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2F45():
        TurnDirection(0xFE, 0x12, 600)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F45)
    Sleep(50)

    def lambda_2F58():
        TurnDirection(0xFE, 0x12, 600)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2F58)
    Sleep(50)

    def lambda_2F6B():
        TurnDirection(0xFE, 0x12, 600)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2F6B)
    Sleep(50)

    def lambda_2F7E():
        TurnDirection(0xFE, 0x12, 600)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F7E)
    OP_22(0x1F5, 0x0, 0x64)

    def lambda_2F91():
        OP_99(0xFE, 0x1, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2F91)
    WaitChrThread(0x12, 0x0)

    NpcTalk(    #58
        0x12,
        "强化猎兵",
        "#5P……太慢了！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    ClearChrFlags(0x101, 0x800)
    OP_6D(1070, 0, -54680, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(15000, 0)
    OP_6E(300, 0)
    LoadEffect(0x4, "Craft\\\\cr161_00.eff")
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3034():
        OP_6D(1300, 0, -49560, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3034)

    def lambda_304C():
        OP_6B(2800, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_304C)

    def lambda_305C():
        OP_6C(45000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_305C)
    OP_7D(0x0, 0x12, 0x14, 0x1F4)
    OP_43(0x12, 0x0, 0x0, 0x23)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0xD, 0x0, 0x0, 0x25)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0xE, 0x0, 0x0, 0x27)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0xF, 0x0, 0x0, 0x26)
    Sleep(200)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_43(0x10, 0x0, 0x0, 0x28)
    SetChrPos(0x12, 1150, 0, -51670, 0)

    def lambda_3100():
        OP_96(0xFE, 0x41A, 0x0, 0xFFFF3DDC, 0x64, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3100)

    def lambda_311E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_311E)
    OP_22(0x9B, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)
    OP_7D(0x1, 0x12, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Sleep(1500)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x12, 0x9, 0xC, 0x5DC)
    Sleep(500)
    OP_43(0xD, 0x0, 0x0, 0x1F)
    Sleep(120)
    OP_43(0xE, 0x0, 0x0, 0x20)
    Sleep(80)
    OP_43(0xF, 0x0, 0x0, 0x21)
    Sleep(120)
    OP_43(0x10, 0x0, 0x0, 0x22)
    WaitChrThread(0x10, 0x0)
    OP_96(0x11, 0x3D4, 0x0, 0xFFFF441C, 0x190, 0x1388)

    def lambda_31AF():
        OP_6D(1570, 0, -48000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31AF)

    def lambda_31C7():
        OP_91(0x11, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_31C7)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #59
        0x11,
        "#1224F#5P什、什、什么！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_323D")
    SetChrFlags(0x101, 0x20)
    OP_8C(0x101, 0, 400)
    ClearChrFlags(0x101, 0x20)
    Jump("loc_3251")

    label("loc_323D")

    OP_99(0x101, 0x3, 0x0, 0x5DC)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 4)
    OP_0D()

    label("loc_3251")

    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#1004F#4P…………咦……………\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #61
        0x11,
        (
            "#1224F#5P你、你在干什么！？\x01",
            "到底想怎样！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #62
        0x12,
        "强化猎兵",
        (
            "#4P不好意思……\x01",
            "我也认为你并不适合战斗。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "scraft\\\\sc000_11.eff")
    OP_99(0x12, 0x0, 0x3, 0x4B0)
    OP_7D(0x0, 0x12, 0x32, 0x1F4)
    OP_43(0x12, 0x1, 0x0, 0x29)
    Sleep(100)

    def lambda_332C():
        OP_6D(2360, 0, -45710, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_332C)

    def lambda_3344():
        OP_6B(3200, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3344)
    WaitChrThread(0x12, 0x1)
    OP_7D(0x1, 0x12, 0x0, 0x0)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x20)
    ClearChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 28)
    SetChrSubChip(0x11, 5)
    OP_96(0x11, 0xFFFFFEA2, 0x0, 0xFFFF4D04, 0x190, 0x2710)

    ChrTalk(    #63 op#5
        0x11,
        "#1227F#5P呜哇！\x05\x02",
    )

    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 5)
    OP_96(0x11, 0xFFFFFBC8, 0x0, 0xFFFF5164, 0xC8, 0x1F40)

    def lambda_33D8():
        OP_8F(0xFE, 0xFFFFF8E4, 0x0, 0xFFFF56DC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_33D8)
    Sleep(50)

    def lambda_33F8():
        OP_8F(0xFE, 0xFFFFF8E4, 0x0, 0xFFFF56DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_33F8)
    Sleep(50)

    def lambda_3418():
        OP_8F(0xFE, 0xFFFFF8E4, 0x0, 0xFFFF56DC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3418)
    WaitChrThread(0x11, 0x2)
    Sleep(1000)
    OP_20(0xBB8)

    def lambda_3442():
        OP_6D(1870, 0, -49200, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3442)

    def lambda_345A():
        OP_6E(308, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_345A)
    Sleep(200)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x12, 0x8, 0xC, 0x5DC)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #64
        0x101,
        "#1004F#4P……………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x12,
        "强化猎兵",
        (
            "#5P……真是的。\x01",
            "你到底在想什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_1D(0x50)
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 30)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x1000)
    SetChrChipByIndex(0x13, 30)
    SetChrSubChip(0x13, 16)
    SetChrPos(0x13, 1500, 600, -48250, 0)

    def lambda_353C():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_353C)
    OP_99(0x12, 0x1, 0x6, 0x514)
    OP_43(0x13, 0x0, 0x0, 0x18)
    OP_99(0x12, 0x7, 0x9, 0x514)
    WaitChrThread(0x13, 0x0)
    Sleep(1500)

    NpcTalk(    #66
        0x12,
        "黑发的少年",
        (
            "#1135F#5P已经当上了正游击士，\x01",
            "但还是和从前一样冒失啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 180, 300)
    Sleep(500)

    NpcTalk(    #67
        0x12,
        "黑发的少年",
        (
            "#1130F#5P在这种时候\x01",
            "有必要如此犯险拼命吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1025F……啊………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364F")
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    Jump("loc_366E")

    label("loc_364F")

    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    label("loc_366E")


    ChrTalk(    #69
        0x101,
        (
            "#1016F#4P啊哈哈……是约修亚……\x02\x03",

            "#1008F唔……不是在做梦吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x12,
        (
            "#1131F#5P真要是做梦的话\x01",
            "那可就轻松多了……\x02\x03",

            "#1135F……但现在的情况\x01",
            "似乎没有那么乐观啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1004F#4P哎……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x14, 1190, 0, -36000, 180)
    ClearChrFlags(0x14, 0x80)

    NpcTalk(    #72
        0x14,
        "青年的声音",
        (
            "#4P呵呵……\x01",
            "你总算现身了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3786():
        OP_6D(2020, 0, -43560, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3786)

    def lambda_379E():
        OP_67(0, 4000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_379E)

    def lambda_37B6():
        OP_6E(263, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37B6)

    def lambda_37C6():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_37C6)

    def lambda_37D6():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFF5EE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_37D6)
    Sleep(500)

    def lambda_37F6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_37F6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    ChrTalk(    #73
        0x12,
        (
            "#1131F#4P……好久不见，莱维。\x02\x03",

            "你好像已经预料到\x01",
            "我会潜入这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x14,
        (
            "#124F#5P从你的能力特点来考虑，\x01",
            "这么做并不奇怪。\x02\x03",

            "#120F不过你究竟是用什么手段潜入的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x12,
        (
            "#1135F#4P在登上这艘船之前，\x01",
            "我就已经潜入到一艘侦察艇了。\x02\x03",

            "#1131F由于里面没有『执行者』，\x01",
            "我的潜入实在是意外的简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14,
        (
            "#120F#5P……连教授会动用方舟\x01",
            "都被你给预料到了吗。\x02\x03",

            "#124F看来你身为『执行者』的直觉\x01",
            "已经完全找回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x12,
        (
            "#1131F#4P托你的福。\x02\x03",

            "其实我一直都很担心，\x01",
            "怕突然被莱维或别人发觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x14,
        (
            "#124F#5P哼，不用谦虚，\x01",
            "没有任何人可以识破你的隐形术。\x02\x03",

            "#123F不过，所谓的隐形术，\x01",
            "一旦现形就毫无用处了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #79
        0x14,
        (
            "#120F#5P你已经失去了最大的武器。\x02\x03",

            "面对我『剑帝』，\x01",
            "你有何打算？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#1130F#4P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1P慢、慢着……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x101, 29)
    SetChrFlags(0x101, 0x1000)

    def lambda_3AFF():
        OP_6D(1760, 0, -43630, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AFF)

    def lambda_3B17():
        OP_67(0, 5000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B17)

    def lambda_3B2F():
        OP_6B(3300, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3B2F)
    OP_8F(0x101, 0x3C, 0x0, 0xFFFF3ED6, 0x1388, 0x0)
    SetChrChipByIndex(0x101, 4)
    WaitChrThread(0x101, 0x3)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #82
        0x101,
        (
            "#1005F#6P话说在先！\x01",
            "我也可以继续战斗！\x02\x03",

            "不管你有多强，\x01",
            "也别想轻轻松松就把我们两个……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x12,
        (
            "#1135F#2P……退下，艾丝蒂尔。\x02\x03",

            "#1133F莱维的实力太强了，\x01",
            "即使你我联手也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1019F#6P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x14,
        (
            "#124F#5P你既然明白这一点，\x01",
            "为什么还敢贸然现身？\x02\x03",

            "为了救她的话，倒是可以理解，\x01",
            "我也并不想指责你太过天真……\x02\x03",

            "#120F但你如果真的这么在意她，\x01",
            "当初为何还要从她的面前消失？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        "#1133F#2P………唔…………！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x14,
        (
            "#120F#5P要守护就守护到底，\x01",
            "要舍弃就别再回头。\x02\x03",

            "一旦作出选择就要贯彻到底。\x01",
            "我不是教过你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x12,
        (
            "#1131F#2P嗯……是啊。\x02\x03",

            "在经过教授的改造之后……\x01",
            "第一次的训练时，你就这么教导我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x14,
        (
            "#124F#5P如果那女孩真的那么重要，\x01",
            "那你无论如何也不该离开她。\x02\x03",

            "即使承受着罪恶感的苛责，\x01",
            "也要一直待在她的身边。\x02\x03",

            "#121F你之所以没有这么做，\x01",
            "只是因为在逃避，在自我欺瞒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x12,
        (
            "#1135F#2P我明白……\x02\x03",

            "#1137F即使莱维不说\x01",
            "我也明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x14,
        "#120F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1026F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x12,
        (
            "#1133F#2P可是……可是……\x01",
            "莱维，你自己又是如何呢……？\x02\x03",

            "需要偿还代价的…\x01",
            "本应只有我一人……\x02\x03",

            "但为什么连你也要加入『结社』，\x01",
            "变成了如今的『剑帝』呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #95
        0x12,
        (
            "#1136F#2P为什么你直到现在…\x01",
            "还在协助教授那种人……！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #96
        0x14,
        (
            "#124F#5P………………………………\x02\x03",

            "#121F我协助教授…\x01",
            "同你完全没有关系。\x02\x03",

            "纯粹只是我自己的意愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x12,
        (
            "#1136F#2P莱维的意愿……\x02\x03",

            "那么说…果然还是\x01",
            "为了给卡琳姐……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x14,
        (
            "#124F#5P即使复了仇，\x01",
            "卡琳也无法再回来了。\x02\x03",

            "#123F所以我……\x01",
            "决定向世界发起试炼。\x02\x03",

            "这就是我协助教授的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x12,
        "#1134F#2P向世界发起试炼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x14,
        (
            "#124F#5P好了……\x01",
            "言尽于此。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x14, 0x2)
    SetChrSubChip(0x14, 5)
    SetChrChipByIndex(0x14, 18)
    OP_0D()
    Sleep(500)

    ChrTalk(    #101
        0x14,
        (
            "#121F#5P你有三条路可以选择。\x02\x03",

            "#124F和那女孩一起投降。\x01",
            "或是保护她，死在我的剑下。\x01",
            "再来就是扔下她，自己一个人逃跑。\x02\x03",

            "#120F怎样──快点做出选择吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1026F#6P约、约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x12,
        (
            "#1133F#2P……………………………\x02\x03",

            "#1135F不好意思，\x01",
            "我要选第四条路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x14,
        "#126F#5P什么……\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x2A)
    OP_43(0x101, 0x2, 0x0, 0x2B)
    Sleep(1000)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #105
        0x101,
        "#1020F#6P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x14,
        "#126F#5P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x12,
        (
            "#1135F#2P……我在导力引擎上\x01",
            "稍微做了点手脚。\x02\x03",

            "要是置之不理的话，这艘船\x01",
            "就会化为海底的藻屑了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #108
        0x101,
        "#1005F#6P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x14, 0x2)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x14, 16)
    OP_0D()
    Sleep(500)

    ChrTalk(    #109
        0x14,
        (
            "#121F#5P……真有你的。\x02\x03",

            "没想到你竟能入侵\x01",
            "需要认证的引擎室……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        (
            "#1131F#2P现在２２个引擎全部\x01",
            "都被我做了不同的设置……\x02\x03",

            "如今教授和玲都不在，\x01",
            "能解除的就只有莱维了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x14,
        (
            "#124F#5P这是你为了阻止我们的计划\x01",
            "而留下来的最后一张底牌吗……\x02\x03",

            "#123F但你却在这个时候\x01",
            "就把它亮了出来……\x02\x03",

            "你打算逃避、欺瞒\x01",
            "到什么时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12,
        "#1133F#2P………这…………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 400)
    Sleep(500)

    ChrTalk(    #113
        0x14,
        (
            "#125F#5P呵呵，下次再见时\x01",
            "准备好答案就行了。\x02\x03",

            "#122F我期待着。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4543():
        OP_6D(1490, 0, -41340, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4543)
    OP_8E(0x14, 0x4CE, 0x96, 0xFFFF95C0, 0xBB8, 0x0)
    SetChrFlags(0x14, 0x80)
    OP_6D(1160, 0, -47700, 2500)
    Sleep(500)

    ChrTalk(    #114
        0x12,
        "#1133F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)
    TurnDirection(0x101, 0x12, 400)
    Sleep(500)

    ChrTalk(    #115
        0x101,
        (
            "#1025F#6P那个，约修亚……\x02\x03",

            "#1003F我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x12,
        "#1135F#5P……有什么话稍后再说。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x101, 400)
    Sleep(500)

    ChrTalk(    #117
        0x12,
        (
            "#1131F#5P我们首先要抢到\x01",
            "一架逃脱用的飞艇。\x02\x03",

            "从前面的阶梯下去\x01",
            "就可以到达停泊飞艇的机库了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1026F#6P啊……\x02\x03",

            "#1002F嗯……明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_31(0x1, 0x0, 0x4B)
    OP_41(0x1, 0x0, 0xFF)
    OP_41(0x1, 0x25, 0xFF)
    OP_41(0x1, 0x103, 0xFF)
    OP_41(0x1, 0x124, 0xFF)
    OP_35(0x1, 0x0)
    OP_37(0x1, 0x7F, 0x2)
    OP_41(0x1, 0x2A6, 0x0)
    OP_41(0x1, 0x2A2, 0x1)
    OP_41(0x1, 0x2CB, 0x2)
    OP_41(0x1, 0x2C7, 0x3)
    OP_41(0x1, 0x25D, 0x4)
    OP_41(0x1, 0x266, 0x5)
    OP_41(0x1, 0x260, 0x6)
    OP_71(0x7, 0x4)
    SetChrFlags(0x13, 0x80)
    OP_6D(1070, 0, -47920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x1, 0xF6, 0xFF)
    AddParty(0x0, 0xF7, 0xFF)
    OP_BB(0x1, 0x0, 0x200033)
    OP_BB(0x1, 0x1, 0x1)
    OP_BD()
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x0, 1070, 0, -47920, 180)
    SetChrPos(0x1, 1070, 0, -47920, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1C27)
    OP_28(0x99, 0x1, 0x100)
    OP_28(0x99, 0x1, 0x200)
    OP_1D(0x71)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_23_23CA end

    def Function_24_47C4(): pass

    label("Function_24_47C4")

    ClearChrFlags(0xFE, 0x80)
    SetChrSubChip(0x13, 16)
    OP_8E(0x13, 0x7B2, 0x0, 0xFFFF407A, 0xFA0, 0x0)
    OP_22(0xB1, 0x0, 0x64)

    def lambda_47ED():
        OP_99(0xFE, 0x11, 0x13, 0x514)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_47ED)
    OP_96(0x13, 0x9E2, 0x0, 0xFFFF3E0E, 0x258, 0x5DC)
    WaitChrThread(0x13, 0x1)

    def lambda_4819():
        OP_99(0xFE, 0x14, 0x17, 0x514)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4819)
    OP_96(0x13, 0xBA4, 0x0, 0xFFFF3C42, 0x12C, 0x4B0)
    WaitChrThread(0x13, 0x1)

    def lambda_4845():
        OP_99(0xFE, 0x18, 0x19, 0x514)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4845)
    OP_8E(0x13, 0xBB8, 0x0, 0xFFFF3B84, 0x1F4, 0x0)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_24_47C4 end

    def Function_25_4869(): pass

    label("Function_25_4869")

    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    ClearChrFlags(0xD, 0x1)
    SetChrSubChip(0xD, 13)
    SetChrChipByIndex(0xD, 10)
    SetChrPos(0xD, 4520, 0, -54070, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x2)
    ClearChrFlags(0xE, 0x1)
    SetChrSubChip(0xE, 13)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, -1990, 0, -54000, 180)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    ClearChrFlags(0xF, 0x1)
    SetChrSubChip(0xF, 14)
    SetChrChipByIndex(0xF, 10)
    SetChrPos(0xF, 4380, 0, -49440, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x1)
    SetChrSubChip(0x10, 12)
    SetChrChipByIndex(0x10, 10)
    SetChrPos(0x10, -1800, 0, -49280, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x1)
    SetChrSubChip(0x11, 6)
    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 5)
    SetChrPos(0x11, -1820, 0, -43300, 180)
    Return()

    # Function_25_4869 end

    def Function_26_4941(): pass

    label("Function_26_4941")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    OP_8E(0xFE, 0xBB8, 0x0, 0xFFFF26EE, 0x1F4, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_26_4941 end

    def Function_27_496A(): pass

    label("Function_27_496A")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0xFFFF26EE, 0x1F4, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_27_496A end

    def Function_28_4993(): pass

    label("Function_28_4993")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    OP_8E(0xFE, 0xB22, 0x0, 0xFFFF3904, 0x1F4, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_28_4993 end

    def Function_29_49BC(): pass

    label("Function_29_49BC")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    OP_8E(0xFE, 0xFFFFFD6C, 0x0, 0xFFFF3904, 0x1F4, 0x0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_29_49BC end

    def Function_30_49E5(): pass

    label("Function_30_49E5")

    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 7)
    Return()

    # Function_30_49E5 end

    def Function_31_4A16(): pass

    label("Function_31_4A16")

    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)

    def lambda_4A40():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFF38, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A40)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 13)
    SetChrChipByIndex(0xFE, 10)
    Return()

    # Function_31_4A16 end

    def Function_32_4A6F(): pass

    label("Function_32_4A6F")

    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)

    def lambda_4A99():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFFF38, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A99)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 13)
    SetChrChipByIndex(0xFE, 10)
    Return()

    # Function_32_4A6F end

    def Function_33_4AC8(): pass

    label("Function_33_4AC8")

    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 225, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)

    def lambda_4AF2():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0xFFFFFF06, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AF2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 14)
    SetChrChipByIndex(0xFE, 10)
    Return()

    # Function_33_4AC8 end

    def Function_34_4B21(): pass

    label("Function_34_4B21")

    ClearChrFlags(0xFE, 0x2)
    OP_8C(0xFE, 135, 0)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)

    def lambda_4B4B():
        OP_91(0xFE, 0xC8, 0x0, 0xFFFFFF38, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B4B)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    SetChrSubChip(0xFE, 12)
    SetChrChipByIndex(0xFE, 10)
    Return()

    # Function_34_4B21 end

    def Function_35_4B7A(): pass

    label("Function_35_4B7A")

    SetChrFlags(0xFE, 0x1000)

    def lambda_4B85():
        OP_99(0xFE, 0x3, 0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B85)

    def lambda_4B95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B95)
    OP_96(0xFE, 0x4A6, 0x0, 0xFFFF29AA, 0x64, 0x7D0)
    Return()

    # Function_35_4B7A end

    def Function_36_4BB9(): pass

    label("Function_36_4BB9")

    SetChrFlags(0xFE, 0x1000)

    def lambda_4BC4():
        OP_99(0xFE, 0x3, 0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BC4)
    OP_96(0xFE, 0xB54, 0x0, 0xFFFF3E9A, 0x64, 0x55F0)
    Return()

    # Function_36_4BB9 end

    def Function_37_4BE6(): pass

    label("Function_37_4BE6")

    PlayEffect(0x4, 0x0, 0xFE, 0, 0, 0, 0, 0, 0, 1500, 1100, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 27)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0x5DC, 0x0, 0x5DC, 0x2710, 0x0)
    OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_4BE6 end

    def Function_38_4C61(): pass

    label("Function_38_4C61")

    PlayEffect(0x4, 0x1, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 6)
    SetChrChipByIndex(0xFE, 27)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0x5DC, 0x0, 0x5DC, 0x2710, 0x0)
    OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_38_4C61 end

    def Function_39_4CDC(): pass

    label("Function_39_4CDC")

    PlayEffect(0x4, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1300, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 5)
    SetChrChipByIndex(0xFE, 27)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x2710, 0x0)
    OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_39_4CDC end

    def Function_40_4D57(): pass

    label("Function_40_4D57")

    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 4)
    SetChrChipByIndex(0xFE, 27)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x2710, 0x0)
    OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_40_4D57 end

    def Function_41_4D9D(): pass

    label("Function_41_4D9D")


    def lambda_4DA3():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_4DA3)
    OP_8E(0x12, 0x42E, 0x0, 0xFFFF44D0, 0x4E20, 0x0)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x11, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_41_4D9D end

    def Function_42_4DFC(): pass

    label("Function_42_4DFC")

    OP_7C(0xC8, 0x0, 0x7D0, 0x3E8)
    Sleep(1000)
    OP_7C(0x64, 0x0, 0x3E8, 0x3E8)
    Sleep(1000)
    OP_7C(0x32, 0x0, 0x1F4, 0x3E8)
    Sleep(1000)
    OP_7C(0x19, 0x0, 0xFA, 0x3E8)
    Sleep(1000)
    OP_7C(0xC, 0x0, 0x7D, 0x3E8)
    Sleep(1000)
    Return()

    # Function_42_4DFC end

    def Function_43_4E6B(): pass

    label("Function_43_4E6B")

    OP_22(0x85, 0x1, 0x64)
    Sleep(4000)
    OP_24(0x85, 0x5F)
    Sleep(100)
    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x55)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x4B)
    Sleep(100)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x41)
    Sleep(100)
    OP_24(0x85, 0x32)
    Sleep(100)
    OP_24(0x85, 0x37)
    Sleep(100)
    OP_24(0x85, 0x32)
    OP_23(0x85)
    Return()

    # Function_43_4E6B end

    def Function_44_4ECE(): pass

    label("Function_44_4ECE")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_A1(0x8, 0x8)
    OP_71(0x8, 0x2)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 800)
    OP_70(0x8, 0x384)
    SetChrPos(0x8, -43670, -35000, -67540, 0)
    OP_6D(-5510, 0, -14200, 0)
    OP_67(0, 9720, -10000, 0)
    OP_6B(23040, 0)
    OP_6C(161000, 0)
    OP_6E(270, 0)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    FadeToBright(1000, 0)

    def lambda_4F72():
        OP_67(0, 8070, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F72)

    def lambda_4F8A():
        OP_6E(245, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F8A)
    OP_98(0x0, 0x8)
    OP_98(0x1, 0xFFFF6370, 0xAFC8, 0xDAC0)
    OP_98(0x1, 0xFFFF9C3C, 0x2E630, 0x318F8)
    OP_98(0x2, 0x8, 0xEA60, 0x6)
    OP_71(0x8, 0x4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_44_4ECE end

    def Function_45_4FDA(): pass

    label("Function_45_4FDA")

    EventBegin(0x0)
    OP_11(0xFF, 0xFF, 0xFF, 0x186A0, 0xF4240, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    OP_A1(0x8, 0x8)
    OP_71(0x8, 0x2)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 800)
    OP_70(0x8, 0x384)
    SetChrPos(0x8, -15000, -70000, -68000, 0)
    OP_D1(8, -20000, 240000, 20000, 0)
    OP_6D(-79860, -8550, -145600, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(14000, 0)
    OP_6C(59000, 0)
    OP_6E(649, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_22(0x131, 0x1, 0x46)
    FadeToBright(1000, 0)

    def lambda_50AB():
        OP_6D(-39860, -8550, -145600, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50AB)

    def lambda_50C3():
        OP_D1(254, -20000, 220000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_50C3)
    OP_98(0x0, 0x8)
    OP_98(0x1, 0xFFFE1BA0, 0x7530, 0xFFFDA288)
    OP_98(0x1, 0xFFFD67F0, 0x12110, 0xFFFC9118)

    def lambda_50FD():
        OP_98(0x2, 0xFE, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_50FD)
    Sleep(2000)

    def lambda_5112():
        OP_D1(254, -20000, 210000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5112)
    WaitChrThread(0x8, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_45_4FDA end

    def Function_46_5148(): pass

    label("Function_46_5148")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_6D(-25640, -21130, -27140, 0)
    OP_67(0, 12400, -10000, 0)
    OP_6B(5680, 0)
    OP_6C(143000, 0)
    OP_6E(803, 0)
    OP_A1(0x8, 0x0)
    OP_A1(0x9, 0x1)
    OP_A1(0xA, 0x2)
    SetChrPos(0x8, -10470, -35000, -49220, 0)
    SetChrPos(0x9, -12870, -35000, -61390, 0)
    SetChrPos(0xA, -12070, -35000, -76540, 0)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    FadeToBright(1000, 0)

    def lambda_51FB():
        OP_6D(-25950, -21130, -30440, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51FB)

    def lambda_5213():
        OP_6C(111000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5213)
    OP_43(0x8, 0x1, 0x0, 0x30)
    Sleep(1000)
    OP_43(0x9, 0x1, 0x0, 0x32)
    Sleep(1000)
    OP_43(0xA, 0x1, 0x0, 0x34)
    WaitChrThread(0xA, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_46_5148 end

    def Function_47_5259(): pass

    label("Function_47_5259")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xFF, 0xFF, 0xFF, 0x186A0, 0xF4240, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    OP_6D(-79860, -8550, -145600, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(14000, 0)
    OP_6C(59000, 0)
    OP_6E(649, 0)
    OP_A1(0x8, 0x0)
    OP_A1(0x9, 0x1)
    OP_A1(0xA, 0x2)
    SetChrPos(0x8, -15000, -70000, -68000, 0)
    SetChrPos(0x9, -15000, -70000, -38000, 0)
    SetChrPos(0xA, -15000, -70000, -8000, 0)
    OP_D1(8, 0, 180000, 0, 0)
    OP_D1(9, 0, 180000, 0, 0)
    OP_D1(10, 0, 180000, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_22(0x131, 0x1, 0x46)
    OP_71(0x0, 0x2)
    OP_72(0x0, 0x4)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_71(0x1, 0x2)
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x384)
    OP_71(0x2, 0x2)
    OP_72(0x2, 0x4)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    Sleep(2000)
    FadeToBright(2000, 0)

    def lambda_53C5():
        OP_6D(-39860, -8550, -145600, 10500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53C5)
    OP_43(0x8, 0x1, 0x0, 0x31)
    OP_43(0x9, 0x1, 0x0, 0x33)
    OP_43(0xA, 0x1, 0x0, 0x35)
    WaitChrThread(0xA, 0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0610   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_47_5259 end

    def Function_48_540E(): pass

    label("Function_48_540E")

    OP_71(0x0, 0x2)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x4)
    OP_6F(0x0, 800)
    OP_8F(0x8, 0xFFFF6B18, 0xFFFF7748, 0xFFFF284C, 0x61A8, 0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)
    OP_8F(0x8, 0xFFFF6348, 0xFFFF7748, 0xFFFF3FBC, 0x9C40, 0x0)
    OP_98(0x0, 0x8)
    OP_98(0x1, 0xFFFF623A, 0xFFFFB1E0, 0xFFFF89F4)
    OP_98(0x1, 0xFFFF6DF2, 0x276, 0xFFFFE00C)
    OP_98(0x1, 0xFFFF89D6, 0xC968, 0xBA5E)
    OP_98(0x2, 0x8, 0xD6D8, 0x6)
    OP_71(0x0, 0x4)
    Return()

    # Function_48_540E end

    def Function_49_549C(): pass

    label("Function_49_549C")


    def lambda_54A2():
        OP_D1(254, -20000, 220000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_54A2)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFE1BA0, 0x7530, 0xFFFDA288)
    OP_98(0x1, 0xFFFD67F0, 0x12110, 0xFFFC9118)

    def lambda_54DC():
        OP_98(0x2, 0xFE, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_54DC)
    Sleep(2000)

    def lambda_54F1():
        OP_D1(254, -20000, 210000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_54F1)
    WaitChrThread(0xFE, 0x0)
    OP_71(0x0, 0x4)
    Return()

    # Function_49_549C end

    def Function_50_5510(): pass

    label("Function_50_5510")

    OP_71(0x1, 0x2)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x4)
    OP_6F(0x1, 800)
    OP_8F(0x9, 0xFFFF6BF4, 0xFFFF7748, 0xFFFEF8C2, 0x61A8, 0x0)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 800)
    OP_70(0x1, 0x384)
    OP_8F(0x9, 0xFFFF603C, 0xFFFF7748, 0xFFFF1032, 0x61A8, 0x0)
    OP_98(0x0, 0x9)
    OP_98(0x1, 0xFFFF623A, 0xFFFFB1E0, 0xFFFF89F4)
    OP_98(0x1, 0xFFFF6DF2, 0x276, 0xFFFFE00C)
    OP_98(0x1, 0xFFFF89D6, 0xC968, 0xBA5E)
    OP_98(0x2, 0x9, 0xD6D8, 0x6)
    OP_71(0x1, 0x4)
    Return()

    # Function_50_5510 end

    def Function_51_559E(): pass

    label("Function_51_559E")

    OP_8F(0xFE, 0xFFFFC568, 0xFFFEEE90, 0xFFFEF660, 0x4E20, 0x0)

    def lambda_55B8():
        OP_D1(254, -20000, 220000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_55B8)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFE1BA0, 0x7530, 0xFFFDA288)
    OP_98(0x1, 0xFFFD67F0, 0x12110, 0xFFFC9118)

    def lambda_55F2():
        OP_98(0x2, 0xFE, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_55F2)
    Sleep(2000)

    def lambda_5607():
        OP_D1(254, -20000, 210000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5607)
    WaitChrThread(0xFE, 0x0)
    OP_71(0x1, 0x4)
    Return()

    # Function_51_559E end

    def Function_52_5626(): pass

    label("Function_52_5626")

    OP_71(0x2, 0x2)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x4)
    OP_6F(0x2, 800)
    OP_8F(0xA, 0xFFFF6B2C, 0xFFFF7748, 0xFFFEBD94, 0x61A8, 0x0)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_8F(0xA, 0xFFFF603C, 0xFFFF7748, 0xFFFED504, 0x61A8, 0x0)
    OP_98(0x0, 0xA)
    OP_98(0x1, 0xFFFF623A, 0xFFFFB1E0, 0xFFFF89F4)
    OP_98(0x1, 0xFFFF6DF2, 0x276, 0xFFFFE00C)
    OP_98(0x1, 0xFFFF89D6, 0xC968, 0xBA5E)
    OP_98(0x2, 0xA, 0xD6D8, 0x6)
    OP_71(0x2, 0x4)
    Return()

    # Function_52_5626 end

    def Function_53_56B4(): pass

    label("Function_53_56B4")

    OP_8F(0xFE, 0xFFFFC568, 0xFFFEEE90, 0xFFFEF660, 0x4E20, 0x0)

    def lambda_56CE():
        OP_D1(254, -20000, 220000, 20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_56CE)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFE1BA0, 0x7530, 0xFFFDA288)
    OP_98(0x1, 0xFFFD67F0, 0x12110, 0xFFFC9118)

    def lambda_5708():
        OP_98(0x2, 0xFE, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_5708)
    Sleep(2000)

    def lambda_571D():
        OP_D1(254, -20000, 210000, -20000, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_571D)
    WaitChrThread(0xFE, 0x0)
    OP_71(0x2, 0x4)
    Return()

    # Function_53_56B4 end

    def Function_54_573C(): pass

    label("Function_54_573C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_57B6"),
        (1, "loc_57BC"),
        (SWITCH_DEFAULT, "loc_57C2"),
    )


    label("loc_57B6")

    OP_A2(0x1200)
    Jump("loc_57C2")

    label("loc_57BC")

    OP_A2(0x1201)
    Jump("loc_57C2")

    label("loc_57C2")

    Return()

    # Function_54_573C end

    SaveToFile()

Try(main)

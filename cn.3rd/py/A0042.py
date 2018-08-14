from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0042   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '03940露菲娜',                          # 9
        '03950奥斯本',                          # 10
        '03960科洛蒂娅',                        # 11
        '03980提妲母亲',                        # 12
        '03970提妲父亲',                        # 13
        '03990礼服的尤莉亚',                    # 14
        '03420护卫',                            # 15
        '03430持枪黑猎兵',                      # 16
        '03440黑骑士莱维',                      # 17
        '02650主办者',                          # 18
        '02670前辈１雷克特',                    # 19
        '02680前辈２雷欧',                      # 20
        '02690前辈３露希',                      # 21
        '02700前辈４利格尔',                    # 22
        '02710爱娜１８岁',                      # 23
        '02720朵洛希１５岁',                    # 24
        '02730伊莉莎１１岁',                    # 25
        '02740缇欧１１岁',                      # 26
        '02750约修亚１１岁',                    # 27
        '02560爱娜',                            # 28
        '02070朵洛希',                          # 29
        '03460护卫',                            # 30
        '02660宾客艾基斯托拉①',                # 31
        '02840宾客艾基斯托拉②',                # 32
        '02850宾客艾基斯托拉③',                # 33
        '02860宾客艾基斯托拉④',                # 34
        '02870宾客艾基斯托拉⑤',                # 35
        '',                                     # 36
    )

    DeclEntryPoint(
        Unknown_00              = 2000,
        Unknown_04              = 0,
        Unknown_08              = 2000,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
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
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03940 ._CH',             # 00
        'ED6_DT27/CH03950 ._CH',             # 01
        'ED6_DT27/CH03960 ._CH',             # 02
        'ED6_DT27/CH03970 ._CH',             # 03
        'ED6_DT27/CH03980 ._CH',             # 04
        'ED6_DT27/CH03990 ._CH',             # 05
        'ED6_DT27/CH03420 ._CH',             # 06
        'ED6_DT27/CH03430 ._CH',             # 07
        'ED6_DT27/CH03440 ._CH',             # 08
        'ED6_DT07/CH02650 ._CH',             # 09
        'ED6_DT07/CH02660 ._CH',             # 0A
        'ED6_DT07/CH02670 ._CH',             # 0B
        'ED6_DT07/CH02680 ._CH',             # 0C
        'ED6_DT07/CH02690 ._CH',             # 0D
        'ED6_DT07/CH02700 ._CH',             # 0E
        'ED6_DT07/CH02710 ._CH',             # 0F
        'ED6_DT07/CH02720 ._CH',             # 10
        'ED6_DT07/CH02730 ._CH',             # 11
        'ED6_DT07/CH02740 ._CH',             # 12
        'ED6_DT07/CH02750 ._CH',             # 13
        'ED6_DT07/CH02560 ._CH',             # 14
        'ED6_DT07/CH02070 ._CH',             # 15
        'ED6_DT27/CH03460 ._CH',             # 16
        'ED6_DT07/CH02840 ._CH',             # 17
        'ED6_DT07/CH02850 ._CH',             # 18
        'ED6_DT07/CH02860 ._CH',             # 19
        'ED6_DT07/CH02870 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT27/CH03940P._CP',             # 00
        'ED6_DT27/CH03950P._CP',             # 01
        'ED6_DT27/CH03960P._CP',             # 02
        'ED6_DT27/CH03970P._CP',             # 03
        'ED6_DT27/CH03980P._CP',             # 04
        'ED6_DT27/CH03990P._CP',             # 05
        'ED6_DT27/CH03420P._CP',             # 06
        'ED6_DT27/CH03430P._CP',             # 07
        'ED6_DT27/CH03440P._CP',             # 08
        'ED6_DT07/CH02650P._CP',             # 09
        'ED6_DT07/CH02660P._CP',             # 0A
        'ED6_DT07/CH02670P._CP',             # 0B
        'ED6_DT07/CH02680P._CP',             # 0C
        'ED6_DT07/CH02690P._CP',             # 0D
        'ED6_DT07/CH02700P._CP',             # 0E
        'ED6_DT07/CH02710P._CP',             # 0F
        'ED6_DT07/CH02720P._CP',             # 10
        'ED6_DT07/CH02730P._CP',             # 11
        'ED6_DT07/CH02740P._CP',             # 12
        'ED6_DT07/CH02750P._CP',             # 13
        'ED6_DT07/CH02560P._CP',             # 14
        'ED6_DT07/CH02070P._CP',             # 15
        'ED6_DT27/CH03460P._CP',             # 16
        'ED6_DT07/CH02840P._CP',             # 17
        'ED6_DT07/CH02850P._CP',             # 18
        'ED6_DT07/CH02860P._CP',             # 19
        'ED6_DT07/CH02870P._CP',             # 1A
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )


    ScpFunction(
        "Function_0_4E2",          # 00, 0
        "Function_1_4E3",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_507",          # 03, 3
        "Function_4_5AE",          # 04, 4
        "Function_5_5C7",          # 05, 5
        "Function_6_5E0",          # 06, 6
        "Function_7_5F9",          # 07, 7
        "Function_8_612",          # 08, 8
        "Function_9_62B",          # 09, 9
        "Function_10_644",         # 0A, 10
        "Function_11_65D",         # 0B, 11
        "Function_12_676",         # 0C, 12
        "Function_13_68F",         # 0D, 13
        "Function_14_6A8",         # 0E, 14
        "Function_15_6C1",         # 0F, 15
        "Function_16_6DA",         # 10, 16
        "Function_17_6F3",         # 11, 17
        "Function_18_70C",         # 12, 18
        "Function_19_725",         # 13, 19
        "Function_20_73E",         # 14, 20
        "Function_21_757",         # 15, 21
        "Function_22_770",         # 16, 22
        "Function_23_789",         # 17, 23
        "Function_24_7A2",         # 18, 24
        "Function_25_7C0",         # 19, 25
        "Function_26_7DE",         # 1A, 26
        "Function_27_7F7",         # 1B, 27
        "Function_28_810",         # 1C, 28
        "Function_29_829",         # 1D, 29
    )


    def Function_0_4E2(): pass

    label("Function_0_4E2")

    Return()

    # Function_0_4E2 end

    def Function_1_4E3(): pass

    label("Function_1_4E3")

    Return()

    # Function_1_4E3 end

    def Function_2_4E4(): pass

    label("Function_2_4E4")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "你好。\x02",
    )

    Jump("loc_4FD")

    label("loc_4FD")

    CloseMessageWindow()
    OP_AE(0x5DC)
    TalkEnd(0xFE)
    Return()

    # Function_2_4E4 end

    def Function_3_507(): pass

    label("Function_3_507")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_538"),
        (1, "loc_544"),
        (2, "loc_550"),
        (3, "loc_55C"),
        (4, "loc_568"),
        (5, "loc_574"),
        (6, "loc_580"),
        (SWITCH_DEFAULT, "loc_58C"),
    )


    label("loc_538")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_598")

    label("loc_544")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_598")

    label("loc_550")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_598")

    label("loc_55C")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_598")

    label("loc_568")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_598")

    label("loc_574")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_598")

    label("loc_580")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_598")

    label("loc_58C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_598")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_598")

    label("loc_5AD")

    Return()

    # Function_3_507 end

    def Function_4_5AE(): pass

    label("Function_4_5AE")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1470F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_5AE end

    def Function_5_5C7(): pass

    label("Function_5_5C7")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "#1480F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5C7 end

    def Function_6_5E0(): pass

    label("Function_6_5E0")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0xFE,
        "#1810F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_5E0 end

    def Function_7_5F9(): pass

    label("Function_7_5F9")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0xFE,
        "#1450F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_5F9 end

    def Function_8_612(): pass

    label("Function_8_612")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#1460F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_612 end

    def Function_9_62B(): pass

    label("Function_9_62B")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        "#1490F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_62B end

    def Function_10_644(): pass

    label("Function_10_644")

    TalkBegin(0xFE)

    ChrTalk(    #7
        0xFE,
        "普通\x02",
    )

    Jump("loc_658")

    label("loc_658")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_644 end

    def Function_11_65D(): pass

    label("Function_11_65D")

    TalkBegin(0xFE)

    ChrTalk(    #8
        0xFE,
        "普通\x02",
    )

    Jump("loc_671")

    label("loc_671")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_65D end

    def Function_12_676(): pass

    label("Function_12_676")

    TalkBegin(0xFE)

    ChrTalk(    #9
        0xFE,
        "#1590F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_676 end

    def Function_13_68F(): pass

    label("Function_13_68F")

    TalkBegin(0xFE)

    ChrTalk(    #10
        0xFE,
        "普通\x02",
    )

    Jump("loc_6A3")

    label("loc_6A3")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_68F end

    def Function_14_6A8(): pass

    label("Function_14_6A8")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0xFE,
        "普通\x02",
    )

    Jump("loc_6BC")

    label("loc_6BC")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_6A8 end

    def Function_15_6C1(): pass

    label("Function_15_6C1")

    TalkBegin(0xFE)

    ChrTalk(    #12
        0xFE,
        "#1770F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_6C1 end

    def Function_16_6DA(): pass

    label("Function_16_6DA")

    TalkBegin(0xFE)

    ChrTalk(    #13
        0xFE,
        "#1780F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_6DA end

    def Function_17_6F3(): pass

    label("Function_17_6F3")

    TalkBegin(0xFE)

    ChrTalk(    #14
        0xFE,
        "#1790F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_6F3 end

    def Function_18_70C(): pass

    label("Function_18_70C")

    TalkBegin(0xFE)

    ChrTalk(    #15
        0xFE,
        "普通\x02",
    )

    Jump("loc_720")

    label("loc_720")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_70C end

    def Function_19_725(): pass

    label("Function_19_725")

    TalkBegin(0xFE)

    ChrTalk(    #16
        0xFE,
        "#1650F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_725 end

    def Function_20_73E(): pass

    label("Function_20_73E")

    TalkBegin(0xFE)

    ChrTalk(    #17
        0xFE,
        "#1660F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_73E end

    def Function_21_757(): pass

    label("Function_21_757")

    TalkBegin(0xFE)

    ChrTalk(    #18
        0xFE,
        "#1690F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_757 end

    def Function_22_770(): pass

    label("Function_22_770")

    TalkBegin(0xFE)

    ChrTalk(    #19
        0xFE,
        "#1680F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_770 end

    def Function_23_789(): pass

    label("Function_23_789")

    TalkBegin(0xFE)

    ChrTalk(    #20
        0xFE,
        "#1670F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_789 end

    def Function_24_7A2(): pass

    label("Function_24_7A2")

    TalkBegin(0xFE)

    ChrTalk(    #21
        0xFE,
        "#410F普通\x02",
    )

    Jump("loc_7BB")

    label("loc_7BB")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_7A2 end

    def Function_25_7C0(): pass

    label("Function_25_7C0")

    TalkBegin(0xFE)

    ChrTalk(    #22
        0xFE,
        "#150F普通\x02",
    )

    Jump("loc_7D9")

    label("loc_7D9")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_7C0 end

    def Function_26_7DE(): pass

    label("Function_26_7DE")

    TalkBegin(0xFE)

    ChrTalk(    #23
        0xFE,
        "普通\x02",
    )

    Jump("loc_7F2")

    label("loc_7F2")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_7DE end

    def Function_27_7F7(): pass

    label("Function_27_7F7")

    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        "普通\x02",
    )

    Jump("loc_80B")

    label("loc_80B")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_7F7 end

    def Function_28_810(): pass

    label("Function_28_810")

    TalkBegin(0xFE)

    ChrTalk(    #25
        0xFE,
        "普通\x02",
    )

    Jump("loc_824")

    label("loc_824")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_810 end

    def Function_29_829(): pass

    label("Function_29_829")

    TalkBegin(0xFE)

    ChrTalk(    #26
        0xFE,
        "普通\x02",
    )

    Jump("loc_83D")

    label("loc_83D")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_829 end

    SaveToFile()

Try(main)

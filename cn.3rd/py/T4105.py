from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '朵洛希',                               # 9
        '奈尔',                                 # 10
        '希德中校',                             # 11
        '菲丝',                                 # 12
        '卡鲁尼洛',                             # 13
        '蒂法露',                               # 14
        '修理员佩顿',                           # 15
        '村中的老年男性',                       # 16
        '乘客街上的绅士',                       # 17
        '村中的中年男性',                       # 18
        '村中的中年女性',                       # 19
        '村中的老年女性',                       # 20
        '村中的青年女性',                       # 21
        '乘客女学生',                           # 22
        '乘客贵族女孩',                         # 23
        '乘客贵族老人',                         # 24
        '乘客街上的绅士',                       # 25
        '乘客街上的淑女',                       # 26
        '乘客街上的女青年',                     # 27
        '奥利维特皇子',                         # 28
        '穆拉少校',                             # 29
        '科洛蒂娅公主',                         # 30
        '卡西乌斯准将',                         # 31
        '奥斯本宰相',                           # 32
        '雷克特书记官',                         # 33
        '尤莉亚上尉',                           # 34
        '雪拉扎德',                             # 35
        '目标用照相机',                         # 36
        '格雷特纳号',                           # 37
        '格雷特纳号的影子',                     # 38
        '王都格兰赛尔·东街区',                 # 39
        '',                                     # 40
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01450 ._CH',             # 03
        'ED6_DT07/CH01550 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01480 ._CH',             # 0C
        'ED6_DT07/CH01490 ._CH',             # 0D
        'ED6_DT07/CH01200 ._CH',             # 0E
        'ED6_DT07/CH01230 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT27/CH03590 ._CH',             # 11
        'ED6_DT27/CH03260 ._CH',             # 12
        'ED6_DT27/CH03570 ._CH',             # 13
        'ED6_DT27/CH03210 ._CH',             # 14
        'ED6_DT27/CH03670 ._CH',             # 15
        'ED6_DT07/CH02090 ._CH',             # 16
        'ED6_DT27/CH03950 ._CH',             # 17
        'ED6_DT26/CH20805 ._CH',             # 18
        'ED6_DT07/CH00020 ._CH',             # 19
        'ED6_DT26/CH20808 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01450P._CP',             # 03
        'ED6_DT07/CH01550P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01480P._CP',             # 0C
        'ED6_DT07/CH01490P._CP',             # 0D
        'ED6_DT07/CH01200P._CP',             # 0E
        'ED6_DT07/CH01230P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT27/CH03590P._CP',             # 11
        'ED6_DT27/CH03260P._CP',             # 12
        'ED6_DT27/CH03570P._CP',             # 13
        'ED6_DT27/CH03210P._CP',             # 14
        'ED6_DT27/CH03670P._CP',             # 15
        'ED6_DT07/CH02090P._CP',             # 16
        'ED6_DT27/CH03950P._CP',             # 17
        'ED6_DT26/CH20805P._CP',             # 18
        'ED6_DT07/CH00020P._CP',             # 19
        'ED6_DT26/CH20808P._CP',             # 1A
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67350,
        Z                   = 0,
        Y                   = 145020,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67340,
        Z                   = 0,
        Y                   = 146190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = -10000,
        Y                   = 163540,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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
        "Function_0_562",          # 00, 0
        "Function_1_5A7",          # 01, 1
        "Function_2_5E2",          # 02, 2
        "Function_3_5F8",          # 03, 3
        "Function_4_2273",         # 04, 4
        "Function_5_22F5",         # 05, 5
        "Function_6_2386",         # 06, 6
        "Function_7_23FC",         # 07, 7
        "Function_8_2446",         # 08, 8
        "Function_9_2482",         # 09, 9
        "Function_10_24D1",        # 0A, 10
        "Function_11_24FF",        # 0B, 11
        "Function_12_2575",        # 0C, 12
        "Function_13_25EB",        # 0D, 13
        "Function_14_3A50",        # 0E, 14
        "Function_15_3A96",        # 0F, 15
        "Function_16_3B12",        # 10, 16
        "Function_17_3B82",        # 11, 17
        "Function_18_3BE8",        # 12, 18
        "Function_19_3C75",        # 13, 19
        "Function_20_3CB8",        # 14, 20
    )


    def Function_0_562(): pass

    label("Function_0_562")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_58A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5A6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_5A6")

    Return()

    # Function_0_562 end

    def Function_1_5A7(): pass

    label("Function_1_5A7")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D1")
    OP_B1("t4105_7")
    Jump("loc_5DA")

    label("loc_5D1")

    OP_B1("t4105_3")

    label("loc_5DA")

    OP_82(0x81, 0x0)
    OP_64(0x0, 0x1)
    Return()

    # Function_1_5A7 end

    def Function_2_5E2(): pass

    label("Function_2_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5E2")

    label("loc_5F7")

    Return()

    # Function_2_5E2 end

    def Function_3_5F8(): pass

    label("Function_3_5F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x2000000)
    OP_1D(0xE)
    SetChrFlags(0x109, 0x80)
    OP_82(0x81, 0x0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_6F(0xA, 161)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x20, 62500, -3000, 165990, 90)
    SetChrPos(0x21, 62320, -3000, 166860, 90)
    SetChrPos(0x22, 56810, 250, 137480, 90)
    SetChrPos(0x2C, 87000, 5500, 130500, 90)
    SetChrPos(0x2D, 87000, -1100, 130500, 90)
    OP_A1(0x2D, 0xB)
    OP_A1(0x2C, 0xA)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_71(0x80A, 0x0)
    ExitThread()
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    OP_48()
    OP_6D(88320, 1550, 192380, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(212000, 0)
    OP_6E(448, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x0, 0x829D8, 0x0)

    def lambda_728():
        OP_6D(91660, 1550, 130380, 9000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_728)

    def lambda_740():
        OP_67(0, 6060, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_740)

    def lambda_758():
        OP_6B(6820, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_758)

    def lambda_768():
        OP_6C(308000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_768)

    def lambda_778():
        OP_6E(310, 9000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_778)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_792():
        OP_8F(0xFE, 0x153D8, 0xFFFFE9EE, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_792)

    def lambda_7AD():
        OP_8F(0xFE, 0x153D8, 0xFFFFEC14, 0x1FDC4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7AD)
    Sleep(2000)
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_D8(0xA, 0x1F4)
    OP_6F(0xA, 261)
    OP_70(0xA, 0x19A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x2C, 0x0)
    WaitChrThread(0x2D, 0x0)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(100)
    Fade(500)
    OP_6D(86890, -650, 129970, 0)
    OP_67(0, 9270, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(134000, 0)
    OP_6E(230, 0)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x3C)
    OP_0D()
    Sleep(100)
    OP_22(0x76, 0x0, 0x64)
    OP_71(0x864, 0x0)
    ExitThread()
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_71(0x805, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    Sleep(300)
    OP_48()
    StopSound(0xEA60, 0x29810, 0x32C8)

    def lambda_8D0():
        OP_6D(87200, 750, 129500, 13000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8D0)

    def lambda_8E8():
        OP_67(0, 6610, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E8)

    def lambda_900():
        OP_6B(3770, 13000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_900)

    def lambda_910():
        OP_6C(135000, 13000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_910)

    def lambda_920():
        OP_6E(260, 13000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_920)
    OP_43(0x17, 0x0, 0x0, 0x6)
    OP_43(0x1F, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x1B, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x18, 0x0, 0x0, 0xB)
    OP_43(0x1D, 0x0, 0x0, 0x6)
    Sleep(1000)
    Sleep(700)
    Sleep(1000)
    OP_43(0x1C, 0x0, 0x0, 0x7)
    Sleep(5000)
    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(7000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x11, 0x3)
    OP_44(0x10, 0x0)
    Fade(1000)
    OP_6D(83460, 1500, 142720, 0)
    OP_67(0, 5180, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(320, 0)
    OP_44(0x11, 0x0)

    def lambda_A08():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A08)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #0
        0x10,
        (
            "#151F#2P啊～真是令人怀念呢。\x02\x03",

            "虽然共和国也很美好，\x01",
            "不过最舒服的果然\x01",
            "还是利贝尔的气息啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1060F#6P半年前明明\x01",
            "发生过那样的巨变，\x01",
            "如今城镇风貌已经一如往常。\x02\x03",

            "这么和平稳定的国家\x01",
            "也有与之相应的骨气呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#157F#2P呵呵，不管怎么说\x01",
            "都是因为女王治国有方呢。\x02\x03",

            "#150F女性在逆境中会更加坚强哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1066F#6P这、这话由朵洛希你说出来\x01",
            "总感觉说服力似有似无啊……\x02\x03",

            "#1075F不过，已经半年没来了，\x01",
            "这个国家的空气的确还是那样怡人呢。\x02\x03",

            "#1060F……我从心底感觉到\x01",
            "一种莫名的怀念。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#150F#2P凯文先生的故乡\x01",
            "是在一个叫亚尔特利亚的地方吧～？\x02\x03",

            "听说那里到处都是\x01",
            "巨大的教会建筑啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1060F#6P啊……我并不是\x01",
            "亚尔特利亚出身。\x02\x03",

            "亚尔特利亚法典国\x01",
            "是七耀教会的总部所在。\x02\x03",

            "虽然大量的信徒和教会相关人士\x01",
            "从整个大陆聚集而来,\x01",
            "但当地出身的人却很少。\x02\x03",

            "虽说是个国家，\x01",
            "但面积却远远小于附近的自治州。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#151F#2P啊～原来是这样啊。\x02\x03",

            "#153F咦，那么\x01",
            "凯文先生的故乡到底是……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 75890, 0, 143270, 90)

    NpcTalk(    #7
        0x11,
        "男人的声音",
        "#1P朵～洛～希～……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x11, 69890, 0, 143270, 90)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    def lambda_E8C():
        OP_6D(78880, 1500, 141980, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E8C)

    def lambda_EA4():
        OP_67(0, 4760, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EA4)

    def lambda_EBC():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EBC)

    def lambda_ECC():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_ECC)

    def lambda_EDC():
        OP_6E(327, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_EDC)

    def lambda_EEC():
        OP_8E(0xFE, 0x134E8, 0x5DC, 0x22EA2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_EEC)
    OP_8C(0x109, 270, 400)
    Sleep(200)
    OP_8C(0x10, 270, 400)
    Sleep(500)
    OP_8E(0x10, 0x13BDC, 0x5DC, 0x22F2E, 0x3E8, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #8
        0x10,
        (
            "#153F#6P啊～奈尔前辈！\x02\x03",

            "#151F朵洛希·海娅特，\x01",
            "顺利归来复命～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "#147F#2P顺利归来复命～\x02\x01",

            "#144F才怪！！\x02\x03",

            "你这家伙……\x01",
            "明明让你去柏斯取材，\x01",
            "怎么变成共和国了！？\x02\x03",

            "那时你到底是不是乘坐的\x01",
            "向西行的定期船！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#154F#6P唔～嗯。\x01",
            "是怎么回事呢～？\x02\x03",

            "#153F啊，难道说……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x11,
        "#142F#2P难道说……什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#155F#6P难道说我……\x01",
            "有梦游的症状吗。\x02\x03",

            "睡着的时候，\x01",
            "在无意识中换乘了定期船……\x02\x03",

            "然后被什么人利用，\x01",
            "当作杀人事件的诡秘手法……\x02\x03",

            "#151F紧张刺激……\x01",
            "充满了惊奇悬疑的气氛呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #13
        0x11,
        (
            "#144F#2P#3S就算再怎么梦游，\x01",
            "也不可能换掉正在乘坐的定期船吧！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #14
        0x11,
        (
            "#145F#2P#2S#40W呼呼呼……\x01",
            "#40W呜，喘不过气来了 ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#154F#6P没、没关系吧～？\x02\x03",

            "前辈已经老大不小了，\x01",
            "不控制吸烟量的话是不行的～\x02\x03",

            "#150F对了，上周星期五\x01",
            "是您３０岁生日呢～\x02\x03",

            "#151F生日快乐～\x01",
            "我在旅行的时候\x01",
            "特地买了大蛋糕来庆祝哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#145F#2P这种小事\x01",
            "就算不记得也无所谓！\x02\x03",

            "#142F再说，\x01",
            "你只不过是自己\x01",
            "想吃蛋糕而已吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#151F#6P呵呵，那是用东方的\x01",
            "抹茶制成的蛋糕～\x02\x03",

            "甜美中交织着淡淡的苦味，\x01",
            "简直是绝妙的口感啊～\x02\x03",

            "#150F我把蛋糕的每个角度都拍下来了，\x01",
            "待会儿就洗出来给你看吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#144F#2P#3S只有照片吗！？\x01",
            "好歹也应该买些礼物吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x109,
        (
            "#1068F#6P（怎、怎么回事……）\x02\x03",

            "（总觉得这相声说得\x01",
            "  比之前更加炉火纯青了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #20
        0x11,
        "#143F#2P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_151F():
        OP_6D(78920, 1500, 142630, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_151F)

    def lambda_1537():
        OP_67(0, 5000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1537)

    def lambda_154F():
        OP_8E(0xFE, 0x13C68, 0x5DC, 0x23424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_154F)
    OP_8C(0x10, 0, 400)
    OP_8C(0x11, 45, 400)
    WaitChrThread(0x109, 0x2)
    OP_8C(0x109, 225, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #21
        0x109,
        (
            "#1066F#6P哈哈……\x01",
            "奈尔先生，久违了。\x02\x03",

            "看到你还是老样子真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#144F#5P凯文·格拉汉姆！？\x01",
            "为什么你会在这里……\x02\x03",

            "难、难道说朵洛希这家伙\x01",
            "还跑到了亚尔特利亚那里去\x01",
            "做了什么乱七八糟的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1061F#6P哈哈，不是的。\x02\x03",

            "#1062F只是碰巧乘上了\x01",
            "同一艘国际定期船而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#143F#5P这、这样啊，那我就安心了。\x02\x03",

            "#145F……我刚才一瞬间还以为\x01",
            "那家伙又犯傻把大圣堂的\x01",
            "彩绘玻璃给打得粉碎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1068F#6P奈尔先生……　\x01",
            "……你真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #26
        0x10,
        (
            "#151F#6P呵呵，前辈你\x01",
            "总是这么爱操心～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#145F#5P你、你还好意思……\x02\x03",

            "#141F不过……\x01",
            "自那以来已经过了半年。\x02\x03",

            "你这次是为了什么来利贝尔的？\x01",
            "又有什么情况了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#6P啊，不过是些琐碎小事罢了。\x02\x03",

            "并非有什么特别的事件，\x01",
            "所以也就不用期待了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#147F#5P嘿嘿……\x01",
            "这可不见得哦。\x02\x03",

            "#141F算了，反正你也会暂时\x01",
            "留在格兰赛尔大圣堂吧？\x02\x03",

            "隔几天我再来问候你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1066F#6P哈哈……还请手下留情。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #31
        0x11,
        (
            "#144F#2P朵洛希！\x01",
            "要回编辑部了！\x02\x03",

            "把这两周你的所作所为\x01",
            "清清楚楚明明白白地说出来！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x10,
        (
            "#151F#6P嘿嘿，\x01",
            "没问题～\x02\x03",

            "每顿饭我都照了相的，\x01",
            "只要照片洗出来我就会全部记起来的～\x02",
        )
    )

    Jump("loc_1A4F")

    label("loc_1A4F")

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#145F#2P不是叫你\x01",
            "报告饮食情况！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A82():

        label("loc_1A82")

        TurnDirection(0x109, 0x11, 0)
        OP_48()
        Jump("loc_1A82")

    QueueWorkItem2(0x109, 3, lambda_1A82)
    OP_8C(0x11, 270, 400)
    Sleep(100)

    def lambda_1A9F():
        OP_6D(77110, 1500, 143410, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A9F)

    def lambda_1AB7():
        OP_67(0, 4760, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AB7)

    def lambda_1ACF():
        OP_8E(0xFE, 0xF5AA, 0x0, 0x22E2A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1ACF)
    Sleep(500)

    def lambda_1AEF():
        OP_8E(0xFE, 0xFA00, 0x0, 0x22E2A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AEF)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_44(0x109, 0x3)
    Sleep(500)

    def lambda_1B27():
        OP_6D(78920, 1500, 142630, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B27)

    def lambda_1B3F():
        OP_67(0, 5020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B3F)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #34
        0x109,
        (
            "#1068F#5P呼～看到那两个人，\x01",
            "真是切身感受到\x01",
            "自己又踏上了利贝尔的土地啊。\x02\x03",

            "#1060F话说回来，\x01",
            "其他人都在做些什么呢……\x02\x03",

            "艾丝蒂尔和约修亚\x01",
            "那两个人好像去了外国……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62480, 0, 142870, 90)

    NpcTalk(    #35
        0x12,
        "男性的声音",
        "#1P格拉汉姆神父……\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1C8D():
        OP_6D(74460, 1500, 142940, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1C8D)

    def lambda_1CA5():
        OP_67(0, 4300, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1CA5)

    def lambda_1CBD():
        OP_8E(0xFE, 0x104F0, 0x0, 0x22E34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1CBD)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #36
        0x109,
        "#1064F#2P希德中校……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1D0D():
        OP_6D(74110, 1500, 142270, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1D0D)

    def lambda_1D25():
        OP_67(0, 5410, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D25)

    def lambda_1D3D():
        OP_6B(2420, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1D3D)

    def lambda_1D4D():
        OP_8E(0xFE, 0x122F0, 0x5DC, 0x23064, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1D4D)
    Sleep(400)

    def lambda_1D6D():
        OP_8E(0xFE, 0x12A5C, 0x5DC, 0x23122, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D6D)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #37
        0x12,
        (
            "#701F#2P哈哈，好久不见。\x02\x03",

            "上次见面还是在那次事件后的宴会吧……\x01",
            "很高兴看到你还是这么有精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        (
            "#1060F#6P中校你也还是老样子，\x01",
            "这就让我放心了。\x02\x03",

            "不过，当我听说王国军\x01",
            "也会参与这次行动的时候……\x02\x03",

            "我还以为来的人\x01",
            "一定会是尤莉亚小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x12,
        (
            "#701F#2P舒华兹上尉现在正在\x01",
            "执行其它的任务。\x02\x03",

            "所以才让我这个闲人\x01",
            "前来接待你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        (
            "#1061F#6P哎呀～你太客气了。\x02\x03",

            "#1062F听传闻说，\x01",
            "你最近是要晋升上校了吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x12,
        (
            "#703F#2P呵呵，虽然已经事到如今，\x01",
            "但你们的情报网却还是让我感到很惊讶啊……\x02\x03",

            "#701F不过，那对现在的我来说\x01",
            "实在是有些过重的职位。\x02\x03",

            "而且，我也希望卡西乌斯准将\x01",
            "能够继续为军队再尽一些力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1066F#6P呵呵，卡西乌斯先生也很辛苦啊。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #43
        0x109,
        (
            "#1063F#6P对了……\x01",
            "那件东西在大圣堂吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x12,
        (
            "#703F#2P嗯……\x01",
            "正保管在地下。\x02\x03",

            "#700F我听说外部人员如果想要进入，\x01",
            "必须要有骑士团的许可吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1060F#6P嗯，这倒是。\x01",
            "因为那里稍微有些特殊。\x02\x03",

            "具体情况\x01",
            "就等到了再说吧。\x02",
        )
    )

    Jump("loc_2170")

    label("loc_2170")

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#703F#2P……明白了。\x02\x03",

            "#701F我正好要为你引荐一个人，\x01",
            "我们这就前往大圣堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1064F#6P咦……引荐一个人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x12,
        (
            "#701F#2P呵呵……\x01",
            "是此次事件的协助者。\x02\x03",

            "详细情况\x01",
            "就向此人咨询吧。\x02",
        )
    )

    Jump("loc_2256")

    label("loc_2256")

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5F8 end

    def Function_4_2273(): pass

    label("Function_4_2273")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0x143E8, 0x60E, 0x209B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142C6, 0x5DC, 0x233F2, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_2273 end

    def Function_5_22F5(): pass

    label("Function_5_22F5")

    Sleep(1500)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8E(0xFE, 0x143E8, 0x60E, 0x209B8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x142DA, 0x5DC, 0x22EA2, 0x7D0, 0x0)
    Return()

    # Function_5_22F5 end

    def Function_6_2386(): pass

    label("Function_6_2386")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14244, 0x60E, 0x207C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14244, 0x5DC, 0x22EB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1095A, 0x0, 0x22EB6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_2386 end

    def Function_7_23FC(): pass

    label("Function_7_23FC")

    OP_43(0x1C, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x1E, 0x1, 0x0, 0x9)
    WaitChrThread(0x1C, 0x1)
    WaitChrThread(0x1E, 0x1)
    Sleep(300)
    OP_43(0x1C, 0x1, 0x0, 0xA)
    Sleep(300)
    OP_8E(0x1E, 0x14316, 0x60E, 0x2076A, 0x7D0, 0x0)
    OP_43(0x1E, 0x1, 0x0, 0xA)
    Return()

    # Function_7_23FC end

    def Function_8_2446(): pass

    label("Function_8_2446")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x144D8, 0x60E, 0x1FDC4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_2446 end

    def Function_9_2482(): pass

    label("Function_9_2482")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14988, 0x60E, 0x1FDCD, 0xBB8, 0x0)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Return()

    # Function_9_2482 end

    def Function_10_24D1(): pass

    label("Function_10_24D1")

    OP_8E(0xFE, 0x14438, 0x5DC, 0x22EF2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x109BE, 0x0, 0x22FB0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_24D1 end

    def Function_11_24FF(): pass

    label("Function_11_24FF")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 93860, 1650, 131620, 0)
    OP_8E(0xFE, 0x16EA4, 0x672, 0x20814, 0x7D0, 0x0)
    OP_8E(0xFE, 0x145E6, 0x60E, 0x2083C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x145E6, 0x5DC, 0x231A4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10892, 0x0, 0x231A4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_24FF end

    def Function_12_2575(): pass

    label("Function_12_2575")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 90830, 1550, 127810, 0)
    OP_8E(0xFE, 0x14D16, 0x60E, 0x1F342, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x60E, 0x1FDA6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x5DC, 0x22DDA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1095A, 0x0, 0x22EB6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_2575 end

    def Function_13_25EB(): pass

    label("Function_13_25EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_A1(0x2C, 0xA)
    SetChrPos(0x2C, 87000, -5650, 130500, 90)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_A1(0x2D, 0xB)
    SetChrPos(0x2D, 87000, -5100, 130500, 90)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x409, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_6F(0xA, 60)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x20, 82820, 1500, 143000, 180)
    SetChrPos(0x21, 81500, 1500, 143000, 270)
    SetChrPos(0x22, 80600, 1500, 143000, 90)
    SetChrPos(0x27, 79280, 1500, 143000, 90)
    SetChrPos(0x28, 78180, 1500, 143000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_11(0xDC, 0xF0, 0xC8, 0xEA60, 0x41EB0, 0x0)
    OP_6D(82000, 1500, 142420, 0)
    OP_67(0, 10640, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(30000, 0)
    OP_6E(590, 0)

    def lambda_272D():
        OP_67(0, 8640, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_272D)

    def lambda_2745():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_2745)

    def lambda_2755():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_2755)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x2B, 0x0)
    Fade(1000)
    OP_6D(82600, 1500, 140480, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(3860, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #49
        "\x07\x05……各位乘客，久等了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("女性的声音")

    AnonymousTalk(    #50
        (
            "\x07\x05前往雷米菲利亚公国的\x01",
            "国际定期船『卡拉布里亚号』\x01",
            "出航准备已经完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("女性的声音")

    AnonymousTalk(    #51
        (
            "\x07\x05请各位注意脚下安全，\x01",
            "依次上船。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x76, 0x0, 0x64)
    OP_71(0x80A, 0x0)
    ExitThread()
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_71(0x805, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_43(0x20, 0x3, 0x0, 0xE)
    OP_43(0x21, 0x3, 0x0, 0xF)
    OP_43(0x22, 0x3, 0x0, 0x10)
    Sleep(3000)

    def lambda_2921():
        OP_6D(85600, 1500, 140480, 2000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_2921)

    def lambda_2939():
        OP_8E(0xFE, 0x143D4, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_2939)
    Sleep(300)

    def lambda_2959():
        OP_8E(0xFE, 0x13E70, 0x5DC, 0x22E34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_2959)
    WaitChrThread(0x27, 0x1)
    Sleep(300)
    OP_8C(0x27, 0, 400)

    def lambda_2985():
        OP_8C(0x28, 0, 400)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_2985)
    Sleep(500)
    SetChrChipByIndex(0x27, 26)
    SetChrSubChip(0x27, 0)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x27, 0x0, 0x5, 0x3E8)
    Sleep(500)
    OP_99(0x27, 0x6, 0x7, 0x3E8)
    SetChrChipByIndex(0x27, 23)
    SetChrSubChip(0x27, 0)
    Sleep(500)
    OP_8C(0x27, 180, 400)
    Sleep(300)

    def lambda_29D9():
        OP_6D(86500, 1500, 133000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_29D9)

    def lambda_29F1():
        OP_67(0, 4500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_29F1)
    OP_43(0x27, 0x3, 0x0, 0x11)
    Sleep(50)
    OP_43(0x28, 0x3, 0x0, 0x12)
    WaitChrThread(0x27, 0x3)
    WaitChrThread(0x28, 0x3)
    OP_6F(0xA, 450)
    OP_70(0xA, 0x19B)
    Sleep(400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(450)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    Sleep(300)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0x5, 0x32)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1300)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xA, 0x1E)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x3C)
    OP_73(0xA)
    Sleep(500)
    OP_23(0x75)
    Fade(1000)
    OP_6D(85600, 1500, 131100, 0)
    OP_67(0, 12800, -10000, 0)
    OP_6B(4160, 0)
    OP_6C(135000, 0)
    OP_6E(314, 0)
    Sleep(500)

    def lambda_2ADF():
        OP_8F(0xFE, 0x153D8, 0xFFFFEDD6, 0x1FDC4, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_2ADF)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0xA, 61)
    OP_70(0xA, 0xA0)
    OP_73(0xA)
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    WaitChrThread(0x2C, 0x0)

    def lambda_2B29():
        OP_6D(113780, 3500, 131100, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_2B29)

    def lambda_2B41():
        OP_67(0, 9800, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_2B41)

    def lambda_2B59():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_2B59)

    def lambda_2B69():
        OP_6B(4460, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_2B69)

    def lambda_2B79():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2B79)

    def lambda_2B94():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2B94)
    Sleep(200)

    def lambda_2BB4():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2BB4)

    def lambda_2BCF():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2BCF)
    Sleep(200)

    def lambda_2BEF():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2BEF)

    def lambda_2C0A():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2C0A)
    Sleep(200)

    def lambda_2C2A():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2C2A)

    def lambda_2C45():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2C45)
    Sleep(200)

    def lambda_2C65():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2C65)

    def lambda_2C80():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2C80)
    Sleep(200)

    def lambda_2CA0():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2CA0)

    def lambda_2CBB():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2CBB)
    Sleep(200)

    def lambda_2CDB():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2CDB)

    def lambda_2CF6():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2CF6)
    Sleep(200)

    def lambda_2D16():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2D16)

    def lambda_2D31():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2D31)
    Sleep(200)

    def lambda_2D51():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2D51)

    def lambda_2D6C():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2D6C)
    Sleep(200)

    def lambda_2D8C():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2D8C)

    def lambda_2DA7():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2DA7)
    Sleep(200)

    def lambda_2DC7():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2DC7)

    def lambda_2DE2():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2DE2)
    Sleep(200)

    def lambda_2E02():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2E02)

    def lambda_2E1D():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2E1D)
    Sleep(200)

    def lambda_2E3D():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2E3D)

    def lambda_2E58():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2E58)
    Sleep(200)

    def lambda_2E78():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2E78)

    def lambda_2E93():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2E93)
    Sleep(200)

    def lambda_2EB3():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2EB3)

    def lambda_2ECE():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2ECE)
    Sleep(2800)
    OP_43(0x23, 0x3, 0x0, 0x13)
    WaitChrThread(0x2B, 0x0)
    Sleep(1000)
    Fade(500)
    OP_44(0x2B, 0xFF)
    OP_6D(69400, -10000, 159000, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(219000, 0)
    OP_6E(414, 0)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x29, 71330, -10000, 158970, 180)
    SetChrPos(0x23, 70590, -10000, 160050, 180)
    SetChrPos(0x24, 69700, -10000, 159590, 180)
    SetChrPos(0x25, 70420, -10000, 161960, 180)
    SetChrPos(0x2A, 71370, -10000, 162100, 180)
    SetChrPos(0x26, 69960, -10000, 162900, 180)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #52
        0x29,
        (
            "#173F#6P那、那就是『铁血宰相』\x01",
            "吉利亚斯·奥斯本阁下吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x2A,
        (
            "#025F#6P明明有专用飞艇，\x01",
            "却特地要乘坐民间的定期船……\x02\x03",

            "#022F……早就听说过他的传闻，\x01",
            "看来是一个相当麻烦的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_309A():
        OP_6D(69400, -10000, 159730, 1000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_309A)

    def lambda_30B2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_30B2)
    Sleep(100)

    def lambda_30C5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_30C5)
    Sleep(100)

    def lambda_30D8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_30D8)
    WaitChrThread(0x2B, 0x0)
    Sleep(300)

    ChrTalk(    #54
        0x23,
        (
            "#1545F#5P呵呵……\x01",
            "是个非常难缠的对手呢。\x02\x03",

            "#1540F雪拉君。\x01",
            "有劳你专程赶来为我送行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x2A,
        (
            "#021F#6P呵呵，只不过是因为\x01",
            "在王都有事才顺便来的罢了。\x02\x03",

            "#524F……而且有种很长时间\x01",
            "不能再见面的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x23,
        (
            "#1541F#5P呼，我的梦想\x01",
            "无非就是和像雪拉君这样的美女\x01",
            "每天在一起寻欢作乐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x2A,
        (
            "#025F#6P是啊是啊。\x01",
            "所以啊，你要好好努力\x01",
            "早日功成名就嘛。\x02\x03",

            "#022F话说回来，那宰相身边的\x01",
            "那个年轻人是什么来头？\x02\x03",

            "从他的步伐上看不出一点破绽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x26,
        (
            "#1122F#11P哦……\x01",
            "你也看出来了啊，雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x2A,
        (
            "#025F#5P是啊，我注意到了。\x02\x03",

            "#524F因为这段时间\x01",
            "一直在和高手切磋嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x23,
        (
            "#1551F#5P……雷克特·亚兰德尔。\x01",
            "帝国政府的外派书记官。\x02\x03",

            "#1540F宰相这次的访问事宜\x01",
            "似乎全都是由他来安排的。\x02\x03",

            "#1545F虽然具体身份不明……\x01",
            "但应该是个相当优秀的参谋。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x25,
        (
            "#1169F#12P……奥利维特殿下。\x02\x03",

            "#1163F其实我……\x01",
            "认识那个人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x26, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_34ED():
        TurnDirection(0xFE, 0x25, 400)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_34ED)

    ChrTalk(    #62
        0x29,
        "#173F#5P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x2A,
        "#023F#6P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x23,
        "#1543F#5P……是真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x25,
        "#1167F#12P是的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05科洛蒂娅将雷克特\x01",
            "是她在王立学院的学长，\x01",
            "并担任学生会长职务的身份……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        (
            "\x07\x05以及他在前年的学院祭之后\x01",
            "递交退学申请离开学校的事情向大家做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #68
        0x24,
        "#270F#5P……这………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x29,
        "#172F#5P难、难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x23,
        (
            "#1551F#5P……『铁血宰相』的手下\x01",
            "在我们之前就已经到访了利贝尔。\x02\x03",

            "#1542F也就意味着宰相\x01",
            "已经在利贝尔建立了\x01",
            "完善的个人情报网……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x26,
        (
            "#1125F#12P唔……\x01",
            "这种可能性很高。\x02\x03",

            "#1128F从情报部的政变\x01",
            "到上回『辉之环』的异变……\x02\x03",

            "#1122F就算他们对其尽收眼底\x01",
            "也不能称得上奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x23,
        "#1551F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x2A,
        "#025F#6P真是不得了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x25,
        (
            "#1169F#12P……刚才学长\x01",
            "让我向殿下转达一句话。\x02\x03",

            "#1162F他说——\x01",
            "『不要在跳舞跳得累了的时候\x01",
            "  被怪物吞掉』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x24,
        "#276F#5P…………哼…………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x23,
        (
            "#1544F#5P哎呀……\x01",
            "刺中我的软肋了。\x02\x03",

            "#1547F呵呵，有一种异样的快感\x01",
            "从我心中觉醒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #77
        0x23,
        (
            "#1545F#5P不过……我也不高兴\x01",
            "总被别人抓到弱点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x25,
        "#1164F#12P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_396D():
        OP_6D(69400, -10000, 159000, 1200)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_396D)

    def lambda_3985():
        OP_6C(206000, 1200)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_3985)
    TurnDirection(0x23, 0x29, 400)

    def lambda_399C():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_399C)

    def lambda_39AA():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_39AA)
    WaitChrThread(0x2B, 0x0)
    Sleep(300)

    ChrTalk(    #79
        0x23,
        (
            "#1541F#12P──尤莉亚上尉。\x02\x03",

            "#1540F在出航之际\x01",
            "我还有一个请求……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A15():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_3A15)

    def lambda_3A23():
        OP_6B(1800, 3000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3A23)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_25EB end

    def Function_14_3A50(): pass

    label("Function_14_3A50")


    def lambda_3A56():
        OP_8E(0xFE, 0x14384, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A56)
    WaitChrThread(0x20, 0x1)

    def lambda_3A76():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A76)
    WaitChrThread(0x20, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_3A50 end

    def Function_15_3A96(): pass

    label("Function_15_3A96")

    SetChrFlags(0xFE, 0x40)
    Sleep(300)
    OP_8C(0xFE, 90, 400)
    Sleep(300)

    def lambda_3AB2():
        OP_8E(0xFE, 0x1444C, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AB2)
    WaitChrThread(0xFE, 0x1)

    def lambda_3AD2():
        OP_8E(0xFE, 0x1444C, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AD2)
    WaitChrThread(0xFE, 0x1)

    def lambda_3AF2():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AF2)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_3A96 end

    def Function_16_3B12(): pass

    label("Function_16_3B12")

    SetChrFlags(0xFE, 0x40)
    Sleep(1300)

    def lambda_3B22():
        OP_8E(0xFE, 0x14384, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B22)
    WaitChrThread(0xFE, 0x1)

    def lambda_3B42():
        OP_8E(0xFE, 0x14384, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B42)
    WaitChrThread(0xFE, 0x1)

    def lambda_3B62():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B62)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_3B12 end

    def Function_17_3B82(): pass

    label("Function_17_3B82")


    def lambda_3B88():
        OP_8E(0xFE, 0x143D4, 0x60E, 0x20BB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B88)
    WaitChrThread(0xFE, 0x1)

    def lambda_3BA8():
        OP_8E(0xFE, 0x14DFC, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BA8)
    WaitChrThread(0xFE, 0x1)

    def lambda_3BC8():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BC8)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_3B82 end

    def Function_18_3BE8(): pass

    label("Function_18_3BE8")

    OP_8C(0x28, 90, 400)

    def lambda_3BF5():
        OP_8E(0xFE, 0x143D4, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3BF5)
    WaitChrThread(0x28, 0x1)

    def lambda_3C15():
        OP_8E(0xFE, 0x143D4, 0x60E, 0x20BB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C15)
    WaitChrThread(0xFE, 0x1)

    def lambda_3C35():
        OP_8E(0xFE, 0x14DFC, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C35)
    WaitChrThread(0xFE, 0x1)

    def lambda_3C55():
        OP_8E(0xFE, 0x154A0, 0x5DC, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_3C55)
    WaitChrThread(0x28, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_3BE8 end

    def Function_19_3C75(): pass

    label("Function_19_3C75")

    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    Return()

    # Function_19_3C75 end

    def Function_20_3CB8(): pass

    label("Function_20_3CB8")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    Return()

    # Function_20_3CB8 end

    SaveToFile()

Try(main)

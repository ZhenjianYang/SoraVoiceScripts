from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5900   ._SN',
        MapName             = 'Other',
        Location            = 'C5900.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        '雪拉扎德',                             # 9
        '奥利维尔',                             # 10
        '科洛丝',                               # 11
        '阿加特',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '凯文神父',                             # 15
        '拉赛尔博士',                           # 16
        '奈尔',                                 # 17
        '朵洛希',                               # 18
        '穆拉少校',                             # 19
        '尤莉亚上尉',                           # 20
        '基库',                                 # 21
        '操舵士勒克司',                         # 22
        '菲',                                   # 23
        '乔丝特',                               # 24
        '亲卫队队员',                           # 25
        '亲卫队队员',                           # 26
        '亲卫队队员',                           # 27
        '亲卫队队员',                           # 28
        '库莱泽',                               # 29
        '公园区域『卡尔玛丽』２',               # 30
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
        'ED6_DT07/CH00020 ._CH',             # 00
        'ED6_DT07/CH00030 ._CH',             # 01
        'ED6_DT27/CH03210 ._CH',             # 02
        'ED6_DT07/CH00050 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT27/CH03080 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT27/CH03570 ._CH',             # 0A
        'ED6_DT27/CH03580 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT27/CH03860 ._CH',             # 0D
        'ED6_DT06/CH20064 ._CH',             # 0E
        'ED6_DT07/CH00310 ._CH',             # 0F
        'ED6_DT27/CH04107 ._CH',             # 10
        'ED6_DT07/CH01550 ._CH',             # 11
        'ED6_DT27/CH03100 ._CH',             # 12
        'ED6_DT07/CH01320 ._CH',             # 13
        'ED6_DT07/CH01450 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT27/CH03210P._CP',             # 02
        'ED6_DT07/CH00050P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT27/CH03080P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT27/CH03570P._CP',             # 0A
        'ED6_DT27/CH03580P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT27/CH03860P._CP',             # 0D
        'ED6_DT06/CH20064P._CP',             # 0E
        'ED6_DT07/CH00310P._CP',             # 0F
        'ED6_DT27/CH04107P._CP',             # 10
        'ED6_DT07/CH01550P._CP',             # 11
        'ED6_DT27/CH03100P._CP',             # 12
        'ED6_DT07/CH01320P._CP',             # 13
        'ED6_DT07/CH01450P._CP',             # 14
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13600,
        Z                   = 0,
        Y                   = 37280,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -21910,
        Z                   = 3500,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -20140,
        Z                   = 3500,
        Y                   = 22380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 2830,
        Z                   = 0,
        Y                   = 28680,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -24350,
        Z                   = 0,
        Y                   = 18840,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -21600,
        Z                   = 0,
        Y                   = 15040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -24920,
        Z                   = 0,
        Y                   = 16710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -13210,
        Z                   = -3390,
        Y                   = 27060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -10,
        Z                   = 0,
        Y                   = -43810,
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
        X                   = -16900,
        Y                   = -3300,
        Z                   = 24600,
        Range               = -15900,
        Unknown_10          = 0xFFFFFAEC,
        Unknown_14          = 0x67E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -24500,
        Y                   = 3200,
        Z                   = 26800,
        Range               = -23500,
        Unknown_10          = 0x1450,
        Unknown_14          = 0x7080,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -2800,
        Y                   = 0,
        Z                   = -34600,
        Range               = 2700,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFF7CC0,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_7D4",          # 01, 1
        "Function_2_8C4",          # 02, 2
        "Function_3_D09",          # 03, 3
        "Function_4_1361",         # 04, 4
        "Function_5_17B3",         # 05, 5
        "Function_6_1D92",         # 06, 6
        "Function_7_21D4",         # 07, 7
        "Function_8_2754",         # 08, 8
        "Function_9_2ECE",         # 09, 9
        "Function_10_38D1",        # 0A, 10
        "Function_11_3DD9",        # 0B, 11
        "Function_12_3DDD",        # 0C, 12
        "Function_13_40E1",        # 0D, 13
        "Function_14_429F",        # 0E, 14
        "Function_15_44DA",        # 0F, 15
        "Function_16_46A5",        # 10, 16
        "Function_17_4C43",        # 11, 17
        "Function_18_5154",        # 12, 18
        "Function_19_537E",        # 13, 19
        "Function_20_5D25",        # 14, 20
        "Function_21_5D48",        # 15, 21
        "Function_22_5D6B",        # 16, 22
        "Function_23_5D8E",        # 17, 23
        "Function_24_5DB1",        # 18, 24
        "Function_25_5DD4",        # 19, 25
        "Function_26_5DF7",        # 1A, 26
        "Function_27_5E1A",        # 1B, 27
        "Function_28_5E3D",        # 1C, 28
        "Function_29_5E5B",        # 1D, 29
        "Function_30_5E61",        # 1E, 30
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_7C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -38250, 4500, 28710, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -45190, 5000, 33140, 45)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E9")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17120, 3500, 23510, 135)

    label("loc_4E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20610, 0, 16960, 315)

    label("loc_50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -23120, 0, 16149, 0)

    label("loc_52F")

    Jump("loc_7C0")

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_670")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -43870, 5000, 31520, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -39890, 4500, 33700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573")
    SetChrFlags(0x11, 0x10)

    label("loc_573")

    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -18420, 3500, 22380, 227)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 1440, -4000, 23570, 45)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 33290, -4000, 16740, 225)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -11560, 0, 34340, 262)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4340, -4000, 19880, 315)
    OP_43(0x12, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4310, -4000, 22130, 315)

    label("loc_615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_627")
    ClearChrFlags(0x17, 0x80)

    label("loc_627")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5070, -3880, 23930, 270)

    label("loc_64A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_66D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_66D")

    Jump("loc_7C0")

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_736")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -18600, 3500, 25160, 35)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 10, -4000, 24410, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14280, 0, 25700, 135)
    OP_43(0x12, 0x0, 0x6, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -16370, 3500, 27040, 170)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 14760, -4000, 19280, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_710")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34850, -4000, 16079, 225)

    label("loc_710")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_733")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_733")

    Jump("loc_7C0")

    label("loc_736")

    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -22940, 0, 39040, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_792")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_792")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -18510, 3500, 22430, 180)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_792")
    SetChrFlags(0x8, 0x10)

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C0")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -43550, 5000, 31240, 225)

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_7D3")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 19)

    label("loc_7D3")

    Return()

    # Function_0_472 end

    def Function_1_7D4(): pass

    label("Function_1_7D4")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE3EC8, 0x230079)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1C3, 0x1, 0x50)
    OP_22(0x1C7, 0x1, 0x64)
    OP_51(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_837")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x6, 0x4)
    OP_72(0x12, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    Jump("loc_873")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_855")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x6, 0x4)
    OP_72(0x12, 0x4)
    Jump("loc_873")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_86E")
    OP_71(0x4, 0x4)
    OP_72(0xA, 0x4)
    OP_71(0x12, 0x4)
    Jump("loc_873")

    label("loc_86E")

    OP_71(0x12, 0x4)

    label("loc_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_8C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B9")
    OP_D2(0x600FC, 0x60101, 0x15)
    Jump("loc_8C3")

    label("loc_8B9")

    OP_D2(0x600FC, 0x60101, 0x15)

    label("loc_8C3")

    Return()

    # Function_1_7D4 end

    def Function_2_8C4(): pass

    label("Function_2_8C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_BFC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A60")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x10B, 0)
    Sleep(1000)

    ChrTalk(    #0
        0x10,
        (
            "#143F哦，莫非你是\x01",
            "空贼团的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#210F呵呵，是啊。\x01",
            "我是卡普亚一家的乔丝特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#141F哦，果然没错啊！\x02\x03",

            "下次有时间的话，\x01",
            "把你们的故事说给我听听吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10B,
        (
            "#212F不好意思，如果是利贝尔通讯\x01",
            "的采访的话我拒绝。\x02\x03",

            "写了那么多别人的坏话，\x01",
            "居然还好意思说这些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#147F这、这个嘛……\x02\x03",

            "你也希望有一个\x01",
            "澄清的机会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10B,
        "#214F不───要。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x2299)
    Jump("loc_AFE")

    label("loc_A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_AB2")
    TurnDirection(0x10, 0x10B, 0)

    ChrTalk(    #6
        0x10,
        (
            "#147F拜托你\x01",
            "别拒绝我的采访。\x02\x03",

            "这、这次我不会\x01",
            "把你们写坏的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFE")

    label("loc_AB2")

    TurnDirection(0x10, 0x10B, 0)

    ChrTalk(    #7
        0x10,
        (
            "#147F拜托，请你别\x01",
            "拒绝我的采访。\x02\x03",

            "这、这次我不会\x01",
            "把你们写坏的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFE")

    Jump("loc_BF9")

    label("loc_B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA8")

    ChrTalk(    #8
        0x10,
        (
            "#140F想不到卡普亚一家\x01",
            "居然会来到这里。\x02\x03",

            "有机会的话真想\x01",
            "拍张空贼艇的照片呢……\x02\x03",

            "不过毕竟还是没办法\x01",
            "在这种地方乱晃。\x02\x03",

            "好吧，先老老实实地\x01",
            "等待机会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_BF9")

    label("loc_BA8")


    ChrTalk(    #9
        0x10,
        (
            "#142F想不到卡普亚一家\x01",
            "居然会来到这里。\x02\x03",

            "真是有够命大的。\x01",
            "简直就像杂草一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF9")

    Jump("loc_D05")

    label("loc_BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(    #10
        0x10,
        (
            "#143F重新看了一下才发现，\x01",
            "这还真是个不得了的东西呢。\x02\x03",

            "虽然有点晚，不过还是让我\x01",
            "想起了『七至宝』的传说。\x02\x03",

            "#145F女神授予的宝物……吗？\x01",
            "看来不只是传说而已啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D05")

    label("loc_CB2")


    ChrTalk(    #11
        0x10,
        (
            "#145F抱歉，让我一个人\x01",
            "静一静吧。\x02\x03",

            "多年积累的常识突然崩溃，\x01",
            "我的脑子里有点乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D05")

    TalkEnd(0xFE)
    Return()

    # Function_2_8C4 end

    def Function_3_D09(): pass

    label("Function_3_D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_126C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1103")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-38760, 4500, 32630, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -37750, 4500, 32580, 298)
    SetChrPos(0x102, -39650, 4500, 31210, 360)
    SetChrPos(0x10B, -38490, 4500, 31610, 317)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    SetChrPos(0xF9, -37690, 4500, 30730, 307)
    Jump("loc_DD2")

    label("loc_DC1")

    SetChrPos(0xF8, -37690, 4500, 30730, 307)

    label("loc_DD2")

    OP_0D()
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x10B, 400)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #12
        0x11,
        (
            "#151F哇，好可爱的护目镜！\x02\x03",

            "请问－－，不好意思，\x01",
            "能不能请您摆个ＰＯＳＥ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E4A():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4A)

    def lambda_E58():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E58)

    ChrTalk(    #13
        0x10B,
        "#213F啊！？ＰＯＳＥ？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 14)

    ChrTalk(    #14
        0x11,
        (
            "#153F快点，不然我就要\x01",
            "拍了哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10B,
        "#216F那、那个……\x02",
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x10B, 15)
    OP_0D()

    ChrTalk(    #16
        0x10B,
        "#214F……这、这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#151F嗯嗯，很好！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #18
        0x11,
        (
            "#151F再来一张～\x01",
            "这次要更可爱点！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10B,
        "#413F那、那么就这样……\x02",
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x10B, 16)
    OP_0D()

    ChrTalk(    #20
        0x11,
        "#151F哇，很棒的感觉！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x11, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x11,
        (
            "#151F好～拍摄完毕～\x01",
            "谢谢您的配合～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Fade(400)
    SetChrChipByIndex(0x10B, 65535)
    OP_0D()
    OP_6D(-38090, 4500, 31080, 1000)

    ChrTalk(    #22
        0x10B,
        (
            "#213F………………………\x02\x03",

            "#215F……咦？刚才那是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        "#1040F就像是在打个招呼之类的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1016F不、不过变得\x01",
            "比以前更变本加厉了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x5)
    OP_A2(0x229A)
    Jump("loc_1196")

    label("loc_1103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1147")

    ChrTalk(    #25
        0x11,
        (
            "#150F嘿嘿，也因此\x01",
            "拍到了很好的照片。\x02\x03",

            "谢谢您的配合～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1196")

    label("loc_1147")


    ChrTalk(    #26
        0x11,
        (
            "#151F从这里看的话，\x01",
            "天空显得特别接近哦。\x02\x03",

            "呼～感觉整个人\x01",
            "要被吸进去似的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1196")

    Jump("loc_1269")

    label("loc_1199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(    #27
        0x11,
        (
            "#151F从这里看的话，\x01",
            "天空显得特别接近哦。\x02\x03",

            "呼～感觉整个人\x01",
            "要被吸进去似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1019F……别掉下去啊，朵洛希。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1269")

    label("loc_121A")


    ChrTalk(    #29
        0x11,
        (
            "#151F从这里看的话，\x01",
            "天空显得特别接近哦。\x02\x03",

            "呼～感觉整个人\x01",
            "要被吸进去似的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1269")

    Jump("loc_135D")

    label("loc_126C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_135D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_130C")

    ChrTalk(    #30
        0x11,
        (
            "#151F哇，好棒的景色！\x02\x03",

            "空气清新又宜人，\x01",
            "真想住在这里呢～\x02\x03",

            "#154F啊，不过没工房的话\x01",
            "就买不到感光结晶回路了～\x02\x03",

            "嗯～这个就\x01",
            "有点伤脑筋了～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_135D")

    label("loc_130C")


    ChrTalk(    #31
        0x11,
        (
            "#150F这里景色好棒，\x01",
            "真想住在这里试试～\x02\x03",

            "要不要干脆把整个\x01",
            "编辑部都搬过来呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135D")

    TalkEnd(0xFE)
    Return()

    # Function_3_D09 end

    def Function_4_1361(): pass

    label("Function_4_1361")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_136E")
    Jump("loc_17AF")

    label("loc_136E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1468")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")

    ChrTalk(    #32
        0xFE,
        "啊，殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "现在正在调整飞翔引擎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽然是很困难的作业，\x01",
            "不过这也是最后的难题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "距离修复完成只差一步了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_140B")


    ChrTalk(    #36
        0xFE,
        (
            "飞翔引擎的调整\x01",
            "是最后的难关了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "只要这方面顺利的话，\x01",
            "距离修复完成只差一步了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1465")

    Jump("loc_155F")

    label("loc_1468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FD")

    ChrTalk(    #38
        0xFE,
        (
            "现在我正在调整\x01",
            "飞翔引擎的状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "因为飞船是一种借由推力平衡的\x01",
            "偏向来改变方向的交通工具……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "引擎的调整就\x01",
            "相当于舵的调整。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_155F")

    label("loc_14FD")


    ChrTalk(    #41
        0xFE,
        (
            "因为飞船是一种借由推力平衡的\x01",
            "偏向来改变方向的交通工具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "引擎的调整\x01",
            "有着非常重要的意义。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155F")

    Jump("loc_17AF")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_17A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1665")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #43
        0xFE,
        (
            "哦，我还在想怎么会有\x01",
            "陌生的面孔出现呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "原来如此，你是\x01",
            "那个空贼团的女孩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "不过，还真没想到\x01",
            "会和你们合作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "算了，虽然感觉很复杂，\x01",
            "不过这段时间还是要拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "现在真是忙得\x01",
            "不可开交啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)
    OP_A2(0x22D0)
    Jump("loc_17A5")

    label("loc_1665")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16E6")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #48
        0xFE,
        (
            "虽然和你们合作\x01",
            "感觉很复杂……\x02",
        )
    )


    ChrTalk(    #49
        0xFE,
        "不过这段时间还是要拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "现在真是忙得\x01",
            "不可开交啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A5")

    label("loc_16E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(    #51
        0xFE,
        (
            "修复左舷脱落的支架\x01",
            "是最庞大的工程呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "必须借助大家的\x01",
            "智慧一起来想办法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A5")

    label("loc_1749")


    ChrTalk(    #53
        0xFE,
        (
            "修复左舷脱落的支架\x01",
            "是个巨大的工程哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "因此，必须借助大家的\x01",
            "智慧一起来想办法……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A5")

    Jump("loc_17AF")

    label("loc_17A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_17AF")

    label("loc_17AF")

    TalkEnd(0xFE)
    Return()

    # Function_4_1361 end

    def Function_5_17B3(): pass

    label("Function_5_17B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EF")
    TurnDirection(0x16, 0x101, 0)

    ChrTalk(    #55
        0xFE,
        "哎呀，又碰到你们了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1846")

    ChrTalk(    #56
        0x101,
        "#1004F啊，菲小姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        "#064F您留在船上吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_186C")

    label("loc_1846")


    ChrTalk(    #58
        0x101,
        (
            "#1004F啊，菲小姐！\x02\x03",

            "你留在船上？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186C")


    ChrTalk(    #59
        0xFE,
        (
            "嗯，我想既然博士留下来了，\x01",
            "那么我也跟着留下来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "和整备人员们商量后，\x01",
            "我就决定一起留下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "不过现在看起来，\x01",
            "这个决定似乎是正确的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1018F不只正确，是明智的决定哦。\x02\x03",

            "因为现在必须要\x01",
            "修理『埃尔赛尤』嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1040F太好了。\x01",
            "专业人员是相当宝贵的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "哈哈，谢谢你们欢迎我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "为了不辜负你们的期望，\x01",
            "我会竭尽所能地努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1001F嗯！　拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x229B)
    Jump("loc_1D8E")

    label("loc_19EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1A47")

    ChrTalk(    #67
        0xFE,
        (
            "看来留在飞船上\x01",
            "似乎是正确的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "就让我这机械专家\x01",
            "竭尽所能地努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8E")

    label("loc_1A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1B53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF8")

    ChrTalk(    #69
        0xFE,
        (
            "呼，还能使用的碎片\x01",
            "差不多都回收完毕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "舷梯的设置也完成了，\x01",
            "我差不多也要回飞船上\x01",
            "去帮忙修理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "他们应该是在忙着进行\x01",
            "零部件的加工与调整吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_1B50")

    label("loc_1AF8")


    ChrTalk(    #72
        0xFE,
        (
            "碎片的回收和舷梯的设置\x01",
            "总算告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "我差不多也要回飞船上\x01",
            "去帮忙修理了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B50")

    Jump("loc_1D8E")

    label("loc_1B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1D0F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C01")

    ChrTalk(    #74
        0xFE,
        (
            "这个新来的女孩……\x01",
            "干得相当不错哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "工具使用起来很熟练，\x01",
            "也具备相当的整备知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "你们还真是在关键时刻\x01",
            "带来了个好女孩过来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_1C50")

    label("loc_1C01")


    ChrTalk(    #77
        0xFE,
        "这个新来的女孩干得不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "你们还真是在关键时刻\x01",
            "带了个有用的人回来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C50")

    Jump("loc_1D0C")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD8")

    ChrTalk(    #79
        0xFE,
        (
            "就如你们所看到的，\x01",
            "舷梯已经完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "接下来预定要\x01",
            "放在必要的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "嗯，还要架设一座\x01",
            "在往下走的时候使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_1D0C")

    label("loc_1CD8")


    ChrTalk(    #82
        0xFE,
        (
            "舷梯已经完成了。\x01",
            "接下来预定要\x01",
            "放在必要的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0C")

    Jump("loc_1D8E")

    label("loc_1D0F")


    ChrTalk(    #83
        0xFE,
        (
            "收拾好下面的碎片之后，\x01",
            "预计要在这里架一座桥哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "这样出入甲板\x01",
            "就方便得多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "你们出去探索的时候\x01",
            "也会比较便利吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8E")

    TalkEnd(0xFE)
    Return()

    # Function_5_17B3 end

    def Function_6_1D92(): pass

    label("Function_6_1D92")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DF3"),
        (1, "loc_21C6"),
        (2, "loc_21CD"),
        (SWITCH_DEFAULT, "loc_21D0"),
    )


    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E5E")

    ChrTalk(    #86
        0x17,
        (
            "#214F你、你们在闲晃些什么啊！\x01",
            "赶快去结社那帮家伙的飞船啊！\x02\x03",

            "哥哥他们\x01",
            "肯定在那里的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x444, 0)), scpexpr(EXPR_END)), "loc_1FAC")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #87
        0x17,
        (
            "#210F啊，约修亚……\x02\x03",

            "#213F……怎么了？\x01",
            "你好像想说什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        "#1042F嗯，我是来报告的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x17,
        "#213F……报告？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1015F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #91
        "\x07\x05说明了在工业区域发现了『古罗力亚斯』的事。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x17,
        (
            "#214F真、真的吗！？\x02\x03",

            "马、马上带我过去！\x01",
            "哥哥他们应该在那里才对！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22D5)
    Jump("loc_21C3")

    label("loc_1FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2149")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #93
        0x17,
        "#415F啊，约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        "#1040F已经开始帮忙了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x17,
        (
            "#210F嗯、嗯，当然啰。\x02\x03",

            "我一开始就说过\x01",
            "会帮忙的吧。\x02\x03",

            "我在『山猫号』上\x01",
            "也经常修东修西。\x02\x03",

            "我会证明自己比某人\x01",
            "要有用得多的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1019F（气、气人……\x01",
            "最令人懊恼的是完全无法反驳。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#1049F谢谢你，实在帮了我们的大忙。\x02\x03",

            "如果发现了吉尔他们的话，\x01",
            "我们会马上来通知你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x17,
        (
            "#210F嗯，拜托了你们。\x02\x03",

            "那么，约修亚也\x01",
            "要当心……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22C7)
    Jump("loc_21C3")

    label("loc_2149")


    ChrTalk(    #99
        0x17,
        (
            "#210F在找到哥哥他们之前，\x01",
            "我会一起帮忙修理的。\x02\x03",

            "我在『山猫号』上\x01",
            "也经常修东修西。\x02\x03",

            "我会证明自己比某人\x01",
            "要有用得多哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C3")

    Jump("loc_21D0")

    label("loc_21C6")

    Call(0, 18)
    Jump("loc_21D0")

    label("loc_21CD")

    Jump("loc_21D0")

    label("loc_21D0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1D92 end

    def Function_7_21D4(): pass

    label("Function_7_21D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2235")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2235")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_224A"),
        (1, "loc_2714"),
        (2, "loc_274D"),
        (SWITCH_DEFAULT, "loc_2750"),
    )


    label("loc_224A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_25E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x453, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_243B")
    TurnDirection(0x9, 0x10B, 0)

    ChrTalk(    #100
        0x9,
        (
            "#035F呼，自从上次王都的\x01",
            "武术大会以来就没见过你了。\x02\x03",

            "而且今天是第一次\x01",
            "和你面对面交谈吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10B,
        (
            "#210F嗯，我也\x01",
            "还记得你。\x02\x03",

            "因为就某方面来说，\x01",
            "你不像是个帝国人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#033F哟，真残酷啊……\x02\x03",

            "#031F我在也用我的方式\x01",
            "爱着我的祖国哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10B,
        (
            "#215F要是你有那份心的话，\x01",
            "为什么不赶快回到国内工作？\x02\x03",

            "在王国到处闲晃，\x01",
            "不像是帝国男儿的作风吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "#035F呵呵，不必担心。\x01",
            "我迟早会回去的。\x02\x03",

            "#030F好了，先不管这些……\x01",
            "以后请多多关照啊。\x02\x03",

            "我们都是用枪的，\x01",
            "一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x229D)
    Jump("loc_25E6")

    label("loc_243B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A6")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #105
        0x9,
        (
            "#030F好了，不管怎么说，\x01",
            "以后请多多关照啊。\x02\x03",

            "我们都是用枪的，\x01",
            "一起努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E6")

    label("loc_24A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_258A")

    ChrTalk(    #106
        0x9,
        (
            "#035F接下来好像要大家\x01",
            "一起合力搬运巨大碎片呢。\x02\x03",

            "不知道为什么，\x01",
            "连我也被拉来当苦力了。\x02\x03",

            "#037F……是、是不是该找我\x01",
            "一起去探索了？\x02\x03",

            "如果需要的话，\x01",
            "跟我打声招呼就行了。\x02\x03",

            "#034F……应该说，拜托你们\x01",
            "把我带离这里吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_25E6")

    label("loc_258A")


    ChrTalk(    #107
        0x9,
        (
            "#037F如果需要我的话，\x01",
            "随时可以过来找我哦。\x02\x03",

            "#034F……应该说，拜托你们\x01",
            "把我带离这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E6")

    Jump("loc_2711")

    label("loc_25E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AC")

    ChrTalk(    #108
        0x9,
        (
            "#034F舰体的碎片还\x01",
            "散落得真远呢。\x02\x03",

            "要靠人力回收的话，\x01",
            "可是个浩大工程哦……\x02\x03",

            "#035F当然，我身为演奏家，\x01",
            "也会发挥我的所长。\x02\x03",

            "呵呵，让我用美丽的音符\x01",
            "来激励流汗劳动的诸位吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_2711")

    label("loc_26AC")


    ChrTalk(    #109
        0x9,
        (
            "#035F在大家流汗的时候，\x01",
            "就让我用歌声来支持大家吧。\x02\x03",

            "因此，体力劳动的事情\x01",
            "交给穆拉来做就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2711")

    Jump("loc_2750")

    label("loc_2714")


    ChrTalk(    #110
        0x9,
        (
            "#035F呵呵，看来你们需要\x01",
            "我这个天才的力量了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_2750")

    label("loc_274D")

    Jump("loc_2750")

    label("loc_2750")

    TalkEnd(0xFE)
    Return()

    # Function_7_21D4 end

    def Function_8_2754(): pass

    label("Function_8_2754")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27B5"),
        (1, "loc_2E9F"),
        (2, "loc_2EC7"),
        (SWITCH_DEFAULT, "loc_2ECA"),
    )


    label("loc_27B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_END)), "loc_2B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1C")

    ChrTalk(    #111
        0x101,
        "#1011F咦，雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#020F呵呵，我就知道\x01",
            "你们差不多该回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        (
            "#1044F莫非……\x01",
            "你在等我们吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #114
        0x8,
        (
            "#026F只是一种预感而已。\x02\x03",

            "你们……\x01",
            "和姐姐她战斗过了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1043F嗯，确实……\x02\x03",

            "#1035F不过，最后\x01",
            "她还是走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1003F她说她和雪拉姐的\x01",
            "缘分还没有断……\x02\x03",

            "以后还有机会相见，\x01",
            "然后就消失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#522F是吗……\x02\x03",

            "果然不会\x01",
            "那么简单就落幕啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#1026F雪拉姐……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #119
        0x8,
        (
            "#524F呵呵，不用担心。\x02\x03",

            "如姐姐所说，\x01",
            "应该还会再相见的……\x02\x03",

            "总之，现在我就先相信这一点，\x01",
            "然后把这件事情放在心底。\x02\x03",

            "……对我们来说，接下来\x01",
            "还有更加重要的事要完成吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1E")

    ChrTalk(    #120
        0x104,
        "#035F呵呵，雪拉说得没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A50")

    ChrTalk(    #121
        0x106,
        "#051F嗯，雪拉扎德说得没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7C")

    ChrTalk(    #122
        0x108,
        "#070F嗯，你说得没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AAF")

    ChrTalk(    #123
        0x109,
        (
            "#1060F是啊……\x01",
            "大姐你说得没错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAF")


    ChrTalk(    #124
        0x101,
        (
            "#1002F嗯……\x01",
            "现在必须前进才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#020F如果需要我帮忙\x01",
            "就过来说，不用客气。\x02\x03",

            "那么，你们小心点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22A1)
    Jump("loc_2B75")

    label("loc_2B1C")


    ChrTalk(    #126
        0x8,
        (
            "#020F我会把露茜奥拉姐姐的事\x01",
            "放在心底的。\x02\x03",

            "不管怎么说，现在\x01",
            "我们必须做好该做的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B75")

    Jump("loc_2E9C")

    label("loc_2B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3F")

    ChrTalk(    #127
        0x8,
        "#522F…………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDF")

    ChrTalk(    #128
        0x104,
        "#033F雪拉……你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_2C74")

    label("loc_2BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C16")

    ChrTalk(    #129
        0x106,
        "#052F雪拉扎德……你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_2C74")

    label("loc_2C16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4D")

    ChrTalk(    #130
        0x108,
        "#072F雪拉扎德……你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)
    Jump("loc_2C74")

    label("loc_2C4D")


    ChrTalk(    #131
        0x102,
        "#1044F雪拉姐……你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    label("loc_2C74")


    ChrTalk(    #132
        0x8,
        (
            "#524F嗯……我只是\x01",
            "在想一些事情。\x02\x03",

            "没事的……\x01",
            "我已经整理好心情了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF0")

    ChrTalk(    #133
        0x104,
        (
            "#033F那就好……\x01",
            "不过也别太勉强。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2CF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(    #134
        0x106,
        (
            "#552F那就好……\x01",
            "不过也别太勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2D27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(    #135
        0x108,
        (
            "#072F是吗……\x01",
            "不过也别太勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D94")

    ChrTalk(    #136
        0x109,
        (
            "#1063F那就好……\x01",
            "不过可别太勉强哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2D94")


    ChrTalk(    #137
        0x102,
        (
            "#1043F那就好……\x01",
            "不过请别太勉强自己。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBF")


    ChrTalk(    #138
        0x8,
        (
            "#025F是是，我知道啦。\x02\x03",

            "唉，为什么男人只有在\x01",
            "这时候才会表现出温柔来呢。\x02\x03",

            "我倒是希望你们平时\x01",
            "能够更多多怜恤女人。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x22A1)
    Jump("loc_2E9C")

    label("loc_2E3F")


    ChrTalk(    #139
        0x8,
        (
            "#020F我已经没事了。\x02\x03",

            "心情也整理好了，\x01",
            "随时可以去探索。\x02\x03",

            "那么，需要我的时候\x01",
            "就来叫我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9C")

    Jump("loc_2ECA")

    label("loc_2E9F")


    ChrTalk(    #140
        0x8,
        "#020F哎呀，要更换成员了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_2ECA")

    label("loc_2EC7")

    Jump("loc_2ECA")

    label("loc_2ECA")

    TalkEnd(0xFE)
    Return()

    # Function_8_2754 end

    def Function_9_2ECE(): pass

    label("Function_9_2ECE")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F2F"),
        (1, "loc_38AA"),
        (2, "loc_38CA"),
        (SWITCH_DEFAULT, "loc_38CD"),
    )


    label("loc_2F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_340F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_END)), "loc_32B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3226")

    ChrTalk(    #141
        0x101,
        (
            "#1011F啊，金先生……\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #142
        0xD,
        (
            "#070F哦，是艾丝蒂尔啊……\x02\x03",

            "……你好像有什么话要说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1002F嗯……\x01",
            "其实是瓦鲁特的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "#074F……他还是出现了吗。\x02\x03",

            "#070F不过，你们能够\x01",
            "安然地回来就代表……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x102,
        "#1040F是的，好不容易才击退了他。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1015F嗯，虽然很危险。\x02\x03",

            "总之，看来这次他是\x01",
            "退出战局了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        (
            "#074F原来如此，他走了吗……\x02\x03",

            "把和我之间的对决\x01",
            "留到下次了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x102,
        (
            "#1043F嗯，瓦鲁特他自己\x01",
            "也是这么说的。\x02\x03",

            "看来是\x01",
            "暂时停战呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        (
            "#074F嗯，应该是这样吧。\x02\x03",

            "虽然心情上有点遗憾……\x01",
            "不过这或许也是件好事。\x02\x03",

            "#572F和瓦鲁特的因缘\x01",
            "是我自己应该解决的问题……\x02\x03",

            "把你们也卷进来的话\x01",
            "是缺乏道义的行为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1026F金先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xD,
        (
            "#070F总之，现在我们应该为\x01",
            "能够突破他的防守而高兴吧。\x02\x03",

            "我们确实面对着\x01",
            "应该完成的使命前进了一步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3226")


    ChrTalk(    #152
        0xD,
        (
            "#070F虽然决战被留到了将来，\x01",
            "不过现在这样说不定也好。\x02\x03",

            "和瓦鲁特的因缘\x01",
            "是我自己应该解决的问题……\x02\x03",

            "把你们也卷进来的话\x01",
            "是缺乏道义的行为。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B2")

    OP_A2(0x22A8)
    Jump("loc_340C")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_340C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3397")

    ChrTalk(    #153
        0xD,
        (
            "#074F瓦鲁特曾是位\x01",
            "天资远胜于我的拳术师。\x02\x03",

            "可是，却被背负『泰斗』\x01",
            "之名的我击败了……\x02\x03",

            "#072F看来重要的不是力量的强与弱，\x01",
            "而是为了什么去使用的问题。\x02\x03",

            "身为一个为武而生的人，\x01",
            "我也必须重新审视自己才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_340C")

    label("loc_3397")


    ChrTalk(    #154
        0xD,
        (
            "#074F看来重要的不是力量的强与弱，\x01",
            "而是为了什么去使用的问题。\x02\x03",

            "身为一个为武而生的人，\x01",
            "我也必须重新审视自己才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_340C")

    Jump("loc_38A7")

    label("loc_340F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_3542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C3")

    ChrTalk(    #155
        0xD,
        (
            "#070F嗯，看来碎片的\x01",
            "回收也快完成了……\x02\x03",

            "收拾完这个，剩下的\x01",
            "就交给亲卫队吧。\x02\x03",

            "毕竟都市的探索\x01",
            "也渐入佳境了。\x02\x03",

            "接下来应该是将力量放在\x01",
            "身为游击士的本分上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_353F")

    label("loc_34C3")


    ChrTalk(    #156
        0xD,
        (
            "#070F收拾完这个，剩下的\x01",
            "就交给亲卫队吧。\x02\x03",

            "毕竟都市的探索\x01",
            "也渐入佳境了。\x02\x03",

            "接下来应该是将力量放在\x01",
            "身为游击士的本分上了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353F")

    Jump("loc_38A7")

    label("loc_3542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_37B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_364B")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #157
        0xD,
        (
            "#073F哦，你……\x01",
            "应该是乔丝特吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10B,
        "#210F嗯，好久不见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xD,
        (
            "#071F哈哈，想不到\x01",
            "会在这种地方再见到你。\x02\x03",

            "#070F不过情况既然变成这样，\x01",
            "我们就是站在同一船上了。\x02\x03",

            "在这段时间里，\x01",
            "就让我们互相协助吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10B,
        "#210F嗯，我明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x17)
    OP_A2(0x22A7)
    Jump("loc_37B3")

    label("loc_364B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36C2")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #161
        0xD,
        (
            "#070F话说回来，真没想到\x01",
            "我们会在这种地方再见面。\x02\x03",

            "真是的，空之女神\x01",
            "还真喜欢恶作剧啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B3")

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3758")

    ChrTalk(    #162
        0xD,
        (
            "#070F为了方便往来艇尾，\x01",
            "这里听说也要修一条通道。\x02\x03",

            "嗯，的确有通道的话，\x01",
            "施工也会变得比较容易。\x02\x03",

            "好，提起精神，\x01",
            "开始着手进行作业吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_37B3")

    label("loc_3758")


    ChrTalk(    #163
        0xD,
        (
            "#070F为了方便往来艇尾，\x01",
            "这里听说也要修一条通道。\x02\x03",

            "好，提起精神，\x01",
            "开始着手进行作业吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B3")

    Jump("loc_38A7")

    label("loc_37B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_38A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3858")

    ChrTalk(    #164
        0xD,
        (
            "#070F听说要从这里\x01",
            "架一座桥到甲板……\x02\x03",

            "所以在此之前必须先把\x01",
            "这块碎片搬走才行。\x02\x03",

            "你们几个\x01",
            "有空也来帮个忙吧。\x02\x03",

            "再怎么说\x01",
            "我一个人也搞不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_38A7")

    label("loc_3858")


    ChrTalk(    #165
        0xD,
        (
            "#070F听说要先搬走碎片，\x01",
            "然后在这里架一座桥。\x02\x03",

            "你们几个\x01",
            "有空也来帮个忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A7")

    Jump("loc_38CD")

    label("loc_38AA")


    ChrTalk(    #166
        0xD,
        "#070F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_38CD")

    label("loc_38CA")

    Jump("loc_38CD")

    label("loc_38CD")

    TalkEnd(0xFE)
    Return()

    # Function_9_2ECE end

    def Function_10_38D1(): pass

    label("Function_10_38D1")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3932"),
        (1, "loc_3DB2"),
        (2, "loc_3DD2"),
        (SWITCH_DEFAULT, "loc_3DD5"),
    )


    label("loc_3932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_3A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C8")

    ChrTalk(    #167
        0xB,
        (
            "#050F碎片的回收进行得很顺利。\x02\x03",

            "接下来只要解决了那个大零件，\x01",
            "基本的工作就完成了。\x02\x03",

            "好，重新提起精神，\x01",
            "开始着手进行作业吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_3A18")

    label("loc_39C8")


    ChrTalk(    #168
        0xB,
        (
            "#050F碎片的回收进行得很顺利。\x02\x03",

            "只要解决了那个大零件，\x01",
            "基本的工作就完成了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A18")

    Jump("loc_3DAF")

    label("loc_3A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3BFC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AAA")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #169
        0xB,
        (
            "#051F哦，这么快要我帮忙探索了？\x02\x03",

            "设想得挺周到的嘛。\x01",
            "那就一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10B,
        "#210F嘿嘿，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x19)
    OP_A2(0x22A9)
    Jump("loc_3BF9")

    label("loc_3AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B0A")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #171
        0xB,
        (
            "#051F这么快要我帮忙探索，\x01",
            "设想得挺周到的嘛。\x02\x03",

            "那就一起加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF9")

    label("loc_3B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA2")

    ChrTalk(    #172
        0xB,
        (
            "#552F这个机翼倒是还好……\x02\x03",

            "不过横躺在上面的零件，\x01",
            "用普通的办法无法回收啊。\x02\x03",

            "#053F虽然似乎是重要的部分，\x01",
            "不过还是跟老爷子商量看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_3BF9")

    label("loc_3BA2")


    ChrTalk(    #173
        0xB,
        (
            "#053F横躺在上面的零件，\x01",
            "用普通的办法无法回收呢……\x02\x03",

            "待会儿去和\x01",
            "老爷子商量看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF9")

    Jump("loc_3DAF")

    label("loc_3BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3DAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCF")

    ChrTalk(    #174
        0xB,
        (
            "#552F真是的……\x01",
            "大得离谱的碎片啊。\x02\x03",

            "竟然叫我们搬这个东西，\x01",
            "胡乱使唤人也要有个限度啊。\x02\x03",

            "#053F不过，在这种时候\x01",
            "发牢骚也没有意义……\x02\x03",

            "先把在甲板上偷懒的\x01",
            "那个家伙抓来好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_3D09")

    label("loc_3CCF")


    ChrTalk(    #175
        0xB,
        (
            "#552F算了，现在\x01",
            "发牢骚也没用。\x02\x03",

            "只有提起精神做事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D09")

    Jump("loc_3DAF")

    label("loc_3D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D75")

    ChrTalk(    #176
        0xB,
        (
            "#552F真是的……\x01",
            "大得离谱的碎片啊。\x02\x03",

            "竟然叫我们搬这个东西，\x01",
            "胡乱使唤人也要有个限度啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)
    Jump("loc_3DAF")

    label("loc_3D75")


    ChrTalk(    #177
        0xB,
        (
            "#053F算了，现在\x01",
            "发牢骚也没用。\x02\x03",

            "只有提起精神做事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAF")

    Jump("loc_3DD5")

    label("loc_3DB2")


    ChrTalk(    #178
        0xB,
        "#050F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_3DD5")

    label("loc_3DD2")

    Jump("loc_3DD5")

    label("loc_3DD5")

    TalkEnd(0xFE)
    Return()

    # Function_10_38D1 end

    def Function_11_3DD9(): pass

    label("Function_11_3DD9")

    TalkBegin(0xFE)
    Return()

    # Function_11_3DD9 end

    def Function_12_3DDD(): pass

    label("Function_12_3DDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3F30")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3B")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #179
        0xFE,
        "辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "目前正在准备\x01",
            "进行下一项工作！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_3F2D")

    label("loc_3E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDE")

    ChrTalk(    #181
        0xFE,
        (
            "呼，在游击士的协助下，\x01",
            "回收碎片总算还是顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "呀～不过话说回来，\x01",
            "男游击士的力量真惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "和我们这些卖弄力气的\x01",
            "士兵感觉有着天壤之别。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_3F2D")

    label("loc_3EDE")


    ChrTalk(    #184
        0xFE,
        "男游击士的力量真惊人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "和我们这些卖弄力气的\x01",
            "士兵感觉有着天壤之别。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2D")

    Jump("loc_40DD")

    label("loc_3F30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4039")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCC")

    ChrTalk(    #186
        0xFE,
        "哎呀，殿下……！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #187
        0xFE,
        (
            "这、这点程度的碎片，\x01",
            "完全没有任何的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "我们很快就会清理掉的，\x01",
            "请您放心！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x11)
    Jump("loc_4036")

    label("loc_3FCC")

    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #189
        0xFE,
        (
            "赌上王国军亲卫队的名誉，\x01",
            "我们会迅速清理掉碎片的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "请殿下安心地\x01",
            "前往探索吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)

    label("loc_4036")

    Jump("loc_40DD")

    label("loc_4039")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4093")

    ChrTalk(    #191
        0xFE,
        (
            "这、这个\x01",
            "要用人力搬走吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "觉、觉得很难的人，\x01",
            "大概只有我一个吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_40DD")

    label("loc_4093")


    ChrTalk(    #193
        0xFE,
        (
            "我、我们现在要\x01",
            "把这个搬走吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "我、我好像已经\x01",
            "有点头晕目眩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DD")

    TalkEnd(0xFE)
    Return()

    # Function_12_3DDD end

    def Function_13_40E1(): pass

    label("Function_13_40E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4178")

    ChrTalk(    #195
        0xFE,
        "啊，公主殿下……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #196
        0xFE,
        (
            "我们正在工程师的指导下\x01",
            "设置通道当中！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "请再稍微等一些时间\x01",
            "就能完成了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_A2(0x10)
    Jump("loc_41DC")

    label("loc_4178")

    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #198
        0xFE,
        (
            "我们正在工程师的指导下\x01",
            "设置通道当中！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "请再稍微等一些时间\x01",
            "就能完成了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)

    label("loc_41DC")

    Jump("loc_429B")

    label("loc_41DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4243")

    ChrTalk(    #200
        0xFE,
        (
            "嗯～接下来好像\x01",
            "就要在这里建造通道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "清理完碎片之后\x01",
            "得去叫菲小姐过来才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_429B")

    label("loc_4243")


    ChrTalk(    #202
        0xFE,
        (
            "有菲小姐在这里\x01",
            "真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "从焊接到导力引擎的调整，\x01",
            "她实在是无所不能啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_429B")

    TalkEnd(0xFE)
    Return()

    # Function_13_40E1 end

    def Function_14_429F(): pass

    label("Function_14_429F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_43EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4301")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #204
        0xFE,
        "视察辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "修复工作很顺利！\x01",
            "请不用担心！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_43EC")

    label("loc_4301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438E")

    ChrTalk(    #206
        0xFE,
        (
            "嗯～就算是这样的碎片，\x01",
            "要一个人搬运也是绝对办不到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "再怎么说，\x01",
            "这都是金属块啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "呼，再去拜托\x01",
            "游击士来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_43EC")

    label("loc_438E")


    ChrTalk(    #209
        0xFE,
        (
            "就算是这样的碎片，\x01",
            "要一个人搬运也是绝对办不到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "没办法，再去拜托\x01",
            "游击士来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43EC")

    Jump("loc_44D6")

    label("loc_43EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_445B")
    SetChrChipByIndex(0xFE, 21)
    SetChrSubChip(0xFE, 0)

    ChrTalk(    #211
        0xFE,
        (
            "这样的碎片\x01",
            "根本就不算什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "马上就会清理掉的，\x01",
            "请不用担心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Jump("loc_44D6")

    label("loc_445B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B1")

    ChrTalk(    #213
        0xFE,
        (
            "接、接下来要\x01",
            "搬动这块碎片吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "尤、尤莉亚上尉也\x01",
            "真会乱来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_44D6")

    label("loc_44B1")


    ChrTalk(    #215
        0xFE,
        (
            "接、接下来要\x01",
            "搬动这块碎片吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D6")

    TalkEnd(0xFE)
    Return()

    # Function_14_429F end

    def Function_15_44DA(): pass

    label("Function_15_44DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4579")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4535")

    ChrTalk(    #216
        0xFE,
        (
            "支架的回收\x01",
            "看来要放到最后了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "如果赶得上\x01",
            "修复就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4576")

    label("loc_4535")


    ChrTalk(    #218
        0xFE,
        (
            "支架的回收\x01",
            "看来要放到最后了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "如果赶得上修复就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_4576")

    Jump("loc_46A1")

    label("loc_4579")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45FF")

    ChrTalk(    #220
        0xFE,
        (
            "哎呀，公主殿下……\x01",
            "您要出发了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "您回来的时候，\x01",
            "这里应该已经造好一座桥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "总之请您期待吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_4648")

    label("loc_45FF")


    ChrTalk(    #223
        0xFE,
        (
            "殿下您回来的时候，\x01",
            "这里应该已经造好一座桥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "总之请您期待吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4648")

    Jump("loc_46A1")

    label("loc_464B")


    ChrTalk(    #225
        0xFE,
        (
            "唔唔～……\x01",
            "近看的话还真是巨大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "不拿出相当的气势的话，\x01",
            "看来是动不了它的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A1")

    TalkEnd(0xFE)
    Return()

    # Function_15_44DA end

    def Function_16_46A5(): pass

    label("Function_16_46A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_46B2")
    Jump("loc_4C3F")

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_47BD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4742")

    ChrTalk(    #227
        0x12,
        (
            "#270F大到这种程度的话，\x01",
            "光靠人力是动不了的吧。\x02\x03",

            "可是，辅助飞翔引擎\x01",
            "只有单翼是靠不住的……\x02\x03",

            "必须想出一个\x01",
            "回收的办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BA")

    label("loc_4742")


    ChrTalk(    #228
        0x12,
        (
            "#270F大到这种程度的话，\x01",
            "光靠人力是动不了的。\x02\x03",

            "可是，辅助飞翔引擎\x01",
            "只有单翼是靠不住的……\x02\x03",

            "必须想出一个\x01",
            "回收的办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BA")

    Jump("loc_4C3F")

    label("loc_47BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4C38")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x455, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4920")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #229
        0x12,
        (
            "#270F嗯……\x01",
            "你就是空贼团的小丫头吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x10B,
        (
            "#212F你、你真没礼貌。\x01",
            "什么小丫头啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x12,
        (
            "#270F把小丫头叫做小丫头，\x01",
            "完全没有什么不妥的地方。\x02\x03",

            "我先声明……\x01",
            "为了你好，你可别太得意忘形。\x02\x03",

            "你能够待在这里，\x01",
            "是因为现在是非常时期。\x01",
            "你可要谨记在心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x10B,
        "#214F我、我当然知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x12,
        (
            "#272F那就好……\x02\x03",

            "你就尽量努力地干活吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C)
    OP_A2(0x22AC)
    Jump("loc_4C35")

    label("loc_4920")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4997")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #234
        0x12,
        (
            "#270F你就尽量努力地干活吧。\x02\x03",

            "你能够待在这里，\x01",
            "是因为现在是非常时期。\x01",
            "你可要谨记在心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C35")

    label("loc_4997")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A10")

    ChrTalk(    #235
        0x12,
        (
            "#270F奥利维尔说的话，\x01",
            "你们当作没听到就好了。\x02\x03",

            "现在正是让他了解到\x01",
            "劳动的价值的绝佳机会。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)
    Jump("loc_4A58")

    label("loc_4A10")


    ChrTalk(    #236
        0x12,
        (
            "#270F那家伙说的话，\x01",
            "你们当作没听到就好了。\x02\x03",

            "别在意，尽管去探索吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A58")

    Jump("loc_4C35")

    label("loc_4A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BBF")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(    #237
        0x12,
        (
            "#276F接下来就要开始\x01",
            "回收碎片了……\x02\x03",

            "#270F这里如果没你这家伙的话\x01",
            "会让人无比遗憾的，奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x104,
        (
            "#035F呵呵，体力劳动虽然也不错，\x01",
            "但不巧的是我正好有重要的使命。\x02\x03",

            "下次有机会再让我\x01",
            "学习劳动的珍贵吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x12,
        (
            "#274F一旦知道和自己没关系\x01",
            "就耍起嘴皮子来了……\x02\x03",

            "艾丝蒂尔，如果你改变心意，\x01",
            "随时都可以把他换下来。\x02\x03",

            "这次我会负责\x01",
            "好好照顾他的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)
    Jump("loc_4C35")

    label("loc_4BBF")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #240
        0x12,
        (
            "#270F艾丝蒂尔，如果你改变心意，\x01",
            "随时都可以把奥利维尔换下来。\x02\x03",

            "我必须让那家伙亲身\x01",
            "体验一下劳动的价值才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C35")

    Jump("loc_4C3F")

    label("loc_4C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4C3F")

    label("loc_4C3F")

    TalkEnd(0xFE)
    Return()

    # Function_16_46A5 end

    def Function_17_4C43(): pass

    label("Function_17_4C43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CE8")

    ChrTalk(    #241
        0xFE,
        (
            "舰内马上就要开始进行\x01",
            "飞翔引擎的最终检查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "调整应该是完美无缺才对，\x01",
            "不过心中还是有些许的不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "所以我才跑到\x01",
            "外面来看看情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_4D4E")

    label("loc_4CE8")


    ChrTalk(    #244
        0xFE,
        (
            "舰内马上就要开始进行\x01",
            "飞翔引擎的最终检查了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "接着只要能回收左舷部的话，\x01",
            "飞行准备就完成了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D4E")

    Jump("loc_5150")

    label("loc_4D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4E72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E08")

    ChrTalk(    #246
        0xFE,
        (
            "不过飞翔引擎的调节是马虎不得的，\x01",
            "所以得跟舵手好好讨论一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "因为最后操纵飞船的是他们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "从直接责任这个意义上来说，\x01",
            "他们的工作比舰长更有压力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_4E6F")

    label("loc_4E08")


    ChrTalk(    #249
        0xFE,
        (
            "不过飞翔引擎的调节是马虎不得的，\x01",
            "所以得跟舵手好好讨论一下才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "因为实际操纵飞船的是他们啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4E6F")

    Jump("loc_5150")

    label("loc_4E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F59")

    ChrTalk(    #251
        0xFE,
        (
            "这突出在舷外的部分\x01",
            "称为支架……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "是搭载着辅助\x01",
            "飞翔引擎的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "本来的话是左右各有一组，\x01",
            "用以保持舰体平衡\x01",
            "的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "不巧的是左舷\x01",
            "被切断了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "为了预防最坏的情况，\x01",
            "必须尽可能事先做些准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_4FC8")

    label("loc_4F59")


    ChrTalk(    #256
        0xFE,
        (
            "总之我决定开始\x01",
            "调整右舷的辅助引擎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "的确是项很难的工作，\x01",
            "不过接下来也正好可以\x01",
            "展示出我维修员的实力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC8")

    Jump("loc_5150")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BA")

    ChrTalk(    #258
        0xFE,
        (
            "看来这个安定翼\x01",
            "好像没有异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "还真能承受住冲击呢。\x01",
            "也因此省下了修理的功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "那么，接下来要去\x01",
            "检查支架才行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "……所谓的支架，\x01",
            "就是突出在舷外的舰体部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "它收纳了各种辅助飞翔引擎，\x01",
            "是个很重要的部位。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_5150")

    label("loc_50BA")


    ChrTalk(    #263
        0xFE,
        (
            "所谓的支架，\x01",
            "就是突出在舷外的舰体部分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "它收纳了各种辅助飞翔引擎，\x01",
            "是个很重要的部位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "这次左舷的支架\x01",
            "整个都脱落了呢。\x01",
            "难怪会坠落下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5150")

    TalkEnd(0xFE)
    Return()

    # Function_17_4C43 end

    def Function_18_5154(): pass

    label("Function_18_5154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_517B")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_5196")

    label("loc_517B")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_5196")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5231")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51E8")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -17120, 3500, 23510, 135)

    label("loc_51E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_520B")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20610, 0, 16960, 315)

    label("loc_520B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_522E")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -23120, 0, 16149, 0)

    label("loc_522E")

    Jump("loc_537C")

    label("loc_5231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_525C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4310, -4000, 22130, 315)

    label("loc_525C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_526E")
    ClearChrFlags(0x17, 0x80)

    label("loc_526E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5291")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 5070, -3880, 23930, 270)

    label("loc_5291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52B4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_52B4")

    Jump("loc_537C")

    label("loc_52B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5308")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52E2")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 34850, -4000, 16079, 225)

    label("loc_52E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5305")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 11730, -4000, 18510, 90)

    label("loc_5305")

    Jump("loc_537C")

    label("loc_5308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_534E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_534E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -18510, 3500, 22430, 180)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_534E")
    SetChrFlags(0x8, 0x10)

    label("loc_534E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_537C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_537C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -43550, 5000, 31240, 225)

    label("loc_537C")

    OP_0D()
    Return()

    # Function_18_5154 end

    def Function_19_537E(): pass

    label("Function_19_537E")

    EventBegin(0x0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_D2(0x260222, 0x260227, 0x15)
    OP_D2(0x6007C, 0x60081, 0x16)
    OP_D2(0x260068, 0x26006D, 0x17)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    OP_6D(58350, -4000, 15070, 0)
    OP_67(0, 9860, -10000, 0)
    OP_6B(4650, 0)
    OP_6C(310000, 0)
    OP_6E(684, 0)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -20700, 3500, 24660, 180)
    SetChrPos(0xC, -22360, 3500, 24090, 225)
    SetChrPos(0xB, -22990, 3500, 24700, 180)
    SetChrPos(0xD, -22150, 3500, 28290, 90)
    SetChrPos(0x102, -21110, 3500, 26540, 135)
    SetChrPos(0xA, -19850, 3500, 23160, 180)
    SetChrPos(0x8, -18490, 3500, 26100, 135)
    SetChrPos(0x9, -17510, 3500, 28380, 45)
    SetChrPos(0xE, -19700, 3500, 25650, 90)
    SetChrPos(0xF, -22180, 3500, 25600, 0)
    SetChrPos(0x13, -18800, 3500, 23370, 0)
    SetChrPos(0x12, -18590, 3500, 27820, 0)
    SetChrPos(0x10, -20780, 3500, 28750, 0)
    SetChrPos(0x11, -19600, 3500, 28870, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    FadeToBright(2000, 0)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 30)

    def lambda_5570():
        OP_6D(-55380, -4000, 35510, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5570)

    def lambda_5588():
        OP_67(0, 8530, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5588)

    def lambda_55A0():
        OP_6E(662, 11000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55A0)
    OP_A2(0x0)
    OP_43(0x101, 0x1, 0x0, 0x14)
    OP_43(0x11, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    OP_43(0xD, 0x1, 0x0, 0x18)
    OP_43(0xA, 0x1, 0x0, 0x14)
    Sleep(100)
    OP_43(0xF, 0x1, 0x0, 0x1A)
    OP_43(0x10, 0x1, 0x0, 0x1B)
    OP_43(0x8, 0x1, 0x0, 0x17)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0xB, 0x1, 0x0, 0x15)
    OP_43(0x13, 0x1, 0x0, 0x16)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0xC, 0x1, 0x0, 0x14)
    OP_43(0x9, 0x1, 0x0, 0x19)
    OP_C8(0x80, 0x172, "C_PLAC25._CH", 0x1, 0x9C4)
    Sleep(8000)
    OP_A3(0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x2)
    Fade(500)
    OP_6D(-20600, 3500, 26640, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(339000, 0)
    OP_6E(392, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #266
        0x101,
        "#1020F#5P这、这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xC,
        "#560F#5P哇……好漂亮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x11,
        (
            "#151F#5P这、这回一定要\x01",
            "拍啊拍啊拍个够～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 22)
    OP_0D()
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 225, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 90, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8C(0x11, 0, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_8C(0x10, 135, 400)
    Sleep(300)

    ChrTalk(    #269
        0x10,
        (
            "#142F#5P喂喂……\x01",
            "别用完感光结晶回路啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #270
        0xE,
        (
            "#1063F#5P不过这里……\x01",
            "还真是个不得了的世外桃源呢。\x02\x03",

            "与其说是城市\x01",
            "不如称为庭园比较恰当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x102,
        (
            "#1043F#5P是啊……\x02\x03",

            "#1042F可能是大城市里\x01",
            "类似公园之类的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        (
            "#1007F#6P确、确实有这种感觉……\x02\x03",

            "#1019F而且，同样的景致\x01",
            "还一直延续到远处……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x9,
        (
            "#035F#6P哟哟……\x01",
            "真是令人无法想象的规模呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #274
        0x101,
        "#1004F#5P基库！？\x02",
    )

    CloseMessageWindow()

    def lambda_59E4():
        OP_6D(-23900, 3500, 19660, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59E4)
    SetChrPos(0x14, -28880, 6500, 7610, 45)
    ClearChrFlags(0x14, 0x80)

    def lambda_5A12():

        label("loc_5A12")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A12")

    QueueWorkItem2(0xA, 1, lambda_5A12)
    Sleep(50)

    def lambda_5A28():

        label("loc_5A28")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A28")

    QueueWorkItem2(0x102, 1, lambda_5A28)

    def lambda_5A39():

        label("loc_5A39")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A39")

    QueueWorkItem2(0x8, 1, lambda_5A39)
    Sleep(50)

    def lambda_5A4F():

        label("loc_5A4F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A4F")

    QueueWorkItem2(0x101, 1, lambda_5A4F)

    def lambda_5A60():

        label("loc_5A60")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A60")

    QueueWorkItem2(0x9, 1, lambda_5A60)
    Sleep(50)

    def lambda_5A76():

        label("loc_5A76")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A76")

    QueueWorkItem2(0xC, 1, lambda_5A76)

    def lambda_5A87():

        label("loc_5A87")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A87")

    QueueWorkItem2(0xE, 1, lambda_5A87)

    def lambda_5A98():

        label("loc_5A98")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A98")

    QueueWorkItem2(0x12, 1, lambda_5A98)
    Sleep(50)

    def lambda_5AAE():

        label("loc_5AAE")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AAE")

    QueueWorkItem2(0xB, 1, lambda_5AAE)

    def lambda_5ABF():

        label("loc_5ABF")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5ABF")

    QueueWorkItem2(0xF, 1, lambda_5ABF)

    def lambda_5AD0():

        label("loc_5AD0")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AD0")

    QueueWorkItem2(0x10, 1, lambda_5AD0)
    Sleep(50)

    def lambda_5AE6():

        label("loc_5AE6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AE6")

    QueueWorkItem2(0xD, 1, lambda_5AE6)

    def lambda_5AF7():

        label("loc_5AF7")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_5AF7")

    QueueWorkItem2(0x13, 1, lambda_5AF7)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 9)

    def lambda_5B12():

        label("loc_5B12")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B12")

    QueueWorkItem2(0x11, 1, lambda_5B12)
    WaitChrThread(0x101, 0x2)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_5B2D():
        OP_8E(0xFE, 0xFFFFB078, 0x157C, 0x5262, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5B2D)
    Sleep(500)

    def lambda_5B4D():
        OP_6D(-20680, 3500, 25150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B4D)
    WaitChrThread(0x14, 0x1)
    OP_43(0x14, 0x1, 0x0, 0x1C)
    WaitChrThread(0x101, 0x2)
    OP_8E(0x14, 0xFFFFB154, 0x1194, 0x5942, 0xBB8, 0x0)
    OP_8C(0x14, 180, 400)
    OP_8F(0x14, 0xFFFFB154, 0xE74, 0x5942, 0x3E8, 0x0)
    OP_A3(0x1)
    Fade(500)
    OP_44(0xA, 0x1)
    SetChrPos(0x14, -19850, 3800, 23160, 0)
    SetChrFlags(0x14, 0x80)
    SetChrSubChip(0xA, 5)
    SetChrChipByIndex(0xA, 21)

    def lambda_5BD1():

        label("loc_5BD1")

        OP_8C(0xFE, 315, 400)
        OP_48()
        Jump("loc_5BD1")

    QueueWorkItem2(0x13, 1, lambda_5BD1)
    OP_0D()

    ChrTalk(    #275
        0x14,
        "#311F#5P啾啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        (
            "#1165F#2P太好了……\x01",
            "我还以为和你失散了呢。\x02\x03",

            "#1168F不要紧……我们也没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x14,
        (
            "#311F#5P啾⊙\x02\x03",

            "#310F啾！\x02\x03",

            "啾啾啾！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xA,
        "#1167F#2P是吗……我知道了。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x20)
    SetChrSubChip(0xA, 3)
    OP_8C(0xA, 0, 400)
    ClearChrFlags(0xA, 0x20)
    Sleep(300)

    ChrTalk(    #279
        0xA,
        (
            "#1162F#6P看来我们迫降到了\x01",
            "浮游都市的最西面。\x02\x03",

            "而且『古罗力亚斯』\x01",
            "正好停泊在\x01",
            "反方向的东边尽头呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0311   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_19_537E end

    def Function_20_5D25(): pass

    label("Function_20_5D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D47")
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    OP_8C(0xFE, 225, 400)
    Sleep(1200)
    Jump("Function_20_5D25")

    label("loc_5D47")

    Return()

    # Function_20_5D25 end

    def Function_21_5D48(): pass

    label("Function_21_5D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D6A")
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    Jump("Function_21_5D48")

    label("loc_5D6A")

    Return()

    # Function_21_5D48 end

    def Function_22_5D6B(): pass

    label("Function_22_5D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D8D")
    OP_8C(0xFE, 45, 400)
    Sleep(1300)
    OP_8C(0xFE, 135, 400)
    Sleep(1300)
    Jump("Function_22_5D6B")

    label("loc_5D8D")

    Return()

    # Function_22_5D6B end

    def Function_23_5D8E(): pass

    label("Function_23_5D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5DB0")
    OP_8C(0xFE, 225, 400)
    Sleep(1800)
    OP_8C(0xFE, 135, 400)
    Sleep(1800)
    Jump("Function_23_5D8E")

    label("loc_5DB0")

    Return()

    # Function_23_5D8E end

    def Function_24_5DB1(): pass

    label("Function_24_5DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5DD3")
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    Jump("Function_24_5DB1")

    label("loc_5DD3")

    Return()

    # Function_24_5DB1 end

    def Function_25_5DD4(): pass

    label("Function_25_5DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5DF6")
    OP_8C(0xFE, 180, 400)
    Sleep(1200)
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    Jump("Function_25_5DD4")

    label("loc_5DF6")

    Return()

    # Function_25_5DD4 end

    def Function_26_5DF7(): pass

    label("Function_26_5DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E19")
    OP_8C(0xFE, 45, 400)
    Sleep(1300)
    OP_8C(0xFE, 180, 400)
    Sleep(1300)
    Jump("Function_26_5DF7")

    label("loc_5E19")

    Return()

    # Function_26_5DF7 end

    def Function_27_5E1A(): pass

    label("Function_27_5E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E3C")
    OP_8C(0xFE, 90, 400)
    Sleep(1200)
    OP_8C(0xFE, 45, 400)
    Sleep(1200)
    Jump("Function_27_5E1A")

    label("loc_5E3C")

    Return()

    # Function_27_5E1A end

    def Function_28_5E3D(): pass

    label("Function_28_5E3D")

    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 23)

    label("loc_5E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5E5A")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_5E47")

    label("loc_5E5A")

    Return()

    # Function_28_5E3D end

    def Function_29_5E5B(): pass

    label("Function_29_5E5B")

    SetMapFlags(0x2000000)
    Return()

    # Function_29_5E5B end

    def Function_30_5E61(): pass

    label("Function_30_5E61")

    ClearMapFlags(0x2000000)
    Return()

    # Function_30_5E61 end

    SaveToFile()

Try(main)

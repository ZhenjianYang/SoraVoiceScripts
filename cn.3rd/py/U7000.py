from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7000   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7000.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/U7000   ._SN',
            'ED6_DT21/U7000_1 ._SN',
            'ED6_DT21/U7000_2 ._SN',
            'ED6_DT21/U7000_3 ._SN',
            'ED6_DT21/U7000_4 ._SN',
            'ED6_DT21/U7000_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '封印石用暂定物体',                     # 9
        '提妲',                                 # 10
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 11
        '穆拉',                                 # 12
        '乔丝特',                               # 13
        '约修亚',                               # 14
        '科洛丝',                               # 15
        '基库',                                 # 16
        '奥利维尔',                             # 17
        '金',                                   # 18
        '亚妮拉丝',                             # 19
        '雪拉扎德',                             # 20
        '阿加特',                               # 21
        '艾丝蒂尔',                             # 22
        '理查德',                               # 23
        '玲',                                   # 24
        '莉丝',                                 # 25
        '凯文',                                 # 26
        '赛雷斯托',                             # 27
        '',                                     # 28
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02891 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03150 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT27/CH03250 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT27/CH03000 ._CH',             # 0F
        'ED6_DT07/CH02030 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT07/CH02760 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH02891P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03150P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT27/CH03250P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT27/CH03000P._CP',             # 0F
        'ED6_DT07/CH02030P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT07/CH02760P._CP',             # 12
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
    )


    DeclEvent(
        X                   = -3130,
        Y                   = -1000,
        Z                   = -25960,
        Range               = 2560,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFAD12,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -32520,
        Y                   = 0,
        Z                   = -33320,
        Range               = 4000,
        Unknown_10          = 0x6590,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 33060,
        Y                   = 0,
        Z                   = -34510,
        Range               = 4000,
        Unknown_10          = 0x6978,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -3550,
        Y                   = 10000,
        Z                   = 34560,
        Range               = 3210,
        Unknown_10          = 0x3A98,
        Unknown_14          = 0x9696,
        Unknown_18          = 0x10000,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -3070,
        Y                   = 2000,
        Z                   = -19730,
        Range               = 2940,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0xFFFFC374,
        Unknown_18          = 0x10000,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = -15750,
        Y                   = 1500,
        Z                   = -13530,
        Range               = 4000,
        Unknown_10          = 0x1450,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = 16270,
        Y                   = 1500,
        Z                   = -13650,
        Range               = 4000,
        Unknown_10          = 0x157C,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 19,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 4150,
        TriggerY            = 6300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 5500,
        ActorY              = 6300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 12000,
        TriggerY            = 35000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 13500,
        ActorY              = 35000,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4EA",          # 00, 0
        "Function_1_A31",          # 01, 1
        "Function_2_B1D",          # 02, 2
        "Function_3_C02",          # 03, 3
        "Function_4_DD7",          # 04, 4
        "Function_5_1063",         # 05, 5
        "Function_6_1070",         # 06, 6
        "Function_7_14C0",         # 07, 7
        "Function_8_156B",         # 08, 8
        "Function_9_1A7F",         # 09, 9
        "Function_10_1A8F",        # 0A, 10
        "Function_11_1B18",        # 0B, 11
        "Function_12_1B97",        # 0C, 12
        "Function_13_1BF2",        # 0D, 13
        "Function_14_1C4D",        # 0E, 14
        "Function_15_1CCF",        # 0F, 15
        "Function_16_1D51",        # 10, 16
        "Function_17_1E3B",        # 11, 17
        "Function_18_1F14",        # 12, 18
        "Function_19_202A",        # 13, 19
        "Function_20_2078",        # 14, 20
    )


    def Function_0_4EA(): pass

    label("Function_0_4EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_509")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_502"),
        (SWITCH_DEFAULT, "loc_509"),
    )


    label("loc_502")

    Event(0, 16)
    Jump("loc_509")

    label("loc_509")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_619")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_529"),
        (101, "loc_579"),
        (102, "loc_5C9"),
        (SWITCH_DEFAULT, "loc_619"),
    )


    label("loc_529")

    SetChrPos(0x0, 130, 1000, -20490, 0)
    SetChrPos(0x1, 130, 1000, -20490, 0)
    SetChrPos(0x2, 130, 1000, -20490, 0)
    SetChrPos(0x3, 130, 1000, -20490, 0)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_619")

    label("loc_579")

    SetChrPos(0x0, -14920, 1000, -13460, 45)
    SetChrPos(0x1, -14920, 1000, -13460, 45)
    SetChrPos(0x2, -14920, 1000, -13460, 45)
    SetChrPos(0x3, -14920, 1000, -13460, 45)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_619")

    label("loc_5C9")

    SetChrPos(0x0, 15210, 1000, -13240, 315)
    SetChrPos(0x1, 15210, 1000, -13240, 315)
    SetChrPos(0x2, 15210, 1000, -13240, 315)
    SetChrPos(0x3, 15210, 1000, -13240, 315)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_619")

    label("loc_619")

    Call(0, 8)
    Call(0, 6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_645")
    Event(1, 5)

    label("loc_645")

    Jump("loc_72E")

    label("loc_648")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66B")
    Event(1, 24)
    Jump("loc_683")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_683")
    Event(1, 8)

    label("loc_683")

    Jump("loc_72E")

    label("loc_686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A9")
    Event(1, 25)
    Jump("loc_6C1")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C1")
    Event(1, 11)

    label("loc_6C1")

    Jump("loc_72E")

    label("loc_6C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EE")
    Event(5, 22)

    label("loc_6EE")

    Jump("loc_72E")

    label("loc_6F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71E")
    Event(5, 19)
    Jump("loc_72E")

    label("loc_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    Event(1, 28)

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_754")
    OP_A3(0x2506)
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(4, 16)
    Jump("loc_9B4")

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_A3(0x2505)
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(4, 3)
    Jump("loc_9B4")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A0")
    OP_A3(0x2505)
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(4, 2)
    Jump("loc_9B4")

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BD")
    OP_A3(0x2505)
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    Event(3, 17)
    Jump("loc_9B4")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DA")
    OP_A3(0x2505)
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(3, 13)
    Jump("loc_9B4")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_A3(0x2505)
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(3, 11)
    Jump("loc_9B4")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81D")
    OP_A3(0x2504)
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(3, 9)
    Jump("loc_9B4")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83A")
    OP_A3(0x2504)
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    Event(3, 2)
    Jump("loc_9B4")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_857")
    OP_A3(0x2504)
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    Event(2, 13)
    Jump("loc_9B4")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_874")
    OP_A3(0x2504)
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    Event(2, 9)
    Jump("loc_9B4")

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_891")
    OP_A3(0x2504)
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(2, 6)
    Jump("loc_9B4")

    label("loc_891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B7")
    OP_A3(0x2504)
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(2, 5)
    Jump("loc_9B4")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D4")
    OP_A3(0x2504)
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(2, 3)
    Jump("loc_9B4")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_8F3")
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(2, 2)
    Jump("loc_9B4")

    label("loc_8F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_909")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    Event(1, 40)
    Jump("loc_9B4")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_91F")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    Event(1, 38)
    Jump("loc_9B4")

    label("loc_91F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_935")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    Event(1, 35)
    Jump("loc_9B4")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_954")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 33)
    Jump("loc_9B4")

    label("loc_954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_96A")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(1, 32)
    Jump("loc_9B4")

    label("loc_96A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_980")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(1, 29)
    Jump("loc_9B4")

    label("loc_980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_99F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 15)
    Jump("loc_9B4")

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B4")
    SetMapFlags(0x10000000)
    Event(1, 2)

    label("loc_9B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DC")
    Event(4, 15)
    Return()

    label("loc_9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F8")
    Event(4, 14)
    Return()

    label("loc_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A14")
    Event(4, 13)
    Return()

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A30")
    Event(4, 12)
    Return()

    label("loc_A30")

    Return()

    # Function_0_4EA end

    def Function_1_A31(): pass

    label("Function_1_A31")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_A61")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A93")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_AA0")
    OP_C4(0x0, 0x200)

    label("loc_AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_END)), "loc_AAF")
    OP_1B(0x3, 0x0, 0x11)
    Jump("loc_AB2")

    label("loc_AAF")

    OP_10(0x3, 0x0)

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABD")
    OP_82(0x81, 0x0)

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_END)), "loc_AC7")
    Jump("loc_AD4")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_END)), "loc_AD4")
    OP_72(0x400, 0x0)
    ExitThread()

    label("loc_AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFC")
    OP_64(0x0, 0x1)
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_END)), "loc_B0A")
    OP_64(0x1, 0x1)
    Jump("loc_B18")

    label("loc_B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_END)), "loc_B14")
    Jump("loc_B18")

    label("loc_B14")

    OP_64(0x1, 0x1)

    label("loc_B18")

    Call(0, 10)
    Return()

    # Function_1_A31 end

    def Function_2_B1D(): pass

    label("Function_2_B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2E")
    Call(1, 21)
    Return()

    label("loc_B2E")

    OP_AA(0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x352, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x353, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x354, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x355, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x356, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x357, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x358, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x359, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x35F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x360, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x361, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BFD")
    Call(0, 4)
    Jump("loc_C01")

    label("loc_BFD")

    Call(0, 3)

    label("loc_C01")

    Return()

    # Function_2_B1D end

    def Function_3_C02(): pass

    label("Function_3_C02")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_C2F")

    label("loc_C2F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB6")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_C94")

    label("loc_C94")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CAC"),
        (1, "loc_D3E"),
        (2, "loc_D72"),
        (SWITCH_DEFAULT, "loc_DA6"),
    )


    label("loc_CAC")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_D1C")
    OP_1D(0xD5)
    SetMapFlags(0x2000000)
    Jump("loc_D1E")

    label("loc_D1C")

    OP_1D(0xD2)

    label("loc_D1E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB3")

    label("loc_D3E")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0xA)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_D6F")

    label("loc_D6F")

    Jump("loc_DB3")

    label("loc_D72")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_DA3")

    label("loc_DA3")

    Jump("loc_DB3")

    label("loc_DA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DB3")

    label("loc_DB3")

    Jump("loc_C42")

    label("loc_DB6")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_3_C02 end

    def Function_4_DD7(): pass

    label("Function_4_DD7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #3
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_E04")

    label("loc_E04")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1042")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "解放封印石\x01",          # 0
            "回复ＨＰ·ＥＰ\x01",      # 1
            "获得武具\x01",            # 2
            "合成结晶回路\x01",        # 3
            "结束\x01",                # 4
        )
    )

    Jump("loc_E74")

    label("loc_E74")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E90"),
        (1, "loc_F3A"),
        (2, "loc_FCA"),
        (3, "loc_FFE"),
        (SWITCH_DEFAULT, "loc_1032"),
    )


    label("loc_E90")

    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB8")
    Call(1, 31)
    Jump("loc_F2D")

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC7")
    Call(1, 34)
    Jump("loc_F2D")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED6")
    Call(1, 37)
    Jump("loc_F2D")

    label("loc_ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE5")
    Call(1, 39)
    Jump("loc_F2D")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF4")
    Call(2, 10)
    Jump("loc_F2D")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F03")
    Call(2, 11)
    Jump("loc_F2D")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F12")
    Call(2, 12)
    Jump("loc_F2D")

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F21")
    Call(3, 10)
    Jump("loc_F2D")

    label("loc_F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2D")
    Call(3, 12)

    label("loc_F2D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103F")

    label("loc_F3A")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(3500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_FA8")
    OP_1D(0xD5)
    SetMapFlags(0x2000000)
    Jump("loc_FAA")

    label("loc_FA8")

    OP_1D(0xD2)

    label("loc_FAA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103F")

    label("loc_FCA")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0xA)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #4
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_FFB")

    label("loc_FFB")

    Jump("loc_103F")

    label("loc_FFE")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A9(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #5
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_102F")

    label("loc_102F")

    Jump("loc_103F")

    label("loc_1032")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103F")

    label("loc_103F")

    Jump("loc_E17")

    label("loc_1042")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFF)
    Return()

    # Function_4_DD7 end

    def Function_5_1063(): pass

    label("Function_5_1063")

    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    Return()

    # Function_5_1063 end

    def Function_6_1070(): pass

    label("Function_6_1070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_14BF")
    OP_43(0x21, 0x0, 0x6, 0x2)
    OP_43(0x12, 0x0, 0x6, 0x2)
    OP_43(0x13, 0x0, 0x6, 0x2)
    OP_43(0x16, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EA")
    SetChrPos(0x13, 5860, 4000, -9280, 180)
    SetChrPos(0x12, 6050, 4000, -11760, 0)
    Jump("loc_1257")

    label("loc_10EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1133")
    SetChrPos(0x13, 5860, 4000, -9280, 180)
    SetChrPos(0x21, 6050, 4000, -11760, 0)
    Jump("loc_1257")

    label("loc_1133")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117C")
    SetChrPos(0x12, 5860, 4000, -9280, 180)
    SetChrPos(0x21, 6050, 4000, -11760, 0)
    Jump("loc_1257")

    label("loc_117C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B4")
    SetChrPos(0x13, 5860, 4000, -9280, 180)
    Jump("loc_1257")

    label("loc_11B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11EC")
    SetChrPos(0x21, 5860, 4000, -9280, 180)
    Jump("loc_1257")

    label("loc_11EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1224")
    SetChrPos(0x12, 5860, 4000, -9280, 180)
    Jump("loc_1257")

    label("loc_1224")

    SetChrPos(0x12, 4280, 4000, -10900, 45)
    SetChrPos(0x21, 5860, 4000, -9280, 180)
    SetChrPos(0x13, 6050, 4000, -11760, 0)

    label("loc_1257")

    Jump("loc_14BF")

    label("loc_125A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1292")
    SetChrPos(0x16, 8000, 4000, -10850, 327)
    Jump("loc_14BF")

    label("loc_1292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EC")
    SetChrPos(0x13, 5860, 4000, -9280, 153)
    SetChrPos(0x12, 6050, 4000, -11760, 0)
    SetChrPos(0x16, 8000, 4000, -10850, 270)
    Jump("loc_14BF")

    label("loc_12EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1346")
    SetChrPos(0x13, 5860, 4000, -9280, 153)
    SetChrPos(0x21, 6050, 4000, -11760, 0)
    SetChrPos(0x16, 8000, 4000, -10850, 270)
    Jump("loc_14BF")

    label("loc_1346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A0")
    SetChrPos(0x12, 5860, 4000, -9280, 153)
    SetChrPos(0x21, 6050, 4000, -11760, 0)
    SetChrPos(0x16, 8000, 4000, -10850, 270)
    Jump("loc_14BF")

    label("loc_13A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E9")
    SetChrPos(0x13, 5860, 4000, -9280, 130)
    SetChrPos(0x16, 8000, 4000, -10850, 310)
    Jump("loc_14BF")

    label("loc_13E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1432")
    SetChrPos(0x21, 5860, 4000, -9280, 130)
    SetChrPos(0x16, 8000, 4000, -10850, 310)
    Jump("loc_14BF")

    label("loc_1432")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147B")
    SetChrPos(0x12, 5860, 4000, -9280, 130)
    SetChrPos(0x16, 8000, 4000, -10850, 310)
    Jump("loc_14BF")

    label("loc_147B")

    SetChrPos(0x12, 4280, 4000, -10900, 45)
    SetChrPos(0x21, 5860, 4000, -9280, 180)
    SetChrPos(0x13, 6050, 4000, -11760, 0)
    SetChrPos(0x16, 8000, 4000, -10850, 270)

    label("loc_14BF")

    Return()

    # Function_6_1070 end

    def Function_7_14C0(): pass

    label("Function_7_14C0")

    Call(0, 8)
    Call(0, 6)
    Call(0, 9)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1516")
    Call(4, 15)
    Return()

    label("loc_1516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1532")
    Call(4, 14)
    Return()

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154E")
    Call(4, 13)
    Return()

    label("loc_154E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    Call(4, 12)
    Return()

    label("loc_156A")

    Return()

    # Function_7_14C0 end

    def Function_8_156B(): pass

    label("Function_8_156B")

    OP_C0(0x23, 0x21, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x21, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E4")
    SetChrFlags(0x11, 0x80)
    Jump("loc_18E9")

    label("loc_18E4")

    ClearChrFlags(0x11, 0x80)

    label("loc_18E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18FF")
    SetChrFlags(0x12, 0x80)
    Jump("loc_1904")

    label("loc_18FF")

    ClearChrFlags(0x12, 0x80)

    label("loc_1904")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_191A")
    SetChrFlags(0x13, 0x80)
    Jump("loc_191F")

    label("loc_191A")

    ClearChrFlags(0x13, 0x80)

    label("loc_191F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1935")
    SetChrFlags(0x14, 0x80)
    Jump("loc_193A")

    label("loc_1935")

    ClearChrFlags(0x14, 0x80)

    label("loc_193A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1950")
    SetChrFlags(0x15, 0x80)
    Jump("loc_1955")

    label("loc_1950")

    ClearChrFlags(0x15, 0x80)

    label("loc_1955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_196B")
    SetChrFlags(0x16, 0x80)
    Jump("loc_1970")

    label("loc_196B")

    ClearChrFlags(0x16, 0x80)

    label("loc_1970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1986")
    SetChrFlags(0x18, 0x80)
    Jump("loc_198B")

    label("loc_1986")

    ClearChrFlags(0x18, 0x80)

    label("loc_198B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A1")
    SetChrFlags(0x19, 0x80)
    Jump("loc_19A6")

    label("loc_19A1")

    ClearChrFlags(0x19, 0x80)

    label("loc_19A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BC")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_19C1")

    label("loc_19BC")

    ClearChrFlags(0x1A, 0x80)

    label("loc_19C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D7")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_19DC")

    label("loc_19D7")

    ClearChrFlags(0x1B, 0x80)

    label("loc_19DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19F2")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_19F7")

    label("loc_19F2")

    ClearChrFlags(0x1C, 0x80)

    label("loc_19F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A0D")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_1A12")

    label("loc_1A0D")

    ClearChrFlags(0x1D, 0x80)

    label("loc_1A12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A28")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_1A2D")

    label("loc_1A28")

    ClearChrFlags(0x1E, 0x80)

    label("loc_1A2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A43")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_1A48")

    label("loc_1A43")

    ClearChrFlags(0x1F, 0x80)

    label("loc_1A48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5E")
    SetChrFlags(0x20, 0x80)
    Jump("loc_1A63")

    label("loc_1A5E")

    ClearChrFlags(0x20, 0x80)

    label("loc_1A63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A79")
    SetChrFlags(0x21, 0x80)
    Jump("loc_1A7E")

    label("loc_1A79")

    ClearChrFlags(0x21, 0x80)

    label("loc_1A7E")

    Return()

    # Function_8_156B end

    def Function_9_1A7F(): pass

    label("Function_9_1A7F")

    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    Return()

    # Function_9_1A7F end

    def Function_10_1A8F(): pass

    label("Function_10_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_1B17")
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x4)
    SetChrPos(0x22, -2100, 4500, 3610, 135)

    def lambda_1AB7():

        label("loc_1AB7")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_1AB7")

    QueueWorkItem2(0x22, 3, lambda_1AB7)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xB4, 0x0)
    LoadEffect(0x7, "map\\mp259_01.eff")
    PlayEffect(0x7, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)

    label("loc_1B17")

    Return()

    # Function_10_1A8F end

    def Function_11_1B18(): pass

    label("Function_11_1B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B33")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 16)
    Return()

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B57")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B57")
    ClearMapFlags(0x2000000)
    OP_20(0x3E8)

    label("loc_1B57")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_1B75():
        OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1B75)
    OP_0D()
    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_11_1B18 end

    def Function_12_1B97(): pass

    label("Function_12_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 16)
    Return()

    label("loc_1BB2")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_1BD0():
        OP_90(0x0, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1BD0)
    OP_0D()
    NewScene("ED6_DT21/U7002   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_12_1B97 end

    def Function_13_1BF2(): pass

    label("Function_13_1BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C0D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 16)
    Return()

    label("loc_1C0D")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_1C2B():
        OP_90(0x0, 0x3E8, 0x0, 0xFFFFFC18, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1C2B)
    OP_0D()
    NewScene("ED6_DT21/U7003   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_13_1BF2 end

    def Function_14_1C4D(): pass

    label("Function_14_1C4D")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -14920, 1000, -13460, 45)
    SetChrPos(0x1, -14920, 1000, -13460, 45)
    SetChrPos(0x2, -14920, 1000, -13460, 45)
    SetChrPos(0x3, -14920, 1000, -13460, 45)
    OP_69(0x0, 0x0)
    Sleep(1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    Return()

    # Function_14_1C4D end

    def Function_15_1CCF(): pass

    label("Function_15_1CCF")

    SetMapFlags(0x80)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 15210, 1000, -13240, 315)
    SetChrPos(0x1, 15210, 1000, -13240, 315)
    SetChrPos(0x2, 15210, 1000, -13240, 315)
    SetChrPos(0x3, 15210, 1000, -13240, 315)
    OP_69(0x0, 0x0)
    Sleep(1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    EventEnd(0x2)
    Return()

    # Function_15_1CCF end

    def Function_16_1D51(): pass

    label("Function_16_1D51")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -140, 11920, 40200, 180)
    SetChrPos(0x1, -780, 11920, 41170, 180)
    SetChrPos(0x2, 930, 11920, 40980, 180)
    SetChrPos(0x3, 280, 11920, 41760, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -30, 11920, 40820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 18)
    EventEnd(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_1E0F")
    SetMapFlags(0x2000000)

    label("loc_1E0F")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_16_1D51 end

    def Function_17_1E3B(): pass

    label("Function_17_1E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4C")
    Call(1, 27)
    Return()

    label("loc_1E4C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 0, 11920, 40000, 0)
    SetChrPos(0x2, -1000, 11920, 41000, 0)
    SetChrPos(0x1, 1000, 11920, 41000, 0)
    SetChrPos(0x0, 0, 11920, 42000, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -30, 11920, 40820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_1F0A")
    ClearMapFlags(0x2000000)

    label("loc_1F0A")

    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1E3B end

    def Function_18_1F14(): pass

    label("Function_18_1F14")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F3D")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F31():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F31)

    label("loc_1F3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F66")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F5A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F5A)

    label("loc_1F66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F83():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F83)

    label("loc_1F8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB8")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FAC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1FAC)

    label("loc_1FB8")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE4")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1FFB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2012")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2012")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2029")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2029")

    Return()

    # Function_18_1F14 end

    def Function_19_202A(): pass

    label("Function_19_202A")


    def lambda_2030():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2030)

    def lambda_2042():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2042)

    def lambda_2054():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2054)

    def lambda_2066():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2066)
    Sleep(1000)
    Return()

    # Function_19_202A end

    def Function_20_2078(): pass

    label("Function_20_2078")

    EventBegin(0x0)
    SetChrPos(0x0, -1000, 4000, 0, 180)
    SetChrPos(0x1, 1000, 4000, 0, 180)
    SetChrPos(0x2, -1000, 4000, 2000, 180)
    SetChrPos(0x3, 1000, 4000, 2000, 180)
    Call(6, 27)
    EventEnd(0x0)
    Return()

    # Function_20_2078 end

    SaveToFile()

Try(main)

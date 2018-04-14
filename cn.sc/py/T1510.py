from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1510   ._SN',
        MapName             = 'Bose',
        Location            = 'T1510.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '雪拉扎德',                             # 9
        '阿加特',                               # 10
        '奥利维尔',                             # 11
        '科洛丝',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '凯文神父',                             # 15
        '索菲娜',                               # 16
        '雷纳德',                               # 17
        '库瓦诺老人',                           # 18
        '诺琪',                                 # 19
        '赫穆特',                               # 20
        '测量师艾柯',                           # 21
        '水壶',                                 # 22
        '红茶',                                 # 23
        '红茶',                                 # 24
        '红茶',                                 # 25
        '红茶',                                 # 26
        '水壶',                                 # 27
        '红茶',                                 # 28
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
        'ED6_DT07/CH00023 ._CH',             # 00
        'ED6_DT07/CH00053 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT07/CH00043 ._CH',             # 03
        'ED6_DT07/CH00063 ._CH',             # 04
        'ED6_DT07/CH00073 ._CH',             # 05
        'ED6_DT27/CH03083 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH00020 ._CH',             # 08
        'ED6_DT07/CH00050 ._CH',             # 09
        'ED6_DT07/CH00030 ._CH',             # 0A
        'ED6_DT07/CH00040 ._CH',             # 0B
        'ED6_DT07/CH00060 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT27/CH03080 ._CH',             # 0E
        'ED6_DT27/CH03003 ._CH',             # 0F
        'ED6_DT06/CH20020 ._CH',             # 10
        'ED6_DT06/CH20109 ._CH',             # 11
        'ED6_DT26/CH20225 ._CH',             # 12
        'ED6_DT26/CH20226 ._CH',             # 13
        'ED6_DT26/CH20231 ._CH',             # 14
        'ED6_DT07/CH01270 ._CH',             # 15
        'ED6_DT07/CH01000 ._CH',             # 16
        'ED6_DT07/CH01233 ._CH',             # 17
        'ED6_DT07/CH01220 ._CH',             # 18
        'ED6_DT26/CH20315 ._CH',             # 19
        'ED6_DT07/CH01460 ._CH',             # 1A
        'ED6_DT27/CH03840 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH00053P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT07/CH00043P._CP',             # 03
        'ED6_DT07/CH00063P._CP',             # 04
        'ED6_DT07/CH00073P._CP',             # 05
        'ED6_DT27/CH03083P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH00020P._CP',             # 08
        'ED6_DT07/CH00050P._CP',             # 09
        'ED6_DT07/CH00030P._CP',             # 0A
        'ED6_DT07/CH00040P._CP',             # 0B
        'ED6_DT07/CH00060P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT27/CH03080P._CP',             # 0E
        'ED6_DT27/CH03003P._CP',             # 0F
        'ED6_DT06/CH20020P._CP',             # 10
        'ED6_DT06/CH20109P._CP',             # 11
        'ED6_DT26/CH20225P._CP',             # 12
        'ED6_DT26/CH20226P._CP',             # 13
        'ED6_DT26/CH20231P._CP',             # 14
        'ED6_DT07/CH01270P._CP',             # 15
        'ED6_DT07/CH01000P._CP',             # 16
        'ED6_DT07/CH01233P._CP',             # 17
        'ED6_DT07/CH01220P._CP',             # 18
        'ED6_DT26/CH20315P._CP',             # 19
        'ED6_DT07/CH01460P._CP',             # 1A
        'ED6_DT27/CH03840P._CP',             # 1B
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 17240,
        Z                   = 0,
        Y                   = 13470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 16219,
        Z                   = 200,
        Y                   = 6370,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 15130,
        Z                   = 0,
        Y                   = 7430,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 23990,
        Z                   = 0,
        Y                   = 8790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
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
        Unknown3            = 1703952,
        ChipIndex           = 0x10,
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
        Unknown3            = 1638416,
        ChipIndex           = 0x10,
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
        Unknown3            = 1638416,
        ChipIndex           = 0x10,
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
        Unknown3            = 1638416,
        ChipIndex           = 0x10,
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
        Unknown3            = 1638416,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14900,
        Z                   = 800,
        Y                   = 6350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703952,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15300,
        Z                   = 800,
        Y                   = 6200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638416,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 23100,
        TriggerZ            = 0,
        TriggerY            = 6000,
        TriggerRange        = 700,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 6100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_42E",          # 00, 0
        "Function_1_A86",          # 01, 1
        "Function_2_B42",          # 02, 2
        "Function_3_CBF",          # 03, 3
        "Function_4_CC4",          # 04, 4
        "Function_5_10A9",         # 05, 5
        "Function_6_15B0",         # 06, 6
        "Function_7_16A0",         # 07, 7
        "Function_8_17F3",         # 08, 8
        "Function_9_18B2",         # 09, 9
        "Function_10_1BCC",        # 0A, 10
        "Function_11_1E23",        # 0B, 11
        "Function_12_21BA",        # 0C, 12
        "Function_13_2516",        # 0D, 13
        "Function_14_2775",        # 0E, 14
        "Function_15_29CA",        # 0F, 15
        "Function_16_2C25",        # 10, 16
        "Function_17_2E52",        # 11, 17
        "Function_18_3B0C",        # 12, 18
        "Function_19_3B50",        # 13, 19
        "Function_20_3B94",        # 14, 20
        "Function_21_3BD8",        # 15, 21
        "Function_22_3C08",        # 16, 22
        "Function_23_3D87",        # 17, 23
        "Function_24_3DE8",        # 18, 24
        "Function_25_3F58",        # 19, 25
        "Function_26_40DC",        # 1A, 26
        "Function_27_425E",        # 1B, 27
        "Function_28_43E8",        # 1C, 28
        "Function_29_4562",        # 1D, 29
        "Function_30_46D2",        # 1E, 30
        "Function_31_4859",        # 1F, 31
        "Function_32_4D01",        # 20, 32
        "Function_33_582F",        # 21, 33
        "Function_34_5875",        # 22, 34
        "Function_35_588A",        # 23, 35
        "Function_36_589F",        # 24, 36
        "Function_37_58B4",        # 25, 37
        "Function_38_58C9",        # 26, 38
        "Function_39_58DE",        # 27, 39
        "Function_40_58F3",        # 28, 40
        "Function_41_591C",        # 29, 41
        "Function_42_594C",        # 2A, 42
        "Function_43_597D",        # 2B, 43
        "Function_44_59AE",        # 2C, 44
        "Function_45_59ED",        # 2D, 45
        "Function_46_5A32",        # 2E, 46
        "Function_47_5A77",        # 2F, 47
        "Function_48_5ABC",        # 30, 48
        "Function_49_5B01",        # 31, 49
        "Function_50_5B53",        # 32, 50
        "Function_51_5EDD",        # 33, 51
        "Function_52_5F09",        # 34, 52
        "Function_53_5F38",        # 35, 53
        "Function_54_5F6C",        # 36, 54
        "Function_55_69DE",        # 37, 55
        "Function_56_6B07",        # 38, 56
        "Function_57_6B91",        # 39, 57
    )


    def Function_0_42E(): pass

    label("Function_0_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_860")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_477")
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 18100, 200, 8820, 270)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)

    label("loc_477")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    SetChrFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5")
    SetChrPos(0x9, 18100, 200, 8820, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4D0")

    label("loc_4B5")

    SetChrPos(0x9, 18100, 200, 10270, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)

    label("loc_4DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_572")
    SetChrFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    SetChrPos(0xA, 18100, 200, 8820, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_563")

    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548")
    SetChrPos(0xA, 18100, 200, 10270, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_563")

    label("loc_548")

    SetChrPos(0xA, 15510, 200, 10470, 90)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_563")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)

    label("loc_572")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B0")
    SetChrPos(0xB, 18100, 200, 8820, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_621")

    label("loc_5B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DB")
    SetChrPos(0xB, 18100, 200, 10270, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_621")

    label("loc_5DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606")
    SetChrPos(0xB, 15510, 200, 10470, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_621")

    label("loc_606")

    SetChrPos(0xB, 15510, 200, 9020, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_621")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)

    label("loc_630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE")
    SetChrFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E")
    SetChrPos(0xC, 18100, 200, 8820, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DF")

    label("loc_66E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_699")
    SetChrPos(0xC, 18100, 200, 10270, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DF")

    label("loc_699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    SetChrPos(0xC, 15510, 200, 10470, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DF")

    label("loc_6C4")

    SetChrPos(0xC, 15510, 200, 9020, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6DF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)

    label("loc_6EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AC")
    SetChrFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    SetChrPos(0xD, 18100, 200, 8820, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79D")

    label("loc_72C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    SetChrPos(0xD, 18100, 200, 10270, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79D")

    label("loc_757")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_782")
    SetChrPos(0xD, 15510, 200, 10470, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79D")

    label("loc_782")

    SetChrPos(0xD, 15510, 200, 9020, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)

    label("loc_7AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_860")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA")
    SetChrPos(0xE, 18100, 200, 8820, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85B")

    label("loc_7EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_815")
    SetChrPos(0xE, 18100, 200, 10270, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85B")

    label("loc_815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    SetChrPos(0xE, 15510, 200, 10470, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85B")

    label("loc_840")

    SetChrPos(0xE, 15510, 200, 9020, 90)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85B")

    ClearChrFlags(0xE, 0x80)

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_87A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_877")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_877")

    label("loc_877")

    Jump("loc_9FE")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_9AA")
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x8, 109270, 200, 12030, 270)
    SetChrPos(0xB, 106990, 200, 13150, 90)
    SetChrPos(0xC, 106980, 200, 12170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x15, 108420, 800, 12550, 0)
    SetChrPos(0x16, 108690, 800, 12880, 90)
    SetChrPos(0x17, 108620, 800, 11860, 90)
    SetChrPos(0x18, 107530, 800, 11920, 270)
    SetChrPos(0x19, 107550, 800, 12940, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0x9, 18100, 200, 8820, 270)
    SetChrPos(0xA, 18100, 200, 10270, 270)
    SetChrPos(0xD, 15510, 200, 10470, 90)
    SetChrPos(0xE, 15510, 200, 9020, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_9FE")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_9CA")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 24700, 0, 8790, 0)
    Jump("loc_9FE")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9E8")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jump("loc_9FE")

    label("loc_9E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_9F2")
    Jump("loc_9FE")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9FE")
    ClearChrFlags(0x11, 0x80)

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A18")
    OP_A3(0x10F0)
    OP_B1("t1510_y")
    Event(0, 32)
    Jump("loc_A85")

    label("loc_A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_A32")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 50)
    Jump("loc_A85")

    label("loc_A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_A55")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    OP_B1("t1510_y")
    Event(0, 54)
    Jump("loc_A85")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_A75")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F(0x5A, 0x64)
    Event(0, 55)
    Jump("loc_A85")

    label("loc_A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A85")
    Event(0, 17)

    label("loc_A85")

    Return()

    # Function_0_42E end

    def Function_1_A86(): pass

    label("Function_1_A86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20")
    OP_B1("t1510_n")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x20)
    OP_72(0x7, 0x8)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    Jump("loc_B41")

    label("loc_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_B38")
    OP_B1("t1510_y")
    OP_71(0x1D, 0x4)
    Jump("loc_B41")

    label("loc_B38")

    OP_B1("t1510_n")

    label("loc_B41")

    Return()

    # Function_1_A86 end

    def Function_2_B42(): pass

    label("Function_2_B42")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_CA9")

    label("loc_B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B80")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_CA9")

    label("loc_B80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B99")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_CA9")

    label("loc_B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB2")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_CA9")

    label("loc_BB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCB")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_CA9")

    label("loc_BCB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE4")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_CA9")

    label("loc_BE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_CA9")

    label("loc_BFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C16")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_CA9")

    label("loc_C16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_CA9")

    label("loc_C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C48")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_CA9")

    label("loc_C48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C61")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_CA9")

    label("loc_C61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_CA9")

    label("loc_C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C93")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_CA9")

    label("loc_C93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA9")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_CA9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_CA9")

    label("loc_CBE")

    Return()

    # Function_2_B42 end

    def Function_3_CBF(): pass

    label("Function_3_CBF")

    Call(0, 4)
    Return()

    # Function_3_CBF end

    def Function_4_CC4(): pass

    label("Function_4_CC4")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D47")

    ChrTalk(    #0
        0xF,
        "哎呀，你去散步吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "离吃晚饭\x01",
            "还有些时间呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "请就随便在四周走走，\x01",
            "享受一下散步的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_D9B")

    label("loc_D47")


    ChrTalk(    #3
        0xF,
        (
            "这个时间，夕阳照射到湖面\x01",
            "折射出非常美丽的光辉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        (
            "我想正是散步\x01",
            "最好的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9B")

    TalkEnd(0xF)
    Return()

    label("loc_D9F")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    OP_A9(0x49)
    TalkEnd(0xF)
    Return()

    label("loc_DB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCA")
    TalkEnd(0xF)
    Return()

    label("loc_DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E60")

    ChrTalk(    #5
        0xF,
        (
            "罗伊德和平时一样\x01",
            "在开心地钓鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xF,
        (
            "明明空中出现了奇怪的岛，\x01",
            "还能这样静下心来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "这样的专业…\x01",
            "还真是个厉害的家伙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_EB8")

    label("loc_E60")


    ChrTalk(    #8
        0xF,
        (
            "在空中浮着岛的时候\x01",
            "竟然还很开心地钓鱼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xF,
        (
            "要是我在这里的话\x01",
            "只会感到不安呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB8")

    Jump("loc_10A5")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4F")

    ChrTalk(    #10
        0xF,
        (
            "王室的船停靠在湖上，\x01",
            "空中又出现岛屿…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        (
            "尽是些难以置信的事，\x01",
            "我也不由地感到不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        (
            "因此昨天就\x01",
            "没怎么睡……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_FA7")

    label("loc_F4F")


    ChrTalk(    #13
        0xF,
        (
            "王室的船停靠在湖上，\x01",
            "空中又出现岛屿…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        (
            "呼，最近尽是些\x01",
            "难以置信的事呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA7")

    Jump("loc_10A5")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_FF4")

    ChrTalk(    #15
        0xF,
        (
            "非常感谢各位\x01",
            "预约本旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "如果有任何指示\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(    #17
        0xF,
        (
            "不安心情在住宿的客人们中间\x01",
            "也散播开来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "王国军好像有什么计划，\x01",
            "真想快点解决骚乱呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A5")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_10A5")

    ChrTalk(    #19
        0xF,
        (
            "欢迎光临。\x01",
            "欢迎来到川蝉亭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "想要住宿的话\x01",
            "请和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A5")

    TalkEnd(0xF)
    Return()

    # Function_4_CC4 end

    def Function_5_10A9(): pass

    label("Function_5_10A9")

    TalkBegin(0x10)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C6")
    OP_A9(0x4A)
    TalkEnd(0x10)
    Return()

    label("loc_10C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D7")
    TalkEnd(0x10)
    Return()

    label("loc_10D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_11ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119A")

    ChrTalk(    #21
        0x10,
        (
            "不过，湖上『埃尔赛尤』\x01",
            "今后怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "这样的异常延续下去，\x01",
            "导力引擎肯定也飞不起来吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "但是，也不可能\x01",
            "整艘拖回王都去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "暂时可能会这样，\x01",
            "浮在湖面上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_11EA")

    label("loc_119A")


    ChrTalk(    #25
        0x10,
        (
            "不过，湖上『埃尔赛尤』\x01",
            "今后怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "暂时可能会这样，\x01",
            "浮在湖面上吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EA")

    Jump("loc_15AC")

    label("loc_11ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(    #27
        0x10,
        (
            "停泊在湖面上的飞船\x01",
            "是王室的船呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "亲卫队的人经常到我们这里\x01",
            "来买些东西回去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "那次异常\x01",
            "幸好发生在水面上，\x01",
            "没事实在太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_12E0")

    label("loc_128A")


    ChrTalk(    #30
        0x10,
        (
            "停泊在湖面上的飞船\x01",
            "是王室的船呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "亲卫队的人经常到我们这里\x01",
            "来买些东西回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E0")

    Jump("loc_15AC")

    label("loc_12E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_1328")

    ChrTalk(    #32
        0x10,
        (
            "今天进了很多\x01",
            "新鲜的鱼贝类食物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "好好期待晚饭吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #34
        0x10,
        (
            "慢慢消遣\x01",
            "等待晚饭吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "没事做的话\x01",
            "试着钓鱼怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "在筏桥的附近\x01",
            "有很好钓鱼点哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1443")

    label("loc_1398")


    ChrTalk(    #37
        0x10,
        "喔，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "非常感谢各位预订\x01",
            "我们兄妹的旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "离晚饭还有段时间，\x01",
            "慢慢消遣等待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "没事做的话\x01",
            "试着钓鱼怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "在筏桥的附近\x01",
            "有很好钓鱼点哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1443")

    Jump("loc_15AC")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_14DC")

    ChrTalk(    #42
        0x10,
        (
            "据说有到拉文努村\x01",
            "好像被龙破坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "虽说离这里有些距离，\x01",
            "但能飞在空中的话就没什么距离可言了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        "这可不能当成别人家的事不管啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_14DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_15AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1541")

    ChrTalk(    #45
        0x10,
        (
            "最近来钓鱼的\x01",
            "客人特别多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "还有年轻的女性，\x01",
            "现在钓鱼爱好者的层面还真广呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AC")

    label("loc_1541")


    ChrTalk(    #47
        0x10,
        "噢，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "最近来钓鱼的\x01",
            "客人特别多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "还有对夫妇一起来的，\x01",
            "现在钓鱼爱好者的层面还真广呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_15AC")

    TalkEnd(0x10)
    Return()

    # Function_5_10A9 end

    def Function_6_15B0(): pass

    label("Function_6_15B0")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_169C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(    #50
        0xFE,
        (
            "听说龙出现了……\x01",
            "真是件难以置信的事呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "因为经常去城里，\x01",
            "没想到有这么大的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169C")

    label("loc_161C")


    ChrTalk(    #52
        0xFE,
        (
            "听说龙出现了……\x01",
            "真是件难以置信的事呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "因为经常去城里，\x01",
            "没想到有这么大的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "『安特洛丝』的各位\x01",
            "没有事吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_169C")

    TalkEnd(0x12)
    Return()

    # Function_6_15B0 end

    def Function_7_16A0(): pass

    label("Function_7_16A0")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_178E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16F2")

    ChrTalk(    #55
        0xFE,
        (
            "在钓鱼比赛中\x01",
            "输给了妻子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "呼，是才能\x01",
            "的差距吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178B")

    label("loc_16F2")


    ChrTalk(    #57
        0xFE,
        (
            "呼，向妻子挑战\x01",
            "比赛钓鱼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "……又输掉了。\x01",
            "已经，无话可说的惨败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "搞不懂为什么总是\x01",
            "她的鱼竿有鱼上钩呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "呼，是才能\x01",
            "的差距吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_178B")

    Jump("loc_17EF")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_17EF")

    ChrTalk(    #61
        0xFE,
        (
            "没想到龙之类的生物\x01",
            "真的存在的呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "好像受到了相当严重的损害，\x01",
            "这里不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17EF")

    TalkEnd(0x13)
    Return()

    # Function_7_16A0 end

    def Function_8_17F3(): pass

    label("Function_8_17F3")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1800")
    Jump("loc_18AE")

    label("loc_1800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_18AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1865")

    ChrTalk(    #63
        0xFE,
        (
            "接下来，休息休息，\x01",
            "那就试着钓钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "这里的湖里\x01",
            "有很多处非常好的钓鱼点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AE")

    label("loc_1865")


    ChrTalk(    #65
        0xFE,
        (
            "呼，到了宿舍后\x01",
            "果然放松下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "在家里的婆婆\x01",
            "实在太烦人了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_18AE")

    TalkEnd(0x11)
    Return()

    # Function_8_17F3 end

    def Function_9_18B2(): pass

    label("Function_9_18B2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B92")

    ChrTalk(    #67
        0xFE,
        "哎呀，是你们呀……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C9")

    ChrTalk(    #68
        0x101,
        (
            "#1001F啊，你好……\x02\x03",

            "#1004F……嗯，咦！？\x01",
            "怎么会有亲卫队的人？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #69
        0xFE,
        (
            "我们划小船来的……\x01",
            "为了筹措食物的任务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1015F是，是吗……\x02\x03",

            "想想好像『埃尔赛尤』\x01",
            "还停靠在湖面上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1043F就连拉赛尔博士也\x01",
            "好像陷入苦战了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6C")

    label("loc_19C9")


    ChrTalk(    #72
        0x101,
        "#1001F嘿嘿，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        "#1040F你是来购物的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "啊啊，准备持久战。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "修复军舰的日期还未确定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#1043F是吗……\x02\x03",

            "就连拉赛尔博士也\x01",
            "好像陷入苦战了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A97")

    ChrTalk(    #77
        0x107,
        "#561F嗯，好像是这样……\x02",
    )

    CloseMessageWindow()

    label("loc_1A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AEC")

    ChrTalk(    #78
        0x106,
        (
            "#051F那是老爷子的事了。\x02\x03",

            "交给他吧，最后一定会\x01",
            "想办法解决好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1AEC")


    ChrTalk(    #79
        0x101,
        (
            "#1000F嗯，既然是博士，\x01",
            "交给他一定能解决好的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1F")


    ChrTalk(    #80
        0xFE,
        "希望是吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "再见，我还有任务……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1011F对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#1041F那么，请代我们\x01",
            "向尤莉亚上尉问好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2095)
    Jump("loc_1BC8")

    label("loc_1B92")


    ChrTalk(    #84
        0xFE,
        "我回去进行自己的任务了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "你们也保重呀……\x02",
    )

    CloseMessageWindow()

    label("loc_1BC8")

    TalkEnd(0x14)
    Return()

    # Function_9_18B2 end

    def Function_10_1BCC(): pass

    label("Function_10_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CDC")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C68")
    Jump("loc_1CAA")

    label("loc_1C68")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C84")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAA")

    label("loc_1C84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CA0")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAA")

    label("loc_1CA0")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CAA")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Call(0, 26)
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    label("loc_1CDC")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D6C")
    Jump("loc_1DAE")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D88")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DAE")

    label("loc_1D88")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DA4")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DAE")

    label("loc_1DA4")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DAE")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #86
        0x8,
        (
            "#026F今天的夕阳也很美呀……\x02\x03",

            "#027F离晚饭还有些时间，\x01",
            "去散散步吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_10_1BCC end

    def Function_11_1E23(): pass

    label("Function_11_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F33")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EBF")
    Jump("loc_1F01")

    label("loc_1EBF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1EDB")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F01")

    label("loc_1EDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EF7")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F01")

    label("loc_1EF7")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F01")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Call(0, 24)
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    label("loc_1F33")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FC3")
    Jump("loc_2005")

    label("loc_1FC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FDF")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2005")

    label("loc_1FDF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFB")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2005")

    label("loc_1FFB")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2005")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2166")

    ChrTalk(    #87
        0x9,
        (
            "#051F哟，艾丝蒂尔。\x02\x03",

            "怎么，还在散步吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#1011F嗯，是啊……\x02\x03",

            "阿加特你们在干吗呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "#050F一边喝酒，\x01",
            "一边闲聊呢。\x02\x03",

            "总之就是在\x01",
            "悠闲的享受啊。\x02\x03",

            "反正这次就是为了休息\x01",
            "才来这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1001F对对……\x01",
            "必须好好休养身心一下。\x02\x03",

            "偶尔把工作抛开\x01",
            "也没什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#051F啊啊，可不是吗。\x02\x03",

            "那么，待会儿见。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C30)
    Jump("loc_21B1")

    label("loc_2166")


    ChrTalk(    #92
        0x9,
        (
            "#051F偶尔这样\x01",
            "深入交流也很好啊。\x02\x03",

            "嗯，到晚饭前就在这里\x01",
            "悠闲地度过吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_11_1E23 end

    def Function_12_21BA(): pass

    label("Function_12_21BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22CA")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2256")
    Jump("loc_2298")

    label("loc_2256")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2272")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2298")

    label("loc_2272")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_228E")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2298")

    label("loc_228E")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2298")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Call(0, 27)
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    label("loc_22CA")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_235A")
    Jump("loc_239C")

    label("loc_235A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2376")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_2376")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2392")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239C")

    label("loc_2392")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239C")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2473")

    ChrTalk(    #93
        0xA,
        (
            "#031F哎呀，你好啊，艾丝蒂尔。\x02\x03",

            "这里有上等的美酒、新鲜的下酒菜……\x01",
            "哎呀真是优雅的黄昏呀。\x02\x03",

            "再有美人来斟酒的话\x01",
            "就没有什么可说的啦……\x02\x03",

            "嗯，好好期待\x01",
            "晚饭之后吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_250D")

    label("loc_2473")


    ChrTalk(    #94
        0xA,
        (
            "#031F这里有上等的美酒、新鲜的下酒菜……\x01",
            "哎呀真是优雅的黄昏呀。\x02\x03",

            "唯一遗憾的是，没有如花似玉的美人相伴\x01",
            "空添了一丝寂寞……\x02\x03",

            "嗯，真期待晚餐后\x01",
            "的时间呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250D")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_12_21BA end

    def Function_13_2516(): pass

    label("Function_13_2516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2626")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25B2")
    Jump("loc_25F4")

    label("loc_25B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25CE")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F4")

    label("loc_25CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25EA")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25F4")

    label("loc_25EA")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25F4")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Call(0, 28)
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    label("loc_2626")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26B6")
    Jump("loc_26F8")

    label("loc_26B6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26D2")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26F8")

    label("loc_26D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26EE")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26F8")

    label("loc_26EE")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26F8")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #95
        0xB,
        (
            "#040F晚霞照映下的瓦雷利亚湖\x01",
            "十分的美丽。\x02\x03",

            "#40F我们接下来也\x01",
            "去阳台看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_13_2516 end

    def Function_14_2775(): pass

    label("Function_14_2775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2885")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2811")
    Jump("loc_2853")

    label("loc_2811")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_282D")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2853")

    label("loc_282D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2849")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2853")

    label("loc_2849")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2853")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Call(0, 25)
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    label("loc_2885")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2915")
    Jump("loc_2957")

    label("loc_2915")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2931")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2957")

    label("loc_2931")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_294D")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2957")

    label("loc_294D")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2957")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #96
        0xC,
        (
            "#060F我们再留在这里\x01",
            "喝一会儿茶。\x02\x03",

            "再见，姐姐。\x01",
            "吃晚饭时再见……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    # Function_14_2775 end

    def Function_15_29CA(): pass

    label("Function_15_29CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ADA")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A66")
    Jump("loc_2AA8")

    label("loc_2A66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A82")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AA8")

    label("loc_2A82")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A9E")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AA8")

    label("loc_2A9E")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AA8")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Call(0, 29)
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    label("loc_2ADA")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B6A")
    Jump("loc_2BAC")

    label("loc_2B6A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B86")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BAC")

    label("loc_2B86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BA2")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BAC")

    label("loc_2BA2")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BAC")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #97
        0xD,
        (
            "#070F又去钓鱼吗？\x02\x03",

            "#071F哈哈，不要太投入，\x01",
            "不然赶不上吃晚饭的时间了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    # Function_15_29CA end

    def Function_16_2C25(): pass

    label("Function_16_2C25")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CB5")
    Jump("loc_2CF7")

    label("loc_2CB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CD1")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CF7")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CED")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CF7")

    label("loc_2CED")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CF7")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2F")
    Call(0, 30)
    Jump("loc_2E49")

    label("loc_2D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFA")

    ChrTalk(    #98
        0xE,
        (
            "#1064F噢，艾丝蒂尔……\x02\x03",

            "喝茶的时间已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1025F不，雪拉姐他们\x01",
            "还在房间里休息……\x02\x03",

            "我稍微想来\x01",
            "看看湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xE,
        (
            "#1060F………………………………\x02\x03",

            "是吗，嗯……\x01",
            "天黑之前要回来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C31)
    Jump("loc_2E49")

    label("loc_2DFA")


    ChrTalk(    #101
        0xE,
        (
            "#1062F如果想欣赏美景的话\x01",
            "现在的确是最好的时机。\x02\x03",

            "不过，天黑之前要回来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E49")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_16_2C25 end

    def Function_17_2E52(): pass

    label("Function_17_2E52")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E69")
    Call(0, 56)
    Call(0, 57)

    label("loc_2E69")

    Call(0, 22)
    SetChrFlags(0xFA, 0x4)
    SetChrFlags(0xFB, 0x4)
    SetChrFlags(0xFC, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0x101, 18570, 0, 3140, 0)
    SetChrPos(0xF7, 17490, -250, 2650, 0)
    SetChrPos(0xF8, 18440, -250, 2200, 0)
    SetChrPos(0xF9, 19610, -250, 2530, 0)
    SetChrPos(0xFA, 15510, 200, 9020, 90)
    SetChrPos(0xFB, 18100, 200, 10270, 270)
    SetChrPos(0xFC, 15510, 200, 10470, 90)
    SetChrPos(0xE, 18100, 200, 8820, 270)
    ClearChrFlags(0xE, 0x80)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xFA)"), scpexpr(EXPR_END)),
        (2, "loc_2F2F"),
        (5, "loc_2F37"),
        (3, "loc_2F3F"),
        (4, "loc_2F47"),
        (6, "loc_2F4F"),
        (7, "loc_2F57"),
        (SWITCH_DEFAULT, "loc_2F5F"),
    )


    label("loc_2F2F")

    SetChrChipByIndex(0xFA, 0)
    Jump("loc_2F5F")

    label("loc_2F37")

    SetChrChipByIndex(0xFA, 1)
    Jump("loc_2F5F")

    label("loc_2F3F")

    SetChrChipByIndex(0xFA, 2)
    Jump("loc_2F5F")

    label("loc_2F47")

    SetChrChipByIndex(0xFA, 3)
    Jump("loc_2F5F")

    label("loc_2F4F")

    SetChrChipByIndex(0xFA, 4)
    Jump("loc_2F5F")

    label("loc_2F57")

    SetChrChipByIndex(0xFA, 5)
    Jump("loc_2F5F")

    label("loc_2F5F")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xFB)"), scpexpr(EXPR_END)),
        (2, "loc_2F80"),
        (5, "loc_2F88"),
        (3, "loc_2F90"),
        (4, "loc_2F98"),
        (6, "loc_2FA0"),
        (7, "loc_2FA8"),
        (SWITCH_DEFAULT, "loc_2FB0"),
    )


    label("loc_2F80")

    SetChrChipByIndex(0xFB, 0)
    Jump("loc_2FB0")

    label("loc_2F88")

    SetChrChipByIndex(0xFB, 1)
    Jump("loc_2FB0")

    label("loc_2F90")

    SetChrChipByIndex(0xFB, 2)
    Jump("loc_2FB0")

    label("loc_2F98")

    SetChrChipByIndex(0xFB, 3)
    Jump("loc_2FB0")

    label("loc_2FA0")

    SetChrChipByIndex(0xFB, 4)
    Jump("loc_2FB0")

    label("loc_2FA8")

    SetChrChipByIndex(0xFB, 5)
    Jump("loc_2FB0")

    label("loc_2FB0")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xFC)"), scpexpr(EXPR_END)),
        (2, "loc_2FD1"),
        (5, "loc_2FD9"),
        (3, "loc_2FE1"),
        (4, "loc_2FE9"),
        (6, "loc_2FF1"),
        (7, "loc_2FF9"),
        (SWITCH_DEFAULT, "loc_3001"),
    )


    label("loc_2FD1")

    SetChrChipByIndex(0xFC, 0)
    Jump("loc_3001")

    label("loc_2FD9")

    SetChrChipByIndex(0xFC, 1)
    Jump("loc_3001")

    label("loc_2FE1")

    SetChrChipByIndex(0xFC, 2)
    Jump("loc_3001")

    label("loc_2FE9")

    SetChrChipByIndex(0xFC, 3)
    Jump("loc_3001")

    label("loc_2FF1")

    SetChrChipByIndex(0xFC, 4)
    Jump("loc_3001")

    label("loc_2FF9")

    SetChrChipByIndex(0xFC, 5)
    Jump("loc_3001")

    label("loc_3001")

    OP_6D(18890, 0, 7310, 0)
    OP_67(0, 6370, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)
    OP_31(0x8, 0x0, 0x41)
    OP_31(0x8, 0xFE, 0x0)
    OP_37(0x8, 0x80, 0x2)
    OP_37(0x8, 0x81, 0x2)
    OP_37(0x8, 0x82, 0x2)
    OP_41(0x8, 0xEA, 0xFF)
    OP_41(0x8, 0x103, 0xFF)
    OP_41(0x8, 0x123, 0xFF)
    OP_41(0x8, 0x275, 0x0)
    OP_41(0x8, 0x25D, 0x1)
    OP_41(0x8, 0x25A, 0x2)
    OP_41(0x8, 0x265, 0x3)
    OP_41(0x8, 0x262, 0x4)
    OP_35(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0xFA, 2)
    Sleep(100)
    SetChrSubChip(0xFB, 1)
    SetChrSubChip(0xFC, 2)
    Sleep(500)

    ChrTalk(    #102
        0xE,
        (
            "#1062F#5P噢，好像\x01",
            "来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1004F#2P啊……！？\x02",
    )

    CloseMessageWindow()

    def lambda_30E7():
        OP_6D(18360, 0, 9200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30E7)

    def lambda_30FF():
        OP_67(0, 5410, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_30FF)

    def lambda_3117():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3117)
    OP_43(0x101, 0x1, 0x0, 0x12)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x13)
    Sleep(300)
    OP_43(0xF8, 0x1, 0x0, 0x14)
    Sleep(300)
    OP_43(0xF9, 0x1, 0x0, 0x15)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #104
        0x101,
        (
            "#1008F为、为什么凯文先生\x01",
            "会在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xE,
        (
            "#1061F哎呀～要问我为什么会在这里，\x01",
            "这话说起来可就长了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3219")

    ChrTalk(    #106
        0x103,
        (
            "#027F到这里来的途中，\x01",
            "正好在街道碰上的。\x02\x03",

            "接着呢\x01",
            "就跟着来到旅馆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3320")

    label("loc_3219")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3272")

    ChrTalk(    #107
        0x108,
        (
            "#070F到这里来的途中，\x01",
            "正好在街道碰上的。\x02\x03",

            "接着呢\x01",
            "就跟着来到旅馆了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3320")

    label("loc_3272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_32C9")

    ChrTalk(    #108
        0x107,
        (
            "#061F来这里的时候，\x01",
            "在街道的路上碰到了。\x02\x03",

            "接着就一起\x01",
            "到这里来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3320")

    label("loc_32C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3320")

    ChrTalk(    #109
        0x104,
        (
            "#035F来这里的路上，\x01",
            "在街道碰上的哦。\x02\x03",

            "#030F交流后\x01",
            "就跟着来到旅馆了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3320")


    ChrTalk(    #110
        0x101,
        (
            "#1015F街道的路上……\x01",
            "为什么会在那里遇到？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        (
            "#1060F坦白说吧，\x01",
            "我是来调查『琥珀之塔』的。\x02\x03",

            "其实，自从在洛连特\x01",
            "和艾丝蒂尔分别后\x01",
            "正在调查所有的『四轮之塔』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x101,
        "#1004F四轮之塔……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3439")

    ChrTalk(    #113
        0x106,
        (
            "#052F也就是说……\x01",
            "其它的三个塔也调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F3")

    label("loc_3439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3478")

    ChrTalk(    #114
        0x105,
        (
            "#044F也就是说……\x01",
            "其它的三个塔也调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F3")

    label("loc_3478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B7")

    ChrTalk(    #115
        0x104,
        (
            "#032F唔，这么说来\x01",
            "其它的三个塔也调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F3")

    label("loc_34B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F3")

    ChrTalk(    #116
        0x103,
        (
            "#023F就是说……\x01",
            "其它的三个塔也要调查吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F3")


    ChrTalk(    #117
        0xE,
        (
            "#1068F嗯，是这样呀。\x02\x03",

            "由于这里龙的骚乱，\x01",
            "我调查完全没有进展。\x02\x03",

            "#1066F所以想来这里交换下情报，\x01",
            "所以才跟着来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1011F这倒没关系……\x02\x03",

            "#1006F那么，这就开始\x01",
            "在这里交换情报吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        (
            "#1060F啊啊，可能的话\x01",
            "晚饭后比较好。\x02\x03",

            "那样的话大家都能\x01",
            "放心地谈话了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1001F啊，也是呢。\x02\x03",

            "#1004F……啊，凯文先生也\x01",
            "打算住在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xE,
        (
            "#1061F哈哈，我听说这\x01",
            "旅馆十分有名呀？\x02\x03",

            "#1062F既然如此，正好我也\x01",
            "想陪伴艾丝蒂尔\x01",
            "一起休假呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016F太，太突然了。\x02\x03",

            "#1006F不过，受到过凯文先生\x01",
            "好多次的关照了……\x02\x03",

            "各位，你们的意思呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x106,
        "#051F啊，蛮不错吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#021F唔，的确是个\x01",
            "回报的好机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x107,
        "#061F嘿嘿，我也赞成。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        "#035F呵，我也没有异议。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x105,
        (
            "#048F呵呵……\x01",
            "这也是种缘分吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x108,
        (
            "#071F嗯，难得有机会\x01",
            "就尽情放松吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xE,
        (
            "#1061F谢谢！\x02\x03",

            "#1062F真的感谢你们。\x01",
            "如果有什么需要\x02\x03",

            "就尽管吩咐吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x1C02)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A34")

    ChrTalk(    #130
        0x101,
        (
            "#1025F嗯，是啊。\x02\x03",

            "好不容易的一次机会，那我们就\x01",
            "先去把行李放好，然后好好地休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "#1064F什么，那好。\x02\x03",

            "#1068F真可惜～难得\x01",
            "我想用身体为你们效劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1019F真是的。\x01",
            "有点太过得意了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#067F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_28(0x97, 0x1, 0x10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3976")

    ChrTalk(    #134
        0x106,
        (
            "#051F好吧，那就\x01",
            "带我们去房间吧\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A16")

    label("loc_3976")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AD")

    ChrTalk(    #135
        0x103,
        (
            "#021F呵呵，接下来\x01",
            "带我们去房间吧\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A16")

    label("loc_39AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E4")

    ChrTalk(    #136
        0x108,
        (
            "#071F那好，接下来\x01",
            "带我们去房间吧\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A16")

    label("loc_39E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A16")

    ChrTalk(    #137
        0x104,
        (
            "#031F呵，接下来\x01",
            "带我们去房间吧\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A16")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 23)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_3B0B")

    label("loc_3A34")


    ChrTalk(    #138
        0x101,
        (
            "#1016F啊哈哈，那就\x01",
            "不客气的麻烦你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x97, 0x1, 0x4)
    OP_28(0x97, 0x1, 0x8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    OP_6D(17250, 0, 5960, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 17250, 0, 5960, 180)
    SetChrPos(0x1, 17250, 0, 5960, 180)
    SetChrPos(0x2, 17250, 0, 5960, 180)
    SetChrPos(0x3, 17250, 0, 5960, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)

    label("loc_3B0B")

    Return()

    # Function_17_2E52 end

    def Function_18_3B0C(): pass

    label("Function_18_3B0C")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4632, 0x0, 0x1CE8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_3B0C end

    def Function_19_3B50(): pass

    label("Function_19_3B50")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x493E, 0x0, 0x193C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_3B50 end

    def Function_20_3B94(): pass

    label("Function_20_3B94")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x43D0, 0x0, 0x17DE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_3B94 end

    def Function_21_3BD8(): pass

    label("Function_21_3BD8")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_21_3BD8 end

    def Function_22_3C08(): pass

    label("Function_22_3C08")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C41")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C7A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C62")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_3C66")

    label("loc_3C62")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_3C66")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CC7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C9B")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_3CB3")

    label("loc_3C9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CAF")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_3CB3")

    label("loc_3CAF")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_3CB3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D14")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE8")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_3D00")

    label("loc_3CE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CFC")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_3D00")

    label("loc_3CFC")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_3D00")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D61")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D35")
    AddParty(0x2, 0xFA, 0xFF)
    Jump("loc_3D4D")

    label("loc_3D35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D49")
    AddParty(0x2, 0xFB, 0xFF)
    Jump("loc_3D4D")

    label("loc_3D49")

    AddParty(0x2, 0xFC, 0xFF)

    label("loc_3D4D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D86")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3D86")

    Return()

    # Function_22_3C08 end

    def Function_23_3D87(): pass

    label("Function_23_3D87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3D97")
    RemoveParty(0x7, 0xFF)

    label("loc_3D97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3DA7")
    RemoveParty(0x4, 0xFF)

    label("loc_3DA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3DB7")
    RemoveParty(0x6, 0xFF)

    label("loc_3DB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3DC7")
    RemoveParty(0x3, 0xFF)

    label("loc_3DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3DD7")
    RemoveParty(0x5, 0xFF)

    label("loc_3DD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3DE7")
    RemoveParty(0x2, 0xFF)

    label("loc_3DE7")

    Return()

    # Function_23_3D87 end

    def Function_24_3DE8(): pass

    label("Function_24_3DE8")


    ChrTalk(    #139
        0x9,
        (
            "#051F哟，来晚了。\x02\x03",

            "准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E87"),
        (1, "loc_3EC7"),
        (2, "loc_3F18"),
        (SWITCH_DEFAULT, "loc_3F57"),
    )


    label("loc_3E87")


    ChrTalk(    #140
        0x9,
        (
            "#052F什么，是这样吗？\x02\x03",

            "#053F算了，办完事\x01",
            "就快点回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F57")

    label("loc_3EC7")


    ChrTalk(    #141
        0x9,
        (
            "#053F喔，是吗。\x02\x03",

            "#051F那好，接下来\x01",
            "带我们去房间吧\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_3F57")

    label("loc_3F18")


    ChrTalk(    #142
        0x9,
        (
            "#052F什么呀？\x01",
            "要更换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_3F57")

    label("loc_3F57")

    Return()

    # Function_24_3DE8 end

    def Function_25_3F58(): pass

    label("Function_25_3F58")


    ChrTalk(    #143
        0xC,
        (
            "#560F啊，姐姐！\x02\x03",

            "事已经办完了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FF7"),
        (1, "loc_403B"),
        (2, "loc_409E"),
        (SWITCH_DEFAULT, "loc_40DB"),
    )


    label("loc_3FF7")


    ChrTalk(    #144
        0xC,
        (
            "#064F哎呀……是吗？\x02\x03",

            "#061F我等着，事情办完了\x01",
            "就回来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40DB")

    label("loc_403B")


    ChrTalk(    #145
        0xC,
        (
            "#560F啊，是这样呀。\x02\x03",

            "#061F嘿嘿，那么就拜托\x01",
            "旅馆的人领我们去房间了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_40DB")

    label("loc_409E")


    ChrTalk(    #146
        0xC,
        (
            "#560F姐姐。\x01",
            "要替换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_40DB")

    label("loc_40DB")

    Return()

    # Function_25_3F58 end

    def Function_26_40DC(): pass

    label("Function_26_40DC")


    ChrTalk(    #147
        0x8,
        (
            "#020F哎呀，艾丝蒂尔。\x02\x03",

            "事情办完了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_417F"),
        (1, "loc_41CD"),
        (2, "loc_421E"),
        (SWITCH_DEFAULT, "loc_425D"),
    )


    label("loc_417F")


    ChrTalk(    #148
        0x8,
        (
            "#023F啊，是这样吗？\x02\x03",

            "#020F我们就在这里等着，\x01",
            "事情办妥后就回来这里哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_425D")

    label("loc_41CD")


    ChrTalk(    #149
        0x8,
        (
            "#021F呵呵，是吗～？\x02\x03",

            "#020F那尽快\x01",
            "带我们去房间吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_425D")

    label("loc_421E")


    ChrTalk(    #150
        0x8,
        (
            "#023F哎呀……\x01",
            "要替换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_425D")

    label("loc_425D")

    Return()

    # Function_26_40DC end

    def Function_27_425E(): pass

    label("Function_27_425E")


    ChrTalk(    #151
        0xA,
        (
            "#030F哎呀，艾丝蒂尔。\x02\x03",

            "已经准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4305"),
        (1, "loc_434F"),
        (2, "loc_439E"),
        (SWITCH_DEFAULT, "loc_43E7"),
    )


    label("loc_4305")


    ChrTalk(    #152
        0xA,
        (
            "#033F哎呀，是这样呀？\x02\x03",

            "#035F呵，我在这里等着\x01",
            "事情办完后就回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E7")

    label("loc_434F")


    ChrTalk(    #153
        0xA,
        (
            "#035F呵，是吗。\x02\x03",

            "#030F那么尽快带我们\x01",
            "去房间吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_43E7")

    label("loc_439E")


    ChrTalk(    #154
        0xA,
        (
            "#035F呵，看来正需要\x01",
            "我这个天才的实力呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_43E7")

    label("loc_43E7")

    Return()

    # Function_27_425E end

    def Function_28_43E8(): pass

    label("Function_28_43E8")


    ChrTalk(    #155
        0xB,
        (
            "#040F啊，艾丝蒂尔。\x02\x03",

            "已经准备完毕了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_448D"),
        (1, "loc_44CF"),
        (2, "loc_4522"),
        (SWITCH_DEFAULT, "loc_4561"),
    )


    label("loc_448D")


    ChrTalk(    #156
        0xB,
        (
            "#044F啊，是这样呀。\x02\x03",

            "#041F我在这里等着\x01",
            "事办完后就过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4561")

    label("loc_44CF")


    ChrTalk(    #157
        0xB,
        (
            "#041F呵呵，辛苦了。\x02\x03",

            "#048F那么快点带大家\x01",
            "去房间吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_4561")

    label("loc_4522")


    ChrTalk(    #158
        0xB,
        (
            "#040F明白了。\x01",
            "要替换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_4561")

    label("loc_4561")

    Return()

    # Function_28_43E8 end

    def Function_29_4562(): pass

    label("Function_29_4562")


    ChrTalk(    #159
        0xD,
        (
            "#070F哟，辛苦了。\x02\x03",

            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4603"),
        (1, "loc_4643"),
        (2, "loc_4694"),
        (SWITCH_DEFAULT, "loc_46D1"),
    )


    label("loc_4603")


    ChrTalk(    #160
        0xD,
        (
            "#073F噢，是吗。\x02\x03",

            "#070F我在这里等着\x01",
            "事情办完后就回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46D1")

    label("loc_4643")


    ChrTalk(    #161
        0xD,
        (
            "#073F噢噢，是吗。\x02\x03",

            "#071F那么尽快带我们\x01",
            "去房间吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_46D1")

    label("loc_4694")


    ChrTalk(    #162
        0xD,
        (
            "#073F噢……\x01",
            "要替换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_46D1")

    label("loc_46D1")

    Return()

    # Function_29_4562 end

    def Function_30_46D2(): pass

    label("Function_30_46D2")


    ChrTalk(    #163
        0xE,
        (
            "#1062F噢，艾丝蒂尔。\x02\x03",

            "还有什么事的话\x01",
            "我也来帮忙吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【已经没有事了】\x01",      # 1
            "【选择同行者】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4783"),
        (1, "loc_47C9"),
        (2, "loc_4818"),
        (SWITCH_DEFAULT, "loc_4858"),
    )


    label("loc_4783")


    ChrTalk(    #164
        0xE,
        (
            "#1064F怎么，不用吩咐？\x02\x03",

            "#1060F那么，我在这里等着\x01",
            "完了回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4858")

    label("loc_47C9")


    ChrTalk(    #165
        0xE,
        (
            "#1064F噢，是吗？\x02\x03",

            "#1061F那么就\x01",
            "带我们去房间吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_4858")

    label("loc_4818")


    ChrTalk(    #166
        0xE,
        (
            "#1061F来了啊。\x01",
            "要替换同行者吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_4858")

    label("loc_4858")

    Return()

    # Function_30_46D2 end

    def Function_31_4859(): pass

    label("Function_31_4859")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    SetMapFlags(0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4917")
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 18100, 200, 8820, 270)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)

    label("loc_4917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497F")
    SetChrFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4955")
    SetChrPos(0x9, 18100, 200, 8820, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4970")

    label("loc_4955")

    SetChrPos(0x9, 18100, 200, 10270, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4970")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)

    label("loc_497F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A12")
    SetChrFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49BD")
    SetChrPos(0xA, 18100, 200, 8820, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A03")

    label("loc_49BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49E8")
    SetChrPos(0xA, 18100, 200, 10270, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A03")

    label("loc_49E8")

    SetChrPos(0xA, 15510, 200, 10470, 90)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A03")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)

    label("loc_4A12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD0")
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A50")
    SetChrPos(0xB, 18100, 200, 8820, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AC1")

    label("loc_4A50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7B")
    SetChrPos(0xB, 18100, 200, 10270, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AC1")

    label("loc_4A7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AA6")
    SetChrPos(0xB, 15510, 200, 10470, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AC1")

    label("loc_4AA6")

    SetChrPos(0xB, 15510, 200, 9020, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AC1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)

    label("loc_4AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B8E")
    SetChrFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0E")
    SetChrPos(0xC, 18100, 200, 8820, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B7F")

    label("loc_4B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B39")
    SetChrPos(0xC, 18100, 200, 10270, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B7F")

    label("loc_4B39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B64")
    SetChrPos(0xC, 15510, 200, 10470, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B7F")

    label("loc_4B64")

    SetChrPos(0xC, 15510, 200, 9020, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B7F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)

    label("loc_4B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4C")
    SetChrFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BCC")
    SetChrPos(0xD, 18100, 200, 8820, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C3D")

    label("loc_4BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF7")
    SetChrPos(0xD, 18100, 200, 10270, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C3D")

    label("loc_4BF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C22")
    SetChrPos(0xD, 15510, 200, 10470, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C3D")

    label("loc_4C22")

    SetChrPos(0xD, 15510, 200, 9020, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C3D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)

    label("loc_4C4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D00")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8A")
    SetChrPos(0xE, 18100, 200, 8820, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CFB")

    label("loc_4C8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CB5")
    SetChrPos(0xE, 18100, 200, 10270, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CFB")

    label("loc_4CB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE0")
    SetChrPos(0xE, 15510, 200, 10470, 90)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CFB")

    label("loc_4CE0")

    SetChrPos(0xE, 15510, 200, 9020, 90)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CFB")

    ClearChrFlags(0xE, 0x80)

    label("loc_4D00")

    Return()

    # Function_31_4859 end

    def Function_32_4D01(): pass

    label("Function_32_4D01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_4A(0xF, 255)
    SetChrPos(0xF, 79400, 0, 14470, 180)
    SetChrPos(0x101, 79500, 0, 13020, 0)
    SetChrPos(0x8, 78510, 0, 11820, 0)
    SetChrPos(0xC, 80360, 0, 12750, 0)
    SetChrPos(0xB, 78510, 0, 12930, 0)
    SetChrPos(0x9, 80460, 0, 11810, 0)
    SetChrPos(0xA, 78550, 0, 10170, 0)
    SetChrPos(0xD, 79750, 0, 10470, 0)
    SetChrPos(0xE, 79540, 0, 11620, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0xB, 11)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    OP_6D(80060, 0, 13840, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(281, 0)
    OP_3F(0x419, 1)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #167
        0xF,
        (
            "#5P非常感谢\x01",
            "大家光临我们旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xF,
        (
            "#5P那就先让我\x01",
            "带领各位去房间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1006F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)

    def lambda_4EBA():
        OP_6D(80870, 0, 13830, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4EBA)
    OP_43(0xF, 0x1, 0x0, 0x21)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #170
        0xF,
        (
            "#5P首先，这里是\x01",
            "各位女士的房间。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0xF, 106650, 0, 11300, 180)
    SetChrPos(0x101, 108000, 0, 9310, 180)
    SetChrPos(0xC, 109430, 0, 10980, 90)
    SetChrPos(0xB, 109080, 0, 9920, 120)
    SetChrPos(0x8, 107110, 0, 10320, 180)
    SetChrPos(0xD, 105160, 0, 14050, 180)
    SetChrPos(0x9, 104860, 0, 12720, 180)
    SetChrPos(0xA, 105190, 0, 11860, 180)
    SetChrPos(0xE, 105900, 0, 13330, 180)
    OP_6D(107830, 0, 7310, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)

    def lambda_4FF4():
        OP_6D(108140, 0, 12550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FF4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #171
        0xC,
        "#061F#5P哇……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xB,
        (
            "#048F#5P很安稳的气氛，\x01",
            "好棒的房间呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#1006F#5P这里，是我们以前\x01",
            "来过的房间呢。\x02\x03",

            "不过，刚到就被派去了空贼基地，\x01",
            "结果没有能住上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xF,
        "#5P呵呵，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "#035F#5P呵，我倒是\x01",
            "在这床上休息过一会。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #176
        0x101,
        (
            "#1019F#2P那只是被雪拉姐\x01",
            "灌醉了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#021F#5P呵呵，我想这次\x01",
            "能好好享受了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0xF, 50100, 0, 25100, 90)
    SetChrPos(0x101, 55160, 0, 26790, 270)
    SetChrPos(0xC, 55040, 0, 25810, 270)
    SetChrPos(0xB, 55200, 0, 25150, 270)
    SetChrPos(0x8, 56030, 0, 25930, 270)
    SetChrPos(0xD, 54140, 0, 24330, 270)
    SetChrPos(0x9, 52100, 0, 25200, 270)
    SetChrPos(0xA, 53740, 0, 25950, 270)
    SetChrPos(0xE, 52050, 0, 24210, 315)
    OP_6D(50870, 0, 24810, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(78000, 0)
    OP_6E(286, 0)
    OP_72(0x14, 0x20)
    OP_72(0x14, 0x10)
    OP_6F(0x14, 59)

    def lambda_5257():
        OP_6D(54890, 0, 25840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5257)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #178
        0xF,
        (
            "#6P这里是各位男士\x01",
            "的客房……\x02\x03",

            "因为是双人间，请和旁边\x01",
            "的房间一起使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 400)

    ChrTalk(    #179
        0xE,
        (
            "#1062F啊，我是中途加入的，\x01",
            "大家先优先选择吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 315, 400)

    ChrTalk(    #180
        0xD,
        (
            "#073F#2P嗯，怎么办？\x01",
            "我哪里都可以哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #181
        0x9,
        "#051F#6P我也随便。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        (
            "#035F#5P呵……\x01",
            "那么我和阿加特\x01",
            "住一起好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #183
        0x9,
        (
            "#555F#6P……稍等一下。\x02\x03",

            "为什么这么突然就\x01",
            "选择我呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "#031F#5P哈哈哈。\x01",
            "就这样决定吧。\x02\x03",

            "#037F那天晚上，\x01",
            "只有你和提妲两个留在了村里，\x01",
            "期间发生过什么事嘛……\x02\x03",

            "我要你从头到尾、仔仔细细、一字不漏、\x01",
            "老老实实地全讲给我听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xC,
        "#064F#5P啊啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#055F#6P……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1007F#5P好变态的家伙……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(500)

    ChrTalk(    #188
        0x101,
        (
            "#1028F#5P嗯～说起来\x01",
            "我也有些兴趣想知道呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 315, 400)

    ChrTalk(    #189
        0xC,
        (
            "#065F#2P不，不过……\x01",
            "就是在一起说了说话啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x8,
        (
            "#021F#5P究竟说了些什么\x01",
            "这才至关重要的呀。\x02\x03",

            "#027F我们也要在睡觉前\x01",
            "好好地问问清楚哟～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        "#562F#5P啊，唔～……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 315, 400)

    ChrTalk(    #192
        0xB,
        (
            "#045F你们２位真是……\x02\x03",

            "#542F不要太乱来了，\x01",
            "你们看看，提妲被你们说得都要哭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    def lambda_562D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_562D)

    def lambda_563B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_563B)

    def lambda_5649():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5649)

    def lambda_5657():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5657)
    Sleep(500)

    ChrTalk(    #193
        0xA,
        (
            "#031F#5P呵，那么\x01",
            "金和凯文神父就\x01",
            "住在旁边的房间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xD,
        "#071F#2P啊啊，我没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xE,
        (
            "#1061F#4P呀，这下可有的好玩了，\x01",
            "我举双手赞成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xF,
        (
            "#6P呵呵，我就带你们\x01",
            "去隔壁的房间吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_43(0x8, 0x1, 0x0, 0x2A)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x2B)
    Sleep(400)
    OP_43(0xB, 0x1, 0x0, 0x2C)
    Sleep(700)
    OP_43(0x101, 0x1, 0x0, 0x2D)
    Sleep(600)
    OP_43(0xA, 0x1, 0x0, 0x2E)
    Sleep(700)
    OP_43(0xD, 0x1, 0x0, 0x2F)
    Sleep(400)
    OP_43(0xE, 0x1, 0x0, 0x30)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x31)

    def lambda_577E():
        OP_6D(55620, 0, 25780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_577E)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_63(0x9)
    Sleep(200)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #197
        0x9,
        (
            "#055F#6P喂，喂！\x01",
            "在关键时刻怎么全都跑了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1501   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4D01 end

    def Function_33_582F(): pass

    label("Function_33_582F")

    OP_8F(0xFE, 0x13A56, 0x0, 0x3A70, 0x7D0, 0x0)
    Sleep(500)
    OP_72(0x15, 0x20)
    OP_72(0x15, 0x10)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x7)
    OP_73(0x15)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_33_582F end

    def Function_34_5875(): pass

    label("Function_34_5875")

    OP_8E(0xFE, 0x13920, 0x0, 0x3192, 0x7D0, 0x0)
    Return()

    # Function_34_5875 end

    def Function_35_588A(): pass

    label("Function_35_588A")

    OP_8E(0xFE, 0x134E8, 0x0, 0x3192, 0x7D0, 0x0)
    Return()

    # Function_35_588A end

    def Function_36_589F(): pass

    label("Function_36_589F")

    OP_8E(0xFE, 0x136DC, 0x0, 0x2EB8, 0x7D0, 0x0)
    Return()

    # Function_36_589F end

    def Function_37_58B4(): pass

    label("Function_37_58B4")

    OP_8E(0xFE, 0x13362, 0x0, 0x2EB8, 0x7D0, 0x0)
    Return()

    # Function_37_58B4 end

    def Function_38_58C9(): pass

    label("Function_38_58C9")

    OP_8E(0xFE, 0x132A4, 0x0, 0x2AE4, 0x7D0, 0x0)
    Return()

    # Function_38_58C9 end

    def Function_39_58DE(): pass

    label("Function_39_58DE")

    OP_8E(0xFE, 0x1357E, 0x0, 0x28E6, 0x7D0, 0x0)
    Return()

    # Function_39_58DE end

    def Function_40_58F3(): pass

    label("Function_40_58F3")

    OP_8E(0xFE, 0x139D4, 0x0, 0x14DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1397A, 0x0, 0x2918, 0x7D0, 0x0)
    Return()

    # Function_40_58F3 end

    def Function_41_591C(): pass

    label("Function_41_591C")

    TurnDirection(0xFE, 0x8, 400)
    OP_8E(0xFE, 0x13844, 0x0, 0x1590, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13844, 0x0, 0x262A, 0x7D0, 0x0)
    Return()

    # Function_41_591C end

    def Function_42_594C(): pass

    label("Function_42_594C")

    OP_8C(0xFE, 90, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_594C end

    def Function_43_597D(): pass

    label("Function_43_597D")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_597D end

    def Function_44_59AE(): pass

    label("Function_44_59AE")

    OP_8C(0xFE, 0, 400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_44_59AE end

    def Function_45_59ED(): pass

    label("Function_45_59ED")

    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_45_59ED end

    def Function_46_5A32(): pass

    label("Function_46_5A32")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_46_5A32 end

    def Function_47_5A77(): pass

    label("Function_47_5A77")

    OP_8C(0xFE, 45, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_47_5A77 end

    def Function_48_5ABC(): pass

    label("Function_48_5ABC")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_48_5ABC end

    def Function_49_5B01(): pass

    label("Function_49_5B01")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xC814, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_49_5B01 end

    def Function_50_5B53(): pass

    label("Function_50_5B53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipByIndex(0x101, 17)
    SetChrChipByIndex(0x8, 18)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xC, 20)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrPos(0x101, 110200, 350, 8200, 0)
    SetChrPos(0xC, 109600, 350, 5300, 0)
    SetChrPos(0x8, 105900, 350, 8300, 0)
    SetChrPos(0xB, 105700, 350, 5300, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(109930, 350, 17110, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6F(0x19, 15)
    OP_6F(0x1C, 18)
    OP_6F(0x1A, 15)
    OP_6F(0x1B, 15)
    OP_22(0x1C2, 0x0, 0x64)
    Sleep(500)

    def lambda_5C6B():
        OP_6D(110740, 350, 8100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C6B)

    def lambda_5C83():
        OP_67(0, 6440, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C83)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_5CAA():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CAA)
    Sleep(500)
    SetChrSubChip(0x101, 15)
    Sleep(100)
    SetChrSubChip(0x101, 16)
    Sleep(1000)
    OP_6F(0x19, 15)
    OP_70(0x19, 0x3C)
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    Sleep(1000)
    OP_23(0x1C2)

    def lambda_5CF2():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CF2)
    OP_9E(0x101, 0xF, 0x0, 0x7D0, 0xFA0)
    OP_99(0x101, 0xC, 0xE, 0x3E8)
    SetChrSubChip(0x101, 14)
    Sleep(200)
    SetChrSubChip(0x101, 17)
    Sleep(200)
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 21)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(500)
    SetChrSubChip(0x101, 21)
    Sleep(500)
    SetChrSubChip(0x101, 18)
    Sleep(1000)
    Fade(500)

    def lambda_5D69():
        OP_6D(110750, 0, 7280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D69)
    SetChrPos(0x101, 109720, 0, 6420, 180)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    OP_8C(0x101, 180, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 25)
    OP_6F(0x19, 20)
    OP_70(0x19, 0xA)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_43(0xC, 0x2, 0x0, 0x35)
    OP_8C(0x101, 270, 400)

    def lambda_5DE6():
        OP_6D(106910, 0, 6690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DE6)
    OP_8E(0x101, 0x19BCC, 0x0, 0x1964, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_43(0x8, 0x2, 0x0, 0x33)
    OP_8C(0x101, 180, 400)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_43(0xB, 0x2, 0x0, 0x34)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #198
        (
            "\x07\x05从每天的紧张中解放出来，\x01",
            "好好地在床上睡上一觉\x01",
            "醒来迎接爽快的清晨……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_50_5B53 end

    def Function_51_5EDD(): pass

    label("Function_51_5EDD")

    Sleep(200)
    OP_62(0xFE, 0x190, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xFE, 2)
    Sleep(300)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_51_5EDD end

    def Function_52_5F09(): pass

    label("Function_52_5F09")

    Sleep(200)
    OP_62(0xFE, 0x1F4, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Return()

    # Function_52_5F09 end

    def Function_53_5F38(): pass

    label("Function_53_5F38")

    Sleep(200)
    OP_62(0xFE, 0x320, 1300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Sleep(500)
    OP_99(0xFE, 0x8, 0xA, 0x3E8)
    Return()

    # Function_53_5F38 end

    def Function_54_5F6C(): pass

    label("Function_54_5F6C")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0x101, 15)
    SetChrPos(0x101, 109300, 200, 13000, 270)
    SetChrPos(0x8, 109300, 200, 12030, 270)
    SetChrPos(0xB, 106990, 200, 13150, 90)
    SetChrPos(0xC, 106980, 200, 12170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x15, 108200, 800, 12550, 0)
    SetChrPos(0x16, 108400, 800, 12980, 90)
    SetChrPos(0x17, 108400, 800, 11960, 90)
    SetChrPos(0x18, 107530, 800, 11920, 270)
    SetChrPos(0x19, 107550, 800, 12940, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_71(0x1D, 0x4)
    OP_6D(108800, 200, 7080, 0)
    OP_67(0, 7120, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(53000, 0)
    OP_6E(249, 0)

    def lambda_6090():
        OP_6D(109020, 200, 13230, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6090)

    def lambda_60A8():
        OP_67(0, 6120, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_60A8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #199
        0x101,
        "#1001F#5P哈，真是有意思㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xC,
        (
            "#061F#6P嘿嘿……\x01",
            "真是开心呀⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "#048F呵呵，全身心都\x01",
            "得到了放松。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        (
            "#021F#2P哎呀，没有喝酒\x01",
            "就这么开心，真是好久没这样了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #203
        0x101,
        (
            "#1019F#5P啊，说错了吧……\x02\x03",

            "我们钓鱼的时候，\x01",
            "不是喝了水果酒吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #204
        0x8,
        (
            "#027F#2P哎呀，那样的轻度饮料\x01",
            "怎么能算上酒啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(400)

    ChrTalk(    #205
        0x8,
        "#021F#2P是吧～？公主，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xC,
        "#067F#6P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xB,
        (
            "#045F呵呵……\x01",
            "我不做任何评价。\x02\x03",

            "#040F话说回来……\x01",
            "艾丝蒂尔对钓鱼\x01",
            "真的很拿手呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #208
        0x101,
        "#1008F#5P嘿嘿，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xC,
        (
            "#061F#6P嗯嗯！\x01",
            "因为姐姐经常钓的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#021F#2P呵呵，这孩子从小\x01",
            "就对钓鱼很感兴趣。\x02\x03",

            "#020F说起来……\x01",
            "凯文神父也很拿手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#1006F#5P啊，嗯。\x01",
            "好像也十分喜欢的样子。\x02\x03",

            "甩竿的技巧\x01",
            "真的很不错呢。\x02\x03",

            "#1001F再稍微磨练一下的话\x01",
            "说不定就能成为\x01",
            "我的一个好对手⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#025F#2P真是的……\x01",
            "稍稍夸了一下，尾巴就翘上天了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xC,
        "#061F#6P嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xB,
        (
            "#041F呵呵……\x02\x03",

            "#048F不知不觉……\x01",
            "已经快要傍晚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#1004F#5P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_6474():
        OP_6D(109140, 200, 15670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6474)

    def lambda_648C():
        OP_67(0, 7540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_648C)

    def lambda_64A4():
        OP_6C(28000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_64A4)

    def lambda_64B4():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64B4)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #216
        0x101,
        "#1026F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(109020, 200, 13230, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(53000, 0)
    OP_6E(249, 0)
    OP_0D()
    Sleep(200)
    SetChrSubChip(0x8, 2)
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(100)

    ChrTalk(    #217
        0xB,
        "#044F？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xC,
        "#064F#6P姐姐，怎么了？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #219
        0x101,
        "#1016F#5P啊，嗯……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 109200, 0, 14020, 0)
    ClearChrFlags(0x101, 0x4)

    def lambda_65F2():
        OP_6D(108880, 0, 13830, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65F2)

    def lambda_660A():
        OP_67(0, 6300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_660A)
    Sleep(1000)
    OP_8C(0x101, 225, 300)
    Sleep(500)

    ChrTalk(    #220
        0x101,
        (
            "#1025F#5P我……\x01",
            "我稍微出去散下步。\x02\x03",

            "吃晚饭的时候就回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x8,
        (
            "#020F#2P是吗……\x02\x03",

            "#021F迟到的话，可\x01",
            "什么都剩不下了哟？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1016F#5P啊哈哈，明白了。\x02\x03",

            "#1006F那么，等会见。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x1A7A2, 0x0, 0x3804, 0x7D0, 0x0)
    OP_8E(0x101, 0x19FD2, 0x0, 0x3822, 0x7D0, 0x0)

    def lambda_6716():
        OP_6D(108160, 0, 13580, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6716)

    def lambda_672E():
        OP_6C(53000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_672E)

    def lambda_673E():
        OP_8E(0xFE, 0x197EE, 0x0, 0x3278, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_673E)
    SetChrSubChip(0xB, 1)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_677E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_677E)
    OP_8E(0x101, 0x19064, 0x0, 0x32F0, 0x7D0, 0x0)
    SetChrFlags(0x101, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_22(0x7, 0x0, 0x64)

    ChrTalk(    #223
        0xC,
        "#065F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_67CC():
        OP_6D(109020, 200, 13230, 1600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67CC)
    SetChrSubChip(0xC, 0)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #224
        0xC,
        "#063F#6P雪拉姐姐，那……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        (
            "#524F#2P没关系的，提妲。\x02\x03",

            "现在这时候\x01",
            "最好还是让她去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xB,
        (
            "#043F难道说……\x01",
            "是约修亚的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xC,
        "#065F#6P啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x8,
        "#026F#2P呵呵，你很明白呢。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(1000)

    ChrTalk(    #229
        0x8,
        (
            "#522F#2P这么说来，那个时候也……\x01",
            "夕阳也和今天一样的美丽。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C03)
    OP_28(0x78, 0x4, 0x40)
    OP_28(0x79, 0x4, 0x40)
    OP_28(0x7A, 0x4, 0x40)
    OP_28(0x7B, 0x4, 0x40)
    OP_28(0x7C, 0x4, 0x40)
    OP_28(0x7D, 0x4, 0x40)
    OP_28(0xB1, 0x4, 0x40)
    OP_28(0xB2, 0x4, 0x40)
    OP_28(0xB3, 0x4, 0x40)
    OP_28(0xB4, 0x4, 0x40)
    OP_28(0x97, 0x1, 0x20)
    OP_28(0x97, 0x1, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x381, 0x0)"), scpexpr(EXPR_END)), "loc_6947")
    OP_3F(0x381, 1)
    OP_3E(0x41B, 1)

    label("loc_6947")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    OP_6F(0x15, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 80170, 0, 14940, 270)
    ClearChrFlags(0x101, 0x80)
    OP_6D(80170, 0, 14940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_31(0xFF, 0xFE, 0x0)
    OP_1D(0xF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_54_5F6C end

    def Function_55_69DE(): pass

    label("Function_55_69DE")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    OP_6D(109500, -250, 13820, 0)
    OP_67(0, 6350, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    SetChrSubChip(0x8, 2)
    Sleep(200)
    SetChrSubChip(0xC, 1)
    Sleep(200)
    SetChrSubChip(0xB, 1)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x80)
    SetChrSubChip(0x9, 2)
    SetChrSubChip(0xA, 2)
    SetChrSubChip(0xD, 1)
    OP_6D(27330, -250, 5710, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(61000, 0)
    OP_6E(262, 0)

    def lambda_6AB1():
        OP_6D(17060, 0, 9800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AB1)

    def lambda_6AC9():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AC9)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_55_69DE end

    def Function_56_6B07(): pass

    label("Function_56_6B07")

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
        (0, "loc_6B84"),
        (1, "loc_6B8A"),
        (SWITCH_DEFAULT, "loc_6B90"),
    )


    label("loc_6B84")

    OP_A2(0x1200)
    Jump("loc_6B90")

    label("loc_6B8A")

    OP_A2(0x1201)
    Jump("loc_6B90")

    label("loc_6B90")

    Return()

    # Function_56_6B07 end

    def Function_57_6B91(): pass

    label("Function_57_6B91")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_57_6B91 end

    SaveToFile()

Try(main)

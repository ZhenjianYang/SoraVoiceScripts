from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Scherazard',                           # 9
        'Agate',                                # 10
        'Olivier',                              # 11
        'Kloe',                                 # 12
        'Tita',                                 # 13
        'Zin',                                  # 14
        'Father Kevin',                         # 15
        'Sophina',                              # 16
        'Lenard',                               # 17
        'Kuwano',                               # 18
        'Norche',                               # 19
        'Helmuth',                              # 20
        'Sensor Operator Echo',                 # 21
        'ポット',                               # 22
        '紅茶',                                 # 23
        '紅茶',                                 # 24
        '紅茶',                                 # 25
        '紅茶',                                 # 26
        'ポット',                               # 27
        '紅茶',                                 # 28
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
        "Function_5_122F",         # 05, 5
        "Function_6_1A3A",         # 06, 6
        "Function_7_1B8B",         # 07, 7
        "Function_8_1D9D",         # 08, 8
        "Function_9_1EBA",         # 09, 9
        "Function_10_2310",        # 0A, 10
        "Function_11_259A",        # 0B, 11
        "Function_12_29E9",        # 0C, 12
        "Function_13_2DDB",        # 0D, 13
        "Function_14_307F",        # 0E, 14
        "Function_15_32E0",        # 0F, 15
        "Function_16_3555",        # 10, 16
        "Function_17_37BF",        # 11, 17
        "Function_18_4831",        # 12, 18
        "Function_19_4875",        # 13, 19
        "Function_20_48B9",        # 14, 20
        "Function_21_48FD",        # 15, 21
        "Function_22_492D",        # 16, 22
        "Function_23_4AAC",        # 17, 23
        "Function_24_4B0D",        # 18, 24
        "Function_25_4CF4",        # 19, 25
        "Function_26_4EAC",        # 1A, 26
        "Function_27_5077",        # 1B, 27
        "Function_28_5270",        # 1C, 28
        "Function_29_5446",        # 1D, 29
        "Function_30_560A",        # 1E, 30
        "Function_31_5814",        # 1F, 31
        "Function_32_5CBC",        # 20, 32
        "Function_33_6B43",        # 21, 33
        "Function_34_6B89",        # 22, 34
        "Function_35_6B9E",        # 23, 35
        "Function_36_6BB3",        # 24, 36
        "Function_37_6BC8",        # 25, 37
        "Function_38_6BDD",        # 26, 38
        "Function_39_6BF2",        # 27, 39
        "Function_40_6C07",        # 28, 40
        "Function_41_6C30",        # 29, 41
        "Function_42_6C60",        # 2A, 42
        "Function_43_6C91",        # 2B, 43
        "Function_44_6CC2",        # 2C, 44
        "Function_45_6D01",        # 2D, 45
        "Function_46_6D46",        # 2E, 46
        "Function_47_6D8B",        # 2F, 47
        "Function_48_6DD0",        # 30, 48
        "Function_49_6E15",        # 31, 49
        "Function_50_6E67",        # 32, 50
        "Function_51_7219",        # 33, 51
        "Function_52_7245",        # 34, 52
        "Function_53_7274",        # 35, 53
        "Function_54_72A8",        # 36, 54
        "Function_55_7F4E",        # 37, 55
        "Function_56_8079",        # 38, 56
        "Function_57_8102",        # 39, 57
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58")

    ChrTalk(    #0
        0xF,
        "Oh, out for a walk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        "We still have a little time before dinner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        "Please, feel free to have a look around!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_DDE")

    label("loc_D58")


    ChrTalk(    #3
        0xF,
        (
            "Isn't the setting sun on the surface of\x01",
            "the lake pretty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xF,
        (
            "It's the perfect time to just go enjoy\x01",
            "yourself outside for a bit!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDE")

    TalkEnd(0xF)
    Return()

    label("loc_DE2")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFC")
    OP_A9(0x49)
    TalkEnd(0xF)
    Return()

    label("loc_DFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0D")
    TalkEnd(0xF)
    Return()

    label("loc_E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDF")

    ChrTalk(    #5
        0xF,
        "Lloyd's out there fishing, as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xF,
        (
            "I'm amazed he can be so calm about it,\x01",
            "what with that island in the sky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "I guess professional fishermen are\x01",
            "in a class all their own...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_F57")

    label("loc_EDF")


    ChrTalk(    #8
        0xF,
        (
            "I'm amazed Lloyd can fish so calmly\x01",
            "with that island hovering over us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xF,
        (
            "I get nervous just by looking\x01",
            "at it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F57")

    Jump("loc_122B")

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1032")

    ChrTalk(    #10
        0xF,
        (
            "The royal airship landed in the lake,\x01",
            "there's an island floating in the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        (
            "With so many crazy things happening,\x01",
            "I can't help but be anxious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        "I barely slept last night, even!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_10B1")

    label("loc_1032")


    ChrTalk(    #13
        0xF,
        (
            "The royal airship landed in the lake,\x01",
            "there's an island floating in the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        "*sigh* Nothing makes sense anymore...\x02",
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_122B")

    label("loc_10B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_113A")

    ChrTalk(    #15
        0xF,
        (
            "Thank you for choosing to stay here at\x01",
            "our inn today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "If you need anything at all, please,\x01",
            "don't hesitate to ask!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122B")

    label("loc_113A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_11C2")

    ChrTalk(    #17
        0xF,
        "Our guests are getting really nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "I know the Royal Army has some kind\x01",
            "of plan. I just hope they use it soon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122B")

    label("loc_11C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_122B")

    ChrTalk(    #19
        0xF,
        "Welcome to the Kingfisher Inn!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "If you're here to book a stay, please\x01",
            "just say the word!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122B")

    TalkEnd(0xF)
    Return()

    # Function_4_CC4 end

    def Function_5_122F(): pass

    label("Function_5_122F")

    TalkBegin(0x10)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124C")
    OP_A9(0x4A)
    TalkEnd(0x10)
    Return()

    label("loc_124C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125D")
    TalkEnd(0x10)
    Return()

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_141C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #21
        0x10,
        (
            "I wonder what the folks on the Arseille\x01",
            "have planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "As long as...whatever THIS is continues,\x01",
            "they won't be able to fly with orbal engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "And at the same time, you can't really\x01",
            "tow it back to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "I guess it's just gonna float out there\x01",
            "on the lake for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1419")

    label("loc_1397")


    ChrTalk(    #25
        0x10,
        (
            "I wonder what the folks on the Arseille\x01",
            "plan on doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "I guess it's just gonna float out there\x01",
            "on the lake for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    Jump("loc_1A36")

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152A")

    ChrTalk(    #27
        0x10,
        (
            "The airship that landed in the lake\x01",
            "is the royal flagship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "The Royal Guardsmen on board come\x01",
            "by here to stock up every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "Apparently they had a splash-down once\x01",
            "everything went crazy. I'm amazed they\x01",
            "made it through that okay!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_15B5")

    label("loc_152A")


    ChrTalk(    #30
        0x10,
        (
            "The airship that landed in the lake\x01",
            "is the royal flagship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "The Royal Guardsmen on board come\x01",
            "by here to stock up every so often.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")

    Jump("loc_1A36")

    label("loc_15B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_161C")

    ChrTalk(    #32
        0x10,
        "We've got lots of fresh fish today, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "I'm looking forward to dinner tonight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_161C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_17F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16D2")

    ChrTalk(    #34
        0x10,
        (
            "Relax and enjoy yourselves.\x01",
            "I'll see you again at dinner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "If you have nothing else to do,\x01",
            "why not try fishing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        "The piers are excellent fishing spots!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17EE")

    label("loc_16D2")


    ChrTalk(    #37
        0x10,
        "Heya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "Thank you for staying at this little corner\x01",
            "of Liberl my sister and I run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "There's still some time until dinner,\x01",
            "so relax and enjoy yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "If you have nothing else to do,\x01",
            "why not try fishing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "The piers are renowned for their\x01",
            "unparalleled catches!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_17EE")

    Jump("loc_1A36")

    label("loc_17F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_18B4")

    ChrTalk(    #42
        0x10,
        (
            "I heard even Ravennue was hit by\x01",
            "the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "May be a long way on foot, but\x01",
            "you could FLY it in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "Can't really think of it as someone\x01",
            "else's problem, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_18B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1972")

    ChrTalk(    #45
        0x10,
        (
            "We've been getting a lot of customers\x01",
            "coming in to fish lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "We've even got a young lady now!\x01",
            "The fishing community's getting\x01",
            "bigger and bigger all the time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_1972")


    ChrTalk(    #47
        0x10,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "We've been getting a lot of customers\x01",
            "coming in to fish lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "We even have a married couple in!\x01",
            "The fishing community's getting\x01",
            "bigger and bigger all the time...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1A36")

    TalkEnd(0x10)
    Return()

    # Function_5_122F end

    def Function_6_1A3A(): pass

    label("Function_6_1A3A")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1B87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AD1")

    ChrTalk(    #50
        0xFE,
        "A dragon... I just can't believe it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I visit Bose a lot, so I really can't\x01",
            "just think of it as 'someone else's'\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B87")

    label("loc_1AD1")


    ChrTalk(    #52
        0xFE,
        "A dragon... I just can't believe it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I visit Bose a lot, so I really can't\x01",
            "just think of it as 'someone else's'\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "I hope everyone at the Anterose is okay...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B87")

    TalkEnd(0x12)
    Return()

    # Function_6_1A3A end

    def Function_7_1B8B(): pass

    label("Function_7_1B8B")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1D19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C0C")

    ChrTalk(    #55
        0xFE,
        "I lost to my wife in a fishing competition...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "*sigh* There really is a gap in talent\x01",
            "between us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D16")

    label("loc_1C0C")


    ChrTalk(    #57
        0xFE,
        "I challenged my wife to a fishing competition...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "...and I lost. Again.\x01",
            "A total loss, fair and incontrovertible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "How does she keep getting hit after\x01",
            "hit on her line? I just don't understand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "*sigh* There really is a gap in talent\x01",
            "between us...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D16")

    Jump("loc_1D99")

    label("loc_1D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(    #61
        0xFE,
        "I never even imagined dragons were real.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "The damage sounds severe.\x01",
            "I hope everyone in the city is all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D99")

    TalkEnd(0x13)
    Return()

    # Function_7_1B8B end

    def Function_8_1D9D(): pass

    label("Function_8_1D9D")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1DAA")
    Jump("loc_1EB6")

    label("loc_1DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E44")

    ChrTalk(    #63
        0xFE,
        (
            "Now, then! I'm all rested up, and\x01",
            "it's time to get back to fishin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Ol' Valleria really does have so\x01",
            "many great fishing spots!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB6")

    label("loc_1E44")


    ChrTalk(    #65
        0xFE,
        "Ahhh, so relaxing, bein' at the inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Back home, my old lady is such a hassle,\x01",
            "I can hardly stand it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1EB6")

    TalkEnd(0x11)
    Return()

    # Function_8_1D9D end

    def Function_9_1EBA(): pass

    label("Function_9_1EBA")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(    #67
        0xFE,
        "Oh, bracers.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2013")

    ChrTalk(    #68
        0x101,
        (
            "#1001FOh, hi!\x02\x03",

            "#1004F...Er, wait, what's a member of the\x01",
            "Royal Guard doing here?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #69
        0xFE,
        (
            "We rowed out to the inn to pick up\x01",
            "supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1015FOh, okay.\x02\x03",

            "...Oh, right! The Arseille is stuck in\x01",
            "the middle of the lake, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1043FEven Professor Russell's struggling\x01",
            "with this, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213B")

    label("loc_2013")


    ChrTalk(    #72
        0x101,
        "#1001FHi, Echo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        "#1040FDoing some shopping?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Yes, we're gathering supplies for the\x01",
            "long term.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "We have no idea when we'll be able to\x01",
            "get the ship airborne again, so we have\x01",
            "to just buy what we can now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#1043FI see...\x02\x03",

            "Even Professor Russell's struggling\x01",
            "with this, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_216D")

    ChrTalk(    #77
        0x107,
        "#561FY-Yeah, sounds like it...\x02",
    )

    CloseMessageWindow()

    label("loc_216D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EA")

    ChrTalk(    #78
        0x106,
        (
            "#051FAh, don't worry about Gramps.\x02\x03",

            "Leave it to him. He'll pull some miracle\x01",
            "outta thin air, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223A")

    label("loc_21EA")


    ChrTalk(    #79
        0x101,
        (
            "#1000FThis IS the professor we're talking about.\x01",
            "I bet he'll pull through!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223A")


    ChrTalk(    #80
        0xFE,
        "We certainly hope he does...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Regardless, I have my mission, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1011FOh, right, sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        "#1041FGive our best to Captain Schwarz.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2095)
    Jump("loc_230C")

    label("loc_22D6")


    ChrTalk(    #84
        0xFE,
        "Back to the grind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Take care of yourselves.\x02",
    )

    CloseMessageWindow()

    label("loc_230C")

    TalkEnd(0x14)
    Return()

    # Function_9_1EBA end

    def Function_10_2310(): pass

    label("Function_10_2310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2420")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23AC")
    Jump("loc_23EE")

    label("loc_23AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23C8")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23EE")

    label("loc_23C8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E4")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23EE")

    label("loc_23E4")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23EE")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Call(0, 26)
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    label("loc_2420")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24B0")
    Jump("loc_24F2")

    label("loc_24B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24CC")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F2")

    label("loc_24CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24E8")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F2")

    label("loc_24E8")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24F2")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #86
        0x8,
        (
            "#026FAnother lovely evening...\x02\x03",

            "#027FYou've got plenty of time until dinner.\x01",
            "Go have a walk and enjoy the fresh air.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_10_2310 end

    def Function_11_259A(): pass

    label("Function_11_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26AA")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2636")
    Jump("loc_2678")

    label("loc_2636")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2652")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2678")

    label("loc_2652")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_266E")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2678")

    label("loc_266E")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2678")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Call(0, 24)
    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    label("loc_26AA")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_273A")
    Jump("loc_277C")

    label("loc_273A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2756")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_277C")

    label("loc_2756")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2772")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_277C")

    label("loc_2772")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_277C")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2966")

    ChrTalk(    #87
        0x9,
        (
            "#051FYo, Estelle.\x02\x03",

            "You walkin' around AGAIN?\x01",
            "You're like a perpetual motion\x01",
            "machine, you know that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#1011FHeehee. I guess so, yeah.\x02\x03",

            "What are you doing, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "#050FJust sittin' back and relaxing\x01",
            "while we can.\x02\x03",

            "...Winding down, basically.\x02\x03",

            "That is why we came out here, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1001FHeck yeah, it is!\x01",
            "You gotta relax sometime.\x02\x03",

            "It won't hurt to take one day off of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "#051FHeh. Darn right.\x02\x03",

            "Anyway, see ya.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C30)
    Jump("loc_29E0")

    label("loc_2966")


    ChrTalk(    #92
        0x9,
        (
            "#051FIt ain't too bad to just kick back and\x01",
            "enjoy the breeze every now an' again.\x02\x03",

            "Anyway, I'll be here till dinner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E0")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_11_259A end

    def Function_12_29E9(): pass

    label("Function_12_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF9")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A85")
    Jump("loc_2AC7")

    label("loc_2A85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AA1")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AC7")

    label("loc_2AA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ABD")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AC7")

    label("loc_2ABD")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AC7")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Call(0, 27)
    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    label("loc_2AF9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B89")
    Jump("loc_2BCB")

    label("loc_2B89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BA5")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BCB")

    label("loc_2BA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BC1")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BCB")

    label("loc_2BC1")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BCB")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF4")

    ChrTalk(    #93
        0xA,
        (
            "#031FAh, good day, Estelle.\x02\x03",

            "The finest liquor, the freshest food...\x01",
            "Indeed, it is the picture of refinement!\x02\x03",

            "If I had a lovely lady pouring my drinks,\x01",
            "then I would have no complaints at all...\x02\x03",

            "But, oh, that can be saved for AFTER dinner!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2DD2")

    label("loc_2CF4")


    ChrTalk(    #94
        0xA,
        (
            "#031FThe finest liquor, the freshest food...\x01",
            "Indeed, it is the picture of refinement.\x02\x03",

            "If I had a lovely lady pouring my drinks,\x01",
            "then I would have no complaints at all...\x02\x03",

            "But, oh, that can be saved for AFTER dinner!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD2")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_12_29E9 end

    def Function_13_2DDB(): pass

    label("Function_13_2DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EEB")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E77")
    Jump("loc_2EB9")

    label("loc_2E77")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E93")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB9")

    label("loc_2E93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EAF")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB9")

    label("loc_2EAF")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB9")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Call(0, 28)
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    label("loc_2EEB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F7B")
    Jump("loc_2FBD")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F97")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FBD")

    label("loc_2F97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FB3")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FBD")

    label("loc_2FB3")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FBD")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #95
        0xB,
        (
            "#040FI'm certain that the sun's reflection on\x01",
            "Valleria Lake must be quite breathtaking.\x02\x03",

            "#40FI think I may go view it myself from\x01",
            "the terrace.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_13_2DDB end

    def Function_14_307F(): pass

    label("Function_14_307F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_318F")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_311B")
    Jump("loc_315D")

    label("loc_311B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3137")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_315D")

    label("loc_3137")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3153")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_315D")

    label("loc_3153")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_315D")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Call(0, 25)
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    label("loc_318F")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_321F")
    Jump("loc_3261")

    label("loc_321F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_323B")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3261")

    label("loc_323B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3257")
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3261")

    label("loc_3257")

    OP_51(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3261")

    OP_51(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(    #96
        0xC,
        (
            "#060FI think I want a little more tea.\x02\x03",

            "I'll see you after dinner, Estelle!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    TalkEnd(0xC)
    Return()

    # Function_14_307F end

    def Function_15_32E0(): pass

    label("Function_15_32E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33F0")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_337C")
    Jump("loc_33BE")

    label("loc_337C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3398")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33BE")

    label("loc_3398")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33B4")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_33BE")

    label("loc_33B4")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33BE")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Call(0, 29)
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    label("loc_33F0")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3480")
    Jump("loc_34C2")

    label("loc_3480")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_349C")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34C2")

    label("loc_349C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34B8")
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34C2")

    label("loc_34B8")

    OP_51(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34C2")

    OP_51(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    ChrTalk(    #97
        0xD,
        (
            "#070FGoing fishing again?\x02\x03",

            "#071FHaha, well, don't get so absorbed that\x01",
            "you forget about dinner!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    TalkEnd(0xD)
    Return()

    # Function_15_32E0 end

    def Function_16_3555(): pass

    label("Function_16_3555")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35E5")
    Jump("loc_3627")

    label("loc_35E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3601")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3627")

    label("loc_3601")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_361D")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3627")

    label("loc_361D")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3627")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_365F")
    Call(0, 30)
    Jump("loc_37B6")

    label("loc_365F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_374C")

    ChrTalk(    #98
        0xE,
        (
            "#1064FOh, heya, Estelle!\x02\x03",

            "Already feeling 'tead' out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1025FNot really.\x01",
            "Schera's still relaxing in her room.\x02\x03",

            "I just wanted to get outside for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xE,
        (
            "#1060F...\x02\x03",

            "All right. Well, try and get back\x01",
            "before dark!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C31)
    Jump("loc_37B6")

    label("loc_374C")


    ChrTalk(    #101
        0xE,
        (
            "#1062FIf you're gonna go enjoy the sights,\x01",
            "now's the time.\x02\x03",

            "Just make sure and get back before\x01",
            "dark!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B6")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_16_3555 end

    def Function_17_37BF(): pass

    label("Function_17_37BF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37D6")
    Call(0, 56)
    Call(0, 57)

    label("loc_37D6")

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
        (2, "loc_389C"),
        (5, "loc_38A4"),
        (3, "loc_38AC"),
        (4, "loc_38B4"),
        (6, "loc_38BC"),
        (7, "loc_38C4"),
        (SWITCH_DEFAULT, "loc_38CC"),
    )


    label("loc_389C")

    SetChrChipByIndex(0xFA, 0)
    Jump("loc_38CC")

    label("loc_38A4")

    SetChrChipByIndex(0xFA, 1)
    Jump("loc_38CC")

    label("loc_38AC")

    SetChrChipByIndex(0xFA, 2)
    Jump("loc_38CC")

    label("loc_38B4")

    SetChrChipByIndex(0xFA, 3)
    Jump("loc_38CC")

    label("loc_38BC")

    SetChrChipByIndex(0xFA, 4)
    Jump("loc_38CC")

    label("loc_38C4")

    SetChrChipByIndex(0xFA, 5)
    Jump("loc_38CC")

    label("loc_38CC")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xFB)"), scpexpr(EXPR_END)),
        (2, "loc_38ED"),
        (5, "loc_38F5"),
        (3, "loc_38FD"),
        (4, "loc_3905"),
        (6, "loc_390D"),
        (7, "loc_3915"),
        (SWITCH_DEFAULT, "loc_391D"),
    )


    label("loc_38ED")

    SetChrChipByIndex(0xFB, 0)
    Jump("loc_391D")

    label("loc_38F5")

    SetChrChipByIndex(0xFB, 1)
    Jump("loc_391D")

    label("loc_38FD")

    SetChrChipByIndex(0xFB, 2)
    Jump("loc_391D")

    label("loc_3905")

    SetChrChipByIndex(0xFB, 3)
    Jump("loc_391D")

    label("loc_390D")

    SetChrChipByIndex(0xFB, 4)
    Jump("loc_391D")

    label("loc_3915")

    SetChrChipByIndex(0xFB, 5)
    Jump("loc_391D")

    label("loc_391D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xFC)"), scpexpr(EXPR_END)),
        (2, "loc_393E"),
        (5, "loc_3946"),
        (3, "loc_394E"),
        (4, "loc_3956"),
        (6, "loc_395E"),
        (7, "loc_3966"),
        (SWITCH_DEFAULT, "loc_396E"),
    )


    label("loc_393E")

    SetChrChipByIndex(0xFC, 0)
    Jump("loc_396E")

    label("loc_3946")

    SetChrChipByIndex(0xFC, 1)
    Jump("loc_396E")

    label("loc_394E")

    SetChrChipByIndex(0xFC, 2)
    Jump("loc_396E")

    label("loc_3956")

    SetChrChipByIndex(0xFC, 3)
    Jump("loc_396E")

    label("loc_395E")

    SetChrChipByIndex(0xFC, 4)
    Jump("loc_396E")

    label("loc_3966")

    SetChrChipByIndex(0xFC, 5)
    Jump("loc_396E")

    label("loc_396E")

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
        "#1062F#6PAnd here's the rest of them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1004F#2PWha...?!\x02",
    )

    CloseMessageWindow()

    def lambda_3A5D():
        OP_6D(18360, 0, 9200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A5D)

    def lambda_3A75():
        OP_67(0, 5410, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_3A75)

    def lambda_3A8D():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A8D)
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
        "#1008FKevin! What are you doing here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xE,
        "#1061FOoooh, it's a long and harrowing story!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B95")

    ChrTalk(    #106
        0x103,
        (
            "#027F#6PWe happened to run into him on the road...\x02\x03",

            "...so we invited him to join us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEC")

    label("loc_3B95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3BEF")

    ChrTalk(    #107
        0x108,
        (
            "#070F#6PWe passed by him on the road.\x02\x03",

            "So we invited him to join us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEC")

    label("loc_3BEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3C4D")

    ChrTalk(    #108
        0x107,
        (
            "#061F#6PWe met Mr. Kevin on the road here.\x02\x03",

            "We invited him to come, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CEC")

    label("loc_3C4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3CEC")

    ChrTalk(    #109
        0x104,
        (
            "#035F#6PWe encountered sir fledgling knight wandering\x01",
            "like a lost chick on the roads.\x02\x03",

            "#030FIt felt right to invite him to join our holiday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CEC")


    ChrTalk(    #110
        0x101,
        (
            "#1015FOn the road?\x01",
            "Why were you traveling again, Kevin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xE,
        (
            "#1060FTo be honest, my goal was to investigate\x01",
            "the Amberl Tower.\x02\x03",

            "After we said our goodbyes in Rolent\x01",
            "I've been runnin' around looking\x01",
            "into all the towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x101,
        "#1004FAll the towers?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E59")

    ChrTalk(    #113
        0x106,
        (
            "#052FThat makes it sound like you've visited\x01",
            "the others already.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5A")

    label("loc_3E59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAE")

    ChrTalk(    #114
        0x105,
        (
            "#044FHave you already visited the other towers,\x01",
            "Father Graham?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5A")

    label("loc_3EAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0A")

    ChrTalk(    #115
        0x104,
        (
            "#032FHm. From your tone, I take it you have\x01",
            "visited the other towers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F5A")

    label("loc_3F0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F5A")

    ChrTalk(    #116
        0x103,
        (
            "#023FI'm curious, have you visited the\x01",
            "other towers already?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F5A")


    ChrTalk(    #117
        0xE,
        (
            "#1068FYep, I've been busy with that, pretty\x01",
            "much.\x02\x03",

            "That's why I was kinda AWOL during the\x01",
            "whole dragon business... Sorry I couldn't\x01",
            "give a hand with that.\x02\x03",

            "#1066FI figured you guys might come out here\x01",
            "for a break after that, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1011FThat makes sense.\x02\x03",

            "#1006FWell, then! Should we have a\x01",
            "sit-down right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xE,
        (
            "#1060FHowsabout we do it over dinner?\x02\x03",

            "That'll help the, uh, information flow\x01",
            "freely, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1001FOh, yeah!\x02\x03",

            "#1004F...Er, so you're really staying here,\x01",
            "Kevin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xE,
        (
            "#1061FHahaha! Wellll, from what I hear, this\x01",
            "is a pretty famous inn, right?\x02\x03",

            "#1062FLike your friends said, I figured I'd join\x01",
            "in the festivities...if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016FThat's, uh, kind of out of the blue.\x02\x03",

            "#1006FYou have helped us out a LOT, though...\x02\x03",

            "What do you think, guys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x106,
        "#051FI ain't got a problem with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#021FHmmmm, it IS a nice way to settle\x01",
            "our debt to the good Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x107,
        "#061FHeehee... Yeah, I want him to stay too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        "#035FI see no reason to object.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x105,
        (
            "#048FHaha... I wonder if it's fate\x01",
            "bringing us together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x108,
        "#071FWell, if he's here, let's have some fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xE,
        (
            "#1061FThank ya!\x02\x03",

            "#1062FAin't much in the way of thanks, but if\x01",
            "you've still got stuff that needs doin',\x01",
            "I'd be happy to tag along.\x02\x03",

            "Abuse me as much as you need!\x02",
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
            "Still Have Business\x01",      # 0
            "Party Time\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x1C02)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4740")

    ChrTalk(    #130
        0x101,
        (
            "#1025FMmm, well.\x02\x03",

            "Thanks for the offer, but I think we're\x01",
            "about ready to drop off our things and\x01",
            "relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "#1064FAwww, really?\x02\x03",

            "#1068FDarn it all. And here I was thinking\x01",
            "I could give up my body to Estelle's\x01",
            "cause!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1019FOh, if you want to sacrifice your body,\x01",
            "trust me, there are ways to arrange\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#067FHeehee...!\x02",
    )

    CloseMessageWindow()
    OP_28(0x97, 0x1, 0x10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4652")

    ChrTalk(    #134
        0x106,
        "#051FAll right, let's get checked in and everything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4722")

    label("loc_4652")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4692")

    ChrTalk(    #135
        0x103,
        (
            "#021FCome on, then.\x01",
            "Let's get checked in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4722")

    label("loc_4692")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46CC")

    ChrTalk(    #136
        0x108,
        "#071FShall we get checked in, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4722")

    label("loc_46CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4722")

    ChrTalk(    #137
        0x104,
        (
            "#031FHeh... Come! Let us check in and\x01",
            "begin the labor of relaxing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4722")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 23)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_4830")

    label("loc_4740")


    ChrTalk(    #138
        0x101,
        (
            "#1016FSure! Well, if you want to help\x01",
            "with something, Kevin...\x02",
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

    label("loc_4830")

    Return()

    # Function_17_37BF end

    def Function_18_4831(): pass

    label("Function_18_4831")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4632, 0x0, 0x1CE8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_4831 end

    def Function_19_4875(): pass

    label("Function_19_4875")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x493E, 0x0, 0x193C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_4875 end

    def Function_20_48B9(): pass

    label("Function_20_48B9")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x43D0, 0x0, 0x17DE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_48B9 end

    def Function_21_48FD(): pass

    label("Function_21_48FD")

    OP_8E(0xFE, 0x4286, 0x0, 0xE38, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4358, 0x0, 0x13B0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_21_48FD end

    def Function_22_492D(): pass

    label("Function_22_492D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4966")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4966")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_499F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4987")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_498B")

    label("loc_4987")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_498B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_499F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C0")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_49D8")

    label("loc_49C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D4")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_49D8")

    label("loc_49D4")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_49D8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A39")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0D")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_4A25")

    label("loc_4A0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A21")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_4A25")

    label("loc_4A21")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_4A25")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A86")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5A")
    AddParty(0x2, 0xFA, 0xFF)
    Jump("loc_4A72")

    label("loc_4A5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A6E")
    AddParty(0x2, 0xFB, 0xFF)
    Jump("loc_4A72")

    label("loc_4A6E")

    AddParty(0x2, 0xFC, 0xFF)

    label("loc_4A72")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AAB")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AAB")

    Return()

    # Function_22_492D end

    def Function_23_4AAC(): pass

    label("Function_23_4AAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4ABC")
    RemoveParty(0x7, 0xFF)

    label("loc_4ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4ACC")
    RemoveParty(0x4, 0xFF)

    label("loc_4ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4ADC")
    RemoveParty(0x6, 0xFF)

    label("loc_4ADC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4AEC")
    RemoveParty(0x3, 0xFF)

    label("loc_4AEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4AFC")
    RemoveParty(0x5, 0xFF)

    label("loc_4AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4B0C")
    RemoveParty(0x2, 0xFF)

    label("loc_4B0C")

    Return()

    # Function_23_4AAC end

    def Function_24_4B0D(): pass

    label("Function_24_4B0D")


    ChrTalk(    #139
        0x9,
        (
            "#051FYo, you've been out there a while.\x02\x03",

            "Finally done with business?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BCF"),
        (1, "loc_4C56"),
        (2, "loc_4CA7"),
        (SWITCH_DEFAULT, "loc_4CF3"),
    )


    label("loc_4BCF")


    ChrTalk(    #140
        0x9,
        (
            "#052FYou're seriously not done yet?\x02\x03",

            "#053FTry not to forget we're on vacation.\x01",
            "Finish up and come back here.\x01",
            "We'll be waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF3")

    label("loc_4C56")


    ChrTalk(    #141
        0x9,
        (
            "#053FHeh, good.\x02\x03",

            "#051FLet's get checked in, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_4CF3")

    label("loc_4CA7")


    ChrTalk(    #142
        0x9,
        "#052FWhat? You need to change up your team?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_4CF3")

    label("loc_4CF3")

    Return()

    # Function_24_4B0D end

    def Function_25_4CF4(): pass

    label("Function_25_4CF4")


    ChrTalk(    #143
        0xC,
        (
            "#560FAh, Estelle!\x02\x03",

            "Done with everything?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D9A"),
        (1, "loc_4DF6"),
        (2, "loc_4E55"),
        (SWITCH_DEFAULT, "loc_4EAB"),
    )


    label("loc_4D9A")


    ChrTalk(    #144
        0xC,
        (
            "#064FHuh? Really?\x02\x03",

            "#061FWell, okay, but don't take too long!\x01",
            "We'll be waiting here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4DF6")


    ChrTalk(    #145
        0xC,
        (
            "#560FYay! Okay!\x02\x03",

            "#061FLet's let the inn people know we're here!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_4EAB")

    label("loc_4E55")


    ChrTalk(    #146
        0xC,
        (
            "#560FOh, okay, Estelle.\x01",
            "Do you want me in your party?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_4EAB")

    label("loc_4EAB")

    Return()

    # Function_25_4CF4 end

    def Function_26_4EAC(): pass

    label("Function_26_4EAC")


    ChrTalk(    #147
        0x8,
        (
            "#020FAh, Estelle!\x02\x03",

            "Finally done with your work?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F59"),
        (1, "loc_4FD9"),
        (2, "loc_5027"),
        (SWITCH_DEFAULT, "loc_5076"),
    )


    label("loc_4F59")


    ChrTalk(    #148
        0x8,
        (
            "#023FReally? Still not done?\x02\x03",

            "#020FDon't kill yourself with work, Estelle.\x01",
            "We'll wait here, so finish up and come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5076")

    label("loc_4FD9")


    ChrTalk(    #149
        0x8,
        (
            "#021FExcellent!\x02\x03",

            "#020FLet's go check in, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_5076")

    label("loc_5027")


    ChrTalk(    #150
        0x8,
        "#023FOh? You need to alter your team a little?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_5076")

    label("loc_5076")

    Return()

    # Function_26_4EAC end

    def Function_27_5077(): pass

    label("Function_27_5077")


    ChrTalk(    #151
        0xA,
        (
            "#030FAh, Estelle!\x02\x03",

            "Have you finished your heavy labors?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_512C"),
        (1, "loc_51A5"),
        (2, "loc_5210"),
        (SWITCH_DEFAULT, "loc_526F"),
    )


    label("loc_512C")


    ChrTalk(    #152
        0xA,
        (
            "#033FYou have not? Surprising.\x02\x03",

            "#035FHeh, well, we shall wait here diligently\x01",
            "for you. Return when you are able.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_526F")

    label("loc_51A5")


    ChrTalk(    #153
        0xA,
        (
            "#035FHeh, wonderful.\x02\x03",

            "#030FLet us announce our presence to\x01",
            "the staff, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_526F")

    label("loc_5210")


    ChrTalk(    #154
        0xA,
        (
            "#035FYou are in need of my genius, then?\x01",
            "It is not surprising.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_526F")

    label("loc_526F")

    Return()

    # Function_27_5077 end

    def Function_28_5270(): pass

    label("Function_28_5270")


    ChrTalk(    #155
        0xB,
        (
            "#040FHello, Estelle.\x02\x03",

            "Have you finished whatever business you had?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5330"),
        (1, "loc_53A1"),
        (2, "loc_53F0"),
        (SWITCH_DEFAULT, "loc_5445"),
    )


    label("loc_5330")


    ChrTalk(    #156
        0xB,
        (
            "#044FYou haven't? I see.\x02\x03",

            "#041FWe will wait here for you, then.\x01",
            "Please, hurry back when you're finished.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5445")

    label("loc_53A1")


    ChrTalk(    #157
        0xB,
        (
            "#041FWonderful!\x02\x03",

            "#048FWe should check in, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_5445")

    label("loc_53F0")


    ChrTalk(    #158
        0xB,
        (
            "#040FI see. You wish to change\x01",
            "your traveling party?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_5445")

    label("loc_5445")

    Return()

    # Function_28_5270 end

    def Function_29_5446(): pass

    label("Function_29_5446")


    ChrTalk(    #159
        0xD,
        (
            "#070FHey! Hope you haven't had trouble.\x02\x03",

            "All done with your work?\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5505"),
        (1, "loc_556B"),
        (2, "loc_55C7"),
        (SWITCH_DEFAULT, "loc_5609"),
    )


    label("loc_5505")


    ChrTalk(    #160
        0xD,
        (
            "#073FOh, all right then.\x02\x03",

            "#070FWe will be waiting here, so return\x01",
            "whenever you have finished.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5609")

    label("loc_556B")


    ChrTalk(    #161
        0xD,
        (
            "#073FOh! Really?\x02\x03",

            "#071FLet's check in and get settled, then!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_5609")

    label("loc_55C7")


    ChrTalk(    #162
        0xD,
        "#073FAhh, changing party members?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_5609")

    label("loc_5609")

    Return()

    # Function_29_5446 end

    def Function_30_560A(): pass

    label("Function_30_560A")


    ChrTalk(    #163
        0xE,
        (
            "#1062FHey, Estelle!\x02\x03",

            "If you still got some business,\x01",
            "want me to help? My body is ready!\x02",
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
            "Still Have Business\x01",      # 0
            "Let's Relax\x01",              # 1
            "Change Party\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_56DF"),
        (1, "loc_5750"),
        (2, "loc_57C4"),
        (SWITCH_DEFAULT, "loc_5813"),
    )


    label("loc_56DF")


    ChrTalk(    #164
        0xE,
        (
            "#1064FWhat, you ain't bringin' me along?\x02\x03",

            "#1060FI guess I'll just have to chill\x01",
            "here until you get back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5813")

    label("loc_5750")


    ChrTalk(    #165
        0xE,
        (
            "#1064FReally? Darn.\x02\x03",

            "#1061FEr, can't complain too much, I guess!\x01",
            "Let's go get rooms.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1510   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_5813")

    label("loc_57C4")


    ChrTalk(    #166
        0xE,
        (
            "#1061FAlllll right, then!\x01",
            "Show me where to go!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 31)
    FadeToBright(300, 0)
    Jump("loc_5813")

    label("loc_5813")

    Return()

    # Function_30_560A end

    def Function_31_5814(): pass

    label("Function_31_5814")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D2")
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 18100, 200, 8820, 270)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)

    label("loc_58D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_593A")
    SetChrFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5910")
    SetChrPos(0x9, 18100, 200, 8820, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_592B")

    label("loc_5910")

    SetChrPos(0x9, 18100, 200, 10270, 270)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_592B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)

    label("loc_593A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59CD")
    SetChrFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5978")
    SetChrPos(0xA, 18100, 200, 8820, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59BE")

    label("loc_5978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A3")
    SetChrPos(0xA, 18100, 200, 10270, 270)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59BE")

    label("loc_59A3")

    SetChrPos(0xA, 15510, 200, 10470, 90)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)

    label("loc_59CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A8B")
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A0B")
    SetChrPos(0xB, 18100, 200, 8820, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A7C")

    label("loc_5A0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A36")
    SetChrPos(0xB, 18100, 200, 10270, 270)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A7C")

    label("loc_5A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A61")
    SetChrPos(0xB, 15510, 200, 10470, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A7C")

    label("loc_5A61")

    SetChrPos(0xB, 15510, 200, 9020, 90)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A7C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)

    label("loc_5A8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B49")
    SetChrFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AC9")
    SetChrPos(0xC, 18100, 200, 8820, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B3A")

    label("loc_5AC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF4")
    SetChrPos(0xC, 18100, 200, 10270, 270)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B3A")

    label("loc_5AF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B1F")
    SetChrPos(0xC, 15510, 200, 10470, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B3A")

    label("loc_5B1F")

    SetChrPos(0xC, 15510, 200, 9020, 90)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B3A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)

    label("loc_5B49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C07")
    SetChrFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B87")
    SetChrPos(0xD, 18100, 200, 8820, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF8")

    label("loc_5B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB2")
    SetChrPos(0xD, 18100, 200, 10270, 270)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF8")

    label("loc_5BB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BDD")
    SetChrPos(0xD, 15510, 200, 10470, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5BF8")

    label("loc_5BDD")

    SetChrPos(0xD, 15510, 200, 9020, 90)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)

    label("loc_5C07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CBB")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C45")
    SetChrPos(0xE, 18100, 200, 8820, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CB6")

    label("loc_5C45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C70")
    SetChrPos(0xE, 18100, 200, 10270, 0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CB6")

    label("loc_5C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C9B")
    SetChrPos(0xE, 15510, 200, 10470, 90)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CB6")

    label("loc_5C9B")

    SetChrPos(0xE, 15510, 200, 9020, 90)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CB6")

    ClearChrFlags(0xE, 0x80)

    label("loc_5CBB")

    Return()

    # Function_31_5814 end

    def Function_32_5CBC(): pass

    label("Function_32_5CBC")

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
            "#6PThank you very much for choosing to\x01",
            "stay at the Kingfisher Inn!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xF,
        "#6PAllow me to show you to your rooms.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1006F#7PYes, please do.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 90, 400)

    def lambda_5EA5():
        OP_6D(80870, 0, 13830, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5EA5)
    OP_43(0xF, 0x1, 0x0, 0x21)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #170
        0xF,
        (
            "#6PThis is the room we have set aside\x01",
            "for the ladies...\x02",
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

    def lambda_5FF6():
        OP_6D(108140, 0, 12550, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FF6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #171
        0xC,
        "#061F#3PWow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xB,
        "#048F#3PThis is lovely! It feels peaceful, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#1006F#5PThis is the room we used the last time\x01",
            "we stayed here, right?\x02\x03",

            "We ended up having to sneak into the\x01",
            "bandit base and didn't really get to\x01",
            "enjoy it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xF,
        (
            "#5PHaha, yes. I hope you can spend\x01",
            "a bit more time in it this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "#035F#5PHeh, I did at least get to spend one night\x01",
            "in a comfortable bed that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #176
        0x101,
        (
            "#1019F#2PThe way I remember it, Schera drank you\x01",
            "under the table and laid you out like\x01",
            "a sack of garbage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#021F#5PHeehee! This time I'll be able to\x01",
            "drink to my heart's content.\x02",
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

    def lambda_6369():
        OP_6D(54890, 0, 25840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6369)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #178
        0xF,
        (
            "#5PThis is the room we had set aside for\x01",
            "the gentlemen, but...\x02\x03",

            "I'm sorry, there must have been some confusion\x01",
            "about your party size. You may use the room\x01",
            "next door for the men, as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 45, 400)

    ChrTalk(    #179
        0xE,
        (
            "#1062FAh, right, I kind of jumped on this train\x01",
            "at the last second. You guys pick rooms\x01",
            "and I'll roll with it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 315, 400)

    ChrTalk(    #180
        0xD,
        (
            "#073F#4PHow about it?\x01",
            "I have no preference.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #181
        0x9,
        "#051F#5PI don't care much either way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        (
            "#035F#3PHeh... Well, then!\x01",
            "I shall share a room with Agate.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #183
        0x9,
        (
            "#555F#5P...Wait a second.\x02\x03",

            "What's with the sudden desire\x01",
            "to bunk with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xA,
        (
            "#031F#3PHa-ha-ha! Is it not obvious, Agate?\x02\x03",

            "#037FA Raven with clipped wings, mended by a\x01",
            "tender-hearted young girl...\x02\x03",

            "I would be a failure of a bard if I did\x01",
            "not hear EVERY detail of that encounter!\x01",
            "And also...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xC,
        "#064F#4PHuuuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#055F#5PWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1007F#3PAgate, TRY not to murder him, okay?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    Sleep(500)

    ChrTalk(    #188
        0x101,
        (
            "#1028F#3PAlthoooough, I'm sorta curious as to\x01",
            "how that went down myself...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 315, 400)

    ChrTalk(    #189
        0xC,
        "#065F#4PB-But, we just talked is all!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #190
        0x8,
        (
            "#021F#4PThat doesn't make us any less interested\x01",
            "in hearing about it--maybe more so, in fact.\x02\x03",

            "#027FPerhaps we should hear the whole story\x01",
            "before calling it a night, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xC,
        "#562F#4PAwwww...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 315, 400)

    ChrTalk(    #192
        0xB,
        (
            "#045FCome now, you two...\x02\x03",

            "#542FDon't tease Tita so much.\x01",
            "I feel bad for her.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    def lambda_68E7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_68E7)

    def lambda_68F5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68F5)

    def lambda_6903():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6903)

    def lambda_6911():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6911)
    Sleep(500)

    ChrTalk(    #193
        0xA,
        (
            "#031F#3PHeh... Regardless! I would ask Zin\x01",
            "and Kevin to share the other room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xD,
        "#071F#4PI have no problem with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xE,
        (
            "#1061F#2PHey, I'm not one to stand in the\x01",
            "way of a good time, so sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xF,
        (
            "#5PAllow me to show you to\x01",
            "your room.\x02",
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

    def lambda_6A78():
        OP_6D(55620, 0, 25780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A78)
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
            "#055F#5PN-Now hang on! We are NOT DONE with\x01",
            "this conversation! Hey!\x02",
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

    # Function_32_5CBC end

    def Function_33_6B43(): pass

    label("Function_33_6B43")

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

    # Function_33_6B43 end

    def Function_34_6B89(): pass

    label("Function_34_6B89")

    OP_8E(0xFE, 0x13920, 0x0, 0x3192, 0x7D0, 0x0)
    Return()

    # Function_34_6B89 end

    def Function_35_6B9E(): pass

    label("Function_35_6B9E")

    OP_8E(0xFE, 0x134E8, 0x0, 0x3192, 0x7D0, 0x0)
    Return()

    # Function_35_6B9E end

    def Function_36_6BB3(): pass

    label("Function_36_6BB3")

    OP_8E(0xFE, 0x136DC, 0x0, 0x2EB8, 0x7D0, 0x0)
    Return()

    # Function_36_6BB3 end

    def Function_37_6BC8(): pass

    label("Function_37_6BC8")

    OP_8E(0xFE, 0x13362, 0x0, 0x2EB8, 0x7D0, 0x0)
    Return()

    # Function_37_6BC8 end

    def Function_38_6BDD(): pass

    label("Function_38_6BDD")

    OP_8E(0xFE, 0x132A4, 0x0, 0x2AE4, 0x7D0, 0x0)
    Return()

    # Function_38_6BDD end

    def Function_39_6BF2(): pass

    label("Function_39_6BF2")

    OP_8E(0xFE, 0x1357E, 0x0, 0x28E6, 0x7D0, 0x0)
    Return()

    # Function_39_6BF2 end

    def Function_40_6C07(): pass

    label("Function_40_6C07")

    OP_8E(0xFE, 0x139D4, 0x0, 0x14DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1397A, 0x0, 0x2918, 0x7D0, 0x0)
    Return()

    # Function_40_6C07 end

    def Function_41_6C30(): pass

    label("Function_41_6C30")

    TurnDirection(0xFE, 0x8, 400)
    OP_8E(0xFE, 0x13844, 0x0, 0x1590, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13844, 0x0, 0x262A, 0x7D0, 0x0)
    Return()

    # Function_41_6C30 end

    def Function_42_6C60(): pass

    label("Function_42_6C60")

    OP_8C(0xFE, 90, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_6C60 end

    def Function_43_6C91(): pass

    label("Function_43_6C91")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_6C91 end

    def Function_44_6CC2(): pass

    label("Function_44_6CC2")

    OP_8C(0xFE, 0, 400)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_44_6CC2 end

    def Function_45_6D01(): pass

    label("Function_45_6D01")

    OP_8C(0xFE, 180, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_45_6D01 end

    def Function_46_6D46(): pass

    label("Function_46_6D46")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_46_6D46 end

    def Function_47_6D8B(): pass

    label("Function_47_6D8B")

    OP_8C(0xFE, 45, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_47_6D8B end

    def Function_48_6DD0(): pass

    label("Function_48_6DD0")

    TurnDirection(0xFE, 0x8, 400)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_48_6DD0 end

    def Function_49_6E15(): pass

    label("Function_49_6E15")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xC814, 0x0, 0x5DC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xD7B4, 0x0, 0x655E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE092, 0x0, 0x655E, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_49_6E15 end

    def Function_50_6E67(): pass

    label("Function_50_6E67")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
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

    def lambda_6F80():
        OP_6D(110740, 350, 8100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F80)

    def lambda_6F98():
        OP_67(0, 6440, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F98)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    def lambda_6FBF():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FBF)
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

    def lambda_7007():
        OP_99(0xFE, 0x8, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7007)
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

    def lambda_707E():
        OP_6D(110750, 0, 7280, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_707E)
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

    def lambda_70FB():
        OP_6D(106910, 0, 6690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70FB)
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
    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #198
        (
            "\x07\x05Setting aside their cares for a while, they\x01",
            "slumbered peacefully and awoke as they\x01",
            "wished come the dawn...\x02",
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

    # Function_50_6E67 end

    def Function_51_7219(): pass

    label("Function_51_7219")

    Sleep(200)
    OP_62(0xFE, 0x190, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xFE, 2)
    Sleep(300)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_51_7219 end

    def Function_52_7245(): pass

    label("Function_52_7245")

    Sleep(200)
    OP_62(0xFE, 0x1F4, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Return()

    # Function_52_7245 end

    def Function_53_7274(): pass

    label("Function_53_7274")

    Sleep(200)
    OP_62(0xFE, 0x320, 1300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Sleep(500)
    OP_99(0xFE, 0x8, 0xA, 0x3E8)
    Return()

    # Function_53_7274 end

    def Function_54_72A8(): pass

    label("Function_54_72A8")

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

    def lambda_73CC():
        OP_6D(109020, 200, 13230, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73CC)

    def lambda_73E4():
        OP_67(0, 6120, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73E4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #199
        0x101,
        "#1001F#4PAhhhh, that was so much fun. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xC,
        "#061F#5PHeehee... It was, it was! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "#048FHaha. It feels like we've been refreshed,\x01",
            "body and soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        (
            "#021F#4PYes... It's been a while since I've had\x01",
            "this much fun without drinking.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #203
        0x101,
        (
            "#1019F#6PSchera. Minors in the room.\x01",
            "Influences. Et cetera.\x02\x03",

            "And weren't you slamming back some\x01",
            "kind of fruit liqueur like a fiend while we\x01",
            "were fishing?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #204
        0x8,
        (
            "#027F#4POh, honey, please.\x01",
            "Something that light doesn't even count.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(400)

    ChrTalk(    #205
        0x8,
        "#021F#4PRight, Princess, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xC,
        "#067F#5PUmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xB,
        (
            "#045FHaha... I think I will invoke, ah,\x01",
            "royal prerogative to refrain from\x01",
            "commenting.\x02\x03",

            "#040FOn a tangent from that, though.\x01",
            "Estelle, you're really very good at fishing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #208
        0x101,
        "#1008F#4PHeheh, you think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xC,
        (
            "#061F#5PYeah, you are!\x01",
            "You pulled them up one after another!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#021F#4PIt's been her hobby since she was little.\x02\x03",

            "#020FSpeaking of... Kevin made quite a showing\x01",
            "for himself, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#1006F#4PI noticed that.\x01",
            "He really seems to like fishing.\x02\x03",

            "He definitely knows how to handle a rod\x01",
            "and whatnot, that's for sure.\x02\x03",

            "#1001FIf he got a bit better, he might even\x01",
            "make a good rival for me. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#025F#4PFor the love of... Not everything has\x01",
            "to be a competition, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xC,
        "#061F#5PHeehee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xB,
        (
            "#041FHaha.\x02\x03",

            "#048FStill, though... It's a lovely evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#1004F#2PAh...\x02",
    )

    CloseMessageWindow()

    def lambda_7974():
        OP_6D(109140, 200, 15670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7974)

    def lambda_798C():
        OP_67(0, 7540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_798C)

    def lambda_79A4():
        OP_6C(28000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79A4)

    def lambda_79B4():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_79B4)
    Sleep(1000)
    SetChrSubChip(0x101, 2)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #216
        0x101,
        "#1026F#2P...\x02",
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
        "#044FHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xC,
        "#064F#5PEstelle? What is it?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #219
        0x101,
        "#1016F#4PAh, nothing.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 109200, 0, 14020, 0)
    ClearChrFlags(0x101, 0x4)

    def lambda_7AE4():
        OP_6D(108880, 0, 13830, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AE4)

    def lambda_7AFC():
        OP_67(0, 6300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AFC)
    Sleep(1000)
    OP_8C(0x101, 225, 300)
    Sleep(500)

    ChrTalk(    #220
        0x101,
        (
            "#1025F#6PI think I...need to go enjoy that\x01",
            "lovely evening for a bit.\x02\x03",

            "I'll be back for dinner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x8,
        (
            "#020F#4PI understand.\x02\x03",

            "#021FDon't be gone too late or I'll\x01",
            "eat your portion, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1016F#6PHaha! Yeah, I know, I know.\x02\x03",

            "#1006FSee you guys later!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x1A7A2, 0x0, 0x3804, 0x7D0, 0x0)
    OP_8E(0x101, 0x19FD2, 0x0, 0x3822, 0x7D0, 0x0)

    def lambda_7C59():
        OP_6D(108160, 0, 13580, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C59)

    def lambda_7C71():
        OP_6C(53000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C71)

    def lambda_7C81():
        OP_8E(0xFE, 0x197EE, 0x0, 0x3278, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C81)
    SetChrSubChip(0xB, 1)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_7CC1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CC1)
    OP_8E(0x101, 0x19064, 0x0, 0x32F0, 0x7D0, 0x0)
    SetChrFlags(0x101, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_22(0x7, 0x0, 0x64)

    ChrTalk(    #223
        0xC,
        "#065F#5PEstelle...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_7D13():
        OP_6D(109020, 200, 13230, 1600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D13)
    SetChrSubChip(0xC, 0)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #224
        0xC,
        "#063F#5PSchera, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        (
            "#524F#4PDon't worry, Tita.\x02\x03",

            "I'd like you to leave her alone\x01",
            "for a little while, if that's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xB,
        "#043FThis is about Joshua, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xC,
        "#065F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x8,
        "#026F#4PHmm... A good guess.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(1000)

    ChrTalk(    #229
        0x8,
        (
            "#522F#4PThe evening was just as lovely\x01",
            "back then, too...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x381, 0x0)"), scpexpr(EXPR_END)), "loc_7EB7")
    OP_3F(0x381, 1)
    OP_3E(0x41B, 1)

    label("loc_7EB7")

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

    # Function_54_72A8 end

    def Function_55_7F4E(): pass

    label("Function_55_7F4E")

    EventBegin(0x0)
    OP_DB()
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

    def lambda_8022():
        OP_6D(17060, 0, 9800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8022)

    def lambda_803A():
        OP_67(0, 8000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_803A)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_55_7F4E end

    def Function_56_8079(): pass

    label("Function_56_8079")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_80F5"),
        (1, "loc_80FB"),
        (SWITCH_DEFAULT, "loc_8101"),
    )


    label("loc_80F5")

    OP_A2(0x1200)
    Jump("loc_8101")

    label("loc_80FB")

    OP_A2(0x1201)
    Jump("loc_8101")

    label("loc_8101")

    Return()

    # Function_56_8079 end

    def Function_57_8102(): pass

    label("Function_57_8102")

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

    # Function_57_8102 end

    SaveToFile()

Try(main)

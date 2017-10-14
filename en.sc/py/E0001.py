from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0001   ._SN',
        MapName             = 'event',
        Location            = 'E0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Father Kevin',                         # 9
        'Targeting Camera',                     # 10
        'Kloe',                                 # 11
        'Sieg',                                 # 12
        'Olivier',                              # 13
        'Tita',                                 # 14
        'Scherazard',                           # 15
        'Agate',                                # 16
        'Zin',                                  # 17
        'Young Passenger',                      # 18
        'Young Passenger',                      # 19
        'Passenger',                            # 20
        'Passenger',                            # 21
        'Tico',                                 # 22
        'Morie',                                # 23
        'Anton',                                # 24
        'Ricky',                                # 25
        'Faults',                               # 26
        'Noticia',                              # 27
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH02320 ._CH',             # 02
        'ED6_DT07/CH02323 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT26/CH20311 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH00050 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01470 ._CH',             # 0A
        'ED6_DT07/CH01170 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01150 ._CH',             # 0D
        'ED6_DT27/CH03085 ._CH',             # 0E
        'ED6_DT07/CH00004 ._CH',             # 0F
        'ED6_DT26/CH20236 ._CH',             # 10
        'ED6_DT06/CH20045 ._CH',             # 11
        'ED6_DT26/CH20241 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH01050 ._CH',             # 14
        'ED6_DT07/CH01140 ._CH',             # 15
        'ED6_DT07/CH01210 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH02320P._CP',             # 02
        'ED6_DT07/CH02323P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT26/CH20311P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH00050P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01470P._CP',             # 0A
        'ED6_DT07/CH01170P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01150P._CP',             # 0D
        'ED6_DT27/CH03085P._CP',             # 0E
        'ED6_DT07/CH00004P._CP',             # 0F
        'ED6_DT26/CH20236P._CP',             # 10
        'ED6_DT06/CH20045P._CP',             # 11
        'ED6_DT26/CH20241P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH01050P._CP',             # 14
        'ED6_DT07/CH01140P._CP',             # 15
        'ED6_DT07/CH01210P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
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
        X                   = 3200,
        Z                   = 5000,
        Y                   = -4800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 59030,
        Z                   = -1800,
        Y                   = 54020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -2220,
        Z                   = 5000,
        Y                   = -2440,
        Direction           = 128,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 59030,
        Z                   = -1800,
        Y                   = 54020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 3860,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = 4800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -480,
        Z                   = 5000,
        Y                   = -10950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 480,
        Z                   = 5000,
        Y                   = -10950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = -4050,
        Direction           = 265,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 5000,
        Y                   = -5190,
        Direction           = 271,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    ScpFunction(
        "Function_0_3CA",          # 00, 0
        "Function_1_588",          # 01, 1
        "Function_2_5F2",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_7B7",          # 05, 5
        "Function_6_7DE",          # 06, 6
        "Function_7_8B1",          # 07, 7
        "Function_8_B41",          # 08, 8
        "Function_9_E20",          # 09, 9
        "Function_10_ED3",         # 0A, 10
        "Function_11_F76",         # 0B, 11
        "Function_12_103E",        # 0C, 12
        "Function_13_10AF",        # 0D, 13
        "Function_14_110F",        # 0E, 14
        "Function_15_128C",        # 0F, 15
        "Function_16_1404",        # 10, 16
        "Function_17_14C9",        # 11, 17
        "Function_18_166E",        # 12, 18
        "Function_19_17E2",        # 13, 19
        "Function_20_182D",        # 14, 20
        "Function_21_18DD",        # 15, 21
        "Function_22_2A38",        # 16, 22
        "Function_23_31D4",        # 17, 23
        "Function_24_3D65",        # 18, 24
        "Function_25_4453",        # 19, 25
        "Function_26_5005",        # 1A, 26
        "Function_27_5091",        # 1B, 27
        "Function_28_5BC8",        # 1C, 28
        "Function_29_5CE0",        # 1D, 29
        "Function_30_5DD4",        # 1E, 30
        "Function_31_5E8E",        # 1F, 31
        "Function_32_738E",        # 20, 32
        "Function_33_73A5",        # 21, 33
    )


    def Function_0_3CA(): pass

    label("Function_0_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrPos(0xE, 3200, 5000, -4800, 90)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_530")

    label("loc_3EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_411")

    Jump("loc_530")

    label("loc_414")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_428"),
        (103, "loc_428"),
        (104, "loc_428"),
        (SWITCH_DEFAULT, "loc_436"),
    )


    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_433")

    label("loc_433")

    Jump("loc_436")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_4B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_45D")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3200, 5000, -3870, 180)
    Jump("loc_473")

    label("loc_45D")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3200, 5000, -3870, 270)

    label("loc_473")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 3200, 5000, -5220, 0)
    SetChrPos(0xB, 3860, 6000, -4520, 270)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_530")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_END)), "loc_530")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x11, -1700, 5000, -3890, 0)
    SetChrPos(0x12, -2750, 5000, -1370, 225)
    SetChrPos(0x13, -2410, 5000, -6360, 45)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_END)), "loc_530")
    SetChrPos(0xB, 3730, 6000, -5280, 270)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_541")
    OP_A3(0x10F3)
    Event(0, 30)
    Jump("loc_587")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_552")
    OP_A3(0x10F2)
    Event(0, 29)
    Jump("loc_587")

    label("loc_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_563")
    OP_A3(0x10F1)
    Event(0, 28)
    Jump("loc_587")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572")
    Event(0, 21)
    Jump("loc_587")

    label("loc_572")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_587")
    Event(0, 27)

    label("loc_587")

    Return()

    # Function_0_3CA end

    def Function_1_588(): pass

    label("Function_1_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_599")
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)

    label("loc_599")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F1")
    Call(0, 32)

    label("loc_5F1")

    Return()

    # Function_1_588 end

    def Function_2_5F2(): pass

    label("Function_2_5F2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_759")

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_759")

    label("loc_630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_759")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_759")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_759")

    label("loc_694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_759")

    label("loc_6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_759")

    label("loc_6C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_759")

    label("loc_6DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_759")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_711")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_759")

    label("loc_711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_759")

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_759")

    label("loc_743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_76E")

    Return()

    # Function_2_5F2 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_792")
    OP_8D(0xFE, -2000, -5830, 320, -2950, 2000)
    Jump("Function_3_76F")

    label("loc_792")

    Return()

    # Function_3_76F end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_8D(0xFE, -2220, -2440, -3190, -5300, 2000)
    Jump("Function_4_793")

    label("loc_7B6")

    Return()

    # Function_4_793 end

    def Function_5_7B7(): pass

    label("Function_5_7B7")


    def lambda_7BD():

        label("loc_7BD")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_7BD")

    QueueWorkItem2(0x13, 1, lambda_7BD)

    label("loc_7C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7C8")

    label("loc_7DD")

    Return()

    # Function_5_7B7 end

    def Function_6_7DE(): pass

    label("Function_6_7DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_814")
    SetChrSubChip(0xFE, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    SetChrSubChip(0xFE, 2)
    Jump("loc_82D")

    label("loc_814")

    SetChrSubChip(0xFE, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)
    SetChrSubChip(0xFE, 2)

    label("loc_82D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_83A")
    OP_A3(0xA)
    Jump("loc_876")

    label("loc_83A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_876")
    Sleep(80)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 4)
    Sleep(150)
    SetChrSubChip(0xFE, 3)
    Sleep(100)
    SetChrSubChip(0xFE, 2)
    OP_A2(0xA)

    label("loc_876")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_899")
    Sleep(50)
    SetChrSubChip(0xFE, 1)
    Sleep(50)
    Jump("loc_8AD")

    label("loc_899")

    SetChrSubChip(0xFE, 2)
    Sleep(150)
    SetChrSubChip(0xFE, 1)
    Sleep(150)

    label("loc_8AD")

    Jump("Function_6_7DE")

    label("loc_8B0")

    Return()

    # Function_6_7DE end

    def Function_7_8B1(): pass

    label("Function_7_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FF")
    TalkBegin(0xA)
    OP_4A(0xA, 255)
    OP_A2(0x0)

    ChrTalk(    #0
        0xA,
        (
            "#542FYou know, the Liberl News wrote\x01",
            "an article about that party.\x02\x03",

            "Julia gained a lot of, um, admirers,\x01",
            "from high society to the poorest\x01",
            "commoner.\x02\x03",

            "#045FI've always felt a little sorry for the\x01",
            "man involved, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1015FSeriously? Don't you think he got\x01",
            "what he deserved?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)
    Jump("loc_AA5")

    label("loc_9FF")

    TalkBegin(0xA)
    OP_4A(0xA, 255)

    ChrTalk(    #2
        0xA,
        (
            "#542FYou know, the Liberl News wrote\x01",
            "an article about that party.\x02\x03",

            "Julia gained a lot of, um, admirers,\x01",
            "from high society to the poorest\x01",
            "commoner.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)

    label("loc_AA5")

    Jump("loc_AAC")

    label("loc_AA8")

    Call(0, 25)

    label("loc_AAC")

    Jump("loc_B31")

    label("loc_AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_B2D")
    TalkBegin(0xA)
    OP_4A(0xA, 255)

    ChrTalk(    #3
        0xA,
        (
            "#048FHaha, I actually thought about\x01",
            "writing her a letter myself.\x02\x03",

            "I do wonder how she's doing...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 255)
    TalkEnd(0xA)
    Jump("loc_B31")

    label("loc_B2D")

    Call(0, 23)

    label("loc_B31")

    Jump("loc_B40")

    label("loc_B34")

    OP_4A(0xA, 255)
    Call(0, 22)
    OP_4B(0xA, 255)

    label("loc_B40")

    Return()

    # Function_7_8B1 end

    def Function_8_B41(): pass

    label("Function_8_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 0)), scpexpr(EXPR_END)), "loc_E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD4")
    TalkBegin(0xC)
    OP_43(0xC, 0x0, 0x0, 0x6)
    OP_A2(0x1)

    ChrTalk(    #4
        0xC,
        (
            "#034FI would presume nothing less\x01",
            "t-terrifying from the lady knight\x01",
            "who defines the Royal Guard.\x02\x03",

            "#032FBut know this! The flames from\x01",
            "which my passion first was kindled\x01",
            "shall ne'er fade!\x02\x03",

            "#530FEven if I must be stripped naked\x01",
            "before her, I shall serenade her\x01",
            "with naught but my lute in hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1019F...I so did not need that mental image.\x01",
            "Thanks, Olivier.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 255)
    TalkEnd(0xC)
    Jump("loc_E0A")

    label("loc_CD4")

    TalkBegin(0xC)
    OP_43(0xC, 0x0, 0x0, 0x6)

    ChrTalk(    #6
        0xC,
        (
            "#034FI would presume nothing less\x01",
            "t-terrifying from the lady knight\x01",
            "who defines the Royal Guard.\x02\x03",

            "#032FBut know this! The flames from\x01",
            "which my passion first was kindled\x01",
            "shall ne'er fade!\x02\x03",

            "#530FEven if I must be stripped naked\x01",
            "before her, I shall serenade her\x01",
            "with naught but my lute in hand!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)

    label("loc_E0A")

    Jump("loc_E11")

    label("loc_E0D")

    Call(0, 25)

    label("loc_E11")

    SetChrChipByIndex(0xC, 17)
    SetChrSubChip(0xC, 0)
    OP_4B(0xC, 255)
    Return()

    # Function_8_B41 end

    def Function_9_E20(): pass

    label("Function_9_E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 5)), scpexpr(EXPR_END)), "loc_ECE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 6)), scpexpr(EXPR_END)), "loc_EC7")
    TalkBegin(0xD)
    OP_4A(0xD, 255)

    ChrTalk(    #7
        0xD,
        (
            "#061FThe last time I came to the capital,\x01",
            "I saw the Arseille! It's really, really\x01",
            "pretty!\x02\x03",

            "Heehee! I wonder if we'll see it again.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    TalkEnd(0xD)
    Jump("loc_ECB")

    label("loc_EC7")

    Call(0, 24)

    label("loc_ECB")

    Jump("loc_ED2")

    label("loc_ECE")

    Call(0, 23)

    label("loc_ED2")

    Return()

    # Function_9_E20 end

    def Function_10_ED3(): pass

    label("Function_10_ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 2)), scpexpr(EXPR_END)), "loc_F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE9")
    Call(0, 31)
    Jump("loc_F75")

    label("loc_EE9")

    TalkBegin(0xE)

    ChrTalk(    #8
        0xE,
        (
            "#027FI'll be back in my seat once I've\x01",
            "enjoyed the wind a little more.\x02\x03",

            "Make sure you're all buckled in\x01",
            "before we land, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)

    label("loc_F75")

    Return()

    # Function_10_ED3 end

    def Function_11_F76(): pass

    label("Function_11_F76")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_FCE")

    ChrTalk(    #9
        0xFE,
        "Whoa! A white hawk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "That's so cooool!\x01",
            "Is it that lady's pet?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xFE, 255)
    Jump("loc_103A")

    label("loc_FCE")


    ChrTalk(    #11
        0xFE,
        (
            "I heard that Zeiss has stairs...\x01",
            "that MOVE. MOVING! STAIRS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I wanna ride them, I wanna ride them!\x02",
    )

    CloseMessageWindow()

    label("loc_103A")

    TalkEnd(0x11)
    Return()

    # Function_11_F76 end

    def Function_12_103E(): pass

    label("Function_12_103E")

    TalkBegin(0x12)

    ChrTalk(    #13
        0xFE,
        (
            "Who cares about moving stairs?\x01",
            "I wanna see the hot springs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I heard it's like one huuuuge bath!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_12_103E end

    def Function_13_10AF(): pass

    label("Function_13_10AF")

    TalkBegin(0x13)

    ChrTalk(    #15
        0xFE,
        (
            "Now, now, that's enough running\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "You're bothering the other passengers.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_13_10AF end

    def Function_14_110F(): pass

    label("Function_14_110F")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_11EA")

    ChrTalk(    #17
        0xFE,
        (
            "Heheh... I'm a total military nut,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "My favorite tank is the original model\x01",
            "of the Imperial Army's Reinford LP-III!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "It gets better mileage than its post-\x01",
            "Hundred Days War successors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1288")

    label("loc_11EA")


    ChrTalk(    #20
        0xFE,
        (
            "Awwww, this sucks. You can't\x01",
            "see Leiston Fortress from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I guess they wouldn't let a passenger\x01",
            "ship near their airspace, though, would\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1288")

    TalkEnd(0x14)
    Return()

    # Function_14_110F end

    def Function_15_128C(): pass

    label("Function_15_128C")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_131B")

    ChrTalk(    #22
        0xFE,
        "I'm off to study the Haken Gate near Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "If I have time, Id like to stop by Rolent,\x01",
            "too, but Haken has to come first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1400")

    label("loc_131B")


    ChrTalk(    #24
        0xFE,
        "I'm off to study the Haken Gate near Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's arguably the most important landmark\x01",
            "in the history of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "And I plan on combing over every crack in\x01",
            "the wall of that landmark, let me tell you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1400")

    TalkEnd(0x15)
    Return()

    # Function_15_128C end

    def Function_16_1404(): pass

    label("Function_16_1404")

    TalkBegin(0x16)

    ChrTalk(    #27
        0xFE,
        (
            "When I get to the Haken Gate,\x01",
            "I'm gonna take so many photos,\x01",
            "you don't even KNOW!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "I've always wanted to get a picture\x01",
            "of a place as striking as the Haken Gate,\x01",
            "so now's my chance!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x16)
    Return()

    # Function_16_1404 end

    def Function_17_14C9(): pass

    label("Function_17_14C9")

    OP_EA(0x1, 0x1, 0x0, 0x0)
    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1575")

    ChrTalk(    #29
        0xFE,
        (
            "I'm not one to smoulder away in the\x01",
            "capital! That's not me, no, sirree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Somewhere out there, someone needs\x01",
            "me! And I'm gonna find that someone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_166A")

    label("loc_1575")


    ChrTalk(    #31
        0xFE,
        (
            "I'm not one to smoulder away in the\x01",
            "capital! That's not me, no, sirree!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I'm going to travel Liberl,\x01",
            "wherever my legs can take me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "I know that, somewhere out there,\x01",
            "there's someone who needs me!\x01",
            "And I'm gonna find that someone!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_166A")

    TalkEnd(0x17)
    Return()

    # Function_17_14C9 end

    def Function_18_166E(): pass

    label("Function_18_166E")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1708")

    ChrTalk(    #34
        0xFE,
        (
            "So suddenly, Anton decides he\x01",
            "absolutely needs to go to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "This, uh, happens a lot, so I'm tagging\x01",
            "along to keep an eye on him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DE")

    label("loc_1708")


    ChrTalk(    #36
        0xFE,
        (
            "So suddenly, Anton decides he\x01",
            "absolutely needs to go to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "This, uh, happens a lot, so I'm tagging\x01",
            "along to keep an eye on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Could be fun playing tourist while\x01",
            "along for the ride, at least.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_17DE")

    TalkEnd(0x18)
    Return()

    # Function_18_166E end

    def Function_19_17E2(): pass

    label("Function_19_17E2")

    TalkBegin(0x19)

    ChrTalk(    #39
        0xFE,
        (
            "*siiigh* Wish I could've spent more\x01",
            "time in the hot springs...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_19_17E2 end

    def Function_20_182D(): pass

    label("Function_20_182D")

    TalkBegin(0x1A)

    ChrTalk(    #40
        0xFE,
        (
            "Magazine reporters don't get any breaks!\x01",
            "Speedy reporting is our lifeblood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "And you can bet I'll have my latest report\x01",
            "written up the instant we hit the dock!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1A)
    Return()

    # Function_20_182D end

    def Function_21_18DD(): pass

    label("Function_21_18DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_D2(0x260157, 0x26015C, 0x16)
    LoadEffect(0x0, "map\\\\mp044_00.eff")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05My Estelle... You shine like the sun.\x02\x03",

            "My time with you was the happiest...\x01",
            "and the most painful...I've ever known.\x02\x03",

            "Just as the brightest light casts\x01",
            "the darkest shadow...\x02\x03",

            "If you stayed with me, you'd find out\x01",
            "just how disgusting my true nature is...\x02\x03",

            "Sometimes, I think it would have\x01",
            "been better if we'd never met...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrPos(0x101, 2660, 5000, -4840, 92)
    OP_6D(-3180, 3500, 2710, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(12000, 0)
    OP_6C(149000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x0, 0x64)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_1AEC():
        OP_6D(3190, 5000, -4610, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AEC)

    def lambda_1B04():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B04)
    Sleep(4000)

    def lambda_1B21():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B21)

    def lambda_1B31():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B31)

    def lambda_1B41():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B41)
    Sleep(6000)
    SetChrPos(0x8, -3160, 5000, -1280, 267)
    ClearChrFlags(0x8, 0x8)

    ChrTalk(    #43
        0x101,
        (
            "#588F...\x02\x03",

            "I...hurt Joshua?\x02\x03",

            "He wishes he'd never met me.\x01",
            "He said... He SAID that...\x02\x03",

            "I... I...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #44
        0x8,
        "Man's Voice",
        "#2PNooo, no, no!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x8, -2960, 5000, 1050, 177)
    ClearChrFlags(0x8, 0x80)
    Sleep(500)

    def lambda_1C29():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C29)

    def lambda_1C37():
        OP_6D(1780, 5000, -4750, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C37)

    def lambda_1C4F():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C4F)

    def lambda_1C67():
        OP_6C(314000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C67)
    Sleep(800)

    def lambda_1C7C():
        OP_8E(0x8, 0xFFFFF7A4, 0x1388, 0xFFFFFB96, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1C7C)
    WaitChrThread(0x8, 0x0)

    def lambda_1C9C():
        OP_8E(0x8, 0xFFFFFCC2, 0x1388, 0xFFFFF128, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1C9C)
    OP_8C(0x101, 273, 500)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 80, 1000)

    ChrTalk(    #45
        0x101,
        "#4P#587FHuh...?\x02",
    )

    CloseMessageWindow()

    def lambda_1CDF():
        OP_8E(0x8, 0x28A, 0x1388, 0xFFFFEF0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1CDF)
    WaitChrThread(0x8, 0x0)

    NpcTalk(    #46
        0x8,
        "Insensitive Jerk",
        (
            "#1061F#3PC'mon, now! Look at this clear\x01",
            "blue sky!\x02\x03",

            "Feel the gentle kiss of the wind\x01",
            "on your cheek!\x02\x03",

            "#1060FA lovely girl like you ain't allowed to\x01",
            "be sad on a gorgeous day like this.\x02\x03",

            "It'd sadden Aidios, too, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#4P#587FUhmmm...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x8,
        "Insensitive Jerk",
        (
            "#1064F#3PH-Hey, waidasec! I'm not dangerous!\x01",
            "Well, okay, maybe I came ACROSS as--\x02\x03",

            "#1065FA-Anyway! You just caught my eye the\x01",
            "moment you came aboard, y'see.\x02\x03",

            "#1062FYou seemed a little broken up over something,\x01",
            "so I thought to myself, 'Heeey! I'll put a smile\x01",
            "on her face with my OVERPOWERING charm.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#4P#004FUmmmm...\x02\x03",

            "#587FI...don't quite get what you mean,\x01",
            "but thanks...I guess?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #50
        0x8,
        "Insensitive Jerk",
        (
            "#1061F#3PTo be honest, this is what we usually\x01",
            "call, ah, 'putting the moves on.'\x02\x03",

            "#1060FSo how 'bout it? Want to head down\x01",
            "to the lower observation deck?\x02\x03",

            "You can get drinks down there, too!\x01",
            "I'd be happy to treat a new friend.\x01",
            "What d'you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#4P#587FWell, um, I appreciate the offer, but...\x02\x03",

            "I'm not...not really in the mood...\x02\x03",

            "#003FI'm sorry...can you just--\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x8,
        "Insensitive Jerk?",
        (
            "#1065F#3PHmmm... I think I see how it is.\x02\x03",

            "#1060FAll right, then, time to knock it\x01",
            "off with the come-ons and put on\x01",
            "the work face, eh?\x02\x03",

            "After all, it's my job to guide lost\x01",
            "lambs like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#4P#004FYour job...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #54
        0x8,
        "Insensitive Jerk?",
        "#1071F#3PHeh, darn right! Look at this!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x8, 22)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0xD8, 0x0, 0x64)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    PlayEffect(0x0, 0x0, 0x8, 0, 550, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_83(0x0, 0x2)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #55
        (
            "\x07\x05The previously-insensitive jerk held forth a medallion with a chalice\x01",
            "engraved in the center.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #56
        0x101,
        (
            "#4P#004FEh? That's...\x02\x03",

            "Isn't that the seal of the Septian Church?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(200)

    NpcTalk(    #57
        0x8,
        "Insensitive Jerk?",
        (
            "#1060F#3PBingo. This is the grail emblem.\x02\x03",

            "Lemme introduce myself properly. I'm\x01",
            "Kevin Graham. Looks and, uh, moves aside,\x01",
            "I really AM a priest of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#4P#501FHuh, wow.\x02\x03",

            "#505FWait. For real, or is this another joke?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#1061F#3PAww, why d'you have to doubt me still?\x01",
            "I'm a serious, devoted priest, y'know!\x02\x03",

            "I never miss the Trinary Prayers, and I\x01",
            "always have my Testaments right...at...\x02\x03",

            "#1062F...hand? Uh...\x02\x03",

            "#1068FI...think I left 'em on my seat. Sorry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#4P#007FYeah, that really helps your\x01",
            "case, there.\x02\x03",

            "#586FHeh heh... You really are kind\x01",
            "of a weirdo, Father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#1061F#3PAH-HA! Laughter! Victory is mine!\x02\x03",

            "#1061FThat's more like it!\x01",
            "Cute girls like you deserve to smile.\x02\x03",

            "#1060FAnyway, if you want, I'll give you an\x01",
            "ear in my official, priestly capacity.\x02\x03",

            "No pick-up lines, I promise.\x01",
            "Aidios smite me dead otherwise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#4P#586FWell...okay...\x02\x03",

            "But...where do I even...?\x02\x03",

            "#587FI...\x02\x03",

            "#003F...*sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 16)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #63
        0x8,
        (
            "#1064F#3PW-Wait, hold on now...\x02\x03",

            "I don't know what I did,\x01",
            "but I'm sorry anyway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#4P#588FI... It's myyyyy...\x02\x03",

            "Muh-My fau-fau-fauauuuuuu...\x01",
            "auuuu-huuuuuu...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 15)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 1)
    Sleep(500)

    ChrTalk(    #65
        0x101,
        "#4P#589F#4SWaaaaa-haaauuu-haaauuuuh!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "#1068F#3PGreat Goddess...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x640, 0x1388, 0xFFFFEBB0, 0x3E8, 0x0)
    TurnDirection(0x8, 0x101, 400)
    Fade(500)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 5)
    OP_0D()
    OP_1D(0x1)
    SetMapFlags(0x2000000)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        (
            "#1060F#3PSteady there, child. You've been keepin'\x01",
            "this bottled up for ages, haven't ya?\x02\x03",

            "My shoulder is yours.\x01",
            "Come on...cry it all out. I'm here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#4P#589F#4SWaaaaa-haaauuu-haaauuuuh!#2S\x02\x03",

            "#4SWAAAAAAAAAAAAAAAAAAH-\x01",
            "HAAAAAAAAAAAAAAAAAAAAAAH!!!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2A06():
        OP_6D(-1960, 5000, 16820, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A06)
    FadeToDark(5000, 0, -1)
    OP_0D()
    OP_23(0x79)
    OP_23(0x1C3)
    Sleep(2000)
    NewScene("ED6_DT21/E0011   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_18DD end

    def Function_22_2A38(): pass

    label("Function_22_2A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3165")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3240, 5000, -4260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3200, 5000, -3800, 180)
    TurnDirection(0xA, 0x101, 0)
    OP_0D()

    ChrTalk(    #69
        0xA,
        (
            "#040F#4POh, hi, Estelle.\x02\x03",

            "Taking a walk around the ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1016F#6PHaha! Yeah, pretty much.\x02\x03",

            "#1011FOh, yeah, Kloe, what do you do when\x01",
            "you need to get back to Grancel?\x02\x03",

            "Do you get the Royal Guard\x01",
            "to fly you there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#045F#4PHaha, no, of course not. That would\x01",
            "be a little obvious! I just use normal\x01",
            "flights like anyone else.\x02\x03",

            "#040FI usually go back twice a year,\x01",
            "once for New Year's and once\x01",
            "for Grandmother's birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006F#6PSo you're kinda used to\x01",
            "passenger flight, huh.\x02\x03",

            "#1015FOh, but what does Sieg do, then?\x02\x03",

            "Does he fly along at his\x01",
            "own pace to the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        "#542F#4POh, well...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xB, 15000, 8000, -4760, 270)
    ClearChrFlags(0xB, 0x80)
    TurnDirection(0xA, 0xB, 400)

    def lambda_2D21():

        label("loc_2D21")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2D21")

    QueueWorkItem2(0xA, 1, lambda_2D21)
    Sleep(500)

    ChrTalk(    #74
        0xA,
        "#040F#6PSieg, come here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()
    OP_22(0x8C, 0x0, 0x64)
    OP_22(0x197, 0x0, 0x64)

    def lambda_2D72():
        OP_6D(10210, 5000, -3880, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D72)

    def lambda_2D8A():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D8A)

    def lambda_2DA2():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DA2)
    WaitChrThread(0x101, 0x1)
    OP_4A(0x11, 255)

    def lambda_2DBB():
        TurnDirection(0x11, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DBB)
    OP_A2(0x9)

    def lambda_2DCC():
        OP_6D(4360, 5000, -4030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DCC)
    ClearChrFlags(0xB, 0x1)
    OP_8F(0xB, 0xE92, 0x1770, 0xFFFFEB60, 0x1388, 0x0)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    OP_44(0xA, 0x1)
    OP_8C(0xA, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #76
        0x101,
        "#1004F#6PWhoaaaa!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #77
        0xB,
        "#310FScree?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "#542F#6PHaha! Sorry, I'm just calling\x01",
            "you for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1008F#6PW-Well, that was a surprise...\x02\x03",

            "So Sieg can follow the ship? Cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        "#311FScree! ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #81
        0xA,
        (
            "#041F#4PSieg can fly level at speeds of\x01",
            "up to 1800 selge per hour.\x02\x03",

            "Most airships cruise at around\x01",
            "half that...\x02\x03",

            "So to Sieg, this isn't much\x01",
            "faster than an evening stroll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1011F#6POh, I see!\x02\x03",

            "#1016FYou really are better than the\x01",
            "average falcon, aren't you, Sieg?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xB,
        "#311FScreee! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "#048F#4PSieg's speed is the reason he's so useful\x01",
            "for contacting the Royal Guard.\x02\x03",

            "If for some reason I can't use powered\x01",
            "communication, nothing in the country\x01",
            "can carry a message faster than Sieg!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1006F#6PI thought so. I remember how fast\x01",
            "you got in touch with Julia during\x01",
            "that thing with the mayor!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1407)
    EventEnd(0x0)
    Jump("loc_31D3")

    label("loc_3165")

    TalkBegin(0xA)

    ChrTalk(    #86
        0xA,
        (
            "#047FMmm, the wind feels so nice...\x02\x03",

            "#048FWith the weather like this,\x01",
            "Zeiss is going to be lovely.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_31D3")

    Return()

    # Function_22_2A38 end

    def Function_23_31D4(): pass

    label("Function_23_31D4")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #87
        0xD,
        "#061FHi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        "#311F#4PScreee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "#040F#4POut for a walk, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1006F#6PUh-huh.\x02\x03",

            "You two just watching the clouds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "#048F#4PHmm... Something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        "#560FKloe helped me become friends with Sieg!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #93
        0xD,
        "#061FRight, Sieg? ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xB,
        "#311F#4PScree. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#1001F#6PHaha. That's great, Tita.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #96
        0xD,
        (
            "#060FOh, and Kloe was telling me\x01",
            "all about the school festival.\x02\x03",

            "You were a knight in the play, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1008F#6PWell, uh, kinda, yeah.\x02\x03",

            "#1006FActually, a lot of people thought I cut\x01",
            "a pretty dashing figure as a knight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#560FWooow, neato!\x02\x03",

            "#561FI wish I could've seen you act...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #99
        0xA,
        (
            "#041FWell, you can come to the\x01",
            "festival next year, Tita.\x02\x03",

            "It's open to the public, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #100
        0xD,
        (
            "#560FWait, really?\x02\x03",

            "Mom and Dad will be back by then,\x01",
            "too...\x02\x03",

            "#061FI'll ask Grandpa about it as soon as\x01",
            "I get home!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #101
        0xA,
        (
            "#048F#4PWell, if we do that...\x02\x03",

            "We'll have to get Estelle on\x01",
            "stage again next year.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3617():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3617)

    ChrTalk(    #102
        0x101,
        (
            "#1016F#6PUh, y'know, I think I'll just\x01",
            "leave my thanks.\x02\x03",

            "#1025FSay, that reminds me. Tita,\x01",
            "your mom and dad are out\x01",
            "of the country working, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        (
            "#560FYeah...\x02\x03",

            "They're helping to establish orbal technology\x01",
            "in places that don't have it yet.\x02\x03",

            "They've been gone for two years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F#6PWow, that IS a long time...\x02\x03",

            "I hope they write you letters or\x01",
            "something at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xD,
        (
            "#061FYeah, once every month. ♪\x02\x03",

            "#060FI, um, wrote about you last time,\x01",
            "Estelle, and in the reply...\x02\x03",

            "They said to give you their regards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1016F#6PAww, that's sweet of them.\x02\x03",

            "#1006FSo what kind of people are\x01",
            "your parents, Tita?\x02\x03",

            "Is your mom like you? I bet she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#064FLike me? I don't think so...\x02\x03",

            "#060FMom's got a really...um, powerful\x01",
            "personality, I guess.\x02\x03",

            "#061FShe and Grandpa kinda end up fighting\x01",
            "and wrestling a lot over stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1004F#6P...Wrestling?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #109
        0xA,
        "#045FWell, um...she certainly sounds...energetic?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #110
        0xD,
        (
            "#067FOh, but they usually get along really well!\x02\x03",

            "Dad says their fighting is just a\x01",
            "way they express their love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1016F#6PWell, uh, okay...\x02\x03",

            "#1011FSo what's your dad like, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #112
        0xD,
        (
            "#560FHe's not like Mom at all. He's sorta\x01",
            "quiet and...reliable, I guess?\x02\x03",

            "He was a bracer until about ten\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1004F#6PWait, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xD,
        (
            "#060FHe told me once that he got hurt\x01",
            "doing something and became\x01",
            "an engineer afterward.\x02\x03",

            "Mom said he was really famous,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1006F#6PHuh, okay.\x02\x03",

            "#1001FThey sound great! I'd love to meet\x01",
            "them when they get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#061FYeah! When they do, come over\x01",
            "to play and I'll introduce you. ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #117
        0xD,
        "#560FOooh, Kloe, you too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        "#041FI'd love to. Thank you, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        "#310F#4PScreee?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #120
        0xD,
        "#061FOh, you can come too, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        "#311F#4PScree! ㈱\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0xD, 0xA, 0)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1605)
    EventEnd(0x0)
    Return()

    # Function_23_31D4 end

    def Function_24_3D65(): pass

    label("Function_24_3D65")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xD, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xD, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #122
        0xD,
        (
            "#560FOh, yeah, Estelle!\x02\x03",

            "Do you know why the wind's nice\x01",
            "and gentle on the deck like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1004F#6PUh... Isn't it just like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#060FOh, no! At the speed we're going,\x01",
            "the wind should be really strong!\x02\x03",

            "We wouldn't be able to hear each other...\x01",
            "we'd get swept off the deck, in fact!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015F#6PWait, seriously...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #126
        0xA,
        (
            "#040FAh, but if I recall correctly, there's a\x01",
            "device aboard an airship that prevents\x01",
            "such things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #127
        0xD,
        (
            "#560FUh-huh! It's a side effect of the Flight\x01",
            "Field that keeps the ship in the air.\x02\x03",

            "#061FAn orbal flight engine envelops the ship\x01",
            "in a field that counteracts gravity, you see!\x02\x03",

            "It also has an anti-inertial effect on anything\x01",
            "striking the field, and that includes the\x01",
            "particles that make up the wind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1019F#6P(...Kloe, are you following any of this?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xA,
        "#045F(I think I understand...half of it?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #130
        0xD,
        (
            "#060FBut, um, generating a flight field\x01",
            "takes a lot of power...\x02\x03",

            "You need a really high-output orbal\x01",
            "engine to create the field at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1006F#6POkay...\x02\x03",

            "So that's why people always say\x01",
            "that it's the engine that determines\x01",
            "what an airship can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#040FSpeaking of which...\x02\x03",

            "The new engine Professor Russell and\x01",
            "everyone developed for the Arseille is\x01",
            "supposed to be incredible, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #133
        0xD,
        (
            "#061FUh-huh! Grandpa showed me the\x01",
            "spec sheet for it, and its capabilities\x01",
            "are waaaaay beyond existing engines!\x02\x03",

            "Grandpa and the rest of the team at the\x01",
            "central factory worked really hard on it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xA,
        (
            "#048FI can imagine...\x01",
            "Oh, Julia will be delighted.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    TurnDirection(0xA, 0xD, 0)
    TurnDirection(0xD, 0xA, 0)
    OP_4B(0xA, 255)
    OP_4B(0xD, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1606)
    EventEnd(0x0)
    Return()

    # Function_24_3D65 end

    def Function_25_4453(): pass

    label("Function_25_4453")

    EventBegin(0x0)
    OP_20(0x3E8)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    SetChrChipByIndex(0xC, 18)
    SetChrSubChip(0xC, 0)
    SetChrFlags(0xC, 0x20)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x101, 1300, 5000, -4640, 109)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #135
        0xC,
        (
            "#031FAh, Estelle, my fair rose.\x02\x03",

            "Welcome to Olivier Lenheim's lovely\x01",
            "solo recital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1007F#6POh, Aidios, he escaped his chair.\x02\x03",

            "#1019FKloe, remember, you have a sword\x01",
            "and you know how to use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xA,
        (
            "#045F#4PHaha. Well, I saw him playing when\x01",
            "I stepped out onto the deck, so I came\x01",
            "by to listen for a little while.\x02\x03",

            "#048FHe really is exceptionally talented.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)
    Sleep(500)

    ChrTalk(    #138
        0xC,
        (
            "#035FMmm... Your compliments do me the\x01",
            "greatest honor, Your Highness.\x02\x03",

            "#037FIf you wish, when we arrive at the capital\x01",
            "I could treat you to a...private concert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        "#310F#4PScreee-eeee?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xC,
        "#033FHmm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)

    def lambda_4741():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4741)

    ChrTalk(    #141
        0xC,
        (
            "#036F#6PEr, Sieg, yes. That did not necessarily\x01",
            "mean anything beyond the obvious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xA,
        (
            "#040FOhhhhh? You meant something else\x01",
            "by 'private concert,' Olivier?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #143
        0xC,
        (
            "#035FHeh, well...if you wish for it to mean\x01",
            "something more, my princess,\x01",
            "it certainly could...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "#310F#3S#4PSCREEEEE!\x02",
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    OP_22(0x8C, 0x1, 0x64)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)
    OP_A2(0x2)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_8C(0xC, 90, 400)
    Sleep(400)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #145
        0xC,
        (
            "#036FWh-Whaaaaa! Bird! BIRD!\x01",
            "Please, stop, Sieg!\x02\x03",

            "I'm sorry, I'm sorry!\x01",
            "I won't do it agaaaaain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1001F#6PHaha. Good job, Sieg!\x01",
            "You're a girl's best friend!\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_A6(0x3)
    OP_8E(0xB, 0xF14, 0x1770, 0xFFFFEE58, 0x5DC, 0x0)
    OP_8C(0xB, 275, 0)
    OP_23(0x8C)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    OP_63(0xC)
    Sleep(500)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #147
        0xC,
        "#034FHaah... Haah... That was terrifying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "#041FHaha... I'm sorry, Olivier.\x02\x03",

            "#542FThat was just Sieg expressing\x01",
            "his...love.\x02\x03",

            "I actually think he likes you,\x01",
            "on the whole, Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xB,
        "#311F#4PScreee! ㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #150
        0xC,
        (
            "#035FI shall bear his peck on my\x01",
            "cheek with pride, then!\x02\x03",

            "#030FI must admit, I did not expect your\x01",
            "escort to be so diligent. He is as vigilant\x01",
            "as any of the human Royal Guards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        (
            "#048FHaha. It depends on who\x01",
            "I'm dealing with, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1007F#6PYou really are totally indiscriminate,\x01",
            "aren't you, Olivier...?\x02\x03",

            "#1019FLook, don't try to put the moves\x01",
            "on Kloe in the capital, okay?\x02\x03",

            "Julia would, like, fire you out of a\x01",
            "cannon--into the sun--if you even\x01",
            "think about it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #153
        0xC,
        (
            "#033FAh, yes, that cold, dignified\x01",
            "lady officer.\x02\x03",

            "#030FShe, too, caught my eye during\x01",
            "the coup. The sort of woman who can\x01",
            "take on ten men... She is quite something.\x02\x03",

            "#031FHmmmm. Should the chance present\x01",
            "itself, I should...endear myself to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        "#049FUm...\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #155
        0xC,
        "#033FHm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #156
        0x101,
        "#1004F#6PWhat's wrong, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#043FIt, um, might not be a good idea\x01",
            "to joke about such things around\x01",
            "Julia, Olivier.\x02\x03",

            "I remember, once, there was a\x01",
            "party at the castle, and a man was\x01",
            "drunk and bothering us...\x02\x03",

            "Julia, um, took her sword, and...his\x01",
            "clothes...well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xC,
        "#036FWha--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1008F#6PYou mean...?\x02\x03",

            "#1013FShe, um...'defrocked' him?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #160
        0xA,
        "#540F#4P*nod*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xC,
        "#036FI'll t-t-take that under...consideration...\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0xA, 0, 0)
    OP_8C(0xC, 270, 0)
    OP_4B(0xA, 255)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 17)
    SetChrSubChip(0xC, 0)
    OP_4B(0xC, 255)
    OP_1D(0x49)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x1608)
    EventEnd(0x0)
    Return()

    # Function_25_4453 end

    def Function_26_5005(): pass

    label("Function_26_5005")

    OP_8E(0xB, 0xFDB, 0x157C, 0xFFFFF164, 0x1F40, 0x0)

    label("loc_5019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5039")
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0x1F40, 0x1)
    OP_48()
    Jump("loc_5019")

    label("loc_5039")

    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0x1770, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFD40E0, 0xFA0, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFEEE90, 0xBB8, 0x1)
    OP_97(0xB, 0xCBC, 0xFFFFF0E2, 0xFFFF8AD0, 0x7D0, 0x1)
    OP_A2(0x3)
    Return()

    # Function_26_5005 end

    def Function_27_5091(): pass

    label("Function_27_5091")

    EventBegin(0x0)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_6D(860, 5000, 20310, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(5380, 0)
    OP_6C(188000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2890, 5000, -4960, 90)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    def lambda_510A():
        OP_6D(2520, 5000, -5080, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_510A)

    def lambda_5122():
        OP_6C(236000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5122)

    def lambda_5132():
        OP_67(0, 6570, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5132)

    def lambda_514A():
        OP_6B(4380, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_514A)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6B(2860, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #162
        0x101,
        (
            "#1003F*sigh*\x02\x03",

            "#1007FCan't believe this...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #163
        (
            "#1007F(This...is definitely Joshua.)\x02\x03",

            "#1025F(Tossing on a scarf...\x01",
            "Trying to look cool, huh?)\x02\x03",

            "(I hope you're taking care\x01",
            "of yourself.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0x101, 0x0, 0x2, 0x3E8)
    Sleep(500)

    ChrTalk(    #164
        0x101,
        (
            "#1003F(Joshua really is still in Liberl.)\x02\x03",

            "(What's he doing helping those bandits?)\x02\x03",

            "#1026F(Why won't he...)\x02\x03",

            "(Why won't he let me help him...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240111, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #165
        (
            "#1027F(Joshua, you idiot...)\x02\x03",

            "(Doing crazy stuff like attacking an\x01",
            "army base...)\x02\x03",

            "(And your eyes are so cold,\x01",
            "like when we first met...)\x02\x03",

            "(And... And...)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrSubChip(0x101, 0)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #166
        0x101,
        (
            "#1014F#3SAND WHY DO YOU LOOK LIKE YOU'RE\x01",
            "GETTING ALONG SO WELL WITH THAT\x01",
            "STUPID TOMBOY?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4A(0xE, 255)
    SetChrPos(0xE, 3160, 5000, 4910, 180)
    ClearChrFlags(0xE, 0x80)

    NpcTalk(    #167
        0xE,
        "Woman's Voice",
        "#1PEstelle?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #168
        0x101,
        "#1004FWha--?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5520():
        OP_6D(2650, 5000, -880, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5520)

    def lambda_5538():
        OP_67(0, 8000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5538)

    def lambda_5550():
        OP_6E(262, 2500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5550)

    def lambda_5560():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5560)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0xE, 0x2)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #169
        0x101,
        "#1015FOh, Schera. Uh, sorry.\x02",
    )

    CloseMessageWindow()

    def lambda_55A6():
        OP_6D(2950, 5000, -4260, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55A6)
    OP_8E(0xE, 0xB54, 0x1388, 0xFFFFF092, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #170
        0xE,
        (
            "#021F#4PI thought I heard your dulcet tones...\x01",
            "from all the way across the ship.\x02\x03",

            "#020FI was worried when you just\x01",
            "wandered off like that, Estelle.\x02\x03",

            "What's wrong?\x01",
            "Airsickness finally getting to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1025F#6PAh, no, don't worry.\x02\x03",

            "I'm not sick or anything, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xE,
        "#020F#4PWell, all right.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 90, 400)
    Sleep(500)

    ChrTalk(    #173
        0xE,
        "#021F#6PAhhh! The weather is fantastic today.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #174
        0xE,
        (
            "#026F#6PTo think there are people plotting dark\x01",
            "deeds under a peaceful sky like this.\x02\x03",

            "#022FMmm. 'Goddess, what fools these mortals be.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1003F#6PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xE,
        (
            "#524F#6PEstelle. Honey.\x02\x03",

            "You don't need to suffer alone, all right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #177
        0x101,
        "#1004F#6PEr.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xE,
        (
            "#524F#6PI won't ask what you talked about with\x01",
            "Nial, but...\x02\x03",

            "Always remember you have friends you\x01",
            "can rely on.\x02\x03",

            "And you'll always, always have me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#1026F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xE,
        (
            "#026F#6POf course, if you really want to sort it\x01",
            "out on your own, that's fine.\x02\x03",

            "#020FBut every one of us wants to help you if\x01",
            "we can.\x02\x03",

            "Don't forget that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1003F#6PUm...Schera...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #182
        0xE,
        (
            "#021F#4PHeehee. That's all, don't worry.\x02\x03",

            "#020FIt'll be a while before we reach Bose.\x02\x03",

            "The ship will be stopping in Rolent on\x01",
            "the way, though, so remember to get in\x01",
            "your seat before then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        "#1025F#6PI will.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)

    def lambda_5AAA():
        OP_6D(2910, 5000, 2500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5AAA)
    OP_8E(0xE, 0xB18, 0x13EC, 0x1A68, 0x9C4, 0x0)
    OP_8C(0xE, 270, 400)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x800)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3B)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x2)
    OP_8E(0xE, 0x2D0, 0x13EC, 0x1BC6, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    OP_6F(0x2, 59)
    OP_70(0x2, 0x0)
    OP_22(0x7, 0x0, 0x64)

    def lambda_5B29():
        OP_6D(2780, 5000, -4080, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B29)
    OP_73(0x2)
    OP_71(0x2, 0x10)
    OP_71(0x2, 0x800)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #184
        0x101,
        (
            "#1007F#6PRelying on others, huh...?\x02\x03",

            "#1015FMaybe speaking to everyone for a bit\x01",
            "will clear my head.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1806)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_D6(0x1)
    Return()

    # Function_27_5091 end

    def Function_28_5BC8(): pass

    label("Function_28_5BC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(-7500, -5100, -12260, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(10000, 0)
    OP_6E(300, 0)
    SetChrPos(0x101, -200, 5000, 3170, 86)
    SetChrFlags(0x101, 0x80)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x1388)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    def lambda_5C62():
        OP_6D(-2580, 5500, -5200, 9000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5C62)

    def lambda_5C7A():
        OP_67(0, 7240, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C7A)

    def lambda_5C92():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C92)

    def lambda_5CA2():
        OP_6E(505, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5CA2)

    def lambda_5CB2():
        OP_6B(3200, 8000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_5CB2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x8, 0x0)
    OP_DC()
    NewScene("ED6_DT21/E0011   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_28_5BC8 end

    def Function_29_5CE0(): pass

    label("Function_29_5CE0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(3710, 0, 27280, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3450, 0)
    OP_EA(0x65, 0x1, 0x0, 0x0)
    OP_6C(206000, 0)
    OP_6E(525, 0)
    SetChrPos(0x101, -200, 5000, 3170, 86)
    SetChrFlags(0x101, 0x80)

    def lambda_5D5B():
        OP_6D(650, 5000, -4910, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5D5B)

    def lambda_5D73():
        OP_67(0, 8600, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D73)

    def lambda_5D8B():
        OP_6C(326000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D8B)

    QueueWorkItem(0x8, 0, None)
    OP_C8(0x200, 0x46, "C_PLAC07._CH", 0x1, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_DC()
    NewScene("ED6_DT21/E0011   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_29_5CE0 end

    def Function_30_5DD4(): pass

    label("Function_30_5DD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xF230, 0x0)
    OP_6D(-6810, 5000, 32110, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(4680, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_C8(0x80, 0x46, "C_PLAC07._CH", 0x1, 0x3E8)
    FadeToBright(1500, 0)

    def lambda_5E52():
        OP_6D(1140, 5000, -29550, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E52)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_DC()
    NewScene("ED6_DT21/E0011   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_30_5DD4 end

    def Function_31_5E8E(): pass

    label("Function_31_5E8E")

    EventBegin(0x0)
    OP_4A(0xE, 255)
    OP_20(0x3E8)
    Fade(1000)
    OP_6D(2850, 5000, -4700, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1870, 5000, -4700, 90)
    TurnDirection(0xE, 0x101, 0)
    OP_0D()
    OP_21()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #185
        0xE,
        "#020F#4PHello, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1025F#6PHi, Schera.\x01",
            "So this is where you went.\x02\x03",

            "#1015FOh, wait... Do you want to be alone for\x01",
            "a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xE,
        (
            "#027F#4POh? This is unlike you, Estelle.\x01",
            "Why so reserved?\x02\x03",

            "You want to ask about Luciola, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1013F#6PUm, yeah...\x02\x03",

            "#1007FShe says we met a long time ago, but\x01",
            "I don't really remember her at all.\x02\x03",

            "I was wondering what she's like,\x01",
            "and if you could jog my memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xE,
        (
            "#524F#4PLet's see... Where to begin, then...\x02\x03",

            "#026FWe have to begin with her stage name,\x01",
            "I suppose. Luciola, the Bewitching Bell.\x02\x03",

            "She could show her audience illusions by\x01",
            "dancing while using bells and fans.\x01",
            "Thus 'bewitching' them, you see.\x02\x03",

            "#020FHers was the centerpiece performance of\x01",
            "our little circus troupe--the one that\x01",
            "really brought the audiences in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1015F#6PIllusions...\x02\x03",

            "Does she use an orbment to make them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xE,
        (
            "#027F#4PNo, she used something she always\x01",
            "called 'illusion magic' which is apparently\x01",
            "some kind of very old, non-orbal art.\x02\x03",

            "Luciola was from a family with a tradition\x01",
            "of working that art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1026F#6PWas?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "#524F#4PPeople who fall in with a traveling circus like\x01",
            "ours tend to be one of two kinds.\x02\x03",

            "People who had cause to abandon their previous\x01",
            "home and families, or people who never had such\x01",
            "things to begin with...\x02\x03",

            "#026FLuciola was one of the former...\x01",
            "and I was the latter.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x79, 0xA)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x14)
    Sleep(100)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Scherazard")

    AnonymousTalk(    #194
        (
            "\x07\x0CI was about seven years old when Mr. Harvey and his band\x01",
            "took me in.\x02\x03",

            "Back then, I was little more than a street urchin living in\x01",
            "the slums of a city.\x02\x03",

            "Pickpocketing, petty theft... There was little I wouldn't do\x01",
            "to try to survive.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007F, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Scherazard")

    AnonymousTalk(    #195
        (
            "\x07\x0CThe ones who reached out a hand to me were the troupe's leader,\x01",
            "Mr. Harvey...and Luciola.\x02\x03",

            "They taught me, the little girl who couldn't trust anyone,\x01",
            "the warmth of a family...\x02\x03",

            "And they taught me all sorts of skills that would let me earn\x01",
            "a place for myself in the troupe.\x02\x03",

            "Dancing, beast handling, tarot reading... Luciola taught me\x01",
            "all of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Scherazard")

    AnonymousTalk(    #196
        (
            "\x07\x0CBut then...eight years ago...\x02\x03",

            "Mr. Harvey died in an accident. Without his leadership,\x01",
            "we all just...drifted apart and went our own ways.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240080, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Scherazard")

    AnonymousTalk(    #197
        (
            "\x07\x0CI'd been planning on staying with Luciola, but...\x02\x03",

            "Soon after Mr. Harvey died, she simply told me,\x01",
            "'There is something I must do'...and vanished.\x02\x03",

            "Hopeless and lost for the first time in years, I turned to\x01",
            "the one remaining man in the world whom I still trusted.\x02\x03",

            "As you might suspect, that was Cassius, who'd already begun\x01",
            "working as a bracer. You know the rest, I imagine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x79, 0x1, 0xA)
    OP_22(0x1C3, 0x1, 0x14)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x32)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x46)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x5A)
    Sleep(100)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #198
        0x101,
        (
            "#1026F#6PSo that's what happened... I had no idea\x01",
            "you'd gone through something like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xE,
        (
            "#026F#4PThe reason I aimed to become a bracer,\x01",
            "at first, was to improve myself.\x02\x03",

            "I wanted to be able to live and prosper on\x01",
            "my own...show Luciola just how far I'd\x01",
            "come once she returned.\x02\x03",

            "#524FBut...well, it has been eight years.\x02\x03",

            "Perhaps that was enough time to re-examine\x01",
            "my reasons...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#1003F#6PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xE,
        (
            "#021F#4PAww... Don't make that face.\x02\x03",

            "#020FLike Zin said, I don't intend to simply\x01",
            "fight her without saying a word.\x02\x03",

            "I want to hear Luciola's story from her\x01",
            "before doing anything.\x02\x03",

            "I want... I have to know what possible reason\x01",
            "could have made her associate with the\x01",
            "society.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1025F#6PYeah...that sounds good.\x02\x03",

            "#1018FI've got your back, Schera!\x01",
            "I'll do anything I can to help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        (
            "#021F#4PHaha! I know I can always\x01",
            "count on you.\x02\x03",

            "#027FStill, you've grown quite a bit,\x01",
            "haven't you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1004F#6PWh-What? That's kinda sudden.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        (
            "#524F#4PI always thought of you as being exactly\x01",
            "what I'd expect of Cassius' daughter...\x02\x03",

            "I don't think that's quite right, or fair,\x01",
            "any more, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        "#1015F#6PUh... What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xE,
        (
            "#020F#4PYour strength isn't quite the\x01",
            "same as Cassius'.\x02\x03",

            "Cassius has a heart as deep\x01",
            "as the ocean and strength like\x01",
            "a relentless wave...\x02\x03",

            "#021FBut you, Estelle? Your strength is like the sun.\x01",
            "You shine, and make others shine just by\x01",
            "being near them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#1004F#6PWh...\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x14)
    OP_24(0x1C3, 0x14)
    Sleep(100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #209
        "\x07\x05My Estelle... You shine like the sun.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_24(0x79, 0x1E)
    OP_24(0x1C3, 0x1E)
    Sleep(100)
    OP_24(0x79, 0x28)
    OP_24(0x1C3, 0x28)
    Sleep(100)
    OP_24(0x79, 0x32)
    OP_24(0x1C3, 0x3C)
    Sleep(100)
    OP_24(0x79, 0x3C)
    OP_24(0x1C3, 0x50)
    Sleep(100)
    OP_24(0x79, 0x46)
    OP_24(0x1C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #210
        0x101,
        "#1025F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xE,
        (
            "#026F#4PI think that's why people are attracted\x01",
            "to you so easily.\x02\x03",

            "It's what I like the most about you...\x01",
            "and I know Joshua felt the same way.\x02\x03",

            "#020FI don't think you need to feel any pressure\x01",
            "to 'live up' to Cassius, is my point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1012F#6PYeah...\x02\x03",

            "#1017FAhaha, you really are my big sister,\x01",
            "Schera.\x02\x03",

            "You always know how to encourage me...\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xE,
        (
            "#027F#4PHeehee. You're very welcome.\x02\x03",

            "#021FNot saying you should return the favor,\x01",
            "mind, but you really should drink with\x01",
            "me sometime.\x02\x03",

            "Now that you're a full bracer,\x01",
            "you'd better learn to handle\x01",
            "your liquor. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1019F#6PHow is booze related to--\x01",
            "You know what? Never mind.\x01",
            "I don't want to know.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1400, 5000, -4730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1400, 5000, -4730, 270)
    OP_8C(0xE, 90, 0)
    OP_4B(0xE, 255)
    Sleep(500)
    OP_A2(0x1A06)
    OP_21()
    OP_1D(0x1)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_31_5E8E end

    def Function_32_738E(): pass

    label("Function_32_738E")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x49)
    Return()

    # Function_32_738E end

    def Function_33_73A5(): pass

    label("Function_33_73A5")

    OP_20(0x3E8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_21()
    OP_1D(0x1)
    Return()

    # Function_33_73A5 end

    SaveToFile()

Try(main)

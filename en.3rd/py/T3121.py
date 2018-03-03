from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3121   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Orbal Gear',                           # 9
        'Agate',                                # 10
        'Tita',                                 # 11
        'Erika',                                # 12
        'Dan',                                  # 13
        'Professor Russell',                    # 14
        'Karl',                                 # 15
        'Worker',                               # 16
        'Box',                                  # 17
        'Box',                                  # 18
        'Drum',                                 # 19
        'Drum',                                 # 20
        'Drum',                                 # 21
        'Drum',                                 # 22
        'Drum',                                 # 23
        'Drum',                                 # 24
        'Drum',                                 # 25
        'Drum',                                 # 26
        'Panel',                                # 27
        'Panel',                                # 28
        'Target Camera',                        # 29
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
        'ED6_DT26/CH20601 ._CH',             # 00
        'ED6_DT27/CH04220 ._CH',             # 01
        'ED6_DT27/CH04221 ._CH',             # 02
        'ED6_DT27/CH04222 ._CH',             # 03
        'ED6_DT27/CH04223 ._CH',             # 04
        'ED6_DT06/CH20053 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT27/CH03970 ._CH',             # 07
        'ED6_DT27/CH03980 ._CH',             # 08
        'ED6_DT07/CH02020 ._CH',             # 09
        'ED6_DT07/CH02620 ._CH',             # 0A
        'ED6_DT07/CH01190 ._CH',             # 0B
        'ED6_DT07/CH01450 ._CH',             # 0C
        'ED6_DT07/CH00065 ._CH',             # 0D
        'ED6_DT06/CH20137 ._CH',             # 0E
        'ED6_DT07/CH00150 ._CH',             # 0F
        'ED6_DT07/CH00151 ._CH',             # 10
        'ED6_DT07/CH00153 ._CH',             # 11
        'ED6_DT07/CH00159 ._CH',             # 12
        'ED6_DT07/CH00064 ._CH',             # 13
        'ED6_DT27/CH04221 ._CH',             # 14
        'ED6_DT06/CH20104 ._CH',             # 15
        'ED6_DT07/CH00061 ._CH',             # 16
        'ED6_DT07/CH00154 ._CH',             # 17
        'ED6_DT07/CH00159 ._CH',             # 18
        'ED6_DT07/CH00151 ._CH',             # 19
        'ED6_DT07/CH00152 ._CH',             # 1A
        'ED6_DT06/CH20061 ._CH',             # 1B
        'ED6_DT26/CH20750 ._CH',             # 1C
        'ED6_DT26/CH20646 ._CH',             # 1D
        'ED6_DT26/CH20647 ._CH',             # 1E
        'ED6_DT26/CH20648 ._CH',             # 1F
        'ED6_DT26/CH20649 ._CH',             # 20
        'ED6_DT26/CH20755 ._CH',             # 21
        'ED6_DT26/CH20756 ._CH',             # 22
        'ED6_DT26/CH20695 ._CH',             # 23
        'ED6_DT26/CH20626 ._CH',             # 24
        'ED6_DT07/CH00054 ._CH',             # 25
        'ED6_DT07/CH00063 ._CH',             # 26
        'ED6_DT26/CH20697 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT26/CH20601P._CP',             # 00
        'ED6_DT27/CH04220P._CP',             # 01
        'ED6_DT27/CH04221P._CP',             # 02
        'ED6_DT27/CH04222P._CP',             # 03
        'ED6_DT27/CH04223P._CP',             # 04
        'ED6_DT06/CH20053P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT27/CH03970P._CP',             # 07
        'ED6_DT27/CH03980P._CP',             # 08
        'ED6_DT07/CH02020P._CP',             # 09
        'ED6_DT07/CH02620P._CP',             # 0A
        'ED6_DT07/CH01190P._CP',             # 0B
        'ED6_DT07/CH01450P._CP',             # 0C
        'ED6_DT07/CH00065P._CP',             # 0D
        'ED6_DT06/CH20137P._CP',             # 0E
        'ED6_DT07/CH00150P._CP',             # 0F
        'ED6_DT07/CH00151P._CP',             # 10
        'ED6_DT07/CH00153P._CP',             # 11
        'ED6_DT07/CH00159P._CP',             # 12
        'ED6_DT07/CH00064P._CP',             # 13
        'ED6_DT27/CH04221P._CP',             # 14
        'ED6_DT06/CH20104P._CP',             # 15
        'ED6_DT07/CH00061P._CP',             # 16
        'ED6_DT07/CH00154P._CP',             # 17
        'ED6_DT07/CH00159P._CP',             # 18
        'ED6_DT07/CH00151P._CP',             # 19
        'ED6_DT07/CH00152P._CP',             # 1A
        'ED6_DT06/CH20061P._CP',             # 1B
        'ED6_DT26/CH20750P._CP',             # 1C
        'ED6_DT26/CH20646P._CP',             # 1D
        'ED6_DT26/CH20647P._CP',             # 1E
        'ED6_DT26/CH20648P._CP',             # 1F
        'ED6_DT26/CH20649P._CP',             # 20
        'ED6_DT26/CH20755P._CP',             # 21
        'ED6_DT26/CH20756P._CP',             # 22
        'ED6_DT26/CH20695P._CP',             # 23
        'ED6_DT26/CH20626P._CP',             # 24
        'ED6_DT07/CH00054P._CP',             # 25
        'ED6_DT07/CH00063P._CP',             # 26
        'ED6_DT26/CH20697P._CP',             # 27
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 800,
        Y                   = 1000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1D5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
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


    ScpFunction(
        "Function_0_48A",          # 00, 0
        "Function_1_61D",          # 01, 1
        "Function_2_672",          # 02, 2
        "Function_3_70E",          # 03, 3
        "Function_4_786",          # 04, 4
        "Function_5_2DA5",         # 05, 5
        "Function_6_2DC1",         # 06, 6
        "Function_7_2E08",         # 07, 7
        "Function_8_2E56",         # 08, 8
        "Function_9_44AE",         # 09, 9
        "Function_10_44FD",        # 0A, 10
        "Function_11_45E6",        # 0B, 11
        "Function_12_467B",        # 0C, 12
        "Function_13_4B34",        # 0D, 13
        "Function_14_5620",        # 0E, 14
        "Function_15_5676",        # 0F, 15
        "Function_16_56F1",        # 10, 16
        "Function_17_5701",        # 11, 17
        "Function_18_5EA0",        # 12, 18
        "Function_19_5EEE",        # 13, 19
        "Function_20_5F35",        # 14, 20
        "Function_21_61F4",        # 15, 21
        "Function_22_6315",        # 16, 22
        "Function_23_7543",        # 17, 23
        "Function_24_755A",        # 18, 24
        "Function_25_7583",        # 19, 25
        "Function_26_75C3",        # 1A, 26
        "Function_27_75EB",        # 1B, 27
        "Function_28_8C38",        # 1C, 28
        "Function_29_8C80",        # 1D, 29
        "Function_30_8CC8",        # 1E, 30
        "Function_31_9DA7",        # 1F, 31
        "Function_32_9DE7",        # 20, 32
        "Function_33_9E10",        # 21, 33
        "Function_34_C00F",        # 22, 34
        "Function_35_C0EF",        # 23, 35
        "Function_36_DB47",        # 24, 36
        "Function_37_DB84",        # 25, 37
        "Function_38_DC10",        # 26, 38
        "Function_39_DC67",        # 27, 39
        "Function_40_DCF4",        # 28, 40
        "Function_41_DDA7",        # 29, 41
        "Function_42_DE66",        # 2A, 42
        "Function_43_DF3E",        # 2B, 43
        "Function_44_DF8E",        # 2C, 44
        "Function_45_E067",        # 2D, 45
        "Function_46_E0FA",        # 2E, 46
        "Function_47_E1CC",        # 2F, 47
        "Function_48_E21C",        # 30, 48
        "Function_49_E22A",        # 31, 49
        "Function_50_E289",        # 32, 50
        "Function_51_E2CB",        # 33, 51
        "Function_52_E321",        # 34, 52
        "Function_53_E380",        # 35, 53
        "Function_54_E3B3",        # 36, 54
        "Function_55_E3F5",        # 37, 55
        "Function_56_E43C",        # 38, 56
        "Function_57_E470",        # 39, 57
        "Function_58_E4D9",        # 3A, 58
        "Function_59_E547",        # 3B, 59
        "Function_60_E58D",        # 3C, 60
        "Function_61_E5DB",        # 3D, 61
        "Function_62_E5F0",        # 3E, 62
        "Function_63_E60A",        # 3F, 63
        "Function_64_E629",        # 40, 64
    )


    def Function_0_48A(): pass

    label("Function_0_48A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_4CC")
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_4EC")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_515")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_53E")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_567")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_590")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_5B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_5D5")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5D5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 30)

    label("loc_5D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_600")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 35)
    Jump("loc_61C")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_61C")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)

    label("loc_61C")

    Return()

    # Function_0_48A end

    def Function_1_61D(): pass

    label("Function_1_61D")

    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    Return()

    # Function_1_61D end

    def Function_2_672(): pass

    label("Function_2_672")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_697")
    OP_99(0xFE, 0x0, 0x5, 0x672)
    Jump("loc_6F8")

    label("loc_697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B0")
    OP_99(0xFE, 0x1, 0x5, 0x640)
    Jump("loc_6F8")

    label("loc_6B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C9")
    OP_99(0xFE, 0x2, 0x5, 0x60E)
    Jump("loc_6F8")

    label("loc_6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")
    OP_99(0xFE, 0x3, 0x5, 0x5DC)
    Jump("loc_6F8")

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x4, 0x5, 0x5AA)

    label("loc_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_99(0xFE, 0x0, 0x5, 0x5DC)
    Jump("loc_6F8")

    label("loc_70D")

    Return()

    # Function_2_672 end

    def Function_3_70E(): pass

    label("Function_3_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    Call(0, 27)

    label("loc_71F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    Call(0, 22)

    label("loc_730")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741")
    Call(0, 17)

    label("loc_741")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752")
    Call(0, 13)

    label("loc_752")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_763")
    Call(0, 12)

    label("loc_763")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_774")
    Call(0, 8)

    label("loc_774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785")
    Call(0, 4)

    label("loc_785")

    Return()

    # Function_3_70E end

    def Function_4_786(): pass

    label("Function_4_786")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x98)
    OP_6D(3260, 0, 7460, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 29)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 1100, 800, 8000, 180)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    ClearChrFlags(0x12, 0x20)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13760, 0, -1400, 90)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, 1260, 0, 3000, 0)
    OP_6F(0x8, 60)
    OP_6F(0x9, 60)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_72(0x1009, 0x0)
    ExitThread()
    LoadEffect(0x1, "map\\mp009_00.eff")
    LoadEffect(0x3, "Scraft\\sc000_31.eff")
    LoadEffect(0x0, "monster\\ms04220b.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    PlayEffect(0x0, 0x6, 0x10, 1000, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x10, -1000, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x10, 500, 700, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x10, -500, 700, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x3DC, 0x1, 0x50)

    def lambda_9D5():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9D5)
    ClearMapFlags(0x10)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x106,
        (
            "#054FYou doin' okay?!\x02\x03",

            "I've stopped it moving! Come on out!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x10,
        "Tita",
        (
            "#065FI-I can't...\x02\x03",

            "The seatbelt's stuck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        "#550FDamn it...\x02",
    )

    CloseMessageWindow()

    def lambda_A8E():
        OP_6D(2640, 0, 9800, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_A8E)

    def lambda_AA6():
        OP_67(0, 4120, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_AA6)

    def lambda_ABE():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_ABE)
    SetChrFlags(0x106, 0x1000)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 25)

    def lambda_ADD():

        label("loc_ADD")

        TurnDirection(0xFE, 0x10, 600)
        OP_48()
        Jump("loc_ADD")

    QueueWorkItem2(0x106, 2, lambda_ADD)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_AF3():
        OP_96(0xFE, 0xFFFFF72C, 0x0, 0x116C, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AF3)
    WaitChrThread(0x106, 0x1)
    OP_44(0x106, 0x2)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_B1F():
        OP_97(0xFE, 0x44C, 0x2008, 0x9C40, 0x1F40, 0x2)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B1F)
    WaitChrThread(0x106, 0x1)
    Sleep(100)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 26)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_B54():
        OP_96(0xFE, 0xFFFFFBC8, 0x0, 0x1F54, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B54)

    def lambda_B72():
        OP_99(0xFE, 0x2, 0x6, 0x384)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B72)
    Sleep(600)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)

    def lambda_B96():
        OP_8F(0xFE, 0x640, 0x320, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B96)
    PlayEffect(0x1, 0xFF, 0x106, 1200, 1000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x10, 0x2)

    def lambda_BFB():
        OP_9E(0xFE, 0x19, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BFB)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 65535)
    ClearChrFlags(0x106, 0x1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    def lambda_C42():
        OP_8F(0xFE, 0xFFFFFFD8, 0x0, 0x1F7C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C42)
    WaitChrThread(0x106, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x106, 0x4)

    def lambda_C6C():
        OP_96(0xFE, 0x410, 0x514, 0x1D74, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C6C)
    WaitChrThread(0x106, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    Fade(1000)
    SetChrChipByIndex(0x10, 32)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x106, 28)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x20)
    SetChrFlags(0x106, 0x1000)
    ClearChrFlags(0x106, 0x1)
    OP_0D()
    SetChrPos(0x13, 2540, 0, -5440, 0)
    OP_99(0x106, 0x0, 0x3, 0x3E8)
    Sleep(100)

    def lambda_CE1():
        OP_6D(3700, 0, 5920, 1200)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_CE1)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_CFE():
        OP_96(0xFE, 0x67C, 0x0, 0xBE0, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_CFE)
    SetChrSubChip(0x106, 4)
    Sleep(500)

    def lambda_D26():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_D26)
    WaitChrThread(0x106, 0x1)
    SetChrFlags(0x106, 0x1)
    ClearChrFlags(0x106, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_D4A():
        OP_8F(0xFE, 0x730, 0x0, 0xFFFFFA10, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D4A)
    Sleep(400)

    ChrTalk(    #3
        0x13,
        "#1833F#6PThank goodne--\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    ClearChrFlags(0x10, 0x20)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_22(0x17E, 0x0, 0x64)
    SetChrSubChip(0x106, 8)
    SetChrPos(0x106, 1600, 0, 4380, 180)
    SetChrPos(0x13, 1600, 0, -1520, 0)
    OP_6D(1600, 0, 7500, 0)
    OP_67(0, 4120, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_E09():
        OP_9E(0xFE, 0x19, 0x0, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E09)
    OP_0D()
    Sleep(1500)
    Fade(1200)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 30)

    def lambda_E7F():
        OP_99(0xFE, 0x0, 0x2, 0x258)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_E7F)
    OP_22(0x116, 0x0, 0x64)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x20)

    def lambda_E9E():
        OP_6B(2200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_E9E)

    def lambda_EAE():
        OP_8F(0xFE, 0x640, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EAE)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_20(0x7D0)
    FadeToDark(2000, 16777215, -1)
    Sleep(50)
    SetChrSubChip(0x10, 3)
    Sleep(50)
    OP_24(0x17E, 0x50)
    Sleep(100)
    OP_24(0x17E, 0x3C)
    Sleep(100)
    OP_24(0x17E, 0x28)
    Sleep(100)
    OP_24(0x17E, 0x14)
    OP_0D()
    OP_23(0x17E)
    Sleep(300)
    OP_22(0xF5, 0x0, 0x64)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 4)
    OP_6D(200, 0, -6340, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -620, -100, -6760, 270)
    SetChrFlags(0x106, 0x2)
    SetChrFlags(0x106, 0x800)
    SetChrFlags(0x106, 0x4)
    SetChrChipByIndex(0x106, 33)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x13, 1600, 0, -2520, 225)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 160, 0, 2820, 180)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_43(0x14, 0x0, 0x0, 0x7)

    def lambda_FD7():
        OP_6D(4040, 0, 4740, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_FD7)

    def lambda_FEF():
        OP_67(0, 3620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_FEF)

    def lambda_1007():
        OP_6B(3180, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1007)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #4
        0x12,
        (
            "#068F#40W...!\x02\x03",

            "#064FH-Huh...?\x02",
        )
    )

    CloseMessageWindow()
    Fade(800)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    OP_0D()
    OP_8C(0x12, 270, 300)
    Sleep(800)
    OP_8C(0x12, 135, 300)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(500)

    def lambda_1071():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1071)
    Sleep(500)
    OP_22(0x17E, 0x0, 0x64)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x12, 45, 500)
    Sleep(200)
    Fade(1500)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 0)
    OP_8C(0x10, 225, 0)
    Sleep(300)

    ChrTalk(    #5 op#A
        0x13,
        "#8A#4P#3STita!#2S\x02",
    )

    OP_0D()
    Sleep(300)

    def lambda_1104():
        OP_8F(0xFE, 0x1CC, 0x0, 0x578, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1104)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 30)

    def lambda_1132():
        OP_99(0xFE, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1132)
    WaitChrThread(0x10, 0x2)
    Fade(300)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x800)
    OP_6D(3220, -100, 7120, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(64000, 0)
    OP_6E(262, 0)

    def lambda_1199():
        OP_6D(2250, -100, 8070, 800)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_1199)

    def lambda_11B1():
        OP_6C(18000, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_11B1)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x8)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 34)
    SetChrSubChip(0x14, 7)
    SetChrPos(0x14, -9000, 0, 4980, 90)

    def lambda_11EB():
        OP_96(0xFE, 0x0, 0x0, 0x1374, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_11EB)
    Sleep(400)

    def lambda_120E():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_120E)

    ChrTalk(    #6 op#A op#5
        0x14,
        "#8A#3S#5PHaaah!#2S\x05\x02",
    )

    WaitChrThread(0x14, 0x1)

    def lambda_123B():

        label("loc_123B")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_123B")

    QueueWorkItem2(0x12, 2, lambda_123B)

    def lambda_124C():

        label("loc_124C")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_124C")

    QueueWorkItem2(0x13, 2, lambda_124C)
    OP_23(0x17E)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 31)

    def lambda_1279():
        OP_8F(0xFE, 0x11F8, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1279)
    PlayEffect(0x1, 0xFF, 0x14, 2000, 1000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)

    def lambda_12DA():
        OP_9E(0xFE, 0x14, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_12DA)
    WaitChrThread(0x10, 0x1)
    Sleep(200)

    def lambda_12FE():
        OP_6D(-670, -100, 8140, 400)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_12FE)

    def lambda_1316():
        OP_6C(323000, 400)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1316)
    OP_8C(0x10, 270, 500)
    SetChrSubChip(0x14, 7)
    SetChrFlags(0x14, 0x4)

    def lambda_1337():
        OP_96(0xFE, 0xC94, 0x0, 0x1374, 0x9C4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1337)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #7 op#A op#5
        0x14,
        "#10A#3S#1PHraaah!#2S\x05\x02",
    )

    Sleep(100)

    def lambda_137E():
        OP_99(0xFE, 0x7, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_137E)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    PlayEffect(0x1, 0xFF, 0x14, 2000, 500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_13E3():
        OP_8F(0xFE, 0x15E0, 0x320, 0x1310, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13E3)

    def lambda_13FE():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_13FE)
    Sleep(1000)
    Sleep(300)
    Fade(500)
    OP_6D(9000, 200, 8390, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0x3D3, 0x0, 0x64)
    PlayEffect(0x3, 0x2, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(500)
    OP_23(0x3DC)
    OP_22(0xF5, 0x0, 0x50)
    SetChrChipByIndex(0x10, 32)
    SetChrSubChip(0x10, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_14C4():
        OP_6D(9000, -100, 8390, 300)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_14C4)
    OP_0D()
    OP_20(0x7D0)
    Sleep(1000)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    OP_82(0x6, 0x2)
    Sleep(1500)

    ChrTalk(    #8
        0x14,
        "#1464FWhew... Just in the nick of time.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x4)
    OP_0D()
    Sleep(300)

    def lambda_154D():
        OP_6D(-1600, -100, 5800, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_154D)

    def lambda_1565():
        OP_67(0, 3780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1565)

    def lambda_157D():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_157D)

    def lambda_158D():
        OP_6C(320000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_158D)

    def lambda_159D():
        OP_6E(239, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_159D)
    OP_8C(0x14, 180, 500)

    def lambda_15B4():
        OP_8E(0xFE, 0x9D8, 0x0, 0x910, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15B4)
    WaitChrThread(0x14, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x13, 0x2)

    def lambda_15DC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_15DC)
    OP_8C(0x14, 270, 400)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #9
        0x14,
        "#1462F#12PAre you two okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x13,
        (
            "#1453F#5PTita and I are fine...\x02\x03",

            "...but...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_164C():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_164C)
    Sleep(300)
    TurnDirection(0x14, 0x106, 300)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    def lambda_1682():
        TurnDirection(0xFE, 0x106, 600)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1682)
    Sleep(500)

    ChrTalk(    #11
        0x12,
        "#065F#11POh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(2180, 0, -720, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(3380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #12
        0x12,
        "#566F#3SAgate!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_171E():
        OP_6D(160, 0, -5900, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_171E)

    def lambda_1736():
        OP_67(0, 5680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1736)

    def lambda_174E():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_174E)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_1768():
        OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0x820, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1768)
    WaitChrThread(0x12, 0x1)

    def lambda_1788():
        OP_8E(0xFE, 0xFFFFFDBC, 0x0, 0xFFFFE9BC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1788)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    Sleep(300)

    ChrTalk(    #13
        0x12,
        "#567F#5PAgate! #3SAgate!#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x106,
        "#4P#40W...\x02",
    )

    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x12, 19)
    SetChrSubChip(0x12, 0)
    OP_0D()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #15
        0x12,
        (
            "#069F#5P#40W...No...\x02\x03",

            "N-No...\x01",
            "This is all my fault...\x02\x03",

            "All because of me, you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x106,
        "#4P#40W...\x02",
    )

    CloseMessageWindow()

    def lambda_186A():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_186A)

    ChrTalk(    #17
        0x12,
        (
            "#562F#5P#40WI-I'm so...sorry...\x02\x03",

            "I'm always causing you nothing but trouble with\x01",
            "my selfishness...\x02\x03",

            "#069FIf I'd just kept quiet, none of this would've\x01",
            "happened...\x02\x03",

            "This is all my fault... All of it...\x02\x03",

            "If I hadn't said I wanted to get closer to Renne...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #18
        0x12,
        (
            "#567F#5PI knew I couldn't really do anything for her...\x01",
            "I knew this was just for my own satisfaction...\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1A00():
        OP_9E(0xFE, 0x5, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1A00)
    Sleep(1000)

    ChrTalk(    #19
        0x12,
        (
            "#562F#5P#40WThis wasn't what I wanted to happen at all...\x02\x03",

            "I swear, this wasn't what I was trying to do by\x01",
            "getting involved in this project...\x02\x03",

            "#069FBut... But...!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x24, 0x2)

    def lambda_1ACD():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1ACD)
    Sleep(1000)

    ChrTalk(    #20
        0x106,
        "#056F#4PGah...\x02",
    )

    CloseMessageWindow()

    def lambda_1B00():
        OP_99(0xFE, 0x0, 0x1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1B00)
    WaitChrThread(0x106, 0x2)
    Sleep(300)

    ChrTalk(    #21
        0x106,
        (
            "#552F#4PG-Give it a rest, will you?\x02\x03",

            "My head's poundin' enough without\x01",
            "you crying...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x64, 1400, 0x2, 0x7, 0x64, 0x1)
    Sleep(800)
    Fade(100)
    SetChrChipByIndex(0x12, 36)
    SetChrSubChip(0x12, 1)
    Sleep(300)

    ChrTalk(    #22
        0x12,
        (
            "#565F#5P#40WOh...\x02\x03",

            "A...Agate...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#057F#4PIt'll take more than that to finish me off.\x01",
            "I figured you knew that...\x02\x03",

            "#056F...Augh...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)

    def lambda_1C35():
        OP_9E(0xFE, 0xA, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_1C35)

    def lambda_1C4F():
        OP_99(0xFE, 0x1, 0x4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1C4F)
    WaitChrThread(0x106, 0x2)
    OP_44(0x106, 0x3)
    Sleep(300)
    OP_43(0x14, 0x0, 0x0, 0x5)
    SetChrPos(0x15, -60, 0, 2700, 180)
    SetChrPos(0x10, 4600, 800, 4880, 225)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)

    ChrTalk(    #24
        0x106,
        (
            "#551F#4PDamn, though. That thing packs a punch.\x02\x03",

            "I'm lucky I was able to block the brunt of\x01",
            "the impact with my sword...\x02\x03",

            "#556FHeh. If I hadn't, I'd probably have a date\x01",
            "with the Goddess right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x12,
        "#069F#5P#40W*hic*...*sniffle*...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 6)
    Sleep(200)
    OP_62(0x106, 0xFA, 1750, 0x28, 0x2B, 0x64, 0x2)
    Sleep(500)

    ChrTalk(    #26
        0x106,
        (
            "#055F#4PH-Hey! I said I'm fine, all right? This is nothing!\x02\x03",

            "So stop your crying, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x12,
        (
            "#562F#5P#40WB-But this is all because of me...\x02\x03",

            "#069F*sob* I'm so sorry! I'm so sorry!\x02\x03",

            "I... I...\x02\x03",

            "I'm not going to do this any more.\x01",
            "I quit...\x02\x03",

            "S-So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#053F#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x106,
        "#054F#4P#3SDon't you dare give up, Tita!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x64, 1400, 0x2, 0x7, 0x64, 0x1)
    Sleep(1000)

    ChrTalk(    #30
        0x12,
        "#065F#5P#40W...What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#057F#4PYou heard me. Don't you dare just throw\x01",
            "in the towel over something this small.\x02\x03",

            "You wanna get closer to Renne, right?\x02\x03",

            "You wanna understand her better, right?\x02\x03",

            "#053FThen try and do it. Don't just give up at\x01",
            "the first hurdle you come across.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        "#063F#5P#40WEven when you get hurt...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 4)
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrSubChip(0x106, 7)
    Sleep(1500)

    ChrTalk(    #33
        0x106,
        (
            "#053F#4PI've had a worthless ten years, Tita.\x02\x03",

            "I'm not gonna deny that...but there was\x01",
            "one thing I could never bring myself to do,\x01",
            "and that was to throw this away.\x02\x03",

            "Never.\x02\x03",

            "#051F...But that's fine.\x02\x03",

            "Because this is why I'm the bracer that\x01",
            "I am now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0xC8, 1600, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)
    SetChrSubChip(0x106, 4)
    Sleep(500)

    ChrTalk(    #34
        0x106,
        (
            "#053F#4PPlenty of folks have things that become\x01",
            "such a big part of them, they can't bear\x01",
            "to throw them away or leave them behind.\x02\x03",

            "Things that, no matter how much they try\x01",
            "to forget, they just can't.\x02\x03",

            "#556FI've got something like that.\x02\x03",

            "And I'm pretty sure you've found something\x01",
            "like that, too. Don't you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #35
        0x12,
        (
            "#064F#5P#40W...I...\x02\x03",

            "#062F(He's right...)\x02\x03",

            "(I... I really do.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x64, 1400, 0x18, 0x1B, 0xFA, 0x2)
    Sleep(2500)

    ChrTalk(    #36
        0x12,
        (
            "#561F#5PUmm... Agate...I...\x02\x03",

            "#062FI change my mind! I won't give up!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x106, 6)
    OP_0D()
    Sleep(300)

    ChrTalk(    #37
        0x12,
        (
            "#062F#5PI don't have time to stand around crying.\x01",
            "Not when I've got things I need to do.\x02\x03",

            "I'll think about what I can do, and I'm going\x01",
            "to do it!\x02\x03",

            "Because just like you're a bracer, I'm now a\x01",
            "researcher!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#556F#4P...\x02\x03",

            "#053FReally, now...?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x106, 0x20)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x106, 0x800)
    ClearChrFlags(0x106, 0x4)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x106, -580, 0, -6740, 0)
    OP_0D()
    OP_8C(0x106, 0, 400)
    Sleep(300)

    ChrTalk(    #39
        0x12,
        (
            "#064F#5P...?\x02\x03",

            "Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        "#556F#4PIt's nothin'.\x02",
    )

    CloseMessageWindow()

    def lambda_2525():
        OP_6D(160, 0, -5200, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_2525)
    OP_8E(0x106, 0xFFFFFE34, 0x0, 0xFFFFE778, 0x3E8, 0x0)
    OP_8C(0x106, 315, 400)
    WaitChrThread(0x24, 0x0)
    OP_22(0x8F, 0x0, 0x64)
    Fade(1000)
    SetChrChipByIndex(0x106, 35)
    SetChrSubChip(0x106, 0)
    SetChrFlags(0x106, 0x2)
    SetChrPos(0x106, -530, 0, -6010, 225)
    SetChrFlags(0x12, 0x8)
    OP_0D()
    Sleep(500)
    Sleep(500)
    OP_20(0x0)
    OP_22(0xF0, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(2000)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0xFA, 2000, 0x2, 0x7, 0x64, 0x1)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    SetChrFlags(0x10, 0x800)
    OP_8C(0x10, 280, 0)

    def lambda_260A():
        OP_6D(1920, 0, -800, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_260A)

    def lambda_2622():
        OP_67(0, 4300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_2622)

    def lambda_263A():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_263A)
    Sleep(500)
    SetChrPos(0x106, -460, 0, -6280, 315)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x106, 0x2)
    ClearChrFlags(0x12, 0x8)

    def lambda_2674():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2674)
    WaitChrThread(0x24, 0x0)
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(1000)

    def lambda_2698():

        label("loc_2698")

        TurnDirection(0xFE, 0x106, 500)
        OP_48()
        Jump("loc_2698")

    QueueWorkItem2(0x12, 2, lambda_2698)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_26BB():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFE9BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_26BB)
    WaitChrThread(0x106, 0x1)
    OP_44(0x12, 0x2)

    def lambda_26DF():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_26DF)
    Sleep(150)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #41
        0x106,
        "#055FWh-What's with the faces?\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    OP_63(0x13)
    OP_63(0x15)
    Sleep(500)

    ChrTalk(    #42
        0x13,
        (
            "#1457F*sigh*\x02\x03",

            "#1453FIt's all starting to make sense now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x15,
        (
            "#104FSee? I told you.\x02\x03",

            "He's rude, he's thickheaded, he's got all the\x01",
            "tact of a wrench to the groin...\x02\x03",

            "#100F...but there's promise in him. That there is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13,
        (
            "#1457FThe preparations for it aren't quite finished...\x02\x03",

            "#1832F...but I think it's time we get to the second\x01",
            "phase of testing our redheaded friend right\x01",
            "away!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #45
        0x106,
        "#055FTh-The hell are you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_28F1():
        OP_6D(2250, 0, -2600, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_28F1)

    def lambda_2909():

        label("loc_2909")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_2909")

    QueueWorkItem2(0x12, 2, lambda_2909)

    def lambda_291A():
        OP_8E(0xFE, 0x244, 0x0, 0xFFFFF218, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_291A)
    WaitChrThread(0x14, 0x1)
    OP_44(0x12, 0x2)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #46
        0x14,
        (
            "#1460F#5PIt looks like I underestimated you, Agate.\x02\x03",

            "Tita seems to have come out of this unharmed,\x01",
            "just as you promised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x106,
        "#052FO-Oh... Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x14,
        "#1461F#5PI'd like you to come to our house this evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#055F...Huh?\x02\x03",

            "I thought coming over for dinner was why\x01",
            "I was here in Zeiss to begin with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14,
        "#1465F#5P#40W...You'll be MORE than welcome.\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_2AC6():
        OP_8F(0xFE, 0x244, 0x0, 0xFFFFE890, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2AC6)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    ChrTalk(    #51
        0x106,
        "#055F(What's goin' on with him all of a sudden?)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x106, 500)
    Sleep(300)

    ChrTalk(    #52
        0x12,
        (
            "#560F#6PA-Agate!\x02\x03",

            "#561FUmm... Thank you very much again for earlier.\x02\x03",

            "You ended up having to protect me again...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x12, 500)
    Sleep(300)

    ChrTalk(    #53
        0x106,
        (
            "#055F#11PIt's fine. It doesn't bother me!\x02\x03",

            "#551FS-Still, sorry, but I think I'm gonna have to\x01",
            "pass on dinn--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "#560F#6PToday we're having a hotpot full of mushrooms\x01",
            "and wild plants, and a soup with lots of seaweed!\x02\x03",

            "#066FMom and Dad finally seem to understand you\x01",
            "better, too, so this should be really fun!\x02\x03",

            "#067FHeehee. Now we all get to enjoy a nice hotpot \x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x106,
        (
            "#556F#11P#40WO-Oh. Right...\x02\x03",

            "#551FHaha... I can hardly wait...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    Sleep(2000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_786 end

    def Function_5_2DA5(): pass

    label("Function_5_2DA5")

    OP_8E(0xFE, 0x5C8, 0x0, 0x578, 0x3E8, 0x0)
    OP_8C(0x14, 180, 400)
    Return()

    # Function_5_2DA5 end

    def Function_6_2DC1(): pass

    label("Function_6_2DC1")

    OP_24(0x3DC, 0x46)
    Sleep(200)
    OP_24(0x3DC, 0x3C)
    Sleep(200)
    OP_24(0x3DC, 0x32)
    Sleep(200)
    OP_24(0x3DC, 0x28)
    Sleep(200)
    OP_24(0x3DC, 0x1E)
    Sleep(200)
    OP_24(0x3DC, 0x14)
    Sleep(200)
    OP_24(0x3DC, 0xA)
    Sleep(200)
    OP_24(0x3DC, 0x0)
    OP_23(0x3DC)
    Return()

    # Function_6_2DC1 end

    def Function_7_2E08(): pass

    label("Function_7_2E08")

    OP_22(0x3DC, 0x1, 0x0)
    Sleep(100)
    OP_24(0x3DC, 0xA)
    Sleep(100)
    OP_24(0x3DC, 0x14)
    Sleep(100)
    OP_24(0x3DC, 0x1E)
    Sleep(100)
    OP_24(0x3DC, 0x28)
    Sleep(100)
    OP_24(0x3DC, 0x32)
    Sleep(100)
    OP_24(0x3DC, 0x3C)
    Sleep(100)
    OP_24(0x3DC, 0x46)
    Sleep(100)
    OP_24(0x3DC, 0x50)
    Return()

    # Function_7_2E08 end

    def Function_8_2E56(): pass

    label("Function_8_2E56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x57)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    LoadEffect(0x0, "monster\\ms04220b.eff")
    LoadEffect(0x1, "monster\\ms30109a.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_6D(7160, 0, 1720, 0)
    OP_67(0, 5980, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 4100, 800, 1000, 90)
    SetChrPos(0x106, 8119, 0, 1000, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6140, 0, -5220, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 13760, 0, -1400, 90)
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, 4600, 0, 8950, 0)
    OP_A1(0x19, 0x9)
    SetChrPos(0x19, 3200, 0, 8950, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2FA8"),
        (0, "loc_2FB5"),
        (SWITCH_DEFAULT, "loc_2FC2"),
    )


    label("loc_2FA8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FC2")

    label("loc_2FB5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2FC2")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FFA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆Won\x01",       # 0
            "◆Lost\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_2FFA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_300B"),
        (0, "loc_3018"),
        (SWITCH_DEFAULT, "loc_3025"),
    )


    label("loc_300B")

    SetChrChipByIndex(0x106, 23)
    SetChrSubChip(0x106, 3)
    Jump("loc_3025")

    label("loc_3018")

    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    Jump("loc_3025")

    label("loc_3025")


    def lambda_302B():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_302B)
    FadeToBright(2000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3050"),
        (0, "loc_3392"),
        (SWITCH_DEFAULT, "loc_367A"),
    )


    label("loc_3050")


    ChrTalk(    #56
        0x12,
        "#065FA-Agate! Are you all right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x106,
        "#053F#11PYeah, I'm fine. This is nothing.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()

    def lambda_30C2():
        OP_6D(9160, 0, 1720, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_30C2)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #58
        0x13,
        (
            "#1833F#1PHeehee... ㈱\x02\x03",

            "#1831FHeeheeheehee... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)
    Sleep(300)

    ChrTalk(    #59
        0x13,
        (
            "#1458F#3PHow does it feel to be thoroughly crushed,\x01",
            "Agate Crosner?\x02\x03",

            "Behold, the power of my Orbal Gear!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #60
        0x13,
        (
            "#1834F#3P#3SSo? How does it feel to be defeated by me?\x01",
            "Well? WELL?\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)

    def lambda_31F7():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_31F7)

    def lambda_3207():
        OP_67(0, 4980, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_3207)

    def lambda_321F():
        OP_8E(0xFE, 0x1FB7, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_321F)
    Sleep(600)

    def lambda_323F():
        OP_8E(0xFE, 0x17FC, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_323F)

    ChrTalk(    #61
        0x106,
        (
            "#555F#5PBy you? I'm pretty sure it was Tita who was\x01",
            "operating it...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x106, 500)
    Sleep(300)

    ChrTalk(    #62
        0x14,
        (
            "#1461F#6PHahaha...\x02\x03",

            "#1460FEither way, I think we can call that a victory\x01",
            "for the Orbal Gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x13,
        (
            "#1832F#12PBah... I was hoping I would get to enjoy that\x01",
            "for a while longer...\x02\x03",

            "This is no fun... This is no fun at all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_367A")

    label("loc_3392")


    ChrTalk(    #64
        0x106,
        "#051F#11P...Heh. That wraps that up.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()

    def lambda_33D8():
        OP_6D(9160, 0, 1720, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_33D8)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #65
        0x13,
        "#1830F#1PGrrr... Grrrrrrrrr...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 500)
    Sleep(300)

    ChrTalk(    #66
        0x13,
        (
            "#1459F#1PYou cheated!\x02\x03",

            "You totally, totally cheated!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)

    ChrTalk(    #67
        0x106,
        (
            "#052F#5PCheated, how?\x02\x03",

            "You're full of shit.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_349C():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_349C)

    def lambda_34AC():
        OP_67(0, 4980, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_34AC)

    def lambda_34C4():
        OP_8E(0xFE, 0x1FB7, 0x0, 0xFFFFFC40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_34C4)
    WaitChrThread(0x13, 0x1)
    Sleep(300)

    ChrTalk(    #68
        0x13,
        "#1830F#12PI am not!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #69
        0x13,
        (
            "#1830F#3S#12PYou used some kind of invisible special power.\x01",
            "You must have!#2S\x02",
        )
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x64)
    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #70
        0x106,
        "#055F#5PL-Like hell, I did!\x02",
    )

    CloseMessageWindow()

    def lambda_35A3():
        OP_8E(0xFE, 0x17FC, 0x0, 0xFFFFFC40, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_35A3)
    WaitChrThread(0x14, 0x1)
    TurnDirection(0x14, 0x106, 500)
    Sleep(300)

    ChrTalk(    #71
        0x14,
        (
            "#1461F#6PAll right, all right.\x02\x03",

            "#1460FWell, I think it's only fair to call this\x01",
            "Agate's victory.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)

    ChrTalk(    #72
        0x13,
        (
            "#1830F#3S#5PGrrrrrr...#2S\x02\x03",

            "#1832FRghhh... Mrrrgrgrr...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_367A")

    label("loc_367A")

    TurnDirection(0x106, 0x14, 500)
    Sleep(300)

    ChrTalk(    #73
        0x106,
        (
            "#053F#5PThat was the last of the tests, right?\x02\x03",

            "Request fulfilled, then. My work here's done.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(    #74
        0x13,
        (
            "#1457F#11PSilly me! I nearly forgot, Dan.\x02\x03",

            "#1450FDidn't you say you wanted a one-on-one fight\x01",
            "against this redheaded ruffian yesterday?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    ChrTalk(    #75
        0x14,
        (
            "#1463F#6PDid I?\x02\x03",

            "#1464FOh, right... I did.\x02\x03",

            "#1465FCassius told me a little about him, so I'd like\x01",
            "the opportunity at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        "#052F#5P...Wh-Wha...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x13, 500)
    Sleep(300)

    ChrTalk(    #77
        0x106,
        "#551F#5P(I have a bad, bad feeling about this...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x13,
        (
            "#1458F#11PHeh. You're the best.\x02\x03",

            "#1456FGo get your weapon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14,
        "#1463F#6PIt doesn't necessarily have to be now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x13,
        "#1834F#11PNo! You're doing it NOW. No time to waste!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14,
        (
            "#1464F#6P...All right.\x02\x03",

            "#1460FI'll leave things here to you, Erika.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 270, 500)

    def lambda_397F():
        OP_8E(0xFE, 0xFFFFF04D, 0x0, 0xFFFFFC40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_397F)
    WaitChrThread(0x14, 0x1)
    SetChrFlags(0x14, 0x8)
    TurnDirection(0x13, 0x106, 400)
    Sleep(300)

    ChrTalk(    #82
        0x13,
        (
            "#1456F#12PDon't think this is going to be easy, either.\x01",
            "He might've been forced to retire because\x01",
            "of an injury, but he's still VERY strong.\x02\x03",

            "He's the one who taught Cassius the basics\x01",
            "of fighting with a staff ten years ago, even.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x106,
        "#052F#5P#3SSeriously?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "#1458F#12PCassius then went on to perfect the art of\x01",
            "using one to fight himself, admittedly...\x02\x03",

            "#1833F...but that should give you an idea of just\x01",
            "how strong my awesome hubby is, surely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        (
            "#051F#5PHeh. Now I really don't wanna back down.\x02\x03",

            "#055F...Hey, wait a sec! The tests are over!\x01",
            "My work is done!\x02\x03",

            "Why am I stuck doin' another completely\x01",
            "unrelated fight?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x13,
        (
            "#1459F#12PYour work's not done until I say it is, bucko!\x02\x03",

            "#1454FOh, yeah. While we're waiting for Dan, I need\x01",
            "to check Tita hasn't got any injuries.\x02\x03",

            "#1835FBecause if she has, you know what's gonna\x01",
            "happen...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(300)

    ChrTalk(    #87
        0x13,
        "#1451F#11PCome on down, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x12,
        "#063FU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    def lambda_3D8B():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3D8B)
    Sleep(500)

    ChrTalk(    #89
        0x13,
        "#1454F#11PWhat's wrong, sweetie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x12,
        (
            "#067FI...kinda can't. Some weird error's come up\x01",
            "and I don't know what to do...\x02\x03",

            "#065FH-Huh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10, 0x2, 0x0, 0x9)
    OP_43(0x10, 0x1, 0x0, 0xA)
    Sleep(1000)
    OP_62(0x12, 0x1C2, 2300, 0x28, 0x2B, 0x96, 0x2)

    ChrTalk(    #91
        0x12,
        "#065FWh-What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x15,
        "#102F#1PO-Oh, no!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x98)
    Sleep(500)
    OP_22(0x17E, 0x0, 0x64)
    OP_43(0x12, 0x3, 0x0, 0xB)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0xC8, 0x0)

    ChrTalk(    #93
        0x13,
        (
            "#1454F#11PN-No...\x02\x03",

            "#1459FDamn it! No!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3EFD():
        OP_8E(0xFE, 0x206C, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3EFD)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 500)
    Sleep(200)
    OP_22(0x2BB, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #94
        0x13,
        (
            "#1830F#6PAgh... No matter what commands I try\x01",
            "to give it, it just won't respond!\x02\x03",

            "Shut it down, Tita!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x12,
        (
            "#065FI-I can't!\x02\x03",

            "It won't do anything I tell it to!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 600)
    Sleep(500)
    OP_8C(0x106, 270, 600)
    Sleep(500)
    OP_8C(0x106, 180, 600)
    Sleep(300)

    ChrTalk(    #96
        0x106,
        (
            "#055F#5PH-Hey... What's going on here?\x02\x03",

            "#054FExplain this in a way I can understand!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    ChrTalk(    #97
        0x12,
        "#065FU-Umm...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #98
        0x12,
        "#068F#3SAaaaaahhh!#2S\x02",
    )

    CloseMessageWindow()

    def lambda_40F1():
        OP_6D(6200, 0, 10160, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_40F1)

    def lambda_4109():
        OP_67(0, 4820, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4109)

    def lambda_4121():
        OP_6B(3100, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4121)
    OP_44(0x12, 0x3)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x1)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 0, 500)
    OP_82(0x7, 0x0)
    OP_44(0x10, 0x2)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_4166():
        OP_8E(0xFE, 0x1004, 0x320, 0x2008, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4166)
    WaitChrThread(0x12, 0x1)
    OP_23(0x187)
    OP_70(0x8, 0x3C)
    OP_70(0x9, 0x3C)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_44(0x10, 0x3)
    OP_43(0x10, 0x2, 0x0, 0x9)

    def lambda_41AC():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_41AC)
    OP_7C(0x1C2, 0x1C2, 0xBB8, 0x1F4)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(300)
    OP_23(0x17E)
    Sleep(1000)

    def lambda_41EE():
        OP_6D(6000, 0, 8240, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_41EE)

    def lambda_4206():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4206)

    def lambda_4216():
        OP_8E(0xFE, 0x10A4, 0x0, 0x10F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4216)
    OP_22(0x17E, 0x0, 0x64)
    Sleep(100)
    OP_23(0x17E)
    Sleep(300)
    OP_22(0x17E, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x12, 500)
    Sleep(300)

    ChrTalk(    #99
        0x106,
        (
            "#054FTita, what's going on?!\x02\x03",

            "Have you lost control of it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x12,
        "#065F#5PAgate...I...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #101
        0x12,
        "#068F#5P#3SRUN!#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()
    OP_8C(0x12, 180, 700)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_42F4():
        OP_9E(0xFE, 0x19, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_42F4)

    def lambda_430E():

        label("loc_430E")

        OP_7C(0x32, 0x32, 0xBB8, 0x7D0)
        OP_48()
        Jump("loc_430E")

    QueueWorkItem2(0x12, 3, lambda_430E)
    Sleep(300)

    ChrTalk(    #102
        0x106,
        "#550F#12P...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x106)
    OP_22(0xD5, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x106, 15)
    SetChrSubChip(0x106, 0)
    Sleep(500)

    def lambda_435D():
        OP_6D(5940, 0, 7020, 800)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_435D)

    def lambda_4375():
        OP_67(0, 3660, -10000, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4375)

    def lambda_438D():
        OP_6B(2540, 800)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_438D)

    def lambda_439D():
        OP_6C(36000, 800)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_439D)

    def lambda_43AD():
        OP_6E(312, 800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_43AD)
    SetChrChipByIndex(0x106, 18)
    SetChrSubChip(0x106, 0)

    def lambda_43C7():
        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_43C7)

    def lambda_43D7():
        OP_96(0xFE, 0x10A4, 0x0, 0x514, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_43D7)
    WaitChrThread(0x106, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x7, 0x0)
    OP_44(0x10, 0x2)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_4437():
        OP_8E(0xFE, 0x1004, 0x320, 0xC80, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4437)

    def lambda_4452():
        OP_6D(5940, 0, 4019, 1000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4452)

    def lambda_446A():
        OP_6B(1900, 1000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_446A)
    Sleep(400)
    OP_44(0x12, 0xFF)
    OP_44(0x10, 0xFF)
    OP_23(0x187)
    OP_44(0x24, 0xFF)
    Battle(0x3B9, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_2E56 end

    def Function_9_44AE(): pass

    label("Function_9_44AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44FC")
    PlayEffect(0x1, 0x7, 0x12, 0, 500, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_22(0x29, 0x0, 0x50)
    OP_83(0x7, 0x2)
    Sleep(1000)
    Jump("Function_9_44AE")

    label("loc_44FC")

    Return()

    # Function_9_44AE end

    def Function_10_44FD(): pass

    label("Function_10_44FD")

    Sleep(2000)
    PlayEffect(0x0, 0x6, 0x12, 1000, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    PlayEffect(0x0, 0x5, 0x12, -1000, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x0, 0x4, 0x12, 500, 1000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x3, 0x12, -500, 1000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_44FD end

    def Function_11_45E6(): pass

    label("Function_11_45E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4670")

    def lambda_45F5():
        OP_7C(0x32, 0x32, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45F5)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)

    def lambda_4617():
        OP_9E(0xFE, 0x0, 0x28, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4617)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_463A")
    Jump("loc_4670")

    label("loc_463A")

    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)

    def lambda_464A():
        OP_9E(0xFE, 0x28, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_464A)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_466D")
    Jump("loc_4670")

    label("loc_466D")

    Jump("Function_11_45E6")

    label("loc_4670")

    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_45E6 end

    def Function_12_467B(): pass

    label("Function_12_467B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_6D(-660, 0, 1260, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -900, 800, 1000, 180)
    SetChrPos(0x106, -2620, 0, 1000, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -2000, 0, -1120, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #103
        0x14,
        (
            "#1464F#12PThe last test we're going to be performing is\x01",
            "a mock battle to test the Orbal Gear's overall\x01",
            "capabilities.\x02\x03",

            "#1462FTake your positions, both of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x12,
        "#062F#5POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        "#053F#5PGot it.\x02",
    )

    CloseMessageWindow()

    def lambda_4837():
        OP_6D(-2000, 0, 1860, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4837)

    def lambda_484F():
        OP_67(0, 5540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_484F)

    def lambda_4867():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4867)

    def lambda_4877():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_4877)

    def lambda_4887():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4887)
    OP_8C(0x12, 90, 200)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)
    OP_22(0x187, 0x0, 0x64)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_48B7():
        OP_8E(0xFE, 0x578, 0x320, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_48B7)

    def lambda_48D2():
        OP_8E(0xFE, 0xFFFFEAE8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_48D2)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_23(0x187)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_4908():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_4908)
    WaitChrThread(0x106, 0x1)

    def lambda_491B():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_491B)
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #106
        0x13,
        (
            "#1457FWe've been through this once before, but it\x01",
            "bears repeating: only aim for the Orbal Gear.\x02\x03",

            "#1457FIf I find so much as a hair out of place on Tita...\x02\x01",

            "#1459F...you will be very painfully executed on the\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        (
            "#551F#5PI know, I know. You don't need to keep stating\x01",
            "the obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x14,
        "#1462FAre you ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#053F#5PYeah...\x02\x03",

            "#051F#3SBring it on!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_41(0x5, 0x0, 0xFF)
    OP_31(0x5, 0x10, 0x5A)
    OP_31(0x5, 0x5, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_35(0x5, 0xFFFF)
    OP_34(0x5, 0xFFFF)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x101)
    OP_37(0x5, 0x7F, 0x0)
    OP_37(0x5, 0x7F, 0x2)
    OP_41(0x5, 0x3E8, 0xFF)
    OP_34(0x5, 0x82)
    OP_34(0x5, 0x83)
    OP_34(0x5, 0x57)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0xA)
    OP_3E(0x207, 10)
    OP_3E(0x1F3, 10)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3B8, 0x300003, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_467B end

    def Function_13_4B34(): pass

    label("Function_13_4B34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x2, "monster\\ms04220.eff")
    OP_72(0x414, 0x0)
    ExitThread()
    OP_72(0x417, 0x0)
    ExitThread()
    OP_72(0x418, 0x0)
    ExitThread()
    OP_72(0x419, 0x0)
    ExitThread()
    OP_72(0x41A, 0x0)
    ExitThread()
    OP_72(0x41B, 0x0)
    ExitThread()
    OP_72(0x41C, 0x0)
    ExitThread()
    OP_72(0x41D, 0x0)
    ExitThread()
    OP_72(0x41E, 0x0)
    ExitThread()
    OP_72(0x41F, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x216, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(-5460, 0, -1060, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(45000, 0)
    OP_6E(448, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -11640, 800, 840, 135)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x106, -11140, 0, -2100, 45)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -9060, 0, -1000, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    OP_A1(0x1A, 0x18)
    OP_A1(0x1B, 0x19)
    OP_A1(0x1C, 0x1A)
    OP_A1(0x1D, 0x1B)
    OP_A1(0x1E, 0x1C)
    OP_A1(0x1F, 0x1D)
    OP_A1(0x20, 0x1E)
    OP_A1(0x21, 0x1F)
    SetChrPos(0x1C, -4000, 0, -6600, 0)
    SetChrPos(0x1A, -4000, 0, -5400, 0)
    SetChrPos(0x1E, -5300, 0, -5400, 0)
    SetChrPos(0x20, -5300, 0, -6600, 0)
    SetChrPos(0x1D, -4000, 0, 3400, 0)
    SetChrPos(0x1B, -4000, 0, 4600, 0)
    SetChrPos(0x1F, -5300, 0, 4600, 0)
    SetChrPos(0x21, -5300, 0, 3400, 0)
    OP_A1(0x22, 0x14)
    OP_A1(0x23, 0x17)
    SetChrPos(0x22, -4300, 0, -6000, 0)
    SetChrPos(0x23, -4300, 0, 4000, 0)

    def lambda_4D6E():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4D6E)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x24, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(-7700, 0, -1000, 0)
    OP_67(0, 6780, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(90000, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #110
        0x106,
        "#052F#12PHuh? What're we doing now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x14,
        (
            "#1460F#5PThis is a test of the Orbal Gear's precision.\x02\x03",

            "What I want you to do is to place the four\x01",
            "colored drum cans on their corresponding\x01",
            "tiles on the floor.\x02\x03",

            "#1461FIt'll be harder than it looks. Don't assume this\x01",
            "is going to be a snap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x106,
        (
            "#053F#12P...\x02\x03",

            "#552F(If I lose this, I'm never going to hear the end\x01",
            "of how I'm a clumsy excuse for a human, am I?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x14,
        "#1460F#5PAll right. Let's get started, then.\x02",
    )

    CloseMessageWindow()

    def lambda_4FA1():
        OP_6D(-5700, 0, -1000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4FA1)
    OP_43(0x12, 0x3, 0x0, 0xE)
    OP_8C(0x106, 135, 500)

    def lambda_4FC7():
        OP_8E(0xFE, 0xFFFFE37C, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4FC7)
    Sleep(1000)

    def lambda_4FE7():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4FE7)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 90, 500)
    WaitChrThread(0x12, 0x3)
    Sleep(1000)

    ChrTalk(    #114
        0x14,
        "#1462F#3SBegin!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-3040, 0, -1000, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(430, 0)
    SetChrPos(0x21, -1660, 0, 7000, 0)
    SetChrPos(0x1D, -7560, 0, 7000, 0)
    SetChrPos(0x1B, -7560, 0, 5260, 0)
    SetChrPos(0x1F, -4000, 0, 3400, 0)
    SetChrPos(0x20, -1660, 0, -3000, 0)
    SetChrPos(0x1E, -1660, 0, -9000, 0)
    SetChrPos(0x1A, -7560, 0, -9000, 0)
    SetChrPos(0x1C, -5300, 0, -5400, 0)
    SetChrPos(0x106, -5240, 0, -6020, 315)
    SetChrPos(0x12, -5600, 800, 7000, 180)

    def lambda_5126():
        OP_8E(0xFE, 0xFFFFE2B4, 0x0, 0xFFFFF1DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5126)

    def lambda_5141():
        OP_8F(0xFE, 0xFFFFE278, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5141)
    OP_43(0x12, 0x3, 0x0, 0xF)
    OP_43(0x1C, 0x3, 0x0, 0x10)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x1C, 0x1)
    Sleep(500)

    def lambda_5183():
        OP_8F(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFEFE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5183)
    WaitChrThread(0x106, 0x1)
    Sleep(300)

    ChrTalk(    #115
        0x106,
        "#051F#11PHeh. Piece of cake.\x02",
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x12, 0x3)
    Fade(500)
    OP_6D(0, 0, -40, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(90000, 0)
    OP_6E(284, 0)
    SetChrPos(0x13, 7000, 0, -5000, 90)
    SetChrPos(0x106, -8000, 0, -1660, 90)
    SetChrPos(0x14, -8960, 0, -400, 90)
    OP_0D()
    Sleep(300)

    ChrTalk(    #116
        0x13,
        (
            "#1454F#6PWow. We got some excellent data out of\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 315, 400)

    def lambda_528D():
        OP_8E(0xFE, 0x190, 0x0, 0xFFFFF9E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_528D)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 315, 400)

    ChrTalk(    #117
        0x13,
        (
            "#1451F#11PWell done, Tita. You did a wonderful job\x01",
            "operating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x12,
        (
            "#067F#6PHeehee.\x02\x03",

            "#560FThe adjustments Dad made made all the\x01",
            "difference, really.\x02\x03",

            "His tuning of the actuators was perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x13,
        (
            "#1451F#11PI don't doubt that.\x02\x03",

            "He's always been good at handling these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x12,
        "#067F#6PThe arms have acceleration control now, too.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 90, 400)
    Sleep(300)

    ChrTalk(    #121
        0x106,
        (
            "#551FMan, was there even any point in me being\x01",
            "here if you're just gonna ignore me?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_546C():
        OP_6D(-3340, 0, -1000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_546C)

    def lambda_5484():
        OP_67(0, 4540, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5484)

    def lambda_549C():
        OP_6B(2980, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_549C)
    WaitChrThread(0x24, 0x0)
    OP_8C(0x14, 135, 400)
    Sleep(300)

    ChrTalk(    #122
        0x14,
        (
            "#1460F#6PWell, that test was just about collecting data.\x01",
            "It didn't really matter who won.\x02\x03",

            "#1464FStill...\x02\x03",

            "#1465F...that's not true for the next one.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)
    Sleep(300)

    ChrTalk(    #123
        0x13,
        (
            "#1458F#12PHahahaha...\x02\x03",

            "#1835FNow the REAL fun begins!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x106, 0x4)
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_4B34 end

    def Function_14_5620(): pass

    label("Function_14_5620")

    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_22(0x187, 0x0, 0x64)
    OP_8C(0x12, 45, 400)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_5643():
        OP_8E(0xFE, 0xFFFFE2B4, 0x320, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5643)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_8C(0x12, 90, 400)
    OP_23(0x187)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    Return()

    # Function_14_5620 end

    def Function_15_5676(): pass

    label("Function_15_5676")

    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x187, 0x1, 0x3C)

    def lambda_5688():
        OP_8E(0xFE, 0xFFFFEA20, 0x320, 0x10A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5688)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 135, 400)

    def lambda_56AF():
        OP_8E(0xFE, 0xFFFFF358, 0x320, 0x744, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_56AF)

    def lambda_56CA():
        OP_8F(0xFE, 0xFFFFF984, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_56CA)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_23(0x187)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_15_5676 end

    def Function_16_56F1(): pass

    label("Function_16_56F1")

    OP_22(0x174, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x174, 0x0, 0x64)
    Return()

    # Function_16_56F1 end

    def Function_17_5701(): pass

    label("Function_17_5701")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_72(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x216, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_6D(-4460, 0, -1060, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(90000, 0)
    OP_6E(448, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, -9960, 800, -200, 90)
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x106, -9960, 0, -1960, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -6560, 0, -1100, 270)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8300, 0, -5000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 90)
    LoadEffect(0x0, "map\\mp021_00.eff")
    LoadEffect(0x1, "map\\mp065_01.eff")
    LoadEffect(0x2, "monster\\ms04220.eff")
    ClearMapFlags(0x10)

    def lambda_5854():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5854)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x24, 0x2)
    Sleep(500)
    Fade(1000)
    OP_6D(-8700, 0, 200, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #124
        0x14,
        (
            "#1460FThe first test is a simple race. You're going to\x01",
            "be doing three laps of the course, and the first\x01",
            "to the finish line wins.\x02\x03",

            "#1460FThere are obstacles in the way, too, just so you\x01",
            "know. Be careful of those.\x02\x03",

            "Are you ready, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#053F#6PReady as I'll ever be. Let's get this started.\x02\x03",

            "#555FI'm here for work, not to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x14,
        (
            "#1461FHaha. So you are.\x02\x03",

            "#1460FWell, take your positions.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x12)
    Sleep(400)

    def lambda_5A5D():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5A5D)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 500)
    Sleep(1000)

    ChrTalk(    #127
        0x14,
        "#1462F#3S#40WReady... Go!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x12, 0x3, 0x0, 0x14)
    OP_43(0x106, 0x3, 0x0, 0x15)
    Sleep(1000)
    Fade(500)
    OP_6D(-4500, 0, -6200, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1500)
    Fade(300)
    OP_6D(2250, 0, 3010, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_5B5D():
        OP_6D(1880, 0, 5150, 500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_5B5D)

    def lambda_5B75():
        OP_6B(2840, 500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5B75)

    def lambda_5B85():
        OP_6C(325000, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5B85)
    Sleep(1300)
    Fade(300)
    OP_6D(-9090, 0, 620, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(38000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x12, 0x3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-8700, 0, -200, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x106, 37)
    SetChrSubChip(0x106, 0)
    SetChrPos(0x12, -8960, 800, -3400, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #128
        0x106,
        (
            "#551F#5P*pant*...*pant*...\x02\x03",

            "#055FWhat just HAPPENED?! It flew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x12,
        (
            "#562FI-I'm sorry, Agate...\x02\x03",

            "But Mom told me I had to finish the race by\x01",
            "jumping over the finishing line all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x13,
        "#1456FHeeheehee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x106,
        "#555F#5P(I should've known...)\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    OP_8C(0x106, 90, 400)
    Sleep(300)

    ChrTalk(    #132
        0x14,
        (
            "#1461F#11PMind you, it's not like jumping was against\x01",
            "the rules of the race.\x02\x03",

            "And we wanted to collect the data from it,\x01",
            "too.\x02\x03",

            "#1465FI'd say you've only got yourself to blame for\x01",
            "getting cocky, wouldn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        "#552F#6PErk...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x106, 0x4)
    OP_71(0x415, 0x0)
    ExitThread()
    OP_72(0x416, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    SetMapFlags(0x10)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_5701 end

    def Function_18_5EA0(): pass

    label("Function_18_5EA0")

    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 45, 400)
    OP_43(0x10, 0x3, 0x0, 0x13)

    def lambda_5EBE():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5EBE)
    WaitChrThread(0x12, 0x1)
    OP_44(0x10, 0x3)
    OP_8C(0x12, 180, 400)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Return()

    # Function_18_5EA0 end

    def Function_19_5EEE(): pass

    label("Function_19_5EEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F34")
    PlayEffect(0x2, 0x3, 0x12, 0, -400, -400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jump("Function_19_5EEE")

    label("loc_5F34")

    Return()

    # Function_19_5EEE end

    def Function_20_5F35(): pass

    label("Function_20_5F35")

    OP_43(0x10, 0x3, 0x0, 0x13)
    OP_22(0x187, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)

    def lambda_5F51():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F51)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 500)

    def lambda_5F78():
        OP_8E(0xFE, 0xFFFFF6F0, 0x320, 0xFFFFE700, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F78)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 45, 400)

    def lambda_5F9F():
        OP_8E(0xFE, 0xA78, 0x320, 0xFFFFFA88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5F9F)
    WaitChrThread(0x12, 0x1)

    def lambda_5FBF():
        OP_8E(0xFE, 0xA78, 0x320, 0xFDB, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5FBF)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    OP_44(0x10, 0x3)
    OP_7C(0x64, 0x64, 0xBB8, 0x1F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x114, 0x0, 0x46)
    PlayEffect(0x1, 0x1, 0x12, -400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x12, 400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_6078():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFDB, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6078)
    WaitChrThread(0x12, 0x1)
    OP_23(0x187)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_8C(0x12, 180, 0)
    PlayEffect(0x1, 0x1, 0x12, -400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x12, 400, -600, 200, 0, 90, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xEE, 0x0, 0x64)

    def lambda_611A():
        OP_96(0xFE, 0xFFFFDD00, 0x320, 0xFFFFEED0, 0x3E8, 0x157C)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_611A)
    WaitChrThread(0x12, 0x1)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_22(0xEC, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0xC8, 0xBB8, 0xC8)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_6179():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6179)
    Sleep(300)

    def lambda_6199():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6199)
    Sleep(300)

    def lambda_61B9():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_61B9)
    Sleep(300)

    def lambda_61D9():
        OP_8E(0xFE, 0xFFFFDD00, 0x320, 0xFFFFE700, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_61D9)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_20_5F35 end

    def Function_21_61F4(): pass

    label("Function_21_61F4")


    def lambda_61FA():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0xFFFFE534, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_61FA)
    WaitChrThread(0x106, 0x1)

    def lambda_621A():
        OP_8E(0xFE, 0xFFFFDD14, 0x0, 0xFFFFDE18, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_621A)
    WaitChrThread(0x106, 0x1)

    def lambda_623A():
        OP_8E(0xFE, 0xFFFFF920, 0x0, 0xFFFFDE18, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_623A)
    WaitChrThread(0x106, 0x1)

    def lambda_625A():
        OP_8E(0xFE, 0x12D4, 0x0, 0xFFFFF7CC, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_625A)
    WaitChrThread(0x106, 0x1)

    def lambda_627A():
        OP_8E(0xFE, 0x12D4, 0x0, 0x120C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_627A)
    WaitChrThread(0x106, 0x1)

    def lambda_629A():
        OP_8E(0xFE, 0xA64, 0x0, 0x1A40, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_629A)
    WaitChrThread(0x106, 0x1)

    def lambda_62BA():
        OP_8E(0xFE, 0xFFFFDE18, 0x0, 0x1A40, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_62BA)
    WaitChrThread(0x106, 0x1)

    def lambda_62DA():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0x10CC, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_62DA)
    WaitChrThread(0x106, 0x1)

    def lambda_62FA():
        OP_8E(0xFE, 0xFFFFD5D0, 0x0, 0xFFFFFF38, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_62FA)
    WaitChrThread(0x106, 0x1)
    Return()

    # Function_21_61F4 end

    def Function_22_6315(): pass

    label("Function_22_6315")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(8420, 0, 1220, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 7000, 800, 1000, 270)
    SetChrPos(0x106, 5100, 0, -1400, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 6200, 0, -1400, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5100, 0, 1000, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 14140, 0, -2360, 100)
    OP_1D(0x57)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #134
        0x13,
        (
            "#1450F#6PWell, Tita? \x02\x03",

            "Do you think you'll be able to operate it all\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x12,
        (
            "#560F#11PYup! I'll be fine. I've had plenty of practice.\x02\x03",

            "I'm ready to go as soon as everyone else is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x15,
        (
            "#100F#3PBeginning monitoring.\x02\x03",

            "No problems in the data link!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14,
        "#1464F#12PLooks like we're good to go.\x02",
    )

    CloseMessageWindow()

    def lambda_6522():
        OP_6D(7300, 0, 260, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6522)

    def lambda_653A():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_653A)

    def lambda_654A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_654A)
    Sleep(150)
    TurnDirection(0x106, 0x14, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #138
        0x14,
        (
            "#1460F#11POkay, Agate. We're now going to begin testing\x01",
            "on the Orbal Gear Ver. 0.5.\x02\x03",

            "You sure you're ready for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x106,
        (
            "#053F#6P...Yeah, I am.\x02\x03",

            "#051FI've come this far. I'm not gonna turn tail now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x14,
        (
            "#1462F#11PI want you to promise one thing before we begin,\x01",
            "though.\x02\x03",

            "#1464FThe final test will be a mock battle between \x01",
            "yourself and the Orbal Gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x13,
        (
            "#1452F#5PIf you cause Tita to have so much as the ti-ni-est\x01",
            "scratch on her...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x106, 500)
    Sleep(300)

    ChrTalk(    #142
        0x13,
        "#1458F#5P...I'll be sending you up to the Goddess personally!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x14,
        (
            "#1461F#11PHahaha...\x02\x03",

            "#1465FI wouldn't go quite that far, but you get the idea.\x02\x03",

            "Don't hurt her, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x106,
        (
            "#551F#6PI know, I know.\x02\x03",

            "#050FI ain't gonna hold back, but I ain't gonna hurt her,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x14,
        (
            "#1464F#11PThat's all I wanted to hear.\x02\x03",

            "#1460FOkay! For starters...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6895():

        label("loc_6895")

        TurnDirection(0xFE, 0x106, 500)
        OP_48()
        Jump("loc_6895")

    QueueWorkItem2(0x14, 2, lambda_6895)

    def lambda_68A6():
        OP_8F(0xFE, 0x13EC, 0x0, 0xFFFFFD6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_68A6)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    def lambda_68FA():
        OP_8F(0xFE, 0x10CC, 0x0, 0xFFFFFA88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_68FA)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x14, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    def lambda_694E():
        OP_8F(0xFE, 0x13EC, 0x0, 0xFFFFF7A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_694E)
    WaitChrThread(0x14, 0x1)
    Sleep(300)
    OP_22(0xA, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x106, 0x1E, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #146
        (
            "\x07\x05Dan went around Agate and began attaching small quartz to various points on\x01",
            "his body.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #147
        0x106,
        "#055F#5PWh-What're you doing?\x02",
    )

    CloseMessageWindow()

    def lambda_6A42():
        OP_8F(0xFE, 0x1A2C, 0x0, 0xFFFFFA88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6A42)
    WaitChrThread(0x14, 0x1)
    OP_44(0x14, 0x2)
    Sleep(300)

    ChrTalk(    #148
        0x14,
        (
            "#1465F#11PThose are so that we can collect data from your\x01",
            "body in real time during the testing process.\x02\x03",

            "This prototype's mobility should be about equal\x01",
            "to your own, if not a little above what you're\x01",
            "capable of.\x02\x03",

            "#1461FSo this should be the perfect way to test what\x01",
            "it can really do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        (
            "#555F#6PWell, if that's your reason...\x02\x03",

            "#552FYou sure this isn't some form of harassment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x14,
        (
            "#1461F#11PHaha. Of course not.\x02\x03",

            "#1460F...Right.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6C20():

        label("loc_6C20")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6C20")

    QueueWorkItem2(0x14, 2, lambda_6C20)
    Sleep(200)

    def lambda_6C36():

        label("loc_6C36")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_6C36")

    QueueWorkItem2(0x106, 2, lambda_6C36)
    Sleep(500)

    ChrTalk(    #151
        0x14,
        "#1460F#12PErika, if you would?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #152
        0x13,
        "#1834F#11PGladly!\x02",
    )

    CloseMessageWindow()
    OP_59()
    LoadEffect(0x0, "map\\mp310_00.eff")

    def lambda_6CA7():
        OP_6D(1560, 0, 1840, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6CA7)

    def lambda_6CBF():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6CBF)

    def lambda_6CD7():
        OP_8F(0xFE, 0xE74, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6CD7)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x24, 0x0)
    Sleep(500)

    ChrTalk(    #153 op#A op#5
        0x13,
        "#20A#3SFuuuuuu!#2S\x05\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    Sleep(2000)

    ChrTalk(    #154 op#A op#5
        0x13,
        "#10A#3SHah!#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_6D53():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6D53)
    WaitChrThread(0x13, 0x1)
    Sleep(800)
    OP_8C(0x13, 180, 0)

    def lambda_6D7F():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xBB8, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6D7F)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #155 op#A op#5
        0x13,
        "#10A#3SHaaaaaah!#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_6DCB():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x1388, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6DCB)
    WaitChrThread(0x13, 0x1)
    Sleep(500)

    ChrTalk(    #156 op#A op#5
        0x13,
        "#15A#3SGaaaaaah!#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_97(0x13, 0xFFFFFE0C, 0xBB8, 0xFFFD40E0, 0x1B58, 0x1)
    OP_97(0x13, 0xFFFFFE0C, 0xFFFFFC18, 0x2BF20, 0x1B58, 0x1)
    Sleep(500)

    ChrTalk(    #157 op#A op#5
        0x13,
        "#15A#3SGaaaaaaaaa!#2\x05\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x64)

    def lambda_6E75():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFC18, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6E75)
    WaitChrThread(0x13, 0x1)

    def lambda_6E98():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x320, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6E98)
    WaitChrThread(0x13, 0x1)
    Sleep(600)

    ChrTalk(    #158 op#A op#5
        0x13,
        "#20A#3SShaaaon!#2\x05\x02",
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x1F4)
    OP_43(0x13, 0x3, 0x0, 0x18)

    def lambda_6EEF():
        OP_8E(0xFE, 0xFFFFEF98, 0x0, 0x3E8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6EEF)
    WaitChrThread(0x13, 0x1)
    OP_44(0x13, 0x3)
    OP_8C(0x13, 270, 0)
    Sleep(500)

    def lambda_6F1F():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6F1F)
    WaitChrThread(0x13, 0x1)
    Sleep(200)
    PlayEffect(0x0, 0x0, 0x13, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_6F81():
        OP_9E(0xFE, 0xF, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6F81)

    ChrTalk(    #159 op#A op#5
        0x13,
        "#20A#3SHaaaaaah!#2\x05\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x1F4)
    Sleep(3000)
    OP_44(0x106, 0xFF)
    OP_8C(0x106, 270, 0)

    def lambda_6FD4():
        OP_6D(4860, 0, 1840, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_6FD4)
    WaitChrThread(0x24, 0x0)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #160
        0x106,
        "#055F#11P...What am I even watching here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        (
            "#1460F#11PThat's Erika's Success Dance. She always does\x01",
            "it before every big test or experiment.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #162
        0x13,
        (
            "#1834F#11P#3SShaaaaaa!\x01",
            "All righty! I'm ready!#2S\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_82(0x0, 0x2)
    CloseMessageWindow()
    SetChrPos(0x15, 11680, 0, -2340, 270)

    def lambda_7105():

        label("loc_7105")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_7105")

    QueueWorkItem2(0x15, 2, lambda_7105)

    def lambda_7116():

        label("loc_7116")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_7116")

    QueueWorkItem2(0x106, 2, lambda_7116)

    def lambda_7127():
        OP_6D(10200, 0, -3140, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7127)

    def lambda_713F():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_713F)

    def lambda_714F():
        OP_8E(0xFE, 0x1F04, 0x0, 0xFFFFEC78, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_714F)
    Sleep(500)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7181():
        OP_8F(0xFE, 0x161C, 0x0, 0xFFFFFCA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7181)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 90, 500)
    OP_44(0x106, 0x2)
    OP_44(0x14, 0x2)
    OP_44(0x15, 0x2)
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x17)

    ChrTalk(    #163
        0x13,
        (
            "#1457F#12PTaptaptap!\x02\x03",

            "#1457FTaptaptaptap!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #164
        0x13,
        "#1834F#12PSetup complete!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x12,
        (
            "#067F#11PI-I can't believe you still do that after all\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x15,
        (
            "#104F#5PHmph. It's not like it actually has any practical\x01",
            "effect, either.\x02\x03",

            "#101FIf you look at the data from all the tests she's\x01",
            "done collectively, there's no difference in the\x01",
            "odds of success whether she does it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x15,
        "#101F#1PHere. Let me take care of that...\x02",
    )


    def lambda_7382():
        OP_8E(0xFE, 0x2698, 0x0, 0xFFFFF6DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7382)
    WaitChrThread(0x15, 0x1)

    def lambda_73A2():
        OP_8E(0xFE, 0x20D0, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_73A2)
    WaitChrThread(0x15, 0x1)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #168 op#A
        0x13,
        "#1830F#15A#3SFiiiiiire!#2S\x02",
    )


    def lambda_73E7():
        OP_8E(0xFE, 0x1F04, 0x0, 0xFFFFEF34, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_73E7)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #169 op#A
        0x15,
        "#103F#10A#3S#1PGraaaaaah!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x8E, 0x0, 0x64)
    OP_43(0x15, 0x3, 0x0, 0x19)
    WaitChrThread(0x15, 0x3)
    Sleep(1500)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x14, 270, 500)
    Sleep(300)

    ChrTalk(    #170
        0x14,
        (
            "#1465F#5PAs you can see, it's best to leave her alone\x01",
            "when she gets all fired up like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x106,
        (
            "#551F#6P(I'm feeling exhausted already, and we haven't\x01",
            "even started yet...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 9)
    SetChrSubChip(0x15, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_6315 end

    def Function_23_7543(): pass

    label("Function_23_7543")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7559")
    OP_22(0x2BB, 0x0, 0x50)
    Sleep(500)
    Jump("Function_23_7543")

    label("loc_7559")

    Return()

    # Function_23_7543 end

    def Function_24_755A(): pass

    label("Function_24_755A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7582")
    OP_8C(0x13, 270, 1000)
    OP_8C(0x13, 180, 1000)
    OP_8C(0x13, 90, 1000)
    OP_8C(0x13, 0, 1000)
    Jump("Function_24_755A")

    label("loc_7582")

    Return()

    # Function_24_755A end

    def Function_25_7583(): pass

    label("Function_25_7583")


    def lambda_7589():
        OP_96(0xFE, 0x2774, 0x0, 0xFFFFF7E0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7589)
    OP_43(0x15, 0x2, 0x0, 0x20)
    WaitChrThread(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_8C(0x15, 225, 0)
    SetChrChipByIndex(0x15, 21)
    SetChrSubChip(0x15, 0)
    Return()

    # Function_25_7583 end

    def Function_26_75C3(): pass

    label("Function_26_75C3")


    def lambda_75C9():
        OP_8E(0xFE, 0x1C34, 0x0, 0xFFFFFBA0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_75C9)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 0, 500)
    Return()

    # Function_26_75C3 end

    def Function_27_75EB(): pass

    label("Function_27_75EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-8400, 0, 9140, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5100, 0, 1000, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    SetChrPos(0x106, -9000, 0, 12000, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)

    def lambda_76D7():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1AF4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_76D7)
    Sleep(2000)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    Sleep(300)
    OP_8C(0x106, 270, 500)
    Sleep(600)
    OP_8C(0x106, 180, 500)
    Sleep(500)

    ChrTalk(    #172
        0x106,
        "#552F#5PI guess this is the place...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 135, 500)
    Sleep(200)

    ChrTalk(    #173
        0x106,
        "#055F#6PW-Wait! Is that it?!\x02",
    )

    CloseMessageWindow()

    def lambda_77A1():
        OP_6D(6400, 0, 1000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_77A1)

    def lambda_77B9():
        OP_6C(90000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_77B9)
    WaitChrThread(0x24, 0x0)
    Sleep(500)

    ChrTalk(    #174
        0x12,
        (
            "#061F#6PThat's all the checks on the legs complete!\x02\x03",

            "#560FI guess I'll check the settings one more time, \x01",
            "too.\x02\x03",

            "I've got nothing to do till Mom and Dad come \x01",
            "back, so I should make the most of it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_789D():
        OP_8E(0xFE, 0x13EC, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_789D)
    WaitChrThread(0x12, 0x1)

    def lambda_78BD():
        OP_8E(0xFE, 0x1E78, 0x0, 0xFFFFED40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_78BD)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    OP_62(0x12, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x106, -3800, 0, 1000, 90)

    def lambda_7916():
        OP_8E(0xFE, 0x898, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7916)
    WaitChrThread(0x106, 0x1)
    Sleep(300)

    ChrTalk(    #175
        0x106,
        (
            "#055FI thought it was gonna be an orbal cannon...\x02\x03",

            "Can't believe you're makin' a robot as nuts\x01",
            "as this.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x12, 315, 500)

    ChrTalk(    #176
        0x12,
        (
            "#064F#1PA-Agate?!\x02\x03",

            "What are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #177
        0x12,
        (
            "#065F#1PIs it because of Mom?!\x02\x03",

            "Did she ask you to come here?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A69():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_7A69)

    def lambda_7A77():
        OP_6D(4700, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7A77)

    def lambda_7A8F():
        OP_67(0, 5820, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7A8F)
    SetChrChipByIndex(0x12, 22)
    SetChrSubChip(0x12, 0)

    def lambda_7AB1():
        OP_8E(0xFE, 0xCF8, 0x0, 0xFFFFFF74, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7AB1)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 6)
    SetChrSubChip(0x12, 0)
    Sleep(500)

    ChrTalk(    #178
        0x12,
        (
            "#562F#11PI-I'm so sorry...\x02\x03",

            "Mom and Dad seem to've got you all wrong...\x02\x03",

            "#063FI keep trying to explain to them what you're\x01",
            "really like, but they never listen to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x106,
        (
            "#551F#6PIt's not a big deal. I ain't here because your\x01",
            "mom asked me to come, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x12,
        "#064F#11PYou're not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x106,
        (
            "#552F#6PI... Well...\x02\x03",

            "I heard you were working pretty hard down\x01",
            "here. Like, as a proper engineer.\x02\x03",

            "#051FSo I figured I'd come and join you as my way\x01",
            "of showing my support, I guess.\x02\x03",

            "Helping with these tests is an official request\x01",
            "anyway, so it works out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x12,
        (
            "#565F#11P...\x02\x03",

            "#067FHeehee...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7D3E():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7D3E)
    Sleep(150)
    OP_8C(0x106, 90, 500)
    Sleep(300)

    ChrTalk(    #183
        0x12,
        (
            "#061F#12POkay. Let me give you a brief rundown of the\x01",
            "Orbal Gear, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x0, 0x0, 0x1A)

    def lambda_7DB1():
        OP_6D(9620, 0, 250, 4500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_7DB1)

    ChrTalk(    #184
        0x12,
        (
            "#061F#12PThe prototype's most distinguishing characteristic\x01",
            "is that the pilot can climb inside and operate it\x01",
            "directly from within.\x02\x03",

            "#060FIt hasn't been decided for sure the final model will\x01",
            "necessarily be like this, though.\x02\x03",

            "Oh, and then there's how it reaches its maximum\x01",
            "mobility...\x02\x03",

            "#560FCome over here for a minute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x106,
        "#052F#5PS-Sure...\x02",
    )

    CloseMessageWindow()

    def lambda_7F26():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_7F26)

    def lambda_7F36():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFFFBA0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7F36)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 0, 500)
    Sleep(300)

    def lambda_7F62():

        label("loc_7F62")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_7F62")

    QueueWorkItem2(0x12, 2, lambda_7F62)

    def lambda_7F73():
        OP_8F(0xFE, 0x1D5B, 0x0, 0xFFFFFCC7, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F73)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #186
        0x12,
        (
            "#560F#12PWe've designed a new walking system to increase\x01",
            "its mobility substantially, you see.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7FFB():
        OP_8F(0xFE, 0x1E82, 0x0, 0xFFFFFDEE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7FFB)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #187
        0x12,
        (
            "#560F#12POrdinarily, bipedal robots require two units that\x01",
            "control their posture and center of gravity which\x01",
            "work in tandem with one another to walk...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80BD():
        OP_8F(0xFE, 0x1FA9, 0x0, 0xFFFFFF15, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_80BD)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #188
        0x12,
        (
            "#061F#12P...but this approach really drains system resources\x01",
            "across the whole archaism. The way we've chosen \x01",
            "to resolve this is...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_816B():
        OP_8F(0xFE, 0x20D0, 0x0, 0x3C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_816B)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8400, 0, 2600, 180)
    WaitChrThread(0x12, 0x0)

    def lambda_81AB():
        OP_8F(0xFE, 0x20D0, 0x0, 0x618, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_81AB)
    WaitChrThread(0x12, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_81D0():
        OP_96(0xFE, 0x2094, 0x0, 0x3C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_81D0)
    WaitChrThread(0x12, 0x1)

    def lambda_81F3():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_81F3)
    OP_44(0x12, 0x2)
    OP_62(0x12, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x12, 0, 500)
    Sleep(300)

    ChrTalk(    #189
        0x12,
        "#064F#12P...H-Huh?\x02",
    )

    CloseMessageWindow()

    def lambda_8245():

        label("loc_8245")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_8245")

    QueueWorkItem2(0x12, 2, lambda_8245)

    def lambda_8256():

        label("loc_8256")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_8256")

    QueueWorkItem2(0x106, 2, lambda_8256)

    def lambda_8267():
        OP_8F(0xFE, 0x20D0, 0x0, 0xFFFFFB50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8267)

    def lambda_8282():
        OP_8F(0xFE, 0x20D0, 0x0, 0x3C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8282)
    WaitChrThread(0x13, 0x1)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #190
        0x106,
        "#055F#6PWh-What the hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x12,
        "#065F#12PM-Mom?! How long have you been there?!\x02",
    )

    CloseMessageWindow()

    def lambda_834A():
        OP_8E(0xFE, 0x1D9C, 0x0, 0xFFFFFBDC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_834A)
    WaitChrThread(0x13, 0x1)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #192
        0x13,
        (
            "#1456F#11PSo you've decided to assist with the tests,\x01",
            "have you, Agate Crosner? You're so sweet.\x02\x03",

            "Does that mean you've finally accepted your\x01",
            "sins and have come to repent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x106,
        "#555F#6PI have no frickin' clue what you're talking about...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x13,
        (
            "#1451F#11PYou were trying to get close to Tita thinking\x01",
            "I wasn't here, weren't you?!\x02\x03",

            "Admit your sins and REPENT!\x02\x03",

            "#1835FI finally have firsthand evidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x106,
        (
            "#055F#6PFor cryin' out loud, will you quit with the eyes?\x01",
            "It's giving me the creeps.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x12, 0x2)
    OP_44(0x106, 0x2)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, 14300, 4000, 100, 270)
    SetChrPos(0x14, 14300, 4000, 1200, 270)

    NpcTalk(    #196
        0x15,
        "Elderly Man's Voice",
        (
            "#12PHe might be completely useless when it\x01",
            "comes to technology...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #197
        0x15,
        "Elderly Man's Voice",
        "#12P...but he's got potential, don't you think?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #198
        0x14,
        "Man's Voice",
        "#3PYou might just be right.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #199
        0x14,
        "Man's Voice",
        "#3PI have to admit, there were concerns...\x02",
    )

    CloseMessageWindow()

    def lambda_86A4():
        OP_6D(10260, 3000, -660, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_86A4)

    def lambda_86BC():
        OP_67(0, 2640, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_86BC)

    def lambda_86D4():
        OP_6B(3540, 2000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_86D4)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #200
        0x14,
        (
            "#1460F#6P...but I can appreciate that he at least tries\x01",
            "to follow subjects he doesn't understand\x01",
            "instead of outright refusing to listen to them.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #201
        0x106,
        (
            "#055F#5PWhat're you two doing up there?!\x02\x03",

            "Especially you, Dan! You were just up\x01",
            "on the roof with me a minute ago! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x14,
        (
            "#1465F#12PI did tell you I was going to watch the tests,\x01",
            "didn't I?\x02\x03",

            "#1461FWell, here I am!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#551F#5P(I-I can't work out what he's thinking any\x01",
            "more than I can his wife...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x13,
        "#1830F#11PDon't you dare ignore me, Agate Crosner!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(8780, 0, 20, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    SetChrPos(0x15, 15200, 0, 7300, 180)
    SetChrPos(0x14, 15200, 0, 7300, 180)
    OP_43(0x15, 0x3, 0x0, 0x1C)
    Sleep(1000)
    OP_43(0x14, 0x3, 0x0, 0x1D)

    def lambda_8978():
        OP_8E(0xFE, 0x19B4, 0x0, 0xFFFFFBDC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8978)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_89AF():
        OP_8F(0xFE, 0x1450, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_89AF)
    WaitChrThread(0x106, 0x1)

    def lambda_89CF():
        OP_8F(0xFE, 0x1D9C, 0x0, 0xFFFFFBDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_89CF)
    WaitChrThread(0x15, 0x3)
    Sleep(300)

    ChrTalk(    #205
        0x15,
        "#101F#11PWell, regardless, that's everyone gathered now.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x3)

    ChrTalk(    #206
        0x14,
        "#1460F#11PI suppose it's time for us to begin.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 0)
    OP_8C(0x12, 95, 500)
    Sleep(600)
    OP_8C(0x12, 135, 500)
    OP_8C(0x12, 270, 500)
    Sleep(300)

    ChrTalk(    #207
        0x12,
        (
            "#064F#11PU-Umm...\x02\x03",

            "Err, what are we doing? I've finished all of\x01",
            "the necessary final checks...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)

    ChrTalk(    #208
        0x13,
        (
            "#1451F#5PGood girl, Tita.\x02\x03",

            "#1834FLet the testing begin!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #209
        0x15,
        "#101F#11PHahahahaha!\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #210
        0x14,
        "#1461F#11PHahaha...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    ChrTalk(    #211
        0x13,
        "#1451F#5P#3SAaaaahahahaha!#2S\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x106,
        "#551F#6PWhat is wrong with this family?\x02",
    )

    CloseMessageWindow()

    def lambda_8C12():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_8C12)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_75EB end

    def Function_28_8C38(): pass

    label("Function_28_8C38")


    def lambda_8C3E():
        OP_8E(0xFE, 0x3B60, 0x0, 0xF3C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8C3E)
    WaitChrThread(0x15, 0x1)

    def lambda_8C5E():
        OP_8E(0xFE, 0x23F0, 0x0, 0xFFFFF7CC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8C5E)
    WaitChrThread(0x15, 0x1)
    OP_8C(0x15, 270, 500)
    Return()

    # Function_28_8C38 end

    def Function_29_8C80(): pass

    label("Function_29_8C80")


    def lambda_8C86():
        OP_8E(0xFE, 0x3B60, 0x0, 0x125C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8C86)
    WaitChrThread(0x14, 0x1)

    def lambda_8CA6():
        OP_8E(0xFE, 0x2710, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8CA6)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 270, 500)
    Return()

    # Function_29_8C80 end

    def Function_30_8CC8(): pass

    label("Function_30_8CC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(8100, 500, 2240, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -9000, 0, 14600, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, 7020, 2000, 980, 90)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5300, 0, 1400, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -4600, 0, 3260, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -9000, 0, 12000, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #213
        0x14,
        (
            "#1460FWell, that's everything switched that needs to be.\x02\x03",

            "The machine guns are new models, so they could\x01",
            "probably do with some tweaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x13,
        (
            "#1458F#6PThat's all of its armaments strengthened.\x02\x03",

            "Its mobility is up 16% because of all the\x01",
            "work we did through the night, you know.\x02\x03",

            "#1456FHah. Okay! I think we should leave it like this\x01",
            "for now and take some data as is before we\x01",
            "start doing anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x14,
        (
            "#1464FWorks for me. Ordinarily, we'd just settle for\x01",
            "testing whether it can perform basic actions\x01",
            "at this stage then call it a day...\x02\x03",

            "#1465F...but thanks to all of Tita's help, it's ended up\x01",
            "relatively complete for a prototype.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 500)

    def lambda_9037():
        OP_96(0xFE, 0x1B6C, 0x0, 0xFFFFFD1C, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9037)
    WaitChrThread(0x14, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x14, 0x4)
    TurnDirection(0x14, 0x13, 400)
    Sleep(300)

    ChrTalk(    #216
        0x14,
        (
            "#1461F#11PI think we could probably get away with doing\x01",
            "a simple combat test using it, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x13,
        (
            "#1457F#6PAnd we should, too!\x02\x03",

            "#1835FAfter all, it just so happens that we have the \x01",
            "peeerfect guinea pig for it coming!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)

    def lambda_9163():
        OP_6D(5900, 0, 1920, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_9163)

    def lambda_917B():
        OP_67(0, 5700, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_917B)

    def lambda_9193():
        OP_8F(0xFE, 0x794, 0x0, 0x104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9193)

    def lambda_91AE():
        OP_8C(0x14, 270, 300)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_91AE)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #218
        0x12,
        (
            "#560F#6PMom! Dad!\x02\x03",

            "Umm...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91E0():
        OP_8F(0xFE, 0x139C, 0x0, 0x78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_91E0)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 270, 500)
    Sleep(300)

    ChrTalk(    #219
        0x14,
        "#1460F#11PMorning, Tita. Did you sleep well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x12,
        (
            "#060F#6PY-Yeah... I'm feeling great.\x02\x03",

            "#063FB-But... Umm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x13,
        (
            "#1456F#5PAll I can picture in my mind is the sight of that red-\x01",
            "haired hooligan crawling on the ground after\x01",
            "getting the beating of a lifetime by the Orbal Gear...\x02\x03",

            "#1831FI can hardly wait to see it in real life, too... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #222
        0x12,
        (
            "#065F#6PM-Mom!\x02\x03",

            "I keep trying to tell you that Agate's really not\x01",
            "a bad person!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x14,
        (
            "#1461F#11PAhaha... Don't take what she's saying to heart,\x01",
            "Tita.\x02\x03",

            "#1465FShe could probably stand to discuss the issue\x01",
            "a bit more...tactfully...\x02\x03",

            "...but I'm sure all she wants is to find out exactly\x01",
            "what Agate's doing trying to worm his way to you\x01",
            "in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x12,
        "#065F#6PU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #225
        0x12,
        (
            "#561F#6P(Oh, boy... Even Dad seems to have him wrong.)\x02\x03",

            "#062FOkay, let me explain this one more time.\x02\x03",

            "He might be sorta rude and blunt, and he does\x01",
            "grumble every time he has to do something, and\x01",
            "he has a bad habit of scaring people off easily...\x02\x03",

            "...but he's actually a kind, good person! I swear!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x13)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #226
        0x14,
        (
            "#1463F#11PR-Really, now...?\x02\x03",

            "#1464FI'm starting to get a little worried about him,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x12,
        (
            "#065F#6PWhaaat?! Why?!\x02\x03",

            "I keep saying he's really a nice person!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #228
        0x13,
        (
            "#1457F#5PAll right. Time to go and get things ready.\x02\x03",

            "#1452FI'll leave the final adjustments to you, Dan.\x01",
            "I've got something to take care of elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 500)
    Sleep(300)

    ChrTalk(    #229
        0x14,
        "#1462F#12PYou're going, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x13,
        (
            "#1457F#5PThat I am.\x02\x03",

            "I've heard more than enough! Something has\x01",
            "to be done!\x02\x03",

            "#1835FThe sinner must be punished...with death!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9878():

        label("loc_9878")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_9878")

    QueueWorkItem2(0x12, 2, lambda_9878)

    def lambda_9889():

        label("loc_9889")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_9889")

    QueueWorkItem2(0x14, 2, lambda_9889)

    def lambda_989A():
        OP_8E(0xFE, 0xFFFFE610, 0x0, 0x578, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_989A)
    Sleep(500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #231
        0x12,
        (
            "#065F#5PWhaaat?!\x02\x03",

            "M-Mom?! Where are you going?\x02\x03",

            "W-Wait!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_9920():
        OP_8E(0xFE, 0xFFFFE9F8, 0x0, 0x104, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9920)
    WaitChrThread(0x12, 0x1)
    Fade(1000)
    OP_6D(-9000, 0, 10480, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_44(0x12, 0x2)
    OP_44(0x14, 0x2)
    SetChrPos(0x13, 480, 0, 1780, 225)
    SetChrPos(0x12, 480, 0, 1780, 225)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)

    def lambda_99D2():
        OP_6D(-7260, 0, 8680, 3500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_99D2)

    def lambda_99EA():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_99EA)

    def lambda_99FA():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_99FA)
    Sleep(100)

    def lambda_9A1A():
        OP_8E(0xFE, 0xFFFFF394, 0x0, 0x6F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9A1A)
    WaitChrThread(0x13, 0x1)

    def lambda_9A3A():
        OP_8E(0xFE, 0xFFFFDECC, 0x0, 0x1BBC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9A3A)
    WaitChrThread(0x13, 0x1)
    OP_22(0x8E, 0x0, 0x64)

    ChrTalk(    #232 op#A
        0x15,
        "#103F#10A#5P#3SGaaah!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_43(0x15, 0x3, 0x0, 0x1F)

    def lambda_9A94():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9A94)
    WaitChrThread(0x13, 0x1)

    def lambda_9AB4():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9AB4)
    WaitChrThread(0x13, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_9AE7():
        OP_8E(0xFE, 0xFFFFF394, 0x0, 0x6F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9AE7)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x13, 0x8)

    def lambda_9B0C():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9B0C)
    Sleep(600)

    ChrTalk(    #233 op#A
        0x12,
        "#068F#10A#6P#3SMoooooom!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    WaitChrThread(0x12, 0x1)

    def lambda_9B62():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9B62)
    Sleep(100)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #234
        0x15,
        "#102F#11PWh-What in Aidios' name is happening here?\x02",
    )

    CloseMessageWindow()

    def lambda_9BEB():
        OP_6D(-5590, 0, 8720, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_9BEB)
    SetChrPos(0x14, -2100, 0, 1900, 315)

    def lambda_9C14():
        OP_8E(0xFE, 0xFFFFE638, 0x0, 0x1900, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9C14)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x14, 0x2)
    OP_8C(0x14, 0, 500)
    Sleep(300)

    ChrTalk(    #235
        0x14,
        "#1460F#12PAre you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x15,
        "#104F#5PI'll live.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x15, 9)
    SetChrSubChip(0x15, 0)
    Sleep(500)
    OP_8C(0x15, 180, 400)
    Sleep(300)

    ChrTalk(    #237
        0x15,
        "#102F#5PWhat was Erika in such a hurry for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x14,
        (
            "#1461F#12PHahaha...\x02\x03",

            "Well, it's time...\x01",
            "for the testing to begin.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #239
        0x15,
        (
            "#104F#5PYou're not much less of an overprotective\x01",
            "parent than she is, I'll have you know...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_8CC8 end

    def Function_31_9DA7(): pass

    label("Function_31_9DA7")


    def lambda_9DAD():
        OP_96(0xFE, 0xFFFFE570, 0x0, 0x1DB0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9DAD)
    OP_43(0x15, 0x2, 0x0, 0x20)
    WaitChrThread(0x15, 0x1)
    OP_44(0x15, 0x2)
    OP_8C(0x15, 270, 0)
    SetChrChipByIndex(0x15, 21)
    SetChrSubChip(0x15, 0)
    Return()

    # Function_31_9DA7 end

    def Function_32_9DE7(): pass

    label("Function_32_9DE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E0F")
    OP_8C(0x15, 270, 1000)
    OP_8C(0x15, 0, 1000)
    OP_8C(0x15, 90, 1000)
    OP_8C(0x15, 180, 1000)
    Jump("Function_32_9DE7")

    label("loc_9E0F")

    Return()

    # Function_32_9DE7 end

    def Function_33_9E10(): pass

    label("Function_33_9E10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(8520, 0, 2460, 0)
    OP_67(0, 4140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -1300, 0, -3240, 0)
    SetChrPos(0x107, -9000, 0, 11940, 180)
    OP_72(0x12, 0x0)
    ExitThread()
    OP_72(0x412, 0x0)
    ExitThread()
    OP_72(0x13, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, 2400, 0, 2700, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x14, 0x3, 0x0, 0x22)

    def lambda_9EC5():
        OP_6D(-2820, 0, 740, 10000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_9EC5)

    def lambda_9EDD():
        OP_6C(24000, 10000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9EDD)

    def lambda_9EED():
        OP_67(0, 5100, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_9EED)

    def lambda_9F05():
        OP_6E(502, 10000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_9F05)
    OP_C8(0x200, 0x46, "C_PLAC40._CH", 0x1, 0xBB8)
    WaitChrThread(0x24, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(-7220, 0, 10500, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 2400, 0, 1000, 90)
    OP_0D()
    Sleep(300)
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_22(0x6D, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)

    def lambda_9FAC():
        OP_6D(-7220, 0, 9000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_9FAC)

    def lambda_9FC4():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x1C84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9FC4)
    WaitChrThread(0x107, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x107, 90, 500)
    Sleep(800)
    OP_8C(0x107, 220, 500)
    Sleep(800)
    OP_8C(0x107, 135, 500)
    Sleep(300)

    def lambda_A020():
        OP_6D(-800, 0, 3020, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_A020)

    def lambda_A038():
        OP_6C(70000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_A038)

    def lambda_A048():
        OP_8E(0xFE, 0xFFFFE8F4, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A048)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x14, 500)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #240
        0x107,
        "#560F#5PDad!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x107, 500)
    Sleep(300)

    ChrTalk(    #241
        0x14,
        (
            "#1463FTita?\x02\x03",

            "#1460FSorry--hold on a minute. I'll be right over.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 400)

    def lambda_A0F0():
        OP_8E(0xFE, 0x960, 0x0, 0xFFFFF31C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A0F0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x14, 0xFF)
    SetChrSubChip(0x14, 0)
    OP_6F(0x7, 0)
    OP_6D(600, 400, 1830, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x107, 0x1)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x107, -800, 400, 380, 270)
    SetChrChipByIndex(0x107, 38)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x14, 0x800)
    ClearChrFlags(0x14, 0x1)
    SetChrFlags(0x14, 0x4)
    SetChrPos(0x14, -700, 300, 1500, 270)
    SetChrChipByIndex(0x14, 39)
    SetChrSubChip(0x14, 0)
    Sleep(1000)

    def lambda_A1B7():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A1B7)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x107, 0x0)
    Sleep(500)

    ChrTalk(    #242
        0x14,
        (
            "#1465F#5PReally?\x02\x03",

            "So she wouldn't give you permission to join,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x107,
        (
            "#063F#12PNope...\x02\x03",

            "I understand what Mom's saying. I really do...\x02\x03",

            "#561FIt's just so frustrating not being able to do\x01",
            "anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x14,
        (
            "#1464F#5PWell, unlike your grandfather, your mother has\x01",
            "very clear reasons for what she does. \x02\x03",

            "She's an engineer with specific goals and ideals \x01",
            "over ones driven by emotion or curiosity.\x02\x03",

            "#1465FThat's especially true for this project, given that\x01",
            "the future of Liberl's national defense may end\x01",
            "up hinging on it.\x02\x03",

            "It was never going to be easy to win her over in\x01",
            "an argument about this, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x107,
        (
            "#063F#12P...\x02\x03",

            "#062FThat doesn't change the fact that I want to \x01",
            "confront Renne, though.\x02\x03",

            "Maybe what I'm saying is childish, I don't know.\x01",
            "But it's what I really feel, and I'm not budging!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x14, 1)
    Sleep(500)

    ChrTalk(    #246
        0x14,
        (
            "#1462F#5PThose are some bold words, Tita...\x02\x03",

            "#1462F(I don't think I've ever seen her look so serious\x01",
            "about anything before...)\x02\x03",

            "#1464FBut even if they're bold, I don't think they're childish.\x02\x03",

            "At the same time, I don't think it has anything to do\x01",
            "with whether you should be involved in developing\x01",
            "the Orbal Gear, either.\x02\x03",

            "#1464FHaving it isn't going to make confronting her any\x01",
            "easier.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x14)
    Sleep(500)

    ChrTalk(    #247
        0x14,
        (
            "#1462F#5P...Tita, confronting someone head on about \x01",
            "something is a very difficult thing to do.\x02\x03",

            "Probably more difficult than you realize.\x02\x03",

            "#1465FYou're certainly kind, but that's not always\x01",
            "going to be enough to change someone's\x01",
            "mind about something once it's made up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x107,
        "#063F#12PI know...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #249
        0x107,
        (
            "#562F#12P#40WMaybe I'm never going to be able to talk to\x01",
            "her like I want to in the end...\x02\x03",

            "Am I doomed to never do anything for her...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x14,
        (
            "#1462F#5P...\x02\x03",

            "#1462FYou backed down when you were arguing with\x01",
            "your mother earlier, right?\x02\x03",

            "That says to me that the convictions she has\x01",
            "are stronger than yours.\x02\x03",

            "#1464FYou already know that it's not going to be easy \x01",
            "to talk to Renne. If you want to succeed, you'll\x01",
            "need a stronger spirit than you've got now.\x02\x03",

            "Otherwise, you won't be able to really tell each\x01",
            "other how you really feel. You'll just back down\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x107,
        (
            "#561F#12PThat reminds me of something Agate said once,\x01",
            "actually.\x02\x03",

            "#062FHe said, 'Fighting's all about guts!'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x14,
        (
            "#1460F#5PW-Well, that's not quite what I'm talking about,\x01",
            "no...\x02\x03",

            "#1464F(I really am starting to worry about this Agate\x01",
            "fellow...)\x02\x03",

            "#1465FI think 'resolve' is a more appropriate word\x01",
            "here than 'guts.'\x02\x03",

            "You'll need to have the resolve to express all\x01",
            "of your honest feelings to her, plus you need\x01",
            "to accept hers in return.\x02\x03",

            "No doubt it'll be a lot easier said than done,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1500, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #253
        0x107,
        (
            "#063F#12PWell, I know she's from the society and that\x01",
            "Pater-Mater is too strong for me to compete\x01",
            "against as I am.\x02\x03",

            "#063FEspecially 'cause I don't have the kinda power\x01",
            "Estelle does...\x02\x03",

            "I'm not even confident she'll want to listen to\x01",
            "what I have to say, and even if she does, that\x01",
            "it'll have any effect on her...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #254
        0x107,
        (
            "#062F#12PBut I can't just leave her and do nothing!\x01",
            "I can't!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x107, 0x1)

    def lambda_ADED():
        OP_96(0xFE, 0xFFFFF8F8, 0x0, 0x17C, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_ADED)
    WaitChrThread(0x107, 0x1)
    ClearChrFlags(0x107, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_AE1A():
        OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x17C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AE1A)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 0, 400)
    Fade(500)
    SetChrSubChip(0x14, 0)
    SetChrPos(0x14, -800, 200, 1500, 270)
    SetChrPos(0x107, -4400, 0, 380, 90)
    OP_6D(-800, 0, 1500, 0)
    OP_67(0, 3740, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x13, -9330, 0, 8610, 135)

    def lambda_AEBB():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AEBB)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x14, 500)
    Sleep(500)

    def lambda_AEE7():
        OP_6B(3000, 20000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_AEE7)

    ChrTalk(    #255
        0x107,
        (
            "#062F#6PListen...\x02\x03",

            "She was part of Ouroboros, and she did some\x01",
            "pretty bad things, sure...\x02\x03",

            "...but that's not all there is. I spent some time with\x01",
            "her, I went shopping with her, I sat and talked with\x01",
            "her... So I know that's true.\x02\x03",

            "#563FDeep down, she's actually a sweet girl. I'm sure she\x01",
            "wasn't faking it, either. It's who she really is.\x02\x03",

            "She's not some kind of inhuman monster; she's an\x01",
            "ordinary girl who was like an excited little kid when\x01",
            "we found a cute pendant in a shop...\x02\x03",

            "#066F...and when I tripped and fell, she didn't hesitate\x01",
            "to hold out her hand for me.\x02\x03",

            "She's a good person, and I still think of her as my\x01",
            "friend even now.\x02\x03",

            "#561FBut after that, she went away from me. Ever since\x01",
            "then, her and Pater-Mater have always been out of\x01",
            "my reach...physically and emotionally.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #256
        0x107,
        (
            "#062F#6PMaybe the Orbal Gear will give me a chance to\x01",
            "change that.\x02\x03",

            "If I have that, I might finally be able to see a\x01",
            "little bit of the world that she does.\x02\x03",

            "Maybe she'll even be willing to open her heart--\x01",
            "even a little--and tell me how she really feels...\x01",
            "all while listening to my feelings, too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #257
        0x107,
        (
            "#566F#6PThat's why I want to be involved in making it,\x01",
            "and I won't take no for an answer!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(300)
    Fade(250)
    SetChrPos(0x14, -2300, 0, 1500, 270)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x1)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #258
        0x14,
        (
            "#1465F#5P(I'm so proud of how much you've grown...)\x02\x03",

            "#1464F...\x02\x03",

            "What do you think about all this, Erika?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x107,
        "#064F#6P...What?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)

    def lambda_B49E():
        OP_6D(-2800, 0, 4000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B49E)

    def lambda_B4B6():
        OP_8F(0xFE, 0xFFFFE214, 0x0, 0x1900, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B4B6)
    Sleep(500)

    def lambda_B4D6():

        label("loc_B4D6")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_B4D6")

    QueueWorkItem2(0x107, 2, lambda_B4D6)

    def lambda_B4E7():

        label("loc_B4E7")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_B4E7")

    QueueWorkItem2(0x14, 2, lambda_B4E7)
    WaitChrThread(0x24, 0x0)
    WaitChrThread(0x13, 0x1)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #260
        0x107,
        (
            "#065FM-Mom?!\x02\x03",

            "How long have you been listening in on us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x13,
        (
            "#1450FNot long. I only overheard the last part\x01",
            "of your conversation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B59D():
        OP_6D(-2000, 0, 3200, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_B59D)

    def lambda_B5B5():
        OP_67(0, 3800, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_B5B5)

    def lambda_B5CD():
        OP_6C(60000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_B5CD)

    def lambda_B5DD():
        OP_6B(2900, 2500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_B5DD)

    def lambda_B5ED():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_B5ED)

    def lambda_B5FD():
        OP_8E(0xFE, 0xFFFFEED0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B5FD)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)

    ChrTalk(    #262
        0x13,
        "#1452F#5PCan I ask you something, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x107,
        "#062F#12PO-Of course... What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x13,
        (
            "#1452F#5PIf you finally get to talk to this Renne girl\x01",
            "again, and it turns out she doesn't see you\x01",
            "as a friend...\x02\x03",

            "...what are you going to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(    #265
        0x107,
        (
            "#066F#12PExactly the same thing.\x02\x03",

            "I'll do exactly the same as I would otherwise.\x02\x03",

            "#563FBecause I've already made up my mind that I want\x01",
            "her to be a part of my life, even if she doesn't\x01",
            "want me to be a part of hers.\x02\x03",

            "I might not be able to chase her around and try\x01",
            "to convince her to come back to us like Estelle\x01",
            "can...\x02\x03",

            "...but I can still try to get to know more about\x01",
            "her and Pater-Mater, and I can make a stronger\x01",
            "connection with her through the Orbal Gear.\x02\x03",

            "#560FThere's nothing stopping me doing any of those\x01",
            "things, right?\x02\x03",

            "Whatever makes it so I can be a part of her life,\x01",
            "I want it to do it. Even if it's small. \x02\x03",

            "#062FBecause that's what friends do.\x01",
            "That's how I really feel.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #266
        0x13,
        (
            "#1457F#5P...I see.\x02\x03",

            "Well, I can't help but feel like you're being a\x01",
            "little naive...but you got me.\x02\x03",

            "#1450FI'll accept all you've said as a sufficient reason\x01",
            "for participating in the Orbal Gear Project.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #267
        0x107,
        "#064F#12PReally?!\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x75)
    OP_8C(0x13, 280, 400)
    Sleep(300)

    ChrTalk(    #268
        0x13,
        (
            "#1458F#5PReally! Now, what're you two waiting for? \x01",
            "We've got work to do!\x02\x03",

            "#1834FDan! I've redone the blueprints, so I need you\x01",
            "to go over them!\x02\x03",

            "Tita! We're going to start making the quartz \x01",
            "prototypes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x107,
        (
            "#560F#12PSo I can be a part of the development?\x02\x03",

            "You promise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x13,
        (
            "#1458F#5P...Haha. We'll see how long that happy face of\x01",
            "yours lasts.\x02\x03",

            "#1456FNow that you're on the team, I'm going to be\x01",
            "working you to the bone. I hope you're ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x107,
        (
            "#067F#12PY-Yeah...\x02\x03",

            "Bring it on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x14,
        "#1461F#11PGood! Are you ready to get started?\x02",
    )

    CloseMessageWindow()

    def lambda_BD2D():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_BD2D)
    OP_8C(0x13, 280, 600)

    def lambda_BD44():
        OP_8E(0xFE, 0xFFFFDC74, 0x0, 0x1630, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BD44)
    Sleep(150)
    OP_44(0x107, 0x2)

    def lambda_BD68():
        OP_8E(0xFE, 0xFFFFDBD4, 0x0, 0x11F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BD68)
    Sleep(200)
    OP_44(0x14, 0x2)

    def lambda_BD8C():
        OP_8E(0xFE, 0xFFFFDD3C, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BD8C)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x24, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #273
        (
            "\x07\x00#40WThanks to her efforts, Tita was finally allowed to\x01",
            "participate in the Orbal Gear's development.\x02\x03",

            "The familiar central factory was filled with a new\x01",
            "sense of tension as it became the building ground\x01",
            "for the new invention.\x02\x03",

            "Tita was able to work as a full-fledged engineer\x01",
            "equal to the adults around her for the first time.\x02\x03",

            "She was also treated no differently than anyone\x01",
            "else, meaning that Erika's demands were constant\x01",
            "and relentless...\x02\x03",

            "...but that was a source of true happiness for Tita.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #274
        "\x07\x00Finally, two weeks later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_9E10 end

    def Function_34_C00F(): pass

    label("Function_34_C00F")


    def lambda_C015():
        OP_8E(0xFE, 0x960, 0x0, 0xFFFFF358, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C015)
    WaitChrThread(0x14, 0x1)

    def lambda_C035():
        OP_8E(0xFE, 0x960, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C035)
    WaitChrThread(0x14, 0x1)

    def lambda_C055():
        OP_8E(0xFE, 0xCE4, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C055)
    WaitChrThread(0x14, 0x1)
    Sleep(2000)
    OP_8C(0x14, 315, 400)

    def lambda_C081():
        OP_8E(0xFE, 0x960, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C081)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 0, 400)
    Sleep(2000)

    def lambda_C0AD():
        OP_8F(0xFE, 0x960, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C0AD)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 90, 400)

    def lambda_C0D4():
        OP_8E(0xFE, 0xCE4, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C0D4)
    WaitChrThread(0x14, 0x1)
    Return()

    # Function_34_C00F end

    def Function_35_C0EF(): pass

    label("Function_35_C0EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x15, -9000, 0, 11940, 180)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 3200, 0, 1000, 90)
    SetChrPos(0x10, 7000, 800, 61000, 270)
    SetChrFlags(0x10, 0x2000)
    SetChrPos(0x14, -1700, 0, 160, 0)
    SetChrPos(0x107, -2100, 0, 1680, 90)
    SetChrChipByIndex(0x107, 36)
    SetChrSubChip(0x107, 0)
    OP_72(0x13, 0x0)
    ExitThread()
    OP_72(0x413, 0x0)
    ExitThread()
    OP_A1(0x18, 0x8)
    SetChrPos(0x18, -3100, 0, 6500, 0)
    OP_6D(8800, 0, 61000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0xF0, 0x0, 0x64)
    OP_6D(8680, 0, 62620, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_6D(8480, 0, 59120, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    Sleep(300)
    FadeToBright(0, 0)
    OP_22(0xF0, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_6D(9400, 0, 61000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(300)
    FadeToBright(0, 0)
    OP_22(0xF0, 0x0, 0x64)
    Sleep(1600)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(2000)
    ClearChrFlags(0x10, 0x2000)
    SetChrPos(0x10, 7000, 800, 1000, 270)
    OP_6D(9400, 0, 1000, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_C37A():
        OP_6D(7400, 0, 1000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C37A)

    def lambda_C392():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C392)

    def lambda_C3AA():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_C3AA)

    def lambda_C3BA():
        OP_6E(268, 3000)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_C3BA)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #275
        0x13,
        "#1456F#4S#300WAaaaaall done.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(500)
    OP_8C(0x13, 270, 500)
    Sleep(300)

    ChrTalk(    #276
        0x13,
        "#1455F#5PAll right! Time to begin our activation test!\x02",
    )

    CloseMessageWindow()

    def lambda_C446():
        OP_6D(1200, 0, 1840, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C446)

    def lambda_C45E():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C45E)
    WaitChrThread(0x24, 0x0)
    OP_8C(0x14, 90, 400)
    Sleep(300)

    ChrTalk(    #277
        0x14,
        (
            "#1464F#6PI-I think we could probably do with a little\x01",
            "break...\x02\x03",

            "#1465FWe've been working almost constantly for\x01",
            "three whole days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x107,
        (
            "#562F#6PH-How do you still have so much energy,\x01",
            "Mom?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C543():
        OP_6D(440, 0, 2410, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C543)

    def lambda_C55B():
        OP_67(0, 5210, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_C55B)

    def lambda_C573():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_C573)

    def lambda_C583():
        OP_8E(0xFE, 0x168, 0x0, 0x3E8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C583)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #279
        0x13,
        (
            "#1459F#11PAnd how do you two have so little?!\x01",
            "Pull yourselves together, people!\x02\x03",

            "The best part of developing something new\x01",
            "is about to begin!\x02\x03",

            "#1455FThat goes for you especially, Tita!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)
    Sleep(150)

    ChrTalk(    #280
        0x107,
        "#065F#6PM-Me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x13,
        (
            "#1456F#11PThe seat in our prototype here is on the small\x01",
            "side, so there's no way anyone other than you\x01",
            "is going to be able to sit in it.\x02\x03",

            "So you're going to need to be part of our tests\x01",
            "until the very end!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x107,
        (
            "#063F#6PI-I know...\x02\x03",

            "#561FBut please, let me have some sleep first...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 0)
    Sleep(500)
    OP_62(0x107, 0x64, 1500, 0x1C, 0x21, 0x12C, 0x0)
    Sleep(2500)

    def lambda_C7C8():
        OP_6D(-140, 0, 2470, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_C7C8)

    def lambda_C7E0():

        label("loc_C7E0")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_C7E0")

    QueueWorkItem2(0x14, 2, lambda_C7E0)
    Sleep(500)

    def lambda_C7F6():
        OP_8F(0xFE, 0xFFFFFD08, 0x0, 0x690, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C7F6)
    WaitChrThread(0x13, 0x1)
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)
    WaitChrThread(0x24, 0x0)

    ChrTalk(    #283
        0x13,
        (
            "#1833F#11PWell, okay. Only because you said, 'please.'\x02\x03",

            "It's better than trying to do the tests today\x01",
            "when you're in this state and ending up with\x01",
            "a bunch of mistakes being made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x14,
        (
            "#1460F#12PShe's done very well in my opinion.\x02\x03",

            "Not even most veteran engineers can keep up\x01",
            "with your working pace. I'm amazed our little\x01",
            "daughter did it on her first project.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 225, 400)
    Sleep(300)

    ChrTalk(    #285
        0x13,
        (
            "#1832F#5PWhat, exactly, are you implying?\x02\x03",

            "That I'm some kind of machine with limitless\x01",
            "stamina? \x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 90, 500)
    Sleep(300)
    OP_22(0x12, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #286
        0x13,
        (
            "#1458F#5POkay...\x02\x03",

            "So that's the activation tests penciled\x01",
            "in for Friday the 28th...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107)
    Sleep(300)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x64, 1500, 0x2, 0x7, 0xC8, 0x1)
    Sleep(300)
    OP_95(0x107, 0x0, 0x12C, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #287
        0x107,
        "#561F#6PMmm...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x107, 1)
    Sleep(300)

    ChrTalk(    #288
        0x107,
        "#560F#6PW-Wait! Tomorrow's Friday?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x107, 500)
    Sleep(300)

    ChrTalk(    #289
        0x13,
        "#1454F#11PY-Yes, it is... Why do you ask?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_0D()

    ChrTalk(    #290
        0x107,
        "#067F#6PI need to start cooking, then!\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_CBB6():

        label("loc_CBB6")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_CBB6")

    QueueWorkItem2(0x13, 2, lambda_CBB6)
    OP_8C(0x107, 315, 500)

    def lambda_CBCE():
        OP_8E(0xFE, 0xFFFFE6B0, 0x0, 0x17D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CBCE)
    Sleep(1000)
    Fade(1000)
    OP_44(0x107, 0x1)
    SetChrPos(0x107, -2000, 0, 1680, 315)
    OP_6D(-8000, 0, 9000, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(14000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_22(0xE, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x7)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, -1500, 0, 980, 300)
    SetChrPos(0x14, -2420, 0, -160, 300)

    def lambda_CCA8():
        OP_6D(-6500, 0, 8020, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_CCA8)
    OP_43(0x15, 0x3, 0x0, 0x25)
    Sleep(500)

    ChrTalk(    #291 op#A op#5
        0x15,
        (
            "#100F#1P#35A#5PI finished running all of the necessary\x01",
            "simulations using the Capel.\x02\x03\x05",

            "#40AIt should be able to perform to roughly\x01",
            "the intended specifications, but...\x02\x03\x05",

            "#103F#30ATita! What's the rush?\x05\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 0x3)
    WaitChrThread(0x107, 0x1)
    Sleep(300)

    ChrTalk(    #292
        0x107,
        (
            "#061F#12PGrandpa!\x02\x03",

            "I just realized tomorrow's the last Friday\x01",
            "of the month!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x15,
        (
            "#101F#5PAhh, yes.\x02\x03",

            "That's when Agate's coming, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x107,
        (
            "#067F#12PYeah! I need to start getting things\x01",
            "ready for tomorrow's food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x15,
        "#104F#5PWell, if you're taking requests, I...\x02",
    )

    CloseMessageWindow()
    OP_22(0xF0, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    OP_1F(0x0, 0x0)
    Sleep(2000)

    def lambda_CECF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CECF)

    def lambda_CEE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_CEE1)

    def lambda_CEF3():
        OP_6D(-3240, 0, 3740, 3000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_CEF3)

    def lambda_CF0B():
        OP_67(0, 4500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_CF0B)

    def lambda_CF23():
        OP_6C(352000, 3000)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_CF23)
    Sleep(3000)
    Sleep(1000)

    ChrTalk(    #296
        0x13,
        "#1451F#12P...Agate?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_C4(0x1, 0x400)
    OP_0D()
    Sleep(1000)
    OP_1F(0x64, 0xBB8)

    def lambda_CF6D():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_CF6D)
    Sleep(1000)

    ChrTalk(    #297
        0x14,
        (
            "#1463F#12PI'm not sure I follow...\x02\x03",

            "What's special about the last Friday\x01",
            "of the month?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x2)
    OP_44(0x14, 0x2)

    def lambda_CFF0():
        OP_6D(-5600, 0, 6920, 2000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_CFF0)

    def lambda_D008():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_D008)

    def lambda_D018():
        OP_8E(0xFE, 0xFFFFEE08, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D018)
    Sleep(400)

    def lambda_D038():
        OP_8E(0xFE, 0xFFFFEB60, 0x0, 0xCBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_D038)
    Sleep(500)
    TurnDirection(0x107, 0x13, 500)
    WaitChrThread(0x14, 0x1)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #298
        0x107,
        (
            "#064F#5PWhoops. I forgot to tell you.\x02\x03",

            "This is going to be your first time meeting\x01",
            "Agate, isn't it?\x02\x03",

            "#061FHeehee. You see, he comes over here to visit\x01",
            "once a month, and tomorrow's that day.\x02\x03",

            "So...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x13, 0x0, 0x0, 0x24)

    ChrTalk(    #299
        0x13,
        (
            "#1451F#12P#130WOh, so our  d e a r  f r i e n d  Agate is visiting,\x01",
            "is he? #20W\x02\x03",

            "Heh. Heheh. What a coincidence that he should\x01",
            "choose the day of our tests to make his arrival.\x02\x03",

            "#1831FHe sure is a LUCKY man!\x01",
            "#3SAhahahaha!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x13, 0x0)

    ChrTalk(    #300
        0x107,
        (
            "#064F#5PUmm...\x02\x03",

            "Mom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x14,
        "#1465F#6PWell, you see, Tita...your mother... Umm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 45, 400)

    def lambda_D295():
        OP_6D(-5000, 0, 7300, 2500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_D295)

    def lambda_D2AD():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_D2AD)

    def lambda_D2BD():
        OP_8E(0xFE, 0xFFFFF1B4, 0x0, 0x1694, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D2BD)

    def lambda_D2D8():

        label("loc_D2D8")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_D2D8")

    QueueWorkItem2(0x107, 2, lambda_D2D8)

    def lambda_D2E9():

        label("loc_D2E9")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_D2E9")

    QueueWorkItem2(0x15, 2, lambda_D2E9)
    Sleep(500)

    def lambda_D2FF():

        label("loc_D2FF")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_D2FF")

    QueueWorkItem2(0x14, 2, lambda_D2FF)
    WaitChrThread(0x13, 0x1)
    OP_44(0x107, 0x2)
    OP_44(0x15, 0x2)

    def lambda_D31D():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_D31D)
    Sleep(300)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x13)
    Sleep(500)

    def lambda_D34F():
        OP_8F(0xFE, 0xFFFFEFFC, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D34F)
    WaitChrThread(0x13, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D378():
        OP_6B(2900, 100)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_D378)

    def lambda_D388():
        OP_8F(0xFE, 0xFFFFF1B4, 0x0, 0x1694, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D388)
    WaitChrThread(0x13, 0x1)
    OP_22(0x154, 0x0, 0x64)
    OP_22(0x11A, 0x0, 0x64)
    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    OP_70(0x8, 0x3C)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(70)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #302
        0x13,
        "#1458F#5P...Dan, darling? I just had a brilliant idea.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    ChrTalk(    #303
        0x13,
        (
            "#1451F#11PI've decided that tomorrow's tests are going\x01",
            "to require a sacrifice.\x02\x03",

            "Heheheh... We can't just let any old person\x01",
            "come over to our house for no good reason,\x01",
            "right?\x02\x03",

            "They need to make a contribution to the family.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 500)
    Sleep(300)

    ChrTalk(    #304
        0x13,
        "#1835F#2P#3SI hope you're ready, Agate Crosner!#2S\x02",
    )

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(2820, 0)
    Sleep(500)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x107, 0x2)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 90, 500)
    Sleep(300)

    ChrTalk(    #305
        0x107,
        "#065F#5PU-Umm... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x14,
        (
            "#1463F#6PS-So let me get this straight...\x02\x03",

            "You're saying you want Agate to help with\x01",
            "the tests, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x15,
        (
            "#104FI'm not sure I'd recommend that, Erika.\x02\x03",

            "He's a useless dolt where technology's\x01",
            "concerned.\x02\x03",

            "I can't see him being much help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x13,
        (
            "#1458F#11PHelp?\x02\x03",

            "Oh, I'm expecting a lot more than that from\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D748():
        OP_6D(-3900, 0, 7600, 1500)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_D748)

    def lambda_D760():
        OP_67(0, 4550, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_D760)

    def lambda_D778():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_D778)

    def lambda_D788():
        OP_6C(35000, 1500)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_D788)
    TurnDirection(0x13, 0x107, 500)
    WaitChrThread(0x24, 0x0)
    Sleep(300)

    ChrTalk(    #309
        0x13,
        (
            "#1834F#11P#3SI'm expecting him to offer his very life in the\x01",
            "name of science!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #310
        0x107,
        "#065F#3S#6PWhaaat?!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #311
        0x14,
        (
            "#1461F#6PA-Ahaha... Come on, now, Erika. This is no time\x01",
            "for being silly.\x02\x03",

            "#1465FI'm not opposed to having him help out, though.\x02\x03",

            "I'd like the chance to have a good, long talk with\x01",
            "him myself.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 135, 500)
    Sleep(300)

    ChrTalk(    #312
        0x107,
        "#065F#5PY-You, too, Dad?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x13,
        (
            "#1458F#11PWell, it's settled.\x02\x03",

            "Today's going to be a good day...\x01",
            "A very, very good day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x107,
        "#065F#5PUhh... Umm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 90, 500)
    Sleep(600)
    OP_8C(0x107, 135, 500)
    Sleep(600)
    OP_8C(0x107, 90, 500)
    Sleep(300)

    ChrTalk(    #315
        0x107,
        (
            "#065F#6P(I-Is it just me...)\x02\x03",

            "(...or do they seem to have Agate all wrong?)\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)

    def lambda_DA37():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_DA37)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0xA, 0x1, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #316
        "\x07\x00Side Story [Orbal Gear Project Part 1] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB37")
    Sleep(1000)
    OP_28(0x1, 0x4, 0x10)
    OP_28(0x1, 0x4, 0x20)
    OP_3E(0x153, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #317
        "\x07\x05Received \x1F\x53\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #318
        "\x07\x05Received \x07\x023,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_DB37")

    OP_C2(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_35_C0EF end

    def Function_36_DB47(): pass

    label("Function_36_DB47")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB83")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_36_DB47")

    label("loc_DB83")

    Return()

    # Function_36_DB47 end

    def Function_37_DB84(): pass

    label("Function_37_DB84")


    def lambda_DB8A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_DB8A)

    def lambda_DB9C():
        OP_8E(0xFE, 0xFFFFDCD8, 0x0, 0x2198, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DB9C)
    WaitChrThread(0x15, 0x1)
    OP_6F(0x7, 30)
    OP_70(0x7, 0x0)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_DBCF():
        OP_8E(0xFE, 0xFFFFE304, 0x0, 0x1B6C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_DBCF)
    WaitChrThread(0x15, 0x1)

    def lambda_DBEF():
        OP_8E(0xFE, 0xFFFFE6B0, 0x0, 0x17D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_DBEF)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Return()

    # Function_37_DB84 end

    def Function_38_DC10(): pass

    label("Function_38_DC10")

    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_DC2F():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DC2F)

    def lambda_DC4A():

        label("loc_DC4A")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DC4A")

    QueueWorkItem2(0xFE, 3, lambda_DC4A)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_38_DC10 end

    def Function_39_DC67(): pass

    label("Function_39_DC67")

    SetChrChipByIndex(0x12, 2)
    SetChrFlags(0xFE, 0x2)

    def lambda_DC77():

        label("loc_DC77")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_DC77")

    QueueWorkItem2(0xFE, 2, lambda_DC77)

    def lambda_DC8A():

        label("loc_DC8A")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DC8A")

    QueueWorkItem2(0xFE, 3, lambda_DC8A)
    OP_22(0xED, 0x0, 0x64)

    def lambda_DCAC():
        OP_8F(0xFE, 0xFFFFF362, 0x320, 0x244, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DCAC)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x2)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_DCDF():

        label("loc_DCDF")

        OP_99(0xFE, 0x0, 0x5, 0x9C4)
        OP_48()
        Jump("loc_DCDF")

    QueueWorkItem2(0x12, 3, lambda_DCDF)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_39_DC67 end

    def Function_40_DCF4(): pass

    label("Function_40_DCF4")

    OP_44(0xFE, 0x3)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_DD0A():
        OP_96(0xFE, 0x56E, 0x0, 0xDD4, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD0A)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_DD52():
        OP_96(0xFE, 0x1432, 0x0, 0x65E, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD52)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x1AA4, 0x0, 0x316, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_40_DCF4 end

    def Function_41_DDA7(): pass

    label("Function_41_DDA7")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_DDCA():
        OP_8F(0xFE, 0xFFFFF33A, 0x320, 0x2094, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DDCA)

    def lambda_DDE5():

        label("loc_DDE5")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DDE5")

    QueueWorkItem2(0xFE, 3, lambda_DDE5)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_7C(0x190, 0x190, 0xBB8, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 0)
    OP_70(0x8, 0x3C)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x2009, 0x0)
    ExitThread()
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Return()

    # Function_41_DDA7 end

    def Function_42_DE66(): pass

    label("Function_42_DE66")

    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_DE85():
        OP_91(0xFE, 0x3E8, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DE85)

    def lambda_DEA0():

        label("loc_DEA0")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DEA0")

    QueueWorkItem2(0xFE, 3, lambda_DEA0)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x2)

    def lambda_DECC():

        label("loc_DECC")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_DECC")

    QueueWorkItem2(0xFE, 2, lambda_DECC)

    def lambda_DEDF():

        label("loc_DEDF")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DEDF")

    QueueWorkItem2(0xFE, 3, lambda_DEDF)
    OP_22(0xED, 0x0, 0x64)
    OP_97(0xFE, 0xFFFFF600, 0x4E2, 0xFFFE7960, 0x1388, 0x1)
    OP_44(0x12, 0x2)
    ClearChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)

    def lambda_DF29():

        label("loc_DF29")

        OP_99(0xFE, 0x0, 0x5, 0x9C4)
        OP_48()
        Jump("loc_DF29")

    QueueWorkItem2(0x12, 3, lambda_DF29)
    OP_8C(0xFE, 0, 500)
    Return()

    # Function_42_DE66 end

    def Function_43_DF3E(): pass

    label("Function_43_DF3E")

    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 180, 0)

    def lambda_DF50():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xEF6, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF50)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_43_DF3E end

    def Function_44_DF8E(): pass

    label("Function_44_DF8E")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_DFB1():
        OP_8F(0xFE, 0xFFFFE1B0, 0x320, 0x5C8, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DFB1)

    def lambda_DFCC():

        label("loc_DFCC")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_DFCC")

    QueueWorkItem2(0xFE, 3, lambda_DFCC)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_8C(0xFE, 270, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    OP_7C(0x190, 0x190, 0xBB8, 0x64)
    OP_22(0x1FE, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x64)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3C)
    OP_72(0x100C, 0x0)
    ExitThread()
    OP_72(0x200C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Return()

    # Function_44_DF8E end

    def Function_45_E067(): pass

    label("Function_45_E067")

    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x64, 0x0, 0x114E, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_E090():
        OP_96(0xFE, 0xFFFFF5F6, 0x0, 0x3D4, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E090)

    def lambda_E0AE():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E0AE)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)

    def lambda_E0C6():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_E0C6)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_45_E067 end

    def Function_46_E0FA(): pass

    label("Function_46_E0FA")

    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFFF9C, 0x0, 0x11A8, 0x1B58, 0x0)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_E123():
        OP_96(0xFE, 0xFFFFF786, 0x0, 0x690, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E123)

    def lambda_E141():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E141)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_E172():
        OP_96(0xFE, 0xFFFFFE48, 0x0, 0xFFFFFA38, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E172)

    def lambda_E190():
        OP_8C(0xFE, 45, 200)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E190)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_E0FA end

    def Function_47_E1CC(): pass

    label("Function_47_E1CC")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    ClearChrFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xFFFFF8A8, 0x0, 0x168A, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x20)
    OP_8C(0xFE, 135, 400)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_47_E1CC end

    def Function_48_E21C(): pass

    label("Function_48_E21C")

    OP_22(0x35A, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x35A)
    Return()

    # Function_48_E21C end

    def Function_49_E22A(): pass

    label("Function_49_E22A")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_E24D():
        OP_91(0xFE, 0xBB8, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E24D)

    def lambda_E268():

        label("loc_E268")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_E268")

    QueueWorkItem2(0xFE, 3, lambda_E268)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    Return()

    # Function_49_E22A end

    def Function_50_E289(): pass

    label("Function_50_E289")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_E294():
        OP_96(0xFE, 0xFFFFF0B0, 0x0, 0x802, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E294)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_50_E289 end

    def Function_51_E2CB(): pass

    label("Function_51_E2CB")

    SetChrFlags(0x12, 0x800)

    def lambda_E2D6():
        OP_91(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E2D6)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    OP_23(0x1A0)
    SetChrChipByIndex(0x12, 3)
    SetChrSubChip(0x12, 0)

    def lambda_E307():
        OP_99(0xFE, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_E307)
    Sleep(200)
    OP_22(0xEE, 0x0, 0x64)
    WaitChrThread(0x12, 0x2)
    Return()

    # Function_51_E2CB end

    def Function_52_E321(): pass

    label("Function_52_E321")

    OP_44(0x12, 0x3)
    SetChrFlags(0x12, 0x1000)
    OP_22(0xED, 0x0, 0x64)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0x12, 0x20)

    def lambda_E344():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E344)

    def lambda_E35F():

        label("loc_E35F")

        OP_9E(0xFE, 0x0, 0x1E, 0x12C, 0x1F40)
        OP_48()
        Jump("loc_E35F")

    QueueWorkItem2(0xFE, 3, lambda_E35F)
    WaitChrThread(0x12, 0x1)
    OP_44(0x12, 0x3)
    Return()

    # Function_52_E321 end

    def Function_53_E380(): pass

    label("Function_53_E380")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 16)
    OP_8F(0xFE, 0xFFFFF844, 0x0, 0x3F2, 0xFA0, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_53_E380 end

    def Function_54_E3B3(): pass

    label("Function_54_E3B3")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_E3BE():
        OP_96(0xFE, 0xFFFFF254, 0x0, 0x3F2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E3BE)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_54_E3B3 end

    def Function_55_E3F5(): pass

    label("Function_55_E3F5")

    OP_22(0xCB, 0x0, 0x64)

    def lambda_E400():
        OP_96(0xFE, 0xFFFFF844, 0x0, 0x3F2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E400)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_55_E3F5 end

    def Function_56_E43C(): pass

    label("Function_56_E43C")

    OP_22(0x92, 0x0, 0x64)
    OP_9E(0xFE, 0xF, 0x0, 0x7D0, 0x2710)
    OP_23(0x92)
    OP_22(0x9D, 0x0, 0x64)

    def lambda_E462():

        label("loc_E462")

        OP_99(0xFE, 0x0, 0x5, 0x5DC)
        OP_48()
        Jump("loc_E462")

    QueueWorkItem2(0xFE, 3, lambda_E462)
    Return()

    # Function_56_E43C end

    def Function_57_E470(): pass

    label("Function_57_E470")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x2436, 0x0, 0xFFFFFB96, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A70, 0x0, 0x1086, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A84, 0x0, 0x22A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3142, 0x0, 0x21E8, 0xBB8, 0x0)
    SetChrPos(0xFE, 14300, 4000, 760, 270)
    Return()

    # Function_57_E470 end

    def Function_58_E4D9(): pass

    label("Function_58_E4D9")

    Sleep(300)
    OP_8C(0xFE, 45, 400)
    OP_8E(0xFE, 0x1022, 0x0, 0xE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3976, 0x0, 0xDA2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3A84, 0x0, 0x22A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3142, 0x0, 0x21E8, 0xBB8, 0x0)
    SetChrPos(0xFE, 15380, 4000, 2130, 270)
    Return()

    # Function_58_E4D9 end

    def Function_59_E547(): pass

    label("Function_59_E547")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -8990, 0, 11860, 180)
    OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x25BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDA4E, 0x0, 0x20EE, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_59_E547 end

    def Function_60_E58D(): pass

    label("Function_60_E58D")

    Sleep(600)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    SetChrPos(0xFE, -8990, 0, 11860, 180)
    OP_8E(0xFE, 0xFFFFDD64, 0x0, 0x25BC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDF6C, 0x0, 0x1FD6, 0x7D0, 0x0)
    Return()

    # Function_60_E58D end

    def Function_61_E5DB(): pass

    label("Function_61_E5DB")

    OP_8E(0xFE, 0xC76, 0x0, 0x6FE, 0x1388, 0x0)
    Return()

    # Function_61_E5DB end

    def Function_62_E5F0(): pass

    label("Function_62_E5F0")

    Sleep(400)
    OP_8E(0xFE, 0xF46, 0x0, 0x410, 0x1388, 0x0)
    Return()

    # Function_62_E5F0 end

    def Function_63_E60A(): pass

    label("Function_63_E60A")

    Sleep(400)
    Sleep(400)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFF56, 0x1388, 0x0)
    Return()

    # Function_63_E60A end

    def Function_64_E629(): pass

    label("Function_64_E629")

    Sleep(400)
    Sleep(400)
    Sleep(400)
    OP_8E(0xFE, 0x1536, 0x0, 0x3AC, 0x1388, 0x0)
    Return()

    # Function_64_E629 end

    SaveToFile()

Try(main)

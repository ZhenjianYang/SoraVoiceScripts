from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4303.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        'Scherazard',                           # 9
        'Olivier',                              # 10
        'Kloe',                                 # 11
        'Agate',                                # 12
        'Tita',                                 # 13
        'Zin',                                  # 14
        'Professor Russell',                    # 15
        'Sieg',                                 # 16
        'Colonel Richard',                      # 17
        'Cassius',                              # 18
        'Mecha',                                # 19
        'Mecha',                                # 20
        'Mecha',                                # 21
        'Mecha',                                # 22
        ' ',                                    # 23
        ' ',                                    # 24
        ' ',                                    # 25
        ' ',                                    # 26
        ' ',                                    # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
        ' ',                                    # 32
        ' ',                                    # 33
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
        'ED6_DT07/CH00040 ._CH',             # 02
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT07/CH00273 ._CH',             # 07
        'ED6_DT07/CH00271 ._CH',             # 08
        'ED6_DT07/CH02000 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH00101 ._CH',             # 0B
        'ED6_DT07/CH00110 ._CH',             # 0C
        'ED6_DT07/CH00111 ._CH',             # 0D
        'ED6_DT07/CH00120 ._CH',             # 0E
        'ED6_DT07/CH00121 ._CH',             # 0F
        'ED6_DT07/CH00130 ._CH',             # 10
        'ED6_DT07/CH00131 ._CH',             # 11
        'ED6_DT07/CH00140 ._CH',             # 12
        'ED6_DT07/CH00141 ._CH',             # 13
        'ED6_DT07/CH00150 ._CH',             # 14
        'ED6_DT07/CH00151 ._CH',             # 15
        'ED6_DT07/CH00160 ._CH',             # 16
        'ED6_DT07/CH00161 ._CH',             # 17
        'ED6_DT07/CH00170 ._CH',             # 18
        'ED6_DT07/CH00171 ._CH',             # 19
        'ED6_DT09/CH11002 ._CH',             # 1A
        'ED6_DT09/CH11000 ._CH',             # 1B
        'ED6_DT07/CH00272 ._CH',             # 1C
        'ED6_DT07/CH00274 ._CH',             # 1D
        'ED6_DT06/CH20021 ._CH',             # 1E
        'ED6_DT06/CH20027 ._CH',             # 1F
        'ED6_DT06/CH20028 ._CH',             # 20
        'ED6_DT06/CH20029 ._CH',             # 21
        'ED6_DT06/CH20084 ._CH',             # 22
        'ED6_DT06/CH20077 ._CH',             # 23
        'ED6_DT07/CH02030 ._CH',             # 24
        'ED6_DT07/CH00104 ._CH',             # 25
        'ED6_DT07/CH00114 ._CH',             # 26
        'ED6_DT07/CH00124 ._CH',             # 27
        'ED6_DT07/CH00134 ._CH',             # 28
        'ED6_DT07/CH00144 ._CH',             # 29
        'ED6_DT07/CH00154 ._CH',             # 2A
        'ED6_DT07/CH00164 ._CH',             # 2B
        'ED6_DT07/CH00174 ._CH',             # 2C
        'ED6_DT06/CH20046 ._CH',             # 2D
        'ED6_DT07/CH00270 ._CH',             # 2E
    )

    AddCharChipPat(
        'ED6_DT07/CH00020P._CP',             # 00
        'ED6_DT07/CH00030P._CP',             # 01
        'ED6_DT07/CH00040P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT07/CH00273P._CP',             # 07
        'ED6_DT07/CH00271P._CP',             # 08
        'ED6_DT07/CH02000P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH00101P._CP',             # 0B
        'ED6_DT07/CH00110P._CP',             # 0C
        'ED6_DT07/CH00111P._CP',             # 0D
        'ED6_DT07/CH00120P._CP',             # 0E
        'ED6_DT07/CH00121P._CP',             # 0F
        'ED6_DT07/CH00130P._CP',             # 10
        'ED6_DT07/CH00131P._CP',             # 11
        'ED6_DT07/CH00140P._CP',             # 12
        'ED6_DT07/CH00141P._CP',             # 13
        'ED6_DT07/CH00150P._CP',             # 14
        'ED6_DT07/CH00151P._CP',             # 15
        'ED6_DT07/CH00160P._CP',             # 16
        'ED6_DT07/CH00161P._CP',             # 17
        'ED6_DT07/CH00170P._CP',             # 18
        'ED6_DT07/CH00171P._CP',             # 19
        'ED6_DT09/CH11002P._CP',             # 1A
        'ED6_DT09/CH11000P._CP',             # 1B
        'ED6_DT07/CH00272P._CP',             # 1C
        'ED6_DT07/CH00274P._CP',             # 1D
        'ED6_DT06/CH20021P._CP',             # 1E
        'ED6_DT06/CH20027P._CP',             # 1F
        'ED6_DT06/CH20028P._CP',             # 20
        'ED6_DT06/CH20029P._CP',             # 21
        'ED6_DT06/CH20084P._CP',             # 22
        'ED6_DT06/CH20077P._CP',             # 23
        'ED6_DT07/CH02030P._CP',             # 24
        'ED6_DT07/CH00104P._CP',             # 25
        'ED6_DT07/CH00114P._CP',             # 26
        'ED6_DT07/CH00124P._CP',             # 27
        'ED6_DT07/CH00134P._CP',             # 28
        'ED6_DT07/CH00144P._CP',             # 29
        'ED6_DT07/CH00154P._CP',             # 2A
        'ED6_DT07/CH00164P._CP',             # 2B
        'ED6_DT07/CH00174P._CP',             # 2C
        'ED6_DT06/CH20046P._CP',             # 2D
        'ED6_DT07/CH00270P._CP',             # 2E
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
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
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1250,
        Y                   = 19300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 917534,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_586",          # 00, 0
        "Function_1_5C0",          # 01, 1
        "Function_2_622",          # 02, 2
        "Function_3_708",          # 03, 3
        "Function_4_2A74",         # 04, 4
        "Function_5_31A8",         # 05, 5
        "Function_6_31DF",         # 06, 6
        "Function_7_44D5",         # 07, 7
        "Function_8_4639",         # 08, 8
        "Function_9_4CE9",         # 09, 9
        "Function_10_9BD5",        # 0A, 10
        "Function_11_9CE5",        # 0B, 11
        "Function_12_9D32",        # 0C, 12
        "Function_13_9D7E",        # 0D, 13
        "Function_14_9DA6",        # 0E, 14
        "Function_15_9E10",        # 0F, 15
        "Function_16_9E42",        # 10, 16
        "Function_17_9E6A",        # 11, 17
        "Function_18_9F47",        # 12, 18
        "Function_19_A008",        # 13, 19
        "Function_20_A06B",        # 14, 20
        "Function_21_A0D6",        # 15, 21
        "Function_22_A187",        # 16, 22
        "Function_23_A1FB",        # 17, 23
        "Function_24_A27D",        # 18, 24
        "Function_25_A2AF",        # 19, 25
    )


    def Function_0_586(): pass

    label("Function_0_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_59D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_59D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A9"),
        (SWITCH_DEFAULT, "loc_5BF"),
    )


    label("loc_5A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BC")
    OP_A2(0x66A)
    Event(0, 3)

    label("loc_5BC")

    Jump("loc_5BF")

    label("loc_5BF")

    Return()

    # Function_0_586 end

    def Function_1_5C0(): pass

    label("Function_1_5C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x39C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3A1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    OP_4F(0x29, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_5F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3A2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x3B3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_621")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_621")

    Return()

    # Function_1_5C0 end

    def Function_2_622(): pass

    label("Function_2_622")

    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    LoadEffect(0x2, "map\\\\mp015_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, 1780, 1500, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_622 end

    def Function_3_708(): pass

    label("Function_3_708")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_71(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3E8)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_70(0x0, 0x3E8)
    OP_70(0x1, 0x3E8)
    OP_70(0x2, 0x3E8)
    OP_70(0x3, 0x3E8)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_792")
    SetChrChipByIndex(0x103, 14)

    label("loc_792")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A8")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BB")
    SetChrChipByIndex(0x106, 20)

    label("loc_7BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CE")
    SetChrChipByIndex(0x105, 18)

    label("loc_7CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E1")
    SetChrChipByIndex(0x107, 22)

    label("loc_7E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F4")
    SetChrChipByIndex(0x108, 24)

    label("loc_7F4")

    SetChrPos(0x101, -1440, 0, -47330, 0)
    SetChrPos(0x102, 720, 0, -47210, 0)

    def lambda_81C():

        label("loc_81C")

        OP_8C(0x101, 45, 0)
        OP_48()
        Jump("loc_81C")

    QueueWorkItem2(0x10, 1, lambda_81C)

    def lambda_82D():

        label("loc_82D")

        OP_8C(0x102, 315, 0)
        OP_48()
        Jump("loc_82D")

    QueueWorkItem2(0x10, 2, lambda_82D)

    def lambda_83E():
        OP_8E(0xFE, 0xFFFFF92A, 0x0, 0x2D82, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83E)

    def lambda_859():
        OP_8E(0xFE, 0x636, 0x0, 0x2D82, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_859)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8BC")
    SetChrPos(0x0, 970, 0, -49020, 0)

    def lambda_8A4():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8A4)
    Jump("loc_8E8")

    label("loc_8BC")

    SetChrPos(0x0, -2029, 0, -48950, 0)

    def lambda_8D3():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8D3)

    label("loc_8E8")

    OP_A2(0xB)

    label("loc_8EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_936")
    SetChrPos(0x1, 970, 0, -49020, 0)

    def lambda_91E():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_91E)
    Jump("loc_962")

    label("loc_936")

    SetChrPos(0x1, -2029, 0, -48950, 0)

    def lambda_94D():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_94D)

    label("loc_962")

    OP_A2(0xB)

    label("loc_965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9B0")
    SetChrPos(0x2, 970, 0, -49020, 0)

    def lambda_998():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_998)
    Jump("loc_9DC")

    label("loc_9B0")

    SetChrPos(0x2, -2029, 0, -48950, 0)

    def lambda_9C7():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_9C7)

    label("loc_9DC")

    OP_A2(0xB)

    label("loc_9DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A2A")
    SetChrPos(0x3, 970, 0, -49020, 0)

    def lambda_A12():
        OP_8E(0xFE, 0x2EE, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A12)
    Jump("loc_A56")

    label("loc_A2A")

    SetChrPos(0x3, -2029, 0, -48950, 0)

    def lambda_A41():
        OP_8E(0xFE, 0xFFFFFD12, 0x0, 0x2602, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_A41)

    label("loc_A56")

    OP_A2(0xB)

    label("loc_A59")

    FadeToBright(2000, 0)
    OP_6E(350, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 600, 18060, 0)

    def lambda_A87():
        OP_6D(-610, 0, -1460, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A87)
    Sleep(1000)

    def lambda_AA4():
        OP_67(0, 3010, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA4)

    def lambda_ABC():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABC)
    Sleep(1000)

    def lambda_AD1():
        OP_6E(757, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AD1)
    Sleep(2000)

    def lambda_AE6():
        OP_6D(130, 1600, 15530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AE6)

    def lambda_AFE():
        OP_6B(1490, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFE)
    WaitChrThread(0x102, 0x1)
    Sleep(1000)

    def lambda_B18():
        OP_6D(0, 270, 15110, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_B18)

    def lambda_B30():
        OP_67(0, 4960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B30)
    Sleep(1000)
    SetChrFlags(0x10, 0x20)
    OP_8C(0x10, 180, 400)
    OP_44(0x10, 0xFF)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #0
        0x10,
        (
            "#6P#110FI figured you'd show up.\x02\x03",

            "#110FIn fact, I couldn't see any\x01",
            "scenario in which you would\x01",
            "do otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#002FColonel Richard...\x02\x03",

            "At the queen's request,\x01",
            "we're here to put a stop\x01",
            "to your plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#012FIt doesn't look like the\x01",
            "Gospel's working yet.\x02\x03",

            "We may still have time,\x01",
            "if we act now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "#6P#111FHaha...\x01",
            "I'm afraid not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#005FWh-Why not?!\x02\x03",

            "What is this 'Aureole' thing\x01",
            "in the first place?!\x02\x03",

            "Why is getting it so\x01",
            "important to you?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(30, 2000, 17430, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(980, 0)
    OP_6C(0, 0)
    OP_6E(757, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#5P#111FLong ago, the ancients were granted the power\x01",
            "of the Sept-Terrions...heavenly treasures,\x01",
            "which could control the ground, sea, and sky.\x02\x03",

            "One of those treasures was\x01",
            "the Aureole, the Shining Ring.\x02\x03",

            "If it's true that it really existed\x01",
            "and was no mere myth...\x02\x03",

            "...do you realize what it could\x01",
            "mean for the country? Can you\x01",
            "even begin to comprehend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#580F#1P'For the country'...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8B")

    NpcTalk(    #7
        0x102,
        "Olivier",
        (
            "#035F#2PYou're talking about using these ancient\x01",
            "weapons to intimidate other countries...\x02\x03",

            "#032FThat must be it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_10A4")

    label("loc_F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")

    NpcTalk(    #8
        0x102,
        "Kloe",
        (
            "#043F#2PYou're talking about using these ancient\x01",
            "weapons to intimidate other countries...\x02\x03",

            "That must be it...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_10A4")

    label("loc_1017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A4")

    NpcTalk(    #9
        0x102,
        "Zin",
        (
            "#074F#2PYou're talking about using these ancient\x01",
            "weapons to intimidate other countries...\x02\x03",

            "#072FThat has to be it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_10A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1124")

    ChrTalk(    #10
        0x102,
        (
            "#015F#2PYou're talking about using these ancient\x01",
            "weapons to intimidate other countries...\x02\x03",

            "#012FThat must be it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1124")


    ChrTalk(    #11
        0x10,
        (
            "#5P#111FPrecisely...\x02\x03",

            "#115FAs you are, no doubt, aware, Liberl\x01",
            "is lacking in political power among\x01",
            "our neighboring nations.\x02\x03",

            "We have only a fifth of\x01",
            "Calvard's population.\x02\x03",

            "And we don't even have\x01",
            "an eighth of Erebonia's\x01",
            "military capacity.\x02\x03",

            "Our sole superior aspect\x01",
            "is our technology, and\x01",
            "that will not last.\x02\x03",

            "#112FWe need some form of real\x01",
            "strength to avoid any chance\x01",
            "of another invasion attempt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#005F#5PTh-That doesn't mean we should\x01",
            "count on some weirdo ancient\x01",
            "weapon thingy!\x02\x03",

            "What about the outcome of\x01",
            "the war ten years ago?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#5P#116FThat happened because we had\x01",
            "Cassius Bright with us.\x02\x03",

            "#115FBut he has left the military.\x02\x03",

            "The country's great champion\x01",
            "is gone.\x02\x03",

            "#112FAnd so, the only ones who may enact\x01",
            "miracles are the Goddess herself,\x01",
            "and the hero beloved by her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#002F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#5P#110FThat is why I established the\x01",
            "Intelligence Division.\x02\x03",

            "It seems that information is our\x01",
            "last bastion of protection against\x01",
            "our enemies.\x02\x03",

            "But in order to make the Intelligence Division as\x01",
            "effective as possible, I've searched all over\x01",
            "Liberl to find some sort of decisive strength.\x02\x03",

            "Something that would invoke\x01",
            "another miracle, should disaster\x01",
            "strike the nation again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#505F#1PAnd THIS is your miracle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#5P#113FOf course. Can you imagine any\x01",
            "greater miracle than this?\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(30, 2000, 13080, 1000)

    ChrTalk(    #18
        0x101,
        (
            "#506F#1PWell, we're bracers, so protecting\x01",
            "what's important is our job...\x02\x03",

            "#501F...but that doesn't mean being\x01",
            "so powerful that everyone else\x01",
            "is cowed into submission.\x02\x03",

            "The greatest miracle of all is\x01",
            "when people band together, and\x01",
            "fight to protect what they love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "#6P#112FNonsense!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#002F#1PMy dad's just one man. He didn't\x01",
            "beat the Imperial Army on his own.\x02\x03",

            "It took a lot of people working\x01",
            "like crazy together to protect\x01",
            "the country.\x02\x03",

            "And it's the work of all\x01",
            "those people that brought\x01",
            "the war to an end.\x02\x03",

            "Weren't you one of those people?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#6P#112F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#003F#1PWe still feel the same,\x01",
            "here and now.\x02\x03",

            "When we found out what you\x01",
            "were planning, we didn't get it...\x02\x03",

            "#006FBut it's our will to help\x01",
            "people that's led us here.\x02\x03",

            "Don't you think that's\x01",
            "miracle enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#6P#115F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#000F#1PEven if it's not...\x02\x03",

            "We still believe that there's\x01",
            "potential in anyone, heck,\x01",
            "everyone.\x02\x03",

            "#500FIf another war should break\x01",
            "out in the future...\x02\x03",

            "...people will do the same thing:\x01",
            "they'll work together and do what \x01",
            "has to be done to make it through.\x02\x03",

            "#508FI don't know much about this ancient\x01",
            "power, but I DO know that we can count\x01",
            "on our fellow Liberlians!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#014F#2PEstelle...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B33")

    ChrTalk(    #26
        0x106,
        (
            "#051FHeh, listen to you with\x01",
            "the rousing speeches.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7A")

    ChrTalk(    #27
        0x104,
        (
            "#031FWell said, Estelle. Your\x01",
            "outlook is admirable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB1")

    ChrTalk(    #28
        0x105,
        "#048FI agree with you completely...\x02",
    )

    CloseMessageWindow()

    label("loc_1BB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEF")

    ChrTalk(    #29
        0x108,
        (
            "#071FHa ha...\x01",
            "Truly the words of a master.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3C")

    ChrTalk(    #30
        0x103,
        (
            "#021FI swear... When did you go\x01",
            "and get all mature on me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C95")

    ChrTalk(    #31
        0x107,
        (
            "#560FThat was awesome...\x02\x03",

            "I didn't get it all,\x01",
            "but it feels right...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C95")


    ChrTalk(    #32
        0x10,
        (
            "#6P#118FHa ha...\x01",
            "You are strong, indeed.\x02\x03",

            "Sadly, not everyone is like you.\x02\x03",

            "When face to face with an incredible\x01",
            "power...it is a temptation that is\x01",
            "simply too much to bear.\x02\x03",

            "And I have put in far too much\x01",
            "time and effort, all for this...\x02\x03",

            "I see no reason to turn back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#013F#2P...\x02\x03",

            "#012F...Just answer me one question.\x02\x03",

            "How did you know about\x01",
            "this place, Colonel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "#6P#113FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#015F#2PA forbidden power, dormant for\x01",
            "untold centuries...unknown\x01",
            "even to Her Majesty...\x02\x03",

            "To say nothing of the elevator,\x01",
            "right beneath the Treasury, that\x01",
            "leads straight here...\x02\x03",

            "#012FIt seems extremely unlikely that you'd have\x01",
            "found out about this place just by using\x01",
            "the resources of the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        "#6P#112FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#012F#2PAlso, this Gospel...\x02\x03",

            "A mysterious orbment, far more powerful\x01",
            "than even the finest ever made in the \x01",
            "Zeiss Central Factory...\x02\x03",

            "Where did you get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#6P#115F...I don't have to answer that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#016F#2PWrong!\x02\x03",

            "You don't want to answer,\x01",
            "because you CAN'T answer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "#6P#117F#3S!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#580F#1PWh-What do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#016F#2PYou simply believed that the\x01",
            "Aureole would be here.\x02\x03",

            "AND that, if you used the Black\x01",
            "Orbment, you could control it.\x02\x03",

            "But you have no idea when\x01",
            "or how you came to that\x01",
            "belief, do you?!\x02\x03",

            "Am I wrong?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        "#6P#117F...\x02",
    )

    CloseMessageWindow()
    OP_A3(0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(    #44
        0x101,
        "#580F#1PB-But that can't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#057FSo his memories could've\x01",
            "been doctored, just like\x01",
            "with Mayor Dalmore...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_23B6")

    label("loc_2238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22CA")

    ChrTalk(    #46
        0x101,
        "#580F#1PB-But that can't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x103,
        (
            "#022FSo his memories might have been\x01",
            "altered, just like with the sky\x01",
            "bandits' leader...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_23B6")

    label("loc_22CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234E")

    ChrTalk(    #48
        0x101,
        "#580F#1PB-But that can't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x108,
        (
            "#072FSo, perhaps his memories\x01",
            "were tampered with, as\x01",
            "they were with Kurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_23B6")

    label("loc_234E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B6")

    ChrTalk(    #50
        0x101,
        (
            "#580F#1PB-But that can't...\x02\x03",

            "You mean you lost your memory,\x01",
            "just like those other people?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B6")


    ChrTalk(    #51
        0x10,
        (
            "#6P#117FS-So what?!\x02\x03",

            "It doesn't matter HOW I got here...just\x01",
            "that I'm here now. And look around you...\x01",
            "I found what I was looking for, didn't I?\x02\x03",

            "These ancient constructs could\x01",
            "never have been crafted with\x01",
            "present-day techniques!\x02\x03",

            "So...I must continue down\x01",
            "my chosen path!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24D2():
        OP_6B(1290, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_24D2)

    def lambda_24E2():
        OP_6D(-100, 300, 15360, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24E2)

    def lambda_24FA():
        OP_67(0, 7570, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24FA)

    def lambda_2512():
        OP_6C(35000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2512)
    OP_9F(0x12, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0x13, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x12, -2000, 7300, 15360, 180)
    SetChrPos(0x13, 2000, 7300, 15360, 225)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x12, 27)
    SetChrChipByIndex(0x13, 27)

    def lambda_2578():
        OP_96(0xFE, 0xFFFFF060, 0x0, 0x3C00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2578)
    OP_9F(0x12, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0x12, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0x12, 26)
    OP_99(0x12, 0x0, 0x3, 0x7D0)

    def lambda_25DE():

        label("loc_25DE")

        OP_99(0xFE, 0x3, 0x7, 0x514)
        OP_48()
        Jump("loc_25DE")

    QueueWorkItem2(0x12, 1, lambda_25DE)

    def lambda_25F1():
        OP_96(0xFE, 0xFA0, 0x0, 0x3C00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_25F1)
    OP_9F(0x13, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0x13, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_99(0x13, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0x13, 26)
    OP_99(0x13, 0x0, 0x3, 0x7D0)

    def lambda_2657():

        label("loc_2657")

        OP_99(0xFE, 0x3, 0x7, 0x514)
        OP_48()
        Jump("loc_2657")

    QueueWorkItem2(0x13, 1, lambda_2657)
    Sleep(1000)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        "#580FOh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#3P#118FIf you truly believe in the path\x01",
            "YOU'VE chosen, then try to stop me!\x02\x03",

            "Succeed or fail, one dream\x01",
            "will be realized, while\x01",
            "another crumbles to dust.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2773():
        OP_6B(1000, 1000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2773)

    def lambda_2783():
        OP_94(0x0, 0xFE, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2783)
    Sleep(100)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 28)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x10, 0x2)
    Sleep(400)

    ChrTalk(    #54
        0x10,
        (
            "#3P#114FNow, allow me to show you the artistry of one\x01",
            "who studied under the Divine Blade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#005F#2PBring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#016F#2PIf this is how it must be, then\x01",
            "you'll be given no quarter!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0x3)

    def lambda_2883():
        OP_6D(-100, 300, 17360, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2883)

    def lambda_289B():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_289B)
    Sleep(20)

    def lambda_28B5():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28B5)
    Sleep(20)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_291D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2905")
    Sleep(20)

    def lambda_28F3():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_28F3)
    Jump("loc_291A")

    label("loc_2905")


    def lambda_290B():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_290B)

    label("loc_291A")

    OP_A2(0xB)

    label("loc_291D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_296E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2956")
    Sleep(20)

    def lambda_2944():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_2944)
    Jump("loc_296B")

    label("loc_2956")


    def lambda_295C():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_295C)

    label("loc_296B")

    OP_A2(0xB)

    label("loc_296E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_29A7")
    Sleep(20)

    def lambda_2995():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_2995)
    Jump("loc_29BC")

    label("loc_29A7")


    def lambda_29AD():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_29AD)

    label("loc_29BC")

    OP_A2(0xB)

    label("loc_29BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_29F8")
    Sleep(20)

    def lambda_29E6():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_29E6)
    Jump("loc_2A0D")

    label("loc_29F8")


    def lambda_29FE():
        OP_92(0xFE, 0x10, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_29FE)

    label("loc_2A0D")

    OP_A2(0xB)

    label("loc_2A10")

    Sleep(300)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    OP_23(0x90)
    OP_83(0x19, 0x0)
    Battle(0x39C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2A44"),
        (SWITCH_DEFAULT, "loc_2A47"),
    )


    label("loc_2A44")

    OP_B4(0x0)
    Return()

    label("loc_2A47")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Call(0, 4)
    Return()

    # Function_3_708 end

    def Function_4_2A74(): pass

    label("Function_4_2A74")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_71(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3E8)
    OP_71(0x0, 0x20)
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_70(0x0, 0x3E8)
    OP_70(0x1, 0x3E8)
    OP_70(0x2, 0x3E8)
    OP_70(0x3, 0x3E8)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    SetChrPos(0x10, -710, 300, 15890, 180)
    SetChrPos(0x101, -760, 0, 12210, 7)
    SetChrPos(0x102, 530, 0, 12680, 344)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2B6B")
    SetChrPos(0x0, -2370, 0, 13570, 34)
    Jump("loc_2B7C")

    label("loc_2B6B")

    SetChrPos(0x0, 1960, 0, 13940, 319)

    label("loc_2B7C")

    OP_A2(0xB)

    label("loc_2B7F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2BAF")
    SetChrPos(0x1, -2370, 0, 13570, 34)
    Jump("loc_2BC0")

    label("loc_2BAF")

    SetChrPos(0x1, 1960, 0, 13940, 319)

    label("loc_2BC0")

    OP_A2(0xB)

    label("loc_2BC3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2BF3")
    SetChrPos(0x2, -2370, 0, 13570, 34)
    Jump("loc_2C04")

    label("loc_2BF3")

    SetChrPos(0x2, 1960, 0, 13940, 319)

    label("loc_2C04")

    OP_A2(0xB)

    label("loc_2C07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2C37")
    SetChrPos(0x3, -2370, 0, 13570, 34)
    Jump("loc_2C48")

    label("loc_2C37")

    SetChrPos(0x3, 1960, 0, 13940, 319)

    label("loc_2C48")

    OP_A2(0xB)

    label("loc_2C4B")

    OP_6D(-940, 40, 14760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(326000, 0)
    OP_6E(262, 0)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #57
        0x10,
        (
            "#4P#118FImpressive... I'd expect no\x01",
            "less from the children of\x01",
            "Colonel Cassius...\x02\x03",

            "But it appears...you are too late.\x02",
        )
    )

    CloseMessageWindow()
    OP_1D(0x5C)

    def lambda_2D62():
        OP_6D(200, 2560, 18960, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D62)

    def lambda_2D7A():
        OP_67(0, 5560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D7A)

    def lambda_2D92():
        OP_6C(338000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D92)

    def lambda_2DA2():
        OP_6E(455, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DA2)
    Sleep(1000)
    OP_22(0xB8, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp007_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#580FNo...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#513F#5P...!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 1100)
    OP_70(0x5, 0x5DC)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x2, 1850)
    OP_6F(0x3, 1880)
    OP_6F(0x1, 1910)
    OP_6F(0x0, 1940)
    OP_70(0x0, 0x94C)
    OP_70(0x1, 0x94C)
    OP_70(0x2, 0x94C)
    OP_70(0x3, 0x94C)
    Sleep(4000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x64)

    def lambda_2EA4():

        label("loc_2EA4")

        OP_7C(0x0, 0x12C, 0xBB8, 0xBB8)
        OP_48()
        Jump("loc_2EA4")

    QueueWorkItem2(0x10, 1, lambda_2EA4)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE4")

    ChrTalk(    #60
        0x107,
        "#068F#5PNooooo...!\x02",
    )

    CloseMessageWindow()

    label("loc_2EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F11")

    ChrTalk(    #61
        0x106,
        "#550F#5PWhat the hell...?\x02",
    )

    CloseMessageWindow()

    label("loc_2F11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4B")

    ChrTalk(    #62
        0x104,
        "#039F#5PI've only heard the stories...\x02",
    )

    CloseMessageWindow()

    label("loc_2F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9D")

    ChrTalk(    #63
        0x105,
        (
            "#046F#5PIt's the light that shut down\x01",
            "the mayor's artifact...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(    #64
        0x108,
        "#077F#5PIs this the energy of the Yin?\x02",
    )

    CloseMessageWindow()

    label("loc_2FD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3019")

    ChrTalk(    #65
        0x103,
        "#523F#5PIt's the Orbal Shutdown Phenomenon...!\x02",
    )

    CloseMessageWindow()

    label("loc_3019")


    def lambda_301F():
        OP_6D(-5080, 5590, -6070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_301F)

    def lambda_3037():
        OP_67(0, 4890, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3037)

    def lambda_304F():
        OP_6B(4730, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_304F)

    def lambda_305F():
        OP_6C(44000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_305F)

    def lambda_306F():
        OP_6E(478, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_306F)
    Sleep(1500)
    OP_44(0x10, 0x1)
    OP_22(0x91, 0x0, 0x64)
    LoadEffect(0x2, "map\\\\mp015_00.eff")
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x6, 0x4)
    OP_6F(0x6, 0)
    OP_70(0x6, 0xF0)
    Sleep(250)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x2, 0xFF, 0xFF, 1780, 1400, 19300, 0, 0, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2A74 end

    def Function_5_31A8(): pass

    label("Function_5_31A8")

    OP_9F(0xFE, 0x64, 0x64, 0xFF, 0xFF, 0x3E8)

    def lambda_31B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_31B9)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 27)
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Return()

    # Function_5_31A8 end

    def Function_6_31DF(): pass

    label("Function_6_31DF")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 2380)
    OP_6F(0x1, 2380)
    OP_6F(0x2, 2380)
    OP_6F(0x3, 2380)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    SetChrPos(0x10, -710, 300, 15890, 180)
    SetChrPos(0x101, -760, 0, 12210, 7)
    SetChrPos(0x102, 530, 0, 12680, 344)
    OP_A3(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_32A2")
    SetChrPos(0x0, -2370, 0, 13570, 34)
    Jump("loc_32B3")

    label("loc_32A2")

    SetChrPos(0x0, 1960, 0, 13940, 319)

    label("loc_32B3")

    OP_A2(0xB)

    label("loc_32B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_32E6")
    SetChrPos(0x1, -2370, 0, 13570, 34)
    Jump("loc_32F7")

    label("loc_32E6")

    SetChrPos(0x1, 1960, 0, 13940, 319)

    label("loc_32F7")

    OP_A2(0xB)

    label("loc_32FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_333E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_332A")
    SetChrPos(0x2, -2370, 0, 13570, 34)
    Jump("loc_333B")

    label("loc_332A")

    SetChrPos(0x2, 1960, 0, 13940, 319)

    label("loc_333B")

    OP_A2(0xB)

    label("loc_333E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_336E")
    SetChrPos(0x3, -2370, 0, 13570, 34)
    Jump("loc_337F")

    label("loc_336E")

    SetChrPos(0x3, 1960, 0, 13940, 319)

    label("loc_337F")

    OP_A2(0xB)

    label("loc_3382")

    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_339F")
    SetChrChipByIndex(0x103, 14)

    label("loc_339F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B2")
    SetChrChipByIndex(0x104, 16)

    label("loc_33B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C5")
    SetChrChipByIndex(0x106, 20)

    label("loc_33C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D8")
    SetChrChipByIndex(0x105, 18)

    label("loc_33D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33EB")
    SetChrChipByIndex(0x107, 22)

    label("loc_33EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33FE")
    SetChrChipByIndex(0x108, 24)

    label("loc_33FE")

    OP_6D(-710, 5300, 15670, 0)
    OP_67(0, 10500, -25720, 0)
    OP_6B(640, 0)
    OP_6C(13000, 0)
    OP_6E(697, 0)
    FadeToBright(2000, 0)
    OP_6D(-710, 300, 15670, 3000)
    OP_0D()

    ChrTalk(    #66
        0x101,
        "#580FWha... What was that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#013FIt's the Orbal Shutdown Phenomenon,\x01",
            "but it's not like before...\x02\x03",

            "It feels like something was released...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)
    OP_22(0xB9, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_73(0x6)

    def lambda_3512():
        OP_6D(-560, 1650, 16460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3512)
    OP_72(0x5, 0x4)
    OP_6F(0x5, 1300)
    OP_70(0x5, 0x3E8)
    Sleep(2000)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 1000)
    OP_70(0x5, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #68
        "\x07\x05...Warning...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #69
        (
            "\x07\x05All personnel...\x01",
            "Warning...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #70
        0x101,
        "#580F#5PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        "#014F#2PThat thing is talking...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("Voice")

    AnonymousTalk(    #72
        (
            "\x07\x05First barrier on sealed Aureole device has\x01",
            "been confirmed as no longer operative.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        "\x07\x05Confirmed 'Gospel' has been activated.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #74
        "\x07\x05'Device Towers' have been enabled.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)
    OP_1D(0x23)
    Sleep(500)

    def lambda_3736():
        OP_6D(2820, 0, 40, 5000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3736)

    def lambda_374E():
        OP_67(0, 19430, -25720, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_374E)

    def lambda_3766():
        OP_6B(1410, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3766)

    def lambda_3776():
        OP_6C(90000, 11000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3776)

    def lambda_3786():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3786)

    def lambda_3794():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3794)

    def lambda_37A2():
        OP_8C(0xFE, 132, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_37A2)

    def lambda_37B0():
        OP_8C(0xFE, 222, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_37B0)
    Sleep(3000)
    OP_6F(0x0, 2380)
    OP_70(0x0, 0xB22)
    OP_6F(0x1, 2380)
    OP_70(0x1, 0xB22)
    OP_6F(0x2, 2380)
    OP_70(0x2, 0xB22)
    OP_6F(0x3, 2380)
    OP_70(0x3, 0xB22)
    OP_73(0x3)
    OP_22(0xBA, 0x0, 0x64)
    OP_6F(0x0, 2851)
    OP_70(0x0, 0xCA8)
    OP_6F(0x1, 2851)
    OP_70(0x1, 0xCA8)
    OP_6F(0x2, 2851)
    OP_70(0x2, 0xCA8)
    OP_6F(0x3, 2851)
    OP_70(0x3, 0xCA8)

    def lambda_383B():
        OP_67(0, 13510, -25720, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_383B)
    OP_73(0x3)
    OP_22(0x9A, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    Sleep(500)
    Fade(1000)
    OP_6F(0x6, 240)
    OP_0D()
    Fade(1000)
    OP_44(0x0, 0xFF)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 1100)
    OP_70(0x5, 0x578)
    OP_6D(-510, 300, 15530, 0)
    OP_67(0, 7800, -15530, 0)
    OP_6B(1000, 0)
    OP_6C(357000, 0)
    OP_6E(697, 0)
    OP_66(0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #75
        0x101,
        "#005FWh-What the hell's going on?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        (
            "#012FThe first barrier...\x01",
            "The sealed Aureole device...\x02\x03",

            "What's this all about, Colonel?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "#6P#117FI... I don't know...\x02\x03",

            "I didn't expect...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #78
        (
            "\x07\x05First barrier has collapsed. 'Ring' is\x01",
            "emitting very slight interference...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #79
        (
            "\x07\x05Destruction of seal on Ring\x01",
            "Guardians confirmed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #80
        (
            "\x07\x05All personnel should evacuate the\x01",
            "sealed area immediately...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_3A8A():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3A8A)

    def lambda_3A98():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_3A98)

    def lambda_3AA6():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_3AA6)

    def lambda_3AB4():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_3AB4)

    def lambda_3AC2():
        OP_6D(21480, 4400, 50, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AC2)

    def lambda_3ADA():
        OP_6E(1000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3ADA)

    def lambda_3AEA():
        OP_67(300, 4890, 20, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3AEA)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x64, 0x3E418, 0x0)
    Sleep(100)
    StopSound(0x3A98, 0x9C40, 0x1770)
    Sleep(1900)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    OP_A1(0x17, 0x7)
    OP_A1(0x18, 0xA)
    OP_A1(0x19, 0xB)
    OP_72(0x7, 0x4)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 40)
    OP_70(0x7, 0x3B)
    SetChrPos(0x17, 49760, 0, 0, 90)
    SetChrPos(0x18, 36600, 3000, 4140, 90)
    SetChrPos(0x19, 36600, 3000, -4140, 90)
    OP_22(0xBB, 0x0, 0x64)
    OP_B0(0x4, 0x50)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3E8)

    def lambda_3BD9():
        OP_6B(210, 14000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3BD9)

    def lambda_3BE9():
        OP_6E(180, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BE9)
    Sleep(7000)
    OP_20(0xBB8)

    def lambda_3C03():
        OP_8F(0xFE, 0x2C88, 0xFA0, 0xCE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3C03)

    def lambda_3C1E():
        OP_8F(0xFE, 0x2C88, 0xFA0, 0xFFFFF31C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3C1E)
    Sleep(3000)
    OP_72(0x7, 0x20)
    OP_73(0x7)
    OP_1D(0x2D)
    LoadEffect(0x5, "map\\\\mp030_0.eff")
    Play3DEffect(0x5, 0x0, 0x7, "Frame8_Bone__7_", 0x3B6, 0x258, 0x1F4, 0x0, 0x0, 0x0, 0x2BC, 0x2BC, 0x2BC, 0x0)
    Sleep(400)
    Play3DEffect(0x5, 0x1, 0x7, "Frame8_Bone__7_", 0x41A, 0xFFFFFF9C, 0x2BC, 0x0, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    Sleep(100)
    Play3DEffect(0x5, 0x2, 0x7, "Frame8_Bone__7_", 0x3B6, 0x12C, 0x384, 0x0, 0x0, 0x0, 0x2BC, 0x2BC, 0x2BC, 0x0)
    Sleep(100)
    Play3DEffect(0x5, 0x3, 0x7, "Frame8_Bone__7_", 0x47E, 0xC8, 0xFA, 0x0, 0x0, 0x0, 0x384, 0x384, 0x384, 0x0)

    def lambda_3D42():
        OP_67(300, -500, 20, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D42)

    def lambda_3D5A():
        OP_6D(16980, 3210, 0, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D5A)

    def lambda_3D72():
        OP_6B(700, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3D72)

    def lambda_3D82():
        OP_6E(730, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D82)
    Sleep(1000)
    OP_43(0x17, 0x3, 0x0, 0x7)
    WaitChrThread(0x18, 0x0)

    def lambda_3DA3():
        OP_8C(0xFE, 45, 80)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3DA3)

    def lambda_3DB1():
        OP_8F(0xFE, 0x2710, 0xBB8, 0x1A90, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3DB1)
    WaitChrThread(0x19, 0x0)

    def lambda_3DD1():
        OP_8C(0xFE, 135, 80)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3DD1)

    def lambda_3DDF():
        OP_8F(0xFE, 0x2710, 0xBB8, 0xFFFFE570, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3DDF)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    WaitChrThread(0x17, 0x3)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0xFF)
    Fade(1500)
    OP_66(0x1)
    SetChrPos(0x0, 3380, 0, 950, 90)
    SetChrPos(0x1, 3480, 0, -870, 90)
    SetChrPos(0x3, 1900, 0, 2270, 90)
    SetChrPos(0x2, 2520, 0, -2190, 90)
    ClearMapFlags(0x10)
    OP_6D(9220, 1300, 140, 0)
    OP_67(0, 7430, -15660, 0)
    OP_6B(1680, 0)
    OP_6C(90000, 0)
    OP_6E(433, 0)
    OP_0D()

    ChrTalk(    #81
        0x101,
        (
            "#509FWhat are THESE freaky-looking\x01",
            "things...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#016FStay on your toes! These\x01",
            "are the Ring Guardians!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F51")

    ChrTalk(    #83
        0x103,
        (
            "#023FHa ha... This is really happening,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F99")

    ChrTalk(    #84
        0x104,
        (
            "#032FAre these artifacts of\x01",
            "the ancients, too...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3F99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FD1")

    ChrTalk(    #85
        0x105,
        "#042FI... I can't believe that...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_3FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401D")

    ChrTalk(    #86
        0x107,
        (
            "#065FI don't believe it...\x01",
            "The archaisms are huge...!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_401D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_406B")

    ChrTalk(    #87
        0x106,
        (
            "#055FHey! Are we actually going\x01",
            "to fight these things?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_406B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40CF")

    ChrTalk(    #88
        0x108,
        (
            "#077FDo not be deceived by their\x01",
            "appearance! They are not to\x01",
            "be trifled with!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_40CF")

    WaitChrThread(0x0, 0x0)
    OP_72(0x7, 0x20)
    OP_73(0x7)

    def lambda_40E2():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40E2)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #89 op#A op#5
        "\x07\x02#15AGate sealed...\x05\x02",
    )

    Sleep(2000)

    AnonymousTalk(    #90 op#A op#5
        "\x07\x02#25AOrbal power source recovered...\x05\x02",
    )

    Sleep(2700)

    AnonymousTalk(    #91 op#A op#5
        "\x07\x02#26ASystem restart complete...\x05\x02",
    )

    Sleep(2500)

    AnonymousTalk(    #92 op#A op#5
        "\x07\x02#45AMODE: Eliminate intruders...\x05\x02",
    )

    Sleep(3000)
    OP_B0(0x7, 0x8)
    OP_6F(0x7, 230)
    OP_70(0x7, 0xEC)
    OP_73(0x7)
    OP_22(0xED, 0x0, 0x64)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 237)
    OP_70(0x7, 0xF3)
    OP_73(0x7)
    OP_22(0xEE, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    AnonymousTalk(    #93 op#A op#5
        "\x07\x02#15ATarget coordinates confirmed...\x05\x02",
    )

    Sleep(300)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 244)
    OP_70(0x7, 0xF9)
    OP_73(0x7)
    OP_22(0xED, 0x0, 0x64)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 250)
    OP_70(0x7, 0xFE)
    OP_73(0x7)
    OP_22(0xEE, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    Sleep(200)

    AnonymousTalk(    #94 op#A op#5
        "\x07\x02#30ASeal mechanism facility: Bottom level...\x05\x02",
    )

    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 254)
    OP_70(0x7, 0x116)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    OP_B0(0x7, 0x14)
    OP_6F(0x7, 279)
    OP_70(0x7, 0x120)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 293)
    OP_70(0x7, 0x133)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 308)
    OP_70(0x7, 0x13B)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)

    AnonymousTalk(    #95 op#A op#5
        "\x07\x02#27ARing Guardian: Reverie...\x05\x02",
    )

    OP_B0(0x7, 0xF)
    OP_6F(0x7, 289)
    OP_70(0x7, 0x124)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    OP_B0(0x7, 0xC)
    OP_6F(0x7, 316)
    OP_70(0x7, 0x144)
    OP_73(0x7)
    OP_B0(0x7, 0x9)
    OP_6F(0x7, 325)
    OP_70(0x7, 0x149)
    OP_73(0x7)
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x14C)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEE, 0x0, 0x64)
    Sleep(1500)

    AnonymousTalk(    #96 op#A op#5
        "\x07\x02#35ANow resuming search for intruders...\x05\x02",
    )

    Sleep(1800)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    Sleep(2000)
    OP_56(0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_22(0xEC, 0x0, 0x5A)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 333)
    OP_70(0x7, 0x17E)
    SetChrFlags(0x17, 0x4)

    def lambda_4452():
        OP_91(0x17, 0xFFFFD120, 0xFFFFE890, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4452)

    def lambda_446D():
        OP_6D(8900, 5600, 110, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_446D)

    def lambda_4485():
        OP_6B(1380, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4485)

    def lambda_4495():
        OP_67(0, -130, -18290, 500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4495)
    Sleep(500)
    OP_44(0x17, 0xFF)
    OP_72(0x7, 0x8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    Battle(0x3A1, 0x100009, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_31DF end

    def Function_7_44D5(): pass

    label("Function_7_44D5")

    OP_B0(0x7, 0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4603")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    def lambda_4500():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4500)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 141)
    OP_70(0x7, 0x92)
    OP_73(0x7)

    def lambda_4530():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4530)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 147)
    OP_70(0x7, 0x96)
    OP_73(0x7)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_4A(0x17, 0)
    Sleep(100)
    OP_4B(0x17, 0)

    def lambda_4583():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4583)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 151)
    OP_70(0x7, 0x9C)
    OP_73(0x7)

    def lambda_45B3():
        OP_8F(0xFE, 0x3EE4, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_45B3)
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 157)
    OP_70(0x7, 0x9F)
    OP_73(0x7)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_4A(0x17, 0)
    Sleep(100)
    OP_4B(0x17, 0)
    Jump("loc_44E3")

    label("loc_4603")

    OP_73(0x7)
    OP_6F(0x7, 180)
    OP_70(0x7, 0xD1)
    Sleep(1000)
    OP_22(0xEC, 0x0, 0x64)
    OP_73(0x7)
    OP_71(0x7, 0x20)
    OP_6F(0x7, 40)
    OP_70(0x7, 0x3B)
    OP_B0(0x7, 0xF)
    Return()

    # Function_7_44D5 end

    def Function_8_4639(): pass

    label("Function_8_4639")

    EventBegin(0x0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x8)
    OP_72(0x8, 0x4)
    OP_6F(0x8, 20)
    OP_6D(-200, 7250, -130, 0)
    OP_67(0, 2930, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4708")
    SetChrChipByIndex(0x103, 14)

    label("loc_4708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_471B")
    SetChrChipByIndex(0x104, 16)

    label("loc_471B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_472E")
    SetChrChipByIndex(0x106, 20)

    label("loc_472E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4741")
    SetChrChipByIndex(0x105, 18)

    label("loc_4741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4754")
    SetChrChipByIndex(0x107, 22)

    label("loc_4754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4767")
    SetChrChipByIndex(0x108, 24)

    label("loc_4767")

    SetChrPos(0x17, 5900, 0, -30, 90)
    SetChrPos(0x0, -6050, 0, -660, 90)
    SetChrPos(0x1, -6050, 0, 660, 90)
    SetChrPos(0x2, -4270, 0, -2020, 90)
    SetChrPos(0x3, -4270, 0, 2020, 90)
    OP_6F(0x8, 22)
    OP_70(0x8, 0x29)
    OP_71(0x8, 0x20)
    FadeToBright(1000, 0)
    OP_6D(-200, 2250, -130, 3000)

    ChrTalk(    #97
        0x101,
        "#580FWhy won't it just DROP already?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x102,
        (
            "#016FLooks like it still has some\x01",
            "power left in it. Watch out!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(200)
    Fade(1000)

    def lambda_4889():
        OP_6C(90000, 11000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4889)
    OP_6D(5470, 1000, -180, 0)
    OP_67(0, 8560, -10000, 0)
    OP_6B(1940, 0)
    OP_6C(134000, 0)
    OP_6E(434, 0)
    OP_72(0x8, 0x20)
    OP_6F(0x8, 42)
    OP_70(0x8, 0x40)
    OP_21()
    OP_1D(0x2E)
    OP_73(0x8)
    OP_22(0xEF, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_6F(0x8, 65)
    OP_70(0x8, 0x50)
    Sleep(500)

    def lambda_4918():
        OP_6D(5470, 3000, -180, 5500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4918)

    def lambda_4930():
        OP_6B(3390, 600)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4930)
    OP_73(0x8)
    OP_6F(0x8, 81)
    OP_70(0x8, 0x6B)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_73(0x8)
    OP_22(0xF0, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    OP_6F(0x8, 108)
    OP_70(0x8, 0x6E)
    OP_73(0x8)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_499D():
        OP_6B(1870, 3500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_499D)
    OP_6F(0x8, 112)
    OP_70(0x8, 0x97)
    OP_73(0x8)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    OP_44(0x0, 0x3)

    def lambda_49D3():
        OP_67(0, 160, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_49D3)
    OP_22(0xF1, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x8, 152)
    OP_70(0x8, 0xAE)
    OP_73(0x8)
    OP_22(0xF1, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    def lambda_4A20():
        OP_6B(1870, 2600)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4A20)
    OP_6F(0x8, 175)
    OP_70(0x8, 0xCE)
    OP_73(0x8)
    OP_22(0xF2, 0x0, 0x64)

    def lambda_4A46():
        OP_6E(651, 300)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4A46)

    def lambda_4A56():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4A56)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_6F(0x8, 207)
    OP_70(0x8, 0xFA)
    Sleep(300)

    def lambda_4A8A():
        OP_6E(409, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4A8A)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 251)
    OP_70(0x8, 0x10E)
    WaitChrThread(0x0, 0x3)
    WaitChrThread(0x0, 0x2)
    OP_44(0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Artificial Voice")

    AnonymousTalk(    #99 op#A op#5
        "\x07\x02#35AMODE: Annihilation\x05\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    Sleep(2000)
    Sleep(1000)

    AnonymousTalk(    #100 op#A op#5
        "\x07\x02#35ARing Guardian: Reverie...\x05\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    Sleep(1500)
    OP_B0(0x7, 0xC)
    OP_6F(0x7, 316)
    OP_70(0x7, 0x144)
    OP_73(0x7)
    OP_B0(0x7, 0x9)
    OP_6F(0x7, 325)
    OP_70(0x7, 0x149)
    OP_73(0x7)
    OP_B0(0x7, 0x7)
    OP_6F(0x7, 330)
    OP_70(0x7, 0x14C)
    OP_73(0x7)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    AnonymousTalk(    #101 op#A op#5
        "\x07\x02#36ANow resuming extermination activity...\x05\x02",
    )

    Sleep(1300)
    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    Sleep(2000)
    OP_56(0x0)
    OP_72(0x8, 0x20)
    OP_73(0x8)

    def lambda_4BF2():
        OP_67(0, 4190, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4BF2)

    def lambda_4C0A():
        OP_6B(2400, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4C0A)
    OP_6F(0x8, 320)
    OP_70(0x8, 0x14E)
    OP_73(0x8)
    LoadEffect(0x4, "map\\\\mp021_04.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 5470, 3000, -180, 0, 90, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_22(0xF3, 0x0, 0x64)

    def lambda_4C79():
        OP_6B(6000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4C79)
    OP_7C(0x0, 0x1F4, 0xBB8, 0xBB8)
    OP_6F(0x8, 336)
    OP_70(0x8, 0x159)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3A2, 0x100008, 0x0, 0x80, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_4CCD"),
        (SWITCH_DEFAULT, "loc_4CD0"),
    )


    label("loc_4CCD")

    OP_B4(0x0)
    Return()

    label("loc_4CD0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4CDF")
    OP_83(0x19, 0x1)

    label("loc_4CDF")

    OP_71(0x8, 0x4)
    Call(0, 9)
    Return()

    # Function_8_4639 end

    def Function_9_4CE9(): pass

    label("Function_9_4CE9")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_3F(0x357, 1)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x9)
    OP_72(0x9, 0x4)
    OP_6F(0x9, 275)
    OP_6D(1640, 0, -1300, 0)
    OP_67(0, 6640, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(111000, 0)
    OP_6E(418, 0)
    SetChrPos(0x17, 5900, 0, -30, 75)
    SetChrPos(0x10, -4780, 0, 6090, 137)
    SetChrFlags(0x10, 0x80)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 29)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    SetChrPos(0x101, -2910, 0, -3850, 47)
    SetChrPos(0x102, -1740, 0, -6390, 6)
    SetChrPos(0x0, -4710, 0, 610, 127)
    SetChrPos(0x1, -5270, 0, -1970, 111)
    SetChrChipByIndex(0x101, 37)
    SetChrChipByIndex(0x102, 38)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E4D")
    SetChrChipByIndex(0x103, 39)

    label("loc_4E4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E60")
    SetChrChipByIndex(0x104, 40)

    label("loc_4E60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E73")
    SetChrChipByIndex(0x106, 42)

    label("loc_4E73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E86")
    SetChrChipByIndex(0x105, 41)

    label("loc_4E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E99")
    SetChrChipByIndex(0x107, 43)

    label("loc_4E99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EAC")
    SetChrChipByIndex(0x108, 44)

    label("loc_4EAC")

    SetChrSubChip(0x0, 3)
    SetChrSubChip(0x1, 3)
    SetChrSubChip(0x2, 3)
    SetChrSubChip(0x3, 3)
    LoadEffect(0x0, "monster\\\\ms10000.eff")
    LoadEffect(0x1, "monster\\\\ms10001.eff")
    LoadEffect(0x2, "monster\\\\ms10002.eff")
    LoadEffect(0x3, "monster\\msc0270b.eff")

    def lambda_4F22():
        OP_6B(2530, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4F22)

    def lambda_4F32():
        OP_6C(69000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F32)
    Sleep(4000)

    ChrTalk(    #102
        0x101,
        (
            "#581F*huff* *huff*\x02\x03",

            "D-Did we beat it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#013FY-Yeah... Or at least, none of\x01",
            "the parts are moving anymore...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 36)
    SetChrSubChip(0x10, 0)
    OP_66(0x0)
    OP_6D(-880, 0, 620, 2000)

    ChrTalk(    #104
        0x10,
        (
            "#6P#112FThe Ring Guardian...\x02\x03",

            "Seems like its goal was to destroy\x01",
            "this facility... to destroy the\x01",
            "seat of the Aureole...\x02\x03",

            "When the Aureole was sealed, it was sealed along\x01",
            "with it. Disabled, but set to be reactivated if\x01",
            "anyone tried to take the artifact...\x02\x03",

            "#115FMaybe the ancients were in\x01",
            "dispute over the Aureole themselves...\x02\x03",

            "#116FBut...where is it, then...?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_B0(0x9, 0x3)
    OP_6F(0x9, 275)
    OP_70(0x9, 0x118)
    Sleep(1000)
    OP_62(0x0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_21()
    OP_73(0x9)
    OP_B0(0x9, 0xC)
    OP_6F(0x9, 281)
    OP_70(0x9, 0x11D)
    OP_73(0x9)
    OP_1D(0x2D)
    OP_B0(0x9, 0x14)
    OP_6F(0x9, 286)
    OP_70(0x9, 0x127)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_22(0xEC, 0x0, 0x64)

    ChrTalk(    #105 op#A op#5
        0x10,
        (
            "#113F#6P#26AWhat...?! How is it still\x01",
            "able to move?!\x05\x02",
        )
    )

    Sleep(1200)
    OP_72(0x9, 0x20)
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x1770)
    Sleep(900)

    def lambda_528C():
        OP_6D(1630, 550, -840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_528C)
    OP_43(0x17, 0x1, 0x0, 0xA)
    Sleep(500)
    WaitChrThread(0x17, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5320")

    ChrTalk(    #106
        0x103,
        (
            "#522F#5PGah... My body's not listening\x01",
            "to what I'm telling it... I can't\x01",
            "move at all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5485")

    label("loc_5320")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5390")

    ChrTalk(    #107
        0x104,
        (
            "#034F#5PMy...body...\x01",
            "My beautiful body...isn't doing\x01",
            "what my brain is telling it to!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5485")

    label("loc_5390")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53CF")

    ChrTalk(    #108
        0x106,
        "#550F#5PGeh! I can't move a muscle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5485")

    label("loc_53CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5410")

    ChrTalk(    #109
        0x107,
        "#069F#5PM-My legs don't wanna work...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5485")

    label("loc_5410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5448")

    ChrTalk(    #110
        0x108,
        "#077F#5PTh-This is unreal...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5485")

    label("loc_5448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5485")

    ChrTalk(    #111
        0x105,
        "#541F#5PI... I can't move my body...\x02",
    )

    CloseMessageWindow()

    label("loc_5485")


    ChrTalk(    #112
        0x101,
        "#581F#5PJ-Joshua...!\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #113
        0x102,
        "#016F#2PEstelle!\x02",
    )

    CloseMessageWindow()

    def lambda_54C3():

        label("loc_54C3")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_54C3")

    QueueWorkItem2(0x102, 2, lambda_54C3)
    SetChrChipByIndex(0x102, 12)
    OP_22(0xA4, 0x0, 0x64)
    OP_96(0x102, 0xFFFFFA1A, 0x0, 0xFFFFF358, 0x1F4, 0xFA0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_73(0x9)
    OP_B0(0x9, 0x6)
    OP_6F(0x9, 210)
    OP_70(0x9, 0xD5)

    def lambda_5518():
        OP_6C(70000, 1700)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5518)

    def lambda_5528():
        OP_67(0, -1770, -30160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5528)

    def lambda_5540():
        OP_6D(2730, 3000, -2190, 1700)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5540)

    def lambda_5558():
        OP_6B(770, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5558)
    OP_73(0x9)
    OP_B0(0x9, 0x6)
    OP_6F(0x9, 214)
    OP_70(0x9, 0xDD)
    OP_73(0x9)
    WaitChrThread(0x0, 0x1)
    SetChrPos(0x1A, 1980, 5000, 1220, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(100)
    OP_7C(0x0, 0xC8, 0xBB8, 0x3E8)
    OP_B0(0x9, 0xD)
    OP_73(0x9)
    OP_6F(0x9, 222)
    OP_70(0x9, 0xE2)
    OP_73(0x9)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 28)
    SetChrPos(0x10, -440, 0, 4310, 119)
    SetChrPos(0x1B, -440, 0, 4310, 119)
    SetChrPos(0x1C, -440, 0, 4310, 119)
    SetChrPos(0x1D, -440, 0, 4310, 119)
    SetChrPos(0x1E, -440, 0, 4310, 119)

    def lambda_565E():
        OP_6D(1680, 1900, 600, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_565E)

    def lambda_5676():
        OP_67(0, 12070, -30160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5676)

    def lambda_568E():
        OP_6B(740, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_568E)

    def lambda_569E():
        OP_6C(18000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_569E)

    def lambda_56AE():
        OP_6E(512, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_56AE)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7C(0x0, 0x258, 0xBB8, 0x64)

    def lambda_56D8():
        OP_8C(0xFE, 120, 50)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_56D8)
    OP_8C(0x17, 110, 0)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 227)
    OP_70(0x9, 0x103)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)
    WaitChrThread(0x0, 0x3)

    ChrTalk(    #114
        0x101,
        "#5P#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        "#5P#114F...Not a chance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        "#014F#5PC-Colonel...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        (
            "#5P#112FI'll deal with this!\x02\x03",

            "Get out of here, NOW!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#580F#5PB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        (
            "#5P#114FYou barely survived fighting\x01",
            "this thing the last time!\x02\x03",

            "I'm still ready for combat!\x02\x03",

            "I can buy you some time\x01",
            "at least!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x10, 0x4)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x1B, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)

    def lambda_58CC():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_58CC)
    Sleep(50)

    def lambda_58EC():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_58EC)
    Sleep(50)

    def lambda_590C():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_590C)
    Sleep(50)

    def lambda_592C():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_592C)
    Sleep(50)

    def lambda_594C():
        OP_8E(0xFE, 0xDB6, 0x0, 0x4CE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_594C)
    WaitChrThread(0x10, 0x0)
    Fade(1000)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(6200, 3370, 160, 0)
    OP_67(0, 12070, -30160, 0)
    OP_6B(850, 0)
    OP_6C(152000, 0)
    OP_6E(512, 0)

    def lambda_59E8():
        OP_6D(5750, 2370, -170, 15000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_59E8)

    def lambda_5A00():
        OP_67(0, 4050, -30160, 15000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5A00)

    def lambda_5A18():
        OP_6B(970, 15000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5A18)

    def lambda_5A28():
        OP_6C(97000, 15000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5A28)

    def lambda_5A38():
        OP_6E(561, 15000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_5A38)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x1B, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)
    SetChrChipByIndex(0x10, 8)
    SetChrPos(0x1B, 5370, 0, 710, 139)
    SetChrPos(0x1C, 5370, 0, 710, 139)
    SetChrPos(0x1D, 5370, 0, 710, 139)
    SetChrPos(0x1E, 5370, 0, 710, 139)
    SetChrPos(0x10, 5370, 0, 710, 139)
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xB)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xC)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 4890, 2450, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_43(0x10, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xD)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xD)
    WaitChrThread(0x10, 0x0)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_73(0x9)
    OP_6F(0x9, 510)
    OP_70(0x9, 0x212)
    OP_43(0x10, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xE)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xE)
    Sleep(600)
    OP_22(0xED, 0x0, 0x64)
    OP_73(0x9)
    OP_22(0x55, 0x0, 0x64)
    OP_7C(0x0, 0x3E8, 0xBB8, 0x64)
    OP_43(0x10, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_7C(0x0, 0xC8, 0xBB8, 0xBB8)
    OP_43(0x1C, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0xF)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0xF)
    WaitChrThread(0x10, 0x0)
    OP_7C(0x0, 0x1, 0xBB8, 0xA)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 3900, 3300, 1120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x9, 227)
    OP_70(0x9, 0xFE)
    OP_43(0x10, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x10)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x10)
    WaitChrThread(0x10, 0x0)
    OP_73(0x9)
    OP_43(0x10, 0x0, 0x0, 0x11)
    Sleep(430)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x73)
    Sleep(200)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x73)
    Sleep(200)
    OP_B0(0x9, 0x50)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_73(0x9)
    OP_6F(0x9, 510)
    OP_70(0x9, 0x213)
    Sleep(200)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)

    def lambda_5E01():
        OP_8C(0xFE, 46, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E01)
    Sleep(650)
    OP_22(0xED, 0x0, 0x64)
    OP_73(0x9)
    OP_6F(0x9, 227)
    OP_70(0x9, 0xFE)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_5E2F():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E2F)
    SetChrSubChip(0x10, 7)
    Sleep(200)

    def lambda_5E54():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E54)
    Sleep(200)

    def lambda_5E74():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E74)
    Sleep(200)

    def lambda_5E94():
        OP_8F(0xFE, 0x2E4, 0x0, 0x780, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E94)

    def lambda_5EAF():
        OP_99(0xFE, 0x7, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_5EAF)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1B, 0x80)
    OP_43(0x1B, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1C, 0x80)
    OP_43(0x1C, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1D, 0x80)
    OP_43(0x1D, 0x0, 0x0, 0x12)
    Sleep(50)
    ClearChrFlags(0x1E, 0x80)
    OP_43(0x1E, 0x0, 0x0, 0x12)
    Sleep(350)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x70)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 1500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x70)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 3300, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 105)
    OP_70(0x9, 0x7E)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2800, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_22(0x1F8, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 4890, 2500, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)

    ChrTalk(    #120
        0x101,
        "#004F#2PW-Wow...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#012F#2PHe really did learn his\x01",
            "techniques from Dad...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    TurnDirection(0x10, 0x101, 800)

    ChrTalk(    #122
        0x10,
        (
            "#5P#114FWhat are you doing?!\x01",
            "GO! NOW!\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x9, 0x20)

    def lambda_6173():
        OP_6B(640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6173)

    def lambda_6183():
        OP_6C(139000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6183)

    def lambda_6193():
        OP_6D(390, 0, 1360, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6193)

    def lambda_61AB():
        OP_6E(561, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_61AB)

    def lambda_61BB():
        OP_67(0, 16200, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_61BB)

    def lambda_61D3():
        OP_8C(0xFE, 90, 100)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_61D3)
    OP_B0(0x9, 0x32)
    OP_6F(0x9, 489)
    OP_70(0x9, 0x1BC)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 443)
    OP_70(0x9, 0x1A5)
    Sleep(60)
    OP_96(0x10, 0xFFFFFFB0, 0x0, 0x942, 0x1F4, 0x1770)
    OP_8C(0x10, 14, 800)
    OP_73(0x9)
    OP_22(0x55, 0x0, 0x50)
    OP_7C(0x0, 0x258, 0xBB8, 0x64)
    WaitChrThread(0x10, 0x1)
    Sleep(100)
    SetChrChipByIndex(0x10, 33)
    OP_22(0x1F8, 0x0, 0x64)
    OP_99(0x10, 0x0, 0x1, 0x7D0)

    def lambda_6261():
        OP_6D(0, 2800, -50, 6000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6261)

    def lambda_6279():
        OP_67(0, 15760, -30160, 6000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6279)

    def lambda_6291():
        OP_6C(130000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6291)
    OP_9E(0x10, 0x50, 0x0, 0xFA, 0x7530)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 100, 1000, 3150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_6302():
        OP_99(0xFE, 0x2, 0x5, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6302)
    OP_B0(0x9, 0x96)
    OP_6F(0x9, 421)
    OP_70(0x9, 0x1BB)
    OP_43(0x20, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1B, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_7C(0x0, 0x64, 0xBB8, 0x1388)
    OP_43(0x1C, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1D, 0x0, 0x0, 0x13)
    Sleep(20)
    OP_43(0x1E, 0x0, 0x0, 0x13)
    OP_73(0x9)
    OP_B0(0x9, 0x1E)
    OP_6F(0x9, 444)
    OP_70(0x9, 0x1E9)
    Sleep(400)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_639D():
        OP_8F(0xFE, 0x33E, 0x0, 0x50A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_639D)

    def lambda_63B8():
        OP_99(0xFE, 0x6, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_63B8)

    def lambda_63C8():

        label("loc_63C8")

        TurnDirection(0xFE, 0x20, 0)
        OP_48()
        Jump("loc_63C8")

    QueueWorkItem2(0x10, 2, lambda_63C8)
    Sleep(1300)
    Sleep(100)

    def lambda_63E3():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_63E3)
    OP_73(0x9)

    def lambda_63F4():
        OP_6B(680, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_63F4)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 515)
    OP_70(0x9, 0x20E)
    OP_73(0x9)
    OP_22(0xED, 0x0, 0x64)
    OP_6F(0x9, 527)
    OP_70(0x9, 0x212)
    OP_73(0x9)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3160, 1480, 1320, 0)

    ChrTalk(    #123 op#A op#5
        0x10,
        "#10A#117FAAAARRGGH!\x05\x02",
    )

    OP_B0(0x9, 0xF)
    OP_6F(0x9, 531)
    OP_70(0x9, 0x24B)
    WaitChrThread(0x0, 0x3)

    def lambda_647E():
        OP_67(0, 6790, -30160, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_647E)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_6F(0x9, 588)
    OP_70(0x9, 0x25F)

    ChrTalk(    #124
        0x101,
        "#580F#2PC-Colonel!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        "#016F#2PWhat should we do?!\x02",
    )

    CloseMessageWindow()

    def lambda_64E6():
        OP_6D(5700, 2800, 380, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_64E6)

    ChrTalk(    #126
        0x10,
        (
            "#5P#117FSh...shut up and go!\x02\x03",

            "My fate was sealed...when\x01",
            "I lost my fight with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#580F#1PN-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x10,
        (
            "#5P#118FD-Don't...worry about it...\x02\x03",

            "My plan may have ended\x01",
            "in failure...\x02\x03",

            "...but if I can help you...perhaps...\x01",
            "that will be repentance enough...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, 260, 0, -8970, 154)

    NpcTalk(    #129
        0x11,
        "Man's Voice",
        "#1PSuch a pity...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #130
        0x11,
        "Man's Voice",
        (
            "#1PIf you think of this as a hopeless\x01",
            "battle, then that's exactly what\x01",
            "it will be!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #131
        0x11,
        "Man's Voice",
        (
            "#1PHave you forgotten everything\x01",
            "I taught you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x15E, 2400, 0x2, 0x7, 0x50, 0x1)
    WaitChrThread(0x0, 0x0)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "craft\\\\cr201_01.eff")
    LoadEffect(0x2, "monster\\\\ms10002.eff")
    LoadEffect(0x3, "monster\\\\ms10001.eff")
    LoadEffect(0x4, "map\\\\mp021_04.eff")
    SoundLoad(132)
    SoundLoad(521)
    SoundLoad(136)
    SetChrFlags(0x20, 0x80)
    OP_72(0x9, 0x20)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0x8)
    OP_6F(0x9, 588)
    OP_70(0x9, 0x25F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_719C")
    OP_A3(0x7)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_67DF():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_67DF)

    def lambda_67F1():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_67F1)

    def lambda_6803():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0xA0, 0x384)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_6803)

    def lambda_6815():
        OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x78, 0x44C)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_6815)

    def lambda_6827():
        OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x50, 0x514)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_6827)

    def lambda_6839():
        OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x28, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_6839)
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x15)
    Sleep(50)
    OP_43(0x1F, 0x0, 0x0, 0x15)

    def lambda_688E():
        OP_6D(5630, 2800, -60, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_688E)

    def lambda_68A6():
        OP_67(0, 16840, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_68A6)

    def lambda_68BE():
        OP_6B(510, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_68BE)

    def lambda_68CE():
        OP_6C(73000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_68CE)

    def lambda_68DE():
        OP_6E(926, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_68DE)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #132 op#A op#5
        0x11,
        "#5P#10AHah!\x05\x02",
    )

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 646)
    OP_70(0x9, 0x2AC)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 685)
    OP_70(0x9, 0x2BF)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #133
        0x101,
        "#004F#2PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        "#014F#2PIt can't be...\x02",
    )

    CloseMessageWindow()
    OP_72(0x9, 0x20)

    def lambda_69C1():
        OP_6D(5610, 1150, -1750, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_69C1)

    def lambda_69D9():
        OP_67(0, 26710, -30160, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_69D9)

    def lambda_69F1():
        OP_6B(460, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_69F1)

    def lambda_6A01():
        OP_6C(18000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6A01)

    def lambda_6A11():
        OP_6E(698, 5000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_6A11)
    OP_43(0x11, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1B, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1C, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1D, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1E, 0x0, 0x0, 0x16)
    Sleep(35)
    OP_43(0x1F, 0x0, 0x0, 0x16)
    OP_A3(0x7)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 5190, 0, -3170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #135 op#A op#5
        0x11,
        "#10AHah!\x05\x02",
    )

    OP_6F(0x9, 746)
    OP_70(0x9, 0x305)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    WaitChrThread(0x11, 0x0)
    Sleep(900)
    OP_43(0x11, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1B, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1C, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1D, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1E, 0x0, 0x0, 0x17)
    Sleep(35)
    OP_43(0x1F, 0x0, 0x0, 0x17)
    OP_A3(0x7)
    OP_73(0x9)
    OP_A2(0x7)
    Sleep(350)
    PlayEffect(0x3, 0xFF, 0xFF, 5690, 4400, -2090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0x88, 0x0, 0x64)

    ChrTalk(    #136 op#A op#5
        0x11,
        "#10AHAAAAHH!\x05\x02",
    )

    Sleep(100)
    OP_6F(0x9, 774)
    OP_70(0x9, 0x31B)
    Sleep(215)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x4, 0xFF, 0xFF, 6210, 400, -720, 0, 90, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x7D0, 0x64)
    OP_73(0x9)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Fade(1500)
    OP_6D(6150, 200, -1670, 0)
    OP_67(0, 19180, -30160, 0)
    OP_6B(500, 0)
    OP_6C(66000, 0)
    OP_6E(702, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6C56():
        OP_6D(6150, 850, -1670, 4500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6C56)

    def lambda_6C6E():
        OP_6C(135000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_6C6E)

    def lambda_6C7E():
        OP_67(0, 11370, -30160, 4500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6C7E)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x11, 0, 0, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    Sleep(1250)
    OP_B0(0x9, 0x8)
    OP_6F(0x9, 796)
    OP_70(0x9, 0x32F)
    OP_73(0x9)
    WaitChrThread(0x0, 0x2)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)

    def lambda_6CF7():
        OP_6B(590, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6CF7)

    def lambda_6D07():
        OP_6D(7980, 1430, -610, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_6D07)
    OP_22(0x84, 0x0, 0x64)
    OP_43(0x11, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1B, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1C, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1D, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1E, 0x0, 0x0, 0x18)
    Sleep(15)
    OP_43(0x1F, 0x0, 0x0, 0x18)
    OP_22(0x209, 0x0, 0x64)
    OP_4A(0x0, 255)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x11, 0)
    SetChrSubChip(0x1B, 7)
    SetChrSubChip(0x1C, 7)
    SetChrSubChip(0x1D, 7)
    SetChrSubChip(0x1E, 7)
    SetChrSubChip(0x11, 7)
    OP_6F(0x9, 816)
    OP_82(0x1, 0x0)
    OP_20(0xBB8)
    PlayEffect(0x2, 0xFF, 0xFF, 5800, 2800, -720, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6B(480, 500)
    OP_4B(0x0, 255)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x11, 0)
    OP_22(0xF6, 0x0, 0x64)

    ChrTalk(    #137 op#A op#5
        0x11,
        "#10AHmph!\x05\x02",
    )

    LoadEffect(0x4, "map\\\\mp031_0.eff")
    PlayEffect(0x4, 0xFF, 0xFF, 7600, 1730, -590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 816)
    OP_70(0x9, 0x34B)
    OP_73(0x9)
    Fade(1000)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x11, 13)
    OP_21()

    ChrTalk(    #138
        0x11,
        (
            "*sigh*\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #139
        0x11,
        (
            "#080FEstelle, Joshua...\x01",
            "I'm home.\x02\x03",

            "It's been quite a while...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(3230, 700, -1570, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3510, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 0, 380, 0)
    SetChrPos(0x102, -1160, 0, -890, 0)
    SetChrPos(0x0, -400, 0, -2790, 0)
    SetChrPos(0x1, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_6FD4():

        label("loc_6FD4")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_6FD4")

    QueueWorkItem2(0x0, 3, lambda_6FD4)

    def lambda_6FE5():

        label("loc_6FE5")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_6FE5")

    QueueWorkItem2(0x1, 3, lambda_6FE5)

    def lambda_6FF6():

        label("loc_6FF6")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_6FF6")

    QueueWorkItem2(0x2, 3, lambda_6FF6)

    def lambda_7007():

        label("loc_7007")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_7007")

    QueueWorkItem2(0x3, 3, lambda_7007)
    OP_0D()

    ChrTalk(    #140
        0x101,
        "#2P#580FD-D-D...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #141
        0x101,
        "#2P#005F#5SDAD?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_705B():
        OP_6D(190, 0, -590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_705B)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0x924, 0x0, 0xFFFFFD76, 0x7D0, 0x1770)
    OP_22(0xA4, 0x0, 0x64)
    SetChrSubChip(0x11, 10)
    Sleep(200)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0x294, 0x0, 0xFFFFFD44, 0x1F4, 0x7D0)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #142
        0x11,
        (
            "#085FFor all your extensive training,\x01",
            "you're still so very naive.\x02\x03",

            "#080FEven so, I suppose I'll give you\x01",
            "a passing grade...this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#005FEnough! Don't give me that!\x02\x03",

            "What are you even doing here?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BC0")

    label("loc_719C")

    OP_A3(0x7)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_71E7():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_71E7)

    def lambda_71F9():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0xC8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_71F9)

    def lambda_720B():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0xA0, 0x384)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_720B)

    def lambda_721D():
        OP_9F(0x1D, 0xFF, 0xFF, 0xFF, 0x78, 0x44C)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_721D)

    def lambda_722F():
        OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x50, 0x514)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_722F)

    def lambda_7241():
        OP_9F(0x1F, 0xFF, 0xFF, 0xFF, 0x28, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_7241)
    OP_43(0x11, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1B, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1C, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1D, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x1F, 0x0, 0x0, 0x19)

    def lambda_7296():
        OP_6D(2340, 1150, 10, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7296)

    def lambda_72AE():
        OP_67(0, 8830, -30160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_72AE)

    def lambda_72C6():
        OP_6B(640, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_72C6)

    def lambda_72D6():
        OP_6C(82000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_72D6)

    def lambda_72E6():
        OP_6E(602, 4000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_72E6)
    OP_A6(0x7)
    OP_A3(0x7)
    OP_22(0x84, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0xFF, 4650, 2500, 3240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #144 op#A op#5
        0x11,
        "#10AHah!\x05\x02",
    )

    OP_20(0x5DC)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    TurnDirection(0x101, 0x17, 0)
    TurnDirection(0x102, 0x17, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_737F")
    SetChrChipByIndex(0x103, 14)
    TurnDirection(0x103, 0x17, 0)

    label("loc_737F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7399")
    SetChrChipByIndex(0x104, 16)
    TurnDirection(0x104, 0x17, 0)

    label("loc_7399")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73B3")
    SetChrChipByIndex(0x106, 20)
    TurnDirection(0x106, 0x17, 0)

    label("loc_73B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73CD")
    SetChrChipByIndex(0x105, 18)
    TurnDirection(0x105, 0x17, 0)

    label("loc_73CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73E7")
    SetChrChipByIndex(0x107, 22)
    TurnDirection(0x107, 0x17, 0)

    label("loc_73E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7401")
    SetChrChipByIndex(0x108, 24)
    TurnDirection(0x108, 0x17, 0)

    label("loc_7401")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x9, 0x20)
    OP_B0(0x9, 0xD)
    OP_6F(0x9, 646)
    OP_70(0x9, 0x2AC)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_73(0x9)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 685)
    OP_70(0x9, 0x2BF)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #145
        0x101,
        "#004F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        "#014F#2PIt can't be...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x11, 13)
    TurnDirection(0x11, 0x101, 800)
    OP_21()
    OP_1D(0x2B)
    Sleep(500)

    ChrTalk(    #147
        0x11,
        "#5P#087FNow! Finish him off!!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_31(0x0, 0xFA, 0x1)
    OP_31(0x1, 0xFA, 0x1)
    OP_31(0x2, 0xFA, 0x1)
    OP_31(0x3, 0xFA, 0x1)
    OP_31(0x4, 0xFA, 0x1)
    OP_31(0x5, 0xFA, 0x1)
    OP_31(0x6, 0xFA, 0x1)
    OP_31(0x7, 0xFA, 0x1)
    OP_31(0x0, 0x5, 0xC8)
    OP_31(0x1, 0x5, 0xC8)
    OP_31(0x2, 0x5, 0xC8)
    OP_31(0x3, 0x5, 0xC8)
    OP_31(0x4, 0x5, 0xC8)
    OP_31(0x5, 0x5, 0xC8)
    OP_31(0x6, 0x5, 0xC8)
    OP_31(0x7, 0x5, 0xC8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7541")
    RemoveParty(0x2, 0xFF)
    AddParty(0x2, 0xFF)

    label("loc_7541")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7555")
    RemoveParty(0x3, 0xFF)
    AddParty(0x3, 0xFF)

    label("loc_7555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7569")
    RemoveParty(0x5, 0xFF)
    AddParty(0x5, 0xFF)

    label("loc_7569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_757D")
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xFF)

    label("loc_757D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7591")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF)

    label("loc_7591")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75A5")
    RemoveParty(0x7, 0xFF)
    AddParty(0x7, 0xFF)

    label("loc_75A5")

    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75C2")
    SetChrChipByIndex(0x103, 14)

    label("loc_75C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75D8")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_75D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75EB")
    SetChrChipByIndex(0x106, 20)

    label("loc_75EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75FE")
    SetChrChipByIndex(0x105, 18)

    label("loc_75FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7611")
    SetChrChipByIndex(0x107, 22)

    label("loc_7611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7624")
    SetChrChipByIndex(0x108, 24)

    label("loc_7624")

    SetChrPos(0x101, -2910, 0, -3850, 47)
    SetChrPos(0x102, -1510, 0, -3240, 47)
    SetChrPos(0x2, -4710, 0, 610, 127)
    SetChrPos(0x3, -5270, 0, -1970, 111)
    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    OP_83(0x19, 0x0)
    Battle(0x3B3, 0x10000A, 0x0, 0x0, 0xFF)
    OP_83(0x19, 0x1)
    EventBegin(0x0)
    RemoveParty(0x0, 0xFF)
    RemoveParty(0x1, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x17, 0x9)
    OP_72(0x9, 0x20)
    OP_72(0x9, 0x4)
    OP_6F(0x9, 843)
    OP_70(0x9, 0x34B)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    SetChrPos(0x11, 3450, 0, 6350, 209)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3590, 1600, 5110, 0)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 32)
    SetChrPos(0x10, 4790, 0, 6510, 0)
    OP_6D(21280, 0, -530, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1170, 0, 380, 0)
    SetChrPos(0x102, -1160, 0, -890, 0)
    SetChrPos(0x0, -400, 0, -2790, 0)
    SetChrPos(0x1, 2090, 0, -3410, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7840")
    SetChrChipByIndex(0x103, 14)

    label("loc_7840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7856")
    SetChrChipByIndex(0x104, 16)
    OP_A2(0x6F5)

    label("loc_7856")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7869")
    SetChrChipByIndex(0x106, 20)

    label("loc_7869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_787C")
    SetChrChipByIndex(0x105, 18)

    label("loc_787C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_788F")
    SetChrChipByIndex(0x107, 22)

    label("loc_788F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78A2")
    SetChrChipByIndex(0x108, 24)

    label("loc_78A2")

    TurnDirection(0x0, 0x17, 0)
    TurnDirection(0x1, 0x17, 0)
    TurnDirection(0x2, 0x17, 0)
    TurnDirection(0x3, 0x17, 0)
    FadeToBright(2000, 0)
    OP_6D(11670, 0, 850, 4000)
    Fade(1000)
    OP_6D(3700, 0, -1810, 0)
    OP_67(0, 7990, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_83(0x19, 0x1)

    ChrTalk(    #148
        0x101,
        (
            "#007FWe...\x01",
            "We won...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x11,
        "#2PThank you for your help, everyone.\x02",
    )

    CloseMessageWindow()
    OP_1D(0x1)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_7993():
        OP_6D(190, 0, -590, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7993)

    def lambda_79AB():
        OP_6B(3300, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_79AB)

    def lambda_79BB():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_79BB)

    def lambda_79C9():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_79C9)

    def lambda_79D7():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_79D7)

    def lambda_79E5():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_79E5)
    Sleep(1500)

    def lambda_79F8():

        label("loc_79F8")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_79F8")

    QueueWorkItem2(0x0, 3, lambda_79F8)

    def lambda_7A09():

        label("loc_7A09")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_7A09")

    QueueWorkItem2(0x1, 3, lambda_7A09)

    def lambda_7A1A():

        label("loc_7A1A")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_7A1A")

    QueueWorkItem2(0x2, 3, lambda_7A1A)

    def lambda_7A2B():

        label("loc_7A2B")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_7A2B")

    QueueWorkItem2(0x3, 3, lambda_7A2B)

    def lambda_7A3C():
        OP_8E(0x11, 0x2BC, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7A3C)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 270, 400)
    Sleep(500)

    ChrTalk(    #150
        0x11,
        (
            "#080FEstelle, Joshua...\x01",
            "I'm home.\x02\x03",

            "It's been quite a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#580FD-D-D...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #152
        0x101,
        "#6P#005F#5SDAD?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #153
        0x11,
        (
            "#085FYou've still got a long way\x01",
            "to go, but I can see that\x01",
            "your training has paid off.\x02\x03",

            "#080FI suppose I'll give you a\x01",
            "passing grade, this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#005FEnough! Don't give me that!\x02\x03",

            "What are you even doing here?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BC0")


    ChrTalk(    #155
        0x11,
        (
            "#084FWhat, indeed...\x02\x03",

            "#081FPerhaps I just wanted\x01",
            "to see the ending?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#509FWhat do you mean by 'ending'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x102,
        (
            "#019FHa ha... I see you're just\x01",
            "as cheerful as ever, Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x11,
        (
            "#080FHuh... Well, you look like\x01",
            "you've gotten taller...\x02\x03",

            "Has looking after Estelle been\x01",
            "as difficult as I think it has?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#009FWhat's that supposed to mean?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        (
            "#019FDepends on the day, really.\x02\x03",

            "#010FBut to be fair, she looks\x01",
            "out for me, too.\x02\x03",

            "It balances out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x11,
        (
            "#080FGood, good... It sounds like it's\x01",
            "been a worthwhile journey.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7DCC():
        OP_6D(720, 0, -2650, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_7DCC)
    WaitChrThread(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FE2")

    ChrTalk(    #162
        0x103,
        (
            "#021FMaster...\x01",
            "It's good to see you again!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #163
        0x11,
        (
            "#080FLikewise, Scherazard.\x02\x03",

            "I assume you've been very\x01",
            "busy in my absence...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        (
            "#027FYes, sir.\x02\x03",

            "But it's been good training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x11,
        (
            "#081FI'd expect no less of\x01",
            "my star pupil.\x02\x03",

            "#080FHow would you rate Estelle\x01",
            "and Joshua's progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        (
            "#020FI think that they're ready\x01",
            "to advance beyond the rank\x01",
            "of apprentice.\x02\x03",

            "#021FThough they might disagree. They seem\x01",
            "to have this humble streak in them.\x01",
            "Not sure where they got it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8238")

    ChrTalk(    #167
        0x104,
        (
            "#030FHm... It's a pleasure to make\x01",
            "your acquaintance, Cassius Bright.\x02\x03",

            "My name is Olivier. I am\x01",
            "a traveling musician from\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x104, 400)

    ChrTalk(    #168
        0x11,
        (
            "#084FIs that so...?\x02\x03",

            "#080FWhen time permits, I should\x01",
            "like to discuss a few things\x01",
            "with you.\x02\x03",

            "In the meantime, please know that\x01",
            "you have my thanks for assisting\x01",
            "my son and daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x104,
        (
            "#031FThink nothing of it. It's been\x01",
            "a worthwhile pursuit.\x02\x03",

            "#030FNevertheless, I am impressed\x01",
            "by your skill.\x02\x03",

            "It is rare that one gets to\x01",
            "watch a living legend at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x11,
        (
            "#080FHa ha... Well, I'm still\x01",
            "working on it, myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8238")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8456")

    ChrTalk(    #171
        0x106,
        (
            "#054FHey, old man!\x02\x03",

            "Was all this supposed to be\x01",
            "some kind of big game?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #172
        0x11,
        (
            "#084FAhh, the bad seed. The professor\x01",
            "told me you were here.\x02\x03",

            "#081FAll things considered, you've\x01",
            "performed admirably.\x02\x03",

            "I'm impressed, really...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x106,
        (
            "#057FDon't talk to me like\x01",
            "I'm some kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x11,
        (
            "#080FMerely a joke.\x02\x03",

            "I'm to understand that you're the one\x01",
            "responsible for the thorough investigation\x01",
            "into the Special Ops group.\x02\x03",

            "I thank you for all the assistance\x01",
            "you've provided my children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x106,
        "#055FUhh... No problem.\x02",
    )

    CloseMessageWindow()

    label("loc_8456")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85FC")

    ChrTalk(    #176
        0x107,
        (
            "#560FMister Cassius...it's sure\x01",
            "been a long time, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x107, 400)

    ChrTalk(    #177
        0x11,
        (
            "#080FHello, Tita.\x02\x03",

            "It's only been a year, but\x01",
            "you've grown so much.\x02\x03",

            "I trust you've gotten along\x01",
            "with Estelle and Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x107,
        (
            "#067FY-Yes, sir.\x02\x03",

            "They said that I could\x01",
            "be their little sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x11,
        (
            "#081FHa ha... Excellent, excellent.\x01",
            "Welcome to the family!\x02\x03",

            "I leave my ever-so-flighty\x01",
            "daughter to you. Keep her safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87F4")

    ChrTalk(    #180
        0x105,
        (
            "#048FIt's been quite a long\x01",
            "time, Mr. Cassius...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x105, 400)

    ChrTalk(    #181
        0x11,
        (
            "#080FYes, Your Highness...\x01",
            "Roughly six months, I believe.\x02\x03",

            "I'd heard of your imprisonment,\x01",
            "but I am glad to see you well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x105,
        (
            "#041FHa ha... Well, you can thank\x01",
            "Estelle and company for\x01",
            "coming to my rescue.\x02\x03",

            "#040FBy the way, Estelle and Joshua\x01",
            "were in this year's play at\x01",
            "the royal academy.\x02\x03",

            "I wish you could have been\x01",
            "there to see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x11,
        (
            "#084FOh, really...? I do wish\x01",
            "I could have been there\x01",
            "for THAT.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A46")

    ChrTalk(    #184
        0x108,
        (
            "#070FHello, sir. I extend to you\x01",
            "a belated 'welcome home.'\x02\x03",

            "We've been very anxiously awaiting\x01",
            "your arrival.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x11, 0x3CA, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    TurnDirection(0x11, 0x108, 400)

    ChrTalk(    #185
        0x11,
        (
            "#082FForgive me, Zin.\x02\x03",

            "I'm so sorry to have called you\x01",
            "all the way from the Republic.\x02\x03",

            "I just...had a feeling something\x01",
            "big was going to happen, and wanted\x01",
            "to make sure Liberl was ready for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x108,
        (
            "#071FIt was no trouble, sir.\x02\x03",

            "After all...now we're even, right?\x02\x03",

            "#070FAnd thanks to your request, I got to\x01",
            "meet your kids, and see just how skilled\x01",
            "they really are!\x02\x03",

            "All in all, I had fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x11,
        "#080FI'm relieved to hear you say that.\x02",
    )

    CloseMessageWindow()

    label("loc_8A46")


    ChrTalk(    #188
        0x101,
        (
            "#005FThis really isn't the\x01",
            "time for chit-chat!\x02\x03",

            "#007FI swear, you just pop up out of nowhere\x01",
            "at just the right moment to make THE\x01",
            "most dramatic entrance you can...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10, 0xFF)
    SetChrChipByIndex(0x10, 31)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, 2670, 0, 6490, 180)
    SetChrPos(0xE, -1860, 0, -15040, 0)

    ChrTalk(    #189
        0xE,
        (
            "#3PAhhh... Well, it seems like\x01",
            "everything's back to normal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B66():
        OP_6D(1200, 0, -3730, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8B66)
    ClearChrFlags(0xE, 0x80)

    def lambda_8B83():
        OP_8E(0xFE, 0x406, 0x0, 0xFFFFED36, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8B83)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB9")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 5)
    Jump("loc_8BEF")

    label("loc_8BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BCC")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 5)
    Jump("loc_8BEF")

    label("loc_8BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BDF")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 5)
    Jump("loc_8BEF")

    label("loc_8BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BEF")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 5)

    label("loc_8BEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C10")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 1)
    Jump("loc_8C46")

    label("loc_8C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C23")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 1)
    Jump("loc_8C46")

    label("loc_8C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C36")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 1)
    Jump("loc_8C46")

    label("loc_8C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C46")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 1)

    label("loc_8C46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C67")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 0)
    Jump("loc_8C9D")

    label("loc_8C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C7A")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 0)
    Jump("loc_8C9D")

    label("loc_8C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8D")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 0)
    Jump("loc_8C9D")

    label("loc_8C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C9D")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 0)

    label("loc_8C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CBE")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 2)
    Jump("loc_8CF4")

    label("loc_8CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD1")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 2)
    Jump("loc_8CF4")

    label("loc_8CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE4")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 2)
    Jump("loc_8CF4")

    label("loc_8CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF4")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 2)

    label("loc_8CF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D15")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 3)
    Jump("loc_8D4B")

    label("loc_8D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D28")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 3)
    Jump("loc_8D4B")

    label("loc_8D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3B")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 3)
    Jump("loc_8D4B")

    label("loc_8D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D4B")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 3)

    label("loc_8D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6C")
    OP_A2(0xC)
    SetChrChipByIndex(0xD, 4)
    Jump("loc_8DA2")

    label("loc_8D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7F")
    OP_A2(0xD)
    SetChrChipByIndex(0x8, 4)
    Jump("loc_8DA2")

    label("loc_8D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D92")
    OP_A2(0xE)
    SetChrChipByIndex(0x9, 4)
    Jump("loc_8DA2")

    label("loc_8D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DA2")
    OP_A2(0xF)
    SetChrChipByIndex(0xA, 4)

    label("loc_8DA2")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 110, 0, -17400, 0)

    def lambda_8DBE():
        OP_8E(0xFE, 0xA8C, 0x0, 0xFFFFE2A0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8DBE)
    Sleep(200)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2180, 0, -17210, 0)

    def lambda_8DF4():
        OP_8E(0xFE, 0xFFFFFB6E, 0x0, 0xFFFFE23C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8DF4)
    Sleep(200)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 0, -17240, 0)

    def lambda_8E2A():
        OP_8E(0xFE, 0xF0, 0x0, 0xFFFFDD46, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E2A)
    Sleep(200)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -720, 0, -17320, 0)

    def lambda_8E60():
        OP_8E(0xFE, 0x55A, 0x0, 0xFFFFDE0E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8E60)
    Sleep(1000)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_8E90():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_8E90)

    def lambda_8E9E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8E9E)

    def lambda_8EAC():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_8EAC)

    def lambda_8EBA():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_8EBA)

    def lambda_8EC8():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_8EC8)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #190
        0x11,
        (
            "#080FProfessor! There you are! You're a bit\x01",
            "late to the party, though, I'm afraid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xE,
        (
            "#102F#4PWell, after you went on ahead,\x01",
            "we were surrounded by a horde\x01",
            "of those mechanized monsters.\x02\x03",

            "We managed to keep them at bay\x01",
            "somehow or another, though...\x01",
            "and here we are!\x02\x03",

            "#101FIn any case, it seems like all\x01",
            "affairs have been set in order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x11,
        (
            "#085FYes...\x02\x03",

            "#080FMuch remains to be done, but this,\x01",
            "at least, has been resolved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#505FB-But...\x02\x03",

            "Isn't the Intelligence Division's\x01",
            "battalion getting close to the\x01",
            "castle by now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        (
            "#013FNo doubt...\x01",
            "Along with patrol ships.\x02\x03",

            "#012FDad, did you check out the\x01",
            "situation on the surface\x01",
            "before coming down here?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 315, 400)

    def lambda_917A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_917A)

    def lambda_9188():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9188)

    ChrTalk(    #195
        0x11,
        (
            "#080F#6PYes, and you've no need\x01",
            "to worry about that.\x02\x03",

            "General Morgan said that he\x01",
            "has the situation under control.\x02\x03",

            "And with Cid's help, this craziness\x01",
            "will be quelled in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#005FWh-WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x10,
        (
            "#2PHa ha... I see...\x02\x03",

            "So you took care of them on your\x01",
            "way here, then...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_92C1():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_92C1)

    def lambda_92CF():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_92CF)

    def lambda_92DD():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_92DD)

    def lambda_92EB():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_92EB)

    def lambda_92F9():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_92F9)
    OP_20(0x5DC)

    def lambda_930C():
        OP_6D(2300, 0, 2700, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_930C)
    OP_6C(44000, 4000)
    OP_21()
    OP_1D(0x53)
    Sleep(400)

    ChrTalk(    #198
        0x11,
        "#082F#2PSo, you're awake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x10,
        (
            "#3P#118FWe'd placed General Morgan\x01",
            "under strict observation...\x02\x03",

            "Cid couldn't risk defying us because\x01",
            "we held his family hostage...\x02\x03",

            "Yet you freed both from our grasp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x11,
        (
            "#085F#2PMmm, I suppose I did.\x02\x03",

            "#080FHowever, Richard...\x01",
            "That's about all I've done.\x02\x03",

            "Even had I not returned, they\x01",
            "would have been able to handle\x01",
            "it themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x10,
        (
            "#3P#115FNo...you're wrong.\x01",
            "You're a hero...\x02\x03",

            "#116FYou left the military...left all of us...\x01",
            "What were we supposed to do...?\x02\x03",

            "I didn't think we could\x01",
            "survive another invasion...\x02\x03",

            "So...I had to find something\x01",
            "else we could rely on.\x02\x03",

            "#118FIf you had stayed in the service,\x01",
            "it never would have come to this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x11,
        "#082F#2P...\x02",
    )

    CloseMessageWindow()

    def lambda_95F2():
        OP_6D(3460, 0, 7840, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_95F2)

    def lambda_960A():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_960A)
    OP_8E(0x11, 0x898, 0x0, 0xF14, 0x7D0, 0x0)
    Sleep(500)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 35)
    SetChrSubChip(0x11, 0)
    OP_8E(0x11, 0x988, 0x0, 0x1568, 0x2710, 0x0)
    SetChrSubChip(0x11, 1)

    def lambda_965B():
        OP_8E(0x11, 0xA28, 0x0, 0x1928, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_965B)
    OP_22(0x1FB, 0x0, 0x64)
    Sleep(50)

    def lambda_9680():
        OP_8E(0x11, 0xA28, 0x0, 0x1928, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_9680)
    OP_22(0x229, 0x0, 0x64)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    OP_96(0x10, 0xADC, 0x0, 0x2486, 0x258, 0xBB8)
    OP_22(0x22A, 0x0, 0x64)
    SetChrChipByIndex(0x10, 32)
    OP_96(0x10, 0xADC, 0x0, 0x285A, 0x12C, 0x3E8)
    Sleep(1000)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    Sleep(300)

    def lambda_96F6():
        OP_99(0x10, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_96F6)
    OP_9E(0x10, 0x14, 0x0, 0x190, 0x1770)

    ChrTalk(    #203
        0x10,
        "#3P#117FUngh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x11,
        (
            "#087F#4PStop being such a child, Richard!\x02\x03",

            "You're the one who made the\x01",
            "mistake of never letting go of\x01",
            "the delusions you had about me!\x02\x03",

            "For all your schemes, why\x01",
            "could you never stand on\x01",
            "your own two feet?!\x02\x03",

            "I thought it would be okay to retire!\x01",
            "I thought I could comfortably leave\x01",
            "the army in your care!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x10,
        "#3P#113FC-Colonel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        (
            "#086F#4PI'm not an icon to be hailed.\x02\x03",

            "A decade ago, you and General\x01",
            "Morgan helped me, and we were\x01",
            "victorious.\x02\x03",

            "But...I'm no more than a man who's run\x01",
            "away from reality without protecting\x01",
            "the things that are important to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x10,
        "#3P#113F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#003FDad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x11,
        (
            "#085F#4PBut I have no intention of running any more.\x02\x03",

            "#082FThat's why I expect the same from you, Richard.\x02\x03",

            "I want you to think about this whole mess. Think\x01",
            "about what you did wrong, and how you can atone\x01",
            "for it. You'll have plenty of time, believe me...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #210
        "\x07\x05And so, the Intelligence Division's planned coup d'etat was thwarted.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #211
        (
            "\x07\x05General Morgan and Major Cid organized the military authorities to keep\x01",
            "the chaos to a minimum...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #212
        "\x07\x05And the conspirators in the Intelligence Division were arrested, one by one.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #213
        "\x07\x05One week later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    ClearMapFlags(0x2000000)
    OP_20(0x7D0)
    OP_21()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_4CE9 end

    def Function_10_9BD5(): pass

    label("Function_10_9BD5")

    OP_66(0x1)

    def lambda_9BDE():
        OP_6D(4690, 2000, -1350, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BDE)

    def lambda_9BF6():
        OP_67(0, 2630, -27100, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BF6)

    def lambda_9C0E():
        OP_6C(85000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C0E)
    OP_7C(0x0, 0x33, 0xBB8, 0x1388)
    OP_B0(0x9, 0x14)
    OP_6F(0x9, 296)
    OP_70(0x9, 0x150)
    OP_73(0x9)
    OP_22(0xF4, 0x0, 0x64)
    OP_B0(0x9, 0x19)
    OP_6F(0x9, 337)
    OP_70(0x9, 0x197)
    Sleep(100)
    OP_7C(0x0, 0x64, 0xBB8, 0x1770)

    def lambda_9C71():
        OP_6B(1110, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C71)
    OP_73(0x9)
    OP_B0(0x9, 0x16)
    OP_6F(0x9, 408)
    OP_70(0x9, 0x1BD)
    OP_73(0x9)
    OP_B0(0x9, 0x13)
    OP_6F(0x9, 446)
    OP_70(0x9, 0x1E0)
    OP_73(0x9)
    OP_B0(0x9, 0x10)
    OP_6F(0x9, 481)
    OP_70(0x9, 0x1EE)
    OP_73(0x9)

    def lambda_9CC3():
        OP_6B(1300, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9CC3)
    OP_71(0x9, 0x20)
    OP_B0(0x9, 0xF)
    OP_6F(0x9, 50)
    OP_70(0x9, 0x45)
    Return()

    # Function_10_9BD5 end

    def Function_11_9CE5(): pass

    label("Function_11_9CE5")

    OP_8F(0xFE, 0xAA0, 0x0, 0x83E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 28)
    Sleep(100)

    def lambda_9D13():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D13)
    OP_8F(0xFE, 0x12D4, 0x7D0, 0x316, 0x2710, 0x0)
    Return()

    # Function_11_9CE5 end

    def Function_12_9D32(): pass

    label("Function_12_9D32")


    def lambda_9D38():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D38)
    OP_96(0xFE, 0x10A4, 0x0, 0xB72, 0x12C, 0x2710)

    def lambda_9D5F():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D5F)
    OP_8F(0xFE, 0x12D4, 0x7D0, 0x316, 0x2710, 0x0)
    Return()

    # Function_12_9D32 end

    def Function_13_9D7E(): pass

    label("Function_13_9D7E")


    def lambda_9D84():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D84)
    OP_96(0xFE, 0xCEE, 0x0, 0x6CC, 0x12C, 0x1F40)
    Return()

    # Function_13_9D7E end

    def Function_14_9DA6(): pass

    label("Function_14_9DA6")

    Sleep(250)

    def lambda_9DB1():
        OP_96(0xFE, 0x582, 0x0, 0xE88, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DB1)
    Sleep(600)

    def lambda_9DD4():
        OP_96(0xFE, 0xA0A, 0x0, 0x1112, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DD4)
    Sleep(300)

    def lambda_9DF7():
        OP_96(0xFE, 0xD02, 0xB4A, 0xF78, 0xFA0, 0x2710)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DF7)
    Return()

    # Function_14_9DA6 end

    def Function_15_9E10(): pass

    label("Function_15_9E10")

    SetChrFlags(0xFE, 0x4)
    WaitChrThread(0xFE, 0x1)

    def lambda_9E20():
        OP_99(0xFE, 0x0, 0x1, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E20)
    OP_96(0xFE, 0xD16, 0x992, 0x550, 0x3E8, 0x1770)
    Return()

    # Function_15_9E10 end

    def Function_16_9E42(): pass

    label("Function_16_9E42")


    def lambda_9E48():
        OP_99(0xFE, 0x5, 0xB, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E48)
    OP_96(0xFE, 0x8FC, 0x0, 0xD66, 0x12C, 0x1770)
    Return()

    # Function_16_9E42 end

    def Function_17_9E6A(): pass

    label("Function_17_9E6A")

    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(200)
    SetChrPos(0x1A, 5140, 2450, 340, 0)
    PlayEffect(0x3, 0xFF, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Return()

    # Function_17_9E6A end

    def Function_18_9F47(): pass

    label("Function_18_9F47")

    SetChrSubChip(0xFE, 11)
    SetChrPos(0xFE, 740, 0, 1920, 46)
    TurnDirection(0xFE, 0x17, 400)
    OP_96(0xFE, 0x1180, 0x0, 0x2DA, 0x1F4, 0xFA0)
    Sleep(50)

    def lambda_9F86():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xBB8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F86)
    OP_99(0xFE, 0x0, 0x2, 0x7D0)
    SetChrFlags(0xFE, 0x2)

    def lambda_9FB2():

        label("loc_9FB2")

        OP_99(0xFE, 0x20, 0x31, 0xDAC)
        OP_48()
        Jump("loc_9FB2")

    QueueWorkItem2(0xFE, 2, lambda_9FB2)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x2)
    TurnDirection(0xFE, 0x17, 0)

    def lambda_9FDA():
        OP_99(0xFE, 0x5, 0xB, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9FDA)
    Sleep(1000)
    OP_96(0xFE, 0x30C, 0x0, 0x11F8, 0x1F4, 0x1770)
    TurnDirection(0xFE, 0x17, 0)
    Return()

    # Function_18_9F47 end

    def Function_19_A008(): pass

    label("Function_19_A008")

    SetChrChipByIndex(0xFE, 45)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 100, -600, 3150, 0)

    def lambda_A03D():

        label("loc_A03D")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_A03D")

    QueueWorkItem2(0xFE, 1, lambda_A03D)
    OP_96(0xFE, 0xFFFFF01A, 0xFFFFFDA8, 0xFDB, 0xFA0, 0xFA0)
    OP_44(0xFE, 0x1)
    SetChrSubChip(0xFE, 8)
    Return()

    # Function_19_A008 end

    def Function_20_A06B(): pass

    label("Function_20_A06B")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3590, 1600, 5110, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    OP_96(0x10, 0x11A8, 0x0, 0x17CA, 0x7D0, 0xFA0)
    SetChrChipByIndex(0x10, 32)
    OP_96(0x10, 0x12B6, 0x0, 0x196E, 0x190, 0xFA0)
    OP_95(0x10, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
    Return()

    # Function_20_A06B end

    def Function_21_A0D6(): pass

    label("Function_21_A0D6")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 1)
    SetChrPos(0xFE, 260, 0, -8970, 154)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 1)
    OP_8E(0xFE, 0x910, 0x0, 0xFFFFF916, 0x2710, 0x0)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A138")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x10)

    label("loc_A138")

    OP_96(0xFE, 0x1180, 0x71C, 0xD0C, 0x76C, 0x3E8)
    OP_A2(0x7)
    SetChrSubChip(0xFE, 1)

    def lambda_A15D():
        OP_8C(0xFE, 77, 400)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A15D)
    OP_96(0xFE, 0x6E0, 0x0, 0xFFFFFC2C, 0xC8, 0xBB8)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 10)
    Return()

    # Function_21_A0D6 end

    def Function_22_A187(): pass

    label("Function_22_A187")

    SetChrSubChip(0xFE, 4)

    def lambda_A192():
        OP_8C(0xFE, 170, 1200)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A192)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1AA")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x12)

    label("loc_A1AA")

    OP_96(0xFE, 0xE7E, 0x0, 0xFFFFF574, 0x1F4, 0x1B58)
    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 90, 1200)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 5)
    OP_8C(0xFE, 135, 1200)
    Sleep(100)
    OP_A2(0x7)
    OP_8C(0xFE, 0, 1200)
    OP_8C(0xFE, 90, 400)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_22_A187 end

    def Function_23_A1FB(): pass

    label("Function_23_A1FB")

    SetChrSubChip(0xFE, 11)

    def lambda_A206():
        OP_8C(0xFE, 90, 800)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_A206)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21E")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x13)

    label("loc_A21E")

    OP_96(0xFE, 0x163A, 0x11F8, 0xFFFFF7D6, 0x1770, 0x1B58)
    SetChrSubChip(0xFE, 12)
    OP_A6(0x7)
    Sleep(250)
    OP_8F(0xFE, 0x152C, 0x8B6, 0xFFFFF61E, 0x3A98, 0x0)
    Sleep(500)
    SetChrSubChip(0xFE, 11)
    OP_96(0xFE, 0x564, 0x0, 0xFFFFFC22, 0x1F4, 0xFA0)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_23_A1FB end

    def Function_24_A27D(): pass

    label("Function_24_A27D")

    SetChrSubChip(0xFE, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A292")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x14)

    label("loc_A292")

    OP_96(0xFE, 0x1DB0, 0x6C2, 0xFFFFFDB2, 0xBB8, 0x2EE0)
    SetChrSubChip(0xFE, 6)
    Return()

    # Function_24_A27D end

    def Function_25_A2AF(): pass

    label("Function_25_A2AF")

    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 1)
    SetChrPos(0xFE, 260, 0, -8970, 154)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrSubChip(0xFE, 1)
    OP_8E(0xFE, 0x910, 0x0, 0xFFFFF916, 0x2710, 0x0)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A311")
    OP_22(0xA3, 0x0, 0x64)
    OP_A2(0x10)

    label("loc_A311")

    OP_96(0xFE, 0x1180, 0x71C, 0xD0C, 0x76C, 0x3E8)
    OP_A2(0x7)
    SetChrSubChip(0xFE, 1)

    def lambda_A336():
        OP_8C(0xFE, 77, 400)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A336)
    OP_96(0xFE, 0xB54, 0x0, 0x161C, 0xC8, 0xBB8)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 10)
    Return()

    # Function_25_A2AF end

    SaveToFile()

Try(main)

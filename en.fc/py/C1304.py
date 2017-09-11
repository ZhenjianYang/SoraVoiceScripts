from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1304   ._SN',
        MapName             = 'Bose',
        Location            = 'C1304.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        'Captain Grandt',                       # 9
        'Trino',                                # 10
        'Crew Member Clare',                    # 11
        'Parker',                               # 12
        'Colton',                               # 13
        'Timon',                                # 14
        'Duncan',                               # 15
        'Finel',                                # 16
        'Blaue',                                # 17
        'Prometheus',                           # 18
        'Lenore',                               # 19
        'Legaro',                               # 20
        'Sylvie',                               # 21
        'Burrell',                              # 22
        'Ruvie',                                # 23
        'Atget',                                # 24
        'Sky Bandit Aaron',                     # 25
        'Sky Bandit Rosco',                     # 26
        'Sky Bandit Lonnie',                    # 27
        'Sky Bandit Dino',                      # 28
        'Sky Bandit',                           # 29
        'Sky Bandit',                           # 30
        'Sky Bandit',                           # 31
        'Sky Bandit',                           # 32
        'Sky Bandit',                           # 33
        'Sky Bandit',                           # 34
        'Sky Bandit',                           # 35
        'Sky Bandit',                           # 36
        'Target Camera',                        # 37
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01440 ._CH',             # 00
        'ED6_DT07/CH01200 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01290 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01100 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT07/CH01220 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01070 ._CH',             # 0D
        'ED6_DT07/CH01380 ._CH',             # 0E
        'ED6_DT07/CH00360 ._CH',             # 0F
        'ED6_DT07/CH00364 ._CH',             # 10
        'ED6_DT07/CH00361 ._CH',             # 11
        'ED6_DT07/CH00363 ._CH',             # 12
        'ED6_DT07/CH00122 ._CH',             # 13
        'ED6_DT07/CH00100 ._CH',             # 14
        'ED6_DT07/CH00101 ._CH',             # 15
        'ED6_DT07/CH00110 ._CH',             # 16
        'ED6_DT07/CH00111 ._CH',             # 17
        'ED6_DT07/CH00120 ._CH',             # 18
        'ED6_DT07/CH00121 ._CH',             # 19
        'ED6_DT07/CH00130 ._CH',             # 1A
        'ED6_DT07/CH00131 ._CH',             # 1B
        'ED6_DT06/CH20074 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT07/CH01440P._CP',             # 00
        'ED6_DT07/CH01200P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01290P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01100P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT07/CH01220P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01070P._CP',             # 0D
        'ED6_DT07/CH01380P._CP',             # 0E
        'ED6_DT07/CH00360P._CP',             # 0F
        'ED6_DT07/CH00364P._CP',             # 10
        'ED6_DT07/CH00361P._CP',             # 11
        'ED6_DT07/CH00363P._CP',             # 12
        'ED6_DT07/CH00122P._CP',             # 13
        'ED6_DT07/CH00100P._CP',             # 14
        'ED6_DT07/CH00101P._CP',             # 15
        'ED6_DT07/CH00110P._CP',             # 16
        'ED6_DT07/CH00111P._CP',             # 17
        'ED6_DT07/CH00120P._CP',             # 18
        'ED6_DT07/CH00121P._CP',             # 19
        'ED6_DT07/CH00130P._CP',             # 1A
        'ED6_DT07/CH00131P._CP',             # 1B
        'ED6_DT06/CH20074P._CP',             # 1C
    )

    DeclNpc(
        X                   = -51200,
        Z                   = 0,
        Y                   = -44970,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -44800,
        Z                   = 0,
        Y                   = -44500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -49400,
        Z                   = 0,
        Y                   = -44100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -52870,
        Z                   = 0,
        Y                   = -45150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -48530,
        Z                   = 0,
        Y                   = -45460,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -53480,
        Z                   = 0,
        Y                   = -43740,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -51250,
        Z                   = 0,
        Y                   = -43660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -49800,
        Z                   = 0,
        Y                   = -41400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -54600,
        Z                   = 0,
        Y                   = -40800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -56400,
        Z                   = 0,
        Y                   = -43000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -47800,
        Z                   = 0,
        Y                   = -42400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -45700,
        Z                   = 0,
        Y                   = -42960,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -45400,
        Z                   = 0,
        Y                   = -41900,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -57380,
        Z                   = 0,
        Y                   = -45290,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -51600,
        Z                   = 0,
        Y                   = -40500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -52100,
        Z                   = 0,
        Y                   = -40700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_532",          # 00, 0
        "Function_1_779",          # 01, 1
        "Function_2_77A",          # 02, 2
        "Function_3_902",          # 03, 3
        "Function_4_BDC",          # 04, 4
        "Function_5_D4B",          # 05, 5
        "Function_6_E48",          # 06, 6
        "Function_7_F2E",          # 07, 7
        "Function_8_1138",         # 08, 8
        "Function_9_1238",         # 09, 9
        "Function_10_1373",        # 0A, 10
        "Function_11_13FD",        # 0B, 11
        "Function_12_14C1",        # 0C, 12
        "Function_13_158F",        # 0D, 13
        "Function_14_1636",        # 0E, 14
        "Function_15_16E2",        # 0F, 15
        "Function_16_17ED",        # 10, 16
        "Function_17_18E8",        # 11, 17
        "Function_18_19CD",        # 12, 18
        "Function_19_1A6F",        # 13, 19
        "Function_20_2A39",        # 14, 20
    )


    def Function_0_532(): pass

    label("Function_0_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_540")
    OP_A3(0x3FA)
    Event(0, 19)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_54E")
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_54E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_562"),
        (102, "loc_66D"),
        (101, "loc_66D"),
        (SWITCH_DEFAULT, "loc_778"),
    )


    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, 10200, 0, -92518, 225)
    SetChrPos(0x19, 3520, 0, -93920, 35)
    SetChrPos(0x1C, 2640, 0, -91700, 4)
    SetChrPos(0x1D, 9860, 0, -97730, 260)
    SetChrPos(0x1E, 1950, 0, -97080, 217)
    SetChrPos(0x1F, 2350, 0, -98760, 140)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66A")

    Jump("loc_778")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, -54970, 0, -93490, 315)
    SetChrPos(0x19, -48920, 0, -91340, 53)
    SetChrPos(0x1C, -45150, 0, -93440, 163)
    SetChrPos(0x1D, -48280, 0, -97510, 119)
    SetChrPos(0x1E, -54960, 0, -97820, 86)
    SetChrPos(0x1F, -53760, 0, -91280, 172)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_775")

    Jump("loc_778")

    label("loc_778")

    Return()

    # Function_0_532 end

    def Function_1_779(): pass

    label("Function_1_779")

    Return()

    # Function_1_779 end

    def Function_2_77A(): pass

    label("Function_2_77A")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AA")
    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_8EC")

    label("loc_7AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3")
    OP_99(0xFE, 0x1, 0x7, 0x514)
    Jump("loc_8EC")

    label("loc_7C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC")
    OP_99(0xFE, 0x2, 0x7, 0x4E2)
    Jump("loc_8EC")

    label("loc_7DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F5")
    OP_99(0xFE, 0x3, 0x7, 0x4B0)
    Jump("loc_8EC")

    label("loc_7F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E")
    OP_99(0xFE, 0x4, 0x7, 0x47E)
    Jump("loc_8EC")

    label("loc_80E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_827")
    OP_99(0xFE, 0x5, 0x7, 0x44C)
    Jump("loc_8EC")

    label("loc_827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    OP_99(0xFE, 0x6, 0x7, 0x41A)
    Jump("loc_8EC")

    label("loc_840")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859")
    OP_99(0xFE, 0x0, 0x7, 0x54B)
    Jump("loc_8EC")

    label("loc_859")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_872")
    OP_99(0xFE, 0x1, 0x7, 0x519)
    Jump("loc_8EC")

    label("loc_872")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    OP_99(0xFE, 0x2, 0x7, 0x4E7)
    Jump("loc_8EC")

    label("loc_88B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4")
    OP_99(0xFE, 0x3, 0x7, 0x4B5)
    Jump("loc_8EC")

    label("loc_8A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")
    OP_99(0xFE, 0x4, 0x7, 0x483)
    Jump("loc_8EC")

    label("loc_8BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D6")
    OP_99(0xFE, 0x5, 0x7, 0x451)
    Jump("loc_8EC")

    label("loc_8D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    OP_99(0xFE, 0x6, 0x7, 0x41F)

    label("loc_8EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_901")
    OP_99(0xFE, 0x0, 0x7, 0x4B0)
    Jump("loc_8EC")

    label("loc_901")

    Return()

    # Function_2_77A end

    def Function_3_902(): pass

    label("Function_3_902")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    OP_A2(0x0)

    ChrTalk(    #0
        0x101,
        (
            "#006FThe sky bandits didn't happen to run\x01",
            "in here, did they, Captain Grandt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "No, but I did happen to hear a bunch\x01",
            "of loud voices and footsteps coming\x01",
            "from outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "It sounds to me like they might\x01",
            "have rushed up the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#012FEstelle, they're going to try to\x01",
            "escape in their airship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#002FRight, we've got to hurry after them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#012FPlease forgive us, Captain, but we'll\x01",
            "need you to sit tight a little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "No worries, you kids just\x01",
            "be careful out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_B08")


    ChrTalk(    #7
        0xFE,
        (
            "It seems like the sky bandits\x01",
            "took off up the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_B54")

    Jump("loc_BD8")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #9
        0xFE,
        (
            "I'm pretty sure the sky bandit\x01",
            "leaders are somewhere on the\x01",
            "lowest level of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Be careful, all of you.\x02",
    )

    CloseMessageWindow()

    label("loc_BD8")

    TalkEnd(0x8)
    Return()

    # Function_3_902 end

    def Function_4_BDC(): pass

    label("Function_4_BDC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(    #11
        0xFE,
        (
            "I had scheduled several business\x01",
            "meetings and purchases...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But they're all down the tubes\x01",
            "now that I'm stuck here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I'm going to have to make a number of\x01",
            "apologies once I get back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D47")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_D47")

    ChrTalk(    #14
        0xFE,
        (
            "All things considered, I'm surprised you\x01",
            "were able to find and get in this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Being a bracer must be a\x01",
            "tough occupation, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D47")

    TalkEnd(0x9)
    Return()

    # Function_4_BDC end

    def Function_5_D4B(): pass

    label("Function_5_D4B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_DCE")

    ChrTalk(    #16
        0xFE,
        (
            "There are still some sky bandits\x01",
            "outside, aren't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "We've got to protect the\x01",
            "passengers at all costs...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E44")

    label("loc_DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(    #18
        0xFE,
        "Thank you for saving us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "All of the passengers are safe\x01",
            "and sound. No one's sick or\x01",
            "injured, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E44")

    TalkEnd(0xA)
    Return()

    # Function_5_D4B end

    def Function_6_E48(): pass

    label("Function_6_E48")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(    #20
        0xFE,
        (
            "You bracers are really something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I can't believe you're launching an\x01",
            "attack on the sky bandits' hideout\x01",
            "with just the handful of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2A")

    label("loc_EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #22
        0xFE,
        "I knew you'd come to save us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Thank you, all!\x02",
    )

    CloseMessageWindow()

    label("loc_F2A")

    TalkEnd(0xB)
    Return()

    # Function_6_E48 end

    def Function_7_F2E(): pass

    label("Function_7_F2E")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1014")
    OP_A2(0x1)

    ChrTalk(    #24
        0xFE,
        (
            "That sky bandit head honcho\x01",
            "was one scary dude...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I almost feel sorry for the men\x01",
            "under his control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Some of the bandits were rather\x01",
            "kind, almost like they were being\x01",
            "forced into doing this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109F")

    label("loc_1014")


    ChrTalk(    #27
        0xFE,
        (
            "Something about this whole\x01",
            "situation makes me feel\x01",
            "kind of sorry for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "And to think that something\x01",
            "like this would happen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109F")

    Jump("loc_1134")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1134")

    ChrTalk(    #29
        0xFE,
        (
            "Man, I thought this was the\x01",
            "end of us for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "There was something just not\x01",
            "right about the look in that\x01",
            "sky bandit boss' eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1134")

    TalkEnd(0xC)
    Return()

    # Function_7_F2E end

    def Function_8_1138(): pass

    label("Function_8_1138")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(    #31
        0xFE,
        (
            "I really want to contact the Orbalship\x01",
            "Corporation and let them know that\x01",
            "we've been saved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1234")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(    #32
        0xFE,
        "I'm glad that we're safe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "But what happened to the Linde?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "We were blindfolded, so we never\x01",
            "exactly saw what happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1234")

    TalkEnd(0xD)
    Return()

    # Function_8_1138 end

    def Function_9_1238(): pass

    label("Function_9_1238")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_12D6")

    ChrTalk(    #35
        0xFE,
        (
            "If those punks set foot in here,\x01",
            "I'm going to give them a good\x01",
            "beating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "It'll be my revenge for the Linde.\x01",
            "Nobody gets away with that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136F")

    label("loc_12D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_136F")

    ChrTalk(    #37
        0xFE,
        (
            "After the way they ripped out the\x01",
            "Linde's engine... I'd kept it in\x01",
            "such good repair, all this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "I'll never forgive them for that.\x02",
    )

    CloseMessageWindow()

    label("loc_136F")

    TalkEnd(0xE)
    Return()

    # Function_9_1238 end

    def Function_10_1373(): pass

    label("Function_10_1373")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #39
        0xFE,
        "I'm sure...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "I'm sure Katrina's worried sick.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F9")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_13F9")

    ChrTalk(    #41
        0xFE,
        (
            "Oh, I wonder what's going on\x01",
            "with my store right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F9")

    TalkEnd(0xF)
    Return()

    # Function_10_1373 end

    def Function_11_13FD(): pass

    label("Function_11_13FD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1470")

    ChrTalk(    #42
        0xFE,
        (
            "I had planned to visit an old friend\x01",
            "in Rolent when I got caught up in\x01",
            "the middle of all this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14BD")

    label("loc_1470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_14BD")

    ChrTalk(    #43
        0xFE,
        "Oh...have we been saved?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I must be dreaming or something...\x02",
    )

    CloseMessageWindow()

    label("loc_14BD")

    TalkEnd(0x10)
    Return()

    # Function_11_13FD end

    def Function_12_14C1(): pass

    label("Function_12_14C1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1550")

    ChrTalk(    #45
        0xFE,
        (
            "I had been away to give a lecture\x01",
            "at the royal academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "But who would have thought this\x01",
            "would happen on the way back?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158B")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_158B")

    ChrTalk(    #47
        0xFE,
        (
            "Oh, I'll finally be able to\x01",
            "get home to Zeiss!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158B")

    TalkEnd(0x11)
    Return()

    # Function_12_14C1 end

    def Function_13_158F(): pass

    label("Function_13_158F")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_15CE")

    ChrTalk(    #48
        0xFE,
        (
            "I'm sure my whole family's\x01",
            "worried about me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1632")

    ChrTalk(    #49
        0xFE,
        (
            "Thanks for coming to our\x01",
            "rescue, bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Now I'll finally be able\x01",
            "to return home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1632")

    TalkEnd(0x12)
    Return()

    # Function_13_158F end

    def Function_14_1636(): pass

    label("Function_14_1636")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1667")

    ChrTalk(    #51
        0xFE,
        "I'm just glad everyone's safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16DE")

    label("loc_1667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_16DE")

    ChrTalk(    #52
        0xFE,
        (
            "Now I'll finally be able to get\x01",
            "back to my travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Being stuck here has put a\x01",
            "real kink in my plans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    TalkEnd(0x13)
    Return()

    # Function_14_1636 end

    def Function_15_16E2(): pass

    label("Function_15_16E2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(    #54
        0xFE,
        (
            "You've got the sky bandits cornered?\x01",
            "I'm sorry I can't be of any help,\x01",
            "but I'm rooting for you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Good luck!\x02",
    )

    CloseMessageWindow()
    Jump("loc_17E9")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_17E9")

    ChrTalk(    #56
        0xFE,
        (
            "Those sky bandits ripped off every-\x01",
            "thing I bought at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Make sure to get my stuff\x01",
            "back, bracers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E9")

    TalkEnd(0x14)
    Return()

    # Function_15_16E2 end

    def Function_16_17ED(): pass

    label("Function_16_17ED")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1862")

    ChrTalk(    #58
        0xFE,
        (
            "Th-There are still sky bandits\x01",
            "out there, aren't there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "P-Please hurry and take care\x01",
            "of them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_1862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(    #60
        0xFE,
        (
            "Th-This was the first time I'd\x01",
            "ever ridden on an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "And to think that something\x01",
            "like this would happen...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E4")

    TalkEnd(0x15)
    Return()

    # Function_16_17ED end

    def Function_17_18E8(): pass

    label("Function_17_18E8")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1974")

    ChrTalk(    #62
        0xFE,
        (
            "Those sky bandits were very nice to\x01",
            "little Atget. They even gave her\x01",
            "sweets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "They might not all be such a\x01",
            "bad bunch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C9")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_19C9")

    ChrTalk(    #64
        0xFE,
        "Thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "More than myself, I'm glad to know\x01",
            "Atget's been saved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C9")

    TalkEnd(0x16)
    Return()

    # Function_17_18E8 end

    def Function_18_19CD(): pass

    label("Function_18_19CD")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_END)), "loc_1A19")

    ChrTalk(    #66
        0xFE,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Don't pick on the nice guards\x01",
            "too much, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6B")

    label("loc_1A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_1A6B")

    ChrTalk(    #68
        0xFE,
        "Are you guys bray-zers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Are you going to arrest\x01",
            "the nice guards?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6B")

    TalkEnd(0x17)
    Return()

    # Function_18_19CD end

    def Function_19_1A6F(): pass

    label("Function_19_1A6F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetMapFlags(0x400000)
    SetChrPos(0x101, 4948, 0, -101090, 0)
    SetChrPos(0x102, 4948, 0, -101090, 0)
    SetChrPos(0x103, 4948, 0, -101090, 0)
    SetChrPos(0x104, 4948, 0, -101090, 0)
    SetChrPos(0x18, 6280, 0, -94290, 270)
    SetChrPos(0x19, 4610, 0, -94970, 0)
    SetChrPos(0x1C, 9423, 0, -92822, 0)
    SetChrPos(0x1D, 9856, 0, -97201, 90)
    SetChrPos(0x1E, 3340, 0, -93640, 90)
    SetChrPos(0x1F, 88, 0, -97865, 270)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 22)
    SetChrChipByIndex(0x103, 24)
    SetChrChipByIndex(0x104, 26)
    OP_6D(5230, 0, -96500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_1C55():
        OP_6D(5440, 0, -94380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C55)
    ClearChrFlags(0x101, 0x80)

    def lambda_1C72():
        OP_8E(0xFE, 0x1308, 0x0, 0xFFFE8271, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C72)
    Sleep(200)
    ClearChrFlags(0x102, 0x80)

    def lambda_1C97():
        OP_8E(0xFE, 0x1631, 0x0, 0xFFFE81AD, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C97)
    Sleep(200)
    ClearChrFlags(0x104, 0x80)

    def lambda_1CBC():
        OP_8E(0xFE, 0x18A9, 0x0, 0xFFFE7EDF, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CBC)
    Sleep(200)
    ClearChrFlags(0x103, 0x80)

    def lambda_1CE1():
        OP_8E(0xFE, 0xF99, 0x0, 0xFFFE7E42, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CE1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x103, 0x1)

    def lambda_1D10():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1D10)

    def lambda_1D1E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1D1E)

    def lambda_1D2C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1D2C)

    def lambda_1D3A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1D3A)

    def lambda_1D48():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1D48)

    def lambda_1D56():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1D56)
    WaitChrThread(0x18, 0x1)

    ChrTalk(    #70
        0x18,
        "#3PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x18,
        "#3POh, you guys new around here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#007FLike in your freaking dreams!\x02\x03",

            "Are these guys for real?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x19,
        (
            "#3PUm, but...if you're not new here,\x01",
            "then who are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x19,
        "#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x18,
        (
            "#3PWhat...? Are you supposed to\x01",
            "be intruders?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0xA6, 0x0, 0x64)

    ChrTalk(    #76
        0x104,
        "#031FBingo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#012FWe're with the Bracer Guild.\x01",
            "I think it would be best if\x01",
            "you surrendered.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x18, 15)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 15)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 15)
    Sleep(100)
    SetChrChipByIndex(0x1D, 15)
    Sleep(75)
    SetChrChipByIndex(0x1E, 15)
    Sleep(50)
    SetChrChipByIndex(0x1F, 15)

    ChrTalk(    #78
        0x19,
        "#3PF-Forget that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x18,
        "#3PWe won't give up without a fight!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)

    def lambda_1FC5():
        OP_6D(5230, 0, -96500, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC5)
    SetChrChipByIndex(0x19, 17)

    def lambda_1FE2():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1FE2)
    SetChrChipByIndex(0x1C, 17)

    def lambda_1FFC():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1FFC)
    SetChrChipByIndex(0x1D, 17)

    def lambda_2016():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2016)
    SetChrChipByIndex(0x1E, 17)

    def lambda_2030():
        OP_92(0xFE, 0x101, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2030)
    SetChrChipByIndex(0x1F, 17)

    def lambda_204A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_204A)
    Sleep(250)
    SetChrChipByIndex(0x18, 17)

    def lambda_2069():
        OP_96(0x18, 0x16D8, 0x0, 0xFFFE84CF, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2069)
    Sleep(400)
    Battle(0x38A, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_209F"),
        (SWITCH_DEFAULT, "loc_20A2"),
    )


    label("loc_209F")

    OP_B4(0x0)
    Return()

    label("loc_20A2")

    EventBegin(0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrPos(0x101, 5750, 0, -97780, 39)
    SetChrPos(0x102, 6780, 0, -98300, 4)
    SetChrPos(0x103, 4320, 0, -97780, 72)
    SetChrPos(0x104, 4700, 0, -96480, 85)
    SetChrPos(0x19, 3520, 0, -93920, 35)
    SetChrPos(0x1C, 2640, 0, -91700, 4)
    SetChrPos(0x1D, 9860, 0, -97730, 260)
    SetChrPos(0x1E, 1950, 0, -97080, 217)
    SetChrPos(0x1F, 2350, 0, -98760, 140)
    SetChrPos(0x18, 6511, 0, -96547, 0)
    TurnDirection(0x19, 0x101, 0)
    TurnDirection(0x18, 0x101, 0)
    TurnDirection(0x1C, 0x101, 0)
    TurnDirection(0x1D, 0x101, 0)
    SetChrChipByIndex(0x18, 16)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x18, 0)
    TurnDirection(0x102, 0x18, 0)
    TurnDirection(0x104, 0x18, 0)
    TurnDirection(0x103, 0x18, 0)
    OP_6D(6280, 0, -96740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(1000)

    ChrTalk(    #80
        0x18,
        "#5PUuughhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#005FAll right! Now where are the\x01",
            "hostages?\x02\x03",

            "If you don't start talking, there are\x01",
            "going to be some serious consequences\x01",
            "involving a whip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        "#5PD-Do what you want with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x18,
        "#5PWe're not going to talk...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#027F#6POh? Is that so?\x02\x03",

            "Let me handle this, Estelle!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #85
        0x101,
        (
            "#004FUh, sure.\x01",
            "Can't say I didn't warn you guys...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23C7():
        OP_8E(0xFE, 0x1536, 0x0, 0xFFFE7ECE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23C7)
    WaitChrThread(0x101, 0x1)

    def lambda_23E7():
        OP_6D(6700, 0, -96370, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23E7)

    def lambda_23FF():
        OP_92(0x103, 0x18, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23FF)
    OP_8C(0x101, 22, 400)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 24)
    Sleep(1000)
    OP_44(0x103, 0xFF)
    SetChrChipByIndex(0x103, 19)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_2438():
        OP_99(0x103, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2438)
    Sleep(200)
    SetChrFlags(0x18, 0x20)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x12, 0x0, 0x18, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x18, 0x20)
    TurnDirection(0x18, 0x103, 0)
    OP_8F(0x18, 0x204F, 0x0, 0xFFFE8E09, 0x1F40, 0x0)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2)

    ChrTalk(    #86
        0x18,
        "Aaaaaah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#027F#3PHmm? Honestly, I'm being quite gentle\x01",
            "with you. Don't think for a second that\x01",
            "you're allowed to pass out yet.\x02\x03",

            "But if you start talking, maybe I'll\x01",
            "be kind enough to let you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x18,
        "Y-Yikes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x18,
        (
            "They're down below! Some of our\x01",
            "crew are guarding them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#020F#3PVery good.\x02\x03",

            "Now where are your leaders?\x01",
            "Kyle and Josette, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x18,
        (
            "F-Forget it, lady!\x01",
            "Do your worst!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x18,
        "No one'll tell you where they are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x103,
        (
            "#020F#3PSo the hostages are one thing,\x01",
            "but you're not going to sell out your\x01",
            "bosses, huh?\x02\x03",

            "#021FI guess there's only one thing left\x01",
            "to do.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrFlags(0x103, 0x20)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2723():
        OP_6D(8010, 0, -95060, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2723)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2740():
        OP_96(0x103, 0x1DE0, 0x0, 0xFFFE8B9B, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2740)
    Sleep(500)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_2768():
        OP_99(0x103, 0x1, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2768)
    Sleep(200)
    SetChrFlags(0x18, 0x20)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x18, 18)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x20)
    TurnDirection(0x18, 0x103, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_8F(0x18, 0x27D8, 0x3E8, 0xFFFE969A, 0x3A98, 0x0)
    PlayEffect(0x12, 0xFF, 0x18, 0, 0, -500, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x8E, 0x0, 0x64)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0x18, 0x27D8, 0x0, 0xFFFE969A, 0x3E8, 0x0)
    OP_22(0x25, 0x0, 0x64)
    SetChrChipByIndex(0x18, 16)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x18, 0x2, 0x3, 0x3E8)

    ChrTalk(    #94
        0x18,
        "Uuunngh...\x02",
    )

    CloseMessageWindow()

    def lambda_2849():
        OP_6D(6700, 0, -96370, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2849)
    Sleep(1000)

    ChrTalk(    #95
        0x101,
        (
            "#007FHoly Stregas...\x01",
            "Schera's as unforgiving as ever.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x103, 24)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #96
        0x103,
        (
            "#020F#6PThis? No, I've been FAR more\x01",
            "unforgiving...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        (
            "#033F#3PAny masochist would be thrilled to\x01",
            "make your acquaintance, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x103,
        (
            "#027F#6PAnd my whip would be thrilled to\x01",
            "make yours. \x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x104, 0xFF)
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #99
        0x104,
        "#035F#3PMaybe some other time.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #100
        0x102,
        (
            "#012FIt looks like the hostages are\x01",
            "being held down below.\x02\x03",

            "Let's hurry.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1E, 0x4)
    OP_44(0x103, 0xFF)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    EventEnd(0x0)
    OP_A2(0x355)
    OP_28(0x39, 0x1, 0x4)
    ClearMapFlags(0x400000)
    Return()

    # Function_19_1A6F end

    def Function_20_2A39(): pass

    label("Function_20_2A39")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetMapFlags(0x400000)
    SetChrPos(0x101, -51020, 0, -100510, 0)
    SetChrPos(0x102, -51020, 0, -100510, 0)
    SetChrPos(0x103, -51020, 0, -100510, 0)
    SetChrPos(0x104, -51020, 0, -100510, 0)
    SetChrPos(0x1A, -49700, 0, -95128, 270)
    SetChrPos(0x1B, -51210, 0, -95060, 90)
    SetChrPos(0x20, -46020, 0, -97600, 90)
    SetChrPos(0x21, -50250, 0, -91580, 270)
    SetChrPos(0x22, -52750, 0, -91250, 90)
    SetChrPos(0x23, -56510, 0, -97430, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrChipByIndex(0x101, 20)
    SetChrChipByIndex(0x102, 22)
    SetChrChipByIndex(0x103, 24)
    SetChrChipByIndex(0x104, 26)
    OP_6D(-50990, 0, -98940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_4A(0x23, 255)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2C2E():
        OP_6D(-51370, 0, -96390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C2E)
    ClearChrFlags(0x101, 0x80)

    def lambda_2C4B():
        OP_8E(0xFE, 0xFFFF363E, 0x0, 0xFFFE816C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C4B)
    Sleep(200)
    ClearChrFlags(0x103, 0x80)

    def lambda_2C70():
        OP_8E(0xFE, 0xFFFF3A9E, 0x0, 0xFFFE7FD2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C70)
    Sleep(200)
    ClearChrFlags(0x102, 0x80)

    def lambda_2C95():
        OP_8E(0xFE, 0xFFFF31CA, 0x0, 0xFFFE7E74, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C95)
    Sleep(200)
    ClearChrFlags(0x104, 0x80)

    def lambda_2CBA():
        OP_8E(0xFE, 0xFFFF3CD8, 0x0, 0xFFFE7C4E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CBA)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 270, 0)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 45, 0)

    def lambda_2CF7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2CF7)

    def lambda_2D05():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2D05)

    def lambda_2D13():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2D13)

    def lambda_2D21():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2D21)

    def lambda_2D2F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2D2F)

    def lambda_2D3D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2D3D)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #101
        0x1A,
        (
            "Wh-Who are you guys supposed\x01",
            "to be?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x1B,
        "Bracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x1B,
        "H-How'd you get in here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        (
            "#022FIt looks like the hostages are\x01",
            "being held in the room just\x01",
            "beyond here.\x02\x03",

            "I think it's time you surrendered\x01",
            "quietly or else...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x22, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x1A, 15)
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1B, 15)
    OP_51(0x1B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x20, 15)
    Sleep(100)
    SetChrChipByIndex(0x21, 15)
    Sleep(75)
    SetChrChipByIndex(0x22, 15)
    Sleep(50)
    SetChrChipByIndex(0x23, 15)

    ChrTalk(    #105
        0x1A,
        "Don't kid yourself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1B,
        "Let's get 'em!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x20, 17)

    def lambda_2F10():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2F10)
    SetChrChipByIndex(0x21, 17)

    def lambda_2F2A():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2F2A)
    SetChrChipByIndex(0x22, 17)

    def lambda_2F44():
        OP_92(0xFE, 0x101, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_2F44)
    SetChrChipByIndex(0x23, 17)

    def lambda_2F5E():
        OP_92(0xFE, 0x101, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2F5E)
    Sleep(250)
    SetChrChipByIndex(0x1A, 17)

    def lambda_2F7D():
        OP_96(0xFE, 0xFFFF3954, 0x0, 0xFFFE84E1, 0x76C, 0x1388)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F7D)
    SetChrChipByIndex(0x1B, 17)

    def lambda_2FA0():
        OP_96(0xFE, 0xFFFF3792, 0x0, 0xFFFE865F, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2FA0)
    Sleep(400)
    Battle(0x38B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2FD6"),
        (SWITCH_DEFAULT, "loc_2FD9"),
    )


    label("loc_2FD6")

    OP_B4(0x0)
    Return()

    label("loc_2FD9")

    EventBegin(0x0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrChipByIndex(0x1A, 16)
    SetChrChipByIndex(0x1B, 16)
    SetChrChipByIndex(0x20, 16)
    SetChrChipByIndex(0x21, 16)
    SetChrChipByIndex(0x22, 16)
    SetChrChipByIndex(0x23, 16)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x20, 0xFF)
    OP_44(0x21, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_51(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-50610, 0, -43450, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrSubChip(0x17, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #107
        0x9,
        "Wh-What's going on out there...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "It seems a bit loud for just\x01",
            "an internal squabble...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x101, -51210, 0, -51500, 0)
    Sleep(500)

    ChrTalk(    #109
        0x101,
        "#005F#1PIs everyone all right?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_332D():
        OP_6D(-50590, 0, -45100, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_332D)
    ClearChrFlags(0x101, 0x80)

    def lambda_334A():
        OP_8E(0xFE, 0xFFFF3562, 0x0, 0xFFFF4782, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_334A)
    Sleep(200)
    SetChrPos(0x103, -51210, 0, -51500, 0)

    def lambda_337B():
        OP_8E(0xFE, 0xFFFF3A44, 0x0, 0xFFFF4638, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_337B)
    Sleep(200)
    SetChrPos(0x102, -51210, 0, -51500, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_33B1():
        OP_8E(0xFE, 0xFFFF3184, 0x0, 0xFFFF43AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33B1)
    Sleep(200)
    SetChrPos(0x104, -51210, 0, -51500, 0)

    def lambda_33E2():
        OP_8E(0xFE, 0xFFFF3CBA, 0x0, 0xFFFF419C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33E2)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 0)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #110
        0x103,
        (
            "#020FWe're with the Bracer Guild and\x01",
            "we've come to rescue you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF4A20, 0x0, 0xFFFF4C64, 0xFA0, 0x0)

    ChrTalk(    #111
        0x9,
        "S-Seriously...? W-We're saved?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FWe've taken care of the guards,\x01",
            "so you don't need to worry about\x01",
            "anything for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        "#1PR-Really...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x12,
        "#3PW-We've been saved?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#1PI'm Grandt, captain of the airliner,\x01",
            "Linde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#1PI don't know how to express my\x01",
            "gratitude for what you've done\x01",
            "for us here today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#006FYou can thank us after we've\x01",
            "gotten you out of here.\x02\x03",

            "By the way...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 45, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x101,
        "#004FHuh...? Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#012FIt doesn't look like he's here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        "#1PWho...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        (
            "#002FUh...\x02\x03",

            "Are these all the hostages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        "#1PYes, that's correct.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#1PThis is everybody who was on the Linde,\x01",
            "including crew and passengers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#004FThat can't be right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#012FWasn't there a man by the name\x01",
            "of Cassius Bright on this flight?\x02\x03",

            "He's a member of the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#1PCassius Bright...? Hmm... I do\x01",
            "seem to remember hearing that\x01",
            "name somewhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #127
        0xA,
        (
            "Umm, Captain...isn't he that\x01",
            "passenger...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #128
        0xA,
        (
            "You know, the one who got off\x01",
            "right before we left?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#3PRight! Now that you mention it,\x01",
            "there was one passenger who\x01",
            "did get off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#002FWh-What do you mean?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #131
        0x8,
        (
            "#1PWell, there was this one passenger\x01",
            "who disembarked the airliner right\x01",
            "before we took off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "#1PA man who had been on-board since the\x01",
            "Royal City, and he did seem to have\x01",
            "such a name if I remember correctly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x101,
        (
            "#004FWh-What?!\x02\x03",

            "B-But his name was on the\x01",
            "passenger list...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#1PWell, since he got off right before\x01",
            "we departed, there wasn't any time\x01",
            "to document the changes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "#1PThis would have been handled had we arrived in\x01",
            "Rolent, but we were attacked by the sky bandits\x01",
            "en route and things were left as they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#015FSo that's what happened, huh?\x02\x03",

            "I thought it would have been awfully\x01",
            "strange if Dad had been captured by\x01",
            "the sky bandits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x103,
        (
            "#027FWell...it looks like our question has\x01",
            "finally been answered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x104,
        "#031FHa ha ha. How ironic.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #140
        0x101,
        (
            "#009F#5PNow wait a minute!\x02\x03",

            "Th-Then...just what is Dad doing?\x02\x03",

            "With something this big going on,\x01",
            "why hasn't he contacted us?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #141
        0x102,
        (
            "#012F#5PCalm down, Estelle.\x02\x03",

            "I know you're as curious to know\x01",
            "as I am, but thinking about it now\x01",
            "isn't going to get us anywhere.\x02\x03",

            "Our focus needs to be on securing\x01",
            "the safety of the hostages.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #142
        0x101,
        (
            "#002F#5POkay...\x02\x03",

            "You're right... I guess I'll just\x01",
            "have to forget about it for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x103,
        (
            "#020FListen up, everyone! We are now\x01",
            "going to go after the sky bandit\x01",
            "leaders and arrest them.\x02\x03",

            "I know how you all must feel,\x01",
            "but I need you to sit tight a\x01",
            "little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        "#1PWe'll be waiting here... Good luck.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #145
        0x9,
        (
            "If that's the case, we'll prepare\x01",
            "for the worst. Our lives are in\x01",
            "your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        "In other words, don't let us down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#006FLeave everything to us!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-51030, 0, -47780, 0)
    OP_6B(2600, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    SetChrPos(0x0, -51030, 0, -47780, 0)
    SetChrPos(0x1, -51030, 0, -47780, 0)
    SetChrPos(0x2, -51030, 0, -47780, 0)
    SetChrPos(0x3, -51030, 0, -47780, 0)
    OP_0D()
    ClearMapFlags(0x400000)
    OP_A2(0x356)
    OP_28(0x39, 0x1, 0x8)
    OP_28(0x39, 0x1, 0x10)
    OP_28(0x39, 0x1, 0x20)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x18, -54970, 0, -93490, 315)
    SetChrPos(0x19, -48920, 0, -91340, 53)
    SetChrPos(0x1C, -45150, 0, -93440, 163)
    SetChrPos(0x1D, -48280, 0, -97510, 119)
    SetChrPos(0x1E, -54960, 0, -97820, 86)
    SetChrPos(0x1F, -53760, 0, -91280, 172)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    SetChrChipByIndex(0x18, 28)
    SetChrChipByIndex(0x19, 28)
    SetChrChipByIndex(0x1C, 28)
    SetChrChipByIndex(0x1D, 28)
    SetChrChipByIndex(0x1E, 28)
    SetChrChipByIndex(0x1F, 28)
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    Return()

    # Function_20_2A39 end

    SaveToFile()

Try(main)

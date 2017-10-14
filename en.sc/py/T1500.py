from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
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
            '',
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
        'Sieg',                                 # 16
        'Boat',                                 # 17
        'Boat',                                 # 18
        'Kurt',                                 # 19
        'Norche',                               # 20
        'Helmuth',                              # 21
        'Sting',                                # 22
        'Lloyd',                                # 23
        'Helmsman Lux',                         # 24
        'Glass',                                # 25
        'Glass',                                # 26
        'Glass',                                # 27
        'Glass',                                # 28
        'Kuwano',                               # 29
        'Fishbucket',                           # 30
        'Fishbucket',                           # 31
        'Fishbucket',                           # 32
        'Fishbucket',                           # 33
        'New Ansel Path',                       # 34
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
        'ED6_DT06/CH20045 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT07/CH00023 ._CH',             # 02
        'ED6_DT07/CH00053 ._CH',             # 03
        'ED6_DT07/CH00033 ._CH',             # 04
        'ED6_DT07/CH00043 ._CH',             # 05
        'ED6_DT07/CH00063 ._CH',             # 06
        'ED6_DT07/CH00073 ._CH',             # 07
        'ED6_DT27/CH03083 ._CH',             # 08
        'ED6_DT07/CH00020 ._CH',             # 09
        'ED6_DT07/CH00050 ._CH',             # 0A
        'ED6_DT07/CH00030 ._CH',             # 0B
        'ED6_DT07/CH00040 ._CH',             # 0C
        'ED6_DT07/CH00060 ._CH',             # 0D
        'ED6_DT07/CH00070 ._CH',             # 0E
        'ED6_DT27/CH03080 ._CH',             # 0F
        'ED6_DT07/CH02323 ._CH',             # 10
        'ED6_DT26/CH20235 ._CH',             # 11
        'ED6_DT26/CH20240 ._CH',             # 12
        'ED6_DT26/CH20402 ._CH',             # 13
        'ED6_DT06/CH20021 ._CH',             # 14
        'ED6_DT26/CH20372 ._CH',             # 15
        'ED6_DT26/CH20395 ._CH',             # 16
        'ED6_DT26/CH20394 ._CH',             # 17
        'ED6_DT26/CH20393 ._CH',             # 18
        'ED6_DT07/CH00150 ._CH',             # 19
        'ED6_DT07/CH00151 ._CH',             # 1A
        'ED6_DT07/CH00152 ._CH',             # 1B
        'ED6_DT07/CH00153 ._CH',             # 1C
        'ED6_DT07/CH00154 ._CH',             # 1D
        'ED6_DT07/CH00159 ._CH',             # 1E
        'ED6_DT06/CH20137 ._CH',             # 1F
        'ED6_DT07/CH00170 ._CH',             # 20
        'ED6_DT07/CH00171 ._CH',             # 21
        'ED6_DT07/CH00172 ._CH',             # 22
        'ED6_DT07/CH00173 ._CH',             # 23
        'ED6_DT07/CH00174 ._CH',             # 24
        'ED6_DT07/CH00178 ._CH',             # 25
        'ED6_DT07/CH01230 ._CH',             # 26
        'ED6_DT07/CH01220 ._CH',             # 27
        'ED6_DT27/CH03790 ._CH',             # 28
        'ED6_DT07/CH01000 ._CH',             # 29
        'ED6_DT07/CH01020 ._CH',             # 2A
        'ED6_DT27/CH03860 ._CH',             # 2B
        'ED6_DT26/CH20408 ._CH',             # 2C
    )

    AddCharChipPat(
        'ED6_DT06/CH20045P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT07/CH00023P._CP',             # 02
        'ED6_DT07/CH00053P._CP',             # 03
        'ED6_DT07/CH00033P._CP',             # 04
        'ED6_DT07/CH00043P._CP',             # 05
        'ED6_DT07/CH00063P._CP',             # 06
        'ED6_DT07/CH00073P._CP',             # 07
        'ED6_DT27/CH03083P._CP',             # 08
        'ED6_DT07/CH00020P._CP',             # 09
        'ED6_DT07/CH00050P._CP',             # 0A
        'ED6_DT07/CH00030P._CP',             # 0B
        'ED6_DT07/CH00040P._CP',             # 0C
        'ED6_DT07/CH00060P._CP',             # 0D
        'ED6_DT07/CH00070P._CP',             # 0E
        'ED6_DT27/CH03080P._CP',             # 0F
        'ED6_DT07/CH02323P._CP',             # 10
        'ED6_DT26/CH20235P._CP',             # 11
        'ED6_DT26/CH20240P._CP',             # 12
        'ED6_DT26/CH20402P._CP',             # 13
        'ED6_DT06/CH20021P._CP',             # 14
        'ED6_DT26/CH20372P._CP',             # 15
        'ED6_DT26/CH20395P._CP',             # 16
        'ED6_DT26/CH20394P._CP',             # 17
        'ED6_DT26/CH20393P._CP',             # 18
        'ED6_DT07/CH00150P._CP',             # 19
        'ED6_DT07/CH00151P._CP',             # 1A
        'ED6_DT07/CH00152P._CP',             # 1B
        'ED6_DT07/CH00153P._CP',             # 1C
        'ED6_DT07/CH00154P._CP',             # 1D
        'ED6_DT07/CH00159P._CP',             # 1E
        'ED6_DT06/CH20137P._CP',             # 1F
        'ED6_DT07/CH00170P._CP',             # 20
        'ED6_DT07/CH00171P._CP',             # 21
        'ED6_DT07/CH00172P._CP',             # 22
        'ED6_DT07/CH00173P._CP',             # 23
        'ED6_DT07/CH00174P._CP',             # 24
        'ED6_DT07/CH00178P._CP',             # 25
        'ED6_DT07/CH01230P._CP',             # 26
        'ED6_DT07/CH01220P._CP',             # 27
        'ED6_DT27/CH03790P._CP',             # 28
        'ED6_DT07/CH01000P._CP',             # 29
        'ED6_DT07/CH01020P._CP',             # 2A
        'ED6_DT27/CH03860P._CP',             # 2B
        'ED6_DT26/CH20408P._CP',             # 2C
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = -2000,
        Y                   = 43140,
        Direction           = 128,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2070,
        Z                   = -2000,
        Y                   = 38510,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -9480,
        Z                   = 0,
        Y                   = 62260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -8170,
        Z                   = 500,
        Y                   = 40910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -11480,
        Z                   = -2000,
        Y                   = 34670,
        Direction           = 267,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327700,
        ChipIndex           = 0x14,
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
        Unknown3            = 327700,
        ChipIndex           = 0x14,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37610,
        Z                   = -2000,
        Y                   = 44850,
        Direction           = 178,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
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
        Unknown3            = 262188,
        ChipIndex           = 0x2C,
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
        Unknown3            = 262188,
        ChipIndex           = 0x2C,
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
        Unknown3            = 44,
        ChipIndex           = 0x2C,
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
        Unknown3            = 65580,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
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
        X                   = -46710,
        Y                   = -2400,
        Z                   = 40980,
        Range               = -43080,
        Unknown_10          = 0xFFFFFE70,
        Unknown_14          = 0xA604,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = -9910,
        TriggerZ            = 500,
        TriggerY            = 47790,
        TriggerRange        = 800,
        ActorX              = -9910,
        ActorZ              = 1500,
        ActorY              = 47790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4980,
        TriggerZ            = 4000,
        TriggerY            = 54310,
        TriggerRange        = 800,
        ActorX              = -4980,
        ActorZ              = 5000,
        ActorY              = 54310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5090,
        TriggerZ            = 4000,
        TriggerY            = 47820,
        TriggerRange        = 800,
        ActorX              = -5090,
        ActorZ              = 5000,
        ActorY              = 47820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2910,
        TriggerZ            = -2000,
        TriggerY            = 32500,
        TriggerRange        = 1000,
        ActorX              = -2980,
        ActorZ              = -3000,
        ActorY              = 29380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_622",          # 00, 0
        "Function_1_752",          # 01, 1
        "Function_2_80D",          # 02, 2
        "Function_3_98A",          # 03, 3
        "Function_4_B18",          # 04, 4
        "Function_5_E33",          # 05, 5
        "Function_6_FD6",          # 06, 6
        "Function_7_2722",         # 07, 7
        "Function_8_2DC7",         # 08, 8
        "Function_9_3152",         # 09, 9
        "Function_10_31A3",        # 0A, 10
        "Function_11_31F4",        # 0B, 11
        "Function_12_3245",        # 0C, 12
        "Function_13_42F3",        # 0D, 13
        "Function_14_4317",        # 0E, 14
        "Function_15_433B",        # 0F, 15
        "Function_16_435F",        # 10, 16
        "Function_17_436F",        # 11, 17
        "Function_18_4403",        # 12, 18
        "Function_19_4461",        # 13, 19
        "Function_20_45BD",        # 14, 20
        "Function_21_4719",        # 15, 21
        "Function_22_479E",        # 16, 22
        "Function_23_4823",        # 17, 23
        "Function_24_4B90",        # 18, 24
        "Function_25_5CB6",        # 19, 25
        "Function_26_5E49",        # 1A, 26
        "Function_27_5EC2",        # 1B, 27
        "Function_28_6010",        # 1C, 28
    )


    def Function_0_622(): pass

    label("Function_0_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_64A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B1("T1500_n")
    Event(0, 12)
    Jump("loc_67A")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_67A")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_B1("T1500_y")
    OP_71(0x1, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F(0x64, 0x64)
    Event(0, 24)

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6F5")
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_6F2")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_6BD")
    SetChrChipByIndex(0x16, 42)
    SetChrPos(0x16, -8170, 500, 40910, 180)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Jump("loc_6DC")

    label("loc_6BD")

    SetChrChipByIndex(0x16, 44)
    SetChrFlags(0x16, 0x10)
    OP_44(0x16, 0x0)
    SetChrPos(0x16, -45020, -2000, 38510, 180)

    label("loc_6DC")

    SetChrPos(0x15, -22540, 0, 47490, 180)
    ClearChrFlags(0x15, 0x80)

    label("loc_6F2")

    Jump("loc_751")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_6FF")
    Jump("loc_751")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_724")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2440, -2000, 38510, 159)
    Jump("loc_751")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_740")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D")
    SetChrFlags(0x15, 0x10)

    label("loc_73D")

    Jump("loc_751")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_751")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_751")

    Return()

    # Function_0_622 end

    def Function_1_752(): pass

    label("Function_1_752")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x230046)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_790")
    OP_B1("T1500_n")
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_783")
    Jump("loc_78D")

    label("loc_783")

    OP_D2(0x600B6, 0x600BB, 0x2C)

    label("loc_78D")

    Jump("loc_7BF")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7A3")
    OP_B1("T1500_n")
    Jump("loc_7BF")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_7B6")
    OP_B1("T1500_y")
    Jump("loc_7BF")

    label("loc_7B6")

    OP_B1("T1500_n")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F2")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x0)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    Jump("loc_807")

    label("loc_7F2")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_10(0x4, 0x1)

    label("loc_807")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_752 end

    def Function_2_80D(): pass

    label("Function_2_80D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_832")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_974")

    label("loc_832")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_974")

    label("loc_84B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_864")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_974")

    label("loc_864")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_974")

    label("loc_87D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_974")

    label("loc_896")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_974")

    label("loc_8AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_974")

    label("loc_8C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_974")

    label("loc_8E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_974")

    label("loc_8FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_913")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_974")

    label("loc_913")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_974")

    label("loc_92C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_945")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_974")

    label("loc_945")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_974")

    label("loc_95E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_974")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_989")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_974")

    label("loc_989")

    Return()

    # Function_2_80D end

    def Function_3_98A(): pass

    label("Function_3_98A")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9FC")

    ChrTalk(    #0
        0xFE,
        "I just can't stop fishing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'd keep doing it even if I had to\x01",
            "pawn off the wife! Ho ho ho.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B14")

    label("loc_9FC")


    ChrTalk(    #2
        0xFE,
        "*pheeew* Finally back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "With all the danger cleared up,\x01",
            "time to relax and wet my line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Somehow I just can't stop fishing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'd keep doing it even if I had to\x01",
            "pawn off the wife! Ho ho ho.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0E")

    ChrTalk(    #6
        0x101,
        (
            "#1007F(Thaaat's gonna have a happy ending,\x01",
            "I'm sure...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E")

    OP_A2(0x1C32)
    OP_A2(0x6)

    label("loc_B14")

    TalkEnd(0x1C)
    Return()

    # Function_3_98A end

    def Function_4_B18(): pass

    label("Function_4_B18")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_CA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BE1")

    ChrTalk(    #7
        0xFE,
        "Ahhhhh! What wonderful, invigorating weather!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I just trounced my hubby, and now\x01",
            "I feel totally energized!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Heehee! Gotta try harder if he\x01",
            "wants to challenge The Wife!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1")

    label("loc_BE1")


    ChrTalk(    #10
        0xFE,
        "Ahhhhh! What wonderful, invigorating weather!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Today's the last day of vacation for\x01",
            "my husband and me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I've beaten him handily in fishing,\x01",
            "so now I can go home feeling great!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CA1")

    Jump("loc_E2F")

    label("loc_CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(    #13
        0xFE,
        (
            "Looks might be deceiving, but I'm a\x01",
            "member of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Let's just say I'm pretty confident\x01",
            "in my rod work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_D38")


    ChrTalk(    #15
        0xFE,
        (
            "We've come out from the capital\x01",
            "for some fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I promised I'd teach my husband how to fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Looks might be deceiving, but I'm a\x01",
            "member of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Heehee! Let's just say I'm pretty confident\x01",
            "in my rod work!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E2F")

    TalkEnd(0x13)
    Return()

    # Function_4_B18 end

    def Function_5_E33(): pass

    label("Function_5_E33")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_ECD")

    ChrTalk(    #19
        0xFE,
        (
            "Mmm, I need to make up some ground\x01",
            "on this trip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "It would feel a little odd if Norche kept\x01",
            "dominating me at my own hobby!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD2")

    label("loc_ECD")


    ChrTalk(    #21
        0xFE,
        (
            "I was the one who originally liked\x01",
            "fishing, out of the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "But at some point, my wife got hooked on it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "And now she's actually a BETTER\x01",
            "fisherman than I am!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I've got ground to make up, even if I\x01",
            "have to steal some tricks from her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FD2")

    TalkEnd(0x14)
    Return()

    # Function_5_E33 end

    def Function_6_FD6(): pass

    label("Function_6_FD6")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_FE3")
    OP_A2(0x2)

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Sting previously\x01",               # 0
            "Set as did not meet Sting previously\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1060"),
        (1, "loc_1066"),
        (SWITCH_DEFAULT, "loc_106C"),
    )


    label("loc_1060")

    OP_A2(0x2)
    Jump("loc_106C")

    label("loc_1066")

    OP_A3(0x2)
    Jump("loc_106C")

    label("loc_106C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_231C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(    #25
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #26
        0x101,
        (
            "#1000FOh, hey, you're, um...\x02\x03",

            "Sting! Right? With the Bose branch.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #27
        0xFE,
        "That right. And you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "You're that recently-promoted bracer\x01",
            "that Lugran can't stop talking about.\x01",
            "And her runaway friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1011FLugran's been talking about us? Uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1041FWe kind of have been a relevant topic\x01",
            "in the news lately, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1000FNah, it was the only thing we could do,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "The Bose region seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D9")

    label("loc_12C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132C")

    ChrTalk(    #36
        0x103,
        (
            "#020FHello, Sting.\x01",
            "It's been quite a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_1395")

    label("loc_132C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138E")

    ChrTalk(    #37
        0x106,
        "#050FSting. Haven't seen you in a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_1395")

    label("loc_138E")

    TurnDirection(0xFE, 0x101, 400)

    label("loc_1395")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(    #38
        0xFE,
        "Scherazard's with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        (
            "#020FNo, hardly.\x01",
            "It was the only thing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_1449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FF")

    ChrTalk(    #42
        0xFE,
        "Agate, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#051FHey, no need for that.\x01",
            "Only thing I could do, really.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1685")

    label("loc_14FF")


    ChrTalk(    #46
        0xFE,
        "You lot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "You're that recently-promoted bracer\x01",
            "that Lugran can't stop talking about.\x01",
            "And her runaway friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1011FLugran's been talking about us? Uh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1041FWe kind of have been a relevant topic\x01",
            "in the news lately, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1000FNah, it was the only thing we could do,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1685")


    ChrTalk(    #53
        0xFE,
        "The Bose region seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()

    label("loc_16D9")

    OP_A2(0x1A53)
    OP_A2(0x3)
    Jump("loc_2319")

    label("loc_16E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1740")

    ChrTalk(    #55
        0xFE,
        "The Bose region seems calm for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "You can focus on your mission.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x408, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D4")
    EventBegin(0x0)
    OP_8C(0xFE, 180, 0)
    Fade(1000)
    OP_6D(-22140, 200, 48600, 0)
    OP_67(0, 7870, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(195000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -21550, 0, 48540, 180)
    SetChrPos(0x102, -22930, 0, 48980, 180)
    SetChrPos(0xF8, -21110, 0, 50050, 180)
    SetChrPos(0xF9, -22490, 0, 50460, 180)
    OP_0D()

    ChrTalk(    #57
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Ah, you all.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1868")

    ChrTalk(    #59
        0x106,
        (
            "#051FHeh, you're the same cool customer as\x01",
            "always, Sting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Heh. Just who I am.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1913")

    label("loc_1868")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BD")

    ChrTalk(    #61
        0x103,
        "#020FStill the same as always, Sting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Heh. Just who I am.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1913")

    label("loc_18BD")


    ChrTalk(    #63
        0x101,
        "#1000FHello, Sting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        "#1040FThank you for your help so far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "Ah, you two.\x02",
    )

    CloseMessageWindow()

    label("loc_1913")

    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #66
        0xFE,
        (
            "Actually.\x01",
            "Sorry to ask this out of the blue, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "Mind taking a look at this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1004FHuh...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #69
        (
            "\x07\x05Sting pulled a gemstone out of his pocket.\x01",
            "It glowed...black.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #70
        0xFE,
        "It looks like a quartz of some kind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I couldn't use it in my orbment, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1015FJoshua, isn't this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#1035FYes, it's most likely an ancient Zemurian\x01",
            "quartz.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0xFE,
        (
            "Really? I'd heard talk about them,\x01",
            "but I never expected to see one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I thought these were supposed to work\x01",
            "with these new orbments we have, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1011FI think so, but first, uh, a question.\x02\x03",

            "#1015FSting, where exactly did you FIND that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "About that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "It was around the Amberl Tower.\x01",
            "I fought this bizarre monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It was like a living fossil, or...\x01",
            "Anyway, it was strange, put it that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I picked this up after I defeated it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D54")

    ChrTalk(    #81
        0x101,
        "#1004FWait a minute, that sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#1042FThat sounds EXACTLY like the thing we\x01",
            "encountered atop the other tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "Ah, so you found one too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0C")

    label("loc_1D54")


    ChrTalk(    #84
        0x101,
        "#1002FYou don't think it could be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1042FYes, it may be a result of the shadow\x01",
            "towers manifesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "The shadow towers. Right, what you\x01",
            "encountered during the invasion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0C")


    ChrTalk(    #87
        0xFE,
        (
            "Anyway, I only ever found the one.\x01",
            "Haven't seen another since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Whatever it was, it was much, much\x01",
            "stronger than your average monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Wouldn't hurt to watch out for more\x01",
            "of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1002FYeah, no kidding.\x01",
            "Thanks for letting us know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Here, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x07\x00Received #717i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x2CD, 1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #94
        0x101,
        "#1004FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        "#1044FSting? Are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "My orbment's about as useful as a rock\x01",
            "right now, so a quartz is pointless for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "But all of you are on a pretty\x01",
            "important mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "What needs to happen seems obvious to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1004FWow...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C4")

    ChrTalk(    #100
        0x106,
        (
            "#051FAh, just come out and say you want\x01",
            "to help us already, ya lug.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214A")

    label("loc_20C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2121")

    ChrTalk(    #101
        0x103,
        (
            "#027FA very cool and distant\x01",
            "way of saying you want to help us,\x01",
            "Sting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_214A")

    label("loc_2121")


    ChrTalk(    #102
        0x102,
        "#1040FThank you very much for this.\x02",
    )

    CloseMessageWindow()

    label("loc_214A")


    ChrTalk(    #103
        0xFE,
        "You don't need to thank me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "You just concentrate on accomplishing\x01",
            "your mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1006FWe will! See you, Sting!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2041)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_2319")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A0")

    ChrTalk(    #106
        0xFE,
        (
            "This problem with the orbments is affecting\x01",
            "the entire kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "We're going to be in real trouble if\x01",
            "this continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Right now, though, all we can do is\x01",
            "give the best we can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2319")

    label("loc_22A0")


    ChrTalk(    #109
        0xFE,
        (
            "We're going to be in real trouble if\x01",
            "this continues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Right now, though, all we can do is\x01",
            "give the best we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2319")

    Jump("loc_271E")

    label("loc_231C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_271E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_246F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2388")

    ChrTalk(    #111
        0xFE,
        "I'll take care of all the side business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "You focus on the dragon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_241D")

    label("loc_2388")


    ChrTalk(    #113
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Heard you're working with the army to\x01",
            "fight the dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "I'll take care of all the side business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "You focus on the dragon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_241D")

    Jump("loc_246C")

    label("loc_2420")


    ChrTalk(    #117
        0xFE,
        "I'll take care of all the side business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "You focus on the dragon.\x02",
    )

    CloseMessageWindow()

    label("loc_246C")

    Jump("loc_271E")

    label("loc_246F")


    ChrTalk(    #119
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2552")

    ChrTalk(    #120
        0x101,
        (
            "#1011FOh, hey, you're, um...\x02\x03",

            "Sting! Right? With the Bose branch.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #121
        0xFE,
        "You're that junior from a month or two ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "You've been promoted since then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1016FYep! Managed it...somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A3")

    label("loc_2552")


    ChrTalk(    #124
        0x101,
        (
            "#1015F(Huh? Hey.)\x02\x03",

            "(Now that I look, doesn't this guy\x01",
            "have a guild emblem?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A3")


    ChrTalk(    #125
        0x106,
        (
            "#050FHaven't seen you in a while, Sting.\x02\x03",

            "You out here chasing those wanted monsters?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #126
        0xFE,
        "Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "You're part of the anti-dragon efforts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x106,
        (
            "#050FYeah, we're helpin' the army.\x02\x03",

            "We were on our way to Nebel Valley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "I'll take care of all the side business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "You focus on the dragon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x106,
        "#051FYou got it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x3)

    label("loc_271E")

    TalkEnd(0x15)
    Return()

    # Function_6_FD6 end

    def Function_7_2722(): pass

    label("Function_7_2722")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_29CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_295D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286A")

    ChrTalk(    #133
        0xFE,
        "I really never imagined you'd fish up the Guardian!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Still, fishing is essentially about finding\x01",
            "oneself within the natural world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Even if the Guardian's been caught,\x01",
            "there's still plenty of fish in the lake,\x01",
            "as it were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Maybe it's time I started thinking\x01",
            "beyond just Liberl...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_295A")

    label("loc_286A")


    ChrTalk(    #137
        0xFE,
        (
            "Even if the Guardian's been caught,\x01",
            "there's still plenty of fish in the lake,\x01",
            "as it were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Still, fishing is essentially about finding\x01",
            "oneself within the natural world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Maybe it's time I started thinking\x01",
            "beyond just Liberl...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295A")

    Jump("loc_29CA")

    label("loc_295D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C1")

    ChrTalk(    #140
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "I'll find you, Guardian of Valleria Lake!\x01",
            "Ohhh, I'll find you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_29CA")

    label("loc_29C1")


    ChrTalk(    #143
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_29CA")

    Jump("loc_2DC3")

    label("loc_29CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_2BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B07")

    ChrTalk(    #144
        0xFE,
        (
            "I came prepared, psyched up, certain\x01",
            "that THIS time I would fish up the Guardian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "And then I find out I was beaten to\x01",
            "the punch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I'm still kind of in shock, but this isn't the\x01",
            "end of my fishing career or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I just need to get it together and find\x01",
            "a new goal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2BCD")

    label("loc_2B07")


    ChrTalk(    #148
        0xFE,
        (
            "Getting beaten to the punch like that...\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I'm still kind of in shock, but this isn't the\x01",
            "end of my fishing career or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "I just need to get it together and find\x01",
            "a new goal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCD")

    Jump("loc_2DC3")

    label("loc_2BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFD")

    ChrTalk(    #151
        0xFE,
        (
            "I came prepared, psyched up, certain\x01",
            "that THIS time I would fish up the Guardian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "What in the world is that island-like\x01",
            "thing floating above the lake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Even the trouts and salmons aren't\x01",
            "biting at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I bet that thing above the lake is\x01",
            "affecting the fish, somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2DC3")

    label("loc_2CFD")


    ChrTalk(    #155
        0xFE,
        (
            "I came prepared, psyched up, certain\x01",
            "that THIS time I would fish up the Guardian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "But even the trouts and salmons\x01",
            "aren't biting at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "This might end up being a test of\x01",
            "endurance...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC3")

    TalkEnd(0x16)
    Return()

    # Function_7_2722 end

    def Function_8_2DC7(): pass

    label("Function_8_2DC7")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B8")

    ChrTalk(    #158
        0xFE,
        "Heya!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 5)), scpexpr(EXPR_END)), "loc_2E94")

    ChrTalk(    #159
        0x101,
        "#1000FOh, hi, Lux.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        "#1040FOut shopping?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #161
        0xFE,
        "Haha! You guys sure hear things awful quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "Yeah, unfortunately.\x01",
            "Got dragged out here without any choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC3")

    label("loc_2E94")


    ChrTalk(    #163
        0x101,
        (
            "#1001FOh, um, hi!\x02\x03",

            "#1004F...Er, wait!\x01",
            "Aren't you a Royal Guardsman?\x01",
            "Why are you out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        "#1044FYou're from the Arseille, aren't you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #165
        0xFE,
        "Yeah, got here on a paddle boat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "A couple of us actually got sent out here\x01",
            "to secure some rations and such.\x01",
            "Can't resupply normally, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC3")


    ChrTalk(    #167
        0x101,
        "#1016FAh, I get it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #168
        0xFE,
        (
            "I was in the middle of some work, but\x01",
            "got drafted to come help out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Normally this'd be Leon's job, but he\x01",
            "managed to get out of it, clever S.O.B...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "*sigh* I'm just easy to play, I guess.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2096)
    Jump("loc_314E")

    label("loc_30B8")


    ChrTalk(    #171
        0xFE,
        "Echo sure is late, either way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "How long does it take to pick up\x01",
            "some foodstuffs, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "Man, this is why I didn't want to\x01",
            "come along.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_314E")

    TalkEnd(0x17)
    Return()

    # Function_8_2DC7 end

    def Function_9_3152(): pass

    label("Function_9_3152")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #174
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_3152 end

    def Function_10_31A3(): pass

    label("Function_10_31A3")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #175
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_31A3 end

    def Function_11_31F4(): pass

    label("Function_11_31F4")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #176
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_31F4 end

    def Function_12_3245(): pass

    label("Function_12_3245")

    EventBegin(0x0)
    OP_DB()
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x40)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x40)
    OP_71(0x3, 0x4)
    OP_A1(0x10, 0x8)
    OP_A1(0x11, 0x1)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -8530, -2500, 32509, 0)
    SetChrPos(0x11, -6040, -2500, 32020, 0)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0xD, 0x1)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0xA, 0)
    OP_48()
    OP_89(0xA, -6050, -2400, 29730, 180)
    OP_89(0xC, -6520, -2400, 31060, 180)
    OP_89(0x9, -5840, -2400, 30990, 180)
    OP_89(0xD, -6350, -2400, 32350, 180)
    OP_89(0x101, -8940, -2400, 31400, 180)
    OP_89(0xB, -8270, -2400, 31410, 180)
    OP_89(0xE, -8950, -2400, 32740, 180)
    OP_89(0xF, -8450, -2400, 30470, 0)
    OP_89(0x8, -8280, -2400, 32740, 180)
    OP_6D(-6750, -2800, 30900, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(280, 0)

    def lambda_3428():

        label("loc_3428")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3428")

    QueueWorkItem2(0xA, 2, lambda_3428)
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    LoadEffect(0x1, "map\\\\mp013_01.eff")
    PlayEffect(0x0, 0x0, 0x10, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x10, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x11, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_22(0x92, 0x0, 0x46)

    def lambda_354A():
        OP_6D(-5900, -2530, 24130, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_354A)

    def lambda_3562():
        OP_67(0, 11840, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3562)

    def lambda_357A():
        OP_6C(49000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_357A)

    def lambda_358A():
        OP_6E(298, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_358A)
    OP_43(0x10, 0x0, 0x0, 0x13)
    Sleep(200)
    OP_43(0x11, 0x0, 0x0, 0x14)
    WaitChrThread(0x10, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x92)
    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #177
        (
            "\x07\x05In the morning, they borrowed a couple of boats\x01",
            "and enjoyed an excursion on the lake...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_44(0xA, 0x2)
    OP_DB()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xF, 0x20)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xF, 0x1)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0xD, 0x1)
    ClearChrBattleFlags(0xA, 0x20)
    ClearChrBattleFlags(0xC, 0x20)
    ClearChrBattleFlags(0x9, 0x20)
    ClearChrBattleFlags(0xE, 0x20)
    ClearChrBattleFlags(0xB, 0x20)
    ClearChrBattleFlags(0xF, 0x20)
    ClearChrBattleFlags(0x8, 0x20)
    ClearChrBattleFlags(0xD, 0x20)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xD, 14)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xB, 2)
    SetChrSubChip(0xC, 2)
    SetChrPos(0x101, -900, -650, 43530, 90)
    SetChrPos(0x8, -1320, -400, 42540, 90)
    SetChrPos(0xA, -1370, -650, 41510, 90)
    SetChrPos(0xB, 660, -1800, 48640, 90)
    SetChrPos(0xC, 660, -1800, 47590, 90)
    SetChrPos(0xE, -1010, -650, 44400, 90)
    SetChrFlags(0x9, 0x800)
    SetChrPos(0x9, 2350, -2000, 40500, 0)
    SetChrPos(0xD, 2390, -2000, 45720, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x9, 27)
    OP_6D(1600, -1260, 44290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(295000, 0)
    OP_6E(272, 0)
    LoadEffect(0x0, "scraft\\\\sc000_00.eff")
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_3820():
        OP_6D(2290, -1260, 42460, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3820)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 31)
    SetChrChipByIndex(0xD, 32)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0xD)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xD, 0x618, 0xFFFFF830, 0xAC08, 0x15E, 0xFA0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xD, 0xA5A, 0xFFFFF830, 0xA8B6, 0x15E, 0x1770)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3890():
        OP_96(0xD, 0x8D4, 0xFFFFF830, 0xA370, 0xC8, 0x1F40)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_3890)
    Sleep(100)
    SetChrChipByIndex(0xD, 34)

    def lambda_38B8():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_38B8)
    OP_22(0x208, 0x0, 0x64)

    def lambda_38CD():

        label("loc_38CD")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_38CD")

    QueueWorkItem2(0x9, 2, lambda_38CD)

    def lambda_38DE():
        OP_96(0x9, 0xC6C, 0xFFFFF830, 0xA078, 0xFA, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_38DE)
    SetChrChipByIndex(0x9, 27)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xD, 0x0)
    TurnDirection(0xD, 0x9, 0)

    def lambda_3917():
        OP_96(0xD, 0x604, 0xFFFFF830, 0xA168, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_3917)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 32)
    Sleep(100)
    OP_44(0x9, 0x2)

    def lambda_3948():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3948)

    def lambda_3958():
        OP_8F(0xFE, 0x906, 0xFFFFF830, 0xA0AA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3958)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(100)
    OP_96(0xD, 0x956, 0xFFFFF830, 0xA410, 0xFA, 0x1B58)
    TurnDirection(0xD, 0x9, 0)
    WaitChrThread(0x9, 0x2)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0x9, 30)

    def lambda_39B1():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39B1)
    WaitChrThread(0x9, 0x1)

    def lambda_39C6():
        OP_99(0xFE, 0xA, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39C6)
    Sleep(100)
    OP_43(0x101, 0x0, 0x0, 0xF)
    PlayEffect(0x1, 0x0, 0xD, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 35)
    OP_96(0xD, 0x956, 0xFFFFF830, 0xAAC8, 0xFA, 0x1388)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 36)
    SetChrSubChip(0xD, 3)
    OP_8F(0xD, 0x956, 0xFFFFF830, 0xAEB0, 0x1388, 0x0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 26)
    SetChrFlags(0xD, 0x8000)
    OP_96(0x9, 0x8A2, 0xFFFFF830, 0x9BAA, 0xC8, 0xFA0)
    SetChrChipByIndex(0xD, 32)
    SetChrSubChip(0xD, 0)

    def lambda_3A90():
        OP_8F(0x9, 0x88E, 0xFFFFF830, 0xA78A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3A90)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3AB5():
        OP_96(0xFE, 0x870, 0xFFFFF830, 0xAAC8, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3AB5)
    SetChrChipByIndex(0x9, 27)

    def lambda_3AD8():
        OP_99(0x9, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3AD8)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)

    def lambda_3AF7():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3AF7)

    def lambda_3B05():
        OP_8F(0xFE, 0xA82, 0xFFFFF830, 0xAE24, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3B05)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0x9, 30)

    def lambda_3B31():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B31)
    WaitChrThread(0x9, 0x1)

    def lambda_3B46():
        OP_99(0xFE, 0xA, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B46)

    def lambda_3B56():
        TurnDirection(0xD, 0x9, 0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_3B56)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0xD, 0x4)

    def lambda_3B78():
        OP_96(0xD, 0xC80, 0xFFFFFAEC, 0xB6B2, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3B78)
    WaitChrThread(0xD, 0x2)
    OP_43(0x101, 0x0, 0x0, 0xE)
    Sleep(100)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 31)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0xD, 34)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3BC7():
        OP_96(0xD, 0x898, 0xFFFFF830, 0xAD34, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_3BC7)
    Sleep(100)

    def lambda_3BEA():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3BEA)
    Sleep(100)
    OP_22(0x1FB, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x20)
    OP_43(0x101, 0x0, 0x0, 0xF)
    OP_8F(0x9, 0x708, 0xFFFFF830, 0xA794, 0x1770, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_43(0x101, 0x0, 0x0, 0x10)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_3C7B():
        OP_96(0xFE, 0x816, 0xFFFFF830, 0xAA96, 0xC7, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3C7B)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 37)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x1, 0x3, 0x708)

    def lambda_3CBB():
        OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3CBB)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0x9, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x106, 0x3, 0x0, 0x12)

    def lambda_3D22():
        OP_8F(0x9, 0x6B8, 0xFFFFF830, 0xA53C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_3D22)
    Sleep(200)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    def lambda_3D53():

        label("loc_3D53")

        OP_9E(0xFE, 0x32, 0x0, 0x64, 0x1388)
        OP_48()
        Jump("loc_3D53")

    QueueWorkItem2(0x9, 1, lambda_3D53)
    OP_99(0xD, 0x8, 0xB, 0x5DC)
    OP_99(0xD, 0x8, 0xB, 0x5DC)
    OP_A2(0x5)
    OP_99(0xD, 0x10, 0x12, 0x5DC)

    def lambda_3D8E():
        OP_99(0xFE, 0x18, 0x1B, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3D8E)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    OP_43(0x9, 0x1, 0x0, 0x11)
    WaitChrThread(0xD, 0x2)
    SetChrSubChip(0xD, 32)
    ClearChrFlags(0xD, 0x4)
    OP_44(0xD, 0xFF)

    def lambda_3E12():
        OP_96(0xFE, 0x898, 0xFFFFF830, 0xAD34, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_3E12)

    def lambda_3E30():
        OP_99(0xFE, 0x28, 0x2C, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3E30)
    WaitChrThread(0xD, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xD, 0x2)
    ClearChrFlags(0xD, 0x2)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xD, 0x40)
    OP_8C(0xD, 180, 0)
    SetChrChipByIndex(0xD, 32)
    SetChrSubChip(0xD, 0)
    WaitChrThread(0x9, 0x1)
    Sleep(1000)

    def lambda_3E79():

        label("loc_3E79")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3E79")

    QueueWorkItem2(0x9, 3, lambda_3E79)
    Sleep(200)
    OP_99(0x9, 0x3, 0x0, 0x5DC)
    Fade(250)
    OP_44(0x9, 0x3)
    SetChrFlags(0x9, 0x2)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 31)
    SetChrSubChip(0x9, 3)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #178
        (
            "\x07\x05Noon saw a pleasant lunch, with no small bit\x01",
            "of horseplay...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0xD, 0x8000)
    OP_DB()
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x101, 21)
    SetChrChipByIndex(0xE, 24)
    SetChrChipByIndex(0xD, 23)
    SetChrChipByIndex(0x9, 22)
    SetChrPos(0x18, -11490, 1100, 41030, 0)
    SetChrPos(0x19, -10530, 1100, 41040, 0)
    SetChrPos(0x1A, -5850, 1100, 41090, 0)
    SetChrPos(0x1B, -4630, 1100, 41090, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xD, -11840, -2300, 33400, 270)
    SetChrPos(0x101, -10130, -2300, 33190, 90)
    SetChrPos(0xE, -3920, -2300, 34150, 270)
    SetChrPos(0x9, -2100, -2300, 33480, 90)
    SetChrPos(0xA, -12850, 700, 41400, 90)
    SetChrPos(0x8, -9540, 700, 41200, 270)
    SetChrPos(0xC, -6940, 700, 41230, 90)
    SetChrPos(0xB, -3850, 700, 41270, 270)
    SetChrPos(0xF, -7030, 1400, 40400, 180)
    SetChrSubChip(0xA, 2)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 6)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x1D, -10730, -2000, 33190, 0)
    SetChrPos(0x1E, -3320, -2000, 34150, 0)
    SetChrPos(0x1F, -2700, -2000, 33480, 0)
    SetChrPos(0x20, -11140, -2000, 33500, 0)
    OP_6D(-8220, -2000, 45620, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(370, 0)
    LoadEffect(0x0, "scraft\\\\sc001_05.eff")

    def lambda_4155():

        label("loc_4155")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_4155")

    QueueWorkItem2(0x101, 3, lambda_4155)

    def lambda_4168():

        label("loc_4168")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_4168")

    QueueWorkItem2(0xE, 3, lambda_4168)

    def lambda_417B():

        label("loc_417B")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_417B")

    QueueWorkItem2(0xD, 3, lambda_417B)

    def lambda_418E():

        label("loc_418E")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_418E")

    QueueWorkItem2(0x9, 3, lambda_418E)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_41B0():
        OP_6D(-7960, -2300, 38310, 6000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_41B0)

    def lambda_41C8():
        OP_67(0, 4840, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_41C8)

    def lambda_41E0():
        OP_6C(341000, 6000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_41E0)

    def lambda_41F0():
        OP_6E(465, 6000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_41F0)
    WaitChrThread(0xD, 0x1)
    Sleep(1000)
    OP_DC()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #179
        (
            "\x07\x05And the evening was perfect for setting a fishing\x01",
            "line and letting the hours disappear...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x05Time passed quickly by the idyllic shores of the lake.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3245 end

    def Function_13_42F3(): pass

    label("Function_13_42F3")

    SetChrSubChip(0xE, 2)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Return()

    # Function_13_42F3 end

    def Function_14_4317(): pass

    label("Function_14_4317")

    SetChrSubChip(0xE, 1)
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    Sleep(100)
    SetChrSubChip(0xA, 1)
    Return()

    # Function_14_4317 end

    def Function_15_433B(): pass

    label("Function_15_433B")

    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    Return()

    # Function_15_433B end

    def Function_16_435F(): pass

    label("Function_16_435F")

    SetChrSubChip(0x101, 2)
    Sleep(100)
    SetChrSubChip(0xE, 2)
    Return()

    # Function_16_435F end

    def Function_17_436F(): pass

    label("Function_17_436F")


    def lambda_4375():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4375)
    Sleep(100)

    def lambda_4395():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4395)
    Sleep(100)

    def lambda_43B5():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_43B5)
    Sleep(100)

    def lambda_43D5():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_43D5)
    WaitChrThread(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 29)
    OP_99(0x9, 0x0, 0x3, 0x5DC)
    Return()

    # Function_17_436F end

    def Function_18_4403(): pass

    label("Function_18_4403")

    Sleep(200)

    label("loc_4408")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4460")
    OP_22(0x321, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4458")
    OP_23(0x321)
    Jump("loc_4460")

    label("loc_4458")

    Sleep(100)
    Jump("loc_4408")

    label("loc_4460")

    Return()

    # Function_18_4403 end

    def Function_19_4461(): pass

    label("Function_19_4461")


    def lambda_4467():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4467)
    Sleep(300)

    def lambda_4487():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4487)
    Sleep(300)

    def lambda_44A7():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44A7)
    Sleep(300)

    def lambda_44C7():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44C7)
    Sleep(300)

    def lambda_44E7():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44E7)
    Sleep(300)

    def lambda_4507():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4507)
    Sleep(300)

    def lambda_4527():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4527)
    Sleep(300)

    def lambda_4547():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4547)
    Sleep(300)

    def lambda_4567():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x834, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4567)
    Sleep(300)

    def lambda_4587():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4587)
    Sleep(300)

    def lambda_45A7():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45A7)
    Return()

    # Function_19_4461 end

    def Function_20_45BD(): pass

    label("Function_20_45BD")


    def lambda_45C3():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45C3)
    Sleep(300)

    def lambda_45E3():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45E3)
    Sleep(300)

    def lambda_4603():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4603)
    Sleep(300)

    def lambda_4623():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4623)
    Sleep(300)

    def lambda_4643():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4643)
    Sleep(300)

    def lambda_4663():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4663)
    Sleep(300)

    def lambda_4683():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4683)
    Sleep(300)

    def lambda_46A3():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46A3)
    Sleep(300)

    def lambda_46C3():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x834, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46C3)
    Sleep(300)

    def lambda_46E3():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46E3)
    Sleep(6500)

    def lambda_4703():
        OP_91(0xFE, 0x3E8, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4703)
    Return()

    # Function_20_45BD end

    def Function_21_4719(): pass

    label("Function_21_4719")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_479D")
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(200)
    OP_8C(0xFE, 45, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    OP_8C(0xFE, 45, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(200)
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    Jump("Function_21_4719")

    label("loc_479D")

    Return()

    # Function_21_4719 end

    def Function_22_479E(): pass

    label("Function_22_479E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4822")
    OP_8C(0xFE, 315, 0)
    Sleep(300)
    OP_8C(0xFE, 270, 0)
    Sleep(300)
    OP_8C(0xFE, 225, 0)
    Sleep(200)
    OP_8C(0xFE, 270, 0)
    Sleep(180)
    OP_8C(0xFE, 225, 0)
    Sleep(400)
    OP_8C(0xFE, 270, 0)
    Sleep(250)
    OP_8C(0xFE, 315, 0)
    Sleep(400)
    OP_8C(0xFE, 270, 0)
    Sleep(350)
    OP_8C(0xFE, 315, 0)
    Sleep(250)
    OP_8C(0xFE, 270, 0)
    Sleep(400)
    Jump("Function_22_479E")

    label("loc_4822")

    Return()

    # Function_22_479E end

    def Function_23_4823(): pass

    label("Function_23_4823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_END)), "loc_482E")
    Return()

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4837")
    Return()

    label("loc_4837")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -44960, -2000, 41690, 180)
    OP_6D(-44990, -2000, 38500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    OP_8E(0x101, 0xFFFF5088, 0xFFFFF830, 0x972C, 0x5DC, 0x0)
    Sleep(500)
    OP_6A(0xFF)

    ChrTalk(    #181
        0x101,
        (
            "#1025FAhhhhh, what a pretty sunset.\x02\x03",

            "It's just like that time...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_AD(0x2400C4, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #182
        0x101,
        "#1027F...\x02",
    )

    CloseMessageWindow()

    def lambda_4933():
        OP_67(0, 7200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4933)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x101, 17)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #183
        0x101,
        (
            "#1003FThe sky, the sunset, the water...\x01",
            "It's all just like before.\x02\x03",

            "Everyone's having fun, but...\x02\x03",

            "It's not really the same at all,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x101,
        (
            "#1007F*siiigh* I'm hopeless, aren't I?\x02\x03",

            "I'd made up my mind to chase after\x01",
            "him at my own pace, but...\x02\x03",

            "Mom AND Joshua must be laughing at me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(500)

    ChrTalk(    #185
        0x101,
        (
            "#1025FThat's right.\x02\x03",

            "I did play it once, during the dream.\x02\x03",

            "I wonder if I can do it again?\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    OP_20(0x5DC)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 18)
    OP_0D()
    Sleep(1000)
    OP_21()

    def lambda_4B3E():

        label("loc_4B3E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4B3E")

    QueueWorkItem2(0x101, 0, lambda_4B3E)
    OP_1D(0x46)
    OP_1F(0x64, 0xC8)

    def lambda_4B59():
        OP_6B(3200, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B59)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4823 end

    def Function_24_4B90(): pass

    label("Function_24_4B90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrPos(0x101, -44920, -2000, 38700, 180)
    OP_6D(-44990, -2000, 38500, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 18)

    def lambda_4BF6():

        label("loc_4BF6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4BF6")

    QueueWorkItem2(0x101, 0, lambda_4BF6)
    FadeToBright(1000, 0)
    OP_0D()
    OP_21()
    OP_44(0x101, 0x0)
    Sleep(1000)
    OP_99(0x101, 0x8, 0x9, 0x5DC)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 10)
    OP_0D()
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_DC()
    SetChrChipByIndex(0x101, 17)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #186
        0x101,
        "#1004FHm?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 15)
    SetChrPos(0xE, -40350, -2000, 48090, 188)
    ClearChrFlags(0xE, 0x80)

    def lambda_4C91():
        OP_6D(-43510, -2000, 43790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C91)

    def lambda_4CA9():
        OP_6C(331000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CA9)
    Sleep(1000)

    def lambda_4CBE():

        label("loc_4CBE")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_4CBE")

    QueueWorkItem2(0x101, 3, lambda_4CBE)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #187
        0xE,
        "#1061F#4PHeheh! That was really pretty, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#1015F#5PKevin?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0xF)
    Sleep(500)

    def lambda_4D3A():
        OP_6D(-45120, -2000, 39640, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D3A)

    def lambda_4D52():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D52)
    OP_8F(0xE, 0xFFFF5100, 0xFFFFF830, 0xAABE, 0x7D0, 0x0)

    def lambda_4D76():
        OP_8E(0xE, 0xFFFF5056, 0xFFFFF830, 0x9F06, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4D76)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x3)

    ChrTalk(    #189
        0xE,
        (
            "#1060FI came by 'cause I was curious who was\x01",
            "beltin' out the melodies.\x02\x03",

            "Gotta admit, I didn't think it would be you!\x02\x03",

            "#1061FSo I guess you do have hobbies other'n\x01",
            "sneakers and fishing, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#1008F#6PAhaha... Harmonica playing's kind of out of\x01",
            "character for me, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xE,
        (
            "#1064FNah, not hardly. It suits you.\x02\x03",

            "#1066FGotta be honest, I think you're\x01",
            "better at fishing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1016F#6PHaha! You can just come out and\x01",
            "tell me I'm bad.\x02\x03",

            "Even I don't think I'm really\x01",
            "good at this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xE,
        (
            "#1065FEh... You made a couple technical\x01",
            "mistakes, sure.\x02\x03",

            "#1060FBut what matters in music is the heart.\x02\x03",

            "And that little performance of yours\x01",
            "carried your heart. Trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1025F#6POh...thanks.\x02\x03",

            "#1003F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xE,
        "#1060FMind if I get a little closer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1025F#6POh, uh, sure, go ahead.\x02",
    )

    CloseMessageWindow()

    def lambda_50B0():
        OP_6D(-44990, -2000, 38510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50B0)

    def lambda_50C8():
        OP_8F(0xFE, 0xFFFF4E4E, 0xFFFFF830, 0x966E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_50C8)
    Sleep(50)
    OP_8F(0x101, 0xFFFF51C8, 0xFFFFF830, 0x9678, 0x3E8, 0x0)
    OP_8C(0x101, 270, 200)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xE)
    Sleep(500)

    ChrTalk(    #197
        0xE,
        (
            "#1065F#6P...Got a question I'd like to ask you.\x02\x03",

            "#1067FEstelle, what're you gonna say when you\x01",
            "meet this boyfriend of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1004F#4PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #199
        0xE,
        (
            "#1060F#6PFrom what I've gathered, he left under\x01",
            "what we might call, ah, 'circumstances.'\x01",
            "Heavy ones.\x02\x03",

            "Even if you finally catch up to him...\x02\x03",

            "Have you thought about what you're going\x01",
            "to SAY to him after all this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#1026F#4P...\x02\x03",

            "#1003FI'd convinced myself I was going to drag\x01",
            "him back even if I had to pull him by\x01",
            "the hair.\x02\x03",

            "But...I don't think I can really do\x01",
            "something that forceful...or crazy.\x02\x03",

            "#1007FTo be completely honest, I don't know\x01",
            "if what I have to say will even reach\x01",
            "Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xE,
        (
            "#1063F#6PAnd even knowin' all that,\x01",
            "you're still set on finding him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1003F#4PYeah.\x02\x03",

            "#1025FI've thought a lot about Joshua's\x01",
            "situation, and my own failings.\x02\x03",

            "No matter how hard I try, though, the words\x01",
            "to deal with it all don't come to me when\x01",
            "I just sit around.\x02\x03",

            "#1010FSo...I'll just let the words come when\x01",
            "I finally meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        "#1064F#6PWha?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1025F#4PAfter all, my feelings aren't mine alone,\x01",
            "right?\x02\x03",

            "They're something that grew between Joshua\x01",
            "and I when we were together.\x02\x03",

            "#1012FSo...I think I'll only really be able to\x01",
            "find those words once I see him again.\x02\x03",

            "#1017FOnce we meet, our hearts will do the talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xE,
        "#1064F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006F#4PThat's why I refuse to worry about that\x01",
            "until we find him.\x02\x03",

            "#1016FHeheh. I mean, sometimes I get a little\x01",
            "sentimental, sure, but...\x02\x03",

            "Let's just call that 'lady's privilege.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #207
        0xE,
        (
            "#1068F#6P*siiiiigh* Oh, man.\x02\x03",

            "That didn't go according to the steps at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x101,
        "#1004F#4PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xE,
        (
            "#1065F#6PSTEP ONE!\x01",
            "Estelle is all sentimental and down.\x02\x03",

            "#1063FSTEP TWO!\x01",
            "Estelle worries over a comment from me.\x02\x03",

            "#1062FSTEP THREE!\x01",
            "I follow up nicely.\x02\x03",

            "#1061FSTEP FOUR!\x01",
            "Estelle starts feeling better, and her opinion\x01",
            "of me rises sharply because of it. See: profit!\x02\x03",

            "#1062FThat was the brilliant plan I was AIMING\x01",
            "for, but, uh...\x02\x03",

            "#1068FSomehow you skipped steps two and\x01",
            "three. And thus, four, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1016F#4PAhaha! Sorry, sorry.\x02\x03",

            "#1006FYou're still a good priest, Kevin.\x02\x03",

            "You do pay attention to people with\x01",
            "worries like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xE,
        (
            "#1068F#6PEr...\x02\x03",

            "#1066FWell, it's true, that's part of a priest's job...\x02\x03",

            "I gotta admit I was paying attention to\x01",
            "you for reasons that're more personal,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1004F#4PHuh?\x02\x03",

            "What're you--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xE, 180, 400)

    ChrTalk(    #213
        0xE,
        "#1063F#6PHold that thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1015F#4PWhat? Now I'm...\x02\x03",

            "*sigh* What is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xE,
        (
            "#1067F#6PNot sure. It looks like a boat's approaching.\x02\x03",

            "And I think someone's inside it.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #216
        0x101,
        "#1020F#4PWhat?!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    OP_72(0x3, 0x2)
    OP_71(0x3, 0x40)
    OP_A1(0x10, 0x3)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x1)
    SetChrSubChip(0x12, 5)
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x1)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -44030, -3000, 23480, 180)
    OP_48()
    OP_89(0x12, -43660, -3000, 24200, 0)

    def lambda_5BE5():
        OP_6D(-44650, -2000, 35970, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BE5)

    def lambda_5BFD():
        OP_67(0, 7280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BFD)

    def lambda_5C15():
        OP_6C(229000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C15)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(1700)
    OP_43(0x10, 0x0, 0x0, 0x19)
    WaitChrThread(0x101, 0x1)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(    #217
        0x101,
        "#1020F#2P#3SK-KURT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1501   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_4B90 end

    def Function_25_5CB6(): pass

    label("Function_25_5CB6")

    PlayEffect(0x0, 0x0, 0x10, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_5CF1():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B74, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5CF1)
    Sleep(300)

    def lambda_5D11():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B74, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D11)
    Sleep(300)

    def lambda_5D31():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B75, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D31)
    WaitChrThread(0x10, 0x1)
    OP_22(0x12E, 0x0, 0x4B)
    PlayEffect(0x1, 0xFF, 0x10, 0, -170, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_82(0x0, 0x0)

    def lambda_5D93():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D93)
    Sleep(200)

    def lambda_5DB3():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5DB3)
    Sleep(200)

    def lambda_5DD3():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5DD3)

    def lambda_5DEE():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5DEE)
    Sleep(200)

    def lambda_5E0E():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E0E)
    Sleep(200)

    def lambda_5E2E():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E2E)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_25_5CB6 end

    def Function_26_5E49(): pass

    label("Function_26_5E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC1")
    EventBegin(0x1)

    ChrTalk(    #218
        0x101,
        (
            "#1015FY'know, I probably shouldn't head out\x01",
            "alone without telling anyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5EC1")

    Return()

    # Function_26_5E49 end

    def Function_27_5EC2(): pass

    label("Function_27_5EC2")

    EventBegin(0x1)

    ChrTalk(    #219
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_5EEE():
        OP_6D(-3550, -2000, 29080, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5EEE)

    def lambda_5F06():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5F06)

    def lambda_5F16():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5F16)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #220
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6000")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FC5")
    OP_C0(0xE, 0xC, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)
    Jump("loc_5FE7")

    label("loc_5FC5")

    OP_C0(0xE, 0xD, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)

    label("loc_5FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FFA")
    OP_A2(0x20E0)
    Call(0, 28)

    label("loc_5FFA")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_600F")

    label("loc_6000")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_600F")
    EventEnd(0x1)

    label("loc_600F")

    Return()

    # Function_27_5EC2 end

    def Function_28_6010(): pass

    label("Function_28_6010")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(-2850, -2000, 32880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0xF7, 0x8)
    SetChrFlags(0xF8, 0x8)
    SetChrFlags(0xF9, 0x8)
    SetChrPos(0x101, -2950, -2000, 33410, 180)
    SetChrPos(0x16, 1930, -2000, 40500, 225)
    SetChrChipByIndex(0x16, 42)
    OP_4A(0x16, 255)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #221
        0x101,
        "#1020F#6PWh... What is this fish?!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #222
        0x16,
        "#3PI CAN'T BELIEVE MY EYES!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6125():

        label("loc_6125")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_6125")

    QueueWorkItem2(0x101, 1, lambda_6125)
    OP_6D(-840, -2000, 38510, 1500)

    ChrTalk(    #223
        0x101,
        "#1011FEr, Lloyd...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6172():
        OP_6D(-2330, -2000, 34690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6172)
    OP_8E(0x16, 0xC8, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8E(0x16, 0xFFFFF466, 0xFFFFF830, 0x9678, 0x1388, 0x0)
    OP_8E(0x16, 0xFFFFF498, 0xFFFFF830, 0x8818, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #224
        0x16,
        (
            "#3PThose sienna scales, those crimson\x01",
            "eyes that burn like flame...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x16,
        (
            "#3PThere's no doubt!\x01",
            "It's HIM!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x16,
        "#3P#4SThis is the Guardian of Valleria Lake!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0x101,
        (
            "#1004F#4PSay WHAT?!\x02\x03",

            "You're serious?\x01",
            "I just caught the Guardian?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x16,
        "#3PI never imagined you would catch him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x16,
        (
            "#3PAs the one who gave you your Fishing Book...\x01",
            "Ah, it feels complicated. I'm frustrated and\x01",
            "proud all at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x16,
        "#3PStill. This, too, must be the will of Aidios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x16,
        (
            "#3PAll I can do is admit what you've\x01",
            "accomplished, and give you this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #232
        "\x07\x00Received #1045i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x415, 1)
    Sleep(500)

    ChrTalk(    #233
        0x16,
        (
            "#3PFrom this moment forward, you are now a\x01",
            "Master Fisher, as acknowledged by\x01",
            "the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x16,
        (
            "#3PHowever! Do not be satisfied with this\x01",
            "alone! Always strive further on the path\x01",
            "of the fisherman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1016F#4PA-haha... Yeah, I, uh, I will...\x02\x03",

            "#1015FAnd, uh, not to change the subject,\x01",
            "but...\x02\x03",

            "What IS this, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x16,
        (
            "#3PIt is an identification pass which marks\x01",
            "you as a Master Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x16,
        (
            "#3PAnyone with this will be able to take\x01",
            "advantage of a wonderful service at\x01",
            "the headquarters of the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x16,
        (
            "#3PShould you return to the capital, please,\x01",
            "stop by. We'd love to have you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1000F#4PHuh, okay. I still don't QUITE get what's\x01",
            "going on, but it sounds cool.\x02\x03",

            "I'll make sure to drop in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x16,
        (
            "#3PHeheh. Trust me, it's a service any\x01",
            "fisherman would dream of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x16,
        (
            "#3PAnyway, if you'll excuse me, I need to\x01",
            "decide what my next goal will be now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x16,
        "#3PFarewell!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x16, 0xFFFFF466, 0xFFFFF830, 0x9678, 0x1388, 0x0)
    OP_8E(0x16, 0xC8, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8E(0x16, 0x78A, 0xFFFFF830, 0x9E34, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    SetChrPos(0x16, -8170, 500, 40910, 180)
    SetChrChipByIndex(0x16, 42)
    ClearChrFlags(0x16, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2950, -2000, 33410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2950, -2000, 33410, 180)
    SetChrPos(0x1, -2950, -2000, 33410, 180)
    SetChrPos(0x2, -2950, -2000, 33410, 180)
    SetChrPos(0x3, -2950, -2000, 33410, 180)
    OP_30(0x0)
    ClearChrFlags(0xF7, 0x8)
    ClearChrFlags(0xF8, 0x8)
    ClearChrFlags(0xF9, 0x8)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_A2(0x8)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_28_6010 end

    SaveToFile()

Try(main)

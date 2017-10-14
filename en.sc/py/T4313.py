from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4313   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Chamberlain Raymond',                  # 9
        'Duke Dunan',                           # 10
        'Renne',                                # 11
        'Lt. Colonel Cid',                      # 12
        'Kanone',                               # 13
        'Cassius',                              # 14
        'Richard',                              # 15
        'Senator Walter',                       # 16
        'Ricarda',                              # 17
        'Ambassador Cochrane',                  # 18
        'Warrant Officer Belc',                 # 19
        'Simone',                               # 20
        'Nena',                                 # 21
        'Librarian Pietro',                     # 22
        'Residing Officer Yakumo',              # 23
        'Tourist',                              # 24
        'Tourist',                              # 25
        'Butler Phillip',                       # 26
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT27/CH03004 ._CH',             # 02
        'ED6_DT27/CH03510 ._CH',             # 03
        'ED6_DT27/CH03590 ._CH',             # 04
        'ED6_DT27/CH03123 ._CH',             # 05
        'ED6_DT27/CH03670 ._CH',             # 06
        'ED6_DT27/CH03690 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01230 ._CH',             # 09
        'ED6_DT27/CH03720 ._CH',             # 0A
        'ED6_DT07/CH01310 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
        'ED6_DT07/CH01770 ._CH',             # 0D
        'ED6_DT07/CH01100 ._CH',             # 0E
        'ED6_DT07/CH01490 ._CH',             # 0F
        'ED6_DT07/CH01050 ._CH',             # 10
        'ED6_DT07/CH01160 ._CH',             # 11
        'ED6_DT07/CH02470 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT27/CH03004P._CP',             # 02
        'ED6_DT27/CH03510P._CP',             # 03
        'ED6_DT27/CH03590P._CP',             # 04
        'ED6_DT27/CH03123P._CP',             # 05
        'ED6_DT27/CH03670P._CP',             # 06
        'ED6_DT27/CH03690P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01230P._CP',             # 09
        'ED6_DT27/CH03720P._CP',             # 0A
        'ED6_DT07/CH01310P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
        'ED6_DT07/CH01770P._CP',             # 0D
        'ED6_DT07/CH01100P._CP',             # 0E
        'ED6_DT07/CH01490P._CP',             # 0F
        'ED6_DT07/CH01050P._CP',             # 10
        'ED6_DT07/CH01160P._CP',             # 11
        'ED6_DT07/CH02470P._CP',             # 12
    )

    DeclNpc(
        X                   = -11850,
        Z                   = 0,
        Y                   = 20220,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -16000,
        Z                   = 0,
        Y                   = -38500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14110,
        Z                   = 0,
        Y                   = -8710,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -10410,
        Z                   = 0,
        Y                   = -15620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -14830,
        Z                   = 0,
        Y                   = -14420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 11910,
        Z                   = 0,
        Y                   = 18100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -19030,
        Z                   = 0,
        Y                   = 20590,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -12710,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 20140,
        Z                   = 0,
        Y                   = -42620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 10340,
        Z                   = 0,
        Y                   = -41560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 14120,
        Z                   = 0,
        Y                   = 50600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 15980,
        Z                   = 0,
        Y                   = 50600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -12960,
        Z                   = 0,
        Y                   = -44100,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 18820,
        TriggerRange        = 800,
        ActorX              = -11850,
        ActorZ              = 1500,
        ActorY              = 20220,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14700,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -17800,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21000,
        TriggerZ            = 0,
        TriggerY            = 47000,
        TriggerRange        = 2000,
        ActorX              = -18500,
        ActorZ              = 1500,
        ActorY              = 46500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1500,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10300,
        TriggerZ            = 0,
        TriggerY            = 19220,
        TriggerRange        = 500,
        ActorX              = -10900,
        ActorZ              = 1500,
        ActorY              = 19110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18200,
        TriggerZ            = 0,
        TriggerY            = 51350,
        TriggerRange        = 800,
        ActorX              = 18200,
        ActorZ              = 1800,
        ActorY              = 51350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 35,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14200,
        TriggerZ            = 0,
        TriggerY            = 51310,
        TriggerRange        = 800,
        ActorX              = 14200,
        ActorZ              = 2000,
        ActorY              = 51310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10220,
        TriggerZ            = 0,
        TriggerY            = 51150,
        TriggerRange        = 800,
        ActorX              = 10220,
        ActorZ              = 1200,
        ActorY              = 51150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24340,
        TriggerZ            = 0,
        TriggerY            = 45480,
        TriggerRange        = 800,
        ActorX              = 24340,
        ActorZ              = 500,
        ActorY              = 45480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_50E",          # 00, 0
        "Function_1_67E",          # 01, 1
        "Function_2_6B7",          # 02, 2
        "Function_3_834",          # 03, 3
        "Function_4_839",          # 04, 4
        "Function_5_114A",         # 05, 5
        "Function_6_12E3",         # 06, 6
        "Function_7_1965",         # 07, 7
        "Function_8_1D8F",         # 08, 8
        "Function_9_262C",         # 09, 9
        "Function_10_2824",        # 0A, 10
        "Function_11_29DD",        # 0B, 11
        "Function_12_2D0B",        # 0C, 12
        "Function_13_30CA",        # 0D, 13
        "Function_14_316A",        # 0E, 14
        "Function_15_32CF",        # 0F, 15
        "Function_16_33F9",        # 10, 16
        "Function_17_34B2",        # 11, 17
        "Function_18_3537",        # 12, 18
        "Function_19_3C61",        # 13, 19
        "Function_20_3EB2",        # 14, 20
        "Function_21_5FB6",        # 15, 21
        "Function_22_6005",        # 16, 22
        "Function_23_6061",        # 17, 23
        "Function_24_60C2",        # 18, 24
        "Function_25_6123",        # 19, 25
        "Function_26_6170",        # 1A, 26
        "Function_27_6462",        # 1B, 27
        "Function_28_708F",        # 1C, 28
        "Function_29_7531",        # 1D, 29
        "Function_30_8858",        # 1E, 30
        "Function_31_9FCC",        # 1F, 31
        "Function_32_9FEF",        # 20, 32
        "Function_33_A087",        # 21, 33
        "Function_34_A108",        # 22, 34
        "Function_35_A15B",        # 23, 35
        "Function_36_A1B1",        # 24, 36
        "Function_37_A208",        # 25, 37
        "Function_38_A255",        # 26, 38
    )


    def Function_0_50E(): pass

    label("Function_0_50E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55E")
    SetChrPos(0x8, -15170, 0, 17070, 225)
    SetChrPos(0x13, -16940, 0, 16460, 90)
    SetChrPos(0x14, -15820, 0, 15350, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    label("loc_55E")

    Jump("loc_63E")

    label("loc_561")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5A8")
    SetChrPos(0xF, -14830, 0, -13010, 180)
    SetChrPos(0x14, 18250, 0, 44450, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_63E")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_5B2")
    Jump("loc_63E")

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_625")
    SetChrPos(0xF, -11700, 0, -14320, 274)
    SetChrPos(0x10, -13610, 0, -14320, 93)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x17, 23640, 0, 44900, 0)
    SetChrPos(0x18, 25640, 0, 44900, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_END)), "loc_622")
    ClearChrFlags(0x19, 0x80)

    label("loc_622")

    Jump("loc_63E")

    label("loc_625")

    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_65D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_67D")

    label("loc_65D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_669"),
        (SWITCH_DEFAULT, "loc_67D"),
    )


    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_67A")

    Jump("loc_67D")

    label("loc_67D")

    Return()

    # Function_0_50E end

    def Function_1_67E(): pass

    label("Function_1_67E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E")
    OP_64(0x0, 0x1)

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_6A5")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x5, 0x1)

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B6")
    OP_72(0x7, 0x4)

    label("loc_6B6")

    Return()

    # Function_1_67E end

    def Function_2_6B7(): pass

    label("Function_2_6B7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_81E")

    label("loc_6DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_81E")

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_81E")

    label("loc_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_81E")

    label("loc_727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_81E")

    label("loc_740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_81E")

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_81E")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_81E")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_81E")

    label("loc_7A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_81E")

    label("loc_7BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_81E")

    label("loc_7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_81E")

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_81E")

    label("loc_808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_81E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_81E")

    label("loc_833")

    Return()

    # Function_2_6B7 end

    def Function_3_834(): pass

    label("Function_3_834")

    Call(0, 4)
    Return()

    # Function_3_834 end

    def Function_4_839(): pass

    label("Function_4_839")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A24")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8F9")

    ChrTalk(    #0
        0x8,
        (
            "Just doing nothing is nerve-racking,\x01",
            "so I've decided to start cleaning the\x01",
            "villa from top to bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Now we just have to wait for\x01",
            "the queen's orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A21")

    label("loc_8F9")


    ChrTalk(    #2
        0x8,
        (
            "Just what in Aidios' name\x01",
            "is going on...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Just doing nothing is nerve-racking,\x01",
            "so I've decided to start cleaning the\x01",
            "villa from top to bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Idle hands make for idle thoughts, as the\x01",
            "saying goes. And since all of my idle thoughts\x01",
            "are filled with worry...I'd much rather work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_A21")

    TalkEnd(0x8)

    label("loc_A24")

    Jump("loc_1149")

    label("loc_A27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_D00")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 2)), scpexpr(EXPR_END)), "loc_ABD")

    ChrTalk(    #5
        0x8,
        (
            "A lot happened, but I'm glad things\x01",
            "were resolved in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "I'm sorry we ended up relying\x01",
            "on you so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFA")

    label("loc_ABD")


    ChrTalk(    #7
        0x8,
        "Ah, you all are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Is Renne not with you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1003FRenne...returned to her parents.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "Really?! You found her parents?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "I was worried, I admit, having\x01",
            "heard some terrible events had\x01",
            "occurred in the capital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "I see. That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1005FIt's not good at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "Eep?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1009FI'm gonna catch her and\x01",
            "drag her back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "D-Drag her back? Was there\x01",
            "a problem with her parents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I've heard more stories than I would have cared\x01",
            "for of parents taking out their troubles on their\x01",
            "children or raising them in poor environments.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1662)

    label("loc_CFA")

    TalkEnd(0x8)
    Jump("loc_1149")

    label("loc_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_F5F")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 1)), scpexpr(EXPR_END)), "loc_D71")

    ChrTalk(    #18
        0x8,
        (
            "I'm relieved to hear Renne\x01",
            "opened up to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "I hope you find her parents soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F59")

    label("loc_D71")

    TurnDirection(0x8, 0x12F, 0)

    ChrTalk(    #20
        0x8,
        "Why, if it isn't Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12F,
        (
            "#261FAh, mister butler!\x02\x03",

            "#265FAhaha, will you play\x01",
            "with Renne today too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Ah...haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "I'm sorry, but I have work today,\x01",
            "so I'll have to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12F,
        (
            "#268FMen are so boring.\x02\x03",

            "#266FIt's always work, work, work,\x01",
            "and they never have time to\x01",
            "play with me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #25
        0x8,
        (
            "Ghk...\x01",
            "Right through the heart...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #26
        0x8,
        (
            "In any case, I'm relieved to\x01",
            "see how much she's opened\x01",
            "up to you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1016FAh...haha, yup,\x01",
            "she sure has.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1661)

    label("loc_F59")

    TalkEnd(0x8)
    Jump("loc_1149")

    label("loc_F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_FF3")
    TalkBegin(0x8)

    ChrTalk(    #28
        0x8,
        "Honestly, I wasn't sure what to do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "However, knowing that she's in\x01",
            "the guild's hands sets me at ease.\x01",
            "I leave her to you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1149")

    label("loc_FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1011")
    Call(0, 27)
    Jump("loc_1149")

    label("loc_1011")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_108C")

    ChrTalk(    #30
        0x8,
        "*sigh* Just where is that girl hiding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "The villa isn't exactly small.\x01",
            "She could be hiding anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1146")

    label("loc_108C")


    ChrTalk(    #32
        0x8,
        (
            "Hey, how's it going?\x01",
            "Find the girl yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007FNope. No luck so far.\x02\x03",

            "#1006FI'm gonna try searching\x01",
            "for a few more hiding spots\x01",
            "before calling it quits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1146")

    TalkEnd(0x8)

    label("loc_1149")

    Return()

    # Function_4_839 end

    def Function_5_114A(): pass

    label("Function_5_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 0)), scpexpr(EXPR_END)), "loc_1220")
    TalkBegin(0x9)

    ChrTalk(    #35
        0x9,
        (
            "#222FLet me guess--you said\x01",
            "something to Phillip, didn't you?\x02\x03",

            "Every time we meet lately,\x01",
            "he pesters me with lectures\x01",
            "on this and that...\x02\x03",

            "#224FReally, just who does he\x01",
            "think he's talking to?!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Jump("loc_12E2")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_127E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")
    Call(0, 26)
    Jump("loc_127B")

    label("loc_1236")

    TalkBegin(0x9)

    ChrTalk(    #36
        0x9,
        (
            "#224FRrrrgh! Take that girl with\x01",
            "you and get out of here!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_127B")

    Jump("loc_12E2")

    label("loc_127E")

    TalkBegin(0x9)

    ChrTalk(    #37
        0x9,
        (
            "#222FA girl in a white dress?\x02\x03",

            "#224FI don't know any such girl!\x01",
            "Now, get out of my room!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_12E2")

    Return()

    # Function_5_114A end

    def Function_6_12E3(): pass

    label("Function_6_12E3")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_135B")

    ChrTalk(    #38
        0xFE,
        (
            "This is my first time meeting\x01",
            "Ambassador Cochrane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "She has...quite the sharp tongue.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1961")

    label("loc_135B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_15B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #40
        0xFE,
        "Ha ha, don't mind my wife.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "She knows very little about politics.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B6")

    label("loc_13B7")


    ChrTalk(    #42
        0xFE,
        (
            "The Republic's Parliament has had\x01",
            "many a divisive argument concerning\x01",
            "the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "One particular hurdle naturally arose\x01",
            "from the Citizen's Union Party, known\x01",
            "for their staunch dislike of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I'm sure the president had a rough\x01",
            "time of it working to counter extremist\x01",
            "opposition, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "That new engine was enticing enough\x01",
            "for him to easily win majority favor this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "With Queen Alicia's skills, I imagine\x01",
            "she could even serve as the president\x01",
            "of the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_15B6")

    Jump("loc_1961")

    label("loc_15B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_17B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(    #47
        0xFE,
        (
            "Haha, it seems her interest is far\x01",
            "more in touring the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Well, the Republic is where so many opinions\x01",
            "and viewpoints exist in harmony, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AE")

    label("loc_166D")


    ChrTalk(    #49
        0xFE,
        (
            "My wife unfortunately lacks a fundamental\x01",
            "understanding of politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Well, this time I had her accompany me\x01",
            "in an attempt to change that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Haha, it seems her interest is\x01",
            "far more in touring the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Well, the Republic is where so many opinions\x01",
            "and viewpoints exist in harmony, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17AE")

    Jump("loc_1961")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(    #53
        0xFE,
        (
            "I am Walter, a senator in the\x01",
            "Republic's Parliament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I've come a bit early in order to\x01",
            "inspect the site and prepare for\x01",
            "the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1961")

    label("loc_185A")


    ChrTalk(    #55
        0xFE,
        (
            "I am Walter, a senator in the\x01",
            "Republic's Parliament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I've come a bit early in order to\x01",
            "inspect the site and prepare for\x01",
            "the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "And what a remarkable villa this is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Indeed, it is more than sufficient\x01",
            "for hosting the ceremony.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1961")

    TalkEnd(0xF)
    Return()

    # Function_6_12E3 end

    def Function_7_1965(): pass

    label("Function_7_1965")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(    #59
        0xFE,
        (
            "I've told my husband time and\x01",
            "time again, but he simply won't\x01",
            "listen to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "He rattles on about political\x01",
            "savviness, but he's hardly aware\x01",
            "of his own meager position. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1B85")

    ChrTalk(    #61
        0xFE,
        (
            "For a little fish like my husband\x01",
            "to speak of the president or Queen\x01",
            "Alicia is absolutely ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Maybe if he learned to show some\x01",
            "humility, he might actually become\x01",
            "as important as he thinks he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "He says he's come here to work, but\x01",
            "funny how someone so important hasn't\x01",
            "been able to meet with the ambassador.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1CC9")

    ChrTalk(    #64
        0xFE,
        (
            "If only he'd realize that there's never\x01",
            "been a need for a senator of his standing\x01",
            "to attend the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I understand, though; he's excited to\x01",
            "have finally been elected, so I'll let him\x01",
            "have his fun here in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I get to tour Grancel while he's at it,\x01",
            "so it's a victory in my book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8B")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D8B")

    ChrTalk(    #67
        0xFE,
        (
            "The Liberl Kingdom is quite small\x01",
            "on the map, and yet it feels anything\x01",
            "but now that I'm actually here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The people are kind, and no matter\x01",
            "where I go, the view is breathtaking!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    TalkEnd(0x10)
    Return()

    # Function_7_1965 end

    def Function_8_1D8F(): pass

    label("Function_8_1D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 3)), scpexpr(EXPR_END)), "loc_1D9B")
    SetChrFlags(0xFE, 0x10)

    label("loc_1D9B")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2628")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CC, 3)), scpexpr(EXPR_END)), "loc_1FF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1EAB")

    ChrTalk(    #69
        0x11,
        (
            "#1113FIf this is a formal inspection, then\x01",
            "it would be natural to go through the\x01",
            "embassy first.\x02\x03",

            "Or are the taxpayers footing the bill\x01",
            "for this 'inspection' while blissfully unaware\x01",
            "that is it a mere excuse to tour the capital?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF6")

    label("loc_1EAB")


    ChrTalk(    #70
        0x11,
        (
            "#1113FNow, then, Senator Walter...\x02\x03",

            "I would like to thank you for coming\x01",
            "all this way, but...\x02\x03",

            "#1112FIf this is a formal inspection, then\x01",
            "it would be natural to go through the\x01",
            "embassy first.\x02\x03",

            "Or are the taxpayers footing the bill\x01",
            "for this 'inspection' while blissfully unaware\x01",
            "that is it a mere excuse to tour the capital?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1FF6")

    Jump("loc_2628")

    label("loc_1FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A0")

    ChrTalk(    #71
        0x11,
        (
            "#1110FHello, everyone. And lovely to see\x01",
            "you as always, Zin.\x02\x03",

            "I wasn't expecting to meet you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x108,
        "#070FHaha, we were just passing through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20E2")

    label("loc_20A0")


    ChrTalk(    #73
        0x11,
        (
            "#1110FHello, everyone.\x02\x03",

            "I wasn't expecting to meet you here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E2")


    ChrTalk(    #74
        0x101,
        "#1000FHello, Ambassador Cochrane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#1110FYour timing is perfect; I received\x01",
            "a report from Liberl regarding that\x01",
            "letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1011FOh, you did?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#1113FYes. I've been told that it was subversive\x01",
            "activity by remnants of the Intelligence\x01",
            "Division's Special Ops forces.\x02\x03",

            "#1110FAlthough I'm certain that Queen Alicia\x01",
            "has long suspected as much.\x02\x03",

            "I have a hunch that there's more to\x01",
            "it than what the reports say, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1016FAh...hahaha...\x02\x03",

            "(T-Talking to foreigners always\x01",
            "makes me so nervous.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2374")

    ChrTalk(    #79
        0x106,
        (
            "#050F(C'mon, show some guts.)\x02\x03",

            "(If you're a bracer, you need to be\x01",
            "able to manage basic negotiations\x01",
            "and conversations with anyone.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241F")

    label("loc_2374")


    ChrTalk(    #80
        0x103,
        (
            "#020F(It's all a matter of experience and\x01",
            "getting used to it.)\x02\x03",

            "(If you're a bracer, you need to be\x01",
            "able to manage basic negotiations\x01",
            "and conversations with anyone.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241F")


    ChrTalk(    #81
        0x11,
        (
            "#1110FQueen Alicia seems to be quite the\x01",
            "suffering type.\x02\x03",

            "Though, I wonder if she isn't relieved\x01",
            "to have the coup d'etat settled.\x02\x03",

            "I've also heard rumors in the embassy\x01",
            "that you played quite a part in that affair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1016FNo, not at all... Just doin' my job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#1111FAs much as I would love to continue this\x01",
            "conversation, I'm afraid you've come at a\x01",
            "very busy time for me.\x02\x03",

            "#1110FI hope to get the chance to speak with\x01",
            "you more next time, Estelle Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1000FS-Sure. Well, uh, if you'll excuse us...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1663)

    label("loc_2628")

    TalkEnd(0x11)
    Return()

    # Function_8_1D8F end

    def Function_9_262C(): pass

    label("Function_9_262C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_26DF")

    ChrTalk(    #85
        0xFE,
        (
            "It's frustrating that we couldn't track\x01",
            "that giant orbal construct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "If something like that attacks again,\x01",
            "how should we even respond...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2820")

    label("loc_26DF")


    ChrTalk(    #87
        0xFE,
        (
            "Sure, you guys had the help of the Royal\x01",
            "Guard, but I still don't have a clue how you\x01",
            "were able to destroy that monster tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "You bracers are incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Still, it's frustrating that we couldn't\x01",
            "track that giant orbal construct.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "If something like that attacks again,\x01",
            "how should we even respond...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2820")

    TalkEnd(0x12)
    Return()

    # Function_9_262C end

    def Function_10_2824(): pass

    label("Function_10_2824")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(    #91
        0xFE,
        "No way am I gonna lose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "We're having a contest to see who can\x01",
            "clean the most rooms, and you can bet\x01",
            "that I have every intention of cleaning house!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D7")

    Jump("loc_29D9")

    label("loc_28DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_298B")

    ChrTalk(    #93
        0xFE,
        (
            "Poor Colonel Cid and his\x01",
            "men haven't been able to get a\x01",
            "wink of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Being in the army must be hard.\x01",
            "I hope they don't work themselves\x01",
            "sick...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D9")

    label("loc_298B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_29D9")
    TurnDirection(0xFE, 0x12F, 0)

    ChrTalk(    #95
        0xFE,
        "Oh, hello, Renne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Playing with your new friends,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D9")

    TalkEnd(0x13)
    Return()

    # Function_10_2824 end

    def Function_11_29DD(): pass

    label("Function_11_29DD")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A76")

    ChrTalk(    #97
        0xFE,
        (
            "Oh, Simone, you're totally getting\x01",
            "played by Raymond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "But, if you're going to call it a\x01",
            "contest, then I won't hold back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A76")

    Jump("loc_2CEF")

    label("loc_2A79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2AF7")

    ChrTalk(    #99
        0xFE,
        (
            "La la laa... ♪\x01",
            "Lalana lala lalala... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Dust up, dust down,\x01",
            "dust right and left... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFA")

    label("loc_2AF7")


    ChrTalk(    #101
        0xFE,
        (
            "We have a lot of things on display\x01",
            "here, so it's pretty hard to keep it\x01",
            "all clean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I like to think of it as a chance to\x01",
            "show off my cleaning skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "La la laa... ♪\x01",
            "Lalana lala lalala... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Dust up, dust down,\x01",
            "dust right and left... ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2BFA")

    Jump("loc_2CEF")

    label("loc_2BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2C86")

    ChrTalk(    #105
        0xFE,
        (
            "La la laa... ♪\x01",
            "Lalana lala lalala... ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Clean until it's all shiiiny... ♪\x01",
            "Clean until it's all tiiidy... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEF")

    label("loc_2C86")


    ChrTalk(    #107
        0xFE,
        (
            "This room is going to be used\x01",
            "for mission planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "I should really finish cleaning soon...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2CEF")

    TalkEnd(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2D0A")
    SetChrFlags(0xFE, 0x10)

    label("loc_2D0A")

    Return()

    # Function_11_29DD end

    def Function_12_2D0B(): pass

    label("Function_12_2D0B")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DC5")

    ChrTalk(    #109
        0xFE,
        (
            "Of course, there aren't many people\x01",
            "who come here in the first place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I lived in an age without orbal energy,\x01",
            "so it doesn't cause me any real problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC5")

    Jump("loc_30C6")

    label("loc_2DC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2E81")

    ChrTalk(    #111
        0xFE,
        (
            "The soldiers brought out a map of\x01",
            "Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "They said they were going to search\x01",
            "for a 'giant orbal doll' on the lake,\x01",
            "but whatever could that mean?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C6")

    label("loc_2E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2F84")

    ChrTalk(    #113
        0xFE,
        (
            "Until the signing ceremony finishes,\x01",
            "citizens won't be allowed entry here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "*sigh* That will make this room all\x01",
            "the quieter, won't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Maybe I can get the soldiers\x01",
            "around here to crack open a nice\x01",
            "book or two. I'm sure they'd love it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C6")

    label("loc_2F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_306E")

    ChrTalk(    #116
        0xFE,
        (
            "A quiet atmosphere is ideal\x01",
            "for reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "And as quiet as this place is,\x01",
            "it's the perfect locations, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Most of the citizens who come\x01",
            "are here for either the garden or\x01",
            "the exhibits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "A bit sad, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C6")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_30C6")

    ChrTalk(    #120
        0xFE,
        "Is there a book you're looking for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "...A girl? No, I haven't seen her.\x02",
    )

    CloseMessageWindow()

    label("loc_30C6")

    TalkEnd(0x15)
    Return()

    # Function_12_2D0B end

    def Function_13_30CA(): pass

    label("Function_13_30CA")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3166")

    ChrTalk(    #122
        0xFE,
        (
            "I'm only here today to accompany\x01",
            "Ambassador Cochrane.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "If you're looking for Elsa, she is\x01",
            "currently visiting Senator Walter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3166")

    TalkEnd(0x16)
    Return()

    # Function_13_30CA end

    def Function_14_316A(): pass

    label("Function_14_316A")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3221")

    ChrTalk(    #124
        0xFE,
        (
            "Whoa, this seat used to belong to\x01",
            "the late Edgar III?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Makes sense. The butt indent in\x01",
            "its cushion DOES leave a rather\x01",
            "noble 'impression.' Heh heh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CB")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_32CB")

    ChrTalk(    #126
        0xFE,
        (
            "This pot presented by the Republic\x01",
            "ambassador is quite lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Yep, the Republic sure has some\x01",
            "nice pottery. I can spot their quality\x01",
            "from an arge away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CB")

    TalkEnd(0x17)
    Return()

    # Function_14_316A end

    def Function_15_32CF(): pass

    label("Function_15_32CF")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3360")

    ChrTalk(    #128
        0xFE,
        (
            "My sister was badmouthing the\x01",
            "chair up and down until she read\x01",
            "the label.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "...Aaaand her jokes suck,\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F5")

    label("loc_3360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_33F5")

    ChrTalk(    #130
        0xFE,
        "That's...an Imperial pot, Sis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "It's written right on the label!\x01",
            "All you have to do is read it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "Talk about eye-roll inducing...\x02",
    )

    CloseMessageWindow()

    label("loc_33F5")

    TalkEnd(0x18)
    Return()

    # Function_15_32CF end

    def Function_16_33F9(): pass

    label("Function_16_33F9")

    TalkBegin(0x19)

    ChrTalk(    #133
        0x19,
        (
            "#720FI believe...\x02\x03",

            "I believe His Grace will someday\x01",
            "awaken to his duty.\x02\x03",

            "Until that day comes, I, Phillip,\x01",
            "will serve as best I am able in mind\x01",
            "and body until I am no more.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x19)
    Return()

    # Function_16_33F9 end

    def Function_17_34B2(): pass

    label("Function_17_34B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C1")
    Call(0, 18)
    Jump("loc_3536")

    label("loc_34C1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #134
        "\x07\x05There is a large dining table.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #135
        "\x07\x05There's no one below the table.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_3536")

    Return()

    # Function_17_34B2 end

    def Function_18_3537(): pass

    label("Function_18_3537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3555")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_3555")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #136
        "\x07\x05There is a large dining table.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_391E")
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -17710, 0, 44750, 360)
    SetChrPos(0x104, -17930, 0, 43630, 360)
    SetChrPos(0xF7, -19230, 0, 43930, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3612")
    SetChrPos(0x105, -16800, 0, 43480, 360)
    Jump("loc_3653")

    label("loc_3612")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3634")
    SetChrPos(0x107, -16800, 0, 43480, 360)
    Jump("loc_3653")

    label("loc_3634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3653")
    SetChrPos(0x108, -16800, 0, 43480, 360)

    label("loc_3653")

    OP_6D(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #137
        0x101,
        "#1004FMaybe she's hiding under here?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #138
        0x101,
        (
            "#1015FHmmm...\x02\x03",

            "#1016FHaha... Yeah, didn't think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x104,
        (
            "#032FAhem! Putting that aside...\x02\x03",

            "Bending over in your current\x01",
            "outfit may not be wise, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x104,
        (
            "#031FHow to put this delicately...\x01",
            "Your unmentionables are now\x01",
            "quite mentionable.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x101, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    TurnDirection(0x101, 0x104, 600)

    ChrTalk(    #142
        0x101,
        "#1019FE x c u s e  m e?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38BD")

    ChrTalk(    #143
        0x106,
        (
            "#552FHe's not wrong, Estelle.\x02\x03",

            "You ain't wearin' shorts anymore,\x01",
            "so be careful, yeah?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_38BD")


    ChrTalk(    #144
        0x103,
        (
            "#524FHe's right, Estelle.\x02\x03",

            "You're wearing a skirt, remember?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FF")


    ChrTalk(    #145
        0x101,
        "#1013FUmmm... R-Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BBB")

    label("loc_391E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -17710, 0, 44750, 360)
    SetChrPos(0xF7, -17930, 0, 43630, 360)
    SetChrPos(0xF8, -19230, 0, 43930, 45)
    SetChrPos(0xF9, -16800, 0, 43480, 360)
    OP_6D(-17730, 0, 44700, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(1380, 0)
    OP_6C(40000, 0)
    OP_6E(504, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #146
        0x101,
        "#1004FMaybe she's hiding under here?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #147
        0x101,
        (
            "#1015FHmmm...\x02\x03",

            "#1016FHaha... Yeah, didn't think so.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB3")

    ChrTalk(    #148
        0x106,
        (
            "#551FUh... Estelle?\x02\x03",

            "You ain't wearin' any shorts anymore,\x01",
            "remember, so, uh, try not to bend over\x01",
            "like...that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0F")

    label("loc_3AB3")


    ChrTalk(    #149
        0x103,
        (
            "#025FAh, Estelle?\x02\x03",

            "You aren't wearing shorts anymore,\x01",
            "so be careful when bending over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0F")


    ChrTalk(    #150
        0x101,
        "#1013FWha...? OH!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0x101, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #151
        0x101,
        "#1008FAhaha... Whoops.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B9E")

    ChrTalk(    #152
        0x106,
        "#552F*sigh*\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BBB")

    label("loc_3B9E")


    ChrTalk(    #153
        0x103,
        "#524F*sigh* Honestly...\x02",
    )

    CloseMessageWindow()

    label("loc_3BBB")

    OP_A2(0x160E)
    OP_28(0x89, 0x1, 0x8)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(-17930, 0, 43830, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -17930, 0, 43830, 180)
    SetChrPos(0x1, -17930, 0, 43830, 180)
    SetChrPos(0x2, -17930, 0, 43830, 180)
    SetChrPos(0x3, -17930, 0, 43830, 180)
    Sleep(500)
    FadeToBright(500, 0)
    EventEnd(0x0)
    Return()

    # Function_18_3537 end

    def Function_19_3C61(): pass

    label("Function_19_3C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E62")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #154
        "\x07\x05A big, scarlet pot sits here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #155
        0x101,
        (
            "#1006FHeeey, this is the pot that had the\x01",
            "spare key when we freed the manor!\x02\x03",

            "This is sort of an actual kid-sized pot,\x01",
            "so maybe she's in here.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC8")

    ChrTalk(    #156
        0x106,
        (
            "#053FAre you kidding me?\x02\x03",

            "#555FFor one thing, how the hell would\x01",
            "she squeeze through the opening?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E33")

    label("loc_3DC8")


    ChrTalk(    #157
        0x103,
        (
            "#025FI doubt that.\x02\x03",

            "#524FUnless you think she's so skinny\x01",
            "as to squeeze through THAT thin\x01",
            "an opening?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E33")


    ChrTalk(    #158
        0x101,
        "#1008FOh, haha, good point.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x160F)
    OP_28(0x89, 0x1, 0x10)
    EventEnd(0x1)
    Jump("loc_3EB1")

    label("loc_3E62")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #159
        "\x07\x05A big, scarlet pot sits here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_3EB1")

    Return()

    # Function_19_3C61 end

    def Function_20_3EB2(): pass

    label("Function_20_3EB2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC9")
    Call(0, 32)
    Call(0, 33)

    label("loc_3EC9")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x9, -15000, 0, -43330, 180)
    OP_4A(0x9, 255)
    OP_67(0, 6640, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_69(0x9, 0x0)
    FadeToBright(2000, 0)
    OP_A2(0x0)
    OP_43(0x9, 0x1, 0x0, 0x15)
    OP_0D()
    Sleep(1000)
    OP_4A(0x9, 1)

    ChrTalk(    #160
        0x9,
        (
            "#222FHe's late! TOO LATE, I say!\x02\x03",

            "Curse you, Phillip! How much time\x01",
            "does it take just to purchase a magazine\x01",
            "and some donuts?!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 1)
    OP_A3(0x0)
    OP_A6(0x1)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F61")

    def lambda_3FFA():
        OP_6D(-14340, 0, -44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3FFA)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0xF7, 0x1, 0x0, 0x17)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #161
        0x9,
        "#224F#6PHow long does he intend to keep me--\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #162
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        "#223F#6PY-Y-Y...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #164
        0x9,
        "#226F#3S#6PYOUUUUU!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_411D")

    ChrTalk(    #165
        0x106,
        "#555F#4PUh, what's up with this dude?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4173")

    label("loc_411D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4173")

    ChrTalk(    #166
        0x103,
        (
            "#023F#4POh! Didn't I see this noble in the\x01",
            "castle during the coup?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4173")


    ChrTalk(    #167
        0x101,
        (
            "#1025F#6PSo this is where you've been,\x01",
            "Duke Dunan.\x02\x03",

            "#1016FWhat's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "#222F#6PARGH! Have you no SHAME,\x01",
            "you brigand?!\x02\x03",

            "Because of you... All because\x01",
            "of YOU...\x02\x03",

            "#224FI have been forced into this life\x01",
            "of shame! House arrest, of all\x01",
            "things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1007F#6POkay, I don't think it's really fair\x01",
            "to say it's 'our' fault.\x02\x03",

            "You're the one who bought into\x01",
            "Colonel Richard's plan, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43D4")

    ChrTalk(    #170
        0x108,
        (
            "#070FYou should probably count yourself\x01",
            "lucky it's only house arrest, given what\x01",
            "you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x104,
        (
            "#035FWere this Erebonia, your 'nobility'\x01",
            "would only serve to speed you to\x01",
            "the gallows.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4548")

    label("loc_43D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4486")

    ChrTalk(    #172
        0x108,
        (
            "#074FYou should probably count yourself\x01",
            "lucky it's only house arrest.\x02\x03",

            "#070FAnywhere else, and you'd be facing\x01",
            "jail time at best, even if you are nobility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4548")

    label("loc_4486")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4548")

    ChrTalk(    #173
        0x104,
        (
            "#035FYou should be grateful you live in\x01",
            "a kingdom as forgiving and merciful\x01",
            "as Liberl.\x02\x03",

            "#030FWere this Erebonia, your 'nobility'\x01",
            "would only serve to speed you to the\x01",
            "gallows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4548")


    ChrTalk(    #174
        0x9,
        (
            "#226F#6PErgh...\x02\x03",

            "#222FI confess that imprisoning\x01",
            "Her Majesty was out of line,\x01",
            "perhaps.\x02\x03",

            "Richard may have suggested it,\x01",
            "but I should have gainsaid him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1006F#6PSo you can actually admit you were\x01",
            "wrong about that whole deal? That's\x01",
            "pretty humble, coming from you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#225F#6PDo not misunderstand me. I love and\x01",
            "respect Her Majesty.\x02\x03",

            "As both a ruler and an aunt, she is\x01",
            "utterly above reproach.\x02\x03",

            "#224FBut to consider naming a little girl like\x01",
            "Klaudia as her successor is simply\x01",
            "madness! Unacceptable insanity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1009F#6PNow just a second!\x02\x03",

            "Kloe's smart, studious, kind, merciful...\x01",
            "She's got all kinds of virtues that attract\x01",
            "people to her!\x02\x03",

            "Where do you get off in calling her a\x01",
            "'little girl,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        (
            "#220F#6PHmph. That's not my point.\x02\x03",

            "It may well be that she is possessed\x01",
            "of incredible potential, yes.\x02\x03",

            "But does she really possess the\x01",
            "mindset required to become the next\x01",
            "queen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#1026F#6POh... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x9,
        (
            "#220F#6PKlaudia has always seemed 'allergic'\x01",
            "to attending public ceremonies.\x02\x03",

            "I am far better known among the citizenry,\x01",
            "while she remains a veritable ghost.\x02\x03",

            "She has not once publicly demonstrated\x01",
            "that she is ready to stand above others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1003F#6PStill...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#222F#6PWhy, from what I understand, she's\x01",
            "hiding her true identity while living as\x01",
            "a student.\x02\x03",

            "And as if that weren't enough, she wastes\x01",
            "her time at some backwater orphanage?\x02\x03",

            "#225FShe should be presiding OVER the\x01",
            "common rabble at ceremonies, not\x01",
            "wallowing in the mud with them!\x02\x03",

            "#224FTHAT is the purpose of nobility!\x01",
            "To stand above all other men in lordship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1002F#6P...\x02\x03",

            "#1007FI'll admit, I don't really know much about\x01",
            "the 'purpose' of nobility, so...\x02\x03",

            "You might have a point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x9,
        "#221F#6PWa-ha-ha! Of course I do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#1002F#6PBut I can say this:\x02\x03",

            "Kloe is trying her very hardest to figure out\x01",
            "what she wants to be, and is helping US out\x01",
            "in the middle of her own problems.\x02\x03",

            "#1005FAnd she sure as hell is doing a LOT more\x01",
            "than some duke who sits around doing\x01",
            "nothing because he's under 'house arrest'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#226F#6PWHAT?! YOU DARE--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1006F#6PYou can judge whether Kloe can be a\x01",
            "queen once she's found her answer.\x02\x03",

            "Heck, I bet even YOU'LL accept her then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x9,
        (
            "#226F#6PGyuuh...\x02\x03",

            "#222FRrrgh, this is absurd!\x02\x03",

            "#224FI will deal with this no further!\x01",
            "Begone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1005F#6PTrust me, I don't wanna stick around!\x02\x03",

            "#1007FThough, come to think of it, I need to.\x01",
            "I gotta ask one thing.\x02\x03",

            "#1015FHas a girl in a white dress come by\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#222F#6PWhat are you talking--\x02\x03",

            "#224FNo, no little girls have come by!\x01",
            "BEGONE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1019F#6PYeah, sure.\x01",
            "Enjoy your donuts or whatever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F94")

    label("loc_4F61")


    def lambda_4F67():
        OP_6D(-14340, 0, -44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F67)
    OP_43(0x101, 0x1, 0x0, 0x16)
    OP_43(0x105, 0x1, 0x0, 0x17)
    OP_43(0xF7, 0x1, 0x0, 0x18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FA6")
    OP_43(0x104, 0x1, 0x0, 0x19)
    Jump("loc_4FD3")

    label("loc_4FA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FBE")
    OP_43(0x107, 0x1, 0x0, 0x19)
    Jump("loc_4FD3")

    label("loc_4FBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FD3")
    OP_43(0x108, 0x1, 0x0, 0x19)

    label("loc_4FD3")

    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #192
        0x9,
        (
            "#224F#6PBLAST IT! How long does he\x01",
            "intend to keep me--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #193
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #194
        0x105,
        "#043F#4POh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#223F#6PY-Y-Y...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #196
        0x9,
        "#226F#3S#6PYOUUUUU!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50EB")

    ChrTalk(    #197
        0x106,
        "#555F#2PUh, what's up with this dude?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5141")

    label("loc_50EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5141")

    ChrTalk(    #198
        0x103,
        (
            "#023F#2POh! Didn't I see this noble in the\x01",
            "castle during the coup?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5141")


    ChrTalk(    #199
        0x101,
        "#1019F#6PDuke Dunan... Oh, joy of joys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x105,
        (
            "#542F#4PUm... Hello, Uncle.\x01",
            "Have you been well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x9,
        (
            "#222F#6PARGH! Have you no SHAME,\x01",
            "Klaudia?! And YOU, brigand!\x02\x03",

            "Because of you... All because\x01",
            "of YOU...\x02\x03",

            "#224FI have been forced into this life\x01",
            "of shame! House arrest, of all\x01",
            "things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1007F#6POkay, I don't think it's really fair\x01",
            "to say it's 'our' fault.\x02\x03",

            "You're the one who bought into\x01",
            "Colonel Richard's plan, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53A0")

    ChrTalk(    #203
        0x108,
        (
            "#074F#2PYou should probably count yourself\x01",
            "lucky it's only house arrest.\x02\x03",

            "#070FAnywhere else, and you'd be facing\x01",
            "jail time at best, even if you are nobility.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5465")

    label("loc_53A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5465")

    ChrTalk(    #204
        0x104,
        (
            "#035F#2PYou should be grateful you live in\x01",
            "a kingdom as forgiving and merciful\x01",
            "as Liberl.\x02\x03",

            "#030FWere this Erebonia, your 'nobility'\x01",
            "would only serve to speed you to the\x01",
            "gallows.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5465")


    ChrTalk(    #205
        0x9,
        (
            "#226F#6PErgh...\x02\x03",

            "#222FI confess that imprisoning\x01",
            "Her Majesty was out of line,\x01",
            "perhaps.\x02\x03",

            "Richard may have suggested it,\x01",
            "but I should have gainsaid him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006F#6PSo you can actually admit you were\x01",
            "wrong about that whole deal? That's\x01",
            "pretty humble, coming from you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x9,
        (
            "#225F#6PDo not misunderstand me. I love and\x01",
            "respect Her Majesty.\x02\x03",

            "As both a ruler and an aunt, she is\x01",
            "utterly above reproach.\x02\x03",

            "#224FBut you, Klaudia!\x02\x03",

            "But to consider naming a little girl\x01",
            "like you as her successor is simply\x01",
            "madness! Unacceptable insanity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x105,
        "#049F#4PI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1005F#6PNow just a second!\x02\x03",

            "Kloe's smart, studious, kind, merciful...\x01",
            "She's got all kinds of virtues that attract\x01",
            "people to her!\x02\x03",

            "Where do you get off in calling her a\x01",
            "'little girl,' huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x105,
        (
            "#047F#4PEstelle, that's enough.\x02\x03",

            "#043FI've always admitted that I'm not\x01",
            "ready to take the throne.\x02\x03",

            "I suppose it's only natural my uncle\x01",
            "finds that unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1026F#6PBut, Kloe...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#220F#6PYou always did have SOME sense,\x01",
            "at the very least.\x02\x03",

            "But you, Klaudia, have always seemed\x01",
            "'allergic' to attending public ceremonies.\x02\x03",

            "I am far better known among the citizenry,\x01",
            "while you remain a veritable ghost.\x02\x03",

            "You have not once publicly demonstrated\x01",
            "that you are ready to stand above others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x105,
        "#043F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x9,
        (
            "#222F#6PWhy, from what I understand, you hide\x01",
            "your true identity while living as a student.\x02\x03",

            "And as if that weren't enough, you even\x01",
            "waste your time at some backwater\x01",
            "orphanage?\x02\x03",

            "#225FShe should be presiding OVER the\x01",
            "common rabble at ceremonies, not\x01",
            "wallowing in the mud with them!\x02\x03",

            "#224FTHAT is the purpose of nobility!\x01",
            "To stand above all other men in lordship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x105,
        "#049F#4PIt's as you say, Uncle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        (
            "#1002F#6P...\x02\x03",

            "#1007FI'll admit, I don't really know much about\x01",
            "the 'purpose' of nobility, so...\x02\x03",

            "You might have a point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x9,
        "#221F#6PWa-ha-ha! Of course I do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1002F#6PBut I can say this:\x02\x03",

            "Kloe is trying her very hardest to figure out\x01",
            "what she wants to be, and is helping US out\x01",
            "in the middle of her own problems.\x02\x03",

            "#1005FAnd she sure as hell is doing a LOT more\x01",
            "than some duke who sits around doing\x01",
            "nothing because he's under 'house arrest'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        "#226F#6PWHAT?! YOU DARE--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x105,
        (
            "#049F#4PEstelle!\x02\x03",

            "#043F...Uncle Dunan?\x02\x03",

            "I am trying, as hard as I can, to find\x01",
            "my own path as I help Estelle.\x02\x03",

            "#047FI think, by the end of it all...\x02\x03",

            "We will know if I have the right to\x01",
            "become the next queen or not.\x02\x03",

            "#042FSo...please.\x01",
            "Hold your judgment until then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#226F#6PWhat? Tch!\x02\x03",

            "#222FRrrgh, this is absurd!\x02\x03",

            "#224FI will deal with this no further!\x01",
            "Begone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        (
            "#1005F#6PTrust me, I don't wanna stick around!\x02\x03",

            "#1007FThough, come to think of it, I need to.\x01",
            "I gotta ask one thing.\x02\x03",

            "#1015FHas a girl in a white dress come by\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x9,
        (
            "#222F#6PWhat are you talking--\x02\x03",

            "#224FNo, no little girls have come by!\x01",
            "BEGONE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        (
            "#1019F#6PYeah, sure.\x01",
            "Enjoy your donuts or whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        "#047FPardon us...\x02",
    )

    CloseMessageWindow()

    label("loc_5F94")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F1)
    OP_A2(0x1612)
    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_20_3EB2 end

    def Function_21_5FB6(): pass

    label("Function_21_5FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5FE8")
    OP_8E(0xFE, 0xFFFFC950, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFC180, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    Jump("Function_21_5FB6")

    label("loc_5FE8")

    OP_22(0x6, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFC568, 0x0, 0xFFFF56BE, 0x7D0, 0x0)
    OP_A2(0x1)
    Return()

    # Function_21_5FB6 end

    def Function_22_6005(): pass

    label("Function_22_6005")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_602C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_602C)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFC73E, 0x0, 0xFFFF4DFE, 0x9C4, 0x0)
    Return()

    # Function_22_6005 end

    def Function_23_6061(): pass

    label("Function_23_6061")

    Sleep(500)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_608D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_608D)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFCA86, 0x0, 0xFFFF4BEC, 0x9C4, 0x0)
    Return()

    # Function_23_6061 end

    def Function_24_60C2(): pass

    label("Function_24_60C2")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_60EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_60EE)
    OP_8E(0xFE, 0xFFFFC8EC, 0x0, 0xFFFF4278, 0x9C4, 0x0)
    OP_8F(0xFE, 0xFFFFC45A, 0x0, 0xFFFF4908, 0x9C4, 0x0)
    Return()

    # Function_24_60C2 end

    def Function_25_6123(): pass

    label("Function_25_6123")

    Sleep(1500)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -14130, 0, -49500, 180)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_614F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_614F)
    OP_8E(0xFE, 0xFFFFC84C, 0x0, 0xFFFF46CE, 0x9C4, 0x0)
    Return()

    # Function_25_6123 end

    def Function_26_6170(): pass

    label("Function_26_6170")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 180, 0)
    SetChrPos(0x12F, -16400, 0, -39920, 0)
    SetChrPos(0x101, -15400, 0, -39750, 0)
    SetChrPos(0xF7, -15710, 0, -41000, 0)
    SetChrPos(0xF8, -16850, 0, -41250, 0)
    SetChrPos(0xF9, -14720, 0, -41100, 0)
    OP_6D(-15710, 0, -39150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #226
        0x9,
        (
            "#222F#6PWhat? Do you truly delight in\x01",
            "torturing me, you bandit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x12F,
        "#264F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x9,
        (
            "#223F#6PWhat in the name of...?\x01",
            "Why is this child staring at\x01",
            "me in such a manner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12F,
        (
            "#260F#1PHey, Miss Estelle?\x02\x03",

            "Why does this odd man have such\x01",
            "a funny hairstyle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        "#226F#6PO-ODD MAN? FUNNY HAIRSTYLE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        (
            "#1016F#4POh, calm down, she's just a kid.\x02\x03",

            "#1006FBy the way, Renne...\x02\x03",

            "It's not just his hair that's funny--\x01",
            "his clothes and manners are, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x12F,
        "#261F#1POh, okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x9,
        (
            "#226F#6PWH-WHAT KIND OF LESSON\x01",
            "IS THAAAT?!\x02\x03",

            "#224FGET OUT OF MY ROOM, AND\x01",
            "TAKE THE BRAT WITH YOU!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_4B(0x9, 255)
    OP_A2(0x1613)
    EventEnd(0x0)
    Return()

    # Function_26_6170 end

    def Function_27_6462(): pass

    label("Function_27_6462")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6482")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_6482")

    Fade(1000)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -13290, 0, 18890, 45)
    SetChrPos(0xF7, -12530, 0, 18230, 0)
    SetChrPos(0xF8, -13740, 0, 17710, 45)
    SetChrPos(0xF9, -14560, 0, 18430, 45)
    OP_6D(-12740, 0, 19290, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6821")

    ChrTalk(    #234
        0x8,
        "Hey, did you manage to find her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        (
            "#1007FNope. Couldn't find a single hair.\x02\x03",

            "I swear, we've covered every hiding\x01",
            "place, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x8,
        "That's unfortunate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x8,
        (
            "You don't think she left the villa,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6622")

    ChrTalk(    #238
        0x106,
        "#552FTch. That'd make this interesting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_664E")

    label("loc_6622")


    ChrTalk(    #239
        0x103,
        "#522FOof... That wouldn't be very fun.\x02",
    )

    CloseMessageWindow()

    label("loc_664E")


    ChrTalk(    #240
        0x101,
        (
            "#1015FHmmm... If she's really playing\x01",
            "hide and seek, I don't think she\x01",
            "would, though.\x02\x03",

            "You're supposed to hide in a place\x01",
            "you can get to by walking not too far\x01",
            "from the 'start point.'\x02\x03",

            "#1006FI kinda suspect she's just in some\x01",
            "place we haven't thought to check yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67A5")

    ChrTalk(    #241
        0x106,
        (
            "#051FHeh, good point.\x02\x03",

            "So, we keep searching then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_681B")

    label("loc_67A5")


    ChrTalk(    #242
        0x103,
        (
            "#021FTrue! You always were good at\x01",
            "this sort of thing when you were\x01",
            "younger.\x02\x03",

            "#020FShall we search a bit longer?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_681B")

    OP_A2(0x1682)
    Jump("loc_68AF")

    label("loc_6821")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_686A")

    ChrTalk(    #243
        0x106,
        (
            "#052FWhat's up, Estelle?\x02\x03",

            "We gonna keep searching?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68AF")

    label("loc_686A")


    ChrTalk(    #244
        0x103,
        (
            "#023FWhat's wrong, Estelle?\x02\x03",

            "Aren't we going to keep searching?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68AF")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Keep Searching\x01",            # 0
            "Olly Olly Oxen Free!\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_691A"),
        (1, "loc_694A"),
        (SWITCH_DEFAULT, "loc_7088"),
    )


    label("loc_691A")


    ChrTalk(    #245
        0x101,
        "#1006FYeah. Let's try changing tactics.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7088")

    label("loc_694A")


    ChrTalk(    #246
        0x101,
        (
            "#1007FHmm... Not exactly what I want to do,\x01",
            "but I think it's time we gave up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x8,
        "But if we give up, how will we find her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1015FIn hide and seek, when the 'it' person\x01",
            "gives up...\x02\x03",

            "#1006FThey run around saying, 'olly olly oxen\x01",
            "free!' to show they give up and to let the\x01",
            "other players know they can come out.\x02\x03",

            "If we do that, the girl should come out\x01",
            "of hiding. Hopefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        "O-Oh, I see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B64")

    ChrTalk(    #250
        0x107,
        (
            "#067FHeehee! Well, running around and\x01",
            "yelling sounds kinda embarrassing...\x02\x03",

            "But okay! I don't mind if we have to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D00")

    label("loc_6B64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C02")

    ChrTalk(    #251
        0x105,
        (
            "#045FHaha. It's a bit embarrassing, but...\x02\x03",

            "If that's what it will take to get her to\x01",
            "come out, then that's just what we'll\x01",
            "have to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D00")

    label("loc_6C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D00")

    ChrTalk(    #252
        0x104,
        (
            "#035FEstelle, you do realize that beckoning\x01",
            "one to come hither by shouting gibberish\x01",
            "would be humiliating for most.\x02\x03",

            "#037FThen again, I've found that there are\x01",
            "certain degrees of humiliation which are\x01",
            "most pleasurable. Well? Shall we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D00")


    ChrTalk(    #253
        0x101,
        (
            "#1006FAll right, guys, let's belt it!\x01",
            "Repeat after me:\x02\x03",

            "#1018FOlly olly oxen free!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, 160, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #254
        "\x07\x00#3SOlly olly oxen free!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -10290, -500, 19160, 0)

    NpcTalk(    #255
        0xA,
        "Voice",
        "#4PMeow. ♪\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E1C")
    OP_62(0xF8, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6E50")

    label("loc_6E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E3E")
    OP_62(0xF8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6E50")

    label("loc_6E3E")

    OP_62(0xF8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E72")
    OP_62(0xF9, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6EA6")

    label("loc_6E72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E94")
    OP_62(0xF9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6EA6")

    label("loc_6E94")

    OP_62(0xF9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6EA6")

    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0xF7)
    OP_63(0xF8)
    OP_63(0xF9)
    OP_63(0x8)

    def lambda_6ED2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6ED2)
    Sleep(50)

    def lambda_6EE5():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6EE5)
    Sleep(50)

    def lambda_6EF8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6EF8)
    Sleep(50)

    def lambda_6F0B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6F0B)
    Sleep(50)

    def lambda_6F1E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6F1E)
    Sleep(500)

    ChrTalk(    #256
        0x101,
        "#1008FHey...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x8,
        "She's...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #258
        0xA,
        "Voice",
        "#4PHeehee! Yay, I win, I win!\x02",
    )

    CloseMessageWindow()

    def lambda_6F7B():

        label("loc_6F7B")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_6F7B")

    QueueWorkItem2(0x8, 1, lambda_6F7B)

    def lambda_6F8C():
        OP_6D(-11020, 0, 19860, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F8C)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFFD95E, 0x0, 0x4F9C, 0x3E8, 0x0)
    OP_44(0x8, 0x1)
    OP_8C(0xA, 225, 400)
    WaitChrThread(0x101, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #259
        0x101,
        (
            "#1004F#5PWhat the? You're that girl we met\x01",
            "at Air-Letten!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xA,
        (
            "#6P#261FHeehee! Hello, miss!\x02\x03",

            "I'm happy you remembered me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    OP_A2(0x1615)
    OP_28(0x89, 0x1, 0x800)
    OP_28(0x89, 0x1, 0x1000)
    Call(0, 29)
    Jump("loc_7088")

    label("loc_7088")

    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_27_6462 end

    def Function_28_708F(): pass

    label("Function_28_708F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70AF")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_70AF")

    Fade(1000)
    SetChrPos(0x101, -9950, 0, 20590, 180)
    SetChrPos(0xF7, -12280, 0, 18190, 45)
    SetChrPos(0xF8, -10910, 0, 18200, 0)
    SetChrPos(0xF9, -9550, 0, 18200, 0)
    OP_6D(-10150, 0, 20240, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #261
        "\x07\x05Estelle checked under the counter, just in case...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 2)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0xC8, 1400, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(    #262
        0x101,
        "#1004FHey!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #263
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        "Something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#1016FHaha.\x02\x03",

            "You could say that...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -10290, -500, 19160, 0)

    NpcTalk(    #266
        0xA,
        "Voice",
        "#5PMrrrrow...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #267
        0xA,
        "Voice",
        "#5PAwwww, I lost...\x02",
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C6")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7304")

    label("loc_72C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72ED")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7304")

    label("loc_72ED")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7304")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_732B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7369")

    label("loc_732B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7352")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7369")

    label("loc_7352")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7369")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(250)

    def lambda_73A5():
        OP_6D(-10460, 0, 20440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_73A5)
    OP_8F(0x101, 0xFFFFD882, 0x0, 0x5352, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFFD95E, 0x0, 0x4F9C, 0x3E8, 0x0)
    OP_44(0x8, 0x1)
    OP_8C(0xA, 225, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #268
        0x8,
        "What the...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7453")

    ChrTalk(    #269
        0x106,
        (
            "#052F#5PHey, aren't you that kid we met\x01",
            "at Air-Letten?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_748A")

    label("loc_7453")


    ChrTalk(    #270
        0x103,
        "#023F#5PAren't you the girl we met at Air-Letten?\x02",
    )

    CloseMessageWindow()

    label("loc_748A")


    ChrTalk(    #271
        0x101,
        (
            "#1017F#6PHeheh! I thought it might be you,\x01",
            "Renne.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #272
        0xA,
        (
            "#261F#4PHeehee! Hello, miss!\x02\x03",

            "I'm happy you remembered me!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    OP_A2(0x1616)
    OP_28(0x89, 0x1, 0x80)
    OP_28(0x89, 0x1, 0x100)
    Call(0, 29)
    Return()

    # Function_28_708F end

    def Function_29_7531(): pass

    label("Function_29_7531")

    EventBegin(0x0)
    AddParty(0x2E, 0xFF, 0xFF)
    SetChrPos(0x101, -13340, 0, 18690, 90)
    SetChrPos(0xF7, -13560, 0, 17570, 90)
    SetChrPos(0xF8, -14890, 0, 17470, 90)
    SetChrPos(0xF9, -14630, 0, 18640, 90)
    SetChrPos(0x12F, -11980, 0, 18170, 270)
    TurnDirection(0x8, 0x101, 0)
    OP_6D(-12300, 0, 19340, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #273
        0x8,
        (
            "#6PGoodness! I wasn't expecting her to\x01",
            "be an acquaintance of yours.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x12F, 400)
    Sleep(500)

    ChrTalk(    #274
        0x8,
        "#6PSo your name is Renne, right?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12F, 0, 400)

    ChrTalk(    #275
        0x12F,
        (
            "#260FThat's right.\x02\x03",

            "#261FSorry for keeping it\x01",
            "a secret, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        "#6PHaha. Don't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x8,
        (
            "#6PBut, Renne, why did you run off\x01",
            "and play hide and seek like that?\x01",
            "I was worried!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x12F,
        (
            "#263FBecause I'd heard Miss Estelle\x01",
            "was coming!\x02\x03",

            "I wanted to play hide and seek\x01",
            "with her, so I worked really hard\x01",
            "to find a nice hiding spot. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        (
            "#1016F#6PHaha, well, okay.\x02\x03",

            "#1006FIt's kind of incredible you knew it\x01",
            "was us coming, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12F, 270, 400)

    ChrTalk(    #280
        0x12F,
        (
            "#264F#4PYou said you're bracers, right?\x02\x03",

            "I heard some bracers would be\x01",
            "coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#1025F#6PWe are, yeah, but...\x02\x03",

            "We're not the only bracers in the\x01",
            "world, you know. It could've been\x01",
            "someone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x12F,
        (
            "#260F#4PBut I believed. I knew you'd be the\x01",
            "ones who'd come.\x02\x03",

            "#261FAnd see? You did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        "#1016F#6PI...guess I can't argue against that logic.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B79")

    ChrTalk(    #284
        0x106,
        (
            "#053F#5PWell, more to the point...\x02\x03",

            "#050FWhere're your mom and dad, kiddo?\x02\x03",

            "Why are you playin' around here on\x01",
            "your own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x12F,
        "#262F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x106,
        "#055F#5PWhat're you lookin' at?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x12F,
        (
            "#268F#4PThat's enough out of you, mister.\x02\x03",

            "You have no idea how to speak to\x01",
            "a young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x106,
        "#057F#5POh, for...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AE1")

    ChrTalk(    #289
        0x107,
        "#067F#5PUm, Agate, it's okay...\x02",
    )

    CloseMessageWindow()

    label("loc_7AE1")


    ChrTalk(    #290
        0x12F,
        (
            "#263F#4PWell, I, Lady Renne, am feeling\x01",
            "generous today, so I'll forgive you.\x02\x03",

            "#260FAnyway, where did Papa and Mama go?\x02\x03",

            "I'm not so sure either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E63")

    label("loc_7B79")


    ChrTalk(    #291
        0x103,
        (
            "#020F#5PWell, putting that aside...\x02\x03",

            "Where did your mother and father go?\x02\x03",

            "Why were you playing all alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x12F,
        (
            "#264F#4PWow! Miss, your clothes are funny!\x02\x03",

            "Don't you get cold with your belly\x01",
            "out like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        (
            "#021F#5PMmm, you get used to it.\x01",
            "It's very comfor--\x02\x03",

            "#023FErm, but that's not the point.\x01",
            "About your parents...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x12F,
        (
            "#265F#4PAnd your skin is so dark! You're from\x01",
            "the south, across the sea, right?\x02\x03",

            "Are you really okay with how cold it\x01",
            "gets here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x103,
        (
            "#021F#5PI traveled all over as a performer with\x01",
            "a circus, so yes.\x02\x03",

            "I'm fine in heat OR cold.\x02\x03",

            "#022FMore. To. The. Point.\x02\x03",

            "#027FWould you mind telling us what\x01",
            "happened to your parents, Renne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x12F,
        (
            "#266F#4PAwwww, okay.\x02\x03",

            "#260FSo, where did Papa and Mama go?\x02\x03",

            "I'm not so sure either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E63")


    ChrTalk(    #297
        0x101,
        "#1004F#6PWait, you don't know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x12F,
        (
            "#263F#4PNot at all. I came here with\x01",
            "Papa and Mama to play.\x02\x03",

            "But after lunch, Papa gave me\x01",
            "a real serious look and said:\x02\x03",

            "#262F'Renne, Papa has something\x01",
            "important to do, so he and Mama\x01",
            "have to say goodbye for now.'\x02\x03",

            "'But don't worry, once it's done,\x01",
            "we'll come and get you.'\x02\x03",

            "'Be a good girl until Papa comes\x01",
            "back, all right?'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8029")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_8067")

    label("loc_8029")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8050")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_8067")

    label("loc_8050")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_8067")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808E")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_80CC")

    label("loc_808E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80B5")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_80CC")

    label("loc_80B5")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_80CC")

    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #299
        0x101,
        "#1019F#6PThey just... What the hell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x12F,
        (
            "#261F#4PI'm already eleven, so I said,\x01",
            "'I'll be good, Papa.'\x02\x03",

            "And after that, Papa and Mama left.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81C1")

    ChrTalk(    #301
        0x106,
        "#551F#5PYou have seriously gotta be kidding me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_820B")

    label("loc_81C1")


    ChrTalk(    #302
        0x103,
        (
            "#025F#5PWell, this is quite a bit worse\x01",
            "than I imagined it would be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_820B")


    ChrTalk(    #303
        0x8,
        (
            "#6PEr... I certainly wasn't expecting\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Sleep(500)

    ChrTalk(    #304
        0x8,
        (
            "#6PWhat should we do?\x01",
            "This seems to be quite a bit beyond\x01",
            "just 'finding' her parents at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8374")

    ChrTalk(    #305
        0x101,
        (
            "#1007F#6PYeah, tell me about it...\x02\x03",

            "#1015FAgate, you think we should?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x106,
        (
            "#552F#2PYeah, that's fine. It's part of the job,\x01",
            "and we can't just leave her here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_840D")

    label("loc_8374")


    ChrTalk(    #307
        0x101,
        (
            "#1007F#6PYeah, tell me about it...\x02\x03",

            "#1015FSchera, you think we should?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x103,
        (
            "#524F#2PYou don't even need to ask.\x01",
            "I'd never leave her here like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_840D")

    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #309
        0x101,
        (
            "#1006F#6PDon't worry, Raymond.\x02\x03",

            "We'll take care of this girl for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        "#6PHm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)
    Sleep(500)

    ChrTalk(    #311
        0x101,
        (
            "#1006F#6PHey, Renne?\x02\x03",

            "Do you want to visit the capital's\x01",
            "Bracer Guild with us?\x02\x03",

            "I bet we'll be able to find your papa\x01",
            "and mama, easy-peasy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x12F,
        (
            "#264F#4PReally?\x02\x03",

            "But Papa and Mama said they\x01",
            "had something important to do\x01",
            "and to wait here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        (
            "#1006F#6PIt's okay. We'll definitely find them.\x02\x03",

            "#1018FTrust in Miss Estelle, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x12F,
        (
            "#267F#4PMmmmm...\x02\x03",

            "#265FOkay, then, I'll go with you.\x02\x03",

            "Thank you, Miss Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        (
            "#1006F#6PIt's okay! Stick close by, though,\x01",
            "Renne. I wouldn't want you to get\x01",
            "hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x8,
        "#6PPhew! Thank you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x8,
        "#6PTake good care of her!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8714")

    ChrTalk(    #318
        0x106,
        (
            "#053F#5PLeave it to us.\x02\x03",

            "#051FLike Estelle said, back to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8774")

    label("loc_8714")


    ChrTalk(    #319
        0x103,
        (
            "#021F#5PDon't worry, you can leave this to us.\x02\x03",

            "#020FSo, let's get back to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8774")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-16620, 0, 16070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -16620, 0, 16070, 180)
    SetChrPos(0x1, -16620, 0, 16070, 180)
    SetChrPos(0x2, -16620, 0, 16070, 180)
    SetChrPos(0x3, -16620, 0, 16070, 180)
    SetChrPos(0x12F, -16620, 0, 16070, 180)
    OP_64(0x5, 0x1)
    OP_8C(0x8, 225, 0)
    OP_4B(0x8, 255)
    OP_A2(0x1617)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_28(0x89, 0x1, 0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 5)), scpexpr(EXPR_END)), "loc_8841")
    Jump("loc_8855")

    label("loc_8841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 2)), scpexpr(EXPR_END)), "loc_8850")
    OP_2B(0x89, 0x1)
    Jump("loc_8855")

    label("loc_8850")

    OP_2B(0x89, 0x3)

    label("loc_8855")

    EventEnd(0x0)
    Return()

    # Function_29_7531 end

    def Function_30_8858(): pass

    label("Function_30_8858")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #320
        (
            "\x07\x05The Royal Army spent the night searching with an\x01",
            "entire airship squadron...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #321
        (
            "\x07\x05...but they could not find the massive orbal 'doll' nor the girl\x01",
            "who rode off on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #322
        "\x07\x05The next day...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_6D(-11130, 0, -43550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(1980, 0)
    OP_6C(33000, 0)
    OP_6E(386, 0)
    SetChrPos(0xC, -11940, 200, -43100, 180)
    SetChrPos(0x10F, -11940, 0, -45090, 0)
    SetChrPos(0xB, -10710, 0, -43660, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0xF7, 0x80)
    OP_1D(0x53)
    Sleep(100)
    FadeToBright(3000, 0)
    OP_6B(1780, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #323
        0xB,
        (
            "#700FCaptain Amalthea. Please, won't you\x01",
            "cooperate with us?\x02\x03",

            "What kind of relationship did you have\x01",
            "with that girl?\x02\x03",

            "And what do you know about the Society\x01",
            "of Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xC,
        "#1238F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x10F,
        (
            "#176F#2PCaptain Amalthea... Kanone.\x01",
            "Stop being stubborn.\x02\x03",

            "#178FAt this point, you're making things\x01",
            "worse not only for yourself, but for\x01",
            "your men as well.\x02\x03",

            "I can't believe that's what you want.\x01",
            "Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xC,
        (
            "#1231F#6PHmph. We all went into this prepared\x01",
            "to lay down our lives.\x02\x03",

            "You'll need to come up with a better\x01",
            "threat than that, CAPTAIN Schwarz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x10F,
        (
            "#177F#2PStop trying to play the martyr!\x02\x03",

            "#177FYou saw it, same as any of us!\x01",
            "That gigantic orbal weapon!\x02\x03",

            "Do you not understand that an\x01",
            "organization which can field such\x01",
            "a thing has infiltrated the kingdom?!\x02\x03",

            "How can you not understand the\x01",
            "gravity of this situation?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xC,
        "#1238F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xB,
        (
            "#703FCaptain Amalthea...\x02\x03",

            "#700FColonel Richard is, in many ways,\x01",
            "a lover of Liberl.\x02\x03",

            "He wished for us to be able to stand,\x01",
            "independently, against any threat we\x01",
            "would ever face.\x02\x03",

            "I KNOW he wanted that, if nothing else.\x02\x03",

            "#703FAnd now, dark clouds gather in the\x01",
            "skies above us...\x02\x03",

            "Can you not consider what he would\x01",
            "do in this situ--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xC,
        "#1238F#6P...ilence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xB,
        "#702FHm?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 1)
    Sleep(500)

    ChrTalk(    #332
        0xC,
        "#1236F#6P#3SSILENCE, YOU PESTS!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #333
        0xC,
        (
            "#1235F#6PHow DARE you speak so casually of the\x01",
            "colonel's feelings!\x02\x03",

            "You dogs gained your new, oh-so-exalted\x01",
            "positions by engineering his fall!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xB,
        "#700F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x10F,
        "#177F#2PKanone, would you--\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0)
    Sleep(300)

    ChrTalk(    #336
        0xC,
        (
            "#1230F#6POh, I have plenty to say to you, too,\x01",
            "Julia!\x02\x03",

            "You must be relishing every second\x01",
            "of this! Watching your longtime rival\x01",
            "falling so far...\x02\x03",

            "#1234FWell, LAUGH, then!\x02\x03",

            "Laugh and gloat to your heart's content!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x10F,
        "#175F#2PThat's enough, Kanone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xC,
        (
            "#1236F#6PI've crawled through filth and given\x01",
            "all of myself to the realization of the\x01",
            "colonel's dream!\x02\x03",

            "Now that I've failed...I no longer have\x01",
            "a reason to live!\x02\x03",

            "So come on, then. Drag me to the firing\x01",
            "line! Let's get this over with!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xD, -14860, 0, -49890, 90)

    NpcTalk(    #339
        0xD,
        "Man's Voice",
        (
            "#5PThat's a foolish thing to say,\x01",
            "Kanone.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0xD, 400)
    SetChrSubChip(0xC, 0)
    Sleep(50)
    SetChrSubChip(0xC, 2)
    TurnDirection(0x10F, 0xD, 400)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, -13940, 0, -49200, 360)
    ClearChrFlags(0xD, 0x80)

    def lambda_9292():

        label("loc_9292")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_9292")

    QueueWorkItem2(0xB, 1, lambda_9292)

    def lambda_92A3():

        label("loc_92A3")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_92A3")

    QueueWorkItem2(0x10F, 1, lambda_92A3)

    def lambda_92B4():
        OP_6D(-11520, 0, -44030, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92B4)

    def lambda_92CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_92CC)
    OP_8E(0xD, 0xFFFFC9F0, 0x0, 0xFFFF4DC2, 0x7D0, 0x0)
    OP_8C(0xD, 90, 400)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_44(0x10F, 0x1)

    ChrTalk(    #340
        0xD,
        "#1120F#5PPardon me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xB,
        "#702F#4PGeneral!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x10F,
        "#173F#2PGeneral, why are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xD,
        (
            "#1125F#5PI needed to speak to Her Majesty about\x01",
            "something related to our most recent case.\x02\x03",

            "#1120FI had some other business as well,\x01",
            "so I thought I'd stop by. I only arrived\x01",
            "in Grancel a few hours ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xB,
        "#701F#4PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x10F,
        (
            "#171F#2PThank you for your help when you're\x01",
            "so busy, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xC,
        (
            "#1231F#6PCassius Bright...the author of all our\x01",
            "suffering.\x02\x03",

            "So you've come to gloat over my fall too,\x01",
            "have you? Here to see me riddled with\x01",
            "gunfire?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)
    Sleep(500)

    ChrTalk(    #347
        0xD,
        (
            "#1123F#5PWell, I certainly seem to be popular today.\x02\x03",

            "And here I was thinking I was actually as\x01",
            "much of a lady killer as Richard! *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #348
        0xC,
        "#1234F#6P#3SHOW DARE YOU! You...\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #349
        0xC,
        (
            "#1235F#6PIf it wasn't for you, the colonel...\x01",
            "He would've...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xE, -14860, 0, -49890, 90)

    NpcTalk(    #350
        0xE,
        "Man's Voice",
        "#5PAh, Cassius.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #351
        0xE,
        "Man's Voice",
        (
            "#5PI know you mean it in good fun,\x01",
            "but don't tease her too much, yes?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xB, 0xE, 400)
    TurnDirection(0x10F, 0xE, 400)
    TurnDirection(0xD, 0xE, 400)

    ChrTalk(    #352
        0xC,
        "#1232F#6PWh... What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        "#702F#6PThat was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x10F,
        "#173F#2PHow on earth...?\x02",
    )

    CloseMessageWindow()

    def lambda_9770():
        OP_6D(-12930, 0, -43070, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9770)

    def lambda_9788():
        OP_67(0, 7500, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9788)

    def lambda_97A0():
        OP_6B(1700, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_97A0)

    def lambda_97B0():
        OP_6C(0, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_97B0)

    def lambda_97C0():
        OP_6E(400, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_97C0)
    OP_43(0xD, 0x0, 0x0, 0x1F)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xE, -13940, 0, -49200, 360)
    ClearChrFlags(0xE, 0x80)

    def lambda_97FD():

        label("loc_97FD")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_97FD")

    QueueWorkItem2(0xB, 1, lambda_97FD)

    def lambda_980E():

        label("loc_980E")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_980E")

    QueueWorkItem2(0x10F, 1, lambda_980E)

    def lambda_981F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_981F)
    OP_8E(0xE, 0xFFFFCA2C, 0x0, 0xFFFF4F0C, 0x5DC, 0x0)
    OP_8C(0xE, 45, 400)
    OP_44(0xB, 0x1)
    OP_44(0x10F, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #355
        0xC,
        "#1239F#4PC... Colonel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x10F,
        "#173F#2PColonel Richard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xB,
        "#701F#4PIt's been some time, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xE,
        (
            "#1170F#5PYes...it has. Maj--ah, Lieutenant Colonel Cid.\x01",
            "Captain Schwarz.\x02\x03",

            "#1171FAnd...it's good to see you safe as well,\x01",
            "Kanone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xC,
        "#1239F#4PS-S-Sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xE,
        (
            "#1170F#5PI begged General Bright to allow me\x01",
            "to leave my cell for a little while so that\x01",
            "I could visit.\x02\x03",

            "You see, I have something I absolutely\x01",
            "must say to you, Kanone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xC,
        "#1239F#4PTo... To me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xE,
        (
            "#1170F#5PYes.\x02\x03",

            "#1173FI'm...sorry, Kanone. I am so very sorry.\x02\x03",

            "I wrapped you up in my pride and narrow\x01",
            "vision.\x02\x03",

            "I've forced many bright young officers to\x01",
            "shoulder the burden of terrible, criminal\x01",
            "deeds.\x02\x03",

            "#1174FI've wanted to apologize to all of you\x01",
            "for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xC,
        (
            "#1233F#4PNo, sir! No! You forced us into nothing!\x01",
            "We followed you freely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xE,
        (
            "#1172F#5PNo... No, you didn't. Even if you think you\x01",
            "followed of your own will...\x02\x03",

            "In the end, I pressured you into following\x01",
            "my desires. The responsibility is mine\x01",
            "alone.\x02\x03",

            "This makes what happened this past\x01",
            "night my responsibility as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xC,
        "#1237F#4PS-Sir, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xE,
        (
            "#1173F#5PSo, let me make a declaration.\x02\x03",

            "#1172FAs of this moment, the Royal Army\x01",
            "Intelligence Division is formally disbanded.\x02\x03",

            "All previous functions and duties are to be taken\x01",
            "up by army headquarters, and all former staff\x01",
            "should give headquarters all due assistance.\x02\x03",

            "#1171FKanone... Captain Amalthea. Thank you for\x01",
            "leading my division in my absence until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xC,
        "#1232F#4PSir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xE,
        (
            "#1170F#5PWith all that said, you no longer need\x01",
            "to do crazy things like this any longer.\x02\x03",

            "You don't need to spend your life\x01",
            "attempting to 'rescue' me.\x02\x03",

            "#1174FSo, please...don't say such terrible\x01",
            "things as, 'Bring me before the firing\x01",
            "line.' Please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xC,
        (
            "#1245F#4PColonel... Sir... Alan...\x02\x03",

            "#1237FAaah... *sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    FadeToDark(1500, 0, -1)

    def lambda_9F7C():
        OP_6B(1980, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9F7C)

    ChrTalk(    #370 op#A op#5
        0xC,
        "#1246F#4S#4P#16AWaaaaaauuuuuuh!\x05\x02",
    )

    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    RemoveParty(0xE, 0xFF)
    OP_A2(0x10F1)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_8858 end

    def Function_31_9FCC(): pass

    label("Function_31_9FCC")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFC824, 0x0, 0xFFFF536C, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_31_9FCC end

    def Function_32_9FEF(): pass

    label("Function_32_9FEF")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_A068"),
        (1, "loc_A06E"),
        (SWITCH_DEFAULT, "loc_A074"),
    )


    label("loc_A068")

    OP_A2(0x1200)
    Jump("loc_A074")

    label("loc_A06E")

    OP_A2(0x1201)
    Jump("loc_A074")

    label("loc_A074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A082")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A086")

    label("loc_A082")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A086")

    Return()

    # Function_32_9FEF end

    def Function_33_A087(): pass

    label("Function_33_A087")

    ClearMapFlags(0x1)
    OP_6D(-3960, 0, -27940, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A0CA")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_A0E8")

    label("loc_A0CA")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_A0E8")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_33_A087 end

    def Function_34_A108(): pass

    label("Function_34_A108")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #371
        "\x07\x05There is a beautiful plate here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_34_A108 end

    def Function_35_A15B(): pass

    label("Function_35_A15B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #372
        "\x07\x05There is an Eastern-style pot here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_35_A15B end

    def Function_36_A1B1(): pass

    label("Function_36_A1B1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #373
        "\x07\x05There is an Imperial-style pot here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_36_A1B1 end

    def Function_37_A208(): pass

    label("Function_37_A208")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #374
        "\x07\x05Fine art is lined up here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_37_A208 end

    def Function_38_A255(): pass

    label("Function_38_A255")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #375
        (
            "\x07\x05[Throne of the Last King] A chair much favored by the\x01",
            "previous king, Edgar III, during his time at the Erbe Villa.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_A255 end

    SaveToFile()

Try(main)

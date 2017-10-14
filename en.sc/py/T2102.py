from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2102   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Elderly Man',                          # 9
        'Middle-Aged Woman',                    # 10
        'Young Boy',                            # 11
        'Santos',                               # 12
        'Nobleman',                             # 13
        'Noble Girl',                           # 14
        'Hardt',                                # 15
        'Airliner, Linde',                      # 16
        'リンデ号影',                           # 17
        'Edwin',                                # 18
        'Clem',                                 # 19
        'Polly',                                # 20
        'Mary',                                 # 21
        'Daniel',                               # 22
        'Jill',                                 # 23
        'Hans',                                 # 24
        'Matron Theresa',                       # 25
        'Dean Collins',                         # 26
        'Clive',                                # 27
        'Samario',                              # 28
        'Todd',                                 # 29
        'Hardt',                                # 30
        'Santos',                               # 31
        'Child',                                # 32
        'Noblewoman',                           # 33
        'Nobleman',                             # 34
        'Ruan - North Block',                   # 35
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH02590 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH02630 ._CH',             # 0A
        'ED6_DT07/CH02640 ._CH',             # 0B
        'ED6_DT07/CH02390 ._CH',             # 0C
        'ED6_DT07/CH02550 ._CH',             # 0D
        'ED6_DT07/CH02570 ._CH',             # 0E
        'ED6_DT07/CH02600 ._CH',             # 0F
        'ED6_DT07/CH01450 ._CH',             # 10
        'ED6_DT07/CH01450 ._CH',             # 11
        'ED6_DT07/CH01470 ._CH',             # 12
        'ED6_DT07/CH01120 ._CH',             # 13
        'ED6_DT07/CH01660 ._CH',             # 14
        'ED6_DT07/CH01470 ._CH',             # 15
        'ED6_DT07/CH01200 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH02590P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH02630P._CP',             # 0A
        'ED6_DT07/CH02640P._CP',             # 0B
        'ED6_DT07/CH02390P._CP',             # 0C
        'ED6_DT07/CH02550P._CP',             # 0D
        'ED6_DT07/CH02570P._CP',             # 0E
        'ED6_DT07/CH02600P._CP',             # 0F
        'ED6_DT07/CH01450P._CP',             # 10
        'ED6_DT07/CH01450P._CP',             # 11
        'ED6_DT07/CH01470P._CP',             # 12
        'ED6_DT07/CH01120P._CP',             # 13
        'ED6_DT07/CH01660P._CP',             # 14
        'ED6_DT07/CH01470P._CP',             # 15
        'ED6_DT07/CH01200P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 101700,
        Z                   = 0,
        Y                   = 83800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 111220,
        Z                   = 6150,
        Y                   = 101150,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 112530,
        Z                   = 6150,
        Y                   = 102340,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 129990,
        Z                   = 8150,
        Y                   = 92560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 111500,
        Z                   = 4150,
        Y                   = 85650,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 108620,
        Z                   = 6150,
        Y                   = 95510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 71170,
        Z                   = 0,
        Y                   = 80860,
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


    DeclActor(
        TriggerX            = 100400,
        TriggerZ            = 0,
        TriggerY            = 83700,
        TriggerRange        = 1000,
        ActorX              = 101700,
        ActorZ              = 1500,
        ActorY              = 83800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 108610,
        TriggerZ            = 6150,
        TriggerY            = 96910,
        TriggerRange        = 800,
        ActorX              = 108610,
        ActorZ              = 8350,
        ActorY              = 96910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 127080,
        TriggerZ            = 6150,
        TriggerY            = 100740,
        TriggerRange        = 800,
        ActorX              = 127080,
        ActorZ              = 8350,
        ActorY              = 100740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 42,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 122620,
        TriggerZ            = 400,
        TriggerY            = 100640,
        TriggerRange        = 800,
        ActorX              = 122620,
        ActorZ              = 1600,
        ActorY              = 100640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 43,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140870,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 140870,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 149330,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 149330,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103030,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 103030,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96980,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 96980,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5EA",          # 00, 0
        "Function_1_72C",          # 01, 1
        "Function_2_74F",          # 02, 2
        "Function_3_8CC",          # 03, 3
        "Function_4_9A6",          # 04, 4
        "Function_5_AE3",          # 05, 5
        "Function_6_1075",         # 06, 6
        "Function_7_1149",         # 07, 7
        "Function_8_152D",         # 08, 8
        "Function_9_1C07",         # 09, 9
        "Function_10_1C0C",        # 0A, 10
        "Function_11_216A",        # 0B, 11
        "Function_12_21B9",        # 0C, 12
        "Function_13_2611",        # 0D, 13
        "Function_14_2653",        # 0E, 14
        "Function_15_2695",        # 0F, 15
        "Function_16_26D2",        # 10, 16
        "Function_17_26FB",        # 11, 17
        "Function_18_2CB5",        # 12, 18
        "Function_19_4A21",        # 13, 19
        "Function_20_4A4A",        # 14, 20
        "Function_21_4A8D",        # 15, 21
        "Function_22_4ABB",        # 16, 22
        "Function_23_4AFE",        # 17, 23
        "Function_24_4B2C",        # 18, 24
        "Function_25_4B70",        # 19, 25
        "Function_26_4BB4",        # 1A, 26
        "Function_27_4BF8",        # 1B, 27
        "Function_28_4C3C",        # 1C, 28
        "Function_29_4C80",        # 1D, 29
        "Function_30_4CC4",        # 1E, 30
        "Function_31_4D08",        # 1F, 31
        "Function_32_4D4C",        # 20, 32
        "Function_33_4D7C",        # 21, 33
        "Function_34_4DB4",        # 22, 34
        "Function_35_4DF1",        # 23, 35
        "Function_36_4E2E",        # 24, 36
        "Function_37_4E6B",        # 25, 37
        "Function_38_4E8B",        # 26, 38
        "Function_39_4EA4",        # 27, 39
        "Function_40_4ECE",        # 28, 40
        "Function_41_4F66",        # 29, 41
        "Function_42_502F",        # 2A, 42
        "Function_43_50AE",        # 2B, 43
    )


    def Function_0_5EA(): pass

    label("Function_0_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_659")
    SetChrFlags(0x1A, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_634")
    SetChrPos(0x11, 108580, 6150, 96500, 0)
    SetChrPos(0x1B, 136340, 8150, 95080, 270)
    SetChrPos(0x1C, 135340, 8150, 95080, 90)
    Jump("loc_656")

    label("loc_634")

    SetChrPos(0x11, 111500, 4150, 80040, 100)
    SetChrPos(0x1B, 134010, 8150, 92800, 270)

    label("loc_656")

    Jump("loc_715")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrPos(0x1A, 139320, 6150, 99610, 180)
    SetChrPos(0x1B, 130460, 8150, 98040, 180)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_715")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_6CF")
    SetChrPos(0x1A, 139320, 6150, 99610, 180)
    SetChrPos(0x1B, 129990, 8150, 92560, 90)
    SetChrFlags(0x1C, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6CC")
    ClearChrFlags(0x1E, 0x80)

    label("loc_6CC")

    Jump("loc_715")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FF")
    SetChrPos(0x1A, 111460, 4150, 79470, 90)
    SetChrPos(0x1B, 141100, 6150, 100100, 39)
    Jump("loc_715")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_715")
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1C, 0x10)

    label("loc_715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_72B")

    Return()

    # Function_0_5EA end

    def Function_1_72C(): pass

    label("Function_1_72C")

    OP_16(0x2, 0xFA0, 0x4E20, 0xFFFF63C0, 0x230049)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_74E")
    OP_64(0x0, 0x1)

    label("loc_74E")

    Return()

    # Function_1_72C end

    def Function_2_74F(): pass

    label("Function_2_74F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_774")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_8B6")

    label("loc_774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_8B6")

    label("loc_78D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_8B6")

    label("loc_7A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_8B6")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_8B6")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_8B6")

    label("loc_7F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_8B6")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_8B6")

    label("loc_823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_8B6")

    label("loc_83C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_8B6")

    label("loc_855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_8B6")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_887")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_8B6")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_8B6")

    label("loc_8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_8B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_8B6")

    label("loc_8CB")

    Return()

    # Function_2_74F end

    def Function_3_8CC(): pass

    label("Function_3_8CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_947")

    ChrTalk(    #0
        0xFE,
        (
            "Seems like it'll be a while\x01",
            "until the next ship comes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Maybe I should get something to eat first.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A2")

    label("loc_947")

    OP_A2(0x5)

    ChrTalk(    #2
        0xFE,
        "Let's see, the ship to the capital is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Yeah, I've still got some time.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_9A2")

    TalkEnd(0xFE)
    Return()

    # Function_3_8CC end

    def Function_4_9A6(): pass

    label("Function_4_9A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A2C")

    ChrTalk(    #4
        0x1D,
        (
            "The capital-bound ship will be arriving soon.\x02\x03",

            "Recently it hasn't been late at all.\x01",
            "Airships really are convenient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADF")

    label("loc_A2C")

    OP_A2(0x4)

    ChrTalk(    #5
        0x1D,
        (
            "This was a very productive trip.\x02\x03",

            "There are a number of spots I'd\x01",
            "like to pick up as a tour guide.\x02\x03",

            "Now, time to go to the capital and negotiate\x01",
            "with the airship company!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADF")

    TalkEnd(0xFE)
    Return()

    # Function_4_9A6 end

    def Function_5_AE3(): pass

    label("Function_5_AE3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_CD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C11")

    ChrTalk(    #6
        0xFE,
        (
            "I've checked again and again but\x01",
            "there's nothing out of the ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "And yet, it just won't work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "But, if I give up here I'm\x01",
            "a failure as an engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm going to check it again! I'll check\x01",
            "it hundreds of times if that's what it\x01",
            "takes to find the cause!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_CD0")

    label("loc_C11")


    ChrTalk(    #10
        0xFE,
        (
            "The basics of engineering is inspection,\x01",
            "after all. Even my brother said so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I'm going to check it again! I'll check\x01",
            "it hundreds of times if that's what it\x01",
            "takes to find the cause!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD0")

    Jump("loc_1071")

    label("loc_CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8A")

    ChrTalk(    #12
        0xFE,
        "My brother Clive is on board the Arseille.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "My brother's great, so I'm sure he's\x01",
            "already fixed his orbal engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I-I'll do my best and not give up!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_DFA")

    label("loc_D8A")


    ChrTalk(    #15
        0xFE,
        (
            "I'm sure my brother Clive's already\x01",
            "fixed his orbal engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "We've got to do our best and do the same!\x02",
    )

    CloseMessageWindow()

    label("loc_DFA")

    Jump("loc_1071")

    label("loc_DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_EE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E80")

    ChrTalk(    #17
        0xFE,
        (
            "I'm slowly doing more and more\x01",
            "advanced work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I need to learn more and more\x01",
            "and become a full engineer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE5")

    label("loc_E80")

    OP_A2(0x3)

    ChrTalk(    #19
        0xFE,
        "The ramp's orbal mechanism is okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "All right, we're ready for docking any time.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_EE5")

    Jump("loc_1071")

    label("loc_EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F79")

    ChrTalk(    #21
        0xFE,
        "I'll do my best to become a full engineer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "For that glorious goal I've still got\x01",
            "a lot of things to study, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FEE")

    label("loc_F79")

    OP_A2(0x3)

    ChrTalk(    #23
        0xFE,
        (
            "I'm sure my brother Clive would\x01",
            "want to be researching too..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "I'll do my best to become a full engineer!\x02",
    )

    CloseMessageWindow()

    label("loc_FEE")

    Jump("loc_1071")

    label("loc_FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #25
        0xFE,
        "I'm an apprentice engineer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1071")

    label("loc_1023")

    OP_A2(0x3)

    ChrTalk(    #26
        0xFE,
        "Orbal mechanism lock checked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Yep, no problems, looks like.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_1071")

    TalkEnd(0xFE)
    Return()

    # Function_5_AE3 end

    def Function_6_1075(): pass

    label("Function_6_1075")


    ChrTalk(    #28
        0x1A,
        "Samario, you check the guidance lights.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1A,
        "Where's Todd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1B,
        "I had Todd check the docking equipment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1A,
        "I see. Well, then, we can leave that to him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1A,
        (
            "We don't have much time,\x01",
            "but be thorough.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1B, 0x10)
    Return()

    # Function_6_1075 end

    def Function_7_1149(): pass

    label("Function_7_1149")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11BF")

    ChrTalk(    #33
        0xFE,
        "Let's see... Next up is the Cecilia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If you intend to use it,\x01",
            "you should check in soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1264")

    label("loc_11BF")

    OP_A2(0x1)

    ChrTalk(    #35
        0xFE,
        "Let's see... Next up is the Cecilia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "At the moment, it'll arrive at\x01",
            "Ruan on schedule, we heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "If you intend to use it,\x01",
            "you should check in soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1264")

    Jump("loc_1529")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_135F")

    ChrTalk(    #38
        0xFE,
        (
            "Lately Todd's been a lot more\x01",
            "like a real engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "He can do most things even without me\x01",
            "giving him detailed instructions now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Haha, when I go away from time to time\x01",
            "and come back, I'm really struck by how \x01",
            "far he's come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1529")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1403")

    ChrTalk(    #41
        0xFE,
        (
            "At last! The new engine from the\x01",
            "central factory's going to be rolled\x01",
            "out, it sounds like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "As a technician, I'd love to have a look.\x02",
    )

    CloseMessageWindow()
    Jump("loc_149A")

    label("loc_1403")

    OP_A2(0x1)

    ChrTalk(    #43
        0xFE,
        (
            "At last! The new engine from the\x01",
            "central factory's going to be rolled\x01",
            "out, it sounds like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Now the Arseille will really be at full power.\x02",
    )

    CloseMessageWindow()

    label("loc_149A")

    Jump("loc_1529")

    label("loc_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1517")
    OP_4A(0x1B, 255)

    ChrTalk(    #45
        0xFE,
        (
            "We don't have much time,\x01",
            "but be thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "There'll be another ship coming plenty soon.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1B, 255)
    Jump("loc_1529")

    label("loc_1517")

    OP_A2(0x1)
    OP_A2(0x2)
    OP_4A(0x1B, 255)
    Call(0, 6)
    OP_4B(0x1B, 255)

    label("loc_1529")

    TalkEnd(0xFE)
    Return()

    # Function_7_1149 end

    def Function_8_152D(): pass

    label("Function_8_152D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1664")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F8")

    ChrTalk(    #47
        0xFE,
        (
            "Yeah, the quartz looks fine and the orbal\x01",
            "device itself seems to be fine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "But, the actual device itself won't move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "There may be some far more\x01",
            "core problem here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1661")

    label("loc_15F8")


    ChrTalk(    #50
        0xFE,
        (
            "I can't find anything abnormal in\x01",
            "any of the orbal devices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "But...the equipment isn't working.\x02",
    )

    CloseMessageWindow()

    label("loc_1661")

    Jump("loc_1C03")

    label("loc_1664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1783")

    ChrTalk(    #52
        0xFE,
        (
            "Even us engineers don't know the reason\x01",
            "the orbal devices have stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "If Clive was here, maybe he'd\x01",
            "know something, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I'm sure he's working hard on board\x01",
            "the Arseille as part of their crew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "I've got no choice but to do what I can.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_181F")

    label("loc_1783")


    ChrTalk(    #56
        0xFE,
        (
            "We still don't know anything about the reason\x01",
            "orbal devices have stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I'm sure Clive's on board the Arseille\x01",
            "having the same problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181F")

    Jump("loc_1C03")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1919")

    ChrTalk(    #58
        0xFE,
        (
            "It probably won't be too long before Todd\x01",
            "is able to work on his own as an engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Once that happens, Clive will finally\x01",
            "be able to join the research team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Job's gonna get busier, but well,\x01",
            "I'll do my best for my staff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C03")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1998")

    ChrTalk(    #61
        0xFE,
        (
            "Phew! We've got to get ready to\x01",
            "take in the next ship on our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "After all, Todd is off at Sunday School.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C03")

    label("loc_1998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A51")

    ChrTalk(    #63
        0xFE,
        (
            "Todd's worked harder than anyone to\x01",
            "make sure his brother's got nothing\x01",
            "to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Just a bit more and that kid'll be\x01",
            "a real good engineer, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAE")

    label("loc_1A51")

    OP_A2(0x2)

    ChrTalk(    #65
        0xFE,
        "Clive's got a great reputation as a researcher.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Enough that he was even asked to take\x01",
            "a look at the new engine design plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "But, he turned down the job to keep\x01",
            "an eye on his brother Todd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Probably because of that, Todd's\x01",
            "been working harder than any man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Just a bit more and that kid'll\x01",
            "be a real good engineer, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAE")

    Jump("loc_1C03")

    label("loc_1BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1C03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(    #70
        0xFE,
        "Sorry, we're in the middle of work stuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C03")

    label("loc_1BF1")

    OP_A2(0x2)
    OP_A2(0x1)
    OP_4A(0x1A, 255)
    Call(0, 6)
    OP_4B(0x1A, 255)

    label("loc_1C03")

    TalkEnd(0xFE)
    Return()

    # Function_8_152D end

    def Function_9_1C07(): pass

    label("Function_9_1C07")

    Call(0, 10)
    Return()

    # Function_9_1C07 end

    def Function_10_1C0C(): pass

    label("Function_10_1C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C27")
    OP_4A(0x11, 255)
    Call(0, 17)
    OP_4B(0x11, 255)
    Jump("loc_2169")

    label("loc_1C27")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCB")

    ChrTalk(    #71
        0x11,
        (
            "There's still been no word\x01",
            "from the airship company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        (
            "I suppose that makes sense, though, since\x01",
            "we can't use orbal communications.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1D05")

    label("loc_1CCB")


    ChrTalk(    #73
        0x11,
        (
            "There's still been no word\x01",
            "from the airship company.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D05")

    Jump("loc_2166")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB6")

    ChrTalk(    #74
        0x11,
        "Huh, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "Sorry, but we have no timeframe for\x01",
            "when airship service will resume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        (
            "I was just putting that up on\x01",
            "the schedule charts.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1E3D")

    label("loc_1DB6")


    ChrTalk(    #77
        0x11,
        (
            "Apparently the airliners are all stuck\x01",
            "in the landing ports all over the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "Well, guess we're lucky they didn't crash.\x02",
    )

    CloseMessageWindow()

    label("loc_1E3D")

    Jump("loc_2166")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(    #79
        0x11,
        (
            "Aww, man. Too bad it's over.\x01",
            "I would have headed out to help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1E")

    label("loc_1E94")

    OP_A2(0x0)

    ChrTalk(    #80
        0x11,
        (
            "Hey, seems like there was a bit\x01",
            "of a fight between both camps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "Aww, man. Too bad it's over.\x01",
            "I would have headed out to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1E")

    Jump("loc_2166")

    label("loc_1F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FD7")

    ChrTalk(    #82
        0x11,
        (
            "Of course we're cheering for Norman,\x01",
            "the promoter of tourism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "Reviving the harbor work's impossible.\x01",
            "The harbor itself is a freakin' ancient\x01",
            "artifact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2071")

    label("loc_1FD7")

    OP_A2(0x0)

    ChrTalk(    #84
        0x11,
        (
            "This election will probably have a big\x01",
            "impact on the landing port, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        (
            "I'm always paying attention to what\x01",
            "the candidates are saying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2071")

    Jump("loc_2166")

    label("loc_2074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2166")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20E8")

    ChrTalk(    #86
        0x11,
        (
            "During an election there are things to see that\x01",
            "you can only see during an election, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2166")

    label("loc_20E8")

    OP_A2(0x0)

    ChrTalk(    #87
        0x11,
        (
            "*yaaaaaaaawn* Lately I've been\x01",
            "kinda without much to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "Seems like tourists avoid the\x01",
            "place during an election.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2166")

    TalkEnd(0x11)

    label("loc_2169")

    Return()

    # Function_10_1C0C end

    def Function_11_216A(): pass

    label("Function_11_216A")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #89
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_216A end

    def Function_12_21B9(): pass

    label("Function_12_21B9")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_21D3")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_21D7")

    label("loc_21D3")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_21D7")

    OP_DB()
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    OP_6D(132050, 8360, 87990, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(7800, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0xA, 0x4)
    OP_6F(0x7, 100)
    OP_72(0xA, 0x4)
    SetChrPos(0xF, 136000, 7500, 82500, 90)
    SetChrPos(0x10, 136000, 5500, 82500, 90)
    SetChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x40)
    OP_A1(0xF, 0x8)
    OP_72(0x8, 0x4)
    OP_72(0x8, 0x20)
    OP_72(0x8, 0x2)
    OP_71(0x8, 0x400)
    OP_71(0x8, 0x40)
    OP_A1(0x10, 0x9)
    OP_72(0x9, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x1A, 134820, 8150, 93440, 180)
    SetChrPos(0x1B, 132030, 8150, 94310, 180)
    SetChrPos(0x1C, 134350, 8150, 92500, 180)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)
    OP_DE("Ruan")
    FadeToBright(2000, 0)

    def lambda_22EB():
        OP_6D(131670, 8360, 81790, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_22EB)

    def lambda_2303():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2303)

    def lambda_231B():
        OP_6B(3500, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_231B)

    def lambda_232B():
        OP_6C(134000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_232B)

    def lambda_233B():
        OP_8F(0xFE, 0x21340, 0x9C4, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_233B)

    def lambda_2356():
        OP_8F(0xFE, 0x21340, 0x7D0, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2356)
    WaitChrThread(0xF, 0x2)
    WaitChrThread(0x10, 0x2)

    def lambda_237B():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_237B)

    def lambda_2396():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2396)
    WaitChrThread(0xF, 0x3)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    WaitChrThread(0x0, 0x3)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_B0(0x8, 0x32)
    OP_B0(0x9, 0x32)
    OP_6F(0x8, 100)
    OP_70(0x8, 0x1)
    OP_6F(0x9, 100)
    OP_70(0x9, 0x1)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0x8)
    OP_73(0x9)
    Sleep(400)
    OP_B0(0x7, 0x2D)
    OP_6F(0x7, 100)
    OP_70(0x7, 0x0)
    OP_71(0xA, 0x4)
    OP_22(0x78, 0x0, 0x64)
    OP_73(0x7)
    Sleep(1000)
    OP_6F(0x8, 410)
    OP_70(0x8, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x8)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0xF7, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0xF7, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_48()
    OP_89(0x101, 137100, 8200, 82210, 90)
    OP_89(0xF7, 137100, 8200, 82210, 90)
    OP_89(0x8, 137100, 8200, 82210, 90)
    OP_89(0x9, 137100, 8200, 82210, 90)
    OP_89(0xA, 137100, 8200, 82210, 90)
    OP_89(0xB, 137100, 8200, 82210, 90)
    OP_89(0xC, 142970, 8300, 85160, 272)
    OP_89(0xD, 137100, 8200, 82210, 90)
    OP_89(0xE, 142970, 8300, 85160, 272)
    OP_43(0xA, 0x1, 0x0, 0xE)
    Sleep(1000)
    OP_43(0x9, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0x8, 0x1, 0x0, 0xD)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(1200)
    OP_43(0xC, 0x1, 0x0, 0x10)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(1000)
    OP_43(0xF7, 0x1, 0x0, 0xF)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x10)
    Sleep(1200)
    OP_43(0xD, 0x1, 0x0, 0xD)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    OP_DC()
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_12_21B9 end

    def Function_13_2611(): pass

    label("Function_13_2611")

    OP_8E(0xFE, 0x20ADA, 0x2008, 0x14294, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_2611 end

    def Function_14_2653(): pass

    label("Function_14_2653")

    OP_8E(0xFE, 0x2092C, 0x2008, 0x14262, 0x1388, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x1388, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_2653 end

    def Function_15_2695(): pass

    label("Function_15_2695")

    OP_8E(0xFE, 0x20ADA, 0x2008, 0x14294, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20274, 0x2008, 0x14C3A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    Return()

    # Function_15_2695 end

    def Function_16_26D2(): pass

    label("Function_16_26D2")

    OP_8E(0xFE, 0x20314, 0x2008, 0x14EBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2031E, 0x1F9A, 0x179D0, 0x7D0, 0x0)
    Return()

    # Function_16_26D2 end

    def Function_17_26FB(): pass

    label("Function_17_26FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2715")
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_2715")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(100140, 0, 83780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 99550, 0, 84460, 90)
    SetChrPos(0xF7, 99470, 0, 83460, 90)
    SetChrPos(0x105, 98390, 0, 84500, 90)
    SetChrPos(0x104, 98500, 0, 83270, 90)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4B")
    OP_A2(0x1402)

    ChrTalk(    #90
        0x11,
        "#6PWelcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#6PYou're the group of bracers\x01",
            "heading for Zeiss, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1011FUh-huh, that's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x11,
        (
            "#6PWe just got word from Jean.\x01",
            "The guild's already paid your fares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        "#6PWould you like to check in now, or...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2913")

    ChrTalk(    #95
        0x106,
        (
            "#050FWe'll have to stick around and wait\x01",
            "for the ship once we check in.\x02\x03",

            "You're all done here in Ruan, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A1")

    label("loc_2913")


    ChrTalk(    #96
        0x103,
        (
            "#020FIt'd be best to stay here and wait\x01",
            "for the ship once we check in.\x02\x03",

            "Are you sure you've done everything\x01",
            "you want to do here in Ruan?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A1")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Still Got Stuff To Do\x01",      # 0
            "Let's Check In\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A48")

    ChrTalk(    #97
        0x11,
        (
            "#6PJust give the word when you\x01",
            "want to check in, then.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2A48")

    Jump("loc_2B1B")

    label("loc_2A4B")


    ChrTalk(    #98
        0x11,
        (
            "#6PHow about it, then?\x01",
            "Ready to check in?\x02",
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
            "Still Got Stuff To Do\x01",      # 0
            "Let's Check In\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")

    ChrTalk(    #99
        0x11,
        (
            "#6PJust give the word when you\x01",
            "want to check in.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2B1B")

    OP_8C(0xF7, 90, 400)

    ChrTalk(    #100
        0x11,
        "#6PAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "#6PJust a little bit of paperwork for you\x01",
            "to fill out first, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1006FSure.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #103
        "\x07\x05Estelle's group checked in for their flight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #104
        0x11,
        (
            "#6PHmm... Okay, no problems,\x01",
            "it looks like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x11,
        (
            "#6PFeel free to make use of the port\x01",
            "until the next flight arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1001FThanks!\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call(0, 18)
    Return()

    # Function_17_26FB end

    def Function_18_2CB5(): pass

    label("Function_18_2CB5")

    ClearMapFlags(0x1)
    OP_6D(132370, 8150, 95580, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(146000, 0)
    OP_6E(302, 0)
    SetChrPos(0xF, 136000, 1000, 82200, 90)
    SetChrPos(0x10, 136000, 1000, 82200, 90)
    SetChrFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x40)
    OP_A1(0xF, 0xB)
    OP_A1(0x10, 0x9)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    OP_72(0xB, 0x4)
    SetChrPos(0x21, 132100, 8150, 96320, 185)
    SetChrPos(0x1F, 132680, 8150, 94880, 197)
    SetChrPos(0xC, 131790, 8150, 94810, 185)
    SetChrPos(0xB, 130490, 8150, 95130, 175)
    SetChrPos(0x20, 131360, 8150, 96150, 177)
    SetChrPos(0xE, 130240, 8150, 96640, 185)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_71(0xA, 0x4)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0x21, 0x20)
    SetChrBattleFlags(0x1F, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0x20, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_48()
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0x101, 132260, 8150, 97290, 184)
    SetChrPos(0xF7, 131250, 8150, 97380, 184)
    SetChrPos(0x104, 131250, 8150, 98500, 184)
    SetChrPos(0x105, 132310, 8150, 98400, 184)
    Sleep(2000)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(2000)
    OP_22(0xC8, 0x0, 0x64)
    Sleep(500)
    OP_22(0x76, 0x0, 0x64)
    OP_22(0x78, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0xB, 1)
    OP_6F(0x7, 0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_62(0x1F, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x1F, 0x1, 0x0, 0x15)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0xC, 0x1, 0x0, 0x16)
    Sleep(300)
    OP_43(0xB, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x21, 0x1, 0x0, 0x17)
    Sleep(1300)
    OP_43(0x20, 0x1, 0x0, 0x17)
    Sleep(200)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(2000)
    OP_6D(131700, 8150, 97100, 1000)

    ChrTalk(    #107
        0x101,
        "#1006F#6PAlrighty then. Off we go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#542F#6PYes, let's.\x02",
    )

    CloseMessageWindow()

    def lambda_2F77():
        OP_8E(0xFE, 0x204A4, 0x1FD6, 0x174B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F77)
    Sleep(50)

    def lambda_2F97():
        OP_8E(0xFE, 0x200B2, 0x1FD6, 0x175AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_2F97)
    Sleep(50)

    def lambda_2FB7():
        OP_8E(0xFE, 0x2049A, 0x1FD6, 0x17A52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FB7)
    Sleep(50)

    def lambda_2FD7():
        OP_8E(0xFE, 0x20030, 0x1FD6, 0x17B42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2FD7)
    Sleep(300)
    SetChrPos(0x12, 122550, 6150, 101030, 90)

    NpcTalk(    #109
        0x12,
        "Boy's Voice",
        (
            "#1PHeeeeeey!\x01",
            "Wait a seeeeeeeeeeec!\x02",
        )
    )

    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x105, 0x0)
    WaitChrThread(0x104, 0x0)
    CloseMessageWindow()
    OP_20(0x3E8)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_30BB():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30BB)

    def lambda_30C9():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30C9)
    Sleep(100)

    def lambda_30DC():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30DC)

    def lambda_30EA():
        OP_8C(0xFE, 334, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_30EA)
    OP_21()
    OP_1D(0x58)
    Sleep(500)

    def lambda_3100():
        OP_6D(124110, 8150, 100440, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3100)

    def lambda_3118():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3118)
    SetChrPos(0x12, 122550, 6150, 101430, 90)
    SetChrPos(0x14, 121550, 6150, 101430, 90)
    SetChrPos(0x13, 120550, 6150, 101430, 90)
    SetChrPos(0x15, 119550, 6150, 101430, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    OP_43(0x12, 0x1, 0x0, 0x18)
    Sleep(100)
    OP_43(0x14, 0x1, 0x0, 0x19)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x1A)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x1B)
    Sleep(3000)

    def lambda_31CC():
        OP_6D(133070, 8150, 96500, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_31CC)

    def lambda_31E4():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_31E4)

    def lambda_31FC():
        OP_8E(0xFE, 0x2060C, 0x1FD6, 0x17CE6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_31FC)
    Sleep(100)

    def lambda_321C():
        OP_8E(0xFE, 0x20666, 0x1FD6, 0x17854, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_321C)
    Sleep(200)

    def lambda_323C():
        OP_8E(0xFE, 0x201A2, 0x1FD6, 0x17854, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_323C)
    Sleep(100)

    def lambda_325C():
        OP_8E(0xFE, 0x200A8, 0x1FD6, 0x17DD6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_325C)
    WaitChrThread(0x101, 0x0)

    def lambda_327C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_327C)
    WaitChrThread(0x105, 0x0)

    def lambda_328F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_328F)
    WaitChrThread(0xF7, 0x0)

    def lambda_32A2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_32A2)
    WaitChrThread(0x104, 0x0)

    def lambda_32B5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32B5)
    WaitChrThread(0x1, 0x2)
    WaitChrThread(0x1, 0x3)

    ChrTalk(    #110
        0x101,
        "#1004F#4PTh-The kids!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x105,
        "#7P#044FWhat are all of you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x13,
        "#1732F#3PWe came to say bye-bye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x12,
        (
            "#772F#6PMaaaan, you guys are COLD!\x02\x03",

            "Just takin' off without sayin'\x01",
            "anything to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x14,
        (
            "#1712F#6PYou guys are meaniefaces!\x01",
            "The worst kind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x15,
        "#1722F#1PMiss Kloeeeee, why do you have to go?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x15, 400)

    ChrTalk(    #116
        0x105,
        (
            "#542F#7POh... I'm sorry, everyone.\x02\x03",

            "I was going to say goodbye, but\x01",
            "we thought you were all out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1016F#4PI get it. They were 'out' coming\x01",
            "to Ruan! I feel kinda silly now...\x02\x03",

            "#1004FHang on, though, that'd mean Matron Theresa's...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x18, 125500, 6400, 101150, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x16, 125500, 6400, 101150, 90)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x17, 125500, 6400, 101150, 90)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x19, 125500, 6400, 101150, 90)
    ClearChrFlags(0x19, 0x80)

    NpcTalk(    #118
        0x18,
        "Woman's Voice",
        "#5PI'm glad to see we made it in time.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x18, 0x3, 0x0, 0x25)
    OP_43(0x18, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x16, 0x1, 0x0, 0x1D)

    def lambda_35EB():

        label("loc_35EB")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_35EB")

    QueueWorkItem2(0x101, 1, lambda_35EB)

    def lambda_35FC():

        label("loc_35FC")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_35FC")

    QueueWorkItem2(0xF7, 1, lambda_35FC)
    OP_43(0x104, 0x0, 0x0, 0x27)
    OP_43(0x105, 0x0, 0x0, 0x26)
    Sleep(500)

    def lambda_3620():
        OP_6D(133670, 8150, 96500, 2000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3620)

    def lambda_3638():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3638)
    OP_43(0x17, 0x1, 0x0, 0x1E)
    OP_43(0x19, 0x1, 0x0, 0x1F)
    WaitChrThread(0x18, 0x1)

    ChrTalk(    #119
        0x101,
        (
            "#1008F#4PMatron Theresa!\x01",
            "And even Jill and Hans came...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x16,
        (
            "#641F#6PHaha, well, duh! Like we'd miss this!\x01",
            "We cut it kinda close, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x17,
        (
            "#734FThanks to the fact that you wanted\x01",
            "to wait till the last second to keep\x01",
            "it a surprise, Jill...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x16,
        "#648F#6PHeeeey, all's well that ends well, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x18,
        (
            "#751F#6PActually, it was Jill who let\x01",
            "us know you were leaving.\x02\x03",

            "I thought it would be nice\x01",
            "if we could see you off.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x105, 0x1)

    ChrTalk(    #124
        0x19,
        (
            "#781F#6PHeheh. And pay no mind to\x01",
            "the old man in the corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#542F#7POh, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x12,
        (
            "#775F#6P...Hey, Estelle?\x02\x03",

            "I heard that Joshua...ran away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1026F#4POh... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14,
        "#1713F#6PMatron Theresa told us what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1007F#4PI see...\x02\x03",

            "#1003FI'm sorry. I should've told you all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x14,
        (
            "#1710F#6PNo, it's okay.\x02\x03",

            "#1718FUm... We'll pray that Joshua\x01",
            "comes home real soon!\x02\x03",

            "We'll pray to Aidios every day!\x01",
            "Promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x15,
        "#1721F#5PI'll pray too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x13,
        "#1732F#6PIt'll come true if we all do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1025F#4POh... You guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x105,
        "#048F#7PHahaha... Oh, children, thank you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x16,
        (
            "#644F#6PI'll throw my prayers into the pile, too.\x02\x03",

            "#648FEstelle, Kloe, you two be careful, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x17,
        (
            "#730FYou do need to try your best, but don't\x01",
            "overdo it and put yourself in danger.\x02\x03",

            "If something happened to you, I...\x01",
            "don't think he'd ever forgive himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x105,
        "#542F#7PJill... Hans...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1017F#4PYeah... I'll remember that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x18,
        (
            "#750F#6PEstelle, please look after Kloe.\x02\x03",

            "I know she seems strong, but she's\x01",
            "still a little fragile in some ways.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #140
        0x105,
        "#540F#7PM-Matron...I'm right here, you know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1008F#4PHaha! Leave her to me!\x02\x03",

            "#1016FI kinda suspect she's going to be helping\x01",
            "US out more than anything, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x18,
        (
            "#751F#6PWell...\x02\x03",

            "#750FKloe? Use this as a chance to examine\x01",
            "yourself and your desires.\x02\x03",

            "Don't fret. Simply look for the\x01",
            "answer you've been seeking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x105,
        "#048F#7PYes... I will. I promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x19,
        (
            "#783F#6PBracers and students... Both aspire to\x01",
            "the path of knowledge, in their own ways.\x02\x03",

            "#780FYou two have grown immensely in the\x01",
            "short amount of time you've been here.\x02\x03",

            "Always remember, you never run out\x01",
            "of things to learn. Do not become so\x01",
            "overconfident that you forget to learn.\x02\x03",

            "#781FIf you remember that, there is no obstacle\x01",
            "in the world that can defeat you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        "#1006F#4P#1KYes, sir!\x02",
    )


    ChrTalk(    #146
        0x105,
        "#041F#1P#1KWe'll remember!\x02",
    )

    OP_56(0x1)
    OP_59()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetChrName("Woman's Voice")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #147
        (
            "\x07\x05This is the final boarding call for\x01",
            "the Cecilia, bound for Zeiss.\x02\x03",

            "All remaining passengers should embark now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #148
        0x101,
        "#1004F#4PEr, whoops!\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_4035():

        label("loc_4035")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4035")

    QueueWorkItem2(0x12, 1, lambda_4035)

    def lambda_4046():

        label("loc_4046")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4046")

    QueueWorkItem2(0x14, 1, lambda_4046)
    Sleep(100)

    def lambda_405C():

        label("loc_405C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_405C")

    QueueWorkItem2(0x13, 1, lambda_405C)

    def lambda_406D():

        label("loc_406D")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_406D")

    QueueWorkItem2(0x15, 1, lambda_406D)
    Sleep(100)

    def lambda_4083():

        label("loc_4083")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4083")

    QueueWorkItem2(0x18, 1, lambda_4083)

    def lambda_4094():

        label("loc_4094")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4094")

    QueueWorkItem2(0x16, 1, lambda_4094)

    def lambda_40A5():

        label("loc_40A5")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40A5")

    QueueWorkItem2(0x17, 1, lambda_40A5)

    def lambda_40B6():

        label("loc_40B6")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_40B6")

    QueueWorkItem2(0x19, 1, lambda_40B6)
    OP_43(0x101, 0x1, 0x0, 0x20)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x20)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x20)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x14, 0x1)
    OP_44(0x13, 0x1)
    OP_44(0x15, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x19, 0x1)
    SetChrPos(0x12, 133000, 8090, 94500, 180)
    SetChrPos(0x14, 132610, 8090, 95000, 180)
    SetChrPos(0x13, 131710, 8090, 94500, 180)
    SetChrPos(0x15, 131100, 8090, 94800, 180)
    SetChrPos(0x18, 133310, 8090, 95600, 180)
    SetChrPos(0x16, 132610, 8090, 96200, 180)
    SetChrPos(0x17, 131610, 8090, 96200, 180)
    SetChrPos(0x19, 132300, 8150, 97250, 180)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrFlags(0x3, 0x20)
    OP_48()
    SetChrPos(0xF7, 133390, 8200, 84310, 0)
    SetChrPos(0x101, 132420, 8200, 84780, 0)
    SetChrPos(0x105, 131400, 8200, 84690, 0)
    SetChrPos(0x104, 132250, 8200, 83530, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x104, 0)
    OP_6D(132310, 8090, 90270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #149
        0x101,
        (
            "#1018F#2PSee you, guys! We'll be back!\x01",
            "I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x105,
        "#048F#2PEveryone, take care!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x12,
        "#771F#6PBe careful, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x16,
        (
            "#641F#6PYou better come back with some great\x01",
            "stories...and bring Joshua back with you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_DB()
    Fade(1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    ClearMapFlags(0x10)
    OP_6D(132160, 8200, 85340, 0)
    OP_67(0, 11210, -10000, 0)
    OP_6B(4730, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    OP_0D()
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x64)
    OP_73(0x7)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x3C)
    OP_73(0xB)
    Sleep(500)
    SetChrFlags(0x0, 0x20)
    SetChrFlags(0x1, 0x20)
    SetChrFlags(0x2, 0x20)
    SetChrFlags(0x3, 0x20)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_43(0xF, 0x2, 0x0, 0x13)

    def lambda_4402():
        OP_6D(160160, 8200, 85340, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4402)

    def lambda_441A():

        label("loc_441A")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_441A")

    QueueWorkItem2(0x101, 2, lambda_441A)

    def lambda_442B():

        label("loc_442B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_442B")

    QueueWorkItem2(0xF7, 2, lambda_442B)

    def lambda_443C():

        label("loc_443C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_443C")

    QueueWorkItem2(0x105, 2, lambda_443C)

    def lambda_444D():

        label("loc_444D")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_444D")

    QueueWorkItem2(0x104, 2, lambda_444D)

    def lambda_445E():

        label("loc_445E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_445E")

    QueueWorkItem2(0x13, 2, lambda_445E)

    def lambda_446F():

        label("loc_446F")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_446F")

    QueueWorkItem2(0x12, 2, lambda_446F)

    def lambda_4480():

        label("loc_4480")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_4480")

    QueueWorkItem2(0x14, 2, lambda_4480)

    def lambda_4491():

        label("loc_4491")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_4491")

    QueueWorkItem2(0x15, 2, lambda_4491)

    def lambda_44A2():

        label("loc_44A2")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_44A2")

    QueueWorkItem2(0x16, 2, lambda_44A2)

    def lambda_44B3():

        label("loc_44B3")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_44B3")

    QueueWorkItem2(0x18, 2, lambda_44B3)

    def lambda_44C4():

        label("loc_44C4")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_44C4")

    QueueWorkItem2(0x17, 2, lambda_44C4)

    def lambda_44D5():

        label("loc_44D5")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_44D5")

    QueueWorkItem2(0x19, 2, lambda_44D5)

    def lambda_44E6():
        OP_8F(0xFE, 0x27100, 0xDDE, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_44E6)

    def lambda_4501():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4501)

    def lambda_451C():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_451C)

    def lambda_4537():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4537)

    def lambda_4552():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4552)

    def lambda_456D():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_456D)
    Sleep(600)

    def lambda_458D():
        OP_8F(0xFE, 0x27100, 0x11C6, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_458D)

    def lambda_45A8():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_45A8)

    def lambda_45C3():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_45C3)

    def lambda_45DE():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_45DE)

    def lambda_45F9():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_45F9)

    def lambda_4614():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4614)
    Sleep(700)

    def lambda_4634():
        OP_8F(0xFE, 0x27100, 0x15AE, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4634)

    def lambda_464F():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_464F)

    def lambda_466A():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_466A)

    def lambda_4685():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4685)

    def lambda_46A0():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_46A0)

    def lambda_46BB():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_46BB)
    Sleep(800)
    OP_43(0x12, 0x0, 0x0, 0x21)
    OP_43(0x14, 0x0, 0x0, 0x22)
    OP_43(0x13, 0x0, 0x0, 0x23)
    OP_43(0x15, 0x0, 0x0, 0x24)

    def lambda_46F7():
        OP_8F(0xFE, 0x27100, 0x1996, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_46F7)

    def lambda_4712():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4712)

    def lambda_472D():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_472D)

    def lambda_4748():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4748)

    def lambda_4763():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4763)

    def lambda_477E():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_477E)
    Sleep(900)

    def lambda_479E():
        OP_8F(0xFE, 0x27100, 0x1D7E, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_479E)

    def lambda_47B9():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_47B9)

    def lambda_47D4():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_47D4)

    def lambda_47EF():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_47EF)

    def lambda_480A():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_480A)

    def lambda_4825():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4825)
    Sleep(1500)

    def lambda_4845():
        OP_8F(0xFE, 0x27100, 0x2166, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4845)

    def lambda_4860():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4860)

    def lambda_487B():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_487B)

    def lambda_4896():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4896)

    def lambda_48B1():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_48B1)

    def lambda_48CC():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_48CC)
    Sleep(1500)
    OP_20(0xFA0)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_43(0xF, 0x3, 0x0, 0x14)

    def lambda_4907():
        OP_8F(0xFE, 0x27100, 0x254E, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4907)

    def lambda_4922():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4922)

    def lambda_493D():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_493D)

    def lambda_4958():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4958)

    def lambda_4973():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4973)

    def lambda_498E():
        OP_91(0xFE, 0x5DC0, 0xA5A, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_498E)
    OP_0D()
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    ClearChrFlags(0x0, 0x20)
    ClearChrFlags(0x1, 0x20)
    ClearChrFlags(0x2, 0x20)
    ClearChrFlags(0x3, 0x20)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x3, 0xFF)
    OP_A2(0x1403)
    OP_A2(0x10F1)
    OP_28(0x65, 0x4, 0x40)
    OP_28(0x66, 0x4, 0x40)
    OP_28(0x67, 0x4, 0x40)
    OP_28(0x68, 0x4, 0x40)
    OP_28(0x69, 0x4, 0x40)
    OP_28(0x6B, 0x4, 0x40)
    OP_28(0xA1, 0x4, 0x40)
    OP_28(0xA2, 0x4, 0x40)
    OP_28(0xA3, 0x4, 0x40)
    OP_28(0xA4, 0x4, 0x40)
    OP_21()
    Sleep(1000)
    OP_DC()
    NewScene("ED6_DT21/E0001   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2CB5 end

    def Function_19_4A21(): pass

    label("Function_19_4A21")

    OP_B0(0xB, 0x32)
    OP_6F(0xB, 61)
    OP_70(0xB, 0xA0)
    OP_73(0xB)
    OP_71(0xB, 0x20)
    OP_6F(0xB, 161)
    OP_70(0xB, 0x104)
    Return()

    # Function_19_4A21 end

    def Function_20_4A4A(): pass

    label("Function_20_4A4A")

    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    Return()

    # Function_20_4A4A end

    def Function_21_4A8D(): pass

    label("Function_21_4A8D")

    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0x1770, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_4A8D end

    def Function_22_4ABB(): pass

    label("Function_22_4ABB")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_63(0xFE)
    Return()

    # Function_22_4ABB end

    def Function_23_4AFE(): pass

    label("Function_23_4AFE")

    OP_8E(0xFE, 0x20350, 0x206C, 0x16E7C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2035A, 0x1FD6, 0x13FCE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_4AFE end

    def Function_24_4B2C(): pass

    label("Function_24_4B2C")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20E4A, 0x1FD6, 0x18042, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20A62, 0x1FD6, 0x173AE, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_24_4B2C end

    def Function_25_4B70(): pass

    label("Function_25_4B70")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20FC6, 0x1FD6, 0x18240, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20AF8, 0x1FD6, 0x1776E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_4B70 end

    def Function_26_4BB4(): pass

    label("Function_26_4BB4")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20EEA, 0x1FD6, 0x1825E, 0xFA0, 0x0)
    OP_8E(0xFE, 0x209CC, 0x1FD6, 0x17B88, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_26_4BB4 end

    def Function_27_4BF8(): pass

    label("Function_27_4BF8")

    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xFA0, 0x0)
    OP_8E(0xFE, 0x20F44, 0x1FD6, 0x18222, 0xFA0, 0x0)
    OP_8E(0xFE, 0x207BA, 0x1FD6, 0x17F84, 0xFA0, 0x0)
    TurnDirection(0xFE, 0x105, 400)
    Return()

    # Function_27_4BF8 end

    def Function_28_4C3C(): pass

    label("Function_28_4C3C")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20E36, 0x1FD6, 0x178EA, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_4C3C end

    def Function_29_4C80(): pass

    label("Function_29_4C80")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20D32, 0x1FD6, 0x17D36, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_4C80 end

    def Function_30_4CC4(): pass

    label("Function_30_4CC4")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x210FC, 0x1FD6, 0x17BE2, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_30_4CC4 end

    def Function_31_4D08(): pass

    label("Function_31_4D08")

    OP_8E(0xFE, 0x1F8E2, 0x1806, 0x18C04, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20EB8, 0x1FD6, 0x1895C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20FE4, 0x1FD6, 0x1809C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_31_4D08 end

    def Function_32_4D4C(): pass

    label("Function_32_4D4C")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x20378, 0x1FD6, 0x170F2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x20422, 0x1F9A, 0x154B4, 0x7D0, 0x0)
    Return()

    # Function_32_4D4C end

    def Function_33_4D7C(): pass

    label("Function_33_4D7C")

    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x224D4, 0x1FD6, 0x16F30, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_4DA8():

        label("loc_4DA8")

        TurnDirection(0xFE, 0xF7, 400)
        OP_48()
        Jump("loc_4DA8")

    QueueWorkItem2(0x12, 2, lambda_4DA8)
    Return()

    # Function_33_4D7C end

    def Function_34_4DB4(): pass

    label("Function_34_4DB4")

    Sleep(300)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x222E0, 0x1FD6, 0x171CE, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_4DE5():

        label("loc_4DE5")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_4DE5")

    QueueWorkItem2(0x14, 2, lambda_4DE5)
    Return()

    # Function_34_4DB4 end

    def Function_35_4DF1(): pass

    label("Function_35_4DF1")

    Sleep(500)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x21E9E, 0x1FD6, 0x16FC6, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_4E22():

        label("loc_4E22")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4E22")

    QueueWorkItem2(0x13, 2, lambda_4E22)
    Return()

    # Function_35_4DF1 end

    def Function_36_4E2E(): pass

    label("Function_36_4E2E")

    Sleep(800)
    OP_44(0xFE, 0x2)
    OP_8C(0xFE, 90, 600)
    OP_8E(0xFE, 0x21C46, 0x1FD6, 0x1721E, 0xFA0, 0x0)
    OP_8C(0xFE, 185, 400)

    def lambda_4E5F():

        label("loc_4E5F")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_4E5F")

    QueueWorkItem2(0x15, 2, lambda_4E5F)
    Return()

    # Function_36_4E2E end

    def Function_37_4E6B(): pass

    label("Function_37_4E6B")

    OP_8C(0x101, 354, 400)
    Sleep(500)
    OP_8C(0xF7, 354, 400)
    Sleep(500)
    OP_8C(0x104, 354, 400)
    Return()

    # Function_37_4E6B end

    def Function_38_4E8B(): pass

    label("Function_38_4E8B")

    OP_8C(0xFE, 315, 400)

    def lambda_4E98():

        label("loc_4E98")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_4E98")

    QueueWorkItem2(0x105, 1, lambda_4E98)
    Return()

    # Function_38_4E8B end

    def Function_39_4EA4(): pass

    label("Function_39_4EA4")

    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)

    def lambda_4EC2():

        label("loc_4EC2")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_4EC2")

    QueueWorkItem2(0x104, 1, lambda_4EC2)
    Return()

    # Function_39_4EA4 end

    def Function_40_4ECE(): pass

    label("Function_40_4ECE")

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
        (0, "loc_4F47"),
        (1, "loc_4F4D"),
        (SWITCH_DEFAULT, "loc_4F53"),
    )


    label("loc_4F47")

    OP_A2(0x1200)
    Jump("loc_4F53")

    label("loc_4F4D")

    OP_A2(0x1201)
    Jump("loc_4F53")

    label("loc_4F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4F61")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_4F65")

    label("loc_4F61")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_4F65")

    Return()

    # Function_40_4ECE end

    def Function_41_4F66(): pass

    label("Function_41_4F66")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4FDD")

    AnonymousTalk(    #153
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "※All flights currently suspended. -Port Reception\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5019")

    label("loc_4FDD")


    AnonymousTalk(    #154
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Bose\x01",
            "⇒ To Zeiss\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5019")

    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_4F66 end

    def Function_42_502F(): pass

    label("Function_42_502F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #155
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_42_502F end

    def Function_43_50AE(): pass

    label("Function_43_50AE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #156
        "\x07\x05※Employees Only 《Liberl Orbalship Co.》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_43_50AE end

    SaveToFile()

Try(main)

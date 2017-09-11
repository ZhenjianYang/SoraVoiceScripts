from ED6ScenarioHelper import *

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
            'ED6_DT01/T2102   ._SN',
            'ED6_DT01/T2102_1 ._SN',
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
        '1st Lieutenant Schwarz',               # 9
        'Nial',                                 # 10
        'Sieg',                                 # 11
        'Colonel Richard',                      # 12
        'Captain Amalthea',                     # 13
        'Simon',                                # 14
        'Camera',                               # 15
        'Hardt',                                # 16
        'Edwin',                                # 17
        'Clive',                                # 18
        'Samario',                              # 19
        'Todd',                                 # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
        'Royal Guardsman',                      # 33
        'Royal Guardsman',                      # 34
        'Royal Guardsman',                      # 35
        'Royal Guardsman',                      # 36
        ' ',                                    # 37
        ' ',                                    # 38
        'Ruan - North Block',                   # 39
    )

    DeclEntryPoint(
        Unknown_00              = 94000,
        Unknown_04              = 0,
        Unknown_08              = 80000,
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
        'ED6_DT07/CH02323 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH02090 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH02100 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01470 ._CH',             # 09
        'ED6_DT07/CH01320 ._CH',             # 0A
        'ED6_DT06/CH20127 ._CH',             # 0B
        'ED6_DT06/CH20128 ._CH',             # 0C
        'ED6_DT06/CH20129 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02323P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH02090P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH02100P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01470P._CP',             # 09
        'ED6_DT07/CH01320P._CP',             # 0A
        'ED6_DT06/CH20127P._CP',             # 0B
        'ED6_DT06/CH20128P._CP',             # 0C
        'ED6_DT06/CH20129P._CP',             # 0D
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 6130,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
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
        X                   = 47780,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
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
        X                   = 111490,
        Z                   = 4150,
        Y                   = 81190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        X                   = 147300,
        Z                   = 8200,
        Y                   = 95200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 134200,
        Z                   = 8200,
        Y                   = 93000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 140500,
        Z                   = 6100,
        Y                   = 100500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 126600,
        Z                   = 8200,
        Y                   = 95200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 134940,
        Z                   = 8050,
        Y                   = 85090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 129360,
        Z                   = 8050,
        Y                   = 85070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130139,
        Z                   = 8050,
        Y                   = 85100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 134140,
        Z                   = 8050,
        Y                   = 85130,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 133300,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 132100,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 83500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 82200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 80900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 130900,
        Z                   = 8050,
        Y                   = 79600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        TriggerX            = 114900,
        TriggerZ            = 0,
        TriggerY            = 101600,
        TriggerRange        = 2000,
        ActorX              = 114900,
        ActorZ              = 1500,
        ActorY              = 101600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
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
        TalkFunctionIndex   = 6,
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
        TalkFunctionIndex   = 16,
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
        TalkFunctionIndex   = 17,
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
        TalkFunctionIndex   = 18,
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
        TalkFunctionIndex   = 18,
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
        TalkFunctionIndex   = 18,
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
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_61A",          # 00, 0
        "Function_1_805",          # 01, 1
        "Function_2_8BF",          # 02, 2
        "Function_3_A3C",          # 03, 3
        "Function_4_AEE",          # 04, 4
        "Function_5_C0A",          # 05, 5
        "Function_6_C8F",          # 06, 6
        "Function_7_159A",         # 07, 7
        "Function_8_1BAC",         # 08, 8
        "Function_9_2214",         # 09, 9
        "Function_10_271D",        # 0A, 10
        "Function_11_472F",        # 0B, 11
        "Function_12_4778",        # 0C, 12
        "Function_13_47AD",        # 0D, 13
        "Function_14_47EF",        # 0E, 14
        "Function_15_4838",        # 0F, 15
        "Function_16_4889",        # 10, 16
        "Function_17_48F2",        # 11, 17
        "Function_18_4971",        # 12, 18
    )


    def Function_0_61A(): pass

    label("Function_0_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_63A")
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x13, 147500, 8150, 95630, 90)
    Jump("loc_7C9")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_65A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x13, 147500, 8150, 95630, 90)
    Jump("loc_7C9")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_67F")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x13, 135010, 8150, 94960, 0)
    Jump("loc_7C9")

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_6C1")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 136900, 6100, 101800, 135)
    SetChrPos(0x13, 137600, 6100, 99400, 0)
    SetChrPos(0x12, 139000, 6100, 101400, 270)
    Jump("loc_7C9")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_70D")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 96700, 1000, 90100, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 98600, 0, 81460, 45)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x13, 159290, 0, 107030, 90)
    Jump("loc_7C9")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_73E")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 132010, 8360, 93010, 90)
    SetChrPos(0x13, 132950, 8150, 96370, 180)
    Jump("loc_7C9")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_76F")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 129600, 8200, 94200, 0)
    SetChrPos(0x13, 129600, 8200, 96800, 180)
    Jump("loc_7C9")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_78A")
    SetChrPos(0x13, 159290, 0, 107030, 90)
    Jump("loc_7C9")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, 131500, 8150, 97650, 180)
    SetChrPos(0x13, 130539, 8150, 96030, 45)
    SetChrPos(0x12, 132620, 8150, 95740, 315)

    label("loc_7C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7E8")
    OP_64(0x0, 0x1)

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_804")
    OP_A3(0x3FA)
    Event(0, 10)
    OP_B1("t2102_1")
    OP_71(0xA, 0x4)

    label("loc_804")

    Return()

    # Function_0_61A end

    def Function_1_805(): pass

    label("Function_1_805")

    OP_16(0x2, 0xFA0, 0x4E20, 0xFFFF63C0, 0x30049)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_838")
    OP_B1("t2102_y")
    Jump("loc_89A")

    label("loc_838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_850")
    OP_B1("t2102_0")
    Jump("loc_89A")

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868")
    OP_B1("t2102_2")
    Jump("loc_89A")

    label("loc_868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_880")
    OP_B1("t2102_0")
    Jump("loc_89A")

    label("loc_880")

    OP_B1("t2102_0")
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x7, 100)

    label("loc_89A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x1, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B9")
    OP_64(0x0, 0x1)

    label("loc_8B9")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_805 end

    def Function_2_8BF(): pass

    label("Function_2_8BF")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A26")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A26")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A26")

    label("loc_916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A26")

    label("loc_92F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A26")

    label("loc_948")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A26")

    label("loc_961")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A26")

    label("loc_97A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A26")

    label("loc_993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A26")

    label("loc_9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A26")

    label("loc_9C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A26")

    label("loc_9DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A26")

    label("loc_9F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A10")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A26")

    label("loc_A10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A26")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A26")

    label("loc_A3B")

    Return()

    # Function_2_8BF end

    def Function_3_A3C(): pass

    label("Function_3_A3C")

    TalkBegin(0x9)

    ChrTalk(    #0
        0xFE,
        (
            "#140FYo. Just got to work on a few\x01",
            "things in Grancel.\x02\x03",

            "I'm holding out for a seat to\x01",
            "free up on the airliner.\x02\x03",

            "I'm planning to come back to\x01",
            "Ruan soon enough, though.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_3_A3C end

    def Function_4_AEE(): pass

    label("Function_4_AEE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    OP_A2(0x1)

    ChrTalk(    #1
        0xFE,
        (
            "Now then...if I go back to Bose,\x01",
            "I'll have a ton of work waiting\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "So much for my vacation...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd better watch my tone, though.\x01",
            "I don't want to make Mirano angry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C06")

    label("loc_BB7")


    ChrTalk(    #4
        0xFE,
        (
            "Now, then...if I go back to Bose,\x01",
            "I'll have a ton of work waiting\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C06")

    TalkEnd(0xD)
    Return()

    # Function_4_AEE end

    def Function_5_C0A(): pass

    label("Function_5_C0A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    OP_A2(0x2)

    ChrTalk(    #5
        0xFE,
        "I'd better get checked in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'm glad the airships are running\x01",
            "on time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8B")

    label("loc_C6B")


    ChrTalk(    #7
        0xFE,
        "I'd better get checked in.\x02",
    )

    CloseMessageWindow()

    label("loc_C8B")

    TalkEnd(0xF)
    Return()

    # Function_5_C0A end

    def Function_6_C8F(): pass

    label("Function_6_C8F")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBB")
    OP_A2(0x3)

    ChrTalk(    #8
        0x10,
        (
            "All this talk of the mayor doing\x01",
            "those terrible things is quite\x01",
            "unsettling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "Even so, it's a good thing that he\x01",
            "was arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "Someone like that would, no doubt,\x01",
            "only get into more trouble if he\x01",
            "were allowed to run free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "The Bracer Guild is to be commended.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E52")

    label("loc_DBB")


    ChrTalk(    #12
        0x10,
        (
            "It's a good thing that the mayor\x01",
            "was arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "Someone like that would, no doubt,\x01",
            "only get into more trouble if he\x01",
            "were allowed to run free.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E52")

    Jump("loc_1596")

    label("loc_E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_EDC")

    ChrTalk(    #14
        0x10,
        (
            "The Liberl Orbalship Corporation has\x01",
            "its headquarters in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "I've been to the main office once,\x01",
            "for training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_10FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106B")
    OP_A2(0x3)

    ChrTalk(    #16
        0x10,
        (
            "Back when this place was still in the planning\x01",
            "stages, there was a lot of arguing about whether\x01",
            "it should be in the north or south block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "Since the north block has so many shops\x01",
            "and tourist attractions, it initially\x01",
            "seemed to be an obvious choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "On the other hand, the south block has the\x01",
            "main city gates, but a lot of delinquent-\x01",
            "types tend to hang out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FB")

    label("loc_106B")


    ChrTalk(    #19
        0x10,
        (
            "Back when this place was still in the planning\x01",
            "stages, there was a lot of arguing about whether\x01",
            "it should be in the north or south block.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    label("loc_10FB")

    Jump("loc_1596")

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1171")

    ChrTalk(    #20
        0x10,
        (
            "The flight to Bose just left a\x01",
            "moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "I'm sorry, but there are no more\x01",
            "flights out today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_1171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1227")

    ChrTalk(    #22
        0x10,
        (
            "Canceled seats are offered for sale\x01",
            "on a first-come, first-served basis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "When you're in a hurry and you\x01",
            "don't have a reservation, it's\x01",
            "always a good idea to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_1227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1340")

    ChrTalk(    #24
        0x10,
        (
            "If you've got a flight to catch, best\x01",
            "stay on THIS side of the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "A lot of folks miss their flights because\x01",
            "they get stuck when the bridge is up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "At those times, the schedule for the\x01",
            "airship departures is jam-packed, too.\x01",
            "It's somewhat problematic...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #27
        0x10,
        "Another nice day today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "But hey, good weather or bad,\x01",
            "I'm ready for anything the day\x01",
            "throws at me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_13B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(    #29
        0x10,
        (
            "We've seen more and more \x01",
            "tourists coming to Ruan over\x01",
            "the last few years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "Since there's basically nothing except\x01",
            "tourist traps, the crowd gets pretty\x01",
            "huge whenever people have the day off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156D")
    OP_A2(0x3)

    ChrTalk(    #31
        0x10,
        (
            "Any time the airships are \x01",
            "grounded, I get absolutely\x01",
            "flooded with inquiries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "Of course, even when everything's\x01",
            "running perfectly smoothly, I'm\x01",
            "still busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "Oh, well. At least it's not boring!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1596")

    label("loc_156D")


    ChrTalk(    #34
        0x10,
        "Oh, well. At least it's not boring!\x02",
    )

    CloseMessageWindow()

    label("loc_1596")

    TalkEnd(0x10)
    Return()

    # Function_6_C8F end

    def Function_7_159A(): pass

    label("Function_7_159A")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B3")
    OP_A2(0x4)

    ChrTalk(    #35
        0xFE,
        (
            "I've been invited to Zeiss as a\x01",
            "guest engineer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "But in the end, I turned down\x01",
            "the invitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "It was very flattering to me as an\x01",
            "engineer, but I'm Todd's brother\x01",
            "first and foremost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I have my own reasons for not\x01",
            "wanting to leave Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171D")

    label("loc_16B3")


    ChrTalk(    #39
        0xFE,
        (
            "I've been invited to Zeiss as a\x01",
            "guest engineer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "But in the end, I turned down\x01",
            "the invitation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    Jump("loc_1BA8")

    label("loc_1720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1794")

    ChrTalk(    #41
        0xFE,
        (
            "I received a communique from the\x01",
            "main office about the R&D work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "It was good news, but still...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_1794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_17BE")

    ChrTalk(    #43
        0xFE,
        "Okay, take five, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_17BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_17D1")

    ChrTalk(    #44
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_17D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_18A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185E")
    OP_A2(0x4)

    ChrTalk(    #45
        0xFE,
        (
            "We need to swap out the parts in\x01",
            "this crazy gizmo, piece by piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I should contact the head office\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A6")

    label("loc_185E")


    ChrTalk(    #47
        0xFE,
        (
            "We need to swap out the parts in\x01",
            "this crazy gizmo, piece by piece.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A6")

    Jump("loc_1BA8")

    label("loc_18A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_19ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198F")
    OP_A2(0x4)

    ChrTalk(    #48
        0xFE,
        "Got that? I'll explain it again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Applying orbal energy to the rotor\x01",
            "blade converts the linear kinetic energy\x01",
            "and causes the blade to rotate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "That's the basis for any standard\x01",
            "orbal engine.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_19EA")

    label("loc_198F")


    ChrTalk(    #51
        0xFE,
        "Todd's the only family I've got.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I just want to help him, in whatever\x01",
            "way I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EA")

    Jump("loc_1BA8")

    label("loc_19ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_1A67")

    ChrTalk(    #53
        0xFE,
        "Oh...looks like the bridge is up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Us Ruanians can pretty much tell\x01",
            "the time by the bridge's schedule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA8")

    label("loc_1A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7D")
    OP_A2(0x4)

    ChrTalk(    #55
        0xFE,
        (
            "It's not a problem yet, but just\x01",
            "to be safe, I need you to swap\x01",
            "out plugs four and seven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Make sure you check the orbal\x01",
            "pressure in the process.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        "Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Todd, you go down to the ware-\x01",
            "house and get the fresh plugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        "Y-Yes, sir!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jump("loc_1BA8")

    label("loc_1B7D")


    ChrTalk(    #60
        0xFE,
        "Sorry, but I'm in the middle of work.\x02",
    )

    CloseMessageWindow()

    label("loc_1BA8")

    TalkEnd(0x11)
    Return()

    # Function_7_159A end

    def Function_8_1BAC(): pass

    label("Function_8_1BAC")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C2A")

    ChrTalk(    #61
        0xFE,
        (
            "We care about each other, so we\x01",
            "try to take care of each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "It's not always easy, that's for sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1CC4")

    ChrTalk(    #63
        0xFE,
        (
            "Ugh...I hate it when it's all gloomy\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Clive's pretty good at designing\x01",
            "stuff, but when it comes to the\x01",
            "fixing part, well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_1D71")

    ChrTalk(    #65
        0xFE,
        (
            "We may not have a maintenance\x01",
            "chief, but that doesn't mean we\x01",
            "can just leave it to die on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "We'll have to check things over\x01",
            "more carefully than usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_1D9F")

    ChrTalk(    #67
        0xFE,
        "Phew...a nice, normal takeoff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(    #68
        0xFE,
        (
            "Thought that last guy who came in\x01",
            "was just another applicant, sent\x01",
            "here on Clive's recommendation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "...but when I went to check on him, I got\x01",
            "the distinct feeling it was something a\x01",
            "bit more important than a simple meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(    #70
        0xFE,
        (
            "There's someone from the head\x01",
            "office in Clive's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I can only guess what it's about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Oh, well. Like that's anything new.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_1F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9C")
    OP_A2(0x5)

    ChrTalk(    #73
        0xFE,
        "Now...let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Until the airship shows up, I should\x01",
            "check over the equipment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC4")

    label("loc_1F9C")


    ChrTalk(    #75
        0xFE,
        "I should check over the equipment.\x02",
    )

    CloseMessageWindow()

    label("loc_1FC4")

    Jump("loc_2210")

    label("loc_1FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_21CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2129")
    OP_A2(0x5)

    ChrTalk(    #76
        0xFE,
        (
            "Clive is such a great engineer\x01",
            "that scouts have been coming\x01",
            "all the way from Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "He's gotten several notices of\x01",
            "personnel change from the\x01",
            "higher-ups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "He'll probably keep working here\x01",
            "his whole life, just to stay close\x01",
            "to family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It's just the kind of person he is...\x01",
            "though it does seem like a bit of\x01",
            "a waste.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CA")

    label("loc_2129")


    ChrTalk(    #80
        0xFE,
        (
            "Clive's gotten several notices of\x01",
            "personnel change from the\x01",
            "higher-ups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "He'll probably keep working here\x01",
            "his whole life, just to stay close\x01",
            "to family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CA")

    Jump("loc_2210")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2210")

    ChrTalk(    #82
        0xFE,
        (
            "I'm in the middle of performing\x01",
            "maintenance right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2210")

    TalkEnd(0x12)
    Return()

    # Function_8_1BAC end

    def Function_9_2214(): pass

    label("Function_9_2214")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_227B")

    ChrTalk(    #83
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "If not for me, my brother'd probably\x01",
            "be researching new kinds of engines...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233C")
    OP_A2(0x6)

    ChrTalk(    #85
        0xFE,
        "He hasn't said anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "...but I heard about it from Edwin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Clive wants to develop a new Zeissian\x01",
            "Orbal Engine model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I think that's pretty awesome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_233C")


    ChrTalk(    #89
        0xFE,
        "Clive's a really amazing guy.\x02",
    )

    CloseMessageWindow()

    label("loc_235F")

    Jump("loc_2719")

    label("loc_2362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_23AC")

    ChrTalk(    #90
        0xFE,
        (
            "My brother isn't here. He's off on\x01",
            "some big business trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_23AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(    #91
        0xFE,
        "He went off to Zeiss.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_23D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2446")

    ChrTalk(    #92
        0xFE,
        "Maybe it's just me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "...but Clive's being super-energetic\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "I wonder what's going on?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_2446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2520")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EE")
    OP_A2(0x6)

    ChrTalk(    #95
        0xFE,
        "Clive sure is amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Heh heh...I'm glad I get to watch my\x01",
            "brother and learn from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I hope I can be an engineer too,\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251D")

    label("loc_24EE")


    ChrTalk(    #98
        0xFE,
        (
            "I hope I can be an engineer too,\x01",
            "someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251D")

    Jump("loc_2719")

    label("loc_2520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_25ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25CB")
    OP_A2(0x6)

    ChrTalk(    #99
        0xFE,
        "Clive's been teaching me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Thanks to him, I'm a lot more\x01",
            "confident in my work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "Heh heh...he's almost more like\x01",
            "a father than a brother.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25EA")

    label("loc_25CB")


    ChrTalk(    #102
        0xFE,
        "Clive's been teaching me.\x02",
    )

    CloseMessageWindow()

    label("loc_25EA")

    Jump("loc_2719")

    label("loc_25ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_END)), "loc_26F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2691")
    OP_A2(0x6)

    ChrTalk(    #103
        0xFE,
        (
            "If they see you've got talent,\x01",
            "the Zeiss central lab will let\x01",
            "you work there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I dream of getting good enough\x01",
            "to work there, someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26EE")

    label("loc_2691")


    ChrTalk(    #105
        0xFE,
        (
            "I dream of getting good enough\x01",
            "at engineering to work at the\x01",
            "Zeiss central lab someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EE")

    Jump("loc_2719")

    label("loc_26F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2719")

    ChrTalk(    #106
        0xFE,
        "I-I'm a mechanic trainee...\x02",
    )

    CloseMessageWindow()

    label("loc_2719")

    TalkEnd(0x13)
    Return()

    # Function_9_2214 end

    def Function_10_271D(): pass

    label("Function_10_271D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(132240, 8150, 95810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_4A(0x9, 255)
    OP_22(0x75, 0x0, 0x64)
    SetChrPos(0x8, 133220, 8150, 96310, 270)
    SetChrPos(0x101, 131000, 8150, 96980, 90)
    SetChrPos(0x102, 130960, 8150, 95770, 90)
    SetChrPos(0x105, 129930, 8150, 96550, 90)
    SetChrPos(0x9, 131860, 8150, 98100, 135)
    SetChrPos(0xA, 133250, 9200, 93100, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #107
        0x8,
        (
            "#178F#3PI pressed Mayor Dalmore for\x01",
            "information once he regained\x01",
            "consciousness, but...\x02\x03",

            "He apparently can't remember anything\x01",
            "regarding the past few hours very well,\x01",
            "if he remembers them at all.\x02\x03",

            "He's also drawing a complete blank\x01",
            "about the arson and robbery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#505F#2PR-Really...?\x02\x03",

            "Kinda like the leader of the\x01",
            "sky bandits...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#013F#4PMaybe it's related to those\x01",
            "men in black from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#176F#3PWell, even if he can't remember,\x01",
            "the crimes are pretty clear-cut.\x02\x03",

            "It should go without saying that we'll\x01",
            "be checking out his steward, too.\x02\x03",

            "#171FIf we uncover anything, we'll be\x01",
            "sure to let the Bracer Guild know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        "#010F#4PWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "#147FBy the way, Lieutenant, I have\x01",
            "a favor to ask.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AC7():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AC7)
    Sleep(300)

    def lambda_2ADA():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ADA)

    def lambda_2AE8():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AE8)

    def lambda_2AF6():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AF6)

    ChrTalk(    #113
        0x8,
        "#173F#3PWhat might that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#141FWould it be at all possible for me\x01",
            "to get on board that ship, as well?\x02\x03",

            "It's supposed to be the most\x01",
            "advanced airship ever to come\x01",
            "out of Zeiss.\x02\x03",

            "It'd make for a great story,\x01",
            "and I really need one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#176F#3PI'm afraid not.\x02\x03",

            "#170FThe Arseille was only just completed,\x01",
            "and is still undergoing flight testing.\x02\x03",

            "I must ask that you not comment on\x01",
            "her at all until she's officially\x01",
            "unveiled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "#142FWha... Oh, come on!\x02\x03",

            "You've got to at least give me\x01",
            "something about the mayor and\x01",
            "his steward being arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#171F#3PDon't worry. The facts of the\x01",
            "story will be given over to the\x01",
            "royal news agency.\x02\x03",

            "Until then, please refrain from\x01",
            "reporting any of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "#145F*sigh* ...What choice do I have?\x02\x03",

            "#144FAll right, I can do this!\x01",
            "I can write a story with even\x01",
            "the barest scrap of info!\x02\x03",

            "I've got to hurry back to the\x01",
            "agency and put these events\x01",
            "to paper!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #119
        0x9,
        "#147FIf you'll pardon me, everyone...!\x02",
    )

    CloseMessageWindow()

    def lambda_2EBF():

        label("loc_2EBF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EBF")

    QueueWorkItem2(0x8, 1, lambda_2EBF)

    def lambda_2ED0():

        label("loc_2ED0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2ED0")

    QueueWorkItem2(0x101, 1, lambda_2ED0)

    def lambda_2EE1():

        label("loc_2EE1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EE1")

    QueueWorkItem2(0x102, 1, lambda_2EE1)

    def lambda_2EF2():

        label("loc_2EF2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2EF2")

    QueueWorkItem2(0x105, 1, lambda_2EF2)
    OP_8C(0x9, 90, 400)
    OP_8E(0x9, 0x20EC2, 0x1FD6, 0x184D4, 0x1388, 0x0)
    OP_8E(0x9, 0x20EF4, 0x1FD6, 0x18A74, 0x1388, 0x0)
    OP_8E(0x9, 0x1ED34, 0x1806, 0x18B8C, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)

    ChrTalk(    #120
        0x101,
        (
            "#506FWell, he's in his usual\x01",
            "high spirits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#019F#4PHa ha... Would you expect\x01",
            "any less?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "#178F#3PI'm told that the Liberl News'\x01",
            "circulation has increased\x01",
            "dramatically, of late.\x02\x03",

            "I hope he's not planning to write\x01",
            "a big propaganda piece...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3046():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3046)

    def lambda_3054():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3054)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #123
        0x102,
        "#014FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #124
        0x8,
        "#175F#3PNever mind...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, 126260, 6150, 101260, 90)
    SetChrPos(0xC, 126260, 6150, 101260, 90)

    NpcTalk(    #125
        0xB,
        "Man's Voice",
        (
            "#5PThat was quite impressive,\x01",
            "1st Lieutenant Schwarz.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_318D():
        OP_6D(132920, 8150, 97630, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_318D)

    def lambda_31A5():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_31A5)

    def lambda_31B5():

        label("loc_31B5")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31B5")

    QueueWorkItem2(0x8, 1, lambda_31B5)

    def lambda_31C6():

        label("loc_31C6")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31C6")

    QueueWorkItem2(0x101, 1, lambda_31C6)

    def lambda_31D7():

        label("loc_31D7")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31D7")

    QueueWorkItem2(0x102, 1, lambda_31D7)

    def lambda_31E8():

        label("loc_31E8")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_31E8")

    QueueWorkItem2(0x105, 1, lambda_31E8)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0xC)
    WaitChrThread(0xB, 0x1)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #126
        0x8,
        "#173FColonel...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#004F#1PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#014FColonel Richard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "#113FOh, I remember you...\x02\x03",

            "#110FI presume that you are the new\x01",
            "bracers the guild spoke of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#004F#1PErr...\x02\x03",

            "Oh, so you were the one Jean\x01",
            "got in touch with, Colonel Richard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "#110FYes, I received word at Leiston\x01",
            "Fortress, where the royal forces\x01",
            "are stationed.\x02\x03",

            "I got here as quickly as I could,\x01",
            "only to find that the crisis had\x01",
            "passed.\x02\x03",

            "Excellent work, Lieutenant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        "#176FTh-That's very kind of you, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        (
            "#182FHa ha... Still, I wonder...\x02\x03",

            "What would bring the guards\x01",
            "from the Royal City here?\x01",
            "And so quickly...\x02\x03",

            "Perhaps you know of a route so\x01",
            "secret that even our Intelligence\x01",
            "Division is unaware of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        "#175FS-Surely you jest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        "#047F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "#111FHa ha. Come now, Captain. This is\x01",
            "hardly a time to pick a fight.\x02\x03",

            "#115FI was simply admiring the proactive\x01",
            "stance of the Royal Guardsmen. It's\x01",
            "good to have you on our side.\x02\x03",

            "#110FIf it please you, Lieutenant, we'll take\x01",
            "over the investigation from here, and\x01",
            "move matters to Leiston Fortress.\x02\x03",

            "I believe the mayor will be\x01",
            "well attended to there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        "#178FYes, sir. I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "#111FNow, if you'll excuse us.\x02\x03",

            "Ladies and gentlemen of the Bracer\x01",
            "Guild and Royal Guard...and the\x01",
            "young lady in the uniform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x105,
        "#040F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "#115FFate willing, I think we shall\x01",
            "see each other again.\x02\x03",

            "#110FAnd with that, I bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xC,
        (
            "#182FHeehee.\x01",
            "Safe travels, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_8C(0xB, 135, 400)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(600)
    OP_8C(0xC, 135, 400)
    OP_43(0xC, 0x1, 0x0, 0xD)
    WaitChrThread(0xC, 0x1)

    def lambda_37E7():
        OP_6D(131910, 8150, 96570, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37E7)
    OP_8C(0x101, 225, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #142
        0x101,
        (
            "#505F#3PMaybe I'm just imagining things...\x02\x03",

            "...but did the Colonel look like he\x01",
            "was eyeballing Kloe to anyone else?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3884():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3884)

    def lambda_3892():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3892)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #143
        0x105,
        "#542FOh, w-was he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x102,
        (
            "#015F#2P...\x02\x03",

            "#010FI'm sure it's just because he\x01",
            "doesn't see students very often\x01",
            "in his line of work.\x02\x03",

            "I wouldn't make too much of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x105,
        (
            "#045FOh, ha ha...\x01",
            "Umm... I'll bet you're right.\x02\x03",

            "That's probably it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#007F#3PHmm... That's not the impression\x01",
            "I got at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "#176F...I'm certain that he's just as\x01",
            "surprised as you are.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A15():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A15)
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #148
        0x8,
        (
            "#171FIt's hard to believe that bracers\x01",
            "so young would be so capable.\x02\x03",

            "He might be scouting you out to\x01",
            "become part of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        (
            "#506F#3POh, come on.\x01",
            "Don't flatter us.\x02\x03",

            "We had a lot of help on this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "#170FYou needn't be so modest.\x02\x03",

            "You're not full-fledged bracers\x01",
            "yet, but I presume that you wish\x01",
            "to become so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#008F#3PWell, yes, we're in training for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x102,
        (
            "#010FWe intend to travel all over the country\x01",
            "before the queen's birthday celebration\x01",
            "as part of our preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "#170FI see... You're partaking in self-study,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x14,
        (
            "#1PLieutenant Schwarz! Everything is ready\x01",
            "for the C.O.'s departure.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x14, 400)

    ChrTalk(    #155
        0x8,
        "#170F#3PAcknowledged.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #156
        0x8,
        (
            "#170FEstelle and Joshua...and Kloe too,\x01",
            "of course.\x02\x03",

            "We must be leaving soon. I hope\x01",
            "that our paths will cross again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        "#006FY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x102,
        "#010FWe'll be looking forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x105,
        "#048F...Thank you very much.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_43(0x8, 0x0, 0x0, 0xE)

    def lambda_3E09():
        OP_6C(224000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E09)

    def lambda_3E19():
        OP_6D(132040, 8960, 87760, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E19)

    def lambda_3E31():
        OP_6B(3680, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E31)

    def lambda_3E41():
        OP_67(0, 5440, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_3E41)
    Sleep(1000)

    def lambda_3E5E():
        OP_8E(0xFE, 0x206C0, 0x1FD6, 0x172A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E5E)

    def lambda_3E79():
        OP_8E(0xFE, 0x201D4, 0x1FD6, 0x171F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E79)

    def lambda_3E94():
        OP_8E(0xFE, 0x20454, 0x1FD6, 0x17610, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E94)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 180, 400)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 13)
    Sleep(100)
    OP_99(0x8, 0x0, 0x1, 0x4B0)

    ChrTalk(    #160
        0x8,
        "#177FRegiment, ATTEN-TION!\x02",
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x1F4)
    OP_22(0x98, 0x0, 0x64)

    def lambda_3F1B():

        label("loc_3F1B")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F1B")

    QueueWorkItem2(0x14, 0, lambda_3F1B)

    def lambda_3F2E():

        label("loc_3F2E")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F2E")

    QueueWorkItem2(0x15, 0, lambda_3F2E)

    def lambda_3F41():

        label("loc_3F41")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F41")

    QueueWorkItem2(0x16, 0, lambda_3F41)

    def lambda_3F54():

        label("loc_3F54")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_3F54")

    QueueWorkItem2(0x17, 0, lambda_3F54)
    SetChrChipByIndex(0x18, 11)
    SetChrChipByIndex(0x1C, 11)
    SetChrChipByIndex(0x20, 11)
    Sleep(100)
    SetChrChipByIndex(0x19, 11)
    SetChrChipByIndex(0x1D, 11)
    SetChrChipByIndex(0x21, 11)
    Sleep(100)
    SetChrChipByIndex(0x1A, 11)
    SetChrChipByIndex(0x1E, 11)
    SetChrChipByIndex(0x22, 11)
    Sleep(100)
    SetChrChipByIndex(0x1B, 11)
    SetChrChipByIndex(0x1F, 11)
    SetChrChipByIndex(0x23, 11)
    Sleep(1000)

    ChrTalk(    #161
        0x101,
        "#004FWhoa...\x02",
    )

    CloseMessageWindow()

    def lambda_3FC9():

        label("loc_3FC9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FC9")

    QueueWorkItem2(0x102, 1, lambda_3FC9)

    def lambda_3FDA():

        label("loc_3FDA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FDA")

    QueueWorkItem2(0x105, 1, lambda_3FDA)

    def lambda_3FEB():

        label("loc_3FEB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3FEB")

    QueueWorkItem2(0x101, 1, lambda_3FEB)

    ChrTalk(    #162
        0x8,
        (
            "#172FRoyal Guardsmen Warship, Arseille...\x01",
            "prepare for takeoff!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(3000)
    OP_6D(159890, 6490, 81650, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(388, 0)
    OP_6F(0x7, 100)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x24, 138000, 6550, 81800, 90)
    SetChrPos(0x25, 138000, 1200, 81800, 90)
    OP_A1(0x24, 0x8)
    OP_72(0x8, 0x4)
    OP_72(0x8, 0x20)
    SetChrFlags(0x24, 0x4)
    OP_A1(0x25, 0x9)
    OP_72(0x9, 0x4)
    SetChrFlags(0x25, 0x4)

    def lambda_4128():
        OP_6D(129389, 10000, 81550, 20000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4128)
    Sleep(2000)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0x8, 1)
    OP_70(0x8, 0x96)
    OP_73(0x4)
    OP_6F(0x8, 150)
    OP_70(0x8, 0x14A)
    OP_43(0x24, 0x3, 0x0, 0xF)

    def lambda_4170():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4170)

    def lambda_4180():
        OP_67(0, 7850, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_4180)
    OP_91(0x24, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x24, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x24, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x24, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x24, 0x0, 0x190, 0x0, 0x190, 0x0)
    OP_73(0x8)
    OP_71(0x8, 0x20)
    OP_6F(0x8, 330)
    OP_70(0x8, 0x1AE)

    def lambda_4212():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4212)

    def lambda_4228():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4228)
    Sleep(200)

    def lambda_4243():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4243)

    def lambda_4259():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4259)
    Sleep(200)

    def lambda_4274():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4274)

    def lambda_428A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_428A)
    Sleep(200)

    def lambda_42A5():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_42A5)

    def lambda_42BB():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_42BB)
    Sleep(200)

    def lambda_42D6():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_42D6)

    def lambda_42EC():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_42EC)
    Sleep(200)

    def lambda_4307():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4307)

    def lambda_431D():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_431D)
    Sleep(200)

    def lambda_4338():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4338)

    def lambda_434E():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_434E)
    Sleep(200)

    def lambda_4369():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4369)

    def lambda_437F():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_437F)
    Sleep(200)

    def lambda_439A():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_439A)

    def lambda_43B0():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_43B0)
    Sleep(200)

    def lambda_43CB():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_43CB)

    def lambda_43E1():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_43E1)
    Sleep(200)

    def lambda_43FC():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_43FC)

    def lambda_4412():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4412)
    Sleep(200)

    def lambda_442D():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_442D)

    def lambda_4443():
        OP_94(0x1, 0xFE, 0x0, 0x30D40, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_4443)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x75, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x75, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x75, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x75, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x75, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x75, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x75, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x75)
    OP_1F(0x64, 0x1F4)
    Fade(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_6D(132060, 8150, 94520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)

    ChrTalk(    #163
        0x101,
        (
            "#506FWow...a salute and fanfare to\x01",
            "go with it.\x02\x03",

            "That's a little overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x102,
        (
            "#019FYeah...and a state-of-the-art ship,\x01",
            "to boot.\x02\x03",

            "But I guess you'd expect as much\x01",
            "from the defenders of Her Majesty,\x01",
            "the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x105,
        "#041FHa ha... True.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #166
        0x101,
        (
            "#501FLieutenant Schwarz sure is cool,\x01",
            "though.\x02\x03",

            "#001FShe kinda reminds me of that\x01",
            "character that Kloe played...\x01",
            "Oscar the Knight. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x105,
        (
            "#040FI think so, too.\x02\x03",

            "#041FHa ha...\x01",
            "What an odd coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        "#311F#3PScreee! ☆\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_10_271D end

    def Function_11_472F(): pass

    label("Function_11_472F")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EAE, 0x1FD6, 0x1856A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x209C2, 0x1FD6, 0x18006, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_11_472F end

    def Function_12_4778(): pass

    label("Function_12_4778")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20D64, 0x1FD6, 0x17FCA, 0xBB8, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_12_4778 end

    def Function_13_47AD(): pass

    label("Function_13_47AD")

    OP_8E(0xFE, 0x20EAE, 0x1FD6, 0x1856A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20EF4, 0x1FD6, 0x18A74, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1ED34, 0x1806, 0x18B8C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_13_47AD end

    def Function_14_47EF(): pass

    label("Function_14_47EF")

    OP_8E(0xFE, 0x20468, 0x1FD6, 0x17250, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2042C, 0x1FD6, 0x14FAA, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x203E6, 0x1F72, 0x14C94, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Return()

    # Function_14_47EF end

    def Function_15_4838(): pass

    label("Function_15_4838")

    OP_6F(0x8, 150)
    OP_70(0x8, 0xFA)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 251)
    OP_70(0x8, 0x109)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 266)
    OP_70(0x8, 0x11F)
    OP_73(0x8)
    OP_22(0xDD, 0x0, 0x64)
    OP_6F(0x8, 288)
    OP_70(0x8, 0x14A)
    Return()

    # Function_15_4838 end

    def Function_16_4889(): pass

    label("Function_16_4889")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #169
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒  To Bose\x01",
            "⇒  To Zeiss\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4889 end

    def Function_17_48F2(): pass

    label("Function_17_48F2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
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

    # Function_17_48F2 end

    def Function_18_4971(): pass

    label("Function_18_4971")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #171
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_4971 end

    SaveToFile()

Try(main)

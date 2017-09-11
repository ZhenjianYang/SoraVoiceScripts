from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'Sister Ellen',                         # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Monster',                              # 15
        'Monster',                              # 16
        'Monster',                              # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Carna',                                # 20
        'Anelace',                              # 21
        'Grant',                                # 22
        'Kurt',                                 # 23
        '1st Lieutenant Schwarz',               # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
        'Royal Avenue',                         # 33
        'Erbe Royal Villa',                     # 34
        'Royal Avenue',                         # 35
        'ダイン・ワニ3',                        # 36
        '沼チュパカブラ2',                      # 37
        'ワニ4',                                # 38
        'ヘルマーズ3',                          # 39
        'プリメーラ3',                          # 40
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT09/CH10780 ._CH',             # 01
        'ED6_DT09/CH10781 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
        'ED6_DT07/CH00171 ._CH',             # 08
        'ED6_DT07/CH01610 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT07/CH00112 ._CH',             # 0B
        'ED6_DT07/CH01240 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT07/CH01260 ._CH',             # 0E
        'ED6_DT07/CH01620 ._CH',             # 0F
        'ED6_DT07/CH02090 ._CH',             # 10
        'ED6_DT07/CH01320 ._CH',             # 11
        'ED6_DT07/CH00172 ._CH',             # 12
        'ED6_DT09/CH10780 ._CH',             # 13
        'ED6_DT09/CH10781 ._CH',             # 14
        'ED6_DT09/CH10790 ._CH',             # 15
        'ED6_DT09/CH10791 ._CH',             # 16
        'ED6_DT09/CH10050 ._CH',             # 17
        'ED6_DT09/CH10051 ._CH',             # 18
        'ED6_DT09/CH10800 ._CH',             # 19
        'ED6_DT09/CH10801 ._CH',             # 1A
        'ED6_DT09/CH10810 ._CH',             # 1B
        'ED6_DT09/CH10811 ._CH',             # 1C
        'ED6_DT09/CH10820 ._CH',             # 1D
        'ED6_DT09/CH10821 ._CH',             # 1E
        'ED6_DT09/CH11220 ._CH',             # 1F
        'ED6_DT09/CH11221 ._CH',             # 20
        'ED6_DT09/CH11230 ._CH',             # 21
        'ED6_DT09/CH11231 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT09/CH10780P._CP',             # 01
        'ED6_DT09/CH10781P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
        'ED6_DT07/CH00171P._CP',             # 08
        'ED6_DT07/CH01610P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT07/CH00112P._CP',             # 0B
        'ED6_DT07/CH01240P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT07/CH01260P._CP',             # 0E
        'ED6_DT07/CH01620P._CP',             # 0F
        'ED6_DT07/CH02090P._CP',             # 10
        'ED6_DT07/CH01320P._CP',             # 11
        'ED6_DT07/CH00172P._CP',             # 12
        'ED6_DT09/CH10780P._CP',             # 13
        'ED6_DT09/CH10781P._CP',             # 14
        'ED6_DT09/CH10790P._CP',             # 15
        'ED6_DT09/CH10791P._CP',             # 16
        'ED6_DT09/CH10050P._CP',             # 17
        'ED6_DT09/CH10051P._CP',             # 18
        'ED6_DT09/CH10800P._CP',             # 19
        'ED6_DT09/CH10801P._CP',             # 1A
        'ED6_DT09/CH10810P._CP',             # 1B
        'ED6_DT09/CH10811P._CP',             # 1C
        'ED6_DT09/CH10820P._CP',             # 1D
        'ED6_DT09/CH10821P._CP',             # 1E
        'ED6_DT09/CH11220P._CP',             # 1F
        'ED6_DT09/CH11221P._CP',             # 20
        'ED6_DT09/CH11230P._CP',             # 21
        'ED6_DT09/CH11231P._CP',             # 22
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62880,
        Z                   = 0,
        Y                   = 55500,
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

    DeclNpc(
        X                   = -25910,
        Z                   = 0,
        Y                   = 25290,
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

    DeclNpc(
        X                   = -107380,
        Z                   = 0,
        Y                   = -10960,
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


    DeclMonster(
        X                   = 54960,
        Z                   = 20,
        Y                   = 1810,
        Unknown_0C          = 0,
        Unknown_0E          = 25,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x264,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39700,
        Z                   = 70,
        Y                   = -19490,
        Unknown_0C          = 0,
        Unknown_0E          = 23,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x263,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18160,
        Z                   = 10,
        Y                   = -7650,
        Unknown_0C          = 0,
        Unknown_0E          = 27,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x265,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32450,
        Z                   = 20,
        Y                   = -19130,
        Unknown_0C          = 0,
        Unknown_0E          = 31,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x267,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30720,
        Z                   = -20,
        Y                   = -16340,
        Unknown_0C          = 0,
        Unknown_0E          = 33,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x268,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 32110,
        Y                   = -1000,
        Z                   = -45500,
        Range               = 35850,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF84AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -88800,
        Y                   = -1000,
        Z                   = -3040,
        Range               = -85900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFB7EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 70260,
        Y                   = -1000,
        Z                   = 32570,
        Range               = 56300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7602,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9670,
        TriggerZ            = 500,
        TriggerY            = -54320,
        TriggerRange        = 1500,
        ActorX              = 9670,
        ActorZ              = 4000,
        ActorY              = -54320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_656",          # 00, 0
        "Function_1_673",          # 01, 1
        "Function_2_686",          # 02, 2
        "Function_3_2D1C",         # 03, 3
        "Function_4_3625",         # 04, 4
        "Function_5_38B5",         # 05, 5
        "Function_6_3A30",         # 06, 6
        "Function_7_3BAC",         # 07, 7
        "Function_8_3C4E",         # 08, 8
    )


    def Function_0_656(): pass

    label("Function_0_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_664")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_672")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_672")

    Return()

    # Function_0_656 end

    def Function_1_673(): pass

    label("Function_1_673")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x30064)
    Return()

    # Function_1_673 end

    def Function_2_686(): pass

    label("Function_2_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1B")
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    SetChrPos(0x9, 12040, 0, -49370, 90)
    SetChrPos(0xA, 12070, 0, -51990, 45)
    SetChrPos(0xB, 14800, 0, -52250, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_6F2():

        label("loc_6F2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6F2")

    QueueWorkItem2(0x9, 1, lambda_6F2)

    def lambda_705():

        label("loc_705")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_705")

    QueueWorkItem2(0xA, 1, lambda_705)

    def lambda_718():

        label("loc_718")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_718")

    QueueWorkItem2(0xB, 1, lambda_718)
    OP_A2(0x616)
    OP_28(0x46, 0x1, 0x20)
    OP_28(0x46, 0x1, 0x40)
    OP_20(0x5DC)

    NpcTalk(    #0
        0x8,
        "Woman's Voice",
        "Noooo!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13F, 0)
    TurnDirection(0x102, 0x13F, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)

    ChrTalk(    #1
        0x101,
        "#005FYou heard that, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#016FIt came from over there!\x01",
            "Let's go!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EB():
        OP_6D(13190, 0, -50600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EB)

    def lambda_803():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_803)

    def lambda_813():
        OP_6C(241000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_813)
    WaitChrThread(0x101, 0x2)
    AddParty(0x3E, 0xFF)
    ClearChrFlags(0x13F, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x13F, 14740, 0, -49400, 225)
    SetChrPos(0x101, 20850, 0, -44670, 0)
    SetChrPos(0x102, 19400, 0, -43210, 0)
    OP_62(0x13F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #3
        0x13F,
        "Nun",
        "AIIIEEEEEEE!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x13F,
        "Nun",
        (
            "Help meeee!\x01",
            "Someone, please help me!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_8C4():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8C4)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_8E3():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8E3)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)

    def lambda_902():
        OP_92(0xFE, 0x13F, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_902)
    Sleep(500)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)

    def lambda_926():
        OP_8E(0xFE, 0x457E, 0x0, 0xFFFF458E, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_926)
    Sleep(300)

    def lambda_946():
        OP_8E(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_946)
    WaitChrThread(0x101, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_96B():
        OP_96(0xFE, 0x3B7E, 0x0, 0xFFFF3B8E, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96B)
    Sleep(200)
    OP_44(0x102, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrFlags(0x101, 0x1000)
    OP_22(0x1F4, 0x0, 0x64)

    def lambda_9A1():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_9B6():
        OP_96(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B6)
    Sleep(200)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 10)

    def lambda_9E3():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E3)
    Sleep(150)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0xB, 1)

    def lambda_A02():

        label("loc_A02")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A02")

    QueueWorkItem2(0xB, 2, lambda_A02)

    def lambda_A15():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A15)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_A3D():
        OP_95(0xFE, 0xFFFFF830, 0x0, 0x0, 0x9C4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A3D)

    def lambda_A5B():

        label("loc_A5B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A5B")

    QueueWorkItem2(0x9, 2, lambda_A5B)
    TurnDirection(0x101, 0xB, 0)
    Sleep(150)
    SetChrChipByIndex(0xA, 1)

    def lambda_A7F():
        OP_95(0xFE, 0xFFFFFD44, 0x0, 0xFFFFFD44, 0x6A4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A7F)

    def lambda_A9D():

        label("loc_A9D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A9D")

    QueueWorkItem2(0xA, 2, lambda_A9D)
    WaitChrThread(0x101, 0x2)
    SetChrChipByIndex(0x101, 3)

    def lambda_ABA():
        OP_8F(0xFE, 0x38AE, 0x0, 0xFFFF3B16, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABA)
    WaitChrThread(0x102, 0x2)
    SetChrChipByIndex(0x102, 5)

    def lambda_ADF():
        OP_8F(0xFE, 0x35D4, 0x0, 0xFFFF3DF0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADF)
    Sleep(150)
    TurnDirection(0x102, 0x9, 0)
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #5
        0x13F,
        "Nun",
        "Eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#006F#1PSister! It'll be all right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#012F#2PStay back!\x01",
            "It's too dangerous!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0x9, 1)

    def lambda_B79():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B79)
    Sleep(50)
    OP_44(0xA, 0xFF)
    SetChrChipByIndex(0xA, 1)

    def lambda_B9D():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B9D)
    Sleep(50)
    OP_44(0xB, 0xFF)
    SetChrChipByIndex(0xB, 1)

    def lambda_BC1():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BC1)
    WaitChrThread(0x9, 0x1)

    def lambda_BDC():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xA28)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BDC)
    Sleep(50)

    def lambda_BFF():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BFF)
    Sleep(50)

    def lambda_C22():
        OP_96(0xFE, 0x3994, 0x0, 0xFFFF3F08, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C22)
    Sleep(500)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C58"),
        (SWITCH_DEFAULT, "loc_C5B"),
    )


    label("loc_C58")

    OP_B4(0x0)
    Return()

    label("loc_C5B")

    OP_31(0x7, 0x0, 0x21)
    OP_B5(0x7, 0x0)
    OP_B5(0x7, 0x1)
    OP_B5(0x7, 0x2)
    OP_B5(0x7, 0x3)
    OP_B5(0x7, 0x4)
    OP_B5(0x7, 0x5)
    OP_41(0x7, 0xD4)
    OP_41(0x7, 0xF5)
    OP_41(0x7, 0x113)
    OP_41(0x7, 0x262, 0x0)
    OP_41(0x7, 0x259, 0x1)
    OP_41(0x7, 0x25F, 0x2)
    OP_41(0x7, 0x274, 0x3)
    OP_35(0x7, 0xDC)
    OP_35(0x7, 0xDD)
    OP_35(0x7, 0xDE)
    OP_35(0x7, 0xDF)
    OP_36(0x7, 0x109)
    OP_36(0x7, 0x10A)
    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 22520, 0, -37100, 0)
    SetChrFlags(0x108, 0x80)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 14390, 0, -50980, 225)
    SetChrPos(0x102, 12920, 0, -49800, 225)
    SetChrPos(0x13F, 14740, 0, -49400, 225)
    OP_6D(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(241000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        (
            "#007FWhew...\x01",
            "That was pretty tough.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x13F, 400)

    ChrTalk(    #9
        0x101,
        "#006FAre you okay, Sister?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)

    def lambda_DCA():
        TurnDirection(0xFE, 0x13F, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCA)

    NpcTalk(    #10
        0x13F,
        "Nun",
        "Y-Yes... Thank you.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x13F,
        "Nun",
        "Umm... Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FWe're with the Bracer Guild.\x02\x03",

            "We heard you scream while\x01",
            "we were looking for someone.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x13F,
        "Nun",
        "I... I see...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x13F,
        "Nun",
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#580FAre you okay?\x01",
            "You don't look okay...\x02\x03",

            "Did you get hurt?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x13F,
        "Nun",
        (
            "No...\x01",
            "Thanks to you, I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x13F,
        "Nun",
        (
            "I'm Sister Ellen. I perform my\x01",
            "duties at Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13F,
        "Thank you so much for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#001FHa ha...\x01",
            "You don't need to thank us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#012FI must ask, though, what is a\x01",
            "clergywoman doing so far from\x01",
            "Grancel without escort?\x02\x03",

            "Did no one accompany you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x13F,
        "No... I came alone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x13F,
        (
            "Actually, we ran out of\x01",
            "medicinal herbs for mixing\x01",
            "at the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13F,
        (
            "The shop was also out of stock,\x01",
            "so I came here to pick some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#007FThat was seriously risky. There\x01",
            "are monsters everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13F,
        (
            "It was not always so... There\x01",
            "used to be none to speak of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13F,
        (
            "It seems their numbers have\x01",
            "greatly increased in recent days.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x5DC)
    OP_8C(0x13F, 45, 600)

    ChrTalk(    #27
        0x13F,
        "Ah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_1D(0x56)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    Sleep(500)

    def lambda_120A():
        OP_8E(0xFE, 0x3CD2, 0x0, 0xFFFF3EB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_120A)
    Sleep(100)

    def lambda_122A():
        OP_8E(0xFE, 0x37C8, 0x0, 0xFFFF4282, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_122A)

    def lambda_1245():
        OP_8F(0xFE, 0x3782, 0x0, 0xFFFF3C24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13F, 3, lambda_1245)
    SetChrPos(0x9, 19840, 0, -40400, 0)
    SetChrPos(0xA, 21100, 0, -41220, 0)
    SetChrPos(0xB, 21440, 0, -39410, 0)
    SetChrPos(0xC, 21420, 0, -38390, 0)
    SetChrPos(0xD, 23130, 0, -39910, 0)
    SetChrPos(0xE, 21460, 0, -36780, 0)
    SetChrPos(0xF, 23510, 0, -37150, 0)
    SetChrPos(0x10, 24560, 0, -39000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_1310():
        OP_8E(0xFE, 0x3BB0, 0x0, 0xFFFF4E44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1310)

    def lambda_132B():
        OP_8E(0xFE, 0x43DA, 0x0, 0xFFFF4BA6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_132B)

    def lambda_1346():
        OP_8E(0xFE, 0x40E2, 0x0, 0xFFFF5060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1346)

    def lambda_1361():
        OP_8E(0xFE, 0x3FAC, 0x0, 0xFFFF56B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1361)

    def lambda_137C():
        OP_8E(0xFE, 0x4A1A, 0x0, 0xFFFF5132, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_137C)

    def lambda_1397():
        OP_8E(0xFE, 0x433A, 0x0, 0xFFFF5A74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1397)

    def lambda_13B2():
        OP_8E(0xFE, 0x4AF6, 0x0, 0xFFFF5ACE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13B2)

    def lambda_13CD():
        OP_8E(0xFE, 0x4A74, 0x0, 0xFFFF55F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_13CD)

    def lambda_13E8():

        label("loc_13E8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13E8")

    QueueWorkItem2(0x9, 2, lambda_13E8)

    def lambda_13FB():

        label("loc_13FB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0xA, 2, lambda_13FB)
    Sleep(100)

    def lambda_1413():

        label("loc_1413")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1413")

    QueueWorkItem2(0xB, 2, lambda_1413)

    def lambda_1426():

        label("loc_1426")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1426")

    QueueWorkItem2(0xC, 2, lambda_1426)
    Sleep(100)

    def lambda_143E():

        label("loc_143E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_143E")

    QueueWorkItem2(0xD, 2, lambda_143E)

    def lambda_1451():

        label("loc_1451")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1451")

    QueueWorkItem2(0xE, 2, lambda_1451)
    Sleep(100)

    def lambda_1469():

        label("loc_1469")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1469")

    QueueWorkItem2(0xF, 2, lambda_1469)

    def lambda_147C():

        label("loc_147C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_147C")

    QueueWorkItem2(0x10, 2, lambda_147C)

    def lambda_148F():
        OP_6D(19250, 0, -43570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_148F)

    def lambda_14A7():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14A7)
    Sleep(1500)

    def lambda_14BC():
        OP_6D(17110, 0, -45970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BC)
    Sleep(3000)

    ChrTalk(    #28
        0x101,
        (
            "#005FWh-What the heck are\x01",
            "these things...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#012FThey must have been attracted\x01",
            "by the noise...\x02\x03",

            "Dealing with this many\x01",
            "might be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#002FYeah, we need to at least\x01",
            "get the sister to safety.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0x108,
        "Man's Voice",
        "#3PYo! Need a hand?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    SetChrPos(0x108, 23450, 0, -37300, 225)

    def lambda_15E7():
        OP_6D(17970, 0, -45090, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15E7)
    SetChrChipByIndex(0x108, 8)
    SetChrFlags(0x108, 0x1000)

    def lambda_1609():
        OP_8E(0xFE, 0x528A, 0x0, 0xFFFF61B8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1609)
    WaitChrThread(0x108, 0x1)
    Sleep(60)
    SetChrFlags(0x108, 0x20)
    SetChrChipByIndex(0x108, 18)
    SetChrFlags(0x108, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_1642():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1642)
    OP_8E(0x108, 0x4CD6, 0x0, 0xFFFF5C36, 0x2134, 0x0)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 19660, 1000, -41900, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_16A5():
        OP_8F(0xFE, 0x43DA, 0x0, 0xFFFF542A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_16A5)

    def lambda_16C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_16C0)
    Sleep(500)
    OP_96(0x108, 0x4F9C, 0x0, 0xFFFF5EDE, 0x1F4, 0x1388)

    def lambda_16EE():
        OP_99(0xFE, 0x4, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_16EE)

    def lambda_16FE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_16FE)

    def lambda_170C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_170C)

    def lambda_171A():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_171A)

    def lambda_1728():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1728)

    def lambda_1736():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1736)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #32
        0x101,
        "#501F#5PZin?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#010F#5PThank Aidios you're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x108,
        (
            "#070FHeh heh... I was wondering who\x01",
            "it was, and here it turns out\x01",
            "to be you guys!\x02\x03",

            "But why don't we save the\x01",
            "chit-chat until we've dealt\x01",
            "with the guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#006F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#010F#5PRoger that!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)
    SetChrChipByIndex(0x108, 7)

    def lambda_185E():
        OP_8E(0xFE, 0x416E, 0x0, 0xFFFF4868, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_185E)

    def lambda_1879():
        OP_92(0xFE, 0xB, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1879)

    def lambda_188E():
        OP_8E(0xFE, 0x492A, 0x0, 0xFFFF5952, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 3, lambda_188E)
    Sleep(400)
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    RemoveParty(0x3E, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_18C4"),
        (SWITCH_DEFAULT, "loc_18C7"),
    )


    label("loc_18C4")

    OP_B4(0x0)
    Return()

    label("loc_18C7")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, 16770, 0, -47500, 45)
    SetChrPos(0x102, 15050, 0, -45990, 45)
    SetChrPos(0x108, 17690, 0, -44440, 225)
    SetChrPos(0x8, 14650, 0, -48360, 45)
    OP_6D(15920, 0, -45970, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x108, 0x1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #37
        0x108,
        (
            "#074FMan, oh, man... Worked up\x01",
            "quite a sweat on that one!\x02\x03",

            "#070FBut honestly, I wasn't expecting\x01",
            "to see you guys here.\x02\x03",

            "Didn't you have business\x01",
            "in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#506FOh, we handled that ages ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#010F#3PActually, we transferred from\x01",
            "the Zeiss branch to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x108,
        (
            "#070FAhh, I see.\x02\x03",

            "Which would mean that you managed\x01",
            "to solve that kidnapping case.\x01",
            "Well done!\x02\x03",

            "#071FHow's the redhead who got\x01",
            "poisoned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#006FOh, he's fine now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x108,
        "#073FOh, pardon my rudeness...\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x108,
        "#072F...Whoa.\x02",
    )

    CloseMessageWindow()

    def lambda_1C0B():

        label("loc_1C0B")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1C0B")

    QueueWorkItem2(0x101, 1, lambda_1C0B)

    def lambda_1C1C():

        label("loc_1C1C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1C1C")

    QueueWorkItem2(0x108, 1, lambda_1C1C)
    OP_8F(0x108, 0x3D72, 0x0, 0xFFFF4DAE, 0xBB8, 0x0)
    OP_44(0x101, 0x1)

    ChrTalk(    #45
        0x108,
        (
            "#070F(Hey... Who's the pretty lady?)\x02\x03",

            "(She with you? ...She single?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #46
        0x102,
        (
            "#014F(Uh, what? I-I don't know.\x01",
            "We only just met her...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #47
        0x101,
        (
            "#007FYour MOUTHS are open, guys...\x02\x03",

            "#507FDo you want me to tell\x01",
            "Kilika about this?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #48
        0x108,
        (
            "#073FI'm...uh...just making an objective\x01",
            "observation...\x02\x03",

            "#072F...And what does Kilika have to do with\x01",
            "this, anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3AE8, 0x0, 0xFFFF455C, 0x7D0, 0x0)

    ChrTalk(    #49
        0x8,
        (
            "Umm... I truly appreciate you \x01",
            "all coming to my assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "You've saved my life.\x02",
    )

    CloseMessageWindow()

    def lambda_1E43():

        label("loc_1E43")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1E43")

    QueueWorkItem2(0x108, 1, lambda_1E43)

    def lambda_1E54():

        label("loc_1E54")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1E54")

    QueueWorkItem2(0x102, 1, lambda_1E54)
    OP_8F(0x108, 0x3DC2, 0x0, 0xFFFF491C, 0xBB8, 0x0)

    ChrTalk(    #51
        0x108,
        (
            "#071F#4PNo, no!\x01",
            "Please, think nothing of it!\x02\x03",

            "Just doing what comes naturally\x01",
            "for a chivalrous man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "Oh, my...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 600)
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4B88, 0xFA0, 0x0)
    OP_8E(0x101, 0x3C8C, 0x0, 0xFFFF4ED0, 0xFA0, 0x0)
    TurnDirection(0x101, 0x108, 600)

    ChrTalk(    #53
        0x101,
        (
            "#506F(Oh, PLEASE...)\x02\x03",

            "(He's a total sucker for \x01",
            "a pretty face, isn't he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#019F(Ha ha... So it appears.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 27890, 0, -33290, 0)
    SetChrPos(0x12, 26890, 0, -32290, 0)

    NpcTalk(    #55
        0x11,
        "Man's Voice",
        (
            "#3PYou there!\x01",
            "What are you doing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_2002():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2002)

    def lambda_2010():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2010)

    def lambda_201E():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_201E)

    def lambda_202C():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_202C)

    def lambda_203A():
        OP_8E(0xFE, 0x4434, 0x0, 0xFFFF55EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_203A)
    Sleep(200)

    def lambda_205A():
        OP_8E(0xFE, 0x48DA, 0x0, 0xFFFF540C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_205A)
    OP_6D(17010, 0, -44670, 3000)

    def lambda_2086():

        label("loc_2086")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2086")

    QueueWorkItem2(0x108, 2, lambda_2086)

    def lambda_2097():

        label("loc_2097")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_2097")

    QueueWorkItem2(0x101, 2, lambda_2097)

    def lambda_20A8():

        label("loc_20A8")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_20A8")

    QueueWorkItem2(0x102, 2, lambda_20A8)

    def lambda_20B9():

        label("loc_20B9")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_20B9")

    QueueWorkItem2(0x8, 2, lambda_20B9)

    ChrTalk(    #56
        0x101,
        "#580FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #58
        0x11,
        (
            "You're four people in an otherwise-deserted area,\x01",
            "discussing what appears to be a confidential topic.\x01",
            "HIGHLY suspicious behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x12,
        "#4PI think you're terrorists.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    ChrTalk(    #60
        0x101,
        (
            "#005FWha... Who are you calling a\x01",
            "terrorist?! If anyone's acting\x01",
            "suspicious here...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x3F2A, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    def lambda_221B():
        OP_8E(0xFE, 0x42FE, 0x0, 0xFFFF49D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_221B)
    OP_8F(0x102, 0x4182, 0x0, 0xFFFF4BF6, 0x7D0, 0x0)

    ChrTalk(    #61
        0x102,
        (
            "#019FWe're with the Bracer Guild,\x01",
            "Grancel branch.\x02\x03",

            "We came to the aid of the\x01",
            "sister here, who was under\x01",
            "attack by some monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        "What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x12,
        "#4PBracers?!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3A84, 0x0, 0xFFFF4B60, 0x7D0, 0x0)

    ChrTalk(    #64
        0x8,
        (
            "Umm... This gentleman speaks\x01",
            "the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "I came here to gather herbs,\x01",
            "when those creatures attacked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x108,
        (
            "#070F#3PAnd on a related note,\x01",
            "I'm also a bracer.\x02\x03",

            "I'll be facing your buddies\x01",
            "in the ring later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "Calvardian martial arts... Ah, you're\x01",
            "that guy in the Martial Arts\x01",
            "Competition that fights solo, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x12,
        (
            "#4PHmph... You've definitely got\x01",
            "the muscles of a prize fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "I'll leave you be,\x01",
            "just this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "But the Erbe Royal Villa is close\x01",
            "by. Wanderers and sightseers\x01",
            "are NOT welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        "#4PAlso, Sister...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        (
            "#4PI think we should escort you\x01",
            "back to Grancel NOW.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x12,
        (
            "#4PYou've already been enough trouble\x01",
            "as it is, from what I can see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Oh...but I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        (
            "#005FOh, for the love of...\x02\x03",

            "You've been nothing but\x01",
            "obnoxious from the moment\x01",
            "you started talki--\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #76
        0x102,
        "#013FEstelle. Shush.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)

    ChrTalk(    #77
        0x102,
        (
            "#010FWe'll take care to avoid the Royal\x01",
            "Villa, sirs. You have our apologies\x01",
            "for any inconvenience we've caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x11,
        (
            "In the future, however, I would advise\x01",
            "you to know your place. Mouthing off\x01",
            "to the wrong people can be...hazardous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        "#4PCome on, Sister. Let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        "A-All right...\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x4042, 0x0, 0xFFFF525E, 0xBB8, 0x0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #82
        0x8,
        (
            "#2PThank you again for\x01",
            "your help...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 51, 400)

    def lambda_27F0():
        OP_6C(20000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27F0)

    def lambda_2800():
        OP_6D(18100, 0, -44370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2800)

    def lambda_2818():
        OP_8F(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2818)
    OP_8C(0x12, 51, 400)

    def lambda_283A():
        OP_8F(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_283A)
    Sleep(200)

    def lambda_285A():
        OP_8E(0xFE, 0x6CF2, 0x0, 0xFFFF7DF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_285A)
    Sleep(4000)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(16870, 0, -45560, 1000)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #83
        0x101,
        "#582F#4PWha... Who... How...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #84
        0x101,
        (
            "#005F#4PWho the HELL do they\x01",
            "think they are?!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #85
        0x108,
        (
            "#070FThey're Special Ops soldiers,\x01",
            "affiliated with the Royal Army's\x01",
            "Intelligence Division.\x02\x03",

            "Skillful, to be sure, but\x01",
            "their strongest suit is\x01",
            "their sneakiness.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29CA():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29CA)
    Sleep(200)

    def lambda_29DD():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29DD)
    Sleep(400)

    ChrTalk(    #86
        0x101,
        (
            "#009F#4PTheir ONLY suit,\x01",
            "if you ask me!\x02\x03",

            "#505FErr...\x02\x03",

            "Wait a second. How do\x01",
            "you know them, Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x108,
        (
            "#070FI ran into their team at the\x01",
            "Martial Arts Competition.\x02\x03",

            "I was introduced to them then.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #88
        0x101,
        (
            "#580F#4P(They're actually fighting...?!)\x02\x03",

            "(What would some spy types be doing\x01",
            "participating in something as public\x01",
            "as a tournament?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        (
            "#012F#6P(I guess they didn't feel it necessary\x01",
            "to conceal their identities...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x108,
        (
            "#074FWell, we should get back to\x01",
            "the city before they decide\x01",
            "that they'd rather fight.\x02\x03",

            "#073F...Oh, right. What brings\x01",
            "you two here, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#506F#4POh, yeah. Duh.\x02\x03",

            "#006FActually, we were looking for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x108,
        "#073FWhy's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010F#6PWe had a favor we needed to ask.\x02\x03",

            "About that Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2D1B")

    Return()

    # Function_2_686 end

    def Function_3_2D1C(): pass

    label("Function_3_2D1C")

    EventBegin(0x0)
    SetChrPos(0x101, 11690, 0, -52560, 225)
    SetChrPos(0x102, 11000, 0, -51680, 225)
    SetChrPos(0x108, 10930, 0, -50240, 196)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x13, 14410, 0, -53900, 257)
    SetChrPos(0x14, 14820, 0, -52280, 244)
    SetChrPos(0x15, 13050, 0, -51640, 207)
    SetChrPos(0x16, 13090, 0, -50260, 213)
    OP_6D(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeToBright(3000, 0)

    def lambda_2DF5():
        OP_6C(249000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DF5)
    OP_6E(309, 5000)

    ChrTalk(    #94
        0x101,
        (
            "#000FSo...are we going to\x01",
            "meet back here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#010FWell, this is the Amberl Monument rest area,\x01",
            "so this should be the place.\x02\x03",

            "The only real issue is whether\x01",
            "or not Lt. Schwarz and her men\x01",
            "can get here undetected.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x17, 17080, 0, -45130, 225)
    SetChrPos(0x18, 17100, 0, -43830, 225)
    SetChrPos(0x19, 18380, 0, -45010, 225)
    SetChrPos(0x1A, 17740, 0, -42700, 225)
    SetChrPos(0x1B, 18600, 0, -43670, 225)
    SetChrPos(0x1C, 19480, 0, -44620, 225)
    SetChrPos(0x1D, 18580, 0, -41840, 225)
    SetChrPos(0x1E, 19520, 0, -42690, 225)
    SetChrPos(0x1F, 20400, 0, -43690, 225)

    ChrTalk(    #96
        0x17,
        (
            "Ha ha... No need to worry\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FDA():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FDA)

    def lambda_2FE8():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FE8)

    def lambda_2FF6():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2FF6)

    def lambda_3004():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3004)

    def lambda_3012():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3012)

    def lambda_3020():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3020)

    def lambda_302E():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_302E)

    def lambda_303C():
        OP_6C(335000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_303C)

    def lambda_304C():
        OP_6D(14730, 0, -48030, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_304C)

    def lambda_3064():
        OP_6E(332, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3064)
    Sleep(2000)

    def lambda_3079():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3079)
    Sleep(100)

    def lambda_3099():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3099)

    def lambda_30B4():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_30B4)
    Sleep(100)

    def lambda_30D4():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_30D4)

    def lambda_30EF():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_30EF)

    def lambda_310A():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_310A)
    Sleep(100)

    def lambda_312A():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_312A)

    def lambda_3145():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3145)

    def lambda_3160():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3160)
    OP_6D(13880, 0, -49890, 4000)

    ChrTalk(    #97
        0x101,
        (
            "#000FWhoa!\x01",
            "When did you get here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x108,
        (
            "#070FHa ha... Nice work staying\x01",
            "hidden in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x17,
        (
            "#170FWe have quite a few sympathizers\x01",
            "among the citizens.\x02\x03",

            "We've finished our preparations.\x01",
            "We can begin whenever you're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x16,
        "All right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(    #101
        0x16,
        (
            "We're waiting on your\x01",
            "order, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_32B4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32B4)

    def lambda_32C2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_32C2)

    def lambda_32D0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_32D0)

    def lambda_32DE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32DE)

    def lambda_32EC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_32EC)

    def lambda_32FA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_32FA)

    ChrTalk(    #102
        0x101,
        (
            "#000FHuh...?\x02\x03",

            "MY order?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x16,
        (
            "You were the ones who originally\x01",
            "received Her Majesty's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x15,
        (
            "So, we're waiting on your\x01",
            "command before we begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#000FB-But...I... I'm just a rookie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x13,
        (
            "Ha ha... That really doesn't\x01",
            "matter. I don't think you'll\x01",
            "have a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x14,
        "Just do it without shouting, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x17,
        (
            "#170FWe'll be there to help.\x01",
            "We have no objections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#000FI...uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#010FHave a little faith in yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#070FDon't worry about the trivial details.\x02\x03",

            "Just deal with things as\x01",
            "they come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#000FRight...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_352D():

        label("loc_352D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_352D")

    QueueWorkItem2(0x102, 1, lambda_352D)

    def lambda_353E():

        label("loc_353E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_353E")

    QueueWorkItem2(0x108, 1, lambda_353E)

    def lambda_354F():

        label("loc_354F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_354F")

    QueueWorkItem2(0x13, 1, lambda_354F)

    def lambda_3560():

        label("loc_3560")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3560")

    QueueWorkItem2(0x14, 1, lambda_3560)

    def lambda_3571():

        label("loc_3571")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3571")

    QueueWorkItem2(0x15, 1, lambda_3571)

    def lambda_3582():

        label("loc_3582")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3582")

    QueueWorkItem2(0x16, 1, lambda_3582)

    def lambda_3593():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3593)
    OP_8E(0x101, 0x2972, 0x1E0, 0xFFFF2F40, 0x258, 0x0)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #113
        0x101,
        (
            "#000FOkay, then, here goes...\x02\x03",

            "Everyone...let's get those\x01",
            "hostages rescued!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2D1C end

    def Function_4_3625(): pass

    label("Function_4_3625")

    EventBegin(0x0)
    OP_6D(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x18, -25890, 0, -4510, 180)
    SetChrPos(0x19, -27370, 0, -4510, 180)
    SetChrPos(0x1A, -27240, 0, -2700, 180)
    SetChrPos(0x1B, -25950, 0, -2920, 180)
    SetChrPos(0x101, -26570, 0, -6220, 0)
    SetChrPos(0x102, -28030, 0, -6250, 45)
    SetChrPos(0x108, -25360, 0, -6190, 313)

    ChrTalk(    #114
        0x108,
        "#070FThe ambush party's on the move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x18,
        (
            "We'll go ahead and lure \x01",
            "the remaining forces into\x01",
            "the front gardens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x18,
        (
            "You can break into the villa\x01",
            "while they're distracted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#000FSounds good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        "#010FAidios be with all of you!\x02",
    )

    CloseMessageWindow()

    def lambda_37E2():

        label("loc_37E2")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_37E2")

    QueueWorkItem2(0x101, 1, lambda_37E2)

    def lambda_37F3():

        label("loc_37F3")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_37F3")

    QueueWorkItem2(0x102, 1, lambda_37F3)

    def lambda_3804():

        label("loc_3804")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_3804")

    QueueWorkItem2(0x108, 1, lambda_3804)

    def lambda_3815():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3815)
    Sleep(100)

    def lambda_3835():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3835)
    Sleep(200)

    def lambda_3855():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3855)
    Sleep(100)

    def lambda_3875():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3875)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_A2(0x651)
    EventEnd(0x0)
    Return()

    # Function_4_3625 end

    def Function_5_38B5(): pass

    label("Function_5_38B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A2F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392D")

    ChrTalk(    #119
        0x101,
        (
            "#002FWe can't miss our chance\x01",
            "to get in.\x02\x03",

            "We have to get to the Erbe\x01",
            "Royal Villa NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A14")

    label("loc_392D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399F")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #120
        0x102,
        (
            "#012FWe're not going to get\x01",
            "another chance at this.\x02\x03",

            "Let's go to the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A14")

    label("loc_399F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A14")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(    #121
        0x108,
        (
            "#072FWe've only got one chance\x01",
            "to do this.\x02\x03",

            "...Come on. Let's hurry to\x01",
            "the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A14")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3A2F")

    Return()

    # Function_5_38B5 end

    def Function_6_3A30(): pass

    label("Function_6_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BAB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AA8")

    ChrTalk(    #122
        0x101,
        (
            "#002FWe can't miss our chance\x01",
            "to get in.\x02\x03",

            "We have to get to the Erbe\x01",
            "Royal Villa NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B90")

    label("loc_3AA8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1B")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #123
        0x102,
        (
            "#012FWe're not going to get\x01",
            "another chance for this.\x02\x03",

            "Let's go to the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B90")

    label("loc_3B1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B90")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(    #124
        0x108,
        (
            "#072FWe've only got one chance\x01",
            "to do this.\x02\x03",

            "...Come on. Let's hurry to\x01",
            "the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B90")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3BAB")

    Return()

    # Function_6_3A30 end

    def Function_7_3BAC(): pass

    label("Function_7_3BAC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #125
        (
            "\x07\x05North:   Erbe Royal Villa\x01",
            "West:    Sanktheim Gate          224 selge\x01",
            "East:    Gurune Gate             256 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_3BAC end

    def Function_8_3C4E(): pass

    label("Function_8_3C4E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #126
        (
            "\x07\x05An ancient monument stands here.\x01",
            "An engraved plate at its base reads,\x01",
            "'Amberl Monument.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_3C4E end

    SaveToFile()

Try(main)

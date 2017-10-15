from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1300   ._SN',
        MapName             = 'Bose',
        Location            = 'R1300.x',
        MapIndex            = 57,
        MapDefaultBGM       = "ed60022",
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
        'East Bose Highway',                    # 9
        'Haken Gate',                           # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10370 ._CH',             # 00
        'ED6_DT09/CH10371 ._CH',             # 01
        'ED6_DT09/CH10360 ._CH',             # 02
        'ED6_DT09/CH10361 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10370P._CP',             # 00
        'ED6_DT09/CH10371P._CP',             # 01
        'ED6_DT09/CH10360P._CP',             # 02
        'ED6_DT09/CH10361P._CP',             # 03
    )

    DeclNpc(
        X                   = -207930,
        Z                   = -20,
        Y                   = -167750,
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
        X                   = -204120,
        Z                   = -200,
        Y                   = 1430,
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
        X                   = -203250,
        Z                   = 10,
        Y                   = -130620,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -218580,
        Z                   = -40,
        Y                   = -112680,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -226560,
        Z                   = -30,
        Y                   = -88140,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -200780,
        Z                   = -20,
        Y                   = -50350,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -188950,
        Z                   = -20,
        Y                   = -42080,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -194620,
        Z                   = -30,
        Y                   = -34740,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x105,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -222450,
        TriggerZ            = -80,
        TriggerY            = -128449,
        TriggerRange        = 1000,
        ActorX              = -222890,
        ActorZ              = -10,
        ActorY              = -128990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -185450,
        TriggerZ            = -120,
        TriggerY            = -39580,
        TriggerRange        = 1000,
        ActorX              = -184980,
        ActorZ              = 40,
        ActorY              = -39110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FA",          # 00, 0
        "Function_1_1FB",          # 01, 1
        "Function_2_266",          # 02, 2
        "Function_3_267",          # 03, 3
    )


    def Function_0_1FA(): pass

    label("Function_0_1FA")

    Return()

    # Function_0_1FA end

    def Function_1_1FB(): pass

    label("Function_1_1FB")

    OP_16(0x2, 0xFA0, 0xFFFADF80, 0xFFFCCBB0, 0x230013)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    OP_6F(0x2, 0)
    Jump("loc_226")

    label("loc_21F")

    OP_6F(0x2, 60)

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238")
    OP_6F(0x3, 0)
    Jump("loc_23F")

    label("loc_238")

    OP_6F(0x3, 60)

    label("loc_23F")

    OP_64(0x0, 0x1)
    OP_71(0x2, 0x0)
    OP_71(0x2, 0x4)
    OP_64(0x1, 0x1)
    OP_71(0x3, 0x0)
    OP_71(0x3, 0x4)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Return()

    # Function_1_1FB end

    def Function_2_266(): pass

    label("Function_2_266")

    Return()

    # Function_2_266 end

    def Function_3_267(): pass

    label("Function_3_267")

    Return()

    # Function_3_267 end

    SaveToFile()

Try(main)

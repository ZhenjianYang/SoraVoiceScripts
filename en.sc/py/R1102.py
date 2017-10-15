from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1102   ._SN',
        MapName             = 'Bose',
        Location            = 'R1102.x',
        MapIndex            = 55,
        MapDefaultBGM       = "ed60029",
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
        'Verte Bridge - Checkpoint',            # 9
        'Bose',                                 # 10
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
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10310 ._CH',             # 02
        'ED6_DT09/CH10311 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
        'ED6_DT09/CH10350 ._CH',             # 08
        'ED6_DT09/CH10351 ._CH',             # 09
        'ED6_DT09/CH10540 ._CH',             # 0A
        'ED6_DT09/CH10541 ._CH',             # 0B
        'ED6_DT09/CH10550 ._CH',             # 0C
        'ED6_DT09/CH10551 ._CH',             # 0D
        'ED6_DT09/CH10870 ._CH',             # 0E
        'ED6_DT09/CH10871 ._CH',             # 0F
        'ED6_DT09/CH10900 ._CH',             # 10
        'ED6_DT09/CH10901 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10310P._CP',             # 02
        'ED6_DT09/CH10311P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
        'ED6_DT09/CH10350P._CP',             # 08
        'ED6_DT09/CH10351P._CP',             # 09
        'ED6_DT09/CH10540P._CP',             # 0A
        'ED6_DT09/CH10541P._CP',             # 0B
        'ED6_DT09/CH10550P._CP',             # 0C
        'ED6_DT09/CH10551P._CP',             # 0D
        'ED6_DT09/CH10870P._CP',             # 0E
        'ED6_DT09/CH10871P._CP',             # 0F
        'ED6_DT09/CH10900P._CP',             # 10
        'ED6_DT09/CH10901P._CP',             # 11
    )

    DeclNpc(
        X                   = -105840,
        Z                   = 0,
        Y                   = -23910,
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
        X                   = -226090,
        Z                   = 0,
        Y                   = -15420,
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
        X                   = -105060,
        Z                   = 140,
        Y                   = -56470,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -112490,
        Z                   = 20,
        Y                   = -60920,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -150760,
        Z                   = 550,
        Y                   = -35150,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -183300,
        Z                   = 90,
        Y                   = -41900,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -168950,
        Z                   = -20,
        Y                   = -29930,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -177370,
        Z                   = 0,
        Y                   = -16920,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xDD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -166760,
        TriggerZ            = 130,
        TriggerY            = -21010,
        TriggerRange        = 1000,
        ActorX              = -166150,
        ActorZ              = 220,
        ActorY              = -20910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -184260,
        TriggerZ            = 1040,
        TriggerY            = -55990,
        TriggerRange        = 1000,
        ActorX              = -184720,
        ActorZ              = 1040,
        ActorY              = -56460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_26B",          # 01, 1
        "Function_2_29A",          # 02, 2
        "Function_3_29B",          # 03, 3
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Return()

    # Function_0_26A end

    def Function_1_26B(): pass

    label("Function_1_26B")

    OP_16(0x2, 0xFA0, 0xFFFB9718, 0xFFFD8730, 0x230017)
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    OP_64(0x1, 0x1)
    OP_71(0x1, 0x0)
    OP_71(0x1, 0x4)
    Return()

    # Function_1_26B end

    def Function_2_29A(): pass

    label("Function_2_29A")

    Return()

    # Function_2_29A end

    def Function_3_29B(): pass

    label("Function_3_29B")

    Return()

    # Function_3_29B end

    SaveToFile()

Try(main)

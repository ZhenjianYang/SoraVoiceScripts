from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5319   ._SN',
        MapName             = 'Other',
        Location            = 'C5319.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60065",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
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
        'ED6_DT29/CH12420 ._CH',             # 00
        'ED6_DT29/CH12421 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH12420P._CP',             # 00
        'ED6_DT29/CH12421P._CP',             # 01
    )

    DeclMonster(
        X                   = 49990,
        Z                   = 100,
        Y                   = -30,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x531,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 89710,
        Z                   = 100,
        Y                   = -330,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x531,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 130530,
        Z                   = 100,
        Y                   = -80,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x531,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_10F",          # 01, 1
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Return()

    # Function_0_10E end

    def Function_1_10F(): pass

    label("Function_1_10F")

    SetMapFlags(0x2000000)
    Return()

    # Function_1_10F end

    SaveToFile()

Try(main)

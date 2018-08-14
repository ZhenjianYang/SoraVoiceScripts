from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4153   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4153.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '',                                     # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT29/CH14450 ._CH',             # 00
        'ED6_DT29/CH14451 ._CH',             # 01
        'ED6_DT29/CH14730 ._CH',             # 02
        'ED6_DT29/CH14730 ._CH',             # 03
        'ED6_DT29/CH14790 ._CH',             # 04
        'ED6_DT29/CH14791 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14450P._CP',             # 00
        'ED6_DT29/CH14451P._CP',             # 01
        'ED6_DT29/CH14730P._CP',             # 02
        'ED6_DT29/CH14730P._CP',             # 03
        'ED6_DT29/CH14790P._CP',             # 04
        'ED6_DT29/CH14791P._CP',             # 05
    )

    DeclMonster(
        X                   = 4500,
        Z                   = 0,
        Y                   = 40200,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4240,
        Z                   = 0,
        Y                   = 49590,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22550,
        Z                   = 0,
        Y                   = 49960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12800,
        Z                   = 0,
        Y                   = 63090,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xD8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_14B",          # 01, 1
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Return()

    # Function_0_14A end

    def Function_1_14B(): pass

    label("Function_1_14B")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x23005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A")
    SetMapFlags(0x2000000)

    label("loc_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178")
    OP_10(0x4, 0x0)
    Jump("loc_17E")

    label("loc_178")

    OP_71(0x429, 0x0)
    ExitThread()

    label("loc_17E")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_14B end

    SaveToFile()

Try(main)

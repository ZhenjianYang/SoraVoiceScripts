from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7307   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7307.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        '',                                     # 13
        '',                                     # 14
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
        'ED6_DT29/CH14440 ._CH',             # 00
        'ED6_DT29/CH14440 ._CH',             # 01
        'ED6_DT29/CH14340 ._CH',             # 02
        'ED6_DT29/CH14340 ._CH',             # 03
        'ED6_DT29/CH14140 ._CH',             # 04
        'ED6_DT29/CH14140 ._CH',             # 05
        'ED6_DT29/CH14150 ._CH',             # 06
        'ED6_DT29/CH14150 ._CH',             # 07
        'ED6_DT29/CH14090 ._CH',             # 08
        'ED6_DT29/CH14090 ._CH',             # 09
        'ED6_DT29/CH14120 ._CH',             # 0A
        'ED6_DT29/CH14120 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14440P._CP',             # 00
        'ED6_DT29/CH14440P._CP',             # 01
        'ED6_DT29/CH14340P._CP',             # 02
        'ED6_DT29/CH14340P._CP',             # 03
        'ED6_DT29/CH14140P._CP',             # 04
        'ED6_DT29/CH14140P._CP',             # 05
        'ED6_DT29/CH14150P._CP',             # 06
        'ED6_DT29/CH14150P._CP',             # 07
        'ED6_DT29/CH14090P._CP',             # 08
        'ED6_DT29/CH14090P._CP',             # 09
        'ED6_DT29/CH14120P._CP',             # 0A
        'ED6_DT29/CH14120P._CP',             # 0B
    )

    DeclMonster(
        X                   = -4340,
        Z                   = 10880,
        Y                   = 32140,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8029,
        Z                   = 20200,
        Y                   = 66070,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29850,
        Z                   = 30330,
        Y                   = 65129,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37120,
        Z                   = 39040,
        Y                   = 28620,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 71180,
        Z                   = 43470,
        Y                   = 30500,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69340,
        Z                   = 49400,
        Y                   = 57210,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_1B2",          # 00, 0
        "Function_1_1B3",          # 01, 1
    )


    def Function_0_1B2(): pass

    label("Function_0_1B2")

    Return()

    # Function_0_1B2 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    OP_16(0x2, 0xFA0, 0xFFFE7960, 0xFFFEA840, 0x23009A)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_1B3 end

    SaveToFile()

Try(main)

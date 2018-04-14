from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2102   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2102.x',
        MapIndex            = 98,
        MapDefaultBGM       = "ed60033",
        Flags               = 1,
        EntryFunctionIndex  = 10,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2102   ._SN',
            'ED6_DT21/C2102_1 ._SN',
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
        '目标用照相机',                         # 9
        '左面的覆盖柱子区域判定用',             # 10
        '右面的覆盖柱子区域判定用',             # 11
        '中央的台座判定',                       # 12
        '',                                     # 13
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
        'ED6_DT09/CH10160 ._CH',             # 00
        'ED6_DT09/CH10161 ._CH',             # 01
        'ED6_DT09/CH10450 ._CH',             # 02
        'ED6_DT09/CH10451 ._CH',             # 03
        'ED6_DT09/CH10220 ._CH',             # 04
        'ED6_DT09/CH10221 ._CH',             # 05
        'ED6_DT09/CH10470 ._CH',             # 06
        'ED6_DT09/CH10471 ._CH',             # 07
        'ED6_DT09/CH10480 ._CH',             # 08
        'ED6_DT09/CH10481 ._CH',             # 09
        'ED6_DT09/CH11060 ._CH',             # 0A
        'ED6_DT09/CH11061 ._CH',             # 0B
        'ED6_DT09/CH10460 ._CH',             # 0C
        'ED6_DT09/CH10461 ._CH',             # 0D
        'ED6_DT27/CH03520 ._CH',             # 0E
        'ED6_DT26/CH20279 ._CH',             # 0F
        'ED6_DT06/CH20064 ._CH',             # 10
        'ED6_DT27/CH03523 ._CH',             # 11
        'ED6_DT06/CH20021 ._CH',             # 12
        'ED6_DT29/CH12140 ._CH',             # 13
        'ED6_DT29/CH12141 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT09/CH10160P._CP',             # 00
        'ED6_DT09/CH10161P._CP',             # 01
        'ED6_DT09/CH10450P._CP',             # 02
        'ED6_DT09/CH10451P._CP',             # 03
        'ED6_DT09/CH10220P._CP',             # 04
        'ED6_DT09/CH10221P._CP',             # 05
        'ED6_DT09/CH10470P._CP',             # 06
        'ED6_DT09/CH10471P._CP',             # 07
        'ED6_DT09/CH10480P._CP',             # 08
        'ED6_DT09/CH10481P._CP',             # 09
        'ED6_DT09/CH11060P._CP',             # 0A
        'ED6_DT09/CH11061P._CP',             # 0B
        'ED6_DT09/CH10460P._CP',             # 0C
        'ED6_DT09/CH10461P._CP',             # 0D
        'ED6_DT27/CH03520P._CP',             # 0E
        'ED6_DT26/CH20279P._CP',             # 0F
        'ED6_DT06/CH20064P._CP',             # 10
        'ED6_DT27/CH03523P._CP',             # 11
        'ED6_DT06/CH20021P._CP',             # 12
        'ED6_DT29/CH12140P._CP',             # 13
        'ED6_DT29/CH12141P._CP',             # 14
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
        X                   = -3200,
        Z                   = 250,
        Y                   = 8710,
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
        X                   = 3200,
        Z                   = 250,
        Y                   = 8710,
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
        X                   = 0,
        Z                   = 950,
        Y                   = 13850,
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


    DeclMonster(
        X                   = -9050,
        Z                   = 250,
        Y                   = 12430,
        Unknown_0C          = 180,
        Unknown_0E          = 19,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BD,
        Unknown_18          = 8451,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_24D",          # 01, 1
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x420, 3)), scpexpr(EXPR_END)), "loc_1FA")
    SetChrFlags(0xC, 0x80)

    label("loc_1FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C")
    OP_B5(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22F")
    SetMapFlags(0x10000000)
    Event(1, 1)
    Jump("loc_24C")

    label("loc_22F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_24C")

    Return()

    # Function_0_1EE end

    def Function_1_24D(): pass

    label("Function_1_24D")

    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)

    label("loc_26A")

    OP_22(0x1C3, 0x1, 0x64)
    Return()

    # Function_1_24D end

    SaveToFile()

Try(main)

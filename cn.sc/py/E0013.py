from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0013   ._SN',
        MapName             = 'event',
        Location            = 'E0013.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/E0013_1 ._SN',
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
        '安莉尔',                               # 9
        '小猫',                                 # 10
        '小猫',                                 # 11
        '小猫',                                 # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
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
        'ED6_DT07/CH01700 ._CH',             # 00
        'ED6_DT27/CH03880 ._CH',             # 01
        'ED6_DT27/CH03005 ._CH',             # 02
        'ED6_DT27/CH03881 ._CH',             # 03
        'ED6_DT27/CH03882 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01700P._CP',             # 00
        'ED6_DT27/CH03880P._CP',             # 01
        'ED6_DT27/CH03005P._CP',             # 02
        'ED6_DT27/CH03881P._CP',             # 03
        'ED6_DT27/CH03882P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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


    DeclEvent(
        X                   = 31660,
        Y                   = -1000,
        Z                   = 7810,
        Range               = 28340,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x2206,
        Unknown_18          = 0x10000,
        Unknown_1C          = 9,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_229",          # 02, 2
        "Function_3_23F",          # 03, 3
    )


    def Function_0_172(): pass

    label("Function_0_172")

    OP_51(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227")
    Event(1, 0)

    label("loc_227")

    Return()

    # Function_0_172 end

    def Function_1_228(): pass

    label("Function_1_228")

    Return()

    # Function_1_228 end

    def Function_2_229(): pass

    label("Function_2_229")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_229")

    label("loc_23E")

    Return()

    # Function_2_229 end

    def Function_3_23F(): pass

    label("Function_3_23F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_262")
    OP_8D(0xFE, 29250, 9730, 30560, 8740, 1000)
    Jump("Function_3_23F")

    label("loc_262")

    Return()

    # Function_3_23F end

    SaveToFile()

Try(main)

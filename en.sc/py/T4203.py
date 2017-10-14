from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4203   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Grancel - North Block',                # 11
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
        'ED6_DT07/CH01300 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02470P._CP',             # 02
        'ED6_DT07/CH01330P._CP',             # 03
        'ED6_DT07/CH00401P._CP',             # 04
        'ED6_DT07/CH00421P._CP',             # 05
        'ED6_DT07/CH00391P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT07/CH02090P._CP',             # 08
        'ED6_DT07/CH00321P._CP',             # 09
        'ED6_DT07/CH02000P._CP',             # 0A
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_13B",          # 01, 1
        "Function_2_14E",          # 02, 2
        "Function_3_155",          # 03, 3
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Return()

    # Function_0_13A end

    def Function_1_13B(): pass

    label("Function_1_13B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    Return()

    # Function_1_13B end

    def Function_2_14E(): pass

    label("Function_2_14E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_2_14E end

    def Function_3_155(): pass

    label("Function_3_155")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_3_155 end

    SaveToFile()

Try(main)
